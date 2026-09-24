#!/usr/bin/env python3
"""Generate GGM-GEMMA CSV export files from parsed XMI + wiki BO pages.

Produces 5 CSV files in exports/:
1. GGM_GEMMA_objecten_{date}.csv     - all entities with GGM + GEMMA fields
2. GGM_GEMMA_relaties_{date}.csv     - all relations with GGM + GEMMA fields
3. GGM_diagram_objecten_{date}.csv   - diagram-entity mapping
4. GGM_beleidsdomeinen_{date}.csv    - beleidsdomein metadata
5. GGM_diagrammen_{date}.csv         - diagram metadata
"""

import csv
import json
import sys
import re
import yaml
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
EXPORTS = BASE / 'exports'
WIKI_BO = BASE / 'Wiki' / 'Bedrijfsobjecten'
WIKI_ELEMENT_DIRS = [WIKI_BO, BASE / 'Wiki' / 'Actoren', BASE / 'Wiki' / 'Rollen']


def clean_nan(val: str) -> str:
    if val in ('nan', 'None', 'none'):
        return ''
    return val


def clean_html(val: str) -> str:
    return re.sub(r'<[^>]+>', '', val).strip()


def load_xmi_data(json_path: str) -> dict:
    with open(json_path) as f:
        return json.load(f)


def load_wiki_bo_pages() -> dict:
    """Load all wiki BO pages. Returns dict keyed by ggm_guid and by naam.

    When a BO has ggm_duplicaat_entiteiten, the same BO entry is registered
    under each duplicate GUID so that the export generates a row per GUID.
    """
    by_guid = {}
    by_name = {}
    for md in (f for d in WIKI_ELEMENT_DIRS if d.exists() for f in d.rglob('*.md')):
        if md.name == 'map.md':
            continue
        content = md.read_text(encoding='utf-8')
        if not content.startswith('---'):
            continue
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            continue
        if not fm or fm.get('type') != 'element':
            continue

        subtypes = fm.get('bo_subtypes', [])
        subtypes_str = ', '.join(s.get('naam', '') for s in subtypes) if subtypes else ''

        entry = {
            'naam': fm.get('naam', ''),
            'bo_definitie': fm.get('bo_definitie', ''),
            'bo_subtypes': subtypes_str,
            'ggm_guid': fm.get('ggm_guid', ''),
            'ggm_entiteit': fm.get('ggm_entiteit', ''),
            'grondslag': fm.get('grondslag', ''),
            'archimate_type': fm.get('archimate_type', ''),
        }

        # Meerdere pagina's mogen dezelfde GUID dragen (twee-pagina-patroon
        # BO + actor/rol): by_guid is een lijst per GUID, business-object
        # eerst, en de export schrijft een rij per pagina.
        def _register(guid, e):
            lst = by_guid.setdefault(guid, [])
            if e['archimate_type'] == 'business-object':
                lst.insert(0, e)
            else:
                lst.append(e)

        if entry['ggm_guid']:
            _register(entry['ggm_guid'], entry)
        if entry['naam'] and (entry['naam'] not in by_name
                or entry['archimate_type'] == 'business-object'):
            by_name[entry['naam']] = entry

        # Register duplicate GUIDs so the export emits a row per GUID
        # Supports both old format (plain GUID string) and new format (dict with 'guid' key)
        duplicates = fm.get('ggm_duplicaat_entiteiten', [])
        if duplicates:
            for dup in duplicates:
                dup_guid = dup if isinstance(dup, str) else dup.get('guid', '')
                if dup_guid and dup_guid not in by_guid:
                    _register(dup_guid, entry)

    return by_guid, by_name


def resolve_taakveld(pkg_id: str, packages: dict) -> str:
    """Walk up from a package to find the taakveld (top-level Domein under Basismodel)."""
    current = pkg_id
    visited = set()
    while current and current not in visited:
        visited.add(current)
        pkg = packages.get(current, {})
        parent_id = pkg.get('parent_id', '')
        parent = packages.get(parent_id, {})
        if parent.get('stereotype') == 'Basismodel':
            return pkg.get('name', '')
        current = parent_id
    return ''


