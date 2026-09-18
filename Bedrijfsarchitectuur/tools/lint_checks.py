#!/usr/bin/env python3
"""Deterministic lint checks for the GEMMA Bedrijfsobjecten wiki.

Read-only. Covers the checklist bullets from `.claude/commands/lint.md` that
have an objectively countable/greppable answer (field present/absent, section
present/absent, count, dead link, schema shape). Bullets that require semantic
judgment (contradicties, verouderde claims, "is dit echt een subtype") are
intentionally left out — those stay with the LLM pass that runs after this
script (see lint.md).

Why this script exists: a Haiku-run `/lint` on 2026-09-17 hallucinated wildly
on exactly these countable checks (e.g. claimed 344 files used a `domein:`
field that didn't exist anywhere in the wiki). Running the same checks as a
script instead of a narrative LLM answer makes them exact and repeatable.

Usage:
  python3 tools/lint_checks.py [onderwerp-substring]
  python3 tools/lint_checks.py --json [onderwerp-substring]   # machine-readable
  python3 tools/lint_checks.py --fix [onderwerp-substring]    # apply safe fixes, then report

With an onderwerp argument, only BO/Actor/Rol files whose `onderwerp:` field
or file path contains that substring (case-insensitive) are checked; wiki-wide
checks (orphan analysis, duplicate filenames, Begrippen/ directory) always run
over the full wiki since they are inherently cross-cutting.

`--fix` applies only categories that are mechanically safe (each verifies its
own write before committing it — see the fix_* functions): alias stripped
from `## Bronnen`-section links, dead `[[Sources/...]]` links resolved to
their real path (only when exactly one candidate file matches by basename),
`ggm_duplicaat_entiteiten` upgraded from the old flat-GUID-list schema to the
dict schema via a `ggm_parsed.json` lookup, and a missing `ggm_entiteit`/
`ggm_guid` in a `bo_homoniemen` item backfilled from its own named
`bedrijfsobject` target's frontmatter (only when that target page exists and
has that data itself). Everything else needs domain knowledge — cardinality
values, which BO a homoniem without a `bedrijfsobject` link should point to,
or (for `## GGM-duplicaten` body sections) an editorial call on which GUID is
"primair" plus a cross-reference into `ggm-terugmeldingen.md` — and is left
to the report, not guessed at.
"""

import glob
import json
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
WIKI = BASE / 'Wiki'
BO_DIRS = [WIKI / 'Bedrijfsobjecten', WIKI / 'Actoren', WIKI / 'Rollen']
GGM_PARSED = BASE / 'Sources' / 'GGM-repository' / 'ggm_parsed.json'

VALID_GRONDSLAG = {'ggm-entiteit', 'ggm-afgeleid', 'procesobject', 'governance-object'}
VALID_ARCHIMATE_TYPE = {'business-object', 'contract', 'product', 'business-actor', 'business-role'}
VALID_GGM_UML_TYPE = {'Class', 'Enumeration'}


# ---------------------------------------------------------------- utilities

def all_element_files(scope=None):
    files = []
    for d in BO_DIRS:
        if d.exists():
            files += sorted(d.rglob('*.md'))
    if scope:
        scope_low = scope.lower()
        files = [f for f in files if scope_low in str(f).lower() or _matches_onderwerp(f, scope_low)]
    return files


def _matches_onderwerp(f, scope_low):
    fm, _ = parse_frontmatter(f)
    if not fm:
        return False
    onderwerp = fm.get('onderwerp')
    if isinstance(onderwerp, list):
        return any(scope_low in str(o).lower() for o in onderwerp)
    return onderwerp is not None and scope_low in str(onderwerp).lower()


def parse_frontmatter(path):
    """Return (fields_dict_or_None, raw_frontmatter_text, body_text)."""
    txt = path.read_text(encoding='utf-8')
    if not txt.startswith('---'):
        return None, '', txt
    parts = txt.split('---', 2)
    if len(parts) < 3:
        return None, '', txt
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None, parts[1], parts[2]
    return fm, parts[1], parts[2]


