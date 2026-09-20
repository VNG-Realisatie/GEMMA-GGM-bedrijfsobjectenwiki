# Bronnen

Paden relatief aan `Bedrijfsarchitectuur/`.

## GGM-bronnen
- [SRC1] `Sources/GGM-repository/Gemeentelijk Gegevensmodel XMI2.1.xml` is de bron van waarheid voor het GGM. NOOIT direct lezen; ALLEEN via de parser.
- [SRC1a] ALS er een nieuwe GGM-release is → zet het XMI om in `Sources/GGM-repository/ggm_parsed.json` met `tools/parse_ggm_xmi.py` (via `/generate-ggm`). Beide bestanden staan in `Sources/GGM-repository/`.
- [SRC2] NOOIT CSV-bestanden (~/Downloads) of andere locaties als GGM-bron gebruiken (afgeleiden; verouderd of incompleet).
- [SRC3] Voor domeinbegrip (entiteiten, definities, relaties) ALTIJD `Wiki/GGM/{taakveld}/` lezen; bij ingest en `/assess-element` eerst deze bestanden lezen.
- [SRC4] `Sources/GGM-repository/ggm_parsed.json` ALLEEN gebruiken voor technische metadata: GUIDs, GEMMA-tags, diagram-IDs (frontmatter).

## Bestanden in Sources/
- [SRC5] NOOIT bestanden in `Sources/` vertalen of herschrijven, en NOOIT per ongeluk uitbreiden (immutabel referentiemateriaal).
- [SRC6] Nederlandse bronnen: originele Nederlandse tekst letterlijk bewaren. Ophalen: `/fetch` (curl, NOOIT WebFetch).
- [SRC7] ALLEEN selectief kopiëren toegestaan: neem de beschrijvingen over; laat ruis weg (navigatie, nieuwslijsten, agenda's, gerelateerde links).
- [SRC8] NOOIT `[[wiki-links]]` in `Sources/`. ALTIJD platte bestandsreferentie: GGM-bronbestand → `bestandsnaam.md`; wiki-pagina → volledig pad, bv. `Wiki/Analyses/bestandsnaam.md`.

## Notes
- Regels voor bronselectie staan in `/ingest`, voor PDF-conversie in `/convert_pdf` en `/fetch`, voor utrecht.bestuurlijkeinformatie.nl in `/fetch`.
