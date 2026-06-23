#!/usr/bin/env python3
"""GGM-dekkingsanalyse: alle Objecttype-entiteiten, volledige hiërarchie."""
import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import yaml

BASE_PATH = Path(__file__).resolve().parent.parent
GGM_JSON = BASE_PATH / "Sources/GGM-repository/ggm_parsed.json"
BO_DIR = BASE_PATH / "Wiki/Bedrijfsobjecten"
SOURCES_DIR = BASE_PATH / "Wiki/Bronsamenvattingen"
GGM_DIR = BASE_PATH / "Wiki/GGM"
ONDERWERP_DIR = BASE_PATH / "Wiki/Onderwerpoverzichten"
OUTPUT_FILE = BASE_PATH / "Wiki/Analyses/ggm-dekking.md"

print("Loading GGM data...")
with open(GGM_JSON, 'r', encoding='utf-8') as f:
    ggm_data = json.load(f)

pkgs = ggm_data['packages']

ggm_entities = {}
ggm_by_domain = defaultdict(list)
filtered_types = defaultdict(int)

for eid, entity in ggm_data['entities'].items():
    stereotype = entity.get('stereotype', '')
    if stereotype != 'Objecttype':
        label = stereotype if stereotype else "Class (geen stereotype)"
        filtered_types[label] += 1
        continue
    taakveld = entity.get('taakveld', '(geen)')
    beleidsdomein = entity.get('beleidsdomein', '(geen)')
    name = entity.get('name', '')
    ggm_entities[eid] = {'name': name, 'taakveld': taakveld, 'beleidsdomein': beleidsdomein}
    ggm_by_domain[(taakveld, beleidsdomein)].append({'id': eid, 'name': name})

total_all = len(ggm_data['entities'])
print(f"GGM totaal: {total_all}, waarvan {len(ggm_entities)} Objecttype across {len(ggm_by_domain)} beleidsdomeinen")

print("Loading BO pages...")

def extract_frontmatter(content):
    if not content.startswith('---'):
        return {}
    lines = content.split('\n')
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            try:
                return yaml.safe_load('\n'.join(lines[1:i])) or {}
            except:
                return {}
    return {}

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

bo_guids = set()
domain_topics = defaultdict(set)
parent_map = {}
bos_per_topic = defaultdict(int)

for bo_file in BO_DIR.rglob("*.md"):
    if bo_file.name == "index.md":
        continue
    try:
        content = bo_file.read_text(encoding='utf-8')
        fm = extract_frontmatter(content)

        # Tel alle BOs per onderwerp (ongeacht GGM-koppeling)
        domein = fm.get('domein', [])
        if isinstance(domein, list):
            for d in domein:
                bos_per_topic[d] += 1
        elif domein:
            bos_per_topic[str(domein)] += 1

        ggm_guid = fm.get('ggm_guid', '')
        ggm_entiteit = fm.get('ggm_entiteit', '')
        ggm_taakveld = fm.get('ggm_taakveld', '')
        ggm_beleidsdomein = fm.get('ggm_beleidsdomein', '')
        if not (ggm_guid and ggm_taakveld and ggm_beleidsdomein):
            continue
        bo_guids.add(ggm_guid)
        for p in extract_parents(content, ggm_entiteit):
            parent_map.setdefault(p, set()).add(ggm_entiteit)
        dk = (ggm_taakveld, ggm_beleidsdomein)
        if isinstance(domein, list):
            for d in domein:
                domain_topics[dk].add(d)
        elif domein:
            domain_topics[dk].add(str(domein))
    except Exception as e:
        print(f"  Error: {bo_file.name}: {e}")

print(f"Loaded {len(bo_guids)} BO pages, {len(parent_map)} parent entities detected")

print("Building wiki link lookups...")

ggm_page_lookup = {}
for tv_dir in GGM_DIR.iterdir():
    if not tv_dir.is_dir():
        continue
    bd_files = []
    for f in tv_dir.glob("*.md"):
        content = f.read_text(encoding='utf-8')
        fm = extract_frontmatter(content)
        naam = fm.get('naam', '')
        if naam:
            rel = f"Wiki/GGM/{tv_dir.name}/{f.stem}"
            ggm_page_lookup[naam.lower()] = rel
            if fm.get('type') == 'ggm-beleidsdomein':
                bd_files.append((fm, rel))
    if len(bd_files) == 1:
        tv_name = bd_files[0][0].get('taakveld', '')
        if tv_name:
            ggm_page_lookup[tv_name.lower()] = bd_files[0][1]

onderwerp_lookup = {}
for f in ONDERWERP_DIR.glob("*.md"):
    content = f.read_text(encoding='utf-8')
    fm = extract_frontmatter(content)
    naam = fm.get('naam', '')
    if naam:
        onderwerp_lookup[naam.lower()] = f"Wiki/Onderwerpoverzichten/{f.stem}"

print(f"  GGM pages: {len(ggm_page_lookup)}, Onderwerpoverzichten: {len(onderwerp_lookup)}")

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

merged_by_domain = defaultdict(list)
for (tv, bd), entities in ggm_by_domain.items():
    if tv in top_taakvelden.values():
        merged_by_domain[(tv, bd)].extend(entities)
    elif tv in sub_to_top:
        merged_by_domain[(sub_to_top[tv], f"{tv}/{bd}")].extend(entities)
    else:
        merged_by_domain[(tv, bd)].extend(entities)

