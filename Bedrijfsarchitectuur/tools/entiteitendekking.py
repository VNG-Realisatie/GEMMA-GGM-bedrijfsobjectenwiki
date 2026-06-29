#!/usr/bin/env python3
"""Entiteitendekking: uniforme GGM-analyse per taakveld/beleidsdomein.

Vervangt ggm-vergelijking, ggm-dekking en bo-dekking in één rapport.
Genereert per-taakveld rapporten en een totaaloverzicht.

Usage:
    python entiteitendekking.py --all
    python entiteitendekking.py --taakveld 9
    python entiteitendekking.py --all --dry-run
"""
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import date

BASE_PATH = Path(__file__).resolve().parent.parent
GGM_JSON = BASE_PATH / "Sources/GGM-repository/ggm_parsed.json"
BO_DIR = BASE_PATH / "Wiki/Bedrijfsobjecten"
ONDERWERP_DIR = BASE_PATH / "Wiki/Onderwerpoverzichten"
GGM_WIKI_DIR = BASE_PATH / "Wiki/GGM"
OUTPUT_DIR = BASE_PATH / "Wiki/Analyses/entiteitendekking"


# ── Helpers ──────────────────────────────────────────────────────────────────

def extract_frontmatter(content):
    if not content.startswith('---'):
        return {}
    lines = content.split('\n')
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            try:
                return __import__('yaml').safe_load('\n'.join(lines[1:i])) or {}
            except Exception:
                return {}
    return {}


def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def split_table_row(line):
    placeholder = '\x00'
    safe = line.replace('\\|', placeholder)
    return [c.strip().replace(placeholder, '\\|') for c in safe.split('|')]


def bo_link(info):
    return f"[[{info['path']}\\|{info['naam']}]]"


def ggm_link(entity_name, beleidsdomein, path_map):
    path = path_map.get(beleidsdomein, '')
    return f"[[{path}\\|{entity_name}]]" if path else entity_name


def taakveld_sort_key(tv):
    m = re.match(r'^(\d+)', tv)
    return int(m.group(1)) if m else 999


# ── Data Loading ─────────────────────────────────────────────────────────────

def load_ggm():
    data = json.loads(GGM_JSON.read_text(encoding='utf-8'))
    objecttypes = {eid: e for eid, e in data['entities'].items()
                   if e.get('stereotype') == 'Objecttype'}
    return data, objecttypes


def load_bo_pages():
    """Load all BO pages with metadata including homoniemen."""
    by_guid = {}
    by_name = {}
    all_bos = []

    for f in BO_DIR.rglob("*.md"):
        if f.name == "index.md":
            continue
        content = f.read_text(encoding='utf-8')
        fm = extract_frontmatter(content)
        if fm.get('type') != 'bedrijfsobject':
            continue

        naam = fm.get('naam', f.stem)
        ggm_ent = fm.get('ggm_entiteit', '') or ''
        ggm_guid = fm.get('ggm_guid', '') or ''
        ggm_bd = fm.get('ggm_beleidsdomein', '') or ''
        rel = str(f.relative_to(BASE_PATH)).replace('.md', '')
        grondslag = fm.get('grondslag', '') or ''

        homoniemen = fm.get('bo_homoniemen', []) or []
        is_data_object = grondslag in ('ggm-entiteit', 'ggm-afgeleid', 'procesobject')

        # Derive taakveld from path: Wiki/Bedrijfsobjecten/{taakveld}/{bd}/
        parts = rel.split('/')
        bo_taakveld_slug = parts[2] if len(parts) > 3 else ''

        info = {
            'naam': naam, 'path': rel, 'ggm_entiteit': ggm_ent,
            'ggm_guid': ggm_guid, 'ggm_beleidsdomein': ggm_bd,
            'grondslag': grondslag, 'homoniemen': homoniemen,
            'is_data_object': is_data_object,
            'taakveld_slug': bo_taakveld_slug,
        }

        if ggm_guid:
            by_guid[ggm_guid] = info
        if ggm_ent:
            by_name[ggm_ent.lower()] = info
        by_name[naam.lower()] = info
        all_bos.append(info)

    return by_guid, by_name, all_bos


def load_ggm_path_map():
    path_map = {}
    for f in GGM_WIKI_DIR.rglob("*.md"):
        if f.name == "structuur-ggm.md":
            continue
        content = f.read_text(encoding='utf-8')
        fm = extract_frontmatter(content)
        if fm.get('type') == 'ggm-beleidsdomein':
            path_map[fm.get('naam', '')] = str(f.relative_to(BASE_PATH)).replace('.md', '')
    return path_map


# ── Relationship Graph ───────────────────────────────────────────────────────

