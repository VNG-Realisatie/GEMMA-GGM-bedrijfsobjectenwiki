#!/usr/bin/env python3
"""BO-dekking: classificeer alle GGM Objecttype-entiteiten als BO, niet-BO, of te-beoordelen."""
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import yaml

BASE_PATH = Path(__file__).resolve().parent.parent
GGM_JSON = BASE_PATH / "Sources/GGM-repository/ggm_parsed.json"
BO_DIR = BASE_PATH / "Wiki/Bedrijfsobjecten"
ONDERWERP_DIR = BASE_PATH / "Wiki/Onderwerpoverzichten"
OUTPUT_JSON = BASE_PATH / "Wiki/Analyses/bo-dekking-data.json"
OUTPUT_MD = BASE_PATH / "Wiki/Analyses/bo-dekking.md"


def extract_frontmatter(content):
    if not content.startswith('---'):
        return {}
    lines = content.split('\n')
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            try:
                return yaml.safe_load('\n'.join(lines[1:i])) or {}
            except Exception:
                return {}
    return {}


def extract_subtypes(content):
    subtypes = set()
    sec = re.search(r'## (?:Subtypes|Specialisaties)\s*\n(.*?)(?=\n##|\Z)', content, re.S)
    if not sec:
        return subtypes
    text = sec.group(1)
    for m in re.finditer(r'\*\*([^*]+?)\*\*', text):
        subtypes.add(m.group(1).strip())
    for m in re.finditer(r'^\|\s*([^|*\-][^|]*?)\s*\|', text, re.M):
        val = m.group(1).strip()
        if val and val.lower() not in ('subtype', 'subtypes', 'naam', 'begrip', '---', ''):
            subtypes.add(val)
    return subtypes


def extract_components(content):
    components = set()
    sec = re.search(r'## GGM-componenten\s*\n(.*?)(?=\n##|\Z)', content, re.S)
    if sec:
        for m in re.finditer(r'\*\*([^*]+?)\*\*', sec.group(1)):
            components.add(m.group(1).strip())
    return components


