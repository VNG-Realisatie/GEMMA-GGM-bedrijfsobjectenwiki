#!/usr/bin/env python3
"""Parse GGM XMI 2.1 export and extract entities, relations, packages, and diagrams.

Outputs JSON with all data needed for BO frontmatter enrichment and CSV export.
"""

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    'xmi': 'http://schema.omg.org/spec/XMI/2.1',
    'uml': 'http://schema.omg.org/spec/UML/2.1',
}


def parse_xmi(xmi_path: str) -> dict:
    tree = ET.parse(xmi_path)
    root = tree.getroot()

    uml_model = root.find('uml:Model', NS)
    extension = root.find('xmi:Extension', NS)

    packages = {}
    package_children = {}
    entities = {}
    relations_uml = {}
    generalizations = {}
    diagrams = {}

    # --- Phase 1: Parse UML model for package hierarchy and entity/relation structure ---
    _parse_uml_packages(uml_model, packages, package_children, entities,
                        relations_uml, generalizations)

    # --- Phase 2: Parse EA extension for rich metadata ---
    elements_section = extension.find('elements')
    if elements_section is not None:
        _parse_ea_elements(elements_section, packages, entities)

    connectors_section = extension.find('connectors')
    if connectors_section is not None:
        _parse_ea_connectors(connectors_section, relations_uml)

    diagrams_section = extension.find('diagrams')
    if diagrams_section is not None:
        _parse_ea_diagrams(diagrams_section, packages, diagrams)

    # --- Phase 3: Build package hierarchy paths ---
    package_hierarchy = _build_package_hierarchy(packages, package_children)

    # --- Phase 4: Resolve entity package paths ---
    for eid, entity in entities.items():
        pkg_id = entity.get('package_id')
        if pkg_id and pkg_id in package_hierarchy:
            entity['package_path'] = package_hierarchy[pkg_id]
            _extract_domain_info(entity, package_hierarchy[pkg_id], packages)

    # --- Phase 5: Build diagram-entity mapping ---
    diagram_entities = {}
    for did, diag in diagrams.items():
        subjects = diag.get('subjects', [])
        entity_refs = [s for s in subjects if s in entities]
        diagram_entities[did] = entity_refs
        for eid in entity_refs:
            entities[eid].setdefault('diagram_ids', []).append(did)
            entities[eid].setdefault('diagram_names', []).append(diag['name'])

    # --- Phase 6: Build relations with resolved names ---
    relations = {}
    for rid, rel in relations_uml.items():
        source_id = rel.get('source_id', '')
        target_id = rel.get('target_id', '')
        rel['source_name'] = entities.get(source_id, {}).get('name', '')
        rel['target_name'] = entities.get(target_id, {}).get('name', '')
        if source_id in entities and target_id in entities:
            relations[rid] = rel

    # --- Phase 7: Add generalizations as relations ---
    for gid, gen in generalizations.items():
        parent_id = gen.get('general', '')
        child_id = gen.get('specific', '')
        relations[gid] = {
            'id': gid,
            'name': '',
            'uml_type': 'Generalization',
            'source_id': child_id,
            'target_id': parent_id,
            'source_name': entities.get(child_id, {}).get('name', ''),
            'target_name': entities.get(parent_id, {}).get('name', ''),
            'source_card': '',
            'target_card': '',
            'documentation': '',
            'tags': {},
        }

    return {
        'entities': entities,
        'relations': relations,
        'packages': packages,
        'diagrams': diagrams,
        'diagram_entities': diagram_entities,
    }


