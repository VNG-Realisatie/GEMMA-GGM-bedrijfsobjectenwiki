#!/usr/bin/env python3
"""Genereer Wiki/GGM markdown-bestanden vanuit ggm_parsed.json.

Eén bestand per beleidsdomein, plus parent-bestanden voor taakvelden
die meerdere beleidsdomeinen bevatten. Telt alleen Objecttype-entiteiten.

Gebruik:
    python tools/generate_ggm_wiki.py [--dry-run]
"""
import json
import re
import sys
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import date

BASE = Path(__file__).resolve().parent.parent
GGM_JSON = BASE / "Sources/GGM-repository/ggm_parsed.json"
OUT_DIR = BASE / "Wiki/GGM"

TAAKVELD_DIRS = {
    "0 Bestuur, Politiek en Ondersteuning": "0-bestuur-politiek-en-ondersteuning",
    "1 Veiligheid en Vergunningen": "1-veiligheid-en-vergunningen",
    "2 Verkeer, Vervoer en Waterstaat": "2-verkeer-vervoer-en-waterstaat",
    "3 Economie": "3-economie",
    "4 Onderwijs": "4-onderwijs",
    "5 Sport, Cultuur en Recreatie": "5-sport-cultuur-en-recreatie",
    "6 Sociaal Domein": "6-sociaal-domein",
    "7 Volksgezondheid en Milieu": "7-volksgezondheid-en-milieu",
    "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing": "8-volkshuisvesting-leefomgeving",
    "9 Interne Organisatie": "9-interne-organisatie",
    "10 Dienstverlening": "10-dienstverlening",
    "99 Kern": "99-kern",
    # Parent-domeinen die zelf als taakveld fungeren
    "Erfgoed": "5-sport-cultuur-en-recreatie",
    "Inkomen": "6-sociaal-domein",
    "Schulden": "6-sociaal-domein",
}


