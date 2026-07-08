#!/usr/bin/env python3
"""Enrich BO page frontmatter with GGM fields from parsed XMI data.

Reads the parsed XMI JSON and updates Wiki/Bedrijfsobjecten/ pages with:
- ggm_guid, ggm_uml_type, ggm_toelichting, ggm_synoniemen, ggm_herkomst
- ggm_gemma_naam, ggm_gemma_guid, ggm_gemma_definitie, ggm_gemma_toelichting,
  ggm_gemma_synoniemen, ggm_gemma_type, ggm_gemma_url, ggm_gemma_bron,
  ggm_gemma_alternate_name
- Updated ggm_diagram with actual diagram names from XMI

Rewrites only the fields it explicitly owns (ggm_*/ggm_gemma_*/bo_definitie/
bo_relaties); every other frontmatter field (bo_toelichting, bo_subtypes,
bo_synoniemen, bo_homoniemen, ggm_duplicaat_entiteiten, analyse_ggm_dekking,
...) is passed through byte-for-byte, in its original relative order and body
content unchanged. Stap 3 van de /generate-ggm skill.
"""

import json
import sys
import re
import yaml
from pathlib import Path


def load_xmi_data(json_path: str) -> dict:
    with open(json_path) as f:
        return json.load(f)


def build_entity_lookup(data: dict) -> tuple[dict, set]:
    """Build a name → entity lookup, and flag ambiguous (homoniem) names.

    Multiple GGM-entiteiten can share the same name in different
    beleidsdomeinen (bijv. "Inschrijving" in Onderwijs vs. Inkoop). A plain
    name → entity dict silently keeps whichever entity is encountered last,
    which can point a BO at the wrong domain's entity. ambiguous_names lets
    callers refuse to guess in that case.
    """
    lookup = {}
    seen_guids_per_name: dict[str, set] = {}
    for eid, entity in data['entities'].items():
        name = entity['name']
        lookup[name] = entity
        seen_guids_per_name.setdefault(name, set()).add(eid)
    ambiguous_names = {name for name, guids in seen_guids_per_name.items()
                       if len(guids) > 1}
    return lookup, ambiguous_names


def split_top_level_blocks(fm_raw: str) -> dict[str, str]:
    """Split raw frontmatter text into {key: raw_text_block} per top-level key.

    Preserves the exact original text (including all indented sub-lines) for
    every key, without interpreting its structure. Used to pass through any
    field this script doesn't explicitly rewrite, byte-for-byte.
    """
    blocks: dict[str, list[str]] = {}
    current_key = None
    for line in fm_raw.split('\n'):
        m = re.match(r'^(\w[\w_]*)\s*:', line)
        if m and not line.startswith((' ', '\t')):
            current_key = m.group(1)
            blocks[current_key] = [line]
        elif current_key is not None:
            blocks[current_key].append(line)
    return {k: '\n'.join(v) for k, v in blocks.items()}


def parse_frontmatter(content: str) -> tuple[dict, dict, str, str]:
    """Parse YAML frontmatter.

    Returns (fields, raw_blocks, frontmatter_raw, body).
    - fields: correctly-typed dict via yaml.safe_load — used for GGM-matching
      logic (naam, ggm_entiteit, grondslag, bo_relaties).
    - raw_blocks: {key: raw_text} per top-level key, exact original text —
      used to passthrough any field this script doesn't explicitly rewrite,
      without needing to understand its internal (possibly nested) structure.
      Previously, any multi-line block field other than bo_relaties/relaties
      (bo_subtypes, bo_synoniemen, bo_homoniemen, ggm_duplicaat_entiteiten,
      bo_toelichting, ...) was silently dropped at parse time. raw_blocks
      fixes that generically, for any current or future field.
    """
    if not content.startswith('---'):
        return {}, {}, '', content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, {}, '', content

    fm_raw = parts[1]
    body = parts[2]

    try:
        fields = yaml.safe_load(fm_raw) or {}
    except yaml.YAMLError:
        fields = {}
    if 'relaties' in fields and 'bo_relaties' not in fields:
        fields['bo_relaties'] = fields.pop('relaties')

    raw_blocks = split_top_level_blocks(fm_raw)

    return fields, raw_blocks, fm_raw, body


# Keys this script explicitly understands and rewrites — everything else in
# raw_blocks is passed through verbatim by build_new_frontmatter().
EXPLICIT_CORE_KEYS = {
    'type', 'naam', 'domein', 'archimate_type', 'grondslag',
    'ggm_entiteit', 'ggm_guid', 'ggm_uml_type', 'ggm_beleidsdomein', 'ggm_taakveld',
    'ggm_diagram', 'ggm_diagram_ids', 'ggm_definitie', 'ggm_toelichting',
    'ggm_synoniemen', 'ggm_herkomst', 'ggm_gemma_naam', 'ggm_gemma_guid',
    'ggm_gemma_definitie', 'ggm_gemma_toelichting', 'ggm_gemma_synoniemen',
    'ggm_gemma_type', 'ggm_gemma_url', 'ggm_gemma_bron', 'ggm_gemma_alternate_name',
    'bo_definitie',
}