def resolve_beleidsdomein_for_diagram(diag: dict, packages: dict) -> tuple[str, str, str]:
    """Find the beleidsdomein that owns a diagram. Returns (id, name, taakveld)."""
    diag_pkg_id = diag.get('package_id', '')
    diag_pkg = packages.get(diag_pkg_id, {})

    # Diagram packages sit inside beleidsdomein packages
    # Walk up until we find a package with stereotype "Domein"
    current = diag_pkg.get('parent_id', diag_pkg_id)
    visited = set()
    while current and current not in visited:
        visited.add(current)
        pkg = packages.get(current, {})
        if pkg.get('stereotype') == 'Domein':
            taakveld = resolve_taakveld(current, packages)
            if taakveld != pkg.get('name', ''):
                return current, pkg.get('name', ''), taakveld
            # This IS the taakveld, not a beleidsdomein
            return current, pkg.get('name', ''), pkg.get('name', '')
        current = pkg.get('parent_id', '')
    return '', '', ''


def get_beleidsdomeinen(packages: dict) -> list[dict]:
    """Extract all beleidsdomein packages (Domein stereotype, not top-level taakvelden)."""
    basismodel_children = set()
    basismodel_id = None
    for pid, pkg in packages.items():
        if pkg.get('stereotype') == 'Basismodel':
            basismodel_id = pid
            break

    for pid, pkg in packages.items():
        if pkg.get('parent_id') == basismodel_id:
            basismodel_children.add(pid)

    result = []
    for pid, pkg in packages.items():
        if pkg.get('stereotype') != 'Domein':
            continue
        taakveld = resolve_taakveld(pid, packages)
        is_taakveld = pid in basismodel_children
        result.append({
            'id': pid,
            'name': pkg.get('name', ''),
            'taakveld': taakveld,
            'is_taakveld': is_taakveld,
            'documentation': pkg.get('documentation', ''),
            'toelichting': pkg.get('tags', {}).get('Toelichting', ''),
        })
    return result


def gemma_tag(entity_or_rel: dict, key: str) -> str:
    val = entity_or_rel.get('gemma_tags', {}).get(key, '')
    return clean_nan(val)


def entity_tag(entity: dict, key: str) -> str:
    val = entity.get('tags', {}).get(key, '')
    return clean_nan(val)


def export_objecten(data: dict, bo_by_guid: dict, bo_by_name: dict,
                    timestamp: str, date_str: str):
    entities = data['entities']
    packages = data['packages']

    rows = []
    nr = 0
    for eid, e in sorted(entities.items(), key=lambda x: x[1].get('name', '')):
        nr += 1
        name = e.get('name', '')

        # Wiki element lookup — bij een gedeelde GUID (twee-pagina-patroon
        # BO + actor/rol) komt er een rij per pagina, business-object eerst.
        pages = bo_by_guid.get(eid)
        if not pages:
            nb = bo_by_name.get(name)
            pages = [nb] if nb else [None]
        for page_i, bo in enumerate(pages):
            if page_i > 0:
                nr += 1
            wiki_naam = bo['naam'] if bo else ''
            wiki_def = bo.get('bo_definitie', '') if bo else ''
            wiki_subtypes = bo.get('bo_subtypes', '') if bo else ''
            wiki_archimate = bo.get('archimate_type', '') if bo else ''
            if wiki_def == 'gelijk aan GGM':
                wiki_def = ''

            # GEMMA fields: wiki first, then XMI GEMMA tags
            gemma_naam = wiki_naam or gemma_tag(e, 'gemma_naam')
            gemma_def = wiki_def or clean_html(gemma_tag(e, 'gemma_definitie'))
            gemma_toel = gemma_tag(e, 'gemma_toelichting')
            gemma_syn = gemma_tag(e, 'gemma_synoniemen')
            gemma_bron = gemma_tag(e, 'gemma_bron')

            # GEMMA-managed fields (always from XMI)
            gemma_guid = gemma_tag(e, 'gemma_guid')
            gemma_type = gemma_tag(e, 'gemma_type')
            gemma_url = gemma_tag(e, 'gemma_url')
            gemma_alt = gemma_tag(e, 'gemma_alternate_name')

            # domein-iv3
            beleidsdomein = e.get('beleidsdomein', '')
            taakveld = e.get('taakveld', '')
            domein_iv3 = f"{taakveld} > {beleidsdomein}" if taakveld and beleidsdomein and taakveld != beleidsdomein else (beleidsdomein or taakveld)

            rows.append({
                'nr': nr,
                'GEMMA-naam': gemma_naam,
                'GGM-naam': name,
                'GEMMA-guid': gemma_guid,
                'GGM-guid': eid,
                'GEMMA-type': gemma_type,
                'GGM-uml-type': e.get('uml_type', '').lower(),
                'archimate_type': wiki_archimate,
                'GEMMA-definitie': gemma_def,
                'GGM-definitie': clean_html(e.get('documentation', '')),
                'GEMMA-toelichting': gemma_toel,
                'GGM-toelichting': entity_tag(e, 'Toelichting'),
                'GEMMA-synoniemen': gemma_syn,
                'GGM-synoniemen': entity_tag(e, 'Synoniemen'),
                'GEMMA-bron': gemma_bron,
                'GGM-bron': entity_tag(e, 'Herkomst'),
                'GEMMA-url': gemma_url,
                'GEMMA-alternate-name': gemma_alt,
                'GEMMA-specialisaties': wiki_subtypes,
                'domein-iv3': domein_iv3,
                'domein-dcat': '',
                'Datum-tijd-export': timestamp,
            })

    path = EXPORTS / f'GGM_GEMMA_objecten_{date_str}.csv'
    _write_csv(path, rows)
    return len(rows)


