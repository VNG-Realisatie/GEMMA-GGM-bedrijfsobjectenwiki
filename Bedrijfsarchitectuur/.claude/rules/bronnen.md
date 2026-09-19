# Bronnen

## ggm-bron-xmi

Gebruik altijd het XMI-bestand `Sources/Gemeentelijk Gegevensmodel XMI2.1.xml` als bron voor GGM-gegevens. CSV-bestanden in ~/Downloads zijn geen bron.

**Why:** De CSV-exports zijn afgeleiden en kunnen verouderd of incompleet zijn. Het XMI-bestand is de bron van waarheid voor het GGM.

**How to apply:** Bij het opzoeken van GGM-entiteiten, attributen of relaties altijd het XMI-bestand in de Sources-directory raadplegen, nooit bestanden in ~/Downloads of andere locaties.

## ggm-wiki-niet-json

Raadpleeg Wiki/GGM/{taakveld}/ voor domeinbegrip (entiteiten, definities, relaties), niet ggm_parsed.json.

**Why:** De Wiki/GGM bestanden zijn de leesbare representatie die daarvoor is gemaakt. De JSON is alleen voor technische metadata (GUIDs, GEMMA-tags, diagram-IDs). Staat ook al in CLAUDE.md § "GGM-data gebruiken".

**How to apply:** Bij ingest/assess-bo: lees eerst Wiki/GGM/{taakveld}/ voor relevante entiteiten. Gebruik ggm_parsed.json alleen als je GUIDs of GEMMA-tags nodig hebt voor frontmatter.

## sources-niet-vertalen

Brondocumenten (Sources/) zijn de basis voor begrippen en mogen NOOIT vertaald of herschreven worden.
**Why:** Bronnen zijn immutabel referentiemateriaal. Vertaling verandert de betekenis en maakt het onbruikbaar als basis voor begripsextractie.
**How to apply:** Bij het ophalen van VNG-pagina's of andere Nederlandse bronnen: bewaar de originele Nederlandse tekst letterlijk. Wat wel mag: selectief kopiëren — neem alleen de beschrijvingen over en laat ruis (navigatie, nieuwslijsten, agenda's, gerelateerde links) weg. Gebruik WebFetch met expliciete instructie om Nederlands te behouden en niet te vertalen. Zie ook geen-wikilinks-in-sources.

## geen-wikilinks-in-sources

Gebruik nooit `[[wiki-links]]` in bestanden onder Sources/. Gebruik in plaats daarvan platte bestandsreferenties (bijv. `structuur-ggm.md`, `Wiki/Analyses/ggm-hiaten-belastingendomein.md`).

**Why:** Wiki-links in Sources/ worden door de IDE geresolveerd relatief aan het huidige bestand. Klikken op `[[ggm-hiaten-belastingendomein]]` in Sources/GGM/ maakt dan een leeg bestand aan in Sources/GGM/ in plaats van te navigeren naar Wiki/Analyses/. Zie ook ggm-bron-xmi — Sources zijn immutabel en mogen niet per ongeluk worden uitgebreid.

**How to apply:** Bij het schrijven van GGM-bronbestanden in Sources/GGM/: verwijs naar andere GGM-bestanden als `bestandsnaam.md` en naar wiki-pagina's met het volledige pad `Wiki/Analyses/bestandsnaam.md`.

## multi-gemeente-bronnen

Bronnen uit andere gemeenten dan Utrecht NIET afwijzen vanwege herkomst. Meerdere gemeenten als bron is juist goed: het leidt tot bedrijfsobjecten die bruikbaar zijn voor alle gemeenten.

**Why:** De wiki bouwt aan GEMMA-standaard bedrijfsobjecten, die voor álle Nederlandse gemeenten gelden. Bronnen uit één gemeente geven een te smal perspectief.

**How to apply:** Bij bronbeoordeling nooit "andere gemeente" als reden voor niet-relevant gebruiken. Beoordeel alleen op inhoudelijke relevantie voor BO-kandidaten. Zie ook gemeentelijk-perspectief.

## pdf-conversie

Converteer PDF's altijd met `python tools/convert_pdf.py {bestand.pdf}`, nooit door de PDF visueel te lezen en handmatig over te typen.

**Why:** Visueel overtypen is extreem traag (minuten per document), foutgevoelig, en kost enorm veel output-tokens. Het script doet het in seconden met betere kwaliteit.

**How to apply:** Bij elke PDF-conversie direct het script gebruiken. De `/convert_pdf` skill wraps dit script al. Ook bij `/fetch` met gelinkte PDF's: download → script → frontmatter toevoegen.

## utrecht-bestuurlijke-informatie-pdf

PDF-documenten op utrecht.bestuurlijkeinformatie.nl zijn niet direct downloadbaar via de pagina-URL. Er zijn twee URL-types met elk een eigen downloadpatroon:

## Patroon 1: Agenda-documenten (`/Agenda/Document/...`)

Pagina-URL bevat `/Agenda/Document/{id}?documentId={docId}&agendaItemId={itemId}`.

1. De download-URL is **`/Document/LoadAgendaItemDocument/{documentId}?agendaItemId={agendaItemId}`**
2. Volledige URL: `https://utrecht.bestuurlijkeinformatie.nl/Document/LoadAgendaItemDocument/{documentId}?agendaItemId={agendaItemId}`

**Let op:** De URL-prefix `/Agenda/Document/LoadAgendaItemDocument/` (zoals in de HTML) werkt NIET — gebruik `/Document/LoadAgendaItemDocument/` (zonder `/Agenda/`).

## Patroon 2: Reports-documenten (`/Reports/Document/...`)

Pagina-URL bevat `/Reports/Document/{id}?documentId={docId}`.

1. Fetch de HTML-pagina met curl
2. Zoek de JavaScript-loader: `grep -oE '"/Script/LoadDocument/[^"]*"'`
3. Fetch die Script-URL — het antwoord bevat een `Document/View/{documentId}` pad
4. De download-URL is **`/Document/View/{documentId}`**
5. Volledige URL: `https://utrecht.bestuurlijkeinformatie.nl/Document/View/{documentId}`

Of sneller: gebruik direct de `documentId` uit de query parameter van de pagina-URL in `/Document/View/{documentId}`.
