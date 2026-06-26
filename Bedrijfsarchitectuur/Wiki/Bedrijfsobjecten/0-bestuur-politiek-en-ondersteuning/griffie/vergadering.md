---
type: bedrijfsobject
naam: Vergadering
onderwerp: [bestuur]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vergadering
ggm_guid: EAID_257F4ABF_7CCD_453f_B2E8_5A6434383A9B
ggm_uml_type: Class
ggm_beleidsdomein: Griffie
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_diagram:
  - Diagram Griffie
ggm_diagram_ids:
  - EAID_A9F0B77B_05F3_4c36_96A0_8841BBAE47E0
ggm_definitie: "Een bijeenkomst van meerdere mensen (meestal van eenzelfde organisatie) die met elkaar spreken en/of afspraken maken over de gemeenschappelijke toekomst."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM

ggm_gemma_naam: Vergadering
ggm_gemma_guid: ea768404-3043-48bc-b0dc-143abc8806d6
ggm_gemma_definitie: "Een bijeenkomst van meerdere mensen (meestal van eenzelfde organisatie) die met elkaar spreken en/of afspraken maken over de gemeenschappelijke toekomst."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-ea768404-3043-48bc-b0dc-143abc8806d6"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

gemma_definitie: "Formele bijeenkomst van de gemeenteraad, een raadscommissie of het college, met agenda, registratie van aanwezigheid en besluitenlijst."
gemma_subtypes: []
relaties:
  - type: associatie
    bedrijfsobject: "[[Raadsstuk]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "raadsstukken worden behandeld in vergadering"
  - type: associatie
    bedrijfsobject: "[[Stemming]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "vergadering bevat stemmingen (via agendapunten)"
bedrijfsprocessen:
  - Raadsbesluitvorming
  - Vergadervoorbereiding
bedrijfsfuncties:
  - Griffie
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Identificeerbaar | ✅ Elke vergadering heeft starttijd, eindtijd, titel, locatie |
| Levenscyclus | ✅ Oproeping → agendering → opening (quorum) → beraadslaging → sluiting → verslag |
| Eigenschap-dragend | ✅ starttijd, eindtijd, titel, locatie |
| Relaties | ✅ Naar agendapunten, raadsstukken, aanwezige deelnemers, raadscommissie, video-opname |
| Bedrijfsrelevantie | ✅ Kernproces van lokale democratie; wettelijke openbaarheids- en verslagplicht |
| Gemeentelijk | ✅ Gemeentewet art. 17-24: vergaderregels, quorum, openbaarheid, besluitenlijst |

Score: **6/6**

## Beschrijving

Een vergadering is een formele bijeenkomst van de gemeenteraad, een raadscommissie of het college. De Gemeentewet stelt gedetailleerde eisen: de burgemeester roept de raad bijeen (art. 17, 19), vergaderingen zijn openbaar tenzij de deuren worden gesloten (art. 23), een quorum van meer dan de helft is vereist (art. 20), en van elke vergadering wordt een besluitenlijst opgemaakt (art. 23).

De griffier bereidt vergaderingen voor, stelt de agenda samen, bewaakt de termijnagenda en draagt zorg voor de verslaglegging (art. 107-107a). Raadsstukken worden via agendapunten aan vergaderingen gekoppeld.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Vergadering. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Agendapunt** — onderwerp dat in de vergadering wordt behandeld; koppelt raadsstukken aan vergadering (attributen: nummer, titel, omschrijving)
- **Aanwezige Deelnemer** — registratie van aanwezigheid bij vergadering met aanvang, einde, rol
- **Video-opname** — audiovisuele registratie van de vergadering

## GGM-bron

> "Een bijeenkomst van meerdere mensen (meestal van eenzelfde organisatie) die met elkaar spreken en/of afspraken maken over de gemeenschappelijke toekomst."
> — GGM, beleidsdomein Griffie, taakveld 0

**Entiteit:** Vergadering
**Attributen:** eindtijd, starttijd, titel, locatie
**Matchsterkte:** exact — 1:1 mapping

## BO-definitie

De GGM-definitie is generiek ("meerdere mensen die afspraken maken"). De GEMMA-definitie specificeert naar de gemeentelijke context: formele bijeenkomst van raad, commissie of college met wettelijke vereisten.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/raadsstuk\|Raadsstuk]] | associatie | naar-dit-BO | 0..* | raadsstukken worden behandeld in vergadering | GGM |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/stemming\|Stemming]] | associatie | van-dit-BO | 0..* | vergadering bevat stemmingen | GGM (via Agendapunt) |

## Bedrijfsprocessen

- **Raadsbesluitvorming** — vergadering is het besluitvormingsmoment
- **Vergadervoorbereiding** — het plannen, oproepen en agenderen

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst]]
- [[Wiki/Bronsamenvattingen/Bestuur/positionering-griffier]]
