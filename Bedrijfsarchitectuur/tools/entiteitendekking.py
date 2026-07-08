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
ACTOR_DIR = BASE_PATH / "Wiki/Actoren"
ROL_DIR = BASE_PATH / "Wiki/Rollen"
ELEMENT_DIRS = (BO_DIR, ACTOR_DIR, ROL_DIR)

# Persistente buiten-scope-registratie: GGM-entiteiten van entiteitstype
# actor/rol die na menselijke beoordeling bewust géén pagina krijgen
# (extern, louter context — zie CLAUDE.md "gemeentelijk perspectief").
# Alleen namen in deze set krijgen nog automatisch n.v.t.; alle overige
# ongematchte actor/rol-entiteiten verschijnen als "⚠️ geen actor/rol-pagina"
# in het rapport én in review.md. Curatie gebeurt hier (overleeft her-runs,
# in tegenstelling tot draft-correcties in de rapporten).
NVT_ACTOR_ROL = set()
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
    specialisatie_by_guid = {}
    via_kandidaat_by_guid = {}

    element_files = [f for d in ELEMENT_DIRS if d.exists() for f in d.rglob("*.md")]
    for f in element_files:
        if f.name == "index.md":
            continue
        content = f.read_text(encoding='utf-8')
        fm = extract_frontmatter(content)
        if fm.get('type') != 'element':
            continue

        naam = fm.get('naam', f.stem)
        ggm_ent = fm.get('ggm_entiteit', '') or ''
        ggm_guid = fm.get('ggm_guid', '') or ''
        ggm_bd = fm.get('ggm_beleidsdomein', '') or ''
        rel = str(f.relative_to(BASE_PATH)).replace('.md', '')
        grondslag = fm.get('grondslag', '') or ''

        homoniemen = fm.get('bo_homoniemen', []) or []
        synoniemen = fm.get('bo_synoniemen', []) or []
        is_data_object = grondslag in ('ggm-entiteit', 'ggm-afgeleid', 'procesobject')

        # Derive taakveld from path: Wiki/Bedrijfsobjecten/{taakveld}/{bd}/
        parts = rel.split('/')
        bo_taakveld_slug = parts[2] if len(parts) > 3 else ''

        archimate_type = fm.get('archimate_type', '') or ''

        info = {
            'naam': naam, 'path': rel, 'ggm_entiteit': ggm_ent,
            'ggm_guid': ggm_guid, 'ggm_beleidsdomein': ggm_bd,
            'grondslag': grondslag, 'homoniemen': homoniemen,
            'synoniemen': synoniemen,
            'is_data_object': is_data_object,
            'taakveld_slug': bo_taakveld_slug,
            'archimate_type': archimate_type,
        }

        # Meerdere pagina's mogen dezelfde ggm_guid dragen (twee-pagina-
        # patroon: BO + actor/rol delen de GGM-entiteit). De business-object-
        # pagina is primair in de index; de overige pagina's worden op de
        # primaire info als tegenhangers geregistreerd zodat niets
        # stilzwijgend wordt overschreven (voorheen last-write-wins).
        def _bo_first(prev, cand, track=False):
            if prev is None or prev is cand:
                return cand if prev is None else prev
            if (cand['archimate_type'] == 'business-object'
                    and prev.get('archimate_type') != 'business-object'):
                winner, loser = cand, prev
            else:
                winner, loser = prev, cand
            if track:
                lst = winner.setdefault('tegenhangers', [])
                for extra in loser.pop('tegenhangers', []) + [loser]:
                    if extra is not winner and all(
                            x['path'] != extra['path'] for x in lst):
                        lst.append(extra)
            return winner

        if ggm_guid:
            by_guid[ggm_guid] = _bo_first(by_guid.get(ggm_guid), info, track=True)
        if ggm_ent:
            by_name[ggm_ent.lower()] = _bo_first(by_name.get(ggm_ent.lower()), info)
        by_name[naam.lower()] = _bo_first(by_name.get(naam.lower()), info)
        all_bos.append(info)

        # ggm_duplicaat_entiteiten: andere GUID's die hetzelfde concept
        # representeren (bijv. dezelfde entiteit dubbel gemodelleerd in het
        # GGM, of — zoals Sportterrein/Sportpark — twee verschillend genoemde
        # entiteiten die als duplicaat zijn vastgesteld). Elke GUID hierin
        # wijst naar dezelfde BO-info, zodat compute_dekking() deze net als
        # de primaire GUID herkent. Twee bestaande notatievormen in de wiki:
        # een platte lijst GUID-strings, of een lijst dicts met een
        # 'guid'-sleutel (het templateformaat).
        for dup in (fm.get('ggm_duplicaat_entiteiten') or []):
            dup_guid = dup if isinstance(dup, str) else (dup or {}).get('guid')
            if dup_guid and dup_guid not in by_guid:
                by_guid[dup_guid] = {**info, 'is_duplicate_guid': True}

        # bo_subtypes met ggm_attribuut: generalisatie zijn échte, aparte
        # GGM-entiteiten (eigen GUID) die bewust geen eigen BO zijn geworden
        # (redactionele keuze, geen BO-criteria-tekort — bijv. Brug bij
        # Kunstwerk). De ggm_attribuut: <attribuutnaam>-variant heeft altijd
        # ggm_guid == de eigen BO-guid (geen aparte entiteit) en heeft dus
        # geen registratie nodig.
        for st in (fm.get('bo_subtypes') or []):
            if not isinstance(st, dict) or st.get('ggm_attribuut') != 'generalisatie':
                continue
            st_guid = st.get('ggm_guid')
            if st_guid and st_guid != ggm_guid and st_guid not in specialisatie_by_guid:
                specialisatie_by_guid[st_guid] = info

        # bo_via_kandidaten: curatie-registry voor entiteiten waarvoor
        # compute_dekking() een echte ambiguïteit vond (meerdere even-goede
        # associatie-kandidaten, geen eenduidige winnaar) — een mens heeft
        # hier bewust deze BO als winnaar aangewezen, zodat een volgende run
        # niet opnieuw "ter discussie" hoeft te tonen. Zelfde vorm als
        # bo_subtypes: lijst van dicts met ggm_guid + reden.
        for vk in (fm.get('bo_via_kandidaten') or []):
            if not isinstance(vk, dict):
                continue
            vk_guid = vk.get('ggm_guid')
            if vk_guid and vk_guid not in via_kandidaat_by_guid:
                via_kandidaat_by_guid[vk_guid] = info

    return by_guid, by_name, all_bos, specialisatie_by_guid, via_kandidaat_by_guid


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
        self.agg_whole = {}
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
                # EA/XMI-richting voor Aggregation is source=geheel,
                # target=deel (bijv. "Beschikking bevat Onderdeel
                # beschikking" -> source_id=Beschikking, target_id=Onderdeel
                # beschikking) — het omgekeerde van Generalization, waar
                # source het specifieke/kind-type is. agg_whole is dus de
                # deel->geheel-kant, nodig om van een deel omhoog naar zijn
                # geheel te wandelen (zie _walk_aggregation_to_bo).
                self.agg_parent[src] = tgt
                self.agg_whole[tgt] = src
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

    def gather_dekking_candidates(self, start_id, bo_ids, objecttypes, max_gen_depth=10,
                                   max_assoc_hops=2):
        """Collect candidate BO's reachable from start_id, in two tiers.

        This is deliberately a *candidate-gathering* step, not a
        winner-picking one — see `_score_candidates` for that. Three
        channels, in priority order:

        1. Generalization-up chain (`gen_parent`): a single, deterministic
           path — every entity has at most one direct generalization parent
           in this model, so climbing it is never a guess. Stops at the
           first BO found.
        2. Own direct children (`gen_children`, start entity only, depth 1):
           the one legitimate use of downward generalization — finding a
           concrete BO subtype of the start entity's own (abstract) type.
           Branching (an abstract type can have multiple BO children) is
           possible here and left to the scoring step; it must never be
           tried again after any further hop (that produces the sibling-hop
           bug this replaced, e.g. Leidingelement -> Beheerobject ->
           Waterobject).
        3. Associations, bounded to `max_assoc_hops`: only consulted when
           channels 1+2 found nothing, since a real generalization relation
           is always stronger evidence than an association chain. Stops at
           the shallowest hop that yields any BO — never chains an
           association off of an ancestor reached via another association
           (that produced the Bak -> Beheerobject -> Melding -> Medewerker
           bug), only off the start entity's own association neighborhood,
           hop by hop.

        Returns a list of dicts: {'bo_eid', 'hops', 'via_names', 'kind'}.
        """
        candidates = []

        cur = start_id
        depth = 0
        via_names = []
        while cur in self.gen_parent and depth < max_gen_depth:
            nxt = self.gen_parent[cur]
            depth += 1
            via_names.append(objecttypes.get(nxt, {}).get('name', '?'))
            if nxt in bo_ids:
                candidates.append({'bo_eid': nxt, 'hops': depth,
                                    'via_names': list(via_names), 'kind': 'generalisatie'})
                break
            cur = nxt

        for child in self.gen_children.get(start_id, []):
            if child in bo_ids:
                candidates.append({'bo_eid': child, 'hops': 1,
                                    'via_names': [objecttypes.get(child, {}).get('name', '?')],
                                    'kind': 'specialisatie-kind'})

        if candidates:
            return candidates

        visited = {start_id}
        frontier = [start_id]
        for hop in range(1, max_assoc_hops + 1):
            next_frontier = []
            hop_hits = []
            for cur in frontier:
                for tgt in self.assoc.get(cur, []):
                    if tgt in visited:
                        continue
                    visited.add(tgt)
                    if tgt in bo_ids:
                        hop_hits.append(tgt)
                    else:
                        next_frontier.append(tgt)
            if hop_hits:
                for tgt in hop_hits:
                    candidates.append({'bo_eid': tgt, 'hops': hop,
                                        'via_names': [objecttypes.get(tgt, {}).get('name', '?')],
                                        'kind': 'associatie'})
                break
            frontier = next_frontier
            if not frontier:
                break
        return candidates


