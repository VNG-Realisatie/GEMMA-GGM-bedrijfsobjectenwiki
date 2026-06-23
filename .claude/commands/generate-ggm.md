Genereer Wiki/GGM vanuit GGM XMI-release: $ARGUMENTS

Volledige pipeline: XMI → parsed JSON → Wiki/GGM markdown-bestanden.
Bron van waarheid is het XMI-bestand in `Sources/GGM-repository/`.

## Wanneer draaien

- Bij een nieuwe GGM-release (nieuw XMI-bestand)
- Bij geconstateerde telfouten of structuurwijzigingen in Wiki/GGM
- Argument `--wiki-only` om alleen stap 2 te draaien (JSON → Wiki)

## Stappen

1. **Parse XMI → JSON** — `python3 tools/parse_ggm_xmi.py` (leest `Sources/GGM-repository/Gemeentelijk Gegevensmodel XMI2.1.xml`, schrijft `Sources/GGM-repository/ggm_parsed.json`)
2. **Genereer Wiki/GGM** — `python3 tools/generate_ggm_wiki.py` (leest JSON, schrijft alle markdown-bestanden)

Bij `--wiki-only`: sla stap 1 over, gebruik bestaande `ggm_parsed.json`.

## Uitvoering

1. Controleer dat het XMI-bestand bestaat in `Sources/GGM-repository/`.
2. Draai stap 1: `python3 tools/parse_ggm_xmi.py` — toon statistieken (entiteiten, relaties, packages).
3. Draai stap 2 eerst als dry run: `python3 tools/generate_ggm_wiki.py --dry-run` — toon resultaat.
4. Na akkoord gebruiker: `python3 tools/generate_ggm_wiki.py` (maakt backup `Wiki/GGM.bak-{datum}`).
5. Verificatie: controleer dat `aantal_entiteiten` alleen Objecttype telt, parent-bestanden kloppen, `structuur-ggm.md` is gegenereerd.
6. Opruimen: als alles klopt, verwijder backup.

## Telregel

`aantal_entiteiten` telt **alleen** entiteiten met `stereotype == 'Objecttype'`. Niet meegeteld: Enumeraties (waardelijsten) en Class zonder stereotype (EA-diagramcontainers).