def export_relaties(data: dict, timestamp: str, date_str: str):
    relations = data['relations']
    entities = data['entities']

    rows = []
    nr = 0
    for rid, r in sorted(relations.items(), key=lambda x: x[1].get('name', '')):
        source_id = r.get('source_id', '')
        target_id = r.get('target_id', '')

        if source_id not in entities or target_id not in entities:
            continue

        nr += 1
        uml_type = r.get('uml_type', '')

        # Map UML type to ArchiMate type
        archimate_type = {
            'Association': 'association-relationship',
            'Generalization': 'specialization-relationship',
            'Aggregation': 'aggregation-relationship',
            'Composition': 'composition-relationship',
        }.get(uml_type, 'association-relationship')

        gemma_type = gemma_tag(r, 'gemma-type') or archimate_type

        # Source/target GEMMA guids
        src_entity = entities.get(source_id, {})
        tgt_entity = entities.get(target_id, {})
        gemma_src_guid = gemma_tag(r, 'gemma-source-guid') or gemma_tag(src_entity, 'gemma_guid')
        gemma_tgt_guid = gemma_tag(r, 'gemma-target-guid') or gemma_tag(tgt_entity, 'gemma_guid')

        rows.append({
            'nr': nr,
            'GEMMA-naam': clean_nan(gemma_tag(r, 'gemma-naam')) or r.get('name', ''),
            'GGM-naam': r.get('name', ''),
            'GEMMA-guid': gemma_tag(r, 'gemma-guid'),
            'GGM-guid': rid,
            'GEMMA-type': gemma_type,
            'GGM-uml-type': uml_type.lower(),
            'GEMMA-definitie': clean_nan(gemma_tag(r, 'gemma-definitie')),
            'GGM-definitie': r.get('documentation', ''),
            'GEMMA-toelichting': clean_nan(gemma_tag(r, 'gemma-toelichting')),
            'GGM-toelichting': clean_nan(r.get('tags', {}).get('toelichting', '')),
            'GEMMA-source-guid': gemma_src_guid,
            'GGM-source-guid': source_id,
            'GEMMA-target-guid': gemma_tgt_guid,
            'GGM-target-guid': target_id,
            'Datum-tijd-export': timestamp,
        })

    path = EXPORTS / f'GGM_GEMMA_relaties_{date_str}.csv'
    _write_csv(path, rows)
    return len(rows)


def export_diagram_objecten(data: dict, date_str: str):
    diagrams = data['diagrams']
    entities = data['entities']
    packages = data['packages']

    rows = []
    for did, diag in sorted(diagrams.items(), key=lambda x: x[1].get('name', '')):
        bd_id, bd_name, taakveld = resolve_beleidsdomein_for_diagram(diag, packages)
        for subject in diag.get('subjects', []):
            if subject in entities:
                e = entities[subject]
                rows.append({
                    'diagram_guid': did,
                    'diagram_naam': diag['name'],
                    'element_guid': subject,
                    'element_naam': e['name'],
                    'element_uml_type': e.get('uml_type', ''),
                    'beleidsdomein_guid': bd_id,
                    'beleidsdomein_naam': bd_name,
                    'taakveld': taakveld,
                })

    path = EXPORTS / f'GGM_diagram_objecten_{date_str}.csv'
    _write_csv(path, rows)
    return len(rows)