def build_new_frontmatter(fields: dict, raw_blocks: dict, entity: dict | None,
                          data: dict) -> str:
    """Build new YAML frontmatter string with enriched fields.

    Fields this script owns (EXPLICIT_CORE_KEYS, plus bo_relaties) are
    rewritten from `fields`. Every other top-level key found in `raw_blocks`
    (bo_toelichting, bo_subtypes, bo_synoniemen, bo_homoniemen,
    ggm_duplicaat_entiteiten, analyse_ggm_dekking, bedrijfsprocessen,
    bedrijfsfuncties, status, ...) is passed through byte-for-byte, in its
    original relative order — this script never needs to understand or
    maintain a list of every field shape that exists elsewhere in the wiki.
    """
    lines = []

    def add_field(key, value):
        if isinstance(value, list) and key != 'bo_relaties':
            if value:
                lines.append(f'{key}: [{", ".join(str(v) for v in value)}]')
            else:
                lines.append(f'{key}: []')
        elif isinstance(value, str):
            if '\n' in value or '"' in value:
                lines.append(f"{key}: '{value}'")
            elif value == '' or value is None:
                lines.append(f'{key}: ""')
            else:
                needs_quote = any(c in value for c in ':{}[]&*?|->!%@`#,')
                if needs_quote or value.startswith('"'):
                    lines.append(f'{key}: "{value}"')
                else:
                    lines.append(f'{key}: {value}')
        else:
            lines.append(f'{key}: {value}')

    def add_quoted_field(key, value):
        if value:
            escaped = value.replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"')
        else:
            lines.append(f'{key}: ""')

    # Core fields (preserve order)
    add_field('type', fields.get('type', 'bedrijfsobject'))
    add_field('naam', fields.get('naam', ''))

    if 'domein' in fields:
        add_field('domein', fields['domein'])

    add_field('archimate_type', fields.get('archimate_type', 'business-object'))
    add_field('grondslag', fields.get('grondslag', ''))

    # GGM entity fields
    ggm_entiteit = fields.get('ggm_entiteit', '')
    add_quoted_field('ggm_entiteit', ggm_entiteit)

    if entity:
        add_field('ggm_guid', entity['id'])
        add_field('ggm_uml_type', entity.get('uml_type', ''))

        beleidsdomein = entity.get('beleidsdomein', '')
        taakveld = entity.get('taakveld', '')
        add_quoted_field('ggm_beleidsdomein', beleidsdomein)
        add_quoted_field('ggm_taakveld', taakveld)

        diagram_names = entity.get('diagram_names', [])
        diagram_ids = entity.get('diagram_ids', [])
        if diagram_names:
            add_field('ggm_diagram', diagram_names)
            add_field('ggm_diagram_ids', diagram_ids)
        else:
            beleidsdomein_id = entity.get('beleidsdomein_id', '')
            add_field('ggm_diagram', [])
            add_field('ggm_diagram_ids', [beleidsdomein_id] if beleidsdomein_id else [])

        add_quoted_field('ggm_definitie', entity.get('documentation', ''))

        toelichting = entity.get('tags', {}).get('Toelichting', '')
        synoniemen = entity.get('tags', {}).get('Synoniemen', '')
        herkomst = entity.get('tags', {}).get('Herkomst', '')
        add_quoted_field('ggm_toelichting', toelichting)
        add_quoted_field('ggm_synoniemen', synoniemen)
        add_quoted_field('ggm_herkomst', herkomst)

        # GEMMA values as found in GGM XMI
        gt = entity.get('gemma_tags', {})
        add_quoted_field('ggm_gemma_naam', gt.get('gemma_naam', ''))
        add_field('ggm_gemma_guid', gt.get('gemma_guid', ''))
        add_quoted_field('ggm_gemma_definitie', gt.get('gemma_definitie', ''))
        add_quoted_field('ggm_gemma_toelichting', gt.get('gemma_toelichting', ''))
        add_quoted_field('ggm_gemma_synoniemen', gt.get('gemma_synoniemen', ''))
        add_field('ggm_gemma_type', gt.get('gemma_type', ''))
        add_quoted_field('ggm_gemma_url', gt.get('gemma_url', ''))
        add_quoted_field('ggm_gemma_bron', gt.get('gemma_bron', ''))
        add_quoted_field('ggm_gemma_alternate_name', gt.get('gemma_alternate_name', ''))
    else:
        # No GGM match - preserve existing fields, add empty new ones
        add_quoted_field('ggm_beleidsdomein', fields.get('ggm_beleidsdomein', ''))
        add_field('ggm_guid', '')
        add_field('ggm_uml_type', '')
        add_quoted_field('ggm_taakveld', '')
        existing_diag = fields.get('ggm_diagram', [])
        if isinstance(existing_diag, str):
            existing_diag = [existing_diag] if existing_diag else []
        add_field('ggm_diagram', existing_diag)
        add_field('ggm_diagram_ids', [])
        add_quoted_field('ggm_definitie', fields.get('ggm_definitie', ''))
        add_quoted_field('ggm_toelichting', '')
        add_quoted_field('ggm_synoniemen', '')
        add_quoted_field('ggm_herkomst', '')
        add_quoted_field('ggm_gemma_naam', '')
        add_field('ggm_gemma_guid', '')
        add_quoted_field('ggm_gemma_definitie', '')
        add_quoted_field('ggm_gemma_toelichting', '')
        add_quoted_field('ggm_gemma_synoniemen', '')
        add_field('ggm_gemma_type', '')
        add_quoted_field('ggm_gemma_url', '')
        add_quoted_field('ggm_gemma_bron', '')
        add_quoted_field('ggm_gemma_alternate_name', '')

    # BO definition (wiki's own)
    bo_def = fields.get('bo_definitie', fields.get('gemma_definitie', ''))
    add_quoted_field('bo_definitie', bo_def)

    # Every other field, in original order: explicit bo_relaties rebuild
    # where it occurs, verbatim passthrough for everything else.
    for key in raw_blocks:
        if key in EXPLICIT_CORE_KEYS:
            continue
        if key in ('bo_relaties', 'relaties'):
            if fields.get('bo_relaties'):
                lines.append('bo_relaties:')
                for rel in fields['bo_relaties']:
                    lines.append(f'  - type: {rel.get("type", "")}')
                    for rkey in ('bedrijfsobject', 'richting', 'kardinaliteit', 'beschrijving'):
                        if rkey in rel:
                            val = rel[rkey]
                            if any(c in str(val) for c in ':{}[]&*?|->!%@`#,'):
                                lines.append(f'    {rkey}: "{val}"')
                            else:
                                lines.append(f'    {rkey}: {val}')
            continue
        lines.append(raw_blocks[key])

    return '\n'.join(lines)


