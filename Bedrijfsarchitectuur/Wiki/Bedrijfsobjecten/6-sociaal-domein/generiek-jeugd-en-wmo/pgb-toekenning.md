---
type: bedrijfsobject
naam: PGB-Toekenning
domein: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: PGB-Toekenning
ggm_guid: EAID_84FE9B56_158D_4b65_BCC1_5FE29D071FCC
ggm_uml_type: Class
ggm_beleidsdomein: "Generiek Jeugd en Wmo"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: ["Sociaal Domein Beschikking en Voorziening: Domain Objects"]
ggm_diagram_ids: [EAID_5AE29494_3572_4924_B2B8_3206E55D71BB]
ggm_definitie: "Betreft alleen toegekende voorzieningen met als leveringsvorm PGB"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: GGM

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Toekenning van een persoonsgebonden budget aan een cliënt voor inkoop van eigen zorg of ondersteuning."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "volgt uit beschikking (via Beschikte Voorziening)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening|Voorziening]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft voorziening met leveringsvorm PGB"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "toegekend aan cliënt"
bedrijfsprocessen: [PGB toekennen, PGB-budget bewaken, PGB-verantwoording verwerken]
bedrijfsfuncties: [beschikkingenbeheer, financieel beheer sociaal domein]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | PGB is een wettelijk verankerde leveringsvorm in Wmo en Jeugdwet |
| Besproken op bestuurlijk niveau | ✅ | PGB-aantallen en -budgetten in programmabegroting en raadsinformatie |
| Vastgelegd in systemen | ✅ | Geregistreerd in suite voor sociaal domein, budget via SVB |
| Eigen attributen | ✅ | datumToekenning, budget, datumEinde |
| Relaties met andere objecten | ✅ | Beschikking, Voorziening, Client |
| Levenscyclus | ✅ | Toegekend bij beschikking, budget wordt uitgeput, eindigt bij einddatum of intrekking |

## Beschrijving

Een PGB-toekenning is de toekenning van een persoonsgebonden budget aan een cliënt die ervoor kiest zelf zorg of ondersteuning in te kopen in plaats van zorg in natura te ontvangen. Het PGB wordt beheerd door de Sociale Verzekeringsbank (SVB), die namens de gemeente de betalingen aan zorgverleners uitvoert. De gemeente bewaakt het budget en de verantwoording.

## GGM-bron

> "Betreft alleen toegekende voorzieningen met als leveringsvorm PGB" — GGM Generiek Jeugd en Wmo

- **Entiteit:** PGB-Toekenning
- **Beleidsdomein:** Generiek Jeugd en Wmo
- **Attributen:** datumToekenning, budget, datumEinde
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | ← | 1 | volgt uit beschikking (via Beschikte Voorziening) | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | ← | 1 | betreft voorziening met leveringsvorm PGB | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 | toegekend aan cliënt | GGM |

## Bedrijfsprocessen

- PGB toekennen
- PGB-budget bewaken
- PGB-verantwoording verwerken

## Bedrijfsfuncties

- Beschikkingenbeheer
- Financieel beheer sociaal domein

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/maatwerkvoorzieningen-wmo]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsregels-jeugdhulp-oost-gelre]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015]]
