---
type: bedrijfsobject
naam: Raadsstuk
onderwerp: [bestuur]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Raadsstuk
ggm_guid: EAID_440219A4_C64B_4eac_ADE5_E79ED6AA9BFE
ggm_uml_type: Class
ggm_beleidsdomein: Griffie
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_diagram:
  - Diagram Griffie
  - Diagram Raadsstukken
ggm_diagram_ids:
  - EAID_A9F0B77B_05F3_4c36_96A0_8841BBAE47E0
  - EAID_108224FC_E160_417a_AFC5_68A484B3B8AE
ggm_definitie: "Stuk dat door de gemeenteraad wordt behandeld"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM

ggm_gemma_naam: Raadsstuk
ggm_gemma_guid: 378dab8d-1135-40b8-9ed5-3591a89c75c2
ggm_gemma_definitie: "Stuk dat door de gemeenteraad wordt behandeld"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-378dab8d-1135-40b8-9ed5-3591a89c75c2"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

bo_definitie: "Stuk dat door de gemeenteraad wordt behandeld"
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Vergadering]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "wordt behandeld in vergadering"
  - type: associatie
    bedrijfsobject: "[[Stemming]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "stemming betreft raadsstuk"
bedrijfsprocessen:
  - Raadsbesluitvorming
  - Vergadervoorbereiding
bedrijfsfuncties:
  - Griffie
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Identificeerbaar | ✅ Elk raadsstuk heeft registratiedatum, publicatiedatum, type |
| Levenscyclus | ✅ Registratie → publicatie → agendering → behandeling → besluit → archivering |
| Eigenschap-dragend | ✅ datumRegistratie, datumPublicatie, datumExpiratie, besloten, typeRaadsstuk |
| Relaties | ✅ Naar vergadering, agendapunt, stemming, indiener, categorie, dossier |
| Bedrijfsrelevantie | ✅ Kernobject van raadsinformatiesysteem; wettelijke publicatie- en archiveringsplicht |
| Gemeentelijk | ✅ Gemeentewet art. 19, 23, 32a, 87-94; griffier ondertekent mee (art. 107d) |

Score: **6/6**

## Beschrijving

Een raadsstuk is een document dat door de gemeenteraad wordt behandeld. Het omvat moties, amendementen, initiatiefvoorstellen, raadsvragen, raadsvoorstellen en verslagen. Raadsstukken doorlopen een formeel proces van indiening, agendering, behandeling in vergadering, en (bij besluitstukken) stemming. De griffier draagt zorg voor registratie, publicatie en archivering.

De Gemeentewet stelt eisen aan openbaarheid (art. 23, 91): stukken zijn in beginsel openbaar, tenzij geheimhouding is opgelegd (art. 87-94). De griffier tekent stukken van de raad mee (art. 107d).

## Subtypes

Herkende specialisaties van Raadsstuk. Gevonden in bronnen en GGM (attribuut typeRaadsstuk). Geen apart BO.

- **Motie** — verzoek of uitspraak van de raad, ingediend tijdens vergadering
- **Amendement** — wijzigingsvoorstel op een raadsbesluit
- **Initiatiefvoorstel** — voorstel van een of meer raadsleden
- **Raadsvraag** — schriftelijke of mondelinge vraag van raadslid aan college
- **Raadsvoorstel** — voorstel van college aan raad ter besluitvorming
- **Vergaderverslag** — verslag van een raadsvergadering

## GGM-componenten

GGM-entiteiten die onderdeel zijn van het raadsstukkendomein. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Categorie** — classificatie van raadsstukken (relatie: heeft)
- **Dossier** — samenhangende set raadsstukken (relatie: hoort bij)
- **Indiener** — persoon die raadsstuk indient; kan raadslid of collegelid zijn
- **Programma** — programma waaronder raadsstuk valt (relatie: hoort bij)
- **Taakveld** — taakveld waaronder raadsstuk valt (relatie: heeft)

## GGM-bron

> "Stuk dat door de gemeenteraad wordt behandeld"
> — GGM, beleidsdomein Griffie, taakveld 0

**Entiteit:** Raadsstuk
**Attributen:** datumRegistratie, datumPublicatie, datumExpiratie, besloten, typeRaadsstuk
**Matchsterkte:** exact — 1:1 mapping, definitie en attributen passen volledig

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/vergadering\|Vergadering]] | associatie | van-dit-BO | 0..* | wordt behandeld in vergadering | GGM |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/stemming\|Stemming]] | associatie | naar-dit-BO | 0..1 | stemming betreft raadsstuk | GGM |

## Bedrijfsprocessen

- **Raadsbesluitvorming** — het primaire proces van agendering, behandeling en besluitvorming
- **Vergadervoorbereiding** — het samenstellen van de agenda en bijbehorende stukken

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst]]
- [[Wiki/Bronsamenvattingen/Bestuur/positionering-griffier]]
