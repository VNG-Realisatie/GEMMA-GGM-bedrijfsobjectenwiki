#!/usr/bin/env python3
"""GGM-vergelijking prep: pre-process matching and classification for all onderwerpen.

Generates draft analysis pages and a compact review summary so the LLM only
needs to review edge cases and write beoordeling sections.

Usage:
    python ggm_vergelijking_prep.py --all              # all onderwerpen
    python ggm_vergelijking_prep.py --onderwerp financien
    python ggm_vergelijking_prep.py --all --dry-run     # preview counts only
"""
import json
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import date

BASE_PATH = Path(__file__).resolve().parent.parent
GGM_JSON = BASE_PATH / "Sources/GGM-repository/ggm_parsed.json"
BO_DIR = BASE_PATH / "Wiki/Bedrijfsobjecten"
ONDERWERP_DIR = BASE_PATH / "Wiki/Onderwerpoverzichten"
GGM_WIKI_DIR = BASE_PATH / "Wiki/GGM"
OUTPUT_DIR = BASE_PATH / "Wiki/Analyses/ggm-vergelijking"
OVERVIEW_PATH = BASE_PATH / "Wiki/Analyses/ggm-vergelijkingen.md"


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


def extract_begrip_name(raw):
    name = re.sub(r'\[\[.*?\\\|([^\]]+?)\]\]', r'\1', raw)
    name = re.sub(r'\[\[.*?\|([^\]]+?)\]\]', r'\1', name)
    name = re.sub(r'\[\[(.*?)\]\]', r'\1', name)
    return name.strip()


def extract_begrip_link(raw):
    m = re.search(r'\[\[(Wiki/Bedrijfsobjecten/[^\]\\|]+)', raw)
    return m.group(1) if m else None


def split_table_row(line):
    """Split markdown table row, respecting \\| inside [[wiki-links]]."""
    placeholder = '\x00'
    safe = line.replace('\\|', placeholder)
    return [c.strip().replace(placeholder, '\\|') for c in safe.split('|')]


# ── Data Loading ─────────────────────────────────────────────────────────────

def load_ggm():
    data = json.loads(GGM_JSON.read_text(encoding='utf-8'))
    objecttypes = {eid: e for eid, e in data['entities'].items()
                   if e.get('stereotype') == 'Objecttype'}
    return data, objecttypes


def load_bo_pages():
    """Returns bo_by_guid, bo_by_ggm_name, bo_by_onderwerp."""
    bo_by_guid = {}
    bo_by_ggm_name = {}
    bo_by_onderwerp = defaultdict(list)

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

        info = {'naam': naam, 'path': rel, 'ggm_entiteit': ggm_ent,
                'ggm_guid': ggm_guid, 'ggm_beleidsdomein': ggm_bd,
                'grondslag': fm.get('grondslag', '')}

        if ggm_guid:
            bo_by_guid[ggm_guid] = info
        if ggm_ent:
            bo_by_ggm_name[ggm_ent.lower()] = info
        bo_by_ggm_name[naam.lower()] = info

        onderwerpen = fm.get('onderwerp', fm.get('domein', []))
        if isinstance(onderwerpen, str):
            onderwerpen = [onderwerpen]
        for ow in (onderwerpen or []):
            bo_by_onderwerp[slugify(ow)].append(info)

    return bo_by_guid, bo_by_ggm_name, bo_by_onderwerp


def load_ggm_path_map():
    """Map beleidsdomein name → Wiki/GGM/... path (without .md)."""
    path_map = {}
    for f in GGM_WIKI_DIR.rglob("*.md"):
        if f.name == "structuur-ggm.md":
            continue
        content = f.read_text(encoding='utf-8')
        fm = extract_frontmatter(content)
        if fm.get('type') == 'ggm-beleidsdomein':
            path_map[fm.get('naam', '')] = str(f.relative_to(BASE_PATH)).replace('.md', '')
    return path_map