def _parse_uml_packages(element, packages, package_children, entities,
                         relations, generalizations, parent_id=None):
    for child in element:
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if tag != 'packagedElement':
            continue

        xmi_type = child.get(f'{{{NS["xmi"]}}}type', '')
        xmi_id = child.get(f'{{{NS["xmi"]}}}id', '')
        name = child.get('name', '').strip()

        if xmi_type == 'uml:Package':
            packages[xmi_id] = {'id': xmi_id, 'name': name, 'parent_id': parent_id}
            package_children.setdefault(parent_id, []).append(xmi_id)
            _parse_uml_packages(child, packages, package_children, entities,
                                relations, generalizations, parent_id=xmi_id)

        elif xmi_type == 'uml:Class':
            entity = {
                'id': xmi_id,
                'name': name,
                'uml_type': 'Class',
                'package_id': parent_id,
                'attributes': [],
                'tags': {},
                'gemma_tags': {},
            }
            for attr in child.findall('ownedAttribute'):
                if attr.get('association'):
                    continue
                attr_name = attr.get('name', '')
                if attr_name:
                    entity['attributes'].append(attr_name)
            for gen in child.findall(f'{{{NS["uml"]}}}Generalization'):
                gen_id = gen.get(f'{{{NS["xmi"]}}}id', '')
                general = gen.get('general', '')
                if gen_id and general:
                    generalizations[gen_id] = {
                        'general': general,
                        'specific': xmi_id,
                    }
            entities[xmi_id] = entity

        elif xmi_type == 'uml:Enumeration':
            entity = {
                'id': xmi_id,
                'name': name,
                'uml_type': 'Enumeration',
                'package_id': parent_id,
                'literals': [],
                'tags': {},
                'gemma_tags': {},
            }
            for lit in child.findall(f'{{{NS["uml"]}}}ownedLiteral'):
                lit_name = lit.get('name', '')
                if lit_name:
                    entity['literals'].append(lit_name)
            entities[xmi_id] = entity

        elif xmi_type == 'uml:Association':
            _parse_uml_association(child, relations)


def _parse_uml_association(assoc_elem, relations):
    xmi_id = assoc_elem.get(f'{{{NS["xmi"]}}}id', '')
    name = assoc_elem.get('name', '')

    ends = []
    for owned_end in assoc_elem.findall('ownedEnd'):
        type_ref = owned_end.find('type')
        type_id = ''
        if type_ref is not None:
            type_id = type_ref.get(f'{{{NS["xmi"]}}}idref', '')
        else:
            type_id = owned_end.get('type', '')
            if not type_id:
                for child in owned_end:
                    idref = child.get(f'{{{NS["xmi"]}}}idref', '')
                    if idref:
                        type_id = idref
                        break

        lower = ''
        upper = ''
        lv = owned_end.find(f'{{{NS["uml"]}}}lowerValue')
        if lv is None:
            lv = owned_end.find('lowerValue')
        uv = owned_end.find(f'{{{NS["uml"]}}}upperValue')
        if uv is None:
            uv = owned_end.find('upperValue')
        if lv is not None:
            lower = lv.get('value', '')
        if uv is not None:
            val = uv.get('value', '')
            upper = '*' if val == '-1' else val

        card = f"{lower}..{upper}" if lower and upper else ''
        eid = owned_end.get(f'{{{NS["xmi"]}}}id', '')
        ends.append({'id': eid, 'type_id': type_id, 'card': card})

    if len(ends) >= 2:
        src_end = next((e for e in ends if 'src' in e['id'].lower()), ends[0])
        tgt_end = next((e for e in ends if 'dst' in e['id'].lower()), ends[1])
        if src_end == tgt_end and len(ends) > 1:
            tgt_end = ends[1] if src_end == ends[0] else ends[0]

        relations[xmi_id] = {
            'id': xmi_id,
            'name': name,
            'uml_type': 'Association',
            'source_id': src_end['type_id'],
            'target_id': tgt_end['type_id'],
            'source_card': src_end['card'],
            'target_card': tgt_end['card'],
            'documentation': '',
            'tags': {},
        }