class RelationGraph:
    def __init__(self, ggm_data, objecttypes):
        self.gen_parent = {}
        self.gen_children = defaultdict(list)
        self.agg_parent = {}
        self.assoc = defaultdict(list)

        for rel in ggm_data['relations'].values():
            uml = rel.get('uml_type', '')
            src, tgt = rel['source_id'], rel['target_id']
            if src not in objecttypes or tgt not in objecttypes:
                continue
            if uml == 'Generalization':
                self.gen_parent[src] = tgt
                self.gen_children[tgt].append(src)
            elif uml == 'Aggregation':
                self.agg_parent[src] = tgt
                self.assoc[src].append(tgt)
                self.assoc[tgt].append(src)
            elif uml == 'Association':
                self.assoc[src].append(tgt)
                self.assoc[tgt].append(src)

    def descendants_of(self, root_ids):
        found = set()
        queue = list(root_ids)
        while queue:
            cur = queue.pop()
            for child in self.gen_children.get(cur, []):
                if child not in found:
                    found.add(child)
                    queue.append(child)
        return found

    def bfs_to_bo(self, start_id, bo_ids, objecttypes, max_depth=3):
        visited = {start_id}
        queue = [(start_id, [])]
        while queue:
            cur, path = queue.pop(0)
            if len(path) >= max_depth:
                continue
            for tgt in self.assoc.get(cur, []):
                if tgt in visited:
                    continue
                visited.add(tgt)
                name = objecttypes.get(tgt, {}).get('name', '?')
                new_path = path + [name]
                if tgt in bo_ids:
                    return new_path, tgt
                queue.append((tgt, new_path))
        return None


# ── Filtering ────────────────────────────────────────────────────────────────

def find_excluded_ids(objecttypes, graph, bo_by_guid):
    geo_roots = {eid for eid, e in objecttypes.items()
                 if e['name'] in ('Geo-Object', 'GeoObject')}
    geo_desc = graph.descendants_of(geo_roots)
    protected = {eid for eid in geo_desc
                 if objecttypes[eid].get('beleidsdomein') == 'BAG'
                 or eid in bo_by_guid}
    geo_desc -= protected
    tekenwijze = {eid for eid, e in objecttypes.items()
                  if re.match(r'^Objecttype[A-Z]$', e['name'])}
    geo_classifiers = set()
    for eid, e in objecttypes.items():
        if eid in geo_desc or eid in geo_roots:
            continue
        for tgt in graph.assoc.get(eid, []):
            if tgt in geo_desc or tgt in geo_roots:
                if re.match(r'^Soort', e['name']) and len(e.get('attributes', [])) <= 4:
                    geo_classifiers.add(eid)
                    break
    return geo_roots | geo_desc | tekenwijze | geo_classifiers


def deduplicate(entity_ids, objecttypes, bo_by_guid):
    by_name = defaultdict(list)
    for eid in entity_ids:
        by_name[objecttypes[eid]['name'].lower()].append(eid)
    keep = set()
    for eids in by_name.values():
        if len(eids) == 1:
            keep.add(eids[0])
        else:
            matched = [e for e in eids if e in bo_by_guid]
            keep.add(matched[0] if matched else eids[0])
    return keep


# ── Classification ───────────────────────────────────────────────────────────

CLASSIF_PREFIXES = ('Soort', 'Aard', 'Reden', 'Autoriteit')
CLASSIF_SUFFIXES = ('soort', 'type', 'code', 'Code', 'Soort', 'Type')
DETAIL_PATTERNS = (
    'geboorte', 'overlijden', 'naam', 'adres', 'verblijf', 'migratie',
    'nationaliteit', 'verstrekkingsbeperking', 'koopsom', 'locatie',
    'handelsnaam', 'correspondentie', 'splitsingstekening', 'referentie',
    'naamgebruik', 'postadres', 'rekeningnummer', 'briefadres',
    'aanduiding', 'filiatie', 'activiteit',
)
PROCESS_WORDS = ('onderzoek', 'aanmelding', 'verwerking', 'procedure', 'behandeling')
ROLE_SUFFIXES = ('begeleider', 'medewerker', 'functionaris', 'beheerder',
                 'ambtenaar', 'adviseur', 'gever', 'nemer')


def classify_entity(eid, entity, graph, bo_ids, objecttypes):
    """Classify entity and return (entiteitstype, rationale, confidence).

    Rationale explains WHY this classification, not WHAT the entity is.
    """
    name = entity['name']
    attrs = entity.get('attributes', [])
    nl = name.lower()

    if entity.get('is_abstract'):
        children = [objecttypes[c]['name'] for c in graph.gen_children.get(eid, [])
                     if c in objecttypes][:3]
        rat = f"Boventype {', '.join(children)}" if children else "Abstract type"
        return 'abstract', rat, 'high'

    if _is_classification(name, attrs):
        return 'classificatie', 'Typering/referentietabel', 'high'

    if any(w in nl for w in ('ontbinding', 'sluiting', 'regel', 'deel')):
        return 'component', 'Component', 'medium'

    if any(nl.endswith(s) for s in ROLE_SUFFIXES):
        return 'rol', 'Functie/verantwoordelijkheid', 'medium'

    if any(w in nl for w in PROCESS_WORDS):
        return 'proces', 'Proces of processtap', 'medium'

    if any(p in nl for p in DETAIL_PATTERNS):
        return 'detail', 'Detailgegeven', 'high'

    has_bo_neighbor = any(t in bo_ids for t in graph.assoc.get(eid, []))
    if has_bo_neighbor and len(attrs) <= 8:
        return 'detail', 'Detailgegeven (geassocieerd met BO)', 'medium'

    if len(attrs) <= 4:
        return 'detail', 'Detailgegeven (weinig attributen)', 'medium'

    return 'detail', 'Detailgegeven', 'low'