# ── Filtering ────────────────────────────────────────────────────────────────

def find_excluded_ids(objecttypes, graph, bo_by_guid, specialisatie_by_guid):
    geo_roots = {eid for eid, e in objecttypes.items()
                 if e['name'] in ('Geo-Object', 'GeoObject')}
    geo_desc = graph.descendants_of(geo_roots)
    # Structureel criterium, geen domeinlabel: een geo-afstammeling blijft
    # buiten de exclusie als hij al een eigen BO heeft of een geregistreerde
    # specialisatie van een BO is (dezelfde curatie-registry als stap 1 in
    # compute_dekking) — niet omdat zijn beleidsdomein toevallig "BAG" heet.
    protected = {eid for eid in geo_desc
                 if eid in bo_by_guid
                 or eid in specialisatie_by_guid}
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
    """Pick one entity per duplicate name, deterministically.

    entity_ids is a set, so plain iteration order depends on Python's string
    hash randomization (PYTHONHASHSEED) and can differ between runs. Break
    ties by preferring an existing BO match, then the entity with the most
    attributes (the more fully-specified, likely-canonical definition), then
    the GUID itself as a final deterministic tiebreak.
    """
    by_name = defaultdict(list)
    for eid in entity_ids:
        by_name[objecttypes[eid]['name'].lower()].append(eid)
    keep = set()
    for eids in by_name.values():
        if len(eids) == 1:
            keep.add(eids[0])
        else:
            matched = [e for e in eids if e in bo_by_guid]
            candidates = matched if matched else eids
            best = sorted(candidates,
                          key=lambda e: (-len(objecttypes[e].get('attributes', [])), e))[0]
            keep.add(best)
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
PROCESS_WORDS = ('onderzoek', 'aanmelding', 'verwerking', 'procedure', 'behandeling',
                 'aanvraag', 'melding', 'beschikking')
