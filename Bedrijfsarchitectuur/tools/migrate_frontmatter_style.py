#!/usr/bin/env python3
"""Normalize frontmatter style across all element pages (Wiki/Bedrijfsobjecten,
Wiki/Actoren, Wiki/Rollen).

Fixes found during a wiki-wide frontmatter audit (zie Wiki/log.md):

1. Field rename: `domein:` -> `onderwerp:` (template canoniek veld).
2. Empty scalar values -> blank (niets na de colon), i.p.v. "", '', ~, '~', "~".
   Van toepassing op alle ggm_*/ggm_gemma_*/bo_toelichting-velden.
3. Empty list values (bedrijfsprocessen/bedrijfsfuncties) -> [] i.p.v. ""/''.
4. Quote-stijl unificeren naar dubbele quotes voor niet-lege GGM-tekstvelden,
   bo_toelichting, bo_definitie en bo_relaties.bedrijfsobject/kardinaliteit.
5. Bugfix: unquoted `bedrijfsobject: [[...]]` in bo_relaties parseert als
   geneste YAML-lijst i.p.v. string — altijd quoten.
6. Literal `null` in kardinaliteit -> blank.

Safety: a handful of fields (ggm_definitie e.a.) contain multi-line values —
either an unterminated quote that closes on a later line, or a bare/plain
scalar that folds onto an indented continuation line. Rewriting those with
per-line regex corrupts the YAML (double-quoting an already-open quote,
orphaning a continuation line). Any field whose value doesn't cleanly
terminate on its own line is left completely untouched.

After writing, every file is re-parsed with yaml.safe_load and checked against
the pre-migration parse (same fields, same values modulo the touched ones) —
a file that fails this check is reverted to its original content and reported.

Safe to run multiple times (idempotent). Only touches frontmatter (between the
--- markers); body content is untouched.

Usage:
  python3 tools/migrate_frontmatter_style.py --dry-run   # preview
  python3 tools/migrate_frontmatter_style.py              # apply
"""

import re
import sys
import yaml
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DIRS = [BASE / 'Wiki' / 'Bedrijfsobjecten', BASE / 'Wiki' / 'Actoren', BASE / 'Wiki' / 'Rollen']

EMPTY_SCALAR_FIELDS = {
    'ggm_entiteit', 'ggm_guid', 'ggm_uml_type', 'ggm_beleidsdomein', 'ggm_taakveld',
    'ggm_definitie', 'ggm_toelichting', 'ggm_synoniemen', 'ggm_herkomst',
    'ggm_gemma_naam', 'ggm_gemma_guid', 'ggm_gemma_definitie', 'ggm_gemma_toelichting',
    'ggm_gemma_synoniemen', 'ggm_gemma_type', 'ggm_gemma_url', 'ggm_gemma_bron',
    'ggm_gemma_alternate_name', 'bo_toelichting',
}
QUOTE_UNIFY_FIELDS = EMPTY_SCALAR_FIELDS | {'bo_definitie'}
ALWAYS_QUOTE_FIELDS = {'bo_definitie'}
EMPTY_LIST_FIELDS = {'bedrijfsprocessen', 'bedrijfsfuncties'}

EMPTY_VALUE_RE = re.compile(r'^(?:""|\'\'|~|\'~\'|"~"|)$')
TOP_LEVEL_KEY_RE = re.compile(r'^[a-zA-Z_][\w]*:')


def unify_quotes(value: str, force: bool = False) -> str:
    """Return value re-quoted with double quotes, preserving content."""
    if value.startswith('"') and value.endswith('"'):
        return value
    if value.startswith("'") and value.endswith("'"):
        inner = value[1:-1].replace("''", "'")
        if '"' not in inner:
            return f'"{inner}"'
        return value
    needs_quote = force or any(c in value for c in ':{}[]&*?|->!%@`#,') or value[:1] in '"\'[{'
    if needs_quote:
        return f'"{value}"'
    return value


def value_closes_on_line(value: str) -> bool:
    """True if a quoted value's opening quote also closes within this line."""
    if value.startswith('"'):
        return len(value) >= 2 and value.endswith('"') and value.count('"') >= 2 and value.count('"') % 2 == 0
    if value.startswith("'"):
        return len(value) >= 2 and value.endswith("'") and value.count("'") >= 2
    return True  # not quoted — caller checks plain-scalar continuation separately


def is_safe_single_line(value: str, next_line: str | None) -> bool:
    """True if `value` is fully self-contained on its own physical line.

    Guards against two multi-line shapes found in the wiki: an opening quote
    that only closes on a later line, and a bare/plain scalar that folds onto
    an indented (or otherwise non-key) continuation line.
    """
    if value == '':
        return True
    if value.startswith('"') or value.startswith("'"):
        return value_closes_on_line(value)
    # Bare/plain scalar: safe only if nothing follows, or the next line
    # clearly starts a new top-level field (or is a blank separator).
    if next_line is None:
        return True
    if next_line.strip() == '':
        return True
    return bool(TOP_LEVEL_KEY_RE.match(next_line))


def process_top_level_line(line: str, next_line: str | None) -> str:
    m = re.match(r'^([a-zA-Z_][\w]*):\s*(.*)$', line)
    if not m:
        return line
    orig_field, value = m.group(1), m.group(2)
    field = 'onderwerp' if orig_field == 'domein' else orig_field

    if field in (EMPTY_SCALAR_FIELDS | QUOTE_UNIFY_FIELDS | EMPTY_LIST_FIELDS):
        if not is_safe_single_line(value, next_line):
            # Multi-line value — leave completely untouched (only apply the
            # domein->onderwerp rename, which never affects the value itself).
            return f'{field}: {value}' if field != orig_field else line

    if field in EMPTY_SCALAR_FIELDS and EMPTY_VALUE_RE.match(value):
        return f'{field}:'

    if field in EMPTY_LIST_FIELDS and value in ('""', "''"):
        return f'{field}: []'

    if field in QUOTE_UNIFY_FIELDS and value and not EMPTY_VALUE_RE.match(value):
        value = unify_quotes(value, force=field in ALWAYS_QUOTE_FIELDS)
        return f'{field}: {value}'

    if field != orig_field:
        return f'{field}: {value}' if value else f'{field}:'

    return line


