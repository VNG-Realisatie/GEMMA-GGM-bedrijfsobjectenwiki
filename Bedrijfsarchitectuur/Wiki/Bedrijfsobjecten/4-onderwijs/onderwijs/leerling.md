---
type: bedrijfsobject
naam: Leerling
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Leerling
ggm_guid: EAID_266057AF_58BD_42e1_B4D5_16EB266B9B7A
ggm_uml_type: Class
ggm_beleidsdomein: Onderwijs
ggm_taakveld: "4 Onderwijs"
ggm_diagram: [Diagram Beslissingen Leerplicht, "Onderwijs: Leerlingen", "Onderwijs: Relaties met Kern"]
ggm_diagram_ids: [EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308, EAID_33E38059_C973_43ff_97EC_B629923074FF, EAID_D33047E8_3A39_4171_A7EC_93B137023ED8]
ggm_definitie: "Mens die een opleiding volgt, heeft gevolgd of gaat volgen of opgaat of is opgegaan voor een toets. (Bron: KOI)"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: Leerling
ggm_gemma_guid: e2ea124f-56ce-4614-9e32-0f13371a5ede
ggm_gemma_definitie: "Mens die een opleiding volgt, heeft gevolgd of gaat volgen of opgaat of is opgegaan voor een toets. (Bron: KOI)"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: "Onderwijsvolger"
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-e2ea124f-56ce-4614-9e32-0f13371a5ede
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Kind of jongere dat onderwijs volgt aan een school in de gemeente."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[School]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Leerling is ingeschreven bij school
  - type: associatie
    bedrijfsobject: "[[Opleidingsinschrijving]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Leerling heeft inschrijvingen
  - type: associatie
    bedrijfsobject: "[[Uitschrijving]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Leerling heeft uitschrijvingen
  - type: associatie
    bedrijfsobject: "[[Verzuimmelding]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Verzuimmelding betreft leerling
  - type: associatie
    bedrijfsobject: "[[Leerplichtvrijstelling]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Vrijstelling betreft leerling
  - type: associatie
    bedrijfsobject: "[[Procesverbaal Onderwijs]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Procesverbaal betreft leerling
  - type: associatie
    bedrijfsobject: "[[Ouder Of Verzorger]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Ouder of verzorger is verantwoordelijk voor leerling
  - type: associatie
    bedrijfsobject: "[[Aanvraag Leerlingenvervoer]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Aanvraag leerlingenvervoer betreft leerling
bedrijfsprocessen: [Leerplichthandhaving, Leerlingenvervoer, Onderwijshuisvesting]
bedrijfsfuncties: [Onderwijsbeleid, Leerplicht]
---

## BO-criteria toetsing

6/6 criteria: heeft betekenis (ja), herkenbaar (ja), eigen bestaan (ja), meervoud (ja), levenscyclus (ja — leerling wordt ingeschreven, volgt onderwijs, wordt uitgeschreven), relaties (ja — met school, inschrijving, verzuimmelding, ouder/verzorger).

## Beschrijving

Een leerling is een kind of jongere dat onderwijs volgt aan een school in de gemeente. De gemeente houdt leerlingen bij voor leerplichthandhaving (verzuimregistratie, vrijstellingen), leerlingenvervoer en capaciteitsplanning van onderwijshuisvesting. In het GGM erft Leerling van IngeschrevenPersoon. Het attribuut kwetsbareJongere markeert leerlingen die extra aandacht nodig hebben in het kader van voortijdig schoolverlaten.

## GGM-bron

> "Mens die een opleiding volgt, heeft gevolgd of gaat volgen of opgaat of is opgegaan voor een toets. (Bron: KOI)" — GGM, entiteit Leerling, beleidsdomein Onderwijs

- **Entiteit:** Leerling
- **Beleidsdomein:** Onderwijs
- **Attributen:** kwetsbareJongere
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving |
|---|---|---|---|---|
| [[School]] | associatie | van-dit-BO | 1..* | Leerling is ingeschreven bij school |
| [[Opleidingsinschrijving]] | associatie | van-dit-BO | 1..* | Leerling heeft inschrijvingen |
| [[Uitschrijving]] | associatie | van-dit-BO | 0..* | Leerling heeft uitschrijvingen |
| [[Verzuimmelding]] | associatie | van-dit-BO | 0..* | Verzuimmelding betreft leerling |
| [[Leerplichtvrijstelling]] | associatie | van-dit-BO | 0..* | Vrijstelling betreft leerling |
| [[Procesverbaal Onderwijs]] | associatie | van-dit-BO | 0..* | Procesverbaal betreft leerling |
| [[Ouder Of Verzorger]] | associatie | naar-dit-BO | 1..* | Ouder of verzorger is verantwoordelijk voor leerling |
| [[Aanvraag Leerlingenvervoer]] | associatie | van-dit-BO | 0..* | Aanvraag leerlingenvervoer betreft leerling |

## Bedrijfsprocessen

- Leerplichthandhaving — verzuimregistratie, procesverbaal, vrijstellingen
- Leerlingenvervoer — aanvragen en toekennen van vervoersvoorzieningen
- Onderwijshuisvesting — capaciteitsplanning op basis van leerlingaantallen

## Bedrijfsfuncties

- Onderwijsbeleid
- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/passend-onderwijs]]
- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
- [[Wiki/Bronsamenvattingen/onderwijs/beleidsnota-onderwijshuisvesting-utrecht]]