def parse_begrippentabel(onderwerp_slug):
    """Parse begrippentabel from onderwerpoverzicht. Returns list of dicts."""
    path = ONDERWERP_DIR / f"{onderwerp_slug}.md"
    if not path.exists():
        return []
    content = path.read_text(encoding='utf-8')

    sec = re.search(r'## Begrippen(?:tabel)?\s*\n(.*?)(?=\n## [^#]|\Z)', content, re.S)
    if not sec:
        return []

    begrippen = []
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
                elif cl.startswith('registratie'):
                    col_map['registratie'] = i
                elif cl.startswith('omschrijving'):
                    col_map['omschrijving'] = i
                elif cl.startswith('bo'):
                    col_map['bo'] = i
                elif cl.startswith('reden'):
                    col_map['reden'] = i
                elif cl.startswith('ggm'):
                    col_map['ggm'] = i
            continue

        if col_map is None or 'begrip' not in col_map:
            continue

        def _col(key):
            idx = col_map.get(key)
            return cols[idx].strip() if idx is not None and idx < len(cols) else ''

        raw = _col('begrip')
        name = extract_begrip_name(raw)
        if not name:
            continue

        begrippen.append({
            'naam': name,
            'raw': raw,
            'bo_link': extract_begrip_link(raw),
            'type': _col('type'),
            'registratie': _col('registratie'),
            'omschrijving': _col('omschrijving'),
            'is_bo': '✅' in _col('bo'),
            'reden': _col('reden'),
            'ggm': _col('ggm').lower().strip(),
        })

    return begrippen


# ── Relationship Graph ───────────────────────────────────────────────────────

class RelationGraph:
    def __init__(self, ggm_data, objecttypes):
        self.parent_of = {}      # child_id → parent_id (generalization)
        self.children_of = defaultdict(list)
        self.assoc_of = defaultdict(list)  # id → [{target, name, card}]

        for rel in ggm_data['relations'].values():
            uml = rel.get('uml_type', '')
            src, tgt = rel['source_id'], rel['target_id']
            if src not in objecttypes or tgt not in objecttypes:
                continue
            if uml == 'Generalization':
                self.parent_of[src] = tgt
                self.children_of[tgt].append(src)
            elif uml in ('Association', 'Aggregation'):
                self.assoc_of[src].append(tgt)
                self.assoc_of[tgt].append(src)

    def descendants_of(self, root_ids):
        found = set()
        queue = list(root_ids)
        while queue:
            cur = queue.pop()
            for child in self.children_of.get(cur, []):
                if child not in found:
                    found.add(child)
                    queue.append(child)
        return found

    def find_path_to_bo(self, start_id, bo_ids, objecttypes, max_depth=3):
        """BFS from start to nearest BO. Returns (path, bo_info) or None."""
        visited = {start_id}
        queue = [(start_id, [])]
        while queue:
            cur, path = queue.pop(0)
            if len(path) >= max_depth:
                continue
            for tgt in self.assoc_of.get(cur, []):
                if tgt in visited:
                    continue
                visited.add(tgt)
                tgt_name = objecttypes.get(tgt, {}).get('name', '?')
                new_path = path + [tgt_name]
                if tgt in bo_ids:
                    return new_path, tgt
                queue.append((tgt, new_path))
        return None


# ── IMGeo/BGT & Tekenwijze Filtering ────────────────────────────────────────

def find_excluded_ids(objecttypes, graph, bo_by_guid):
    """Identify IMGeo/BGT entities and tekenwijze to exclude from analyses.

    Geo-Object descendants are IMGeo/BGT, BUT BAG entities (Pand, Ligplaats,
    etc.) also inherit from Geo-Object. We protect BAG-domain entities and
    any entity that has a BO match.
    """
    geo_roots = {eid for eid, e in objecttypes.items()
                 if e['name'] in ('Geo-Object', 'GeoObject')}
    geo_descendants = graph.descendants_of(geo_roots)

    protected = {eid for eid in geo_descendants
                 if objecttypes[eid].get('beleidsdomein') == 'BAG'
                 or eid in bo_by_guid}
    geo_descendants -= protected

    tekenwijze = {eid for eid, e in objecttypes.items()
                  if re.match(r'^Objecttype[A-Z]$', e['name'])}

    geo_classifiers = set()
    for eid, e in objecttypes.items():
        if eid in geo_descendants or eid in geo_roots:
            continue
        for tgt in graph.assoc_of.get(eid, []):
            if tgt in geo_descendants or tgt in geo_roots:
                if re.match(r'^Soort', e['name']) and len(e.get('attributes', [])) <= 4:
                    geo_classifiers.add(eid)
                    break

    excluded = geo_roots | geo_descendants | tekenwijze | geo_classifiers
    return excluded


# ── Scope Determination ──────────────────────────────────────────────────────