FORCE_QUOTE_NESTED_FIELDS = {'bedrijfsobject', 'kardinaliteit'}
NESTED_EMPTY_FIELDS = FORCE_QUOTE_NESTED_FIELDS | {
    'ggm_entiteit', 'ggm_guid', 'ggm_attribuut', 'afwijkende_attributen',
}
NESTED_FIELD_RE = re.compile(
    r'^(\s+)(' + '|'.join(sorted(NESTED_EMPTY_FIELDS)) + r'):\s*(.*)$'
)


def process_relatie_line(line: str) -> str:
    m = NESTED_FIELD_RE.match(line)
    if not m:
        return line
    indent, field, value = m.group(1), m.group(2), m.group(3)

    if not is_safe_single_line(value, None) and value != 'null':
        return line

    if value == 'null' or EMPTY_VALUE_RE.match(value):
        return f'{indent}{field}:'

    if field in FORCE_QUOTE_NESTED_FIELDS:
        value = unify_quotes(value, force=True)
        return f'{indent}{field}: {value}'

    return line


def migrate_frontmatter(fm: str) -> str:
    lines = fm.split('\n')
    out_lines = []
    for i, line in enumerate(lines):
        next_line = lines[i + 1] if i + 1 < len(lines) else None
        if re.match(r'^\s+(?:' + '|'.join(sorted(NESTED_EMPTY_FIELDS)) + r'):', line):
            out_lines.append(process_relatie_line(line))
        elif TOP_LEVEL_KEY_RE.match(line):
            out_lines.append(process_top_level_line(line, next_line))
        else:
            out_lines.append(line)
    return '\n'.join(out_lines)


def norm_val(v):
    """Recursively normalize a value for equivalence comparison: empty-ish
    scalars collapse to None, everything else is stringified so intentional
    type changes (bare 1 -> quoted "1") don't register as a mismatch.
    """
    if v in (None, '', '~', []):
        return None
    if isinstance(v, dict):
        d = dict(v)
        bo = d.get('bedrijfsobject')
        # Known bug: unquoted `[[naam]]` parses as [['naam']] instead of the
        # string "[[naam]]" — recognize and reconstruct for comparison, since
        # fixing this is an intentional part of the migration.
        if isinstance(bo, list) and len(bo) == 1 and isinstance(bo[0], list) \
                and len(bo[0]) == 1 and isinstance(bo[0][0], str):
            d['bedrijfsobject'] = f'[[{bo[0][0]}]]'
        return {k: norm_val(val) for k, val in d.items()}
    if isinstance(v, list):
        return [norm_val(x) for x in v]
    return str(v)


def semantically_equivalent(old_fields: dict, new_fields: dict) -> bool:
    """True if every key/value in old_fields survives in new_fields, allowing
    for the domein->onderwerp rename, empty-value normalization, and
    intentional scalar-type changes (str() equal counts as equal).
    """
    def norm_key(k):
        return 'onderwerp' if k == 'domein' else k

    old_norm = {norm_key(k): norm_val(v) for k, v in old_fields.items()}
    new_norm = {norm_key(k): norm_val(v) for k, v in new_fields.items()}
    return old_norm == new_norm


def migrate_file(path: Path, dry_run: bool) -> str:
    content = path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return 'skip:no-frontmatter'

    parts = content.split('---', 2)
    if len(parts) < 3:
        return 'skip:malformed'

    fm = parts[1]
    try:
        old_fields = yaml.safe_load(fm) or {}
    except yaml.YAMLError as e:
        return f'skip:unparseable-original:{e}'

    new_fm = migrate_frontmatter(fm)
    if new_fm == fm:
        return 'unchanged'

    try:
        new_fields = yaml.safe_load(new_fm) or {}
    except yaml.YAMLError as e:
        return f'ABORT:new-yaml-invalid:{e}'

    if not semantically_equivalent(old_fields, new_fields):
        return 'ABORT:semantic-mismatch'

    new_content = f'---{new_fm}---{parts[2]}'
    if not dry_run:
        path.write_text(new_content, encoding='utf-8')
    return 'migrated'


def main():
    dry_run = '--dry-run' in sys.argv
    results = {'migrated': 0, 'unchanged': 0, 'skipped': 0, 'aborted': 0}

    files = sorted(f for d in DIRS if d.exists() for f in d.rglob('*.md'))
    for md in files:
        result = migrate_file(md, dry_run)
        rel = md.relative_to(BASE)
        if result == 'migrated':
            results['migrated'] += 1
            print(f'  ✅ {rel}')
        elif result == 'unchanged':
            results['unchanged'] += 1
        elif result.startswith('ABORT'):
            results['aborted'] += 1
            print(f'  ❌ {rel} — {result}')
        else:
            results['skipped'] += 1
            print(f'  ⏭  {rel} ({result})')

    mode = 'DRY RUN' if dry_run else 'DONE'
    print(f'\n{mode}: {results["migrated"]} migrated, {results["unchanged"]} unchanged, '
          f'{results["skipped"]} skipped, {results["aborted"]} ABORTED (unsafe, left untouched)')


if __name__ == '__main__':
    main()
