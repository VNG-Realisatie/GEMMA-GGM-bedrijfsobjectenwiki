# Bronnen

Paden relatief aan `Bedrijfsarchitectuur/`.

## GGM-bronnen
- [SRC1] `Sources/GGM-repository/Gemeentelijk Gegevensmodel XMI2.1.xml` is de bron van waarheid voor het GGM. NOOIT direct lezen; ALLEEN via de parser.
- [SRC2] ALS er een nieuwe GGM-release is → zet het XMI om in `Sources/GGM-repository/ggm_parsed.json` met `tools/parse_ggm_xmi.py` (via `/generate-ggm`). Beide bestanden staan in `Sources/GGM-repository/`.
- [SRC3] NOOIT CSV-bestanden (~/Downloads) of andere locaties als GGM-bron gebruiken (afgeleiden; verouderd of incompleet).
- [SRC4] ALTIJD zoeken en matchen in `Sources/GGM-repository/ggm_parsed.json` (structurele query, bv. Python/jq): entiteiten (incl. enumeraties) over alle beleidsdomeinen, namen en synoniemen, relaties, generalisaties (`uml_type: Generalization`), attributen, GUIDs, GEMMA-tags, diagram-IDs.
- [SRC5] `Wiki/GGM/{taakveld}/` ALLEEN gebruiken om een beleidsdomein leesbaar door te lopen (definities, attributen). Het bevat alleen Objecttypen en geen relaties, generalisaties, enumeraties, GUIDs of tags.

## Bestanden in Sources/
- [SRC6] NOOIT bestanden in `Sources/` vertalen of herschrijven, en NOOIT per ongeluk uitbreiden (immutabel referentiemateriaal).
- [SRC7] Nederlandse bronnen: originele Nederlandse tekst letterlijk bewaren. Ophalen: `/fetch` (curl, NOOIT WebFetch).
- [SRC8] ALLEEN selectief kopiëren toegestaan: neem de beschrijvingen over; laat ruis weg (navigatie, nieuwslijsten, agenda's, gerelateerde links).
- [SRC9] NOOIT `[[wiki-links]]` in `Sources/`. ALTIJD platte bestandsreferentie: GGM-bronbestand → `bestandsnaam.md`; wiki-pagina → volledig pad, bv. `Wiki/Analyses/bestandsnaam.md`.

## Notes
- Regels voor bronselectie staan in `/ingest`, voor PDF-conversie in `/convert_pdf` en `/fetch`, voor utrecht.bestuurlijkeinformatie.nl in `/fetch`.
