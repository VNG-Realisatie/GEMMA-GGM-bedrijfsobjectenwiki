# generate-ggm

**Doel:** de volledige GGM-pipeline draaien: XMI → geparsede JSON → `Wiki/GGM/`-markdown → verversen van BO-frontmatter. Bron van waarheid is het XMI-bestand.
**Aanbevolen model:** standaard
**Parameters:** {{modus}} — optioneel: `--wiki-only` (sla het parsen over, gebruik bestaande JSON) of `--dry-run` (alleen preview).
**Benodigde context:** [../tools/README.md](../tools/README.md), `Sources/GGM-repository/`.
**Verwachte uitvoer:** verse `ggm_parsed.json`, geregenereerde `Wiki/GGM/`, gesynchroniseerde `ggm_*`/`ggm_gemma_*`-frontmatter op BO-pagina's.

## Prompt

Genereer `Wiki/GGM/` vanuit de GGM XMI-release. Modus: {{modus}}

**Wanneer draaien:** bij een nieuwe GGM-release (nieuw XMI-bestand), of bij telfouten/structuurwijzigingen in `Wiki/GGM/` (dan `--wiki-only`).

1. Controleer dat het XMI-bestand bestaat in `Sources/GGM-repository/`.
2. **Parse XMI → JSON:** `python3 tools/parse_ggm_xmi.py` — toon de statistieken (entiteiten, relaties, packages).
3. **Genereer Wiki/GGM**, eerst als preview: `python3 tools/generate_ggm_wiki.py --dry-run`. Na akkoord van de gebruiker: zonder `--dry-run` (maakt automatisch een backup `Wiki/GGM.bak-{datum}`).
4. **Verifieer:** `aantal_entiteiten` telt alleen stereotype Objecttype (geen Enumeraties, geen Class zonder stereotype — dat zijn diagramcontainers); parent-bestanden kloppen; `structuur-ggm.md` is gegenereerd. Klopt alles, verwijder de backup.
5. **Ververs BO-frontmatter**, eerst als preview: `python3 tools/generate_ggm_enrich_bo.py --dry-run`. Controleer welke BO's een gewijzigde `ggm_guid` of definitie krijgen — dat kan wijzen op een homoniem of verplaatste entiteit; **nooit blind toepassen bij onverwachte GUID-wijzigingen**. Na akkoord: zonder `--dry-run`. Dit herschrijft alleen de `ggm_*`/`ggm_gemma_*`-velden; `bo_*`, `ggm_duplicaat_entiteiten` en `analyse_ggm_dekking` blijven ongemoeid.
6. Werk `Wiki/log.md` bij en stel voor de dekkingsanalyse te verversen (prompt `entiteitendekking`).

## Voorbeeld

> Genereer Wiki/GGM vanuit de GGM XMI-release. Modus: --wiki-only