def _is_classification(name, attrs):
    if len(attrs) > 6:
        return False
    if any(name.startswith(p) for p in CLASSIF_PREFIXES):
        return True
    if any(name.endswith(s) for s in CLASSIF_SUFFIXES):
        return True
    al = ' '.join(a.lower() for a in attrs)
    return (('code' in al or 'nummer' in al) and
            ('omschrijving' in al or 'naam' in al) and
            'datum' in al and len(attrs) <= 6)


# ── Relatie tot BO ───────────────────────────────────────────────────────────

def compute_dekking(eid, etype, name, graph, bo_by_guid, bo_by_name, objecttypes):
    """Compute dekking: welk BO dekt deze entiteit structureel?

    Dekkingswaarden (zelfde semantiek als ggm-vergelijking):
    - beschrijft [[BO]]          — direct pad naar BO
    - via X → [[BO]]             — via tussenentiteit naar BO
    - typering [[BO]]            — classificatie-entiteit bij BO
    - ⚠️ geen BO bereikbaar      — geen pad gevonden
    - referentietabel            — classificatie zonder specifiek BO
    - n.v.t.                     — abstract/proces/actor/rol
    """
    if etype in ('abstract', 'proces', 'actor', 'rol', 'meetinstrument', 'cross-cutting'):
        return 'n.v.t.'

    bo_ids = set(bo_by_guid.keys())
    verb = "typering" if etype == 'classificatie' else "beschrijft"

    # 1. Generalization parent → trace to BO
    if eid in graph.gen_parent:
        pid = graph.gen_parent[eid]
        pname = objecttypes.get(pid, {}).get('name', '?')
        if pid in bo_ids:
            return f"{verb} {bo_link(bo_by_guid[pid])}"
        if pid in graph.gen_parent:
            gpid = graph.gen_parent[pid]
            if gpid in bo_ids:
                return f"via {pname} → {bo_link(bo_by_guid[gpid])}"
        for tgt in graph.assoc.get(pid, []):
            if tgt in bo_ids:
                return f"via {pname} → {bo_link(bo_by_guid[tgt])}"

    # 2. Aggregation parent → trace to BO
    if eid in graph.agg_parent:
        wid = graph.agg_parent[eid]
        if wid in bo_ids:
            return f"{verb} {bo_link(bo_by_guid[wid])}"
        wname = objecttypes.get(wid, {}).get('name', '?')
        for tgt in graph.assoc.get(wid, []):
            if tgt in bo_ids:
                return f"via {wname} → {bo_link(bo_by_guid[tgt])}"

    # 3. BFS via all relations
    result = graph.bfs_to_bo(eid, bo_ids, objecttypes)
    if result:
        path, bo_eid = result
        if len(path) == 1:
            return f"{verb} {bo_link(bo_by_guid[bo_eid])}"
        return f"via {path[0]} → {bo_link(bo_by_guid[bo_eid])}"

    # 4. Name-based
    nl = name.lower().replace('-', '').replace(' ', '')
    best, best_len = None, 0
    for key, info in bo_by_name.items():
        kc = key.replace('-', '').replace(' ', '')
        if len(kc) >= 3 and kc in nl and len(kc) > best_len:
            if info.get('ggm_guid') and info['ggm_guid'] in bo_ids:
                best, best_len = info, len(kc)
    if best:
        return f"{verb} {bo_link(best)}"

    # 5. Strip classification prefix
    if etype == 'classificatie':
        for pfx in CLASSIF_PREFIXES:
            if name.startswith(pfx):
                base = name[len(pfx):]
                bo = bo_by_name.get(base.lower())
                if bo and bo.get('ggm_guid') and bo['ggm_guid'] in bo_ids:
                    return f"typering {bo_link(bo)}"
        return 'referentietabel'

    return '⚠️ geen BO bereikbaar'


# ── RSGBPlus Registratie-groepering ──────────────────────────────────────────

RSGB_GROUPS = {
    'BRP': {'burgerzaken', 'ingeschreven', 'huwelijk', 'reisdocument',
            'natuurlijk persoon', 'partij', 'nationaliteit', 'personen',
            'kern:personen', 'gezag', 'mgba'},
    'BRK': {'brk', 'kadastrale', 'kadastraal', 'tenaamstelling', 'zekerheidsrecht',
            'zakelijk recht', 'appartementsrecht', 'appartement'},
    'NHR': {'kvk', 'nhr', 'maatschappelijke activiteit', 'vestiging',
            'niet-natuurlijk persoon'},
    'WOZ': {'woz', 'vastgoed woz'},
}


def classify_rsgb_entity(entity):
    """Classify an RSGBPlus entity into a registratie group."""
    name_lower = entity['name'].lower()
    diagrams = ' '.join(d.lower() for d in (entity.get('diagram_names', []) or []))

    for group, patterns in RSGB_GROUPS.items():
        if any(p in name_lower for p in patterns):
            return group
    for group, patterns in RSGB_GROUPS.items():
        if any(p in diagrams for p in patterns):
            return group
    return 'Overig'