ROLE_SUFFIXES = ('begeleider', 'medewerker', 'functionaris', 'beheerder',
                 'ambtenaar', 'adviseur', 'gever', 'nemer',
                 'houder', 'eigenaar', 'indiener', 'contactpersoon')
# Namen die toevallig "regel"/"sluiting" als substring bevatten maar niet de
# "onderdeel"-betekenis hebben (regel-als-voorschrift resp. toeval), dus
# uitgesloten van de ONDERDEEL_NAAMWOORDEN-match hieronder.
ONDERDEEL_UITZONDERINGEN = (
    'maatregel', 'uitsluitingsgrond', 'regeling', 'regeltekst',
    'regel voor iedereen', 'toepasbare regel', 'toepasbareregelbestand',
    'uitvoeringsregel', 'deelnemer',
)
ONDERDEEL_NAAMWOORDEN = ('ontbinding', 'sluiting', 'regel', 'deel')


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

    if (any(w in nl for w in ONDERDEEL_NAAMWOORDEN)
            and not any(x in nl for x in ONDERDEEL_UITZONDERINGEN)):
        return 'onderdeel', 'Onderdeel (naamindicatie)', 'medium'

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
        return 'detail', 'Detailgegeven (weinig attributen, geen structureel signaal)', 'low'

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

GENERIC_BUILDING_BLOCKS = {
    'Locatie', 'Punt', 'Lijn', 'Gebied', 'Puntengroep', 'Lijnengroep', 'Gebiedengroep',
    'Foto', 'Video-opname', 'Periode',
    'FormeleHistorie', 'MaterieleHistorie', 'StrijdigheidOfNietigheid',
}


def _camel_words(name):
    """Split CamelCase/PascalCase and hyphen/space-separated names into lowercase words."""
    parts = re.findall(r'[A-Z]?[a-z0-9]+|[A-Z]+(?=[A-Z]|$|[^a-z])', name)
    return {p.lower() for p in parts if p}


def _walk_aggregation_to_bo(eid, bo_ids, agg_whole, max_depth=3):
    """Loop de aggregatie-keten omhoog (deel->geheel, bijv. Onderdeel
    beschikking -> Beschikking) tot een BO gevonden wordt. Net als gen_parent
    is agg_whole per entiteit enkelvoudig, dus een simpele keten-wandeling
    volstaat (geen volledige BFS nodig)."""
    cur = eid
    for _ in range(max_depth):
        cur = agg_whole.get(cur)
        if cur is None:
            return None
        if cur in bo_ids:
            return cur
    return None