def slug(name):
    """Naam → bestandsnaam slug."""
    s = name.lower().strip()
    s = s.replace(" ", "-").replace(",", "").replace("(", "").replace(")", "")
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def clean_html(text):
    """Verwijder HTML-tags en entities uit GGM-documentatie."""
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace("&#235;", "ë").replace("&#225;", "á")
    text = text.replace("&#233;", "é").replace("&#237;", "í")
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def load_data():
    with open(GGM_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_domain_model(data):
    """Bouw per-beleidsdomein model met entiteiten, relaties, generalisaties."""
    domains = defaultdict(lambda: {
        "entities": [],
        "taakveld": "",
        "definition": "",
        "diagrams": defaultdict(list),
        "enums": 0,
        "no_stereotype": 0,
    })

    entity_by_id = {}
    entity_bd = {}

    for eid, e in data['entities'].items():
        bd = e.get('beleidsdomein', '(geen)')
        tv = e.get('taakveld', '(geen)')
        stereo = e.get('stereotype', '')

        domains[bd]["taakveld"] = tv

        if stereo == 'Objecttype':
            entity_by_id[eid] = e
            entity_bd[eid] = bd
            domains[bd]["entities"].append(e)
            for dname in e.get('diagram_names', []):
                domains[bd]["diagrams"][dname].append(e)
        elif stereo == 'Enumeratie':
            domains[bd]["enums"] += 1
        elif stereo == '':
            domains[bd]["no_stereotype"] += 1

    # Package-definities ophalen voor beleidsdomein-beschrijvingen
    for pid, p in data['packages'].items():
        pname = p.get('name', '')
        pstereo = p.get('stereotype', '')
        pdoc = p.get('documentation', '')
        if pstereo == 'Domein' and pdoc and pname in domains:
            domains[pname]["definition"] = clean_html(pdoc)

    # Relaties per beleidsdomein (alleen tussen Objecttypen in hetzelfde domein)
    domain_rels = defaultdict(list)
    for rid, r in data['relations'].items():
        sid = r.get('source_id', '')
        tid = r.get('target_id', '')
        uml = r.get('uml_type', '')
        if uml not in ('Association', 'Aggregation', 'Composition'):
            continue
        if sid in entity_by_id and tid in entity_by_id:
            sbd = entity_bd[sid]
            tbd = entity_bd[tid]
            if sbd == tbd:
                domain_rels[sbd].append(r)

    # Generalisaties per beleidsdomein
    domain_gens = defaultdict(list)
    for rid, r in data['relations'].items():
        if r.get('uml_type') != 'Generalization':
            continue
        sid = r.get('source_id', '')
        tid = r.get('target_id', '')
        if sid in entity_by_id or tid in entity_by_id:
            sname = r.get('source_name_ea', '') or data['entities'].get(sid, {}).get('name', '?')
            tname = r.get('target_name_ea', '') or data['entities'].get(tid, {}).get('name', '?')
            # source = child, target = parent in EA Generalization
            sbd = entity_bd.get(sid, entity_bd.get(tid, ''))
            if sbd:
                domain_gens[sbd].append({
                    "child": sname,
                    "parent": tname,
                    "child_abstract": data['entities'].get(sid, {}).get('is_abstract', False),
                })

    # Taakveld → beleidsdomeinen mapping
    tv_children = defaultdict(list)
    for bd, info in domains.items():
        if bd == '(geen)':
            continue
        tv_children[info["taakveld"]].append(bd)

    return domains, domain_rels, domain_gens, tv_children, entity_by_id


def render_entity_table(entities):
    """Render entiteitstabel."""
    lines = []
    lines.append("| Entiteit | Definitie | Attributen | Abstract | Herkomst |")
    lines.append("|---|---|---|---|---|")
    for e in sorted(entities, key=lambda x: x['name']):
        name = e['name']
        doc = clean_html(e.get('documentation', ''))
        if not doc:
            doc = clean_html(e.get('gemma_tags', {}).get('gemma_definitie', ''))
        if not doc:
            doc = "*(geen definitie in GGM)*"
        attrs = ", ".join(e.get('attributes', [])) or "*(geen attributen)*"
        abstract = "Ja" if e.get('is_abstract') else "Nee"
        herkomst = e.get('tags', {}).get('Herkomst', '') or 'GGM'
        lines.append(f"| **{name}** | {doc} | {attrs} | {abstract} | {herkomst} |")
    return "\n".join(lines)


def render_generalizations(gens):
    """Render overervingshiërarchie."""
    if not gens:
        return ""
    # Groepeer per parent
    parent_children = defaultdict(list)
    for g in gens:
        parent_children[g["parent"]].append(g["child"])
    lines = ["## Overervingshiërarchie", ""]
    for parent in sorted(parent_children):
        lines.append("```")
        lines.append(f"{parent} (abstract)")
        for child in sorted(parent_children[parent]):
            lines.append(f"    └── {child}")
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def render_relations(rels, entity_by_id):
    """Render relatiediagrammen per diagram."""
    if not rels:
        return ""
    lines = ["## Relatiediagrammen", "", "```"]
    seen = set()
    for r in sorted(rels, key=lambda x: (x.get('source_name_ea', ''), x.get('target_name_ea', ''))):
        sname = r.get('source_name_ea', '?')
        tname = r.get('target_name_ea', '?')
        scard = r.get('source_card', '') or ''
        tcard = r.get('target_card', '') or ''
        rname = r.get('name', '')
        # Bepaal relatielabel uit documentation of name
        label = clean_html(r.get('documentation', '')) or rname or ''
        key = (sname, tname, scard, tcard)
        if key in seen:
            continue
        seen.add(key)
        spart = f"{sname} [{scard}]" if scard else sname
        tpart = f"{tname} [{tcard}]" if tcard else tname
        if label and not re.match(r'^[\d.*]+$', label):
            lines.append(f"{spart} ──── {tpart} ({label})")
        else:
            lines.append(f"{spart} ──── {tpart}")
    lines.append("```")
    return "\n".join(lines)


def render_domain_file(bd, info, rels, gens, entity_by_id):
    """Genereer markdown voor één beleidsdomein."""
    entities = info["entities"]
    n_obj = len(entities)
    tv = info["taakveld"]
    definition = info["definition"] or f"Beleidsdomein {bd} binnen taakveld {tv}."

    # Frontmatter
    lines = [
        "---",
        "type: ggm-beleidsdomein",
        f"naam: {bd}",
        f'definitie: "{definition}"',
        f'taakveld: "{tv}"',
        f"aantal_entiteiten: {n_obj}",
        "---",
        "",
        f"# GGM Beleidsdomein: {bd}",
        "",
    ]

    # Entiteiten per diagramgroep
    diagram_entities = info["diagrams"]
    if diagram_entities:
        # Gebruik diagramgroepen als secties
        placed = set()
        for dname in sorted(diagram_entities.keys()):
            d_ents = [e for e in diagram_entities[dname] if e['id'] not in placed]
            if not d_ents:
                continue
            lines.append(f"### {dname}")
            lines.append("")
            lines.append(render_entity_table(d_ents))
            lines.append("")
            for e in d_ents:
                placed.add(e['id'])

        # Overgebleven entiteiten (niet op een diagram)
        remaining = [e for e in entities if e['id'] not in placed]
        if remaining:
            lines.append("### Overig")
            lines.append("")
            lines.append(render_entity_table(remaining))
            lines.append("")
    else:
        lines.append("## Entiteiten")
        lines.append("")
        lines.append(render_entity_table(entities))
        lines.append("")

    # Generalisaties
    gen_text = render_generalizations(gens)
    if gen_text:
        lines.append(gen_text)

    # Relaties
    rel_text = render_relations(rels, entity_by_id)
    if rel_text:
        lines.append(rel_text)
        lines.append("")

    # Observaties
    lines.append("## Observaties")
    lines.append("")
    obs = [f"- Dit beleidsdomein bevat {n_obj} Objecttype-entiteiten"]
    if info["enums"]:
        obs[0] += f" (+ {info['enums']} Enumeraties"
        if info["no_stereotype"]:
            obs[0] += f", {info['no_stereotype']} diagramhulpobjecten zonder stereotype"
        obs[0] += ")."
    elif info["no_stereotype"]:
        obs[0] += f" (+ {info['no_stereotype']} diagramhulpobjecten zonder stereotype)."
    else:
        obs[0] += "."

    if diagram_entities:
        dg_summary = ", ".join(
            f"{dname} ({len(ents)})"
            for dname, ents in sorted(diagram_entities.items())
        )
        obs.append(f"- Entiteiten zijn gegroepeerd in {len(diagram_entities)} diagramgroepen: {dg_summary}.")
    if gens:
        obs.append(f"- Er zijn {len(gens)} generalisatierelaties aanwezig.")
    lines.extend(obs)
    lines.append("")

    return "\n".join(lines)


def render_parent_file(parent_name, parent_tv, children, domains, domain_gens):
    """Genereer parent-bestand dat sub-beleidsdomeinen samenvat."""
    total_obj = sum(len(domains[c]["entities"]) for c in children)
    definition = domains.get(parent_name, {}).get("definition", "")
    if not definition:
        # Probeer package-definitie
        definition = f"Overkoepelend beleidsdomein met {len(children)} sub-domeinen."

    lines = [
        "---",
        "type: ggm-beleidsdomein",
        f"naam: {parent_name}",
        f'definitie: "{definition}"',
        f'taakveld: "{parent_tv}"',
        f"aantal_entiteiten: {total_obj}",
        f"beleidsdomeinen: [{', '.join(children)}]",
        "---",
        "",
        f"# GGM Beleidsdomein: {parent_name}",
        "",
        f"Overkoepelend beleidsdomein binnen taakveld \"{parent_tv}\".",
        "",
        "## Sub-beleidsdomeinen",
        "",
    ]
    for c in sorted(children):
        n = len(domains[c]["entities"])
        cslug = slug(c)
        lines.append(f"- [[{cslug}|{c}]] ({n} entiteiten)")
    lines.append("")
    lines.append("## Observaties")
    lines.append("")
    lines.append(f"- Totaal {total_obj} Objecttype-entiteiten over {len(children)} sub-beleidsdomeinen.")

    # Tel enums en no-stereotype over kinderen
    total_enum = sum(domains[c].get("enums", 0) for c in children)
    total_ns = sum(domains[c].get("no_stereotype", 0) for c in children)
    if total_enum or total_ns:
        parts = []
        if total_enum:
            parts.append(f"{total_enum} Enumeraties")
        if total_ns:
            parts.append(f"{total_ns} diagramhulpobjecten")
        lines.append(f"- Daarnaast {', '.join(parts)} (niet meegeteld).")

    total_gens = sum(len(domain_gens.get(c, [])) for c in children)
    if total_gens:
        lines.append(f"- Er zijn {total_gens} generalisatierelaties aanwezig.")
    lines.append("")

    return "\n".join(lines)


def detect_parents(data, domains):
    """Detecteer tussenliggende parent-domeinen (bijv. Erfgoed, Inkomen, Schulden).

    Alleen Domein-packages die:
    1. Kinderen hebben die ook Domein zijn met Objecttype-entiteiten
    2. Zelf GEEN top-level taakveld zijn (naam begint niet met cijfer)
    """
    parents = {}

    for pid, p in data['packages'].items():
        if p.get('stereotype') != 'Domein':
            continue
        pname = p['name']
        if re.match(r'^\d', pname):
            continue

        children = []
        for cid, cp in data['packages'].items():
            if cp.get('parent_id') == pid and cp.get('stereotype') == 'Domein':
                if cp['name'] in domains and domains[cp['name']]["entities"]:
                    children.append(cp['name'])
        if len(children) > 1:
            parent_of_parent = data['packages'].get(p.get('parent_id', ''), {})
            tv = parent_of_parent.get('name', '') or pname
            parents[pname] = {"taakveld": tv, "children": children}

    return parents


def main():
    dry_run = '--dry-run' in sys.argv

    print("Loading ggm_parsed.json...")
    data = load_data()
    print(f"  {len(data['entities'])} entities, {len(data['relations'])} relations")

    print("Building domain model...")
    domains, domain_rels, domain_gens, tv_children, entity_by_id = build_domain_model(data)
    print(f"  {len(domains)} beleidsdomeinen")

    # Detecteer parent-domeinen
    parents = detect_parents(data, domains)
    print(f"  {len(parents)} parent-domeinen: {list(parents.keys())}")

    if not dry_run:
        # Backup en maak output directory schoon
        if OUT_DIR.exists():
            backup = OUT_DIR.parent / f"GGM.bak-{date.today().isoformat()}"
            if backup.exists():
                shutil.rmtree(backup)
            shutil.copytree(OUT_DIR, backup)
            print(f"  Backup: {backup}")
            shutil.rmtree(OUT_DIR)
        OUT_DIR.mkdir(parents=True, exist_ok=True)

    files_written = 0
    total_entities = 0

    # Genereer per beleidsdomein
    for bd, info in sorted(domains.items(), key=lambda x: (x[1]["taakveld"], x[0])):
        if bd == '(geen)' or not info["entities"]:
            continue

        tv = info["taakveld"]
        tv_dir_name = TAAKVELD_DIRS.get(tv)
        if not tv_dir_name:
            # Check of tv een parent is waarvan de children in een bekende dir zitten
            for pname, pinfo in parents.items():
                if bd in pinfo.get("children", []):
                    parent_tv = pinfo["taakveld"]
                    tv_dir_name = TAAKVELD_DIRS.get(parent_tv)
                    break
        if not tv_dir_name:
            print(f"  SKIP {bd} (taakveld '{tv}' niet in TAAKVELD_DIRS)")
            continue

        outdir = OUT_DIR / tv_dir_name
        filename = slug(bd) + ".md"
        filepath = outdir / filename

        content = render_domain_file(
            bd, info,
            domain_rels.get(bd, []),
            domain_gens.get(bd, []),
            entity_by_id
        )

        n = len(info["entities"])
        total_entities += n

        if dry_run:
            print(f"  [DRY] {filepath.relative_to(BASE)} ({n} entiteiten)")
        else:
            outdir.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content, encoding='utf-8')
            files_written += 1

    # Genereer parent-bestanden
    for pname, pinfo in sorted(parents.items()):
        tv = pinfo["taakveld"]
        tv_dir_name = TAAKVELD_DIRS.get(tv) or TAAKVELD_DIRS.get(pname)
        if not tv_dir_name:
            print(f"  SKIP parent {pname} (geen dir mapping)")
            continue

        outdir = OUT_DIR / tv_dir_name
        filename = slug(pname) + ".md"
        filepath = outdir / filename

        content = render_parent_file(pname, tv, pinfo["children"], domains, domain_gens)

        if dry_run:
            n = sum(len(domains[c]["entities"]) for c in pinfo["children"])
            print(f"  [DRY] {filepath.relative_to(BASE)} (parent, {n} entiteiten)")
        else:
            outdir.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content, encoding='utf-8')
            files_written += 1

    # Genereer structuur-ggm.md (overzicht taakvelden)
    struct_content = render_structure(data, domains, parents)
    struct_path = OUT_DIR / "structuur-ggm.md"
    if dry_run:
        print(f"  [DRY] {struct_path.relative_to(BASE)}")
    else:
        struct_path.write_text(struct_content, encoding='utf-8')
        files_written += 1

    print(f"\nResultaat: {files_written} bestanden geschreven, {total_entities} Objecttype-entiteiten")
    if dry_run:
        print("(dry run — geen bestanden geschreven)")