print("Classifying entities...")

domain_classified = {}
for domain_key, entities in merged_by_domain.items():
    bo, not_bo, not_assessed = [], [], []
    for ent in sorted(entities, key=lambda e: e['name']):
        name = ent['name']
        if ent['id'] in bo_guids:
            bo.append(name)
        elif name in parent_map:
            children = sorted(parent_map[name])
            cs = ", ".join(children[:3]) + (", ..." if len(children) > 3 else "")
            not_bo.append(f"{name} (generalisatie van {cs})")
        else:
            not_assessed.append(name)
    domain_classified[domain_key] = {'bo': bo, 'not_bo': not_bo, 'not_assessed': not_assessed}

merged_topics = defaultdict(set)
for (tv, bd), topics in domain_topics.items():
    if tv in top_taakvelden.values():
        merged_topics[(tv, bd)].update(topics)
    elif tv in sub_to_top:
        merged_topics[(sub_to_top[tv], f"{tv}/{bd}")].update(topics)
    else:
        merged_topics[(tv, bd)].update(topics)

print("Loading source summaries...")
sources_by_topic = defaultdict(int)
for f in SOURCES_DIR.rglob("*.md"):
    if f.name != "index.md":
        sources_by_topic[f.parent.name] += 1

def make_bd_link(display_name):
    leaf = display_name.split('/')[-1] if '/' in display_name else display_name
    path = ggm_page_lookup.get(leaf.lower())
    if path:
        return f"[[{path}\\|{display_name}]]"
    return display_name

def make_onderwerp_link(topic_name):
    path = onderwerp_lookup.get(topic_name.lower())
    if path:
        return f"[[{path}\\|{topic_name}]]"
    return topic_name

def taakveld_sort_key(tv):
    m = re.match(r'^(\d+)\s', tv)
    return (0, int(m.group(1)), tv) if m else (1, 999, tv)

print("Generating report...")

lines = []
lines.append("# GGM-dekkingsanalyse")
lines.append("")
lines.append(f"**Gegenereerd:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
lines.append("")

total = sum(len(v) for v in merged_by_domain.values())
total_bo = sum(len(c['bo']) for c in domain_classified.values())
total_not_bo = sum(len(c['not_bo']) for c in domain_classified.values())
total_not_assessed = sum(len(c['not_assessed']) for c in domain_classified.values())

lines.append("## Samenvattende statistieken")
lines.append("")
lines.append(f"- **Totaal GGM-entiteiten:** {total_all}")
for ft, cnt in sorted(filtered_types.items()):
    lines.append(f"  - {ft}: {cnt} (niet meegeteld)")
lines.append(f"- **Objecttype-entiteiten (in tabellen):** {total}")
lines.append(f"- **Bedrijfsobjecten vastgelegd:** {total_bo}")
lines.append(f"- **Geen bedrijfsobject (generalisaties):** {total_not_bo}")
lines.append(f"- **Entiteiten niet beoordeeld:** {total_not_assessed}")
lines.append("")

lines.append("## Beleidsdomeinen zonder bronnen")
lines.append("")
no_source = []
for dk in sorted(merged_by_domain.keys(), key=lambda x: (taakveld_sort_key(x[0]), x[1])):
    topics = merged_topics.get(dk, set())
    has_sources = any(sources_by_topic.get(t, 0) > 0 for t in topics)
    if not topics or not has_sources:
        no_source.append(f"- {dk[0]} → {dk[1]}")
if no_source:
    lines.extend(no_source)
else:
    lines.append("(Alle beleidsdomeinen hebben bronnen)")
lines.append("")

lines.append("## GGM-entiteitendekking per beleidsdomein")
lines.append("")
lines.append("| Taakveld | Beleidsdomein (aantal entiteiten) | Entiteit is bedrijfsobject | Entiteit is geen bedrijfsobject | Entiteit is niet beoordeeld | Onderwerp (aantal bedrijfsobjecten) |")
lines.append("|---|---|---|---|---|---|")

all_keys = sorted(merged_by_domain.keys(), key=lambda x: (taakveld_sort_key(x[0]), x[1]))

prev_tv = None
for tv, bd in all_keys:
    key = (tv, bd)
    ents = merged_by_domain[key]
    cl = domain_classified[key]

    if tv != prev_tv:
        tv_col = f"**{tv}**"
        prev_tv = tv
    else:
        tv_col = ""

    bd_link = make_bd_link(bd)
    bd_col = f"{bd_link} ({len(ents)})"

    topics = sorted(merged_topics.get(key, set()))
    if topics:
        topic_parts = []
        for t in topics:
            link = make_onderwerp_link(t)
            bo_count = bos_per_topic.get(t, 0)
            topic_parts.append(f"{link} ({bo_count})")
        topic_col = ", ".join(topic_parts)
    else:
        topic_col = "—"

    bo_str = ", ".join(cl['bo']) if cl['bo'] else "—"
    nb_str = "<br>".join(cl['not_bo']) if cl['not_bo'] else "—"
    na_str = ", ".join(cl['not_assessed']) if cl['not_assessed'] else "—"

    lines.append(f"| {tv_col} | {bd_col} | {bo_str} | {nb_str} | {na_str} | {topic_col} |")

lines.append("")

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text('\n'.join(lines), encoding='utf-8')
print(f"Written to {OUTPUT_FILE}")
print("Done!")