def _score_candidates(candidates, objecttypes, prefer_bd, start_name):
    """Rank dekking-kandidaten en wijs een winnaar aan, of signaleer ambiguïteit.

    Retourneert ('winner', kandidaat) of ('ambigu', [kandidaten die gelijk
    staan]). Minste hops wint eerst; bij gelijke hops wint hetzelfde
    beleidsdomein als de startentiteit; bij een resterende gelijkstand wint
    een kandidaat wiens naam een CamelCase-woord deelt met de startentiteit
    (onafhankelijk bevestigend signaal, los van het graph-pad). Blijven er na
    alle drie de criteria nog kandidaten gelijk staan, dan is dat een echte
    ambiguïteit — geen stille eerste-de-beste-keuze meer.
    """
    min_hops = min(c['hops'] for c in candidates)
    pool = [c for c in candidates if c['hops'] == min_hops]
    if len(pool) == 1:
        return 'winner', pool[0]

    start_words = _camel_words(start_name)

    def _rank(c):
        bo_entity = objecttypes.get(c['bo_eid'], {})
        same_bd = prefer_bd is not None and bo_entity.get('beleidsdomein') == prefer_bd
        name_confirmed = bool(start_words & _camel_words(bo_entity.get('name', '')))
        return (0 if same_bd else 1, 0 if name_confirmed else 1)

    pool.sort(key=_rank)
    best_rank = _rank(pool[0])
    tied = [c for c in pool if _rank(c) == best_rank]
    if len(tied) == 1:
        return 'winner', tied[0]
    return 'ambigu', tied