def get_section(body, heading):
    """Return the body text under `## {heading}` up to the next `## `, or None."""
    m = re.search(rf'^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    return m.group(1) if m else None


def rel(path):
    return str(path.relative_to(BASE))


def wiki_relpath_no_ext(path):
    """Path relative to BASE, no .md, forward slashes — matches the `Wiki/...` prefix used in [[links]]."""
    return str(path.relative_to(BASE)).replace('\\', '/')[:-3]


# ------------------------------------------------------------------ checks

def check_bronnen_section(files):
    missing, alias_present = [], []
    for f in files:
        fm, _, body = parse_frontmatter(f)
        section = get_section(body, 'Bronnen')
        if section is None:
            missing.append(rel(f))
            continue
        for line in section.splitlines():
            if '[[' in line and '|' in line:
                alias_present.append(rel(f))
                break
    return missing, alias_present


def check_bronsamenvattingen():
    missing_section, missing_source_link = [], []
    for f in sorted((WIKI / 'Bronsamenvattingen').rglob('*.md')):
        _, _, body = parse_frontmatter(f)
        section = get_section(body, 'Bronnen')
        if section is None:
            missing_section.append(rel(f))
            continue
        if 'Sources/' not in section:
            missing_source_link.append(rel(f))
    return missing_section, missing_source_link


def check_source_links():
    """Cross-reference [[Sources/...]] links in Bronsamenvattingen against real
    files on disk. Returns (dead_links, orphan_sources) — dead_links are broken
    references (typo'd path), orphan_sources are real files nothing points to.
    'Niet-relevant' subfolders are excluded from orphan_sources: a source
    filed there was deliberately assessed as out of scope, not forgotten.
    """
    referenced = set()
    dead_links = []
    for f in sorted((WIKI / 'Bronsamenvattingen').rglob('*.md')):
        txt = f.read_text(encoding='utf-8')
        for m in re.finditer(r'\[\[(Sources/[^\]|]+)\]\]', txt):
            path = m.group(1).strip()
            referenced.add(path)
            candidate = BASE / path if path.endswith('.md') else BASE / f'{path}.md'
            if not candidate.exists():
                dead_links.append((rel(f), path))

    orphan_sources = []
    sources_dir = BASE / 'Sources' / 'Onderwerpen'
    if sources_dir.exists():
        for f in sorted(sources_dir.rglob('*.md')):
            if 'Niet-relevant' in f.parts:
                continue
            relpath = str(f.relative_to(BASE)).replace('\\', '/')[:-3]
            if relpath not in referenced:
                orphan_sources.append(rel(f))
    return dead_links, orphan_sources


def check_frontmatter_completeness(files):
    missing_grondslag, missing_ggm_fields, invalid_enum, wrong_folder = [], [], [], []
    for f in files:
        fm, _, _ = parse_frontmatter(f)
        if fm is None:
            continue
        grondslag = fm.get('grondslag')
        if not grondslag:
            missing_grondslag.append(rel(f))
            continue
        if grondslag not in VALID_GRONDSLAG:
            invalid_enum.append((rel(f), f'grondslag={grondslag!r}'))
        if grondslag == 'ggm-entiteit':
            if not fm.get('ggm_entiteit') or not fm.get('ggm_guid'):
                missing_ggm_fields.append(rel(f))
        archimate_type = fm.get('archimate_type')
        if archimate_type and archimate_type not in VALID_ARCHIMATE_TYPE:
            invalid_enum.append((rel(f), f'archimate_type={archimate_type!r}'))
        ggm_uml_type = fm.get('ggm_uml_type')
        if ggm_uml_type and ggm_uml_type not in VALID_GGM_UML_TYPE:
            invalid_enum.append((rel(f), f'ggm_uml_type={ggm_uml_type!r}'))
        if archimate_type == 'business-actor' and 'Actoren' not in str(f):
            wrong_folder.append((rel(f), 'business-actor niet in Wiki/Actoren/'))
        elif archimate_type == 'business-role' and 'Rollen' not in str(f):
            wrong_folder.append((rel(f), 'business-role niet in Wiki/Rollen/'))
        elif archimate_type not in (None, 'business-actor', 'business-role') and (
            'Actoren' in str(f) or 'Rollen' in str(f)
        ):
            wrong_folder.append((rel(f), f'{archimate_type} staat in Actoren/Rollen'))
    return missing_grondslag, missing_ggm_fields, invalid_enum, wrong_folder


def check_ggm_guid_validity(files):
    if not GGM_PARSED.exists():
        return []
    entities = json.loads(GGM_PARSED.read_text(encoding='utf-8'))['entities']
    valid_guids = set(entities.keys())
    invalid = []
    for f in files:
        fm, _, _ = parse_frontmatter(f)
        if fm is None:
            continue
        guid = fm.get('ggm_guid')
        if guid and guid not in valid_guids:
            invalid.append((rel(f), guid))
    return invalid


def check_bo_definitie(files):
    missing, placeholder = [], []
    for f in files:
        fm, _, _ = parse_frontmatter(f)
        if fm is None:
            continue
        val = (fm.get('bo_definitie') or '').strip()
        if not val:
            missing.append(rel(f))
        elif val.lower().strip('"\'') == 'gelijk aan ggm':
            placeholder.append(rel(f))
    return missing, placeholder


def check_bo_relaties(files):
    incomplete, unlinked = [], []
    for f in files:
        fm, _, _ = parse_frontmatter(f)
        if fm is None:
            continue
        relaties = fm.get('bo_relaties') or []
        for i, r in enumerate(relaties):
            if not isinstance(r, dict):
                unlinked.append((rel(f), i, 'bo_relaties item is geen dict — vermoedelijk ongequote [[..]] bug'))
                continue
            required = ['type', 'richting'] if r.get('type') == 'generalisatie' else ['type', 'richting', 'kardinaliteit']
            missing_fields = [k for k in required if not r.get(k)]
            if missing_fields:
                incomplete.append((rel(f), i, ','.join(missing_fields)))
            bo = r.get('bedrijfsobject')
            if bo is not None and not (isinstance(bo, str) and bo.strip().startswith('[[')):
                unlinked.append((rel(f), i, f'bedrijfsobject={bo!r} is geen wiki-link'))
    return incomplete, unlinked


def check_subtypes(files):
    # bo_subtypes is gedeprecieerd (zie templates/element.md): subtypes staan
    # sinds die update alleen nog in de ## Subtypes-body-sectie. Een gevulde
    # sectie zonder frontmatter-tegenhanger is dus het verwachte, correcte
    # patroon voor elke BO geschreven na de deprecatie — geen bevinding.
    fm_no_body, mismatch, missing_ggm_link = [], [], []
    for f in files:
        fm, _, body = parse_frontmatter(f)
        if fm is None:
            continue
        subtypes = fm.get('bo_subtypes') or []
        section = get_section(body, 'Subtypes')
        fm_names = set()
        for st in subtypes:
            if isinstance(st, dict):
                naam = str(st.get('naam', '')).strip('"\'')
                fm_names.add(naam)
                if st.get('ggm_entiteit') and not (st.get('ggm_guid') or st.get('ggm_attribuut')):
                    missing_ggm_link.append((rel(f), naam))
        if subtypes and section is None:
            fm_no_body.append(rel(f))
        elif subtypes and section is not None:
            body_names = set(re.findall(r'\*\*([^*]+)\*\*', section))
            missing_in_body = fm_names - body_names
            missing_in_fm = body_names - fm_names
            if missing_in_body or missing_in_fm:
                mismatch.append((rel(f), sorted(missing_in_body), sorted(missing_in_fm)))
    return fm_no_body, mismatch, missing_ggm_link


def check_duplicaten(files):
    old_schema, section_mismatch, incomplete_dict = [], [], []
    for f in files:
        fm, _, body = parse_frontmatter(f)
        if fm is None:
            continue
        dup = fm.get('ggm_duplicaat_entiteiten') or []
        section = get_section(body, 'GGM-duplicaten')
        if dup:
            for item in dup:
                if isinstance(item, str):
                    old_schema.append(rel(f))
                    break
                elif isinstance(item, dict):
                    missing = [k for k in ('entiteit', 'guid', 'beleidsdomein', 'taakveld') if not item.get(k)]
                    if missing:
                        incomplete_dict.append((rel(f), ','.join(missing)))
        if bool(dup) != (section is not None):
            section_mismatch.append(rel(f))
    return old_schema, section_mismatch, incomplete_dict


def check_homoniemen(files):
    incomplete, one_sided = [], []
    homoniem_map = {}  # this BO's relpath -> set of referenced BO wiki-link targets
    for f in files:
        fm, _, _ = parse_frontmatter(f)
        if fm is None:
            continue
        hom = fm.get('bo_homoniemen') or []
        targets = set()
        for item in hom:
            if not isinstance(item, dict):
                continue
            missing = [k for k in ('bedrijfsobject', 'ggm_entiteit', 'ggm_guid', 'ggm_beleidsdomein', 'toelichting') if not item.get(k)]
            if missing:
                incomplete.append((rel(f), ','.join(missing)))
            bo = item.get('bedrijfsobject') or ''
            m = re.search(r'\[\[([^\]|]+)', bo)
            if m:
                targets.add(m.group(1).strip())
        if targets:
            homoniem_map[wiki_relpath_no_ext(f)] = targets

    for src, targets in homoniem_map.items():
        for target in targets:
            target_norm = target.split('|')[0]
            target_back = homoniem_map.get(target_norm)
            src_wiki = f'Wiki/{src}' if not src.startswith('Wiki/') else src
            if target_back is None or not any(src_wiki in t or src in t for t in target_back):
                one_sided.append((src, target_norm))
    return incomplete, one_sided


def check_synoniemen(files):
    incomplete = []
    for f in files:
        fm, _, _ = parse_frontmatter(f)
        if fm is None:
            continue
        syn = fm.get('bo_synoniemen') or []
        for item in syn:
            if not isinstance(item, dict) or not item.get('naam') or not item.get('context'):
                incomplete.append(rel(f))
                break
    return incomplete


def check_orphan_bos():
    """Only Wiki/Bedrijfsobjecten/ — Actoren/Rollen have their own flat
    namespace and are referenced from bo_relaties, not from onderwerpoverzicht
    begrippentabellen, so they are not expected to show up there."""
    overzicht_text = ''
    for f in (WIKI / 'Onderwerpoverzichten').glob('*.md'):
        overzicht_text += f.read_text(encoding='utf-8') + '\n'
    orphans = []
    for f in sorted((WIKI / 'Bedrijfsobjecten').rglob('*.md')):
        needle = f'[[{wiki_relpath_no_ext(f)}'
        if needle not in overzicht_text:
            orphans.append(rel(f))
    return orphans


def check_begrippen_directory():
    exists = (WIKI / 'Begrippen').exists()
    dead_links = []
    for f in WIKI.rglob('*.md'):
        txt = f.read_text(encoding='utf-8')
        if '[[Wiki/Begrippen/' in txt:
            dead_links.append(rel(f))
    return exists, dead_links


def check_wiki_link_aliases():
    pattern = re.compile(r'\[\[(Wiki/[^\]|]+)\]\]')
    findings = []
    for f in WIKI.rglob('*.md'):
        txt = f.read_text(encoding='utf-8')
        txt_no_bronnen = re.sub(r'^## Bronnen\s*$\n.*?(?=^## |\Z)', '', txt, flags=re.M | re.S)
        for m in pattern.finditer(txt_no_bronnen):
            if m.group(1).count('/') >= 2:
                findings.append((rel(f), m.group(1)))
    return findings


def check_duplicate_filenames(files):
    by_name = {}
    for f in files:
        by_name.setdefault(f.name, []).append(rel(f))
    return {name: paths for name, paths in by_name.items() if len(paths) > 1}


def check_ggm_dekking_headers(scope_dir=None):
    forbidden = []
    for f in (WIKI / 'Onderwerpoverzichten').glob('*.md'):
        txt = f.read_text(encoding='utf-8')
        if re.search(r'^## GGM-(entiteitendekking|dekkingsanalyse)\s*$', txt, re.M):
            forbidden.append(rel(f))
    return forbidden


def check_begrippentabel_format():
    no_table, no_dataobject_col, empty_bo_col = [], [], []
    for f in (WIKI / 'Onderwerpoverzichten').glob('*.md'):
        txt = f.read_text(encoding='utf-8')
        section = get_section(txt, 'Begrippen')
        if section is None:
            continue
        header_match = re.search(r'^\|.*\|\s*$', section, re.M)
        if not header_match:
            no_table.append(rel(f))
            continue
        header = header_match.group(0)
        if 'Data-object' not in header:
            no_dataobject_col.append(rel(f))
        cols = [c.strip() for c in header.strip('|').split('|')]
        try:
            bo_idx = next(i for i, c in enumerate(cols) if c.strip() == 'BO?')
        except StopIteration:
            continue
        rows = re.findall(r'^\|.*\|\s*$', section, re.M)[2:]  # skip header + separator
        for row in rows:
            cells = [c.strip() for c in row.strip('|').split('|')]
            if len(cells) > bo_idx and not cells[bo_idx]:
                empty_bo_col.append(rel(f))
                break
    return no_table, no_dataobject_col, empty_bo_col


def check_antipatroon_registr(files):
    candidates = []
    pattern = re.compile(r'registreerbaar|registratieobject', re.IGNORECASE)
    for f in files:
        _, _, body = parse_frontmatter(f)
        for line in body.splitlines():
            if pattern.search(line):
                candidates.append((rel(f), line.strip()[:140]))
    for f in (WIKI / 'Onderwerpoverzichten').glob('*.md'):
        txt = f.read_text(encoding='utf-8')
        for line in txt.splitlines():
            if pattern.search(line) and '|' in line:
                candidates.append((rel(f), line.strip()[:140]))
    return candidates


# -------------------------------------------------------------------- fixes

def _strip_bronnen_aliases_text(text):
    """Remove `|alias` from `[[path|alias]]` links inside `## Bronnen`
    sections only. Pure function of the file text — used by
    fix_bronnen_aliases and unit-testable without touching disk."""
    pattern = re.compile(r'^(\s*-\s*\[\[)([^\]|]+)\|([^\]]+)(\]\])(.*)$')
    lines = text.split('\n')
    out = []
    in_bronnen = False
    changed = False
    for line in lines:
        if re.match(r'^## Bronnen\s*$', line):
            in_bronnen = True
            out.append(line)
            continue
        if in_bronnen and re.match(r'^## ', line):
            in_bronnen = False
        if in_bronnen:
            m = pattern.match(line)
            if m:
                out.append(f'{m.group(1)}{m.group(2)}{m.group(4)}{m.group(5)}')
                changed = True
                continue
        out.append(line)
    return '\n'.join(out), changed


def fix_bronnen_aliases(dry_run=True):
    fixed_files = []
    for f in sorted(WIKI.rglob('*.md')):
        txt = f.read_text(encoding='utf-8')
        new_txt, changed = _strip_bronnen_aliases_text(txt)
        if changed:
            fixed_files.append(rel(f))
            if not dry_run:
                f.write_text(new_txt, encoding='utf-8')
    return fixed_files


def fix_dead_source_links(dry_run=True):
    """Only fixes an unambiguous case: exactly one file under
    Sources/Onderwerpen/ matches the broken link's basename. Anything else
    (zero or multiple matches) is reported as unresolved, not guessed at."""
    dead_links, _ = check_source_links()
    fixed, unresolved = [], []
    for fpath_rel, broken in dead_links:
        fpath = BASE / fpath_rel
        basename = broken[:-3] if broken.endswith('.md') else broken
        basename = basename.rsplit('/', 1)[-1]
        candidates = list((BASE / 'Sources' / 'Onderwerpen').rglob(f'{basename}.md'))
        if len(candidates) != 1:
            unresolved.append((fpath_rel, broken, len(candidates)))
            continue
        real_path = str(candidates[0].relative_to(BASE)).replace('\\', '/')[:-3]
        txt = fpath.read_text(encoding='utf-8')
        new_txt = txt.replace(f'[[{broken}]]', f'[[{real_path}]]')
        if new_txt == txt:
            unresolved.append((fpath_rel, broken, 0))
            continue
        fixed.append((fpath_rel, broken, real_path))
        if not dry_run:
            fpath.write_text(new_txt, encoding='utf-8')
    return fixed, unresolved


def _yaml_scalar(s):
    s = str(s)
    if re.match(r'^[\w\s\-]+$', s) and not s[:1].isdigit():
        return s
    return f'"{s}"'


def fix_duplicaat_schema(dry_run=True):
    """Upgrades ggm_duplicaat_entiteiten from a flat GUID-string list to the
    dict schema (entiteit/guid/beleidsdomein/taakveld), via ggm_parsed.json.
    afwijkende_attributen is left blank — not derivable from the GGM source.
    Verifies the GUID set is unchanged before writing; aborts per-file (does
    not write) on a missing GUID or any mismatch after the rewrite."""
    if not GGM_PARSED.exists():
        return [], []
    entities = json.loads(GGM_PARSED.read_text(encoding='utf-8'))['entities']
    old_schema_files, _, _ = check_duplicaten(all_element_files())

    fixed, aborted = [], []
    for relpath in old_schema_files:
        f = BASE / relpath
        txt = f.read_text(encoding='utf-8')
        parts = txt.split('---', 2)
        fm_text = parts[1]
        old_fields = yaml.safe_load(fm_text) or {}

        m = re.search(r'^ggm_duplicaat_entiteiten:\n((?:  - "?EAID_[A-Za-z0-9_]+"?\n)+)', fm_text, re.M)
        if not m:
            aborted.append((relpath, 'patroon niet gevonden (afwijkend format)'))
            continue
        guids = re.findall(r'EAID_[A-Za-z0-9_]+', m.group(1))

        new_items, ok = [], True
        for guid in guids:
            ent = entities.get(guid)
            if not ent:
                aborted.append((relpath, f'guid niet in ggm_parsed.json: {guid}'))
                ok = False
                break
            new_items.append(
                f'  - entiteit: {_yaml_scalar(ent["name"])}\n'
                f'    guid: {guid}\n'
                f'    beleidsdomein: {_yaml_scalar(ent.get("beleidsdomein") or "")}\n'
                f'    taakveld: {_yaml_scalar(ent.get("taakveld") or "")}\n'
                f'    afwijkende_attributen:\n'
            )
        if not ok:
            continue

        new_fm_text = fm_text[:m.start()] + 'ggm_duplicaat_entiteiten:\n' + ''.join(new_items) + fm_text[m.end():]
        new_fields = yaml.safe_load(new_fm_text) or {}
        old_guids = {x if isinstance(x, str) else x.get('guid') for x in old_fields.get('ggm_duplicaat_entiteiten', [])}
        new_guids = {x.get('guid') for x in new_fields.get('ggm_duplicaat_entiteiten', [])}
        if old_guids != new_guids:
            aborted.append((relpath, f'guid-mismatch na herschrijven: oud={old_guids} nieuw={new_guids}'))
            continue

        fixed.append((relpath, len(guids)))
        if not dry_run:
            new_txt = parts[0] + '---' + new_fm_text + '---' + parts[2]
            f.write_text(new_txt, encoding='utf-8')
    return fixed, aborted


def fix_homoniemen_ggm_backfill(dry_run=True):
    """Backfills a missing ggm_entiteit/ggm_guid in a bo_homoniemen item —
    but only when that item already names a `bedrijfsobject` target that (a)
    exists as a real wiki page and (b) itself has non-blank ggm_entiteit/
    ggm_guid to copy from. Anything else (no target page, target has no GGM
    grounding either, missing `bedrijfsobject` itself) is a real content gap
    that requires a human decision — reported as unresolved, not guessed at.
    """
    guid_index = {}  # relpath (no .md, Wiki/... prefix) -> (ggm_entiteit, ggm_guid)
    for f in all_element_files():
        fm, _, _ = parse_frontmatter(f)
        if fm and fm.get('ggm_entiteit') and fm.get('ggm_guid'):
            guid_index[wiki_relpath_no_ext(f)] = (fm['ggm_entiteit'], fm['ggm_guid'])

    fixed, unresolved = [], []
    for f in all_element_files():
        fm, fm_text, body = parse_frontmatter(f)
        if fm is None or not fm.get('bo_homoniemen'):
            continue
        new_fm_text = fm_text
        item_changed = False
        for item in fm['bo_homoniemen']:
            if not isinstance(item, dict):
                continue
            missing = [k for k in ('ggm_entiteit', 'ggm_guid') if not item.get(k)]
            if not missing:
                continue
            bo = item.get('bedrijfsobject') or ''
            m = re.search(r'\[\[([^\]|]+)', bo)
            if not m:
                unresolved.append((rel(f), 'bedrijfsobject zelf ontbreekt — geen target om van te lenen'))
                continue
            target_path = m.group(1).strip()
            target_data = guid_index.get(target_path)
            if not target_data:
                unresolved.append((rel(f), f'target {target_path} bestaat niet of heeft zelf geen ggm_entiteit/ggm_guid'))
                continue
            target_entiteit, target_guid = target_data
            # Only touch the specific empty scalar lines that sit right after
            # this item's `- bedrijfsobject:` line, up to the next item/field,
            # so we never risk touching an unrelated homoniem entry.
            bo_line_pat = re.escape(bo.strip())
            item_block_pat = re.compile(
                rf'(-\s*bedrijfsobject:\s*"?{bo_line_pat}"?\n(?:    [a-z_]+:.*\n)*)', re.M
            )
            block_m = item_block_pat.search(new_fm_text)
            if not block_m:
                unresolved.append((rel(f), f'kon item-blok voor {target_path} niet exact terugvinden in ruwe tekst'))
                continue
            block = block_m.group(1)
            new_block = block
            if 'ggm_entiteit' in missing:
                new_block = re.sub(r'(\n    ggm_entiteit:)\s*\n', rf'\1 {_yaml_scalar(target_entiteit)}\n', new_block)
            if 'ggm_guid' in missing:
                new_block = re.sub(r'(\n    ggm_guid:)\s*\n', rf'\1 {target_guid}\n', new_block)
            if new_block != block:
                new_fm_text = new_fm_text[:block_m.start()] + new_block + new_fm_text[block_m.end():]
                item_changed = True
        if item_changed:
            new_fields = yaml.safe_load(new_fm_text) or {}
            # semantic check: every old field/value survives, only the
            # targeted blanks became non-blank
            old_homoniemen = fm['bo_homoniemen']
            new_homoniemen = new_fields.get('bo_homoniemen') or []
            if len(old_homoniemen) != len(new_homoniemen):
                unresolved.append((rel(f), 'ABORT: aantal homoniem-items veranderd na herschrijven'))
                continue
            ok = True
            for old_item, new_item in zip(old_homoniemen, new_homoniemen):
                for k, v in old_item.items():
                    if v and new_item.get(k) != v:
                        ok = False
            if not ok:
                unresolved.append((rel(f), 'ABORT: bestaande waarde veranderd na herschrijven'))
                continue
            fixed.append(rel(f))
            if not dry_run:
                txt = f.read_text(encoding='utf-8')
                parts = txt.split('---', 2)
                new_txt = parts[0] + '---' + new_fm_text + '---' + parts[2]
                f.write_text(new_txt, encoding='utf-8')
    return fixed, unresolved


def run_fixes():
    print('# Fixes toegepast\n')

    alias_fixed = fix_bronnen_aliases(dry_run=False)
    print(f'Bronnen-alias gestript: {len(alias_fixed)}')
    for x in alias_fixed:
        print(f'  - {x}')

    link_fixed, link_unresolved = fix_dead_source_links(dry_run=False)
    print(f'\nDode Sources-links opgelost: {len(link_fixed)}')
    for f, old, new in link_fixed:
        print(f'  - {f}: [[{old}]] -> [[{new}]]')
    if link_unresolved:
        print(f'Niet opgelost, handmatig nodig ({len(link_unresolved)}):')
        for f, old, n in link_unresolved:
            print(f'  - {f}: [[{old}]] ({n} kandidaten)')

    dup_fixed, dup_aborted = fix_duplicaat_schema(dry_run=False)
    print(f'\nggm_duplicaat_entiteiten schema-upgrades: {len(dup_fixed)}')
    for f, n in dup_fixed:
        print(f'  - {f} ({n} entiteit(en))')
    if dup_aborted:
        print(f'Niet opgelost, handmatig nodig ({len(dup_aborted)}):')
        for f, reason in dup_aborted:
            print(f'  - {f}: {reason}')

    hom_fixed, hom_unresolved = fix_homoniemen_ggm_backfill(dry_run=False)
    print(f'\nbo_homoniemen ggm_entiteit/ggm_guid aangevuld vanuit target-BO: {len(hom_fixed)}')
    for f in hom_fixed:
        print(f'  - {f}')
    if hom_unresolved:
        print(f'Niet opgelost, vereist inhoudelijke keuze ({len(hom_unresolved)}):')
        for f, reason in hom_unresolved:
            print(f'  - {f}: {reason}')

    print('\n---\n')


# ------------------------------------------------------------------- main

def fmt_list(items, limit=25):
    out = [f'    - {x}' for x in items[:limit]]
    if len(items) > limit:
        out.append(f'    ... (+{len(items) - limit} meer)')
    return '\n'.join(out)


def main():
    args = [a for a in sys.argv[1:] if a not in ('--json', '--fix')]
    as_json = '--json' in sys.argv
    do_fix = '--fix' in sys.argv
    scope = args[0] if args else None

    if do_fix:
        run_fixes()

    files = all_element_files(scope)
    report = {}

    missing_bronnen, alias_bronnen = check_bronnen_section(files)
    report['BO zonder ## Bronnen sectie'] = missing_bronnen
    report['Alias in Bronnen-sectie (verboden)'] = alias_bronnen

    if not scope:
        bs_missing_section, bs_missing_source = check_bronsamenvattingen()
        report['Bronsamenvatting zonder ## Bronnen sectie'] = bs_missing_section
        report['Bronsamenvatting zonder Sources-link'] = bs_missing_source
        dead_links, orphan_sources = check_source_links()
        report['Dode Sources-link in bronsamenvatting (kapot pad)'] = [f'{f}: [[{p}]]' for f, p in dead_links]
        report['Source zonder bronsamenvatting-referentie (excl. Niet-relevant/)'] = orphan_sources

    missing_grondslag, missing_ggm_fields, invalid_enum, wrong_folder = check_frontmatter_completeness(files)
    report['Ontbrekende grondslag'] = missing_grondslag
    report['grondslag=ggm-entiteit zonder ggm_entiteit/ggm_guid'] = missing_ggm_fields
    report['Ongeldige enum-waarde'] = [f'{f}: {m}' for f, m in invalid_enum]
    report['Element in verkeerde map (Actoren/Rollen/Bedrijfsobjecten)'] = [f'{f}: {m}' for f, m in wrong_folder]

    invalid_guids = check_ggm_guid_validity(files)
    report['ggm_guid niet gevonden in ggm_parsed.json'] = [f'{f}: {g}' for f, g in invalid_guids]

    missing_def, placeholder_def = check_bo_definitie(files)
    report['bo_definitie ontbrekend/leeg'] = missing_def
    report['bo_definitie = placeholder "gelijk aan GGM"'] = placeholder_def

    incomplete_rel, unlinked_rel = check_bo_relaties(files)
    report['bo_relaties item mist type/richting/kardinaliteit'] = [f'{f}[{i}]: mist {m}' for f, i, m in incomplete_rel]
    report['bo_relaties.bedrijfsobject geen wiki-link / parse-bug'] = [f'{f}[{i}]: {m}' for f, i, m in unlinked_rel]

    fm_no_body, subtype_mismatch, subtype_ggm_missing = check_subtypes(files)
    report['bo_subtypes gevuld zonder ## Subtypes sectie'] = fm_no_body
    report['bo_subtypes frontmatter/body mismatch'] = [f'{f}: alleen-fm={a} alleen-body={b}' for f, a, b in subtype_mismatch]
    report['Subtype met ggm_entiteit maar zonder ggm_guid/ggm_attribuut'] = [f'{f}: {n}' for f, n in subtype_ggm_missing]

    old_schema, dup_section_mismatch, dup_incomplete = check_duplicaten(files)
    report['ggm_duplicaat_entiteiten oude schema (string i.p.v. dict)'] = old_schema
    report['ggm_duplicaat_entiteiten/## GGM-duplicaten sectie mismatch'] = dup_section_mismatch
    report['ggm_duplicaat_entiteiten dict mist verplicht veld'] = [f'{f}: mist {m}' for f, m in dup_incomplete]

    hom_incomplete, hom_one_sided = check_homoniemen(files)
    report['bo_homoniemen item mist verplicht veld'] = [f'{f}: mist {m}' for f, m in hom_incomplete]
    report['bo_homoniemen eenzijdig (geen symmetrie)'] = [f'{s} -> {t}' for s, t in hom_one_sided]

    report['bo_synoniemen item mist naam/context'] = check_synoniemen(files)

    if not scope:
        report['Wees-BO (niet gelinkt vanuit onderwerpoverzicht)'] = check_orphan_bos()
        begrippen_exists, begrippen_dead_links = check_begrippen_directory()
        report['Wiki/Begrippen/ directory bestaat (mag niet)'] = ['Wiki/Begrippen/ bestaat!'] if begrippen_exists else []
        report['Dode [[Wiki/Begrippen/ links'] = begrippen_dead_links
        report['Wiki-link zonder verplichte alias'] = [f'{f}: {p}' for f, p in check_wiki_link_aliases()]
        dupes = check_duplicate_filenames(files)
        report['Duplicaat bestandsnamen (potentieel homoniem)'] = [f'{name}: {", ".join(paths)}' for name, paths in dupes.items()]
        report['Onderwerpoverzicht met verwijderde GGM-dekkingssectie'] = check_ggm_dekking_headers()
        no_table, no_dataobj, empty_bo = check_begrippentabel_format()
        report['Onderwerpoverzicht: begrippentabel ontbreekt/geen tabel'] = no_table
        report['Onderwerpoverzicht: geen Data-object kolom'] = no_dataobj
        report['Onderwerpoverzicht: BO?-kolom leeg voor een begrip'] = empty_bo

    report['Anti-patroon "registreerbaar/registratieobject" — kandidaten voor LLM-beoordeling'] = [
        f'{f}: {line}' for f, line in check_antipatroon_registr(files)
    ]

    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    total = 0
    print(f'# Deterministische lint-check{" — scope: " + scope if scope else " — hele wiki"}')
    print(f'({len(files)} element-pagina\'s gecontroleerd)\n')
    for name, items in report.items():
        n = len(items)
        total += n
        marker = '⚠️ ' if n else '✅ '
        print(f'{marker}{name}: {n}')
        if items:
            print(fmt_list(items))
        print()
    print(f'TOTAAL: {total} bevindingen (excl. registr*-kandidaten die LLM-beoordeling vereisen)')


if __name__ == '__main__':
    main()