def _parse_ea_elements(elements_section, packages, entities):
    for elem in elements_section.findall('element'):
        idref = elem.get(f'{{{NS["xmi"]}}}idref', '')
        xmi_type = elem.get(f'{{{NS["xmi"]}}}type', '')
        name = elem.get('name', '')

        props = elem.find('properties')
        model = elem.find('model')
        tags_elem = elem.find('tags')

        if xmi_type == 'uml:Package':
            if idref in packages:
                if props is not None:
                    packages[idref]['documentation'] = props.get('documentation', '')
                    packages[idref]['stereotype'] = props.get('stereotype', '')
                if model is not None:
                    pkg_parent = model.get('package', '')
                    if pkg_parent and not packages[idref].get('parent_id'):
                        packages[idref]['parent_id'] = pkg_parent
                if tags_elem is not None:
                    packages[idref]['tags'] = _extract_tags(tags_elem)

        elif xmi_type in ('uml:Class', 'uml:Enumeration'):
            if idref not in entities:
                continue
            entity = entities[idref]

            if props is not None:
                entity['documentation'] = props.get('documentation', '')
                entity['stereotype'] = props.get('stereotype', '')
                entity['is_abstract'] = props.get('isAbstract', 'false') == 'true'

            if model is not None:
                pkg = model.get('package', '')
                if pkg:
                    entity['package_id'] = pkg

            ext_props = elem.find('extendedProperties')
            if ext_props is not None:
                entity['package_name'] = ext_props.get('package_name', '')

            if tags_elem is not None:
                for tag in tags_elem.findall('tag'):
                    tag_name = tag.get('name', '')
                    tag_value = tag.get('value', '')
                    clean_value = _clean_tag_value(tag_value)

                    if tag_name.startswith('GEMMA'):
                        gemma_key = tag_name.replace(' ', '_').lower()
                        entity['gemma_tags'][gemma_key] = clean_value
                    elif tag_name in ('Toelichting', 'Synoniemen', 'Herkomst',
                                      'Herkomst definitie', 'Begrip', 'Kwaliteit',
                                      'Populatie', 'Datum opname',
                                      'Domein IV3', 'Domein DCAT',
                                      'Datum tijd export', 'Name'):
                        entity['tags'][tag_name] = clean_value


def _parse_ea_connectors(connectors_section, relations):
    for conn in connectors_section.findall('connector'):
        idref = conn.get(f'{{{NS["xmi"]}}}idref', '')

        props = conn.find('properties')
        source = conn.find('source')
        target = conn.find('target')
        labels = conn.find('labels')
        tags_elem = conn.find('tags')
        docs = conn.find('documentation')

        if idref in relations:
            rel = relations[idref]
        else:
            rel = {
                'id': idref,
                'name': '',
                'uml_type': '',
                'source_id': '',
                'target_id': '',
                'source_card': '',
                'target_card': '',
                'documentation': '',
                'tags': {},
            }
            relations[idref] = rel

        if props is not None:
            ea_type = props.get('ea_type', '')
            if ea_type:
                rel['uml_type'] = ea_type
            stereotype = props.get('stereotype', '')
            if stereotype:
                rel['stereotype'] = stereotype

        if source is not None:
            model = source.find('model')
            if model is not None:
                rel['source_id'] = model.get('ea_localid', rel.get('source_id', ''))
                src_name = model.get('name', '')
                if src_name:
                    rel['source_name_ea'] = src_name
            idref_src = source.get(f'{{{NS["xmi"]}}}idref', '')
            if idref_src:
                rel['source_id'] = idref_src

        if target is not None:
            model = target.find('model')
            if model is not None:
                rel['target_id'] = model.get('ea_localid', rel.get('target_id', ''))
                tgt_name = model.get('name', '')
                if tgt_name:
                    rel['target_name_ea'] = tgt_name
            idref_tgt = target.get(f'{{{NS["xmi"]}}}idref', '')
            if idref_tgt:
                rel['target_id'] = idref_tgt

        if labels is not None:
            mt = labels.get('mt', '')
            if mt:
                rel['name'] = mt
            lb = labels.get('lb', '')
            if lb and not rel.get('source_card'):
                rel['source_card'] = lb
            rb = labels.get('rb', '')
            if rb and not rel.get('target_card'):
                rel['target_card'] = rb

        if docs is not None:
            doc_val = docs.get('value', '')
            if doc_val:
                rel['documentation'] = doc_val

        if tags_elem is not None:
            for tag in tags_elem.findall('tag'):
                tag_name = tag.get('name', '')
                tag_value = _clean_tag_value(tag.get('value', ''))
                if tag_name.startswith('GEMMA'):
                    rel.setdefault('gemma_tags', {})[
                        tag_name.replace(' ', '_').lower()] = tag_value
                else:
                    rel['tags'][tag_name] = tag_value


