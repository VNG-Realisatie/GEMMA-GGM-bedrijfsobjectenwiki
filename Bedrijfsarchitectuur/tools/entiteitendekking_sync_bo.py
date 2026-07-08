#!/usr/bin/env python3
"""Synchroniseer analyse_ggm_dekking op BO-pagina's vanuit de entiteitendekking-analyse.

Beantwoordt, per BO-pagina, de vraag "welke GGM-entiteiten worden door dit BO
gedekt?" — het omgekeerde van wat de per-taakveld rapporten tonen (die gaan per
GGM-entiteit uit en wijzen naar één BO). Herbruikt entiteitendekking.py's
matching/classificatie-logica via run_full_analysis() (geen dubbele logica),
keert het resultaat om naar "per-BO → welke entiteiten", en schrijft alleen het
analyse_ggm_dekking-veld — alle overige frontmatter blijft ongewijzigd
(chirurgische patch, geen full rebuild).

Stap 5 van de /entiteitendekking skill — losse aanroep, niet gebundeld in
entiteitendekking.py --all, zodat git diff altijd laat zien of een run alleen
Wiki/Analyses/ raakte of ook BO-pagina's.

Usage:
    python3 tools/entiteitendekking_sync_bo.py --dry-run
    python3 tools/entiteitendekking_sync_bo.py
"""
import argparse
import re
from collections import defaultdict
from pathlib import Path

from entiteitendekking import run_full_analysis, load_ggm, BASE_PATH

FIELD_NAME = 'analyse_ggm_dekking'

_WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')


def _strip_wikilinks(text):
    """Frontmatter wordt buiten de wiki gebruikt (csv_export) — wiki-links
    ([[pad\\|Weergavenaam]], bijv. overgenomen uit een onderwerpoverzicht-
    begrippentabel) mogen daar niet in staan. Vervang door de weergavetekst."""
    def repl(m):
        inner = m.group(1).replace('\\|', '|')
        if '|' in inner:
            return inner.split('|', 1)[1]
        return inner.rsplit('/', 1)[-1]
    return _WIKILINK_RE.sub(repl, text)


def build_bo_dekking_index(all_tv_results, bo_by_path):
    """Groepeer het dekkingsresultaat per BO-pad: eigen exacte match (primary)
    + lijst van via-via gedekte entiteiten (via).

    Een BO met ggm_duplicaat_entiteiten (bijv. Sportpark, dat ook matcht op de
    GGM-entiteit Sportterrein) levert twee bo_matches-rijen voor hetzelfde pad
    op — één voor de eigen ggm_guid, één voor elke duplicaat-GUID. Alleen de
    rij die daadwerkelijk overeenkomt met het BO's eigen ggm_guid wordt de
    primary; de rest wordt als 'duplicaat' via-via-entiteit behandeld, in
    plaats van de echte primary stil te overschrijven.
    """
    by_bo = defaultdict(lambda: {'primary': None, 'via': []})
    for tv_r in all_tv_results.values():
        for bd_r in tv_r['beleidsdomeinen'].values():
            for m in bd_r['bo_matches']:
                bo_path = m['bo_path']
                own_guid = bo_by_path.get(bo_path, {}).get('ggm_guid')
                if not own_guid or m['eid'] == own_guid:
                    by_bo[bo_path]['primary'] = m
                else:
                    by_bo[bo_path]['via'].append({
                        'ggm_name': m['ggm_name'], 'eid': m['eid'],
                        'entiteitstype': m['entiteitstype'],
                        'match_kind': 'duplicaat',
                        'beoordeling': m['beoordeling'],
                    })
            for g in bd_r['geen_match']:
                bo_path = g.get('dekking_bo_path')
                if bo_path:
                    by_bo[bo_path]['via'].append(g)
    return dict(by_bo)


