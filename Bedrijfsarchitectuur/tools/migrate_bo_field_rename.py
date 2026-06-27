#!/usr/bin/env python3
"""Migrate BO frontmatter field names from gemma_/relaties to bo_ prefix.

Renames:
  gemma_definitie  -> bo_definitie
  gemma_subtypes   -> bo_subtypes
  relaties:        -> bo_relaties:

Preserves all content and formatting. Safe to run multiple times (idempotent).

Usage:
  python3 tools/migrate_bo_field_rename.py --dry-run   # preview changes
  python3 tools/migrate_bo_field_rename.py              # apply changes
"""

import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
WIKI_BO = BASE / 'Wiki' / 'Bedrijfsobjecten'

RENAMES = [
    # Use regex patterns to avoid matching ggm_gemma_definitie
    (re.compile(r'^gemma_definitie:', re.MULTILINE), 'bo_definitie:'),
    (re.compile(r'^gemma_subtypes:', re.MULTILINE), 'bo_subtypes:'),
]

RELATIES_OLD = re.compile(r'^relaties:\s*$', re.MULTILINE)
RELATIES_ITEM = re.compile(r"^(  - type:.*)", re.MULTILINE)


def migrate_file(path: Path, dry_run: bool) -> dict:
    content = path.read_text(encoding='utf-8')

    if not content.startswith('---'):
        return {'status': 'skip', 'reason': 'no frontmatter'}

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {'status': 'skip', 'reason': 'malformed frontmatter'}

    fm = parts[1]
    body = parts[2]
    changes = []

    for pattern, new in RENAMES:
        if pattern.search(fm) and new not in fm:
            fm = pattern.sub(new, fm)
            old_name = new.replace('bo_', 'gemma_').rstrip(':')
            new_name = new.rstrip(':')
            changes.append(f'{old_name} -> {new_name}')

    if re.search(r'^relaties:', fm, re.MULTILINE) and not re.search(r'^bo_relaties:', fm, re.MULTILINE):
        fm = re.sub(r'^relaties:', 'bo_relaties:', fm, flags=re.MULTILINE)
        changes.append('relaties -> bo_relaties')

    if not changes:
        return {'status': 'unchanged'}

    new_content = f'---{fm}---{body}'

    if not dry_run:
        path.write_text(new_content, encoding='utf-8')

    return {'status': 'migrated', 'changes': changes}


def main():
    dry_run = '--dry-run' in sys.argv

    results = {'migrated': 0, 'unchanged': 0, 'skipped': 0}

    for md in sorted(WIKI_BO.rglob('*.md')):
        result = migrate_file(md, dry_run)
        rel = md.relative_to(WIKI_BO)

        if result['status'] == 'migrated':
            results['migrated'] += 1
            changes_str = ', '.join(result['changes'])
            tag = '(dry-run)' if dry_run else ''
            print(f'  ✅ {rel} — {changes_str} {tag}')
        elif result['status'] == 'unchanged':
            results['unchanged'] += 1
        else:
            results['skipped'] += 1
            print(f'  ⏭  {rel} — {result["reason"]}')

    mode = 'DRY RUN' if dry_run else 'DONE'
    print(f'\n{mode}: {results["migrated"]} migrated, '
          f'{results["unchanged"]} unchanged, {results["skipped"]} skipped')


if __name__ == '__main__':
    main()
