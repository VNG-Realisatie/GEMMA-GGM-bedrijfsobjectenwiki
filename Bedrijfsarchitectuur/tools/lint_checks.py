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

With an onderwerp argument, only BO/Actor/Rol files whose `onderwerp:` field
or file path contains that substring (case-insensitive) are checked; wiki-wide
checks (orphan analysis, duplicate filenames, Begrippen/ directory) always run
over the full wiki since they are inherently cross-cutting.
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
    fm_no_body, body_no_fm, mismatch, missing_ggm_link = [], [], [], []
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
        elif not subtypes and section is not None:
            body_no_fm.append(rel(f))
        elif subtypes and section is not None:
            body_names = set(re.findall(r'\*\*([^*]+)\*\*', section))
            missing_in_body = fm_names - body_names
            missing_in_fm = body_names - fm_names
            if missing_in_body or missing_in_fm:
                mismatch.append((rel(f), sorted(missing_in_body), sorted(missing_in_fm)))
    return fm_no_body, body_no_fm, mismatch, missing_ggm_link


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


# ------------------------------------------------------------------- main

def fmt_list(items, limit=25):
    out = [f'    - {x}' for x in items[:limit]]
    if len(items) > limit:
        out.append(f'    ... (+{len(items) - limit} meer)')
    return '\n'.join(out)


def main():
    args = [a for a in sys.argv[1:] if a != '--json']
    as_json = '--json' in sys.argv
    scope = args[0] if args else None

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

    fm_no_body, body_no_fm, subtype_mismatch, subtype_ggm_missing = check_subtypes(files)
    report['bo_subtypes gevuld zonder ## Subtypes sectie'] = fm_no_body
    report['## Subtypes sectie zonder bo_subtypes in frontmatter'] = body_no_fm
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