def extract_parents(content, bo_name):
    parents = set()
    for m in re.finditer(r'specialisatie van\s*\*\*([^*]+?)\*\*', content, re.I):
        p = m.group(1).strip()
        if p and p != bo_name:
            parents.add(p)
    sec = re.search(r'## Relaties\s*\n\n(.*?)(?=\n##|\Z)', content, re.S)
    if sec:
        for m in re.finditer(r'\|\s*generalisatie\s*\|\s*([^|]+?)\s*\|', sec.group(1)):
            p = re.sub(r'\(.*?\)', '', m.group(1)).strip()
            p = re.sub(r'\[\[.*?\|([^\]]+?)\]\]', r'\1', p)
            p = re.sub(r'\[\[(.*?)\]\]', r'\1', p)
            p = re.sub(r'\*\*|\*|`', '', p).strip()
            if p and p != bo_name:
                parents.add(p)
    return parents


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_ggm_data():
    print("Loading GGM data...")
    with open(GGM_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    objecttypes = {}
    for eid, entity in data['entities'].items():
        if entity.get('stereotype') != 'Objecttype':
            continue
        objecttypes[eid] = entity
    print(f"  Objecttype-entiteiten: {len(objecttypes)}")
    return data, objecttypes


def load_bo_pages():
    print("Loading BO pages...")
    bo_guids = {}
    bo_by_name = {}
    parent_map = {}
    subtype_map = {}
    component_map = {}

    for bo_file in BO_DIR.rglob("*.md"):
        if bo_file.name == "index.md":
            continue
        try:
            content = bo_file.read_text(encoding='utf-8')
            fm = extract_frontmatter(content)
            bo_naam = fm.get('naam', bo_file.stem)
            ggm_entiteit = fm.get('ggm_entiteit', '')
            ggm_guid = fm.get('ggm_guid', '')

            rel_path = bo_file.relative_to(BASE_PATH)
            wiki_path = str(rel_path).replace('.md', '')

            if ggm_guid:
                bo_guids[ggm_guid] = {'naam': bo_naam, 'path': wiki_path}
            if ggm_entiteit:
                bo_by_name[ggm_entiteit.lower()] = {'naam': bo_naam, 'path': wiki_path}
            bo_by_name[bo_naam.lower()] = {'naam': bo_naam, 'path': wiki_path}

            for p in extract_parents(content, ggm_entiteit):
                parent_map.setdefault(p, set()).add(ggm_entiteit or bo_naam)
            for st in extract_subtypes(content):
                subtype_map[st] = bo_naam
            for comp in extract_components(content):
                component_map[comp] = bo_naam
        except Exception as e:
            print(f"  Error: {bo_file.name}: {e}")

    print(f"  BO's: {len(bo_guids)}, subtypes: {len(subtype_map)}, componenten: {len(component_map)}")
    return bo_guids, bo_by_name, parent_map, subtype_map, component_map


def load_begrippentabel():
    print("Loading begrippentabel assessments...")
    begrip_bo = {}
    begrip_no_bo = {}

    for ow_file in ONDERWERP_DIR.glob("*.md"):
        try:
            content = ow_file.read_text(encoding='utf-8')
            sec = re.search(r'## Begrippen(?:tabel)?\s*\n(.*?)(?=\n##|\Z)', content, re.S)
            if not sec:
                continue
            for line in sec.group(1).split('\n'):
                if not line.strip().startswith('|') or '---' in line:
                    continue
                cols = [c.strip() for c in line.split('|')]
                if len(cols) < 9:
                    continue
                begrip_raw = cols[1]
                bo_col = cols[4]
                reden = cols[6]
                ggm_col = cols[8]
                if ggm_col.lower().strip() != 'ja':
                    continue
                name = re.sub(r'\[\[.*?\|([^\]]+?)\]\]', r'\1', begrip_raw)
                name = re.sub(r'\[\[(.*?)\]\]', r'\1', name)
                name = re.sub(r'\s*\(GGM\)\s*', '', name)
                name = name.strip()
                if not name:
                    continue
                if '✅' in bo_col:
                    begrip_bo[name.lower()] = reden
                elif '❌' in bo_col:
                    begrip_no_bo[name.lower()] = reden
        except Exception as e:
            print(f"  Error: {ow_file.name}: {e}")

    print(f"  Begrippen GGM=ja: BO={len(begrip_bo)}, niet-BO={len(begrip_no_bo)}")
    return begrip_bo, begrip_no_bo


def build_relation_indices(ggm_data):
    print("Building relation indices...")
    parent_of = {}
    children_of = defaultdict(list)
    agg_whole_of = {}
    assoc_of = defaultdict(list)
    assoc_count = defaultdict(int)

    for rel in ggm_data['relations'].values():
        uml_type = rel.get('uml_type', '')
        src = rel['source_id']
        tgt = rel['target_id']

        if uml_type == 'Generalization':
            parent_of[src] = tgt
            children_of[tgt].append(src)
        elif uml_type == 'Aggregation':
            agg_whole_of[src] = tgt
        elif uml_type == 'Association':
            assoc_count[src] += 1
            assoc_count[tgt] += 1
            assoc_of[src].append({'target': tgt, 'name': rel.get('name', ''),
                                   'source_card': rel.get('source_card', ''),
                                   'target_card': rel.get('target_card', '')})
            assoc_of[tgt].append({'target': src, 'name': rel.get('name', ''),
                                   'source_card': rel.get('target_card', ''),
                                   'target_card': rel.get('source_card', '')})

    print(f"  Generalizations: {len(parent_of)}, Aggregations: {len(agg_whole_of)}, Associations: {sum(assoc_count.values()) // 2}")
    return parent_of, children_of, agg_whole_of, assoc_of, assoc_count


def build_domain_merge(ggm_data, objecttypes):
    """Merge sub-taakvelden into their parent taakveld, matching coverage_analysis.py logic."""
    pkgs = ggm_data['packages']
    ggm_root_id = next(pid for pid, p in pkgs.items()
                       if p['name'] == 'Delfts Gemeentelijk Gegevensmodel')
    top_taakvelden = {pid: p['name'] for pid, p in pkgs.items()
                      if p.get('parent_id') == ggm_root_id}
    sub_to_top = {}
    for top_pid, top_name in top_taakvelden.items():
        for pid, p in pkgs.items():
            if p.get('parent_id') == top_pid and p['name'] not in top_taakvelden.values():
                sub_to_top[p['name']] = top_name

    def merge_key(entity):
        tv = entity.get('taakveld', '(geen)')
        bd = entity.get('beleidsdomein', '(geen)')
        if tv in top_taakvelden.values():
            return (tv, bd)
        elif tv in sub_to_top:
            return (sub_to_top[tv], f"{tv}/{bd}")
        return (tv, bd)

    return merge_key, sub_to_top


# ---------------------------------------------------------------------------
# Classification phases
# ---------------------------------------------------------------------------

def classify_phase1(objecttypes, bo_guids, bo_by_name, parent_map, subtype_map,
                    component_map, begrip_bo, begrip_no_bo):
    """Phase 1: already assessed entities."""
    results = {}

    for eid, entity in objecttypes.items():
        name = entity['name']

        if eid in bo_guids:
            bo_info = bo_guids[eid]
            results[eid] = {
                'status': 'bo',
                'classificatie': 'bo',
                'motivatie': f"[[{bo_info['path']}\\|{bo_info['naam']}]]",
            }
        elif name in parent_map:
            children = sorted(parent_map[name])
            cs = ", ".join(children[:3]) + (", ..." if len(children) > 3 else "")
            results[eid] = {
                'status': 'verwerkt',
                'classificatie': 'generalisatie (wiki)',
                'motivatie': f"generalisatie van {cs}",
            }
        elif name in subtype_map:
            results[eid] = {
                'status': 'verwerkt',
                'classificatie': 'subtype (wiki)',
                'motivatie': f"subtype van {subtype_map[name]}",
            }
        elif name in component_map:
            results[eid] = {
                'status': 'verwerkt',
                'classificatie': 'component (wiki)',
                'motivatie': f"onderdeel van {component_map[name]}",
            }
        elif name.lower() in begrip_no_bo:
            results[eid] = {
                'status': 'niet-bo',
                'classificatie': 'begrippentabel',
                'motivatie': begrip_no_bo[name.lower()],
            }

    return results


def classify_phase2(objecttypes, phase1, parent_of, children_of, agg_whole_of,
                    assoc_count):
    """Phase 2: deterministic structural classification of remaining entities."""
    results = {}
    name_to_ids = defaultdict(list)
    for eid, entity in objecttypes.items():
        name_to_ids[entity['name'].lower()].append(eid)

    for eid, entity in objecttypes.items():
        if eid in phase1:
            continue
        name = entity['name']

        # 2a: Abstract entity
        if entity.get('is_abstract'):
            if eid in children_of:
                child_names = sorted(objecttypes[cid]['name'] for cid in children_of[eid]
                                     if cid in objecttypes)[:3]
                cs = ", ".join(child_names)
                results[eid] = {
                    'status': 'niet-bo',
                    'classificatie': 'abstract',
                    'motivatie': f"abstracte parent van {cs} — geen instanties",
                }
            else:
                results[eid] = {
                    'status': 'niet-bo',
                    'classificatie': 'abstract',
                    'motivatie': "abstract type zonder bekende subtypes",
                }
            continue

        # 2b: Subtype (has parent via generalization)
        if eid in parent_of:
            parent_id = parent_of[eid]
            parent_name = objecttypes[parent_id]['name'] if parent_id in objecttypes else '?'
            # Check if parent is already a BO
            parent_is_bo = parent_id in phase1 and phase1[parent_id]['status'] == 'bo'
            if parent_is_bo:
                results[eid] = {
                    'status': 'niet-bo',
                    'classificatie': 'subtype',
                    'motivatie': f"subtype van {parent_name} (BO) — specialisatie",
                }
            else:
                results[eid] = {
                    'status': 'niet-bo',
                    'classificatie': 'subtype',
                    'motivatie': f"subtype van {parent_name} — erft definitie en attributen",
                }
            continue

        # 2c: Aggregation part
        if eid in agg_whole_of:
            whole_id = agg_whole_of[eid]
            whole_name = objecttypes[whole_id]['name'] if whole_id in objecttypes else '?'
            results[eid] = {
                'status': 'niet-bo',
                'classificatie': 'component',
                'motivatie': f"onderdeel van {whole_name} — compositierelatie",
            }
            continue

        # 2d: Classification entity (name pattern + few attrs)
        attrs = entity.get('attributes', [])
        if re.search(r'(soort|type|status|categorie|classificatie)$', name, re.I) and len(attrs) <= 5:
            base_name = re.sub(r'(soort|type|status|categorie|classificatie)$', '', name, flags=re.I).strip()
            if base_name.lower() in name_to_ids:
                results[eid] = {
                    'status': 'niet-bo',
                    'classificatie': 'classificatie',
                    'motivatie': f"typering bij {base_name} — waardelijst, geen eigen levenscyclus",
                }
                continue

        # 2e: Cross-domain duplicate
        same_name_ids = name_to_ids.get(name.lower(), [])
        if len(same_name_ids) > 1:
            assessed_twin = None
            for twin_id in same_name_ids:
                if twin_id != eid and twin_id in phase1:
                    assessed_twin = twin_id
                    break
            if assessed_twin:
                twin_entity = objecttypes[assessed_twin]
                twin_bd = twin_entity.get('beleidsdomein', '?')
                results[eid] = {
                    'status': 'niet-bo',
                    'classificatie': 'cross-domein',
                    'motivatie': f"duplicaat — al beoordeeld in {twin_bd}",
                }
                continue

    return results


def compute_indicators(eid, entity, parent_of, children_of, agg_whole_of,
                       assoc_of, assoc_count_map, objecttypes):
    """Compute structural indicators for LLM assessment."""
    attrs = entity.get('attributes', [])
    n_assoc = assoc_count_map.get(eid, 0)
    doc = entity.get('documentation', '')
    has_def = bool(doc and len(doc.strip()) > 10)

    assocs = []
    for a in assoc_of.get(eid, []):
        tgt = objecttypes.get(a['target'], {})
        assocs.append({
            'target': tgt.get('name', '?'),
            'cardinality': a.get('target_card', ''),
        })

    is_parent = eid in children_of
    child_names = []
    if is_parent:
        child_names = sorted(objecttypes[cid]['name'] for cid in children_of[eid]
                             if cid in objecttypes)

    # BO-score hint
    if len(attrs) >= 4 and n_assoc >= 2 and has_def:
        hint = 'sterk-kandidaat'
    elif (len(attrs) >= 2 or n_assoc >= 1) and has_def:
        hint = 'kandidaat'
    else:
        hint = 'twijfelgeval'

    return {
        'attribute_count': len(attrs),
        'attributes': attrs[:10],
        'association_count': n_assoc,
        'associations': assocs[:5],
        'has_definition': has_def,
        'definition': doc[:200] if doc else '',
        'is_parent': is_parent,
        'children': child_names,
        'bo_score_hint': hint,
    }


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def taakveld_sort_key(tv):
    m = re.match(r'^(\d+)\s', tv)
    return (0, int(m.group(1)), tv) if m else (1, 999, tv)


def generate_outputs(objecttypes, phase1, phase2, remaining, merge_key):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Generating outputs...")

    # Merge all results
    all_results = {}
    for eid, entity in objecttypes.items():
        name = entity['name']
        tv, bd = merge_key(entity)
        base = {
            'name': name,
            'taakveld': tv,
            'beleidsdomein': bd,
            'ggm_id': eid,
        }

        if eid in phase1:
            base.update(phase1[eid])
        elif eid in phase2:
            base.update(phase2[eid])
        elif eid in remaining:
            base.update({
                'status': 'te-beoordelen',
                'classificatie': remaining[eid]['bo_score_hint'],
                'motivatie': '',
                'indicators': remaining[eid],
            })
        else:
            base.update({
                'status': 'te-beoordelen',
                'classificatie': 'onbekend',
                'motivatie': '',
            })
        all_results[eid] = base

    # Statistics
    stats = defaultdict(int)
    for r in all_results.values():
        stats[r['status']] += 1
    hint_stats = defaultdict(int)
    for r in all_results.values():
        if r['status'] == 'te-beoordelen':
            hint_stats[r.get('classificatie', '?')] += 1

    print(f"\n  Statistieken:")
    print(f"    BO: {stats['bo']}")
    print(f"    Verwerkt (in BO-beschrijving): {stats['verwerkt']}")
    print(f"    Niet-BO: {stats['niet-bo']}")
    print(f"    Te beoordelen: {stats['te-beoordelen']}")
    if hint_stats:
        for h, c in sorted(hint_stats.items()):
            print(f"      - {h}: {c}")

    # Write JSON
    json_output = {
        'generated': now,
        'statistics': {
            'total': len(all_results),
            'bo': stats['bo'],
            'verwerkt': stats['verwerkt'],
            'niet_bo': stats['niet-bo'],
            'te_beoordelen': stats['te-beoordelen'],
            'te_beoordelen_detail': dict(hint_stats),
        },
        'entities': all_results,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(json_output, f, ensure_ascii=False, indent=2)
    print(f"  JSON: {OUTPUT_JSON}")

    # Write Markdown
    lines = []
    lines.append("---")
    lines.append('type: analyse')
    lines.append('titel: "BO-dekking"')
    lines.append(f'datum: {now[:10]}')
    lines.append('aanleiding: "Structurele batch-beoordeling van alle GGM Objecttype-entiteiten"')
    lines.append("---")
    lines.append("")
    lines.append("# BO-dekking")
    lines.append("")
    lines.append(f"**Gegenereerd:** {now}")
    lines.append("")
    lines.append("## Samenvatting")
    lines.append("")
    lines.append("| Categorie | Aantal |")
    lines.append("|---|---|")
    lines.append(f"| BO | {stats['bo']} |")
    lines.append(f"| Verwerkt in BO-beschrijving | {stats['verwerkt']} |")
    lines.append(f"| Niet-BO (met reden) | {stats['niet-bo']} |")
    lines.append(f"| Te beoordelen | {stats['te-beoordelen']} |")
    lines.append(f"| **Totaal** | **{len(all_results)}** |")
    lines.append("")

    if hint_stats:
        lines.append("### Te beoordelen — structurele indicatoren")
        lines.append("")
        lines.append("| Indicatie | Aantal |")
        lines.append("|---|---|")
        for h in ['sterk-kandidaat', 'kandidaat', 'twijfelgeval']:
            if h in hint_stats:
                lines.append(f"| {h} | {hint_stats[h]} |")
        lines.append("")

    # Bronnen-opportuniteiten: group te-beoordelen by beleidsdomein
    domain_open = defaultdict(lambda: {'sterk': 0, 'kandidaat': 0, 'twijfel': 0, 'entities': []})
    for r in all_results.values():
        if r['status'] == 'te-beoordelen':
            key = (r['taakveld'], r['beleidsdomein'])
            hint = r.get('classificatie', '')
            if hint == 'sterk-kandidaat':
                domain_open[key]['sterk'] += 1
            elif hint == 'kandidaat':
                domain_open[key]['kandidaat'] += 1
            else:
                domain_open[key]['twijfel'] += 1
            domain_open[key]['entities'].append(r['name'])

    if domain_open:
        sorted_domains = sorted(domain_open.items(),
                                key=lambda x: -(x[1]['sterk'] + x[1]['kandidaat']))
        lines.append("## Bronnen-opportuniteiten")
        lines.append("")
        lines.append("Beleidsdomeinen met openstaande entiteiten, gesorteerd op aantal BO-kandidaten.")
        lines.append("")
        lines.append("| Taakveld | Beleidsdomein | Sterk | Kandidaat | Twijfel | Entiteiten |")
        lines.append("|---|---|---|---|---|---|")
        for (tv, bd), counts in sorted_domains:
            names = ", ".join(sorted(counts['entities'])[:8])
            if len(counts['entities']) > 8:
                names += f", ... (+{len(counts['entities']) - 8})"
            lines.append(f"| {tv} | {bd} | {counts['sterk']} | {counts['kandidaat']} | {counts['twijfel']} | {names} |")
        lines.append("")

    # Main table: all entities
    lines.append("## Alle entiteiten")
    lines.append("")
    lines.append("| Taakveld | Beleidsdomein | Entiteit | Status | Motivatie |")
    lines.append("|---|---|---|---|---|")

    sorted_entities = sorted(all_results.values(),
                             key=lambda r: (taakveld_sort_key(r['taakveld']),
                                            r['beleidsdomein'], r['name']))
    prev_tv = None
    prev_bd = None
    for r in sorted_entities:
        motivatie = r.get('motivatie', '')
        if not motivatie and r['status'] == 'te-beoordelen':
            hint = r.get('classificatie', '')
            ind = r.get('indicators', {})
            parts = []
            if ind.get('attribute_count', 0) > 0:
                parts.append(f"{ind['attribute_count']} attrs")
            if ind.get('association_count', 0) > 0:
                parts.append(f"{ind['association_count']} relaties")
            if ind.get('has_definition'):
                parts.append("definitie")
            if ind.get('is_parent'):
                parts.append(f"parent van {', '.join(ind.get('children', [])[:2])}")
            motivatie = f"[{hint}] {', '.join(parts)}" if parts else f"[{hint}]"

        tv_col = r['taakveld'] if r['taakveld'] != prev_tv else ""
        bd_col = r['beleidsdomein'] if r['beleidsdomein'] != prev_bd or r['taakveld'] != prev_tv else ""
        prev_tv = r['taakveld']
        prev_bd = r['beleidsdomein']

        lines.append(f"| {tv_col} | {bd_col} | {r['name']} | {r['status']} | {motivatie} |")

    lines.append("")

    OUTPUT_MD.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  Markdown: {OUTPUT_MD}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='BO-dekking: classificeer GGM-entiteiten')
    parser.add_argument('--json-only', action='store_true', help='Schrijf alleen JSON')
    parser.add_argument('--domain', type=str, help='Filter op beleidsdomein')
    args = parser.parse_args()

    ggm_data, objecttypes = load_ggm_data()
    bo_guids, bo_by_name, parent_map, subtype_map, component_map = load_bo_pages()
    begrip_bo, begrip_no_bo = load_begrippentabel()
    parent_of, children_of, agg_whole_of, assoc_of, assoc_count_map = build_relation_indices(ggm_data)
    merge_key, _ = build_domain_merge(ggm_data, objecttypes)

    if args.domain:
        objecttypes = {eid: e for eid, e in objecttypes.items()
                       if args.domain.lower() in e.get('beleidsdomein', '').lower()}
        print(f"Filtered to {len(objecttypes)} entities for domain '{args.domain}'")

    print("\nPhase 1: already assessed...")
    phase1 = classify_phase1(objecttypes, bo_guids, bo_by_name, parent_map,
                             subtype_map, component_map, begrip_bo, begrip_no_bo)
    print(f"  Phase 1: {len(phase1)} entities classified")

    print("Phase 2: structural classification...")
    phase2 = classify_phase2(objecttypes, phase1, parent_of, children_of,
                             agg_whole_of, assoc_count_map)
    print(f"  Phase 2: {len(phase2)} entities classified")

    print("Phase 3: computing indicators for remaining...")
    remaining = {}
    for eid, entity in objecttypes.items():
        if eid not in phase1 and eid not in phase2:
            remaining[eid] = compute_indicators(eid, entity, parent_of, children_of,
                                                agg_whole_of, assoc_of, assoc_count_map,
                                                objecttypes)
    print(f"  Remaining: {len(remaining)} entities need LLM assessment")

    generate_outputs(objecttypes, phase1, phase2, remaining, merge_key)
    print("\nDone!")


if __name__ == '__main__':
    main()