def render_field_text(entry, bo, objecttypes):
    """Render de intro+bullets-tekst voor één BO. `bo` is de BO-info uit
    all_bos (fallback als er geen primary-match uit de analyse kwam, bijv.
    omdat de eigen GGM-entiteit is uitgesloten van verwerking)."""
    primary = entry.get('primary')
    via = entry.get('via') or []

    duplicates = sorted((g for g in via if g.get('match_kind') == 'duplicaat'),
                        key=lambda x: x['ggm_name'])
    others = sorted((g for g in via if g.get('match_kind') != 'duplicaat'),
                    key=lambda x: x['ggm_name'])

    is_synoniem = bool(primary) and primary['entiteitstype'] == 'hernoemd'
    primary_name = primary['ggm_name'] if primary else bo.get('ggm_entiteit', '')

    sentences = []
    if primary_name:
        if is_synoniem:
            sentences.append(f"Dit BO is de hernoeming van GGM-entiteit **{primary_name}**.")
        else:
            sentences.append(f"Dit BO heeft de GGM-entiteit **{primary_name}** als directe tegenhanger.")

    for d in duplicates:
        bd = objecttypes.get(d['eid'], {}).get('beleidsdomein', '')
        bd_note = f" (beleidsdomein {bd})" if bd else ""
        sentences.append(f"Daarnaast is **{d['ggm_name']}**{bd_note} als vermoedelijk duplicaat "
                         f"gekoppeld — zie ggm_duplicaat_entiteiten.")

    if others:
        sentences.append("Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:")

    lines = [' '.join(sentences)] if sentences else []
    for g in others:
        beoordeling = _strip_wikilinks(g['beoordeling'])
        lines.append(f"- **{g['ggm_name']}** ({g['entiteitstype']}) — {beoordeling}")
    return '\n'.join(lines)


def render_field_lines(text):
    if not text:
        return [f'{FIELD_NAME}: ""']
    lines = [f'{FIELD_NAME}: |']
    for line in text.split('\n'):
        lines.append(f'  {line}' if line else '')
    return lines


_FIELD_BLOCK_RE = re.compile(rf'(?m)^{FIELD_NAME}:.*\n(?:[ \t]+\S.*\n?|\n)*')
_ANCHOR_RE = re.compile(r'(?m)^ggm_duplicaat_entiteiten:.*\n(?:[ \t]+\S.*\n?|\n)*')
_FALLBACK_RE = re.compile(r'(?m)^bo_definitie:')


def patch_frontmatter(fm_raw, new_lines):
    """Vervang of voeg het analyse_ggm_dekking-blok chirurgisch toe — alle
    overige frontmatter blijft byte-voor-byte ongewijzigd."""
    new_block = '\n'.join(new_lines) + '\n'
    if _FIELD_BLOCK_RE.search(fm_raw):
        return _FIELD_BLOCK_RE.sub(lambda _: new_block, fm_raw, count=1)
    m = _ANCHOR_RE.search(fm_raw)
    if m:
        return fm_raw[:m.end()] + new_block + fm_raw[m.end():]
    m2 = _FALLBACK_RE.search(fm_raw)
    if m2:
        return fm_raw[:m2.start()] + new_block + fm_raw[m2.start():]
    return fm_raw.rstrip('\n') + '\n' + new_block


def sync_bo_page(path: Path, entry, bo, objecttypes, dry_run=False):
    if not path.exists():
        return 'skip:not-found', ''
    full = path.read_text(encoding='utf-8')
    if not full.startswith('---'):
        return 'skip:no-frontmatter', ''
    parts = full.split('---', 2)
    if len(parts) < 3:
        return 'skip:malformed', ''
    fm_raw, body = parts[1], parts[2]

    text = render_field_text(entry, bo, objecttypes)
    new_fm_raw = patch_frontmatter(fm_raw, render_field_lines(text))
    if new_fm_raw == fm_raw:
        return 'unchanged', text
    if not dry_run:
        path.write_text(f'---{new_fm_raw}---{body}', encoding='utf-8')
    return 'updated', text


def main():
    parser = argparse.ArgumentParser(
        description='Synchroniseer analyse_ggm_dekking op BO-pagina\'s')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    all_tv_results, _, _, bo_by_guid, bo_by_name, all_bos = run_full_analysis(verbose=True)
    _, objecttypes = load_ggm()
    bo_by_path = {bo['path']: bo for bo in all_bos}
    by_bo = build_bo_dekking_index(all_tv_results, bo_by_path)

    targets = {bo['path'] for bo in all_bos if bo['ggm_guid']} | set(by_bo.keys())

    counts = defaultdict(int)
    print()
    for bo_path in sorted(targets):
        bo = bo_by_path.get(bo_path, {})
        entry = by_bo.get(bo_path, {'primary': None, 'via': []})
        result, text = sync_bo_page(
            BASE_PATH / f"{bo_path}.md", entry, bo, objecttypes, dry_run=args.dry_run)
        counts[result] += 1
        if result == 'updated':
            marker = '~' if args.dry_run else '✅'
            print(f"  {marker} {bo_path}")
            if args.dry_run:
                for line in text.split('\n'):
                    print(f"       {line}")

    mode = 'DRY RUN' if args.dry_run else 'DONE'
    print(f"\n{mode}: {dict(counts)}")


if __name__ == '__main__':
    main()