def determine_scope(onderwerp_slug, bo_by_onderwerp, objecttypes, excluded_ids,
                     begrippen, bo_by_ggm_name):
    """Determine which beleidsdomeinen and entity IDs are in scope.

    Uses both BO onderwerp-tags AND begrippentabel wiki-links to find
    all relevant BO's (handles cases like WOZ tagged as 'Belastingen').
    """
    bo_list = list(bo_by_onderwerp.get(onderwerp_slug, []))

    seen_names = {b['naam'].lower() for b in bo_list}
    for b in begrippen:
        if b['is_bo']:
            bo_info = bo_by_ggm_name.get(b['naam'].lower())
            if bo_info and bo_info['naam'].lower() not in seen_names:
                bo_list.append(bo_info)
                seen_names.add(bo_info['naam'].lower())

    beleidsdomeinen = set()
    for bo in bo_list:
        bd = bo.get('ggm_beleidsdomein', '')
        if bd:
            beleidsdomeinen.add(bd)

    scope_ids = set()
    for eid, e in objecttypes.items():
        if eid in excluded_ids:
            continue
        if e.get('beleidsdomein', '') in beleidsdomeinen:
            scope_ids.add(eid)

    return beleidsdomeinen, scope_ids


# ── Deduplication ────────────────────────────────────────────────────────────

def deduplicate(scope_ids, objecttypes, bo_by_guid):
    """Remove duplicate entities (same name, keep the one with BO match)."""
    by_name = defaultdict(list)
    for eid in scope_ids:
        name = objecttypes[eid]['name']
        by_name[name.lower()].append(eid)

    keep = set()
    for name_lower, eids in by_name.items():
        if len(eids) == 1:
            keep.add(eids[0])
            continue
        matched = [eid for eid in eids if eid in bo_by_guid]
        if matched:
            keep.add(matched[0])
        else:
            keep.add(eids[0])

    return keep


# ── Matching ─────────────────────────────────────────────────────────────────

def match_entities(scope_ids, objecttypes, bo_by_guid, bo_by_ggm_name, begrippen):
    """Match GGM entities to BO's and bronbegrippen.

    Returns:
        tabel1: list of matched entries
        tabel2_ids: set of unmatched entity IDs
        tabel3: list of BO's without GGM match
    """
    begrip_by_name = {}
    for b in begrippen:
        begrip_by_name[b['naam'].lower()] = b

    tabel1 = []
    matched_ids = set()

    for eid in sorted(scope_ids, key=lambda x: objecttypes[x]['name']):
        e = objecttypes[eid]
        name = e['name']
        bd = e.get('beleidsdomein', '')

        bo_info = bo_by_guid.get(eid)
        if not bo_info:
            bo_info = bo_by_ggm_name.get(name.lower())
            if bo_info and bo_info.get('ggm_guid') and bo_info['ggm_guid'] != eid:
                bo_info = None

        begrip = begrip_by_name.get(name.lower())

        if bo_info:
            entry_type = '—'
            bo_naam = bo_info['naam']
            if bo_naam.lower() != name.lower():
                entry_type = 'synoniem'
            tabel1.append({
                'ggm_name': name, 'beleidsdomein': bd, 'eid': eid,
                'match_type': 'bo', 'bo_naam': bo_naam,
                'bo_path': bo_info['path'], 'entiteitstype': entry_type,
                'beoordeling': begrip.get('reden', 'Exact match') if begrip else 'Exact match',
            })
            matched_ids.add(eid)
        elif begrip and begrip['ggm'].startswith('ja'):
            etype = _begrip_to_entiteitstype(begrip, e)
            tabel1.append({
                'ggm_name': name, 'beleidsdomein': bd, 'eid': eid,
                'match_type': 'begrip', 'begrip_naam': begrip['naam'],
                'is_bo': begrip['is_bo'], 'entiteitstype': etype,
                'beoordeling': begrip.get('reden', ''),
                'bo_path': begrip.get('bo_link', ''),
            })
            matched_ids.add(eid)

    tabel2_ids = scope_ids - matched_ids

    bo_hiaten = []
    for b in begrippen:
        if not b['is_bo']:
            continue
        has_match = any(t.get('bo_naam', '').lower() == b['naam'].lower() or
                        t.get('begrip_naam', '').lower() == b['naam'].lower()
                        for t in tabel1)
        if not has_match:
            bo_hiaten.append(b)

    return tabel1, tabel2_ids, bo_hiaten


def _begrip_to_entiteitstype(begrip, entity):
    t = begrip.get('type', '').lower()
    if t in ('attribuut', 'waarde', 'gebeurtenis'):
        return 'detail'
    if t in ('classificatie',):
        return 'classificatie'
    if t in ('subtype',):
        return 'abstract'
    if t in ('actor',):
        return 'actor'
    if t in ('rol',):
        return 'rol'
    if entity.get('is_abstract'):
        return 'abstract'
    return 'detail'


