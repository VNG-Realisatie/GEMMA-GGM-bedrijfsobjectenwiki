---
type: element
naam: Koppeling
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Koppeling
ggm_guid: EAID_AB7CF266_388F_413a_92D0_B2FA67C75633
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items]
ggm_diagram_ids: [EAID_4F14E8D8_5502_4880_9E83_D912BE451EB1]
ggm_definitie: "Verbinding tussen twee systemen"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Koppeling** als directe tegenhanger.
bo_definitie: "Systematiek voor uitwisseling van data tussen systemen binnen of buiten het applicatielandschap."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Koppeling verbindt applicaties onderling of met externe systemen"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server|Server]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Koppeling loopt via servers"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database|Database]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Koppeling kan data uitwisselen met databases"
bedrijfsprocessen: [Applicatiebeheer, Integratiebeheer, Wijzigingsbeheer]
bedrijfsfuncties: [Informatievoorziening, ICT-beheer]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Systematiek voor data-uitwisseling tussen systemen; kern van het applicatielandschap |
| Herkenbaarheid | "de StUF-koppeling", "de API naar het zaaksysteem", "de BRP-koppeling" |
| Eigen bestaan | 3 attributen in GGM (direct, beschrijving, toelichting); relaties met Linkbaar CMDB-item |
| Meervoud | Tientallen tot honderden per gemeente |
| Levenscyclus | Ontwerp → realisatie → testen → operationeel → onderhoud → uitfasering |
| Relaties | Applicatie, Database, Server, Software |

Resultaat: 6/6 — BO.

## Beschrijving

Een koppeling is de systematiek waarmee twee systemen data uitwisselen. In het gemeentelijk applicatielandschap verbinden koppelingen applicaties onderling (bijv. zaaksysteem ↔ DMS) en met externe systemen (bijv. BRP-bevraging bij RvIG, StUF-berichten naar ketenpartners).

De GIBIT 2025 definieert een koppeling als "de systematiek voor uitwisseling van Data tussen enerzijds de ICT Prestatie en anderzijds (onderdelen van) het Applicatielandschap". Elke koppeling heeft een eigen levenscyclus: ontwerpen, bouwen, testen, in productie nemen, onderhouden bij versie-updates, en uitfaseren bij applicatievervanging. Koppelingen zijn een belangrijk aandachtspunt bij impactanalyses: wijziging van één applicatie kan tientallen koppelingen raken.

In het GGM relateert Koppeling aan Linkbaar CMDB-item (waarvan [[Applicatie]], [[Database]] en [[Server]] subtypes zijn). Een koppeling verbindt altijd twee Linkbare CMDB-items.

## GGM-bron

> "Verbinding tussen twee systemen"
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Koppeling | Matchsterkte: **exact** | Attributen: direct, beschrijving, toelichting

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | Koppeling verbindt applicaties onderling of met externe systemen |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] | naar-dit-BO | Koppeling loopt via servers |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database\|Database]] | naar-dit-BO | Koppeling kan data uitwisselen met databases |

## Bedrijfsprocessen

- **Applicatiebeheer** — koppelingen beheren als onderdeel van het applicatielandschap
- **Integratiebeheer** — ontwerpen, testen en monitoren van koppelingen
- **Wijzigingsbeheer** — impactanalyse bij wijzigingen aan gekoppelde systemen

## Bedrijfsfuncties

- **Informatievoorziening** — koppelingen als ruggengraat van de informatiehuishouding
- **ICT-beheer** — technisch beheer van integratieplatformen en berichtenverkeer

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/gibit-2025|GIBIT 2025]]
- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer|CMDB & Informatiebeheerplan]]