# ── Process Beleidsdomein ────────────────────────────────────────────────────

def load_all_begrippen():
    """Load begrippen from all onderwerpoverzichten, indexed by name."""
    begrip_index = {}
    for f in ONDERWERP_DIR.glob("*.md"):
        content = f.read_text(encoding='utf-8')
        sec = re.search(r'## Begrippen(?:tabel)?\s*\n(.*?)(?=\n## [^#]|\Z)', content, re.S)
        if not sec:
            continue
        col_map = None
        for line in sec.group(1).split('\n'):
            line = line.strip()
            if not line.startswith('|'):
                col_map = None
                continue
            cols = split_table_row(line)
            if len(cols) < 4:
                continue
            if '---' in line and not any('✅' in c or '❌' in c for c in cols):
                continue
            if col_map is None:
                col_map = {}
                for i, c in enumerate(cols):
                    cl = c.lower().strip()
                    if cl == 'begrip':
                        col_map['begrip'] = i
                    elif cl in ('type', 'begripstype'):
                        col_map['type'] = i
                    elif cl.startswith('bo'):
                        col_map['bo'] = i
                    elif cl.startswith('reden'):
                        col_map['reden'] = i
                    elif cl.startswith('ggm'):
                        col_map['ggm'] = i
                continue
            if not col_map or 'begrip' not in col_map:
                continue
            def _c(key):
                idx = col_map.get(key)
                return cols[idx].strip() if idx and idx < len(cols) else ''
            raw = _c('begrip')
            name = re.sub(r'\[\[.*?\\\|([^\]]+?)\]\]', r'\1', raw)
            name = re.sub(r'\[\[.*?\|([^\]]+?)\]\]', r'\1', name)
            name = re.sub(r'\[\[(.*?)\]\]', r'\1', name).strip()
            if name and '❌' in _c('bo'):
                begrip_index[name.lower()] = {
                    'type': _c('type'), 'reden': _c('reden'),
                    'ggm': _c('ggm').lower().strip(),
                }
    return begrip_index


# Begrippen-index (module-level, loaded once)
_begrip_index = None

def get_begrip_index():
    global _begrip_index
    if _begrip_index is None:
        _begrip_index = load_all_begrippen()
    return _begrip_index


BEGRIP_TYPE_MAP = {
    'actor': 'actor', 'rol': 'rol', 'proces': 'proces',
    'classificatie': 'classificatie', 'subtype': 'detail',
    'attribuut': 'detail', 'waarde': 'detail',
    'gebeurtenis': 'detail', 'object': 'detail',
    'governance-instrument': 'detail', 'thema': 'detail',
    'status': 'detail',
}


def process_beleidsdomein(bd_name, entity_ids, objecttypes, graph,
                           bo_by_guid, bo_by_name, all_bos):
    """Process one beleidsdomein: match, classify, compute dekking."""
    bo_matches = []
    geen_match = []
    review_items = []
    bo_ids = set(bo_by_guid.keys())
    begrip_index = get_begrip_index()

    for eid in sorted(entity_ids, key=lambda x: objecttypes[x]['name']):
        e = objecttypes[eid]
        name = e['name']

        # Try BO match
        bo_info = bo_by_guid.get(eid)
        if not bo_info:
            bo_info = bo_by_name.get(name.lower())
            if bo_info and bo_info.get('ggm_guid') and bo_info['ggm_guid'] != eid:
                bo_info = None

        if bo_info:
            etype = '—'
            if bo_info['naam'].lower() != name.lower():
                etype = 'synoniem'

            naamoverlap = ''
            for h in (bo_info.get('homoniemen') or []):
                other = h.get('bedrijfsobject', '')
                if other:
                    naamoverlap = other

            bo_matches.append({
                'ggm_name': name, 'eid': eid,
                'bo_naam': bo_info['naam'], 'bo_path': bo_info['path'],
                'entiteitstype': etype, 'naamoverlap': naamoverlap,
                'beoordeling': 'Exact match' if etype == '—' else f"BO hernoemd: {bo_info['naam']}",
            })
        else:
            etype, rationale, conf = classify_entity(eid, e, graph, bo_ids, objecttypes)

            # Override with begrippentabel if available (handmatig geclassificeerd)
            begrip = begrip_index.get(name.lower())
            if begrip and begrip.get('type'):
                mapped = BEGRIP_TYPE_MAP.get(begrip['type'].lower(), '')
                if mapped:
                    etype = mapped
                    conf = 'high'
                if begrip.get('reden'):
                    rationale = begrip['reden']

            dekking = compute_dekking(eid, etype, name, graph, bo_by_guid, bo_by_name, objecttypes)

            geen_match.append({
                'ggm_name': name, 'eid': eid,
                'entiteitstype': etype, 'dekking': dekking,
                'beoordeling': rationale, 'confidence': conf,
            })

            if conf == 'low':
                review_items.append({
                    'entity': name, 'suggested': etype,
                    'attrs': len(e.get('attributes', [])),
                    'doc': (e.get('documentation', '') or '')[:120],
                })

    match_count = len(bo_matches)
    ondersteunend = sum(1 for g in geen_match if '⚠️' not in g.get('dekking', ''))
    niet_gedekt = sum(1 for g in geen_match if '⚠️' in g.get('dekking', ''))

    return {
        'naam': bd_name,
        'entity_count': len(entity_ids),
        'match_count': match_count,
        'ondersteunend': ondersteunend,
        'niet_gedekt': niet_gedekt,
        'bo_matches': bo_matches,
        'geen_match': geen_match,
        'review': review_items,
    }