# ── Entity Type Classification ───────────────────────────────────────────────

CLASSIF_PREFIXES = ('Soort', 'Aard', 'Reden', 'Autoriteit')
CLASSIF_SUFFIXES = ('soort', 'type', 'code', 'Code', 'Soort', 'Type')

PROCESS_WORDS = ('onderzoek', 'aanmelding', 'verwerking', 'procedure',
                 'behandeling')

ROLE_SUFFIXES = ('begeleider', 'medewerker', 'functionaris', 'beheerder',
                 'ambtenaar', 'adviseur', 'gever', 'nemer')

DETAIL_PATTERNS = (
    'geboorte', 'overlijden', 'naam', 'adres', 'verblijf', 'migratie',
    'nationaliteit', 'verstrekkingsbeperking', 'koopsom', 'locatie',
    'handelsnaam', 'correspondentie', 'splitsingstekening', 'referentie',
    'naamgebruik', 'postadres', 'rekeningnummer', 'briefadres',
    'aanduiding', 'filiatie', 'activiteit',
)


def classify_entity(eid, entity, graph, bo_ids, objecttypes, scope_bds):
    """Classify an unmatched GGM entity. Returns (entiteitstype, beoordeling, confidence)."""
    name = entity['name']
    attrs = entity.get('attributes', [])
    doc = entity.get('documentation', '') or ''
    name_lower = name.lower()

    if entity.get('is_abstract'):
        children = [objecttypes[c]['name'] for c in graph.children_of.get(eid, [])
                     if c in objecttypes][:3]
        desc = f"Boventype {', '.join(children)}" if children else "Abstract type"
        return 'abstract', desc, 'high'

    if _is_classification(name, attrs):
        return 'classificatie', _classification_desc(name), 'high'

    if _is_component(name, doc):
        return 'component', 'Component', 'medium'

    if any(name_lower.endswith(s) for s in ROLE_SUFFIXES):
        return 'rol', 'Functie/verantwoordelijkheid', 'medium'

    if any(w in name_lower for w in PROCESS_WORDS):
        return 'proces', 'Proces of processtap', 'medium'

    # Detail with known pattern → high confidence
    if any(p in name_lower for p in DETAIL_PATTERNS):
        return 'detail', 'Detailgegeven', 'high'

    # Detail with few attributes and association to BO → medium
    has_bo_neighbor = any(t in bo_ids for t in graph.assoc_of.get(eid, []))
    if has_bo_neighbor and len(attrs) <= 8:
        return 'detail', 'Detailgegeven (geassocieerd met BO)', 'medium'

    # Few attributes, likely detail → medium
    if len(attrs) <= 4:
        return 'detail', 'Detailgegeven (weinig attributen)', 'medium'

    # Ambiguous — needs review
    return 'detail', 'Detailgegeven', 'low'


def _is_classification(name, attrs):
    if len(attrs) > 6:
        return False
    if any(name.startswith(p) for p in CLASSIF_PREFIXES):
        return True
    if any(name.endswith(s) for s in CLASSIF_SUFFIXES):
        return True
    attr_lower = ' '.join(a.lower() for a in attrs)
    if ('code' in attr_lower or 'nummer' in attr_lower) and \
       ('omschrijving' in attr_lower or 'naam' in attr_lower) and \
       'datum' in attr_lower and len(attrs) <= 6:
        return True
    return False


def _classification_desc(name):
    for p in CLASSIF_PREFIXES:
        if name.startswith(p):
            base = name[len(p):]
            return f"Typering/referentietabel ({base})"
    return "Typering/referentietabel"


def _is_component(name, doc):
    component_words = ('ontbinding', 'sluiting', 'regel', 'deel')
    return any(w in name.lower() for w in component_words)


# ── Dekking Chain ────────────────────────────────────────────────────────────