def enrich_file(md_path: Path, entity_lookup: dict, ambiguous_names: set, data: dict,
                dry_run: bool = False) -> str:
    content = md_path.read_text(encoding='utf-8')
    fields, raw_blocks, fm_raw, body = parse_frontmatter(content)

    if not fields:
        return 'skip:no-frontmatter'

    naam = fields.get('naam', '')
    ggm_entiteit = fields.get('ggm_entiteit', '')
    ggm_guid = fields.get('ggm_guid', '') or ''
    grondslag = fields.get('grondslag', '')

    match_name = ggm_entiteit if ggm_entiteit else naam

    # Prefer re-matching by the BO's own existing GUID: multiple GGM-entities
    # can share a name across beleidsdomeinen (homoniem, bijv. "Inschrijving"
    # in Onderwijs vs. Inkoop) — a name-only lookup could silently repoint an
    # already-correct BO at the wrong domain's entity.
    entity = data['entities'].get(ggm_guid) if ggm_guid else None

    if not entity and match_name in ambiguous_names:
        return 'skip:ambiguous-name'

    if not entity:
        entity = entity_lookup.get(match_name)

    if not entity and grondslag == 'ggm-entiteit':
        # Try case-insensitive
        for ename, e in entity_lookup.items():
            if ename.lower() == match_name.lower():
                entity = e
                break

    new_fm = build_new_frontmatter(fields, raw_blocks, entity, data)
    new_content = f'---\n{new_fm}\n---{body}'

    if dry_run:
        return f'match:{entity["name"]}' if entity else 'no-match'

    md_path.write_text(new_content, encoding='utf-8')
    return f'updated:{entity["name"]}' if entity else 'updated:no-ggm'


def main():
    dry_run = '--dry-run' in sys.argv

    base = Path(__file__).resolve().parent.parent
    default_json = base / 'Sources' / 'GGM-repository' / 'ggm_parsed.json'
    json_path = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') \
        else str(default_json)

    data = load_xmi_data(json_path)
    entity_lookup, ambiguous_names = build_entity_lookup(data)
    bo_dir = base / 'Wiki' / 'Bedrijfsobjecten'

    results = {'updated': 0, 'no_match': 0, 'skipped': 0}

    for md in sorted(bo_dir.rglob('*.md')):
        result = enrich_file(md, entity_lookup, ambiguous_names, data, dry_run=dry_run)
        rel_path = md.relative_to(bo_dir)

        if result.startswith('updated:'):
            results['updated'] += 1
            ggm = result.split(':', 1)[1]
            print(f'  ✅ {rel_path} → {ggm}')
        elif result.startswith('match:'):
            results['updated'] += 1
            ggm = result.split(':', 1)[1]
            print(f'  ✅ {rel_path} → {ggm} (dry-run)')
        elif result == 'no-match':
            results['no_match'] += 1
            print(f'  — {rel_path} (no GGM match)')
        else:
            results['skipped'] += 1
            print(f'  ⏭  {rel_path} ({result})')

    mode = 'DRY RUN' if dry_run else 'DONE'
    print(f'\n{mode}: {results["updated"]} updated, '
          f'{results["no_match"]} no match, {results["skipped"]} skipped')


if __name__ == '__main__':
    main()