# ── Find Hiaten ──────────────────────────────────────────────────────────────

def find_hiaten(all_bos, bo_by_guid):
    """Find BO's without GGM entity match. Group by taakveld_slug."""
    hiaten_by_tv = defaultdict(list)
    for bo in all_bos:
        has_match = bool(bo['ggm_guid']) and bo['ggm_guid'] in bo_by_guid
        if not has_match and not bo['ggm_guid']:
            is_data = bo['grondslag'] in ('ggm-entiteit', 'ggm-afgeleid', '')
            hiaten_by_tv[bo['taakveld_slug']].append({
                'naam': bo['naam'], 'path': bo['path'],
                'grondslag': bo['grondslag'],
                'is_data_object': is_data,
                'status': 'Terugmelding' if is_data else 'Alleen BO',
            })
    return dict(hiaten_by_tv)


# ── Build Taakveld Structure ─────────────────────────────────────────────────

def build_hierarchy_merges(ggm_data):
    """Build merge maps for sub-taakvelden and sub-beleidsdomeinen.

    Returns (tv_merge, bd_merge):
      tv_merge: sub-taakveld name → parent taakveld name
      bd_merge: sub-beleidsdomein name → parent beleidsdomein name
    """
    pkgs = ggm_data['packages']
    ggm_root = next((pid for pid, p in pkgs.items()
                     if 'Gemeentelijk Gegevensmodel' in p['name']), None)
    if not ggm_root:
        return {}, {}

    top = {pid: p['name'] for pid, p in pkgs.items()
           if p.get('parent_id') == ggm_root}

    tv_merge = {}
    bd_merge = {}

    for top_pid, top_name in top.items():
        children = {pid: p['name'] for pid, p in pkgs.items()
                    if p.get('parent_id') == top_pid}
        for child_pid, child_name in children.items():
            if child_name not in top.values():
                tv_merge[child_name] = top_name

            for pid, p in pkgs.items():
                if p.get('parent_id') != child_pid:
                    continue
                bd_merge[p['name']] = child_name

    return tv_merge, bd_merge


def build_taakveld_structure(objecttypes, excluded_ids, bo_by_guid, tv_merge, bd_merge):
    """Group GGM entities by taakveld → beleidsdomein, merging sub-levels."""
    tv_structure = defaultdict(lambda: defaultdict(set))

    for eid, e in objecttypes.items():
        if eid in excluded_ids:
            continue
        tv = e.get('taakveld', '(geen)')
        bd = e.get('beleidsdomein', '(geen)')
        tv = tv_merge.get(tv, tv)
        bd = bd_merge.get(bd, bd)
        tv_structure[tv][bd].add(eid)

    for tv in tv_structure:
        for bd in tv_structure[tv]:
            tv_structure[tv][bd] = deduplicate(tv_structure[tv][bd], objecttypes, bo_by_guid)

    return dict(tv_structure)


# ── Process Taakveld ─────────────────────────────────────────────────────────

def process_taakveld(tv_name, bd_entities, objecttypes, graph,
                      bo_by_guid, bo_by_name, all_bos):
    """Process all beleidsdomeinen within one taakveld."""
    results = {}
    rsgb_sub = None

    for bd_name in sorted(bd_entities.keys()):
        eids = bd_entities[bd_name]
        bd_result = process_beleidsdomein(
            bd_name, eids, objecttypes, graph, bo_by_guid, bo_by_name, all_bos)

        # RSGBPlus: add registratie subgroups
        if bd_name == 'RSGBPlus':
            rsgb_sub = defaultdict(lambda: {'bo_matches': [], 'geen_match': []})
            for entry in bd_result['bo_matches']:
                grp = classify_rsgb_entity(objecttypes[entry['eid']])
                rsgb_sub[grp]['bo_matches'].append(entry)
            for entry in bd_result['geen_match']:
                grp = classify_rsgb_entity(objecttypes[entry['eid']])
                rsgb_sub[grp]['geen_match'].append(entry)
            bd_result['rsgb_subgroups'] = dict(rsgb_sub)

        results[bd_name] = bd_result

    # Totals
    total_entities = sum(r['entity_count'] for r in results.values())
    total_matches = sum(r['match_count'] for r in results.values())
    total_ondersteunend = sum(r['ondersteunend'] for r in results.values())
    total_niet_gedekt = sum(r['niet_gedekt'] for r in results.values())
    total_review = sum(len(r['review']) for r in results.values())

    return {
        'taakveld': tv_name,
        'slug': slugify(tv_name),
        'beleidsdomeinen': results,
        'total_entities': total_entities,
        'total_matches': total_matches,
        'total_ondersteunend': total_ondersteunend,
        'total_niet_gedekt': total_niet_gedekt,
        'total_review': total_review,
    }