def render_structure(data, domains, parents):
    """Genereer structuur-ggm.md overzicht."""
    # Groepeer beleidsdomeinen per taakveld
    tv_bds = defaultdict(list)
    for bd, info in domains.items():
        if bd == '(geen)' or not info["entities"]:
            continue
        tv = info["taakveld"]
        tv_bds[tv].append((bd, len(info["entities"])))

    lines = [
        "---",
        "type: ggm-overzicht",
        "naam: Structuur GGM",
        f"gegenereerd: {date.today().isoformat()}",
        "---",
        "",
        "# Structuur GGM",
        "",
        "Overzicht van taakvelden en beleidsdomeinen in het Gemeentelijk Gegevensmodel.",
        "Alleen Objecttype-entiteiten geteld (Enumeraties en diagramhulpobjecten niet meegeteld).",
        "",
    ]

    # Sorteer taakvelden
    def tv_sort_key(tv):
        m = re.match(r'^(\d+)', tv)
        return (int(m.group(1)) if m else 999, tv)

    all_tvs = set(tv_bds.keys())
    # Voeg parent-domeinen toe als sub-taakveld
    parent_tvs = set(parents.keys())

    for tv in sorted(all_tvs - parent_tvs, key=tv_sort_key):
        bds = sorted(tv_bds[tv], key=lambda x: x[0])
        total = sum(n for _, n in bds)
        lines.append(f"## {tv} ({total} entiteiten)")
        lines.append("")
        for bd, n in bds:
            bslug = slug(bd)
            # Check of dit een parent is
            if bd in parents:
                children = parents[bd]["children"]
                child_list = ", ".join(f"{c} ({len(domains[c]['entities'])})" for c in sorted(children))
                lines.append(f"- **{bd}** ({n}) — sub-domeinen: {child_list}")
            else:
                lines.append(f"- [[{bslug}|{bd}]] ({n})")
        lines.append("")

    # Parent-domeinen als eigen sectie
    for pname in sorted(parent_tvs):
        if pname not in tv_bds:
            continue
        bds = sorted(tv_bds[pname], key=lambda x: x[0])
        total = sum(n for _, n in bds)
        parent_tv = parents[pname]["taakveld"]
        lines.append(f"## {pname} ({total} entiteiten) — sub-domein van {parent_tv}")
        lines.append("")
        for bd, n in bds:
            bslug = slug(bd)
            lines.append(f"- [[{bslug}|{bd}]] ({n})")
        lines.append("")

    # Totaalstatistiek
    grand_total = sum(len(info["entities"]) for info in domains.values() if info["entities"])
    n_domains = sum(1 for info in domains.values() if info["entities"])
    lines.append(f"**Totaal:** {grand_total} Objecttype-entiteiten in {n_domains} beleidsdomeinen.")
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
