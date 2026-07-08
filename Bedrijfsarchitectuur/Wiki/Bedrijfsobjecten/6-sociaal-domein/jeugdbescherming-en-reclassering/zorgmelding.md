---
type: bedrijfsobject
naam: Zorgmelding
domein:
- maatschappelijke ondersteuning
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Zorgmelding
ggm_guid: EAID_B852AF03_A5E0_4148_AFC1_108509FF8BBD
ggm_uml_type: Class
ggm_beleidsdomein: Jeugdbescherming en reclassering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Zorgmelding
ggm_diagram_ids:
- EAID_96845001_991F_4bd6_9249_FBE26A26AC4C
ggm_definitie: Een Zorgmelding is een officiële melding bij een gemeente of jeugdhulporganisatie waarin zorgen worden geuit over de veiligheid, gezondheid, of ontwikkeling van een kind of jongere.
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Zorgmelding** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Incident** (detail) — Detailgegeven
  - **Informering** (detail) — Detailgegeven (weinig attributen)
  - **Leefgebied** (detail) — Detailgegeven (weinig attributen)
  - **Zorgelijke Situatie** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Een Zorgmelding is een officiële melding bij een gemeente of jeugdhulporganisatie waarin zorgen worden geuit over de veiligheid, gezondheid, of ontwikkeling van een kind of jongere."
bo_toelichting: ''
bo_relaties:
- type: associatie
  bedrijfsobject: NatuurlijkPersoon
  richting: van-dit-BO
  kardinaliteit: '1'
  beschrijving: betreft een persoon
- type: associatie
  bedrijfsobject: Medewerker
  richting: van-dit-BO
  kardinaliteit: 0..1
  beschrijving: betrokken professional
- type: generalisatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|Aanvraag of melding]]'
  richting: naar-dit-BO
  kardinaliteit: ''
  beschrijving: specialisatie van AanvraagOfMelding (abstract)
bedrijfsprocessen:
- melding kindermishandeling beoordelen
- onderzoek Veilig Thuis
- triage zorgmelding
bedrijfsfuncties:
- jeugdbescherming
- veilig thuis
---

# Zorgmelding

Melding bij de gemeente of Veilig Thuis over de veiligheid of ontwikkeling van een kind, als startpunt voor beoordeling en eventuele beschermingsmaatregelen.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | De gemeente registreert zorgmeldingen met soort, omschrijving, verzoek en terugkoppelingsvoorkeur |
| Meervoud | Honderden tot duizenden meldingen per gemeente per jaar |
| Levenscyclus | Ontvangst → triage → onderzoek → besluit (beschermingsmaatregel of afsluiting) |
| Eigendom | De gemeente ontvangt de melding en is verantwoordelijk voor de beoordeling |
| Gemeentelijk belang | Kernproces binnen jeugdbescherming; wordt gerapporteerd in beleidsinformatie |
| Bronnen | Kindermishandeling en huiselijk geweld, beleidsnota Jeugd Utrecht |

## Beschrijving

Een zorgmelding is het formele startpunt van het beschermingsproces. Professionals, burgers of instellingen kunnen bij de gemeente of Veilig Thuis een melding doen wanneer zij zorgen hebben over de veiligheid, gezondheid of ontwikkeling van een kind of jongere. De melding wordt beoordeeld op ernst en urgentie en kan leiden tot een onderzoek door Veilig Thuis, inzet van vrijwillige jeugdhulp of een verzoek tot een kinderbeschermingsmaatregel.

Het GGM modelleert Zorgmelding als specialisatie van AanvraagOfMelding (abstract), met specifieke attributen voor het type melding, de omschrijving en of terugkoppeling gewenst is. De relatie met Zorgelijke Situatie legt het verband met de aanleiding voor de melding.

## GGM-bron

> Een Zorgmelding is een officiële melding bij een gemeente of jeugdhulporganisatie waarin zorgen worden geuit over de veiligheid, gezondheid, of ontwikkeling van een kind of jongere.

- **Entiteit:** Zorgmelding
- **Beleidsdomein:** Jeugdbescherming en reclassering (taakveld 6 — Sociaal Domein)
- **Attributen:** zorgmeldingsoort, terugkoppelingGewenst, verzoek, omschrijving, nadereOmschrijving
- **Overerving:** AanvraagOfMelding (abstract) → Zorgmelding
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Richting | Kardinaliteit |
|---|---|---|---|
| Betreft persoon | NatuurlijkPersoon | → | 1 |
| Naar aanleiding van | Zorgelijke Situatie | ← | 0..* |
| Betrokken professional | Medewerker | → | 0..1 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/kindermishandeling-en-huiselijk-geweld]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]
