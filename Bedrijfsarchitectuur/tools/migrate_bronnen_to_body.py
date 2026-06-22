#!/usr/bin/env python3
"""Migrate bronnen references from frontmatter to body sections.

BO files: moves `bronnen:` array → `## Bronnen` section with wiki-links.
Bronsamenvatting files: moves `bron:` markdown-link → `## Bronnen` section with wiki-link.
"""

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
WIKI_BO = BASE / 'Wiki' / 'Bedrijfsobjecten'
WIKI_BS = BASE / 'Wiki' / 'Bronsamenvattingen'


def split_frontmatter(content: str) -> tuple[str, str]:
    m = re.match(r'^---\n(.*?\n)---\n(.*)', content, re.DOTALL)
    if not m:
        raise ValueError("No frontmatter found")
    return m.group(1), m.group(2)


def remove_bronnen_from_fm(fm: str) -> tuple[str, list[str]]:
    """Remove bronnen: field from BO frontmatter, return (cleaned_fm, paths)."""
    lines = fm.split('\n')
    paths = []
    new_lines = []
    in_bronnen_list = False

    for line in lines:
        if line.startswith('bronnen:'):
            inline = line[len('bronnen:'):].strip()
            if inline.startswith('[') and inline.endswith(']'):
                raw = inline[1:-1]
                if raw:
                    paths = [p.strip().strip('"').strip("'") for p in raw.split(',')]
            elif inline:
                paths = [inline.strip('"').strip("'")]
            else:
                in_bronnen_list = True
            continue

        if in_bronnen_list:
            if line.startswith('  - ') or line.startswith('  -\t'):
                val = line.strip().lstrip('- ').strip('"').strip("'")
                val = re.sub(r'^\[\[(.+?)(?:\|.+?)?\]\]$', r'\1', val)
                paths.append(val)
                continue
            else:
                in_bronnen_list = False

        new_lines.append(line)

    return '\n'.join(new_lines), paths


def remove_bron_from_fm(fm: str) -> tuple[str, str]:
    """Remove bron: field from bronsamenvatting frontmatter, return (cleaned_fm, source_path)."""
    lines = fm.split('\n')
    new_lines = []
    source_path = ''

    for line in lines:
        if line.startswith('bron:'):
            val = line[len('bron:'):].strip().strip('"').strip("'")
            m = re.search(r'\]\((.*?)\)', val)
            if m:
                source_path = m.group(1)
            else:
                source_path = val
            continue
        new_lines.append(line)

    return '\n'.join(new_lines), source_path


def normalize_source_path(path: str) -> str:
    """Normalize a source path to be relative to Bedrijfsarchitectuur root."""
    path = path.replace('\\', '/')
    if '../../Sources/' in path:
        path = 'Sources/' + path.split('../../Sources/')[-1]
    elif not path.startswith('Sources/'):
        pass
    if path.endswith('.md'):
        path = path[:-3]
    return path


def normalize_bo_bron_path(path: str) -> str:
    """Normalize a BO bronnen path to a wiki-link target."""
    path = path.strip()
    if path.startswith('Wiki/'):
        return path
    if path.startswith('Bronsamenvattingen/'):
        return 'Wiki/' + path
    return path


def insert_bronnen_section(body: str, links: list[str]) -> str:
    """Insert ## Bronnen section in BO body, before ## Terugmelding GGM if present."""
    section = '\n## Bronnen\n\n' + '\n'.join(f'- [[{link}]]' for link in links) + '\n'

    if '## Terugmelding GGM' in body:
        return body.replace('## Terugmelding GGM', section.rstrip('\n') + '\n\n## Terugmelding GGM')

    return body.rstrip('\n') + '\n' + section


def append_bronnen_section(body: str, links: list[str]) -> str:
    """Append ## Bronnen section at end of body."""
    section = '\n## Bronnen\n\n' + '\n'.join(f'- [[{link}]]' for link in links) + '\n'
    return body.rstrip('\n') + '\n' + section


def migrate_bo(md_path: Path) -> str:
    content = md_path.read_text(encoding='utf-8')
    fm, body = split_frontmatter(content)
    cleaned_fm, paths = remove_bronnen_from_fm(fm)

    if not paths:
        if 'bronnen:' not in fm:
            return f'  SKIP {md_path.name}: no bronnen field'
        md_path.write_text(f'---\n{cleaned_fm}---\n{body}', encoding='utf-8')
        return f'  CLEAN {md_path.name}: empty bronnen removed'

    links = [normalize_bo_bron_path(p) for p in paths]

    if '## Bronnen' in body:
        md_path.write_text(f'---\n{cleaned_fm}---\n{body}', encoding='utf-8')
        return f'  UPDATE {md_path.name}: removed fm only (body section exists)'

    new_body = insert_bronnen_section(body, links)
    md_path.write_text(f'---\n{cleaned_fm}---\n{new_body}', encoding='utf-8')
    return f'  OK {md_path.name}: {len(links)} bronnen → body'


def migrate_bs(md_path: Path) -> str:
    content = md_path.read_text(encoding='utf-8')

    if 'bron:' not in content.split('---')[1] if content.startswith('---') else '':
        return f'  SKIP {md_path.name}: no bron field'

    fm, body = split_frontmatter(content)
    cleaned_fm, source_path = remove_bron_from_fm(fm)

    if not source_path:
        md_path.write_text(f'---\n{cleaned_fm}---\n{body}', encoding='utf-8')
        return f'  CLEAN {md_path.name}: empty bron removed'

    normalized = normalize_source_path(source_path)

    if '## Bronnen' in body:
        md_path.write_text(f'---\n{cleaned_fm}---\n{body}', encoding='utf-8')
        return f'  UPDATE {md_path.name}: removed fm only (body section exists)'

    new_body = append_bronnen_section(body, [normalized])
    md_path.write_text(f'---\n{cleaned_fm}---\n{new_body}', encoding='utf-8')
    return f'  OK {md_path.name}: bron → body'


def main():
    print('=== Migrating BO files ===')
    bo_count = 0
    for md in sorted(WIKI_BO.rglob('*.md')):
        if md.name == 'map.md':
            continue
        print(migrate_bo(md))
        bo_count += 1

    print(f'\nBO files processed: {bo_count}')

    print('\n=== Migrating Bronsamenvatting files ===')
    bs_count = 0
    for md in sorted(WIKI_BS.rglob('*.md')):
        print(migrate_bs(md))
        bs_count += 1

    print(f'\nBronsamenvatting files processed: {bs_count}')


if __name__ == '__main__':
    main()
