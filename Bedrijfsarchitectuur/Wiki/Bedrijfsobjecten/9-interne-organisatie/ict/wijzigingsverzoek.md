---
type: bedrijfsobject
naam: Wijzigingsverzoek
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Wijzigingsverzoek
ggm_guid: EAID_EFBF46D1_6A51_44fd_BAEA_47BCDFEEE27A
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "Een aanvraag voor wijziging"
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
  Dit BO heeft de GGM-entiteit **Wijzigingsverzoek** als directe tegenhanger.
bo_definitie: "Aanvraag voor een wijziging aan een ICT-component of het applicatielandschap."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Wijzigingsverzoek betreft een applicatie"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/storing-ict|Storing (ICT)]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Wijzigingsverzoek kan voortkomen uit een storing"
bedrijfsprocessen: [Wijzigingsbeheer, Releasebeheer]
bedrijfsfuncties: [ICT-beheer]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Formele aanvraag voor wijziging aan IT-landschap; kern van change management |
| Herkenbaarheid | "change request", "RFC", "wijzigingsaanvraag" |
| Eigen bestaan | Eigen levenscyclus; ITIL change management proces |
| Meervoud | Wekelijks tot maandelijks |
| Levenscyclus | Indienen → beoordelen → goedkeuren → plannen → implementeren → afsluiten |
| Relaties | Applicatie, Storing, Server |

Resultaat: 5/6 — BO.

## Beschrijving

Een wijzigingsverzoek is een formele aanvraag voor een wijziging aan het applicatielandschap of de IT-infrastructuur. In het ITSM-model (ITIL) is change management een kernproces: elke significante wijziging doorloopt een beoordelings- en goedkeuringsproces.

De CMDB-bron beschrijft hoe CMDB-data wordt gebruikt voor impactanalyse bij wijzigingsverzoeken: welke systemen worden geraakt, welke afhankelijkheden bestaan. De GIBIT 2025 regelt onderhoud en wijzigingen contractueel via de SLA.

## GGM-bron

> "Een aanvraag voor wijziging"
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Wijzigingsverzoek | Matchsterkte: **exact** | Attributen: *(geen in GGM)*

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | Wijzigingsverzoek betreft een applicatie |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/storing-ict\|Storing (ICT)]] | naar-dit-BO | Wijzigingsverzoek kan voortkomen uit een storing |

## Bedrijfsprocessen

- **Wijzigingsbeheer** — beoordeling, goedkeuring en planning van wijzigingen
- **Releasebeheer** — bundeling van wijzigingen in releases

## Bedrijfsfuncties

- **ICT-beheer** — uitvoering van goedgekeurde wijzigingen

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/gibit-2025|GIBIT 2025]]
- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer|CMDB & Informatiebeheerplan]]
