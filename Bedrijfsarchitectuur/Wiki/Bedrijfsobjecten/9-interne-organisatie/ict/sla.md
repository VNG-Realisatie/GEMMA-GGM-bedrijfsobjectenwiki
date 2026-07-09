---
type: element
naam: Service Level Agreement
onderwerp: [Informatiesystemen]
archimate_type: contract
grondslag: governance-object

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
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

bo_definitie: "Nadere overeenkomst met concrete afspraken over het onderhoudsniveau van een ICT-prestatie, inclusief service levels en maatregelen bij niet-naleving."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract|Contract]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "SLA is een nadere overeenkomst bij een IT-contract"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "SLA beschrijft het onderhoudsniveau voor een applicatie"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier|Leverancier]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "SLA wordt afgesloten met een leverancier"
bedrijfsprocessen: [Leveranciersmanagement, Incidentbeheer, Servicebeheer]
bedrijfsfuncties: [ICT-beheer, Inkoop]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Contractueel instrument dat onderhoudsnormen vastlegt; essentieel voor IT-dienstverlening |
| Herkenbaarheid | "de SLA met TOPdesk", "de SLA voor het zaaksysteem" |
| Eigen bestaan | Eigen attributen: reactietijd, functiehersteltijd, beschikbaarheid, meetperiodes |
| Meervoud | Per leverancier/applicatie een SLA |
| Levenscyclus | Opstellen → afsluiten → monitoren → evalueren → bijstellen → beëindigen |
| Relaties | Contract, Applicatie, Leverancier |

Resultaat: 6/6 — BO (governance-object).

## Juridische bron

De GIBIT 2025 (art. 10.10–10.13) definieert de SLA als "de nadere overeenkomst met betrekking tot het Onderhoud, waaronder begrepen het soort Onderhoud dat wordt verleend en de daarop toepasselijke Service Levels." Verplichte service levels zijn de reactietijd en de functiehersteltijd.

## Beschrijving

Een Service Level Agreement (SLA) is een nadere overeenkomst bij een IT-contract waarin concrete afspraken staan over het onderhoudsniveau. De GIBIT 2025 beschrijft vier typen onderhoud (correctief, preventief, innovatief en gebruikersondersteuning) en verplicht twee service levels:

- **Reactietijd** — de tijd waarbinnen de leverancier adequaat moet reageren op een melding
- **Functiehersteltijd** — de periode tussen melding en herstel van een gebrek

Bij herhaald niet halen van service levels kan de gemeente een verbeterplan eisen of de overeenkomst ontbinden. De SLA relateert aan [[Contract]] (waarvan het een nadere overeenkomst is), [[Applicatie]] (waarvoor het geldt) en [[Leverancier]] (met wie het is afgesloten).

Geen GGM-match: het GGM modelleert data-objecten maar geen contractuele instrumenten. Dit is een structureel hiaat (governance-objecten vallen buiten de GGM-scope).

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract\|Contract]] | naar-dit-BO | SLA is een nadere overeenkomst bij een IT-contract |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | SLA beschrijft het onderhoudsniveau voor een applicatie |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | naar-dit-BO | SLA wordt afgesloten met een leverancier |

## Bedrijfsprocessen

- **Leveranciersmanagement** — afsluiten, monitoren en evalueren van SLA's
- **Incidentbeheer** — SLA bepaalt responstijden bij storingen
- **Servicebeheer** — bewaking van service levels

## Bedrijfsfuncties

- **ICT-beheer** — monitoring en rapportage van SLA-naleving
- **Inkoop** — contractuele afspraken over service levels

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/gibit-2025|GIBIT 2025]]