# ── Markdown Generation ─────────────────────────────────────────────────────

def generate_taakveld_md(tv_result, hiaten_by_tv, ggm_path_map):
    """Generate per-taakveld report markdown."""
    tv = tv_result['taakveld']
    slug = tv_result['slug']
    bds = tv_result['beleidsdomeinen']
    today = date.today().isoformat()
    tv_hiaten = hiaten_by_tv.get(slug, [])

    total_bo = tv_result['total_matches'] + len(tv_hiaten)
    lines = []

    # Frontmatter
    lines.append('---')
    lines.append('type: analyse')
    lines.append(f'titel: "Entiteitendekking: {tv}"')
    lines.append(f'datum: {today}')
    lines.append(f'taakveld: "{tv}"')
    lines.append('beleidsdomeinen:')
    for bd in sorted(bds.keys()):
        lines.append(f'  - {bd}')
    lines.append(f'totaal_entiteiten: {tv_result["total_entities"]}')
    lines.append(f'totaal_bo: {total_bo}')
    lines.append(f'totaal_matches: {tv_result["total_matches"]}')
    lines.append(f'totaal_hiaten: {len(tv_hiaten)}')
    lines.append('---')
    lines.append('')
    lines.append(f'# Entiteitendekking: {tv}')
    lines.append('')

    # Beoordeling (bovenin)
    lines.append('## Beoordeling')
    lines.append('')
    lines.append('<!-- REVIEW: pas deze beoordeling aan met domeinkennis -->')
    lines.append('')
    gedekt = tv_result['total_matches'] + tv_result['total_ondersteunend']
    pct = round(100 * gedekt / tv_result['total_entities']) if tv_result['total_entities'] else 0
    lines.append(f"{len(bds)} beleidsdomeinen, {tv_result['total_entities']} GGM-entiteiten. "
                 f"Dekking: {gedekt} van {tv_result['total_entities']} ({pct}%) — "
                 f"{tv_result['total_matches']} met BO, "
                 f"{tv_result['total_ondersteunend']} ondersteunend, "
                 f"{tv_result['total_niet_gedekt']} niet gedekt. "
                 f"{len(tv_hiaten)} BO's zonder GGM-entiteit.")
    lines.append('')

    # Type stats across all bds
    type_counts = defaultdict(int)
    for bd_r in bds.values():
        for g in bd_r['geen_match']:
            type_counts[g['entiteitstype']] += 1
    if type_counts:
        parts = ', '.join(f'{c}× {t}' for t, c in sorted(type_counts.items()))
        lines.append(f'Niet-BO entiteiten: {parts}.')
    lines.append('')

    # Per beleidsdomein
    for bd_name in sorted(bds.keys()):
        bd_r = bds[bd_name]
        lines.append(f'## {bd_name}')
        lines.append('')
        lines.append(f'{bd_r["entity_count"]} entiteiten, '
                     f'{bd_r["match_count"]} Entiteiten met BO.')
        lines.append('')

        # RSGBPlus: subsecties
        if 'rsgb_subgroups' in bd_r:
            _write_rsgb_sections(lines, bd_r, ggm_path_map, bd_name)
        else:
            _write_bd_tables(lines, bd_r, ggm_path_map, bd_name)

    # BO's zonder GGM-entiteit
    if tv_hiaten:
        lines.append('## BO\'s zonder GGM-entiteit')
        lines.append('')
        lines.append('BO\'s waarvoor geen overeenkomstige GGM-entiteit bestaat. '
                     'Data-objecten worden als hiaat teruggemeld aan het GGM-team; '
                     'overige BO\'s bestaan alleen in GEMMA.')
        lines.append('')
        lines.append('| BO | Data-object | Grondslag | Status |')
        lines.append('|---|---|---|---|')
        for h in sorted(tv_hiaten, key=lambda x: x['naam']):
            link = f"[[{h['path']}\\|{h['naam']}]]"
            is_do = 'ja' if h['is_data_object'] else 'nee'
            status = 'Terugmelding' if h['is_data_object'] else 'Alleen GEMMA-BO'
            lines.append(f"| {link} | {is_do} | {h['grondslag']} | **{status}** |")
        lines.append('')

    return '\n'.join(lines)


