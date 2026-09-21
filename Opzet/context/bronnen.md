# Bronnen (Sources)

## Wat een bron is

Gemeentelijke beleidsdocumenten, VNG-publicaties, proposities, toelichtingen, verordeningen en wetten — plus het GGM zelf. Bronnen uit verschillende gemeenten zijn welkom: juist meerdere gemeenten samen leiden tot generiek bruikbare bedrijfsobjecten.

## Immutabiliteit

- De **inhoud** van een bronbestand wordt nooit gewijzigd, vertaald, samengevat of herschreven — een bron is een exacte kopie van de originele tekst (alleen opmaakruis zoals navigatie en footers wordt bij intake verwijderd).
- **Ordenen mag wel**: verplaatsen of hernoemen binnen `Sources/` en frontmatter aanvullen bij intake zijn toegestaan.

## Waar bronnen staan

- Gemeentelijke onderwerpen: altijd `Sources/Onderwerpen/{onderwerp}/`.
- Vaste uitzonderingen direct onder `Sources/`: `GGM/`, `GGM-repository/`, `GEMMA/`, `Standaarden/`, `informatiebeheer/`, `informatiesystemen/`.
- Controleer bestaande onderwerpmappen voordat je een nieuwe aanmaakt; een nieuwe map alleen voor een echt nieuw onderwerp.

## Bronnen toevoegen

Twee routes, beide eindigend als bestand in `Sources/Onderwerpen/{onderwerp}/`:

1. **Via URL** — de LLM haalt de pagina op als exacte kopie: [../prompts/fetch.md](../prompts/fetch.md).
2. **Via webclipper** — de gebruiker clipt naar `Clippings/`; de LLM verplaatst en vult frontmatter aan: [../prompts/clip.md](../prompts/clip.md).

PDF's worden geconverteerd met [../prompts/convert-pdf.md](../prompts/convert-pdf.md); complexe webpagina's met [../prompts/crawl.md](../prompts/crawl.md).

Bestandsnaam: beschrijvende slug, lowercase, kebab-case, max 60 tekens. Bestaat de naam al, voeg een numeriek suffix toe (`-2.md`).

## Frontmatter van een bron

```yaml
---
title: "{titel van de pagina}"
source: "{originele URL}"
author: "{auteur of organisatie, leeg als onbekend}"
published: {publicatiedatum, leeg als onbekend}
created: {datum van ophalen}
description: "{korte beschrijving, max 1 zin}"
tags:
  - "{onderwerp}"
---
```

Bij bestanden afkomstig van een gelinkte pagina of PDF komt er een veld `source_page:` bij (de pagina waar de link op stond).

In bronbestanden staan **geen wiki-links** — het zijn kopieën van externe documenten, geen wiki-pagina's.

## GGM als bron

- **Het XMI-bestand is de bron van waarheid** (`Sources/GGM-repository/`). Nooit rechtstreeks lezen — altijd via de parser (zie [../tools/README.md](../tools/README.md)).
- `Sources/GGM/` is de leesbare conversie: letterlijke definities zonder interpretatie.
- `ggm_parsed.json` bevat de technische metadata (GUIDs, GEMMA-tags, relaties, diagrammen).

## GGM-terminologie

Het GGM is hiërarchisch: **taakvelden** (afgeleid van IV3, bijv. "6 Sociaal Domein") bevatten **beleidsdomeinen** (bijv. "Schulden"). Het volledige overzicht staat in `Sources/GGM/structuur-ggm.md`.
