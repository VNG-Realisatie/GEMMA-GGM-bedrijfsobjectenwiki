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
- [SRC6] Nederlandse bronnen: originele Nederlandse tekst letterlijk bewaren. Bij WebFetch expliciet instrueren: Nederlands behouden, niet vertalen.
- [SRC7] ALLEEN selectief kopiëren toegestaan: neem de beschrijvingen over; laat ruis weg (navigatie, nieuwslijsten, agenda's, gerelateerde links).
- [SRC8] NOOIT `[[wiki-links]]` in `Sources/`. ALTIJD platte bestandsreferentie: GGM-bronbestand → `bestandsnaam.md`; wiki-pagina → volledig pad, bv. `Wiki/Analyses/bestandsnaam.md`.

## Bronbeoordeling
- [SRC9] NOOIT "andere gemeente dan Utrecht" als reden gebruiken om een bron af te wijzen of niet-relevant te noemen.
- [SRC10] Bronnen uit meerdere gemeenten zijn gewenst (leiden tot BO's bruikbaar voor alle gemeenten).
- [SRC11] Beoordeel een bron ALLEEN op inhoudelijke relevantie voor BO-kandidaten. Verdere bronbeoordeling: [BO7]; scope: [WC4].

## PDF-conversie
- [SRC12] ALTIJD PDF's converteren met `python tools/convert_pdf.py {bestand.pdf}`. NOOIT de PDF visueel lezen en overtypen.
- [SRC13] De skill `/convert_pdf` gebruikt dit script al.
- [SRC14] Bij `/fetch` met gelinkte PDF: download → script → frontmatter toevoegen.

## utrecht.bestuurlijkeinformatie.nl (iBabs)
- [SRC15] Pagina-URL's zijn NIET direct downloadbaar. Bepaal het URL-type en gebruik het bijbehorende patroon.
- [SRC16] Agenda-document — pagina-URL: `/Agenda/Document/{id}?documentId={docId}&agendaItemId={itemId}` → download: `https://utrecht.bestuurlijkeinformatie.nl/Document/LoadAgendaItemDocument/{documentId}?agendaItemId={agendaItemId}`. NOOIT prefix `/Agenda/Document/LoadAgendaItemDocument/` gebruiken (werkt niet).
- [SRC17] Reports-document — pagina-URL: `/Reports/Document/{id}?documentId={docId}` → download: `https://utrecht.bestuurlijkeinformatie.nl/Document/View/{documentId}`, met `documentId` uit de query-parameter van de pagina-URL.
- [SRC18] ALS [SRC17] geen resultaat geeft: pagina met curl ophalen → `grep -oE '"/Script/LoadDocument/[^"]*"'` → die Script-URL ophalen → antwoord bevat pad `Document/View/{documentId}`.