def _write_bd_tables(lines, bd_r, pm, bd_name):
    """Write Entiteiten met BO + Geen BO-match tables for a beleidsdomein."""
    if bd_r['bo_matches']:
        lines.append('### Entiteiten met BO')
        lines.append('')
        lines.append('| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |')
        lines.append('|---|---|---|---|---|')
        for m in bd_r['bo_matches']:
            gl = ggm_link(m['ggm_name'], bd_name, pm)
            bl = f"[[{m['bo_path']}\\|{m['bo_naam']}]] ✅"
            lines.append(f"| {gl} | {bl} | {m['entiteitstype']} | {m['naamoverlap']} | {m['beoordeling']} |")
        lines.append('')

    if bd_r['geen_match']:
        lines.append('### Entiteiten zonder BO')
        lines.append('')
        lines.append('| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |')
        lines.append('|---|---|---|---|')
        for g in sorted(bd_r['geen_match'], key=lambda x: (x['entiteitstype'], x['ggm_name'])):
            gl = ggm_link(g['ggm_name'], bd_name, pm)
            lines.append(f"| {gl} | {g['entiteitstype']} | {g['dekking']} | {g['beoordeling']} |")
        lines.append('')


def _write_rsgb_sections(lines, bd_r, pm, bd_name):
    """Write RSGBPlus with subsecties per registratie."""
    groups = bd_r['rsgb_subgroups']
    order = ['BRP', 'BRK', 'NHR', 'WOZ', 'Overig']
    labels = {
        'BRP': 'BRP — personen en burgerzaken',
        'BRK': 'BRK — kadaster en rechten',
        'NHR': 'NHR — handelsregister',
        'WOZ': 'WOZ — waardering onroerende zaken',
        'Overig': 'Overig — generiek en RSGB-uitbreidingen',
    }

    for grp in order:
        if grp not in groups:
            continue
        data = groups[grp]
        if not data['bo_matches'] and not data['geen_match']:
            continue

        lines.append(f"### {labels.get(grp, grp)}")
        lines.append('')

        if data['bo_matches']:
            lines.append('| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |')
            lines.append('|---|---|---|---|---|')
            for m in data['bo_matches']:
                gl = ggm_link(m['ggm_name'], bd_name, pm)
                bl = f"[[{m['bo_path']}\\|{m['bo_naam']}]] ✅"
                lines.append(f"| {gl} | {bl} | {m['entiteitstype']} | {m['naamoverlap']} | {m['beoordeling']} |")
            lines.append('')

        if data['geen_match']:
            lines.append('**Entiteiten zonder BO:**')
            lines.append('')
            lines.append('| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |')
            lines.append('|---|---|---|---|')
            for g in sorted(data['geen_match'], key=lambda x: (x['entiteitstype'], x['ggm_name'])):
                gl = ggm_link(g['ggm_name'], bd_name, pm)
                lines.append(f"| {gl} | {g['entiteitstype']} | {g['dekking']} | {g['beoordeling']} |")
            lines.append('')


# ── Totaaloverzicht ──────────────────────────────────────────────────────────

def generate_totaaloverzicht(all_tv_results, hiaten_by_tv):
    today = date.today().isoformat()
    total_ent = sum(r['total_entities'] for r in all_tv_results.values())
    total_match = sum(r['total_matches'] for r in all_tv_results.values())
    total_hiaten = sum(len(h) for h in hiaten_by_tv.values())

    lines = []
    lines.append('---')
    lines.append('type: analyse')
    lines.append('titel: "Entiteitendekking — totaaloverzicht"')
    lines.append(f'datum: {today}')
    lines.append('---')
    lines.append('')
    lines.append('# Entiteitendekking — totaaloverzicht')
    lines.append('')
    total_ondersteunend = sum(r['total_ondersteunend'] for r in all_tv_results.values())
    total_niet_gedekt = sum(r['total_niet_gedekt'] for r in all_tv_results.values())
    total_gedekt = total_match + total_ondersteunend
    pct_all = round(100 * total_gedekt / total_ent) if total_ent else 0
    lines.append(f"{total_ent} GGM-entiteiten. Dekking: {total_gedekt} gedekt ({pct_all}%), "
                 f"{total_niet_gedekt} niet gedekt. {total_hiaten} BO's zonder GGM-entiteit.")
    lines.append('')
    lines.append("| Taakveld | Beleidsdomein | GGM-entiteiten | Entiteiten met BO "
                 "| Entiteiten ondersteunend aan BO | Niet gedekt | Dekking "
                 "| BO zonder GGM-entiteit |")
    lines.append('|---|---|---|---|---|---|---|---|')

    for tv_name in sorted(all_tv_results.keys(), key=taakveld_sort_key):
        tv_r = all_tv_results[tv_name]
        slug = tv_r['slug']
        tv_hiaten = hiaten_by_tv.get(slug, [])
        first_bd = True

        rapport = f"[[Wiki/Analyses/entiteitendekking/{slug}\\|{tv_name}]]"

        for bd_name in sorted(tv_r['beleidsdomeinen'].keys()):
            bd_r = tv_r['beleidsdomeinen'][bd_name]
            tv_col = f"**{rapport}**" if first_bd else ""
            first_bd = False
            total = bd_r['entity_count']
            gedekt = bd_r['match_count'] + bd_r['ondersteunend']
            pct = f"{round(100 * gedekt / total)}%" if total else "—"
            lines.append(
                f"| {tv_col} | {bd_name} | {total} | {bd_r['match_count']} "
                f"| {bd_r['ondersteunend']} | {bd_r['niet_gedekt']} | {pct} "
                f"| |"
            )

        if tv_hiaten:
            tv_col = f"**{rapport}**" if not tv_r['beleidsdomeinen'] else ""
            lines.append(
                f"| {tv_col} | | | | | | | {len(tv_hiaten)} |"
            )

    lines.append('')
    return '\n'.join(lines)