def compute_dekking(eid, etype, name, graph, bo_by_guid, bo_by_name, objecttypes,
                     specialisatie_by_guid, via_kandidaat_by_guid):
    """Compute dekking: welk BO dekt deze entiteit structureel?

    Retourneert (dekking_str, target_bo_info_of_None, match_kind).

    Dekkingswaarden (zelfde semantiek als ggm-vergelijking):
    - specialisatie van [[BO]]   — geregistreerd bo_subtypes-kind (generalisatie), bewust geen eigen BO
    - onderdeel van [[BO]]       — GGM-Aggregation-keten naar een BO (bestaat-uit)
    - beschrijft [[BO]]          — direct pad naar BO
    - via X → [[BO]]             — via tussenentiteit naar BO
    - typering [[BO]]            — classificatie-entiteit bij BO
    - ⚠️ ter discussie tussen [[BO]] / [[BO]] — meerdere gelijkwaardige kandidaten, curatie nodig
    - ⚠️ geen BO bereikbaar      — geen pad gevonden
    - referentietabel            — classificatie zonder specifiek BO
    - n.v.t.                     — abstract/proces/actor/rol
    - generieke bouwsteen        — gebruikt door meerdere BO's, geen eigenaar

    match_kind: 'n.v.t.' | 'specialisatie' | 'onderdeel' | 'generiek' |
                'duplicaat' | 'graph' | 'ambigu' | 'naam' | 'classificatie-prefix' |
                'referentietabel' | 'geen-match'
    """
    if etype in ('abstract', 'proces', 'meetinstrument', 'cross-cutting'):
        return 'n.v.t.', None, 'n.v.t.'

    if etype in ('actor', 'rol'):
        # De directe GUID/naam-match is al geprobeerd (process_beleidsdomein);
        # hier komen alleen actor/rol-entiteiten zónder pagina. n.v.t. geldt
        # alleen nog bij expliciete curatie in NVT_ACTOR_ROL (buiten scope,
        # extern); alle andere gevallen zijn kandidaten voor een pagina in
        # Wiki/Actoren/ of Wiki/Rollen/ en verschijnen in review.md.
        if name in NVT_ACTOR_ROL:
            return 'n.v.t.', None, 'n.v.t.'
        return f"⚠️ geen {etype}-pagina", None, 'geen-match'

    bo_ids = set(bo_by_guid.keys())
    verb = "typering" if etype == 'classificatie' else "beschrijft"

    # 0. Gecureerde keuze uit een eerder gedetecteerde ambiguïteit
    #    (bo_via_kandidaten) — een mens heeft deze BO al aangewezen als
    #    winnaar tussen meerdere gelijkwaardige kandidaten; gaat vóór alles,
    #    net als specialisatie_by_guid, zodat een volgende run niet opnieuw
    #    "ter discussie" hoeft te tonen.
    via_kandidaat_target = via_kandidaat_by_guid.get(eid)
    if via_kandidaat_target:
        return f"{verb} {bo_link(via_kandidaat_target)}", via_kandidaat_target, 'via-kandidaat'

    # 1. Geregistreerd subtype (bo_subtypes met ggm_attribuut: generalisatie)
    #    — curated door /write-element, gaat vóór elke heuristiek: dit is precies
    #    het Brug/Kunstwerk-scenario waarin de graph-search (stap 3) een
    #    verkeerde sibling-BO zou vinden omdat de echte GGM-ouder
    #    (Overbruggingsobject) zelf geen BO is.
    specialisatie_target = specialisatie_by_guid.get(eid)
    if specialisatie_target:
        return f"specialisatie van {bo_link(specialisatie_target)}", specialisatie_target, 'specialisatie'

    # 2. Aggregatie-keten (bestaat-uit, bijv. Diensttype -> Onderdeel
    #    beschikking -> Beschikking) — een echte structurele Aggregation-edge
    #    in het GGM is een sterker signaal dan de generieke associatie/naam-
    #    heuristieken verderop.
    agg_bo_eid = _walk_aggregation_to_bo(eid, bo_ids, graph.agg_whole)
    if agg_bo_eid:
        target = bo_by_guid[agg_bo_eid]
        return f"onderdeel van {bo_link(target)}", target, 'onderdeel'

    # 3. Generieke bouwsteen: geen eigenaar-BO, gebruikt door tientallen BO's
    if name in GENERIC_BUILDING_BLOCKS:
        return "generieke bouwsteen — gebruikt door meerdere BO's", None, 'generiek'

    # 4. Twee-fasen kandidatenzoektocht: fase 1 verzamelt kandidaten via
    #    generalisatie (omhoog, enkelvoudig) / eigen generalisatie-kinderen
    #    (alleen vanaf deze entiteit) / begrensde associatie-hops (alleen als
    #    de eerste twee niets vinden), fase 2 (_score_candidates) kiest een
    #    winnaar of signaleert een echte ambiguïteit. Vóór de naam-duplicaat-
    #    stap (5): een echte structurele relatie (bijv. Rioolput als
    #    generalisatie-kind van Put) moet als 'graph' herkend worden, niet
    #    toevallig als 'duplicaat' omdat het kind dezelfde naam draagt als de
    #    BO waarin het opgaat.
    own_bd = objecttypes.get(eid, {}).get('beleidsdomein')
    candidates = graph.gather_dekking_candidates(eid, bo_ids, objecttypes)
    if candidates:
        # Dedupliceren op BO-pagina: twee GGM-GUID's die als ggm_duplicaat_entiteiten
        # aan dezelfde BO-pagina hangen (bijv. Buurt in RSGBPlus én BAG) zijn geen
        # echte ambiguïteit — hetzelfde doel twee keer bereikt, niet twee kandidaten.
        by_path = {}
        for c in candidates:
            path = bo_by_guid[c['bo_eid']]['path']
            if path not in by_path or c['hops'] < by_path[path]['hops']:
                by_path[path] = c
        candidates = list(by_path.values())
        outcome, result = _score_candidates(candidates, objecttypes, own_bd, name)
        if outcome == 'ambigu':
            links = " / ".join(bo_link(bo_by_guid[c['bo_eid']]) for c in result)
            return f"⚠️ ter discussie tussen {links}", None, 'ambigu'
        target = bo_by_guid[result['bo_eid']]
        if result['hops'] == 1:
            return f"{verb} {bo_link(target)}", target, 'graph'
        return f"via {result['via_names'][0]} → {bo_link(target)}", target, 'graph'

    # 5. Exacte naam-duplicaat van een bestaand BO (andere GUID) — zelfde
    #    concept dubbel gemodelleerd in het GGM (bijv. RSGB Wijk vs. BAG Wijk).
    #    Uitgesloten: entiteiten die het doel-BO al expliciet als homoniem
    #    (ander concept, zelfde naam) heeft geregistreerd in bo_homoniemen —
    #    die zijn per definitie geen duplicaat.
    dup = bo_by_name.get(name.lower())
    if dup and dup.get('ggm_guid') and dup['ggm_guid'] in bo_ids and dup['ggm_guid'] != eid:
        is_registered_homoniem = any(
            h.get('ggm_guid') == eid for h in (dup.get('homoniemen') or []))
        if not is_registered_homoniem:
            return f"{verb} {bo_link(dup)}", dup, 'duplicaat'

    # 6. Naam-gebaseerd: CamelCase-woordgrens, of prefix/suffix-match voor
    #    Nederlandse samenstellingen ("Bemiddelingsactiviteit" eindigt op
    #    "activiteit", "Heffingskorting" begint met "heffing"). Nooit een kale
    #    middenin-substring-match — die geeft valse hits (bijv. "wijk" in
    #    "Afwijkend...", "leiding" in "Opleidingsnaam...").
    name_words = _camel_words(name)
    nl = name.lower().replace('-', '').replace(' ', '')
    best, best_len = None, 0
    for key, info in bo_by_name.items():
        key_words = set(re.split(r'[-\s]+', key.lower())) - {''}
        kc = key.replace('-', '').replace(' ', '').lower()
        if len(kc) < 3:
            continue
        whole_word = bool(key_words) and key_words <= name_words
        # Nederlands meervoud ("Brondocumenten" = "Brondocument" + "en")
        boundary = len(kc) >= 5 and (
            nl.startswith(kc) or nl.endswith(kc) or
            nl.endswith(kc + 'en') or nl.endswith(kc + 's'))
        if (whole_word or boundary) and len(kc) > best_len:
            if info.get('ggm_guid') and info['ggm_guid'] in bo_ids:
                best, best_len = info, len(kc)
    if best:
        return f"{verb} {bo_link(best)}", best, 'naam'

    # 7. Strip classification prefix
    if etype == 'classificatie':
        for pfx in CLASSIF_PREFIXES:
            if name.startswith(pfx):
                base = name[len(pfx):]
                bo = bo_by_name.get(base.lower())
                if bo and bo.get('ggm_guid') and bo['ggm_guid'] in bo_ids:
                    return f"typering {bo_link(bo)}", bo, 'classificatie-prefix'
        return 'referentietabel', None, 'referentietabel'

    return '⚠️ geen BO bereikbaar', None, 'geen-match'


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
                           bo_by_guid, bo_by_name, all_bos, specialisatie_by_guid,
                           via_kandidaat_by_guid):
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
            # Hernoemd dekt zowel een letterlijke naamswijziging (zelfde GUID,
            # andere BO-naam) als een dubbele GGM-modellering (andere GUID,
            # via ggm_duplicaat_entiteiten geregistreerd) — dekking gaat uit
            # van het GGM: in beide gevallen ís dit het BO, alleen anders
            # benoemd/gemodelleerd. Geen synoniem (dat zou een tweede naam
            # zijn die naast de eerste blijft bestaan).
            if bo_info.get('is_duplicate_guid'):
                etype = 'hernoemd'
                beoordeling = (f"Hernoemd naar {bo_info['naam']} "
                                f"(dubbel gemodelleerd in GGM, zie ggm_duplicaat_entiteiten)")
            elif bo_info['naam'].lower() != name.lower():
                etype = 'hernoemd'
                beoordeling = f"Hernoemd naar {bo_info['naam']}"
            else:
                etype = '—'
                beoordeling = 'Exacte match'
            page_kind = {'business-actor': 'actor-pagina',
                         'business-role': 'rol-pagina'}.get(
                bo_info.get('archimate_type', ''))
            if page_kind:
                beoordeling += f' ({page_kind})'

            naamoverlap_parts = []
            for s in (bo_info.get('synoniemen') or []):
                syn_naam = s.get('naam', '')
                if syn_naam:
                    naamoverlap_parts.append(f"synoniem: {syn_naam}")
            for h in (bo_info.get('homoniemen') or []):
                other = h.get('bedrijfsobject', '')
                if other:
                    naamoverlap_parts.append(f"homoniem: {other}")
            naamoverlap = '; '.join(naamoverlap_parts)

            bo_matches.append({
                'ggm_name': name, 'eid': eid,
                'bo_naam': bo_info['naam'], 'bo_path': bo_info['path'],
                'entiteitstype': etype, 'naamoverlap': naamoverlap,
                'beoordeling': beoordeling,
            })
        else:
            etype, rationale, conf = classify_entity(eid, e, graph, bo_ids, objecttypes)

            # Override with begrippentabel if available (handmatig geclassificeerd).
            # Nooit een XMI-abstract entiteit downgraden naar een concreet type: een
            # begrip met dezelfde naam elders in de wiki (ander domein, andere GUID)
            # mag de eigen GGM-structuur van deze entiteit niet overschrijven.
            begrip = begrip_index.get(name.lower())
            if begrip and begrip.get('type') and not e.get('is_abstract'):
                mapped = BEGRIP_TYPE_MAP.get(begrip['type'].lower(), '')
                if mapped:
                    etype = mapped
                    conf = 'high'
                if begrip.get('reden'):
                    rationale = begrip['reden']

            dekking, dekking_bo, match_kind = compute_dekking(
                eid, etype, name, graph, bo_by_guid, bo_by_name, objecttypes,
                specialisatie_by_guid, via_kandidaat_by_guid)
            if match_kind == 'specialisatie' and dekking_bo:
                etype = 'specialisatie'
                rationale = f"Specialisatie van {dekking_bo['naam']} — zie bo_subtypes"
            elif match_kind == 'onderdeel' and dekking_bo:
                etype = 'onderdeel'
                rationale = f"Onderdeel van {dekking_bo['naam']}"
            elif match_kind == 'ambigu':
                rationale = ("Meerdere gelijkwaardige BO-kandidaten, geen eenduidige winnaar — "
                             "kies er één en registreer via bo_via_kandidaten op die BO-pagina")

            geen_match.append({
                'ggm_name': name, 'eid': eid,
                'entiteitstype': etype, 'dekking': dekking,
                'dekking_bo_path': dekking_bo['path'] if dekking_bo else None,
                'match_kind': match_kind,
                'beoordeling': rationale, 'confidence': conf,
            })

            # Ambigue matches horen altijd bij review, los van de classify_entity-
            # confidence — dit is een compute_dekking-bevinding (echte
            # gelijkstand tussen kandidaten), niet een classificatie-twijfel.
            if (conf == 'low' or match_kind == 'ambigu'
                    or (etype in ('actor', 'rol') and '⚠️' in dekking)):
                review_items.append({
                    'entity': name, 'suggested': etype,
                    'attrs': len(e.get('attributes', [])),
                    'doc': (e.get('documentation', '') or '')[:120],
                })

    match_count = len(bo_matches)
    # n.v.t. (abstract/proces/actor/rol) staat buiten scope van BO-dekking —
    # apart geteld zodat het dekkingspercentage alleen over daadwerkelijk
    # BO-relevante entiteiten gaat, niet stilzwijgend als "ondersteunend" meetelt.
    nvt = sum(1 for g in geen_match if g.get('dekking') == 'n.v.t.')
    ondersteunend = sum(1 for g in geen_match
                         if '⚠️' not in g.get('dekking', '') and g.get('dekking') != 'n.v.t.')
    niet_gedekt = sum(1 for g in geen_match if '⚠️' in g.get('dekking', ''))

    return {
        'naam': bd_name,
        'entity_count': len(entity_ids),
        'match_count': match_count,
        'ondersteunend': ondersteunend,
        'niet_gedekt': niet_gedekt,
        'nvt': nvt,
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
                      bo_by_guid, bo_by_name, all_bos, specialisatie_by_guid,
                      via_kandidaat_by_guid):
    """Process all beleidsdomeinen within one taakveld."""
    results = {}
    rsgb_sub = None

    for bd_name in sorted(bd_entities.keys()):
        eids = bd_entities[bd_name]
        bd_result = process_beleidsdomein(
            bd_name, eids, objecttypes, graph, bo_by_guid, bo_by_name, all_bos,
            specialisatie_by_guid, via_kandidaat_by_guid)

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
    total_nvt = sum(r['nvt'] for r in results.values())
    total_review = sum(len(r['review']) for r in results.values())

    return {
        'taakveld': tv_name,
        'slug': slugify(tv_name),
        'beleidsdomeinen': results,
        'total_entities': total_entities,
        'total_matches': total_matches,
        'total_ondersteunend': total_ondersteunend,
        'total_niet_gedekt': total_niet_gedekt,
        'total_nvt': total_nvt,
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
    relevant = tv_result['total_entities'] - tv_result['total_nvt']
    gedekt = tv_result['total_matches'] + tv_result['total_ondersteunend']
    pct = round(100 * gedekt / relevant) if relevant else 0
    lines.append(f"{len(bds)} beleidsdomeinen, {tv_result['total_entities']} GGM-entiteiten "
                 f"({tv_result['total_nvt']} n.v.t.). "
                 f"Dekking: {gedekt} van {relevant} ({pct}%) — "
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
        lines.append(_bd_stats_line(bd_r))
        lines.append('')

        # RSGBPlus: subsecties
        if 'rsgb_subgroups' in bd_r:
            _write_rsgb_sections(lines, bd_r, ggm_path_map, bd_name)
        else:
            _write_bd_table(lines, bd_r, ggm_path_map, bd_name)

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


def _bd_stats_line(bd_r):
    """Scriptgegenereerde statistiekregel per beleidsdomein (nooit stale, want
    altijd vers berekend — de Beoordeling-proza hoeft deze aantallen dus niet
    te herhalen). n.v.t. (abstract/proces/actor/rol) telt niet mee in het
    dekkingspercentage — dat gaat alleen over daadwerkelijk BO-relevante
    entiteiten (total - nvt), niet over alles wat bewust buiten scope viel."""
    total = bd_r['entity_count']
    nvt = bd_r['nvt']
    relevant = total - nvt
    gedekt = bd_r['match_count'] + bd_r['ondersteunend']
    pct = round(100 * gedekt / relevant) if relevant else 0
    return (f"{total} GGM-entiteiten ({nvt} n.v.t.): {bd_r['match_count']} met BO, "
            f"{bd_r['ondersteunend']} ondersteunend aan BO, "
            f"{bd_r['niet_gedekt']} niet gedekt. "
            f"Dekking: {gedekt} van {relevant} ({pct}%).")


def _write_entity_table(lines, bo_matches, geen_match, pm, bd_name):
    """Eén samengevoegde tabel: BO-matches en niet-gematchte entiteiten,
    alfabetisch op GGM-entiteitnaam. De BO/Dekking-kolom toont óf de directe
    BO-link (✅) óf de beschrijft/via/typering/n.v.t./⚠️-route."""
    rows = []
    for m in bo_matches:
        rows.append({
            'ggm_name': m['ggm_name'],
            'bo_dekking': f"[[{m['bo_path']}\\|{m['bo_naam']}]] ✅",
            'entiteitstype': m['entiteitstype'], 'naamoverlap': m['naamoverlap'],
            'beoordeling': m['beoordeling'],
        })
    for g in geen_match:
        rows.append({
            'ggm_name': g['ggm_name'], 'bo_dekking': g['dekking'],
            'entiteitstype': g['entiteitstype'], 'naamoverlap': '',
            'beoordeling': g['beoordeling'],
        })
    if not rows:
        return

    lines.append('| GGM-entiteit | BO / Dekking | Entiteitstype | Naamoverlap | Beoordeling |')
    lines.append('|---|---|---|---|---|')
    for r in sorted(rows, key=lambda x: x['ggm_name']):
        gl = ggm_link(r['ggm_name'], bd_name, pm)
        lines.append(f"| {gl} | {r['bo_dekking']} | {r['entiteitstype']} "
                     f"| {r['naamoverlap']} | {r['beoordeling']} |")
    lines.append('')


def _write_bd_table(lines, bd_r, pm, bd_name):
    _write_entity_table(lines, bd_r['bo_matches'], bd_r['geen_match'], pm, bd_name)


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
        _write_entity_table(lines, data['bo_matches'], data['geen_match'], pm, bd_name)


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
    total_nvt = sum(r['total_nvt'] for r in all_tv_results.values())
    total_relevant = total_ent - total_nvt
    total_gedekt = total_match + total_ondersteunend
    pct_all = round(100 * total_gedekt / total_relevant) if total_relevant else 0
    lines.append(f"{total_ent} GGM-entiteiten ({total_nvt} n.v.t.). "
                 f"Dekking: {total_gedekt} gedekt van {total_relevant} relevante ({pct_all}%), "
                 f"{total_niet_gedekt} niet gedekt. {total_hiaten} BO's zonder GGM-entiteit.")
    lines.append('')
    lines.append("| Taakveld | Beleidsdomein | GGM-entiteiten | n.v.t. | Entiteiten met BO "
                 "| Entiteiten ondersteunend aan BO | Niet gedekt | Dekking "
                 "| BO zonder GGM-entiteit |")
    lines.append('|---|---|---|---|---|---|---|---|---|')

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
            relevant = total - bd_r['nvt']
            gedekt = bd_r['match_count'] + bd_r['ondersteunend']
            pct = f"{round(100 * gedekt / relevant)}%" if relevant else "—"
            lines.append(
                f"| {tv_col} | {bd_name} | {total} | {bd_r['nvt']} | {bd_r['match_count']} "
                f"| {bd_r['ondersteunend']} | {bd_r['niet_gedekt']} | {pct} "
                f"| |"
            )

        if tv_hiaten:
            tv_col = f"**{rapport}**" if not tv_r['beleidsdomeinen'] else ""
            lines.append(
                f"| {tv_col} | | | | | | | | {len(tv_hiaten)} |"
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

def run_full_analysis(taakveld_filter=None, verbose=True):
    """Laad GGM+BO-data en bereken de volledige entiteitendekking-analyse.

    Herbruikt door zowel main() als tools/entiteitendekking_sync_bo.py, zodat
    er maar één plek is die de matching/classificatie-pipeline uitvoert.

    Retourneert (all_tv_results, hiaten_by_tv, ggm_path_map, bo_by_guid,
    bo_by_name, all_bos).
    """
    if verbose:
        print("Loading data...")
    ggm_data, objecttypes = load_ggm()
    bo_by_guid, bo_by_name, all_bos, specialisatie_by_guid, via_kandidaat_by_guid = load_bo_pages()
    ggm_path_map = load_ggm_path_map()
    graph = RelationGraph(ggm_data, objecttypes)
    excluded_ids = find_excluded_ids(objecttypes, graph, bo_by_guid, specialisatie_by_guid)

    if verbose:
        print(f"  GGM: {len(objecttypes)} Objecttype, {len(bo_by_guid)} BO's, "
              f"{len(excluded_ids)} excluded")

    tv_merge, bd_merge = build_hierarchy_merges(ggm_data)
    tv_structure = build_taakveld_structure(objecttypes, excluded_ids, bo_by_guid, tv_merge, bd_merge)
    hiaten_by_tv = find_hiaten(all_bos, bo_by_guid)

    if taakveld_filter:
        tv_structure = {tv: bds for tv, bds in tv_structure.items()
                        if taakveld_filter in tv or taakveld_filter == slugify(tv)}

    all_tv_results = {}
    for tv_name in sorted(tv_structure.keys(), key=taakveld_sort_key):
        bd_entities = tv_structure[tv_name]
        tv_result = process_taakveld(
            tv_name, bd_entities, objecttypes, graph,
            bo_by_guid, bo_by_name, all_bos, specialisatie_by_guid, via_kandidaat_by_guid)

        all_tv_results[tv_name] = tv_result
        if verbose:
            slug = tv_result['slug']
            tv_hiaten = hiaten_by_tv.get(slug, [])
            bd_summary = ', '.join(
                f"{bd}({r['match_count']})" for bd, r in sorted(tv_result['beleidsdomeinen'].items()))
            print(f"  {tv_name}: {tv_result['total_entities']} ent, "
                  f"{tv_result['total_matches']} matches, "
                  f"{len(tv_hiaten)} hiaten, {tv_result['total_review']} review "
                  f"[{bd_summary}]")

    return all_tv_results, hiaten_by_tv, ggm_path_map, bo_by_guid, bo_by_name, all_bos


def main():
    parser = argparse.ArgumentParser(description='Entiteitendekking: GGM-analyse per taakveld')
    parser.add_argument('--taakveld', type=str, help='Filter op taakveld (nummer of naam)')
    parser.add_argument('--all', action='store_true', help='Alle taakvelden')
    parser.add_argument('--dry-run', action='store_true', help='Alleen counts tonen')
    args = parser.parse_args()

    if not args.taakveld and not args.all:
        parser.error('Specify --taakveld or --all')

    all_tv_results, hiaten_by_tv, ggm_path_map, bo_by_guid, bo_by_name, all_bos = \
        run_full_analysis(taakveld_filter=args.taakveld)

    if not args.dry_run:
        for tv_name, tv_result in all_tv_results.items():
            slug = tv_result['slug']
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