def compute_dekking(eid, entiteitstype, entity_name, graph, bo_by_guid,
                     bo_by_ggm_name, objecttypes):
    """Compute dekking string for an unmatched entity.

    Uses three strategies:
    1. BFS via explicit GGM associations
    2. Name-based: entity name contains a BO name (e.g. GeboorteIngeschrevenPersoon)
    3. Prefix stripping for classificatie (AardZakelijkRecht → ZakelijkRecht)
    """
    if entiteitstype in ('abstract', 'proces', 'actor', 'rol',
                          'meetinstrument', 'cross-cutting'):
        return 'n.v.t.'

    def _bo_link(info):
        return f"[[{info['path']}\\|{info['naam']}]]"

    # Strategy 1: BFS via explicit relations
    bo_ids = set(bo_by_guid.keys())
    result = graph.find_path_to_bo(eid, bo_ids, objecttypes)
    if result is not None:
        path, bo_eid = result
        link = _bo_link(bo_by_guid[bo_eid])
        if len(path) == 1:
            return f"beschrijft {link}"
        return f"via {path[0]} → {link}"

    # Strategy 2: name contains a BO name
    name_lower = entity_name.lower().replace('-', '').replace(' ', '')
    best_match = None
    best_len = 0
    for key, info in bo_by_ggm_name.items():
        key_clean = key.replace('-', '').replace(' ', '')
        if len(key_clean) >= 3 and key_clean in name_lower and len(key_clean) > best_len:
            if info.get('ggm_guid') and info['ggm_guid'] in bo_by_guid:
                best_match = info
                best_len = len(key_clean)

    if best_match:
        link = _bo_link(best_match)
        return f"typering {link}" if entiteitstype == 'classificatie' else f"beschrijft {link}"

    # Strategy 3: strip classification prefix
    if entiteitstype == 'classificatie':
        for prefix in CLASSIF_PREFIXES:
            if entity_name.startswith(prefix):
                base = entity_name[len(prefix):]
                bo = bo_by_ggm_name.get(base.lower())
                if bo and bo.get('ggm_guid') and bo['ggm_guid'] in bo_by_guid:
                    return f"typering {_bo_link(bo)}"

    if entiteitstype == 'classificatie':
        return 'referentietabel'
    return '⚠️ geen BO bereikbaar'


# ── Cross-cutting Detection ──────────────────────────────────────────────────

def detect_cross_cutting(eid, entity, scope_bds, bo_by_ggm_name):
    """Check if entity is cross-cutting (BO in different domain)."""
    name = entity['name']
    bo = bo_by_ggm_name.get(name.lower())
    if bo and bo.get('ggm_beleidsdomein') and bo['ggm_beleidsdomein'] not in scope_bds:
        return True, f"BO in domein {bo['ggm_beleidsdomein']}"

    cross_names = {'huishouden', 'provincie', 'gebied', 'functioneelgebied'}
    if name.lower().replace(' ', '').replace('-', '') in cross_names:
        return True, "Meerdere domeinen"

    return False, ''


# ── Process One Onderwerp ────────────────────────────────────────────────────

def process_onderwerp(onderwerp_slug, objecttypes, ggm_data, graph,
                       excluded_ids, bo_by_guid, bo_by_ggm_name,
                       bo_by_onderwerp, ggm_path_map):
    """Full processing pipeline for one onderwerp."""

    begrippen = parse_begrippentabel(onderwerp_slug)
    beleidsdomeinen, scope_ids = determine_scope(
        onderwerp_slug, bo_by_onderwerp, objecttypes, excluded_ids,
        begrippen, bo_by_ggm_name)

    if not beleidsdomeinen:
        return None

    scope_ids = deduplicate(scope_ids, objecttypes, bo_by_guid)

    tabel1, tabel2_ids, tabel3 = match_entities(
        scope_ids, objecttypes, bo_by_guid, bo_by_ggm_name, begrippen)

    tabel2 = []
    review_items = []

    for eid in sorted(tabel2_ids, key=lambda x: objecttypes[x]['name']):
        e = objecttypes[eid]
        bd = e.get('beleidsdomein', '')

        is_cc, cc_reason = detect_cross_cutting(
            eid, e, beleidsdomeinen, bo_by_ggm_name)

        if is_cc:
            etype, desc, conf = 'cross-cutting', cc_reason, 'medium'
        else:
            etype, desc, conf = classify_entity(
                eid, e, graph, set(bo_by_guid.keys()), objecttypes, beleidsdomeinen)

        dekking = compute_dekking(eid, etype, e['name'], graph, bo_by_guid,
                                  bo_by_ggm_name, objecttypes)

        entry = {
            'ggm_name': e['name'], 'beleidsdomein': bd, 'eid': eid,
            'entiteitstype': etype, 'dekking': dekking,
            'beoordeling': desc, 'confidence': conf,
        }
        tabel2.append(entry)

        if conf == 'low':
            review_items.append({
                'entity': e['name'], 'suggested': etype,
                'reason': desc, 'attrs': len(e.get('attributes', [])),
                'doc': (e.get('documentation', '') or '')[:120],
            })

    bo_count = sum(1 for t in tabel1 if t['match_type'] == 'bo') + len(tabel3)
    bo_hiaat_count = sum(1 for t in tabel2
                         if '⚠️' in t.get('dekking', '')
                         and t['entiteitstype'] in ('detail', 'component'))

    structurele = 'compleet' if bo_hiaat_count == 0 else \
        f"incompleet ({bo_hiaat_count} BO-hiaat)"

    return {
        'onderwerp': onderwerp_slug,
        'beleidsdomeinen': sorted(beleidsdomeinen),
        'has_begrippen': len(begrippen) > 0,
        'ggm_count': len(scope_ids),
        'begrippen_count': len(begrippen),
        'bo_count': bo_count,
        'hiaten_count': len(tabel3),
        'bo_hiaten_count': bo_hiaat_count,
        'structurele_dekking': structurele,
        'tabel1': tabel1,
        'tabel2': tabel2,
        'tabel3': tabel3,
        'review': review_items,
        'ggm_path_map': ggm_path_map,
    }