# ── Review Summary ───────────────────────────────────────────────────────────

def generate_review(all_tv_results):
    total_review = sum(r['total_review'] for r in all_tv_results.values())
    lines = []
    lines.append(f'# Entiteitendekking review — {date.today().isoformat()}')
    lines.append('')
    lines.append(f'Totaal review-items: {total_review}.')
    lines.append('')

    lines.append('## Samenvatting')
    lines.append('')
    lines.append('| Taakveld | GGM | Entiteiten met BO | Review |')
    lines.append('|---|---|---|---|')
    for tv in sorted(all_tv_results.keys(), key=taakveld_sort_key):
        r = all_tv_results[tv]
        lines.append(f"| {tv} | {r['total_entities']} | {r['total_matches']} | {r['total_review']} |")
    lines.append('')

    # Review items
    any_review = False
    for tv in sorted(all_tv_results.keys(), key=taakveld_sort_key):
        for bd_name, bd_r in sorted(all_tv_results[tv]['beleidsdomeinen'].items()):
            if not bd_r['review']:
                continue
            if not any_review:
                lines.append('## Items voor review')
                lines.append('')
                any_review = True
            lines.append(f'### {tv} — {bd_name}')
            lines.append('')
            for item in bd_r['review']:
                lines.append(
                    f"- **{item['entity']}** → {item['suggested']} "
                    f"({item['attrs']} attrs). {item['doc']}"
                )
            lines.append('')

    return '\n'.join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Entiteitendekking: GGM-analyse per taakveld')
    parser.add_argument('--taakveld', type=str, help='Filter op taakveld (nummer of naam)')
    parser.add_argument('--all', action='store_true', help='Alle taakvelden')
    parser.add_argument('--dry-run', action='store_true', help='Alleen counts tonen')
    args = parser.parse_args()

    if not args.taakveld and not args.all:
        parser.error('Specify --taakveld or --all')

    print("Loading data...")
    ggm_data, objecttypes = load_ggm()
    bo_by_guid, bo_by_name, all_bos = load_bo_pages()
    ggm_path_map = load_ggm_path_map()
    graph = RelationGraph(ggm_data, objecttypes)
    excluded_ids = find_excluded_ids(objecttypes, graph, bo_by_guid)

    print(f"  GGM: {len(objecttypes)} Objecttype, {len(bo_by_guid)} BO's, "
          f"{len(excluded_ids)} excluded")

    tv_merge, bd_merge = build_hierarchy_merges(ggm_data)
    tv_structure = build_taakveld_structure(objecttypes, excluded_ids, bo_by_guid, tv_merge, bd_merge)
    hiaten_by_tv = find_hiaten(all_bos, bo_by_guid)

    # Filter if --taakveld
    if args.taakveld:
        filtered = {}
        for tv in tv_structure:
            if args.taakveld in tv or args.taakveld == slugify(tv):
                filtered[tv] = tv_structure[tv]
        tv_structure = filtered

    all_tv_results = {}
    for tv_name in sorted(tv_structure.keys(), key=taakveld_sort_key):
        bd_entities = tv_structure[tv_name]
        tv_result = process_taakveld(
            tv_name, bd_entities, objecttypes, graph,
            bo_by_guid, bo_by_name, all_bos)

        all_tv_results[tv_name] = tv_result
        slug = tv_result['slug']
        tv_hiaten = hiaten_by_tv.get(slug, [])

        bd_summary = ', '.join(
            f"{bd}({r['match_count']})" for bd, r in sorted(tv_result['beleidsdomeinen'].items()))
        print(f"  {tv_name}: {tv_result['total_entities']} ent, "
              f"{tv_result['total_matches']} matches, "
              f"{len(tv_hiaten)} hiaten, {tv_result['total_review']} review "
              f"[{bd_summary}]")

        if not args.dry_run:
            md = generate_taakveld_md(tv_result, hiaten_by_tv, ggm_path_map)
            out = OUTPUT_DIR / f"{slug}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding='utf-8')

    if not args.dry_run and all_tv_results:
        overview = generate_totaaloverzicht(all_tv_results, hiaten_by_tv)
        (OUTPUT_DIR / "totaaloverzicht.md").write_text(overview, encoding='utf-8')

        review = generate_review(all_tv_results)
        (OUTPUT_DIR / "review.md").write_text(review, encoding='utf-8')

        print(f"\nOutput: {OUTPUT_DIR}/")

    total_ent = sum(r['total_entities'] for r in all_tv_results.values())
    total_match = sum(r['total_matches'] for r in all_tv_results.values())
    total_review = sum(r['total_review'] for r in all_tv_results.values())
    print(f"\nDone: {len(all_tv_results)} taakvelden, "
          f"{total_ent} entiteiten, {total_match} matches, "
          f"{total_review} review-items")


if __name__ == '__main__':
    main()
