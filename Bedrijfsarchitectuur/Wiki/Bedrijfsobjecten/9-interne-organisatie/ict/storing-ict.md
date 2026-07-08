---
type: bedrijfsobject
naam: Storing (ICT)
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Storing
ggm_guid: EAID_4E5F272E_00CA_481c_A51B_7D08B5E6B0A9
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren."
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
  Dit BO is de hernoeming van GGM-entiteit **Storing**. Daarnaast is **Storing** (beleidsdomein Beheer Openbare Ruimte) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Verlies van de mogelijkheid van een ICT-component om volgens specificatie te werken of het vereiste resultaat te leveren."
bo_toelichting: ''
bo_homoniemen:
  - bedrijfsobject: ""
    ggm_entiteit: Storing
    ggm_guid: EAID_0EF67A8B_AEBE_4a00_B1EF_2EFD0DCC9F5D
    ggm_beleidsdomein: Beheer Openbare Ruimte
    toelichting: "BOR-storing betreft uitval van fysieke assets in de openbare ruimte (straatverlichting, gemaal); ICT-storing betreft uitval van informatiesystemen."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Storing treft een applicatie"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/wijzigingsverzoek|Wijzigingsverzoek]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Storing kan leiden tot een wijzigingsverzoek"
bedrijfsprocessen: [Incidentbeheer, Probleembeheer]
bedrijfsfuncties: [ICT-beheer, Dienstverlening]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Incident waarbij een ICT-component niet naar specificatie werkt |
| Herkenbaarheid | "storing in het zaaksysteem", "e-mailstoring", "netwerkstoring" |
| Eigen bestaan | Eigen levenscyclus en impact; GIBIT beschrijft meld- en herstelprocedures |
| Meervoud | Dagelijks tot wekelijks |
| Levenscyclus | Melding → diagnose → workaround → herstel → evaluatie |
| Relaties | Applicatie, Server, Wijzigingsverzoek |

Resultaat: 5/6 — BO.

## Naamkeuze

De GGM-entiteitnaam "Storing" is een homoniem — dezelfde naam wordt in beleidsdomein Beheer Openbare Ruimte gebruikt voor een ander concept (uitval van fysieke assets in de openbare ruimte). Dit BO heet **Storing (ICT)**.

**Overwogen namen:**
- **Storing (ICT)** — gekozen: duidelijke disambiguatie, herkenbaar
- ICT-storing — niet gekozen: ongebruikelijk als samengesteld woord
- Incident — niet gekozen: bredere ITIL-term die ook niet-storingen omvat

## Beschrijving

Een ICT-storing is het verlies van de mogelijkheid van een ICT-component om volgens specificatie te werken. De GIBIT 2025 beschrijft het melden van storingen en gebreken bij de leverancier (art. 10), inclusief reactietijden en functiehersteltijden als Service Levels.

In het ITSM-model (ITIL) is een storing onderdeel van het incidentbeheerproces. De CMDB-bron beschrijft hoe CMDB-data wordt gebruikt voor root cause analysis en impactanalyse bij storingen.

## GGM-bron

> "Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren."
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Storing | Matchsterkte: **exact** | Attributen: *(geen in GGM)*

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | Storing treft een applicatie |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/wijzigingsverzoek\|Wijzigingsverzoek]] | van-dit-BO | Storing kan leiden tot een wijzigingsverzoek |

## Bedrijfsprocessen

- **Incidentbeheer** — melding, diagnose, workaround, herstel
- **Probleembeheer** — structurele oorzaakanalyse na herhaalde storingen

## Bedrijfsfuncties

- **ICT-beheer** — technische afhandeling van storingen
- **Dienstverlening** — impact op dienstverlening aan inwoners

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/gibit-2025|GIBIT 2025]]
- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer|CMDB & Informatiebeheerplan]]