# ── Markdown Generation ─────────────────────────────────────────────────────

def generate_md(data):
    """Generate complete analysis markdown for one onderwerp."""
    ow = data['onderwerp']
    title = ow.replace('-', ' ').title()
    today = date.today().isoformat()
    pm = data['ggm_path_map']
    bds = data['beleidsdomeinen']

    lines = []

    # Frontmatter
    lines.append('---')
    lines.append('type: analyse')
    lines.append(f'titel: "GGM-vergelijking {title}"')
    lines.append(f'datum: {today}')
    lines.append(f'aanleiding: "Vergelijking GGM-entiteiten met bronbegrippen voor {ow}"')
    lines.append('scope_beleidsdomeinen:')
    for bd in bds:
        lines.append(f'  - {bd}')
    lines.append(f'ggm_entiteiten_count: {data["ggm_count"]}')
    lines.append(f'bronbegrippen_count: {data["begrippen_count"]}')
    lines.append(f'bo_count: {data["bo_count"]}')
    lines.append(f'hiaten_count: {data["hiaten_count"]}')
    lines.append('---')
    lines.append('')
    lines.append(f'# GGM-vergelijking {title}')
    lines.append('')

    bd_str = ', '.join(f'**{b}**' for b in bds)
    lines.append(
        f'Vergelijking van de {data["ggm_count"]} GGM-entiteiten in '
        f'{("beleidsdomein " if len(bds)==1 else "beleidsdomeinen ")}{bd_str} '
        f'met de {data["begrippen_count"]} begrippen en {data["bo_count"]} '
        f'BO\'s uit het [[Wiki/Onderwerpoverzichten/{ow}|onderwerpoverzicht '
        f'{title}]].'
    )
    lines.append('')

    # Tabel 1
    lines.append('## Tabel 1: GGM-entiteiten met match in de bronnen')
    lines.append('')
    lines.append('| GGM-entiteit | GGM-beleidsdomein | Bronbegrip / BO | Entiteitstype | Beoordeling |')
    lines.append('|---|---|---|---|---|')

    for t in sorted(data['tabel1'], key=lambda x: (x['beleidsdomein'], x['ggm_name'])):
        ggm_link = _ggm_link(t['ggm_name'], t['beleidsdomein'], pm)
        if t['match_type'] == 'bo':
            bo_link = f"[[{t['bo_path']}\\|{t['bo_naam']}]] ✅ BO"
            etype = t['entiteitstype']
        else:
            if t.get('is_bo'):
                bo_link = f"[[{t['bo_path']}\\|{t['begrip_naam']}]] ✅ BO" if t.get('bo_path') else f"{t['begrip_naam']} ✅ BO"
            else:
                bo_link = f"{t['begrip_naam']} ❌"
            etype = t['entiteitstype']
        lines.append(f"| {ggm_link} | {t['beleidsdomein']} | {bo_link} | {etype} | {t['beoordeling']} |")

    lines.append('')

    # Tabel 2
    lines.append('## Tabel 2: GGM-entiteiten zonder match in de bronnen')
    lines.append('')
    lines.append('| GGM-entiteit | GGM-beleidsdomein | Entiteitstype | Dekking | Beoordeling |')
    lines.append('|---|---|---|---|---|')

    for t in sorted(data['tabel2'], key=lambda x: (x['beleidsdomein'], x['entiteitstype'], x['ggm_name'])):
        ggm_link = _ggm_link(t['ggm_name'], t['beleidsdomein'], pm)
        lines.append(
            f"| {ggm_link} | {t['beleidsdomein']} | {t['entiteitstype']} "
            f"| {t['dekking']} | {t['beoordeling']} |"
        )

    lines.append('')

    # Tabel 3
    if data['tabel3']:
        lines.append('## Tabel 3: Bronbegrippen zonder GGM-equivalent (hiaten)')
        lines.append('')
        lines.append('| Begrip uit bronnen | BO-status | Grondslag | GGM-hiaat? |')
        lines.append('|---|---|---|---|')

        for b in data['tabel3']:
            naam = b['naam']
            link = f"[[{b['bo_link']}\\|{naam}]]" if b.get('bo_link') else naam
            lines.append(
                f"| {link} | ✅ BO | {b.get('reden', '')} "
                f"| **Ja** — ontbreekt in GGM |"
            )
        lines.append('')

    # Beoordeling stub
    matched_bos = sum(1 for t in data['tabel1'] if t['match_type'] == 'bo')
    total_bos = data['bo_count']
    pct = round(100 * matched_bos / total_bos) if total_bos else 0

    lines.append('## Beoordeling')
    lines.append('')
    lines.append(f'<!-- REVIEW: onderstaande tekst is automatisch gegenereerd; '
                 f'controleer en pas aan -->')
    lines.append('')
    lines.append('### Dekking')
    lines.append('')
    lines.append(f'{matched_bos} van {total_bos} BO\'s hebben een GGM-match ({pct}%).')
    lines.append('')

    # Entiteitstype stats
    type_counts = defaultdict(int)
    for t in data['tabel2']:
        type_counts[t['entiteitstype']] += 1

    lines.append('### Structurele patronen')
    lines.append('')
    lines.append(f'Van de {data["ggm_count"]} GGM-entiteiten:')
    lines.append(f'- **{len(data["tabel1"])} in tabel 1** (match in bronnen)')
    parts = ', '.join(f'{c}× {t}' for t, c in sorted(type_counts.items()))
    lines.append(f'- **{len(data["tabel2"])} in tabel 2** (geen match): {parts}')
    lines.append('')

    if data['hiaten_count'] > 0:
        lines.append('### Hiaten')
        lines.append('')
        for b in data['tabel3']:
            lines.append(f'- **{b["naam"]}**: {b.get("reden", "")}')
        lines.append('')

    return '\n'.join(lines)


