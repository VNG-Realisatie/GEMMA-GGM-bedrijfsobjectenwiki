---
type: bedrijfsobject
naam: Vastgoedcontract
onderwerp: [Vastgoed]
archimate_type: contract
grondslag: ggm-entiteit

ggm_entiteit: Vastgoed Contract
ggm_guid: EAID_1C84E4B6_1BB5_4a0d_A945_FFFDFDFB544B
ggm_uml_type: Class
ggm_beleidsdomein: Vastgoed
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Vastgoed Domeinmodel, Vastgoed verankering RSGB IMBAG]
ggm_diagram_ids: [EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291, EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45]
ggm_definitie: "Een contract is een afspraak tussen 2 of meer partijen. Sluit u een contract, dan moet u een bepaalde prestatie leveren of u heeft recht op een prestatie. Een ander woord voor een contract is een overeenkomst. Daarnaast komt de term overeenkomst van opdracht ook voor."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Vastgoed Contract**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Pachter** (detail) — Detailgegeven (weinig attributen)
  - **Vastgoedcontractregel** (onderdeel) — Onderdeel (naamindicatie)
bo_definitie: "Een contract is een afspraak tussen 2 of meer partijen."
bo_toelichting: "Sluit u een contract, dan moet u een bepaalde prestatie leveren of u heeft recht op een prestatie. Een ander woord voor een contract is een overeenkomst. Daarnaast komt de term overeenkomst van opdracht ook voor."
bo_subtypes: []
bo_via_kandidaten:
  - ggm_entiteit: "Vastgoedcontractregel"
    ggm_guid: "EAID_1C25D70B_AE22_4654_9190_2F55272D9BE6"
    reden: "Een vastgoedcontractregel is onderdeel van een vastgoedcontract — expliciet in de GGM-definitie."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Vastgoedobject]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een contract heeft betrekking op vastgoedobjecten via contractregels"
  - type: associatie
    bedrijfsobject: "[[Verhuurbare Eenheid]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een contractregel betreft een verhuurbare eenheid"
bedrijfsprocessen: [verhuur gemeentelijk vastgoed, huurprijsberekening, leegstandbeheer]
bedrijfsfuncties: [vastgoedexploitatie, vastgoedmanagement]
---

## BO-criteria toetsing

1. **Heeft betekenis** — juridische en financiële grondslag van de vastgoedexploitatie
2. **Herkenbaar** — gestandaardiseerde huurovereenkomsten (ROZ-contracten), huurders en financiën werken ermee
3. **Eigen bestaan** — een contract bestaat onafhankelijk van het vastgoedobject; het vastgoedobject kan bestaan zonder contract
4. **Meervoud** — duizenden huurovereenkomsten in een gemeente als Amsterdam
5. **Levenscyclus** — concept → ondertekening → lopend → indexering → opzegging → beëindiging
6. **Relaties** — naar [[Vastgoedobject]], [[Verhuurbare Eenheid]], Rechtspersoon (huurder)

## Beschrijving

Een vastgoedcontract is de huurovereenkomst tussen de gemeente en een huurder over het gebruik van een [[Vastgoedobject]] of [[Verhuurbare Eenheid]]. De gemeente werkt met gestandaardiseerde huurovereenkomsten en huurvoorwaarden (ROZ-contracten). De huurprijs wordt bepaald door de huurprijssystematiek (kostprijsdekkend of marktconform) en jaarlijks geïndexeerd met de CPI.

Een contract bestaat uit contractregels die elk betrekking hebben op een verhuurbare eenheid of een vastgoedobject. De contractregel legt het bedrag, de frequentie, de looptijd en het type vast.

> "We werken met standaard huurovereenkomsten en huurvoorwaarden. Dat zorgt voor minder administratieve handelingen en meer duidelijkheid voor de huurder, beleidsdirecties en stadsdelen." (bron: Vastgoedstrategie Amsterdam)

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Vastgoedcontract. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Vastgoedcontractregel** — onderdeel van een vastgoedcontract; legt type, omschrijving, bedrag, frequentie en looptijd vast per verhuurbare eenheid

## GGM-bron

> Een contract is een afspraak tussen 2 of meer partijen. Sluit u een contract, dan moet u een bepaalde prestatie leveren of u heeft recht op een prestatie.

- **Entiteit:** Vastgoed Contract
- **Beleidsdomein:** Vastgoed
- **Attributen:** datumStart, datumEinde, maandbedrag, beschrijving, status, type, identificatie, opzegtermijn
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | naar-dit-BO | 1..* | Via vastgoedcontractregel | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/verhuurbare-eenheid\|Verhuurbare Eenheid]] | naar-dit-BO | 0..* | Via vastgoedcontractregel | GGM |

## Bedrijfsprocessen

- Verhuur en exploitatie van gemeentelijk vastgoed
- Huurprijsberekening (kostprijsdekkend, marktconform, algemeenbelangbesluit)
- Procedure vrijkomend vastgoed
- Leegstandbeheer en tijdelijke verhuur
- Huurindexering (CPI)

## Bronnen

- [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam]]
