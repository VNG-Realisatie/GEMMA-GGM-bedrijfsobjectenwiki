#!/usr/bin/env python3
"""Enrich BO page frontmatter with GGM fields from parsed XMI data.

Reads the parsed XMI JSON and updates Wiki/Bedrijfsobjecten/ pages with:
- ggm_guid, ggm_uml_type, ggm_toelichting, ggm_synoniemen, ggm_herkomst
- ggm_gemma_naam, ggm_gemma_guid, ggm_gemma_definitie, ggm_gemma_toelichting,
  ggm_gemma_synoniemen, ggm_gemma_type, ggm_gemma_url, ggm_gemma_bron,
  ggm_gemma_alternate_name
- Updated ggm_diagram with actual diagram names from XMI

Preserves existing frontmatter field order and body content.
"""

import json
import sys
import re
from pathlib import Path


def load_xmi_data(json_path: str) -> dict:
    with open(json_path) as f:
        return json.load(f)


def build_entity_lookup(data: dict) -> dict:
    lookup = {}
    for eid, entity in data['entities'].items():
        lookup[entity['name']] = entity
    return lookup


def parse_frontmatter(content: str) -> tuple[dict, str, str]:
    """Parse YAML frontmatter manually to preserve formatting.

    Returns (fields_dict, frontmatter_raw, body).
    """
    if not content.startswith('---'):
        return {}, '', content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, '', content

    fm_raw = parts[1]
    body = parts[2]

    # Simple YAML parse for flat fields + relaties block
    fields = {}
    current_key = None
    current_list = None

    for line in fm_raw.split('\n'):
        if not line.strip():
            continue

        # Top-level key
        match = re.match(r'^(\w[\w_]*)\s*:\s*(.*)', line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            current_key = key

            if key == 'relaties':
                current_list = []
                fields[key] = current_list
            elif value.startswith('[') and value.endswith(']'):
                items = [v.strip().strip('"').strip("'")
                         for v in value[1:-1].split(',') if v.strip()]
                fields[key] = items
            elif value.startswith('"') and value.endswith('"'):
                fields[key] = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                fields[key] = value[1:-1]
            else:
                fields[key] = value
        elif line.startswith('  - type:') and current_key == 'relaties':
            current_list.append({'type': line.split(':', 1)[1].strip()})
        elif line.startswith('    ') and current_list and current_list:
            m = re.match(r'\s+(\w+)\s*:\s*(.*)', line)
            if m and current_list:
                current_list[-1][m.group(1)] = m.group(2).strip().strip('"')

    return fields, fm_raw, body


def build_new_frontmatter(fields: dict, entity: dict | None, data: dict) -> str:
    """Build new YAML frontmatter string with enriched fields."""
    lines = []

    def add_field(key, value):
        if isinstance(value, list) and key != 'relaties':
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

    # GEMMA definition (wiki's own)
    gemma_def = fields.get('gemma_definitie', '')
    add_quoted_field('gemma_definitie', gemma_def)

    # Remaining fields
    for key in ('definitie', 'gerelateerde_begrippen', 'bedrijfsprocessen',
                'bedrijfsfuncties', 'status'):
        if key in fields:
            add_field(key, fields[key])

    # Relaties block
    if 'relaties' in fields and fields['relaties']:
        lines.append('relaties:')
        for rel in fields['relaties']:
            lines.append(f'  - type: {rel.get("type", "")}')
            for rkey in ('bedrijfsobject', 'richting', 'kardinaliteit', 'beschrijving'):
                if rkey in rel:
                    val = rel[rkey]
                    if any(c in str(val) for c in ':{}[]&*?|->!%@`#,'):
                        lines.append(f'    {rkey}: "{val}"')
                    else:
                        lines.append(f'    {rkey}: {val}')

    return '\n'.join(lines)


def enrich_file(md_path: Path, entity_lookup: dict, data: dict,
                dry_run: bool = False) -> str:
    content = md_path.read_text(encoding='utf-8')
    fields, fm_raw, body = parse_frontmatter(content)

    if not fields:
        return 'skip:no-frontmatter'

    naam = fields.get('naam', '')
    ggm_entiteit = fields.get('ggm_entiteit', '')
    grondslag = fields.get('grondslag', '')

    match_name = ggm_entiteit if ggm_entiteit else naam
    entity = entity_lookup.get(match_name)

    if not entity and grondslag == 'ggm-entiteit':
        # Try case-insensitive
        for ename, e in entity_lookup.items():
            if ename.lower() == match_name.lower():
                entity = e
                break

    new_fm = build_new_frontmatter(fields, entity, data)
    new_content = f'---\n{new_fm}\n---{body}'

    if dry_run:
        return f'match:{entity["name"]}' if entity else 'no-match'

    md_path.write_text(new_content, encoding='utf-8')
    return f'updated:{entity["name"]}' if entity else 'updated:no-ggm'


def main():
    dry_run = '--dry-run' in sys.argv

    base = Path(__file__).resolve().parent.parent
    json_path = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') \
        else '/tmp/ggm_parsed.json'

    data = load_xmi_data(json_path)
    entity_lookup = build_entity_lookup(data)
    bo_dir = base / 'Wiki' / 'Bedrijfsobjecten'

    results = {'updated': 0, 'no_match': 0, 'skipped': 0}

    for md in sorted(bo_dir.rglob('*.md')):
        if md.name == 'map.md':
            continue

        result = enrich_file(md, entity_lookup, data, dry_run=dry_run)
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