def _ggm_link(entity_name, beleidsdomein, path_map):
    path = path_map.get(beleidsdomein, '')
    if path:
        return f"[[{path}\\|{entity_name}]]"
    return entity_name


# ── Review Summary ───────────────────────────────────────────────────────────

def generate_review(all_results):
    """Generate compact review summary for LLM."""
    lines = []
    lines.append(f'# GGM-vergelijking review — {date.today().isoformat()}')
    lines.append('')

    generated = [r for r in all_results if r['has_begrippen']]
    partial = [r for r in all_results if not r['has_begrippen']]
    total_review = sum(len(r['review']) for r in all_results)

    lines.append(f'Gegenereerd: {len(generated)} volledig, {len(partial)} partieel '
                 f'(geen begrippentabel). Review-items: {total_review}.')
    lines.append('')

    # Summary table
    lines.append('## Samenvatting per onderwerp')
    lines.append('')
    lines.append('| Onderwerp | GGM | BO | Match | Hiaten | BO-hiaten | Review |')
    lines.append('|---|---|---|---|---|---|---|')
    for r in sorted(all_results, key=lambda x: x['onderwerp']):
        matched = sum(1 for t in r['tabel1'] if t['match_type'] == 'bo')
        lines.append(
            f"| {r['onderwerp']} | {r['ggm_count']} | {r['bo_count']} "
            f"| {matched} | {r['hiaten_count']} | {r['bo_hiaten_count']} "
            f"| {len(r['review'])} |"
        )
    lines.append('')

    # Review items
    items_by_ow = [(r['onderwerp'], r['review']) for r in all_results if r['review']]
    if items_by_ow:
        lines.append('## Items voor review')
        lines.append('')
        lines.append('Entiteiten met `confidence=low` — classificatie onzeker.')
        lines.append('')
        for ow, items in sorted(items_by_ow):
            lines.append(f'### {ow}')
            lines.append('')
            for item in items:
                doc = item['doc']
                lines.append(
                    f"- **{item['entity']}** → suggested: {item['suggested']} "
                    f"({item['attrs']} attrs). {doc}"
                )
            lines.append('')

    return '\n'.join(lines)


# ── Overview Update ──────────────────────────────────────────────────────────

