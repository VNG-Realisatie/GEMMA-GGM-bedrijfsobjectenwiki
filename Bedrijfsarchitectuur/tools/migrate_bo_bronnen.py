#!/usr/bin/env python3
"""Migrate BO frontmatter: replace gerelateerde_begrippen with bronnen.

Maps each BO to relevant bronsamenvattingen based on its domain/directory.
"""

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
WIKI_BO = BASE / 'Wiki' / 'Bedrijfsobjecten'
WIKI_BS = BASE / 'Wiki' / 'Bronsamenvattingen'

DOMAIN_MAP = {
    '6-sociaal-domein/inburgering': [
        'Bronsamenvattingen/Asiel en Integratie/vng-inburgering.md',
        'Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer.md',
    ],
    '6-sociaal-domein/terug-en-invordering': [
        'Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding.md',
    ],
    '9-interne-organisatie/financien': [
        'Bronsamenvattingen/Financien/raadgever-gemeentebegroting.md',
        'Bronsamenvattingen/Financien/raadgever-inkomstenbronnen.md',
    ],
    '99-kern': [
        'Bronsamenvattingen/Belastingen/raadgever-woz.md',
    ],
}

SPECIAL = {
    'Bestuursovereenkomst': [
        'Bronsamenvattingen/Asiel en Integratie/vng-asielopvang.md',
    ],
    'Opvanglocatie': [
        'Bronsamenvattingen/Asiel en Integratie/vng-asielopvang.md',
        'Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel.md',
    ],
    'Kwijtschelding': [
        'Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding.md',
    ],
}


def get_bronnen(md_path: Path, naam: str) -> list[str]:
    if naam in SPECIAL:
        return SPECIAL[naam]

    rel = md_path.relative_to(WIKI_BO)
    parts = str(rel.parent).replace('\\', '/')

    for prefix, bronnen in DOMAIN_MAP.items():
        if parts.startswith(prefix):
            return bronnen

    return []


def migrate_file(md_path: Path) -> str:
    content = md_path.read_text(encoding='utf-8')

    naam_match = re.search(r'^naam:\s*"?([^"\n]+)"?\s*$', content, re.MULTILINE)
    naam = naam_match.group(1).strip() if naam_match else ''

    bronnen = get_bronnen(md_path, naam)

    if 'gerelateerde_begrippen:' in content:
        content = re.sub(
            r'^gerelateerde_begrippen:.*$',
            'bronnen: [' + ', '.join(f'"{b}"' for b in bronnen) + ']',
            content,
            count=1,
            flags=re.MULTILINE,
        )
    elif 'bronnen:' not in content:
        content = content.replace(
            'gemma_definitie:',
            'bronnen: [' + ', '.join(f'"{b}"' for b in bronnen) + ']\ngemma_definitie:',
            1,
        )

    md_path.write_text(content, encoding='utf-8')
    return f'{naam}: {len(bronnen)} bronnen'


def main():
    count = 0
    for md in sorted(WIKI_BO.rglob('*.md')):
        if md.name == 'map.md':
            continue
        result = migrate_file(md)
        print(f'  ✅ {result}')
        count += 1
    print(f'\nDone: {count} files migrated')


if __name__ == '__main__':
    main()