def export_beleidsdomeinen(data: dict, date_str: str):
    packages = data['packages']
    beleidsdomeinen = get_beleidsdomeinen(packages)

    rows = []
    for bd in sorted(beleidsdomeinen, key=lambda x: x['name']):
        rows.append({
            'beleidsdomein_guid': bd['id'],
            'beleidsdomein_naam': bd['name'],
            'is_taakveld': 'ja' if bd['is_taakveld'] else 'nee',
            'taakveld': bd['taakveld'],
            'definitie': bd['documentation'],
            'toelichting': bd['toelichting'],
        })

    path = EXPORTS / f'GGM_beleidsdomeinen_{date_str}.csv'
    _write_csv(path, rows)
    return len(rows)


def export_diagrammen(data: dict, date_str: str):
    diagrams = data['diagrams']
    packages = data['packages']

    rows = []
    for did, diag in sorted(diagrams.items(), key=lambda x: x[1].get('name', '')):
        bd_id, bd_name, taakveld = resolve_beleidsdomein_for_diagram(diag, packages)
        entity_count = sum(1 for s in diag.get('subjects', []) if s in data['entities'])
        rows.append({
            'diagram_guid': did,
            'diagram_naam': diag['name'],
            'beleidsdomein_guid': bd_id,
            'beleidsdomein_naam': bd_name,
            'taakveld': taakveld,
            'aantal_entiteiten': entity_count,
        })

    path = EXPORTS / f'GGM_diagrammen_{date_str}.csv'
    _write_csv(path, rows)
    return len(rows)


def _write_csv(path: Path, rows: list[dict]):
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter=';',
                                quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


def main():
    base = Path(__file__).resolve().parent.parent
    default_json = base / 'Sources' / 'GGM-repository' / 'ggm_parsed.json'
    json_path = sys.argv[1] if len(sys.argv) > 1 else str(default_json)
    if not Path(json_path).exists():
        print(f"Error: {json_path} not found. Run parse_ggm_xmi.py first.", file=sys.stderr)
        sys.exit(1)

    now = datetime.now()
    timestamp = now.strftime('%d%m%Y-%H:%M:%S')
    date_str = now.strftime('%Y%m%d')

    print("Loading XMI data...", file=sys.stderr)
    data = load_xmi_data(json_path)

    print("Loading wiki BO pages...", file=sys.stderr)
    bo_by_guid, bo_by_name = load_wiki_bo_pages()

    print(f"Wiki BO pages: {len(bo_by_guid)} with ggm_guid, "
          f"{len(bo_by_name)} total", file=sys.stderr)
    print(file=sys.stderr)

    n_obj = export_objecten(data, bo_by_guid, bo_by_name, timestamp, date_str)
    print(f"✅ GGM_GEMMA_objecten_{date_str}.csv — {n_obj} objecten", file=sys.stderr)

    n_rel = export_relaties(data, timestamp, date_str)
    print(f"✅ GGM_GEMMA_relaties_{date_str}.csv — {n_rel} relaties", file=sys.stderr)

    n_diag_obj = export_diagram_objecten(data, date_str)
    print(f"✅ GGM_diagram_objecten_{date_str}.csv — {n_diag_obj} diagram-entiteit regels",
          file=sys.stderr)

    n_bd = export_beleidsdomeinen(data, date_str)
    print(f"✅ GGM_beleidsdomeinen_{date_str}.csv — {n_bd} beleidsdomeinen", file=sys.stderr)

    n_diag = export_diagrammen(data, date_str)
    print(f"✅ GGM_diagrammen_{date_str}.csv — {n_diag} diagrammen", file=sys.stderr)

    # Summary
    entities_with_bo = sum(1 for eid in data['entities']
                          if eid in bo_by_guid or data['entities'][eid]['name'] in bo_by_name)
    entities_with_gemma = sum(1 for e in data['entities'].values()
                             if e.get('gemma_tags', {}).get('gemma_guid'))

    print(file=sys.stderr)
    print(f"Samenvatting:", file=sys.stderr)
    print(f"  Entiteiten totaal:       {len(data['entities'])}", file=sys.stderr)
    print(f"  Met wiki-BO:             {entities_with_bo}", file=sys.stderr)
    print(f"  Met GEMMA-guid in XMI:   {entities_with_gemma}", file=sys.stderr)
    print(f"  Relaties:                {n_rel}", file=sys.stderr)
    print(f"  Diagrammen:              {n_diag}", file=sys.stderr)
    print(f"  Beleidsdomeinen:         {n_bd}", file=sys.stderr)
    print(f"  Bestanden in:            {EXPORTS}/", file=sys.stderr)


if __name__ == '__main__':
    main()