def update_overview(all_results):
    """Update ggm-vergelijkingen.md with results, preserving hand-edited rows."""
    if not OVERVIEW_PATH.exists():
        return

    content = OVERVIEW_PATH.read_text(encoding='utf-8')
    results_by_ow = {r['onderwerp']: r for r in all_results}
    new_lines = []

    for line in content.split('\n'):
        if not line.startswith('| [[Wiki/Onderwerpoverzichten/'):
            new_lines.append(line)
            continue

        cols = split_table_row(line)
        ow_match = re.search(r'Onderwerpoverzichten/([^\]\\|]+)', cols[1] if len(cols) > 1 else '')
        if not ow_match:
            new_lines.append(line)
            continue

        ow_slug = ow_match.group(1)

        has_existing = len(cols) > 3 and cols[3].strip() not in ('', '|')
        if has_existing:
            new_lines.append(line)
            continue

        result = results_by_ow.get(ow_slug)
        if not result:
            new_lines.append(line)
            continue

        matched = sum(1 for t in result['tabel1'] if t['match_type'] == 'bo')
        ow_link = f"[[Wiki/Onderwerpoverzichten/{ow_slug}\\|{ow_slug}]]"
        vgl_link = f"[[Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-{ow_slug}\\|{ow_slug}]]"
        struct = result['structurele_dekking']

        new_lines.append(
            f"| {ow_link} | {vgl_link} | {result['ggm_count']} "
            f"| {result['bo_count']} | {result['hiaten_count']} "
            f"| {result['bo_hiaten_count']} | {struct} | <!-- review --> |"
        )

    OVERVIEW_PATH.write_text('\n'.join(new_lines), encoding='utf-8')
    print(f"Overview: {OVERVIEW_PATH}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='GGM-vergelijking prep: pre-process matching and classification')
    parser.add_argument('--onderwerp', type=str, help='Process single onderwerp')
    parser.add_argument('--all', action='store_true', help='Process all onderwerpen')
    parser.add_argument('--dry-run', action='store_true', help='Preview counts only')
    args = parser.parse_args()

    if not args.onderwerp and not args.all:
        parser.error('Specify --onderwerp or --all')

    print("Loading data...")
    ggm_data, objecttypes = load_ggm()
    bo_by_guid, bo_by_ggm_name, bo_by_onderwerp = load_bo_pages()
    ggm_path_map = load_ggm_path_map()
    graph = RelationGraph(ggm_data, objecttypes)
    excluded_ids = find_excluded_ids(objecttypes, graph, bo_by_guid)

    print(f"  GGM Objecttype: {len(objecttypes)}, BO's: {len(bo_by_guid)}, "
          f"excluded (IMGeo/tekenwijze): {len(excluded_ids)}")

    if args.onderwerp:
        onderwerpen = [args.onderwerp]
    else:
        onderwerpen = sorted(f.stem for f in ONDERWERP_DIR.glob("*.md"))

    all_results = []
    for ow in onderwerpen:
        result = process_onderwerp(
            ow, objecttypes, ggm_data, graph, excluded_ids,
            bo_by_guid, bo_by_ggm_name, bo_by_onderwerp, ggm_path_map)

        if result is None:
            print(f"  {ow}: geen beleidsdomeinen gevonden — overgeslagen")
            continue

        all_results.append(result)
        matched = sum(1 for t in result['tabel1'] if t['match_type'] == 'bo')
        print(f"  {ow}: {result['ggm_count']} entiteiten, "
              f"{result['bo_count']} BO's, {matched} matches, "
              f"{result['hiaten_count']} hiaten, "
              f"{len(result['review'])} review-items")

        if not args.dry_run:
            md = generate_md(result)
            out_path = OUTPUT_DIR / f"ggm-vergelijking-{ow}.md"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(md, encoding='utf-8')

    if not args.dry_run and all_results:
        review = generate_review(all_results)
        review_path = OUTPUT_DIR / "ggm-vergelijking-review.md"
        review_path.write_text(review, encoding='utf-8')
        print(f"\nReview: {review_path}")

        update_overview(all_results)

    print(f"\nDone: {len(all_results)} onderwerpen verwerkt")
    if all_results:
        total_ggm = sum(r['ggm_count'] for r in all_results)
        total_bo = sum(r['bo_count'] for r in all_results)
        total_review = sum(len(r['review']) for r in all_results)
        print(f"  Totaal: {total_ggm} GGM-entiteiten, {total_bo} BO's, "
              f"{total_review} review-items")


if __name__ == '__main__':
    main()