def _parse_ea_diagrams(diagrams_section, packages, diagrams):
    for diag in diagrams_section.findall('diagram'):
        xmi_id = diag.get(f'{{{NS["xmi"]}}}id', '')
        model = diag.find('model')
        props = diag.find('properties')
        elems = diag.find('elements')

        pkg_id = ''
        if model is not None:
            pkg_id = model.get('package', '')

        name = ''
        if props is not None:
            name = props.get('name', '')

        subjects = []
        if elems is not None:
            for e in elems.findall('element'):
                subj = e.get('subject', '')
                if subj:
                    subjects.append(subj)

        diagrams[xmi_id] = {
            'id': xmi_id,
            'name': name,
            'package_id': pkg_id,
            'subjects': subjects,
        }


def _build_package_hierarchy(packages, package_children):
    hierarchy = {}
    for pid, pkg in packages.items():
        path = []
        current = pid
        visited = set()
        while current and current in packages and current not in visited:
            visited.add(current)
            path.insert(0, {'id': current, 'name': packages[current]['name']})
            current = packages[current].get('parent_id')
        hierarchy[pid] = path
    return hierarchy


def _extract_domain_info(entity, path, packages):
    for i, node in enumerate(path):
        pkg = packages.get(node['id'], {})
        stereotype = pkg.get('stereotype', '')
        name = node['name']

        if stereotype == 'Domein' and i > 0:
            parent = path[i - 1] if i > 0 else None
            if parent:
                parent_pkg = packages.get(parent['id'], {})
                parent_stereo = parent_pkg.get('stereotype', '')
                if parent_stereo == 'Domein':
                    entity['taakveld'] = parent['name']
                    entity['beleidsdomein'] = name
                    entity['beleidsdomein_id'] = node['id']
                elif parent_stereo == 'Basismodel':
                    entity['taakveld'] = name
                    entity['beleidsdomein'] = name
                    entity['beleidsdomein_id'] = node['id']

        if name.startswith('Model '):
            entity['model_package'] = name
            entity['model_package_id'] = node['id']


def _extract_tags(tags_elem):
    result = {}
    for tag in tags_elem.findall('tag'):
        name = tag.get('name', '')
        value = _clean_tag_value(tag.get('value', ''))
        if value:
            result[name] = value
    return result


def _clean_tag_value(value: str) -> str:
    if not value:
        return ''
    if '#NOTES#' in value:
        parts = value.split('#NOTES#')
        value = parts[0].strip()
    value = value.replace('&#xA;', '\n').strip()
    return value


def main():
    base = Path(__file__).resolve().parent.parent
    repo_dir = base / 'Sources' / 'GGM-repository'

    if len(sys.argv) < 2:
        xmi_path = repo_dir / 'Gemeentelijk Gegevensmodel XMI2.1.xml'
    else:
        xmi_path = Path(sys.argv[1])

    if not xmi_path.exists():
        print(f"Error: {xmi_path} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing {xmi_path}...", file=sys.stderr)
    data = parse_xmi(str(xmi_path))

    entity_count = len(data['entities'])
    class_count = sum(1 for e in data['entities'].values() if e['uml_type'] == 'Class')
    enum_count = sum(1 for e in data['entities'].values() if e['uml_type'] == 'Enumeration')
    rel_count = len(data['relations'])
    diag_count = len(data['diagrams'])
    pkg_count = len(data['packages'])

    print(f"Entities: {entity_count} ({class_count} classes, {enum_count} enumerations)",
          file=sys.stderr)
    print(f"Relations: {rel_count}", file=sys.stderr)
    print(f"Diagrams: {diag_count}", file=sys.stderr)
    print(f"Packages: {pkg_count}", file=sys.stderr)

    output_path = repo_dir / 'ggm_parsed.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written to {output_path}", file=sys.stderr)


if __name__ == '__main__':
    main()
