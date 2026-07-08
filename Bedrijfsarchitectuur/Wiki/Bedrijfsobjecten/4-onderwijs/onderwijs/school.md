---
type: element
naam: School
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: School
ggm_guid: EAID_32DFC5DD_79D9_45d5_8F9D_7D5125961817
ggm_uml_type: Class
ggm_beleidsdomein: Onderwijs
ggm_taakveld: "4 Onderwijs"
ggm_diagram: [Diagram Beslissingen Leerplicht, "Onderwijs: Leerlingen", "Onderwijs: Relaties met Kern", Diagram Sportbeleid]
ggm_diagram_ids: [EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308, EAID_33E38059_C973_43ff_97EC_B629923074FF, EAID_D33047E8_3A39_4171_A7EC_93B137023ED8, EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F]
ggm_definitie: "Gebouw in gebruik voor basis, middelbaar of hoger onderwijs."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: School
ggm_gemma_guid: f2c26bb2-4c76-4b03-8ceb-6397b5a12ae8
ggm_gemma_definitie: "Gebouw in gebruik voor basis, middelbaar of hoger onderwijs."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-f2c26bb2-4c76-4b03-8ceb-6397b5a12ae8
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **School** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Onderwijssoort** (detail) — Classificatie; attribuut van School
bo_definitie: "Instelling voor funderend onderwijs waarvoor de gemeente verantwoordelijk is voor de huisvesting."
bo_toelichting: ''
bo_subtypes:
  - naam: PO-school
    omschrijving: "School voor primair onderwijs"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: VO-school
    omschrijving: "School voor voortgezet onderwijs"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: SO/SBO/VSO-school
    omschrijving: "School voor speciaal (basis/voortgezet) onderwijs"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: Buurtschool
    omschrijving: "Multifunctionele school met maatschappelijke partners in de wijk"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: Kindcentrum
    omschrijving: "Integrale voorziening onderwijs en kinderopvang 0-12 jaar"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: Multifunctionele accommodatie
    omschrijving: "Gebouw waar meerdere (overwegend maatschappelijke) organisaties voorzieningen aanbieden"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Leerling is ingeschreven bij school
  - type: associatie
    bedrijfsobject: "[[Opleidingsinschrijving]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: School heeft inschrijvingen
  - type: associatie
    bedrijfsobject: "[[Verzuimmelding]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: School meldt verzuim
  - type: associatie
    bedrijfsobject: "[[Leerplichtvrijstelling]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Vrijstelling betreft school
bedrijfsprocessen: [Onderwijshuisvesting, Leerplichthandhaving]
bedrijfsfuncties: [Onderwijsbeleid, Vastgoedbeheer]
---

## BO-criteria toetsing

6/6 criteria: heeft betekenis (ja), herkenbaar (ja), eigen bestaan (ja), meervoud (ja), levenscyclus (ja — school wordt gesticht, gehuisvest, gerenoveerd, opgeheven), relaties (ja — met leerlingen, inschrijvingen, gebouwen).

## Beschrijving

Een school is een instelling voor funderend onderwijs. De gemeente is verantwoordelijk voor de bekostiging van schoolgebouwen (nieuwbouw en renovatie), terwijl het schoolbestuur verantwoordelijk is voor het onderwijs en het onderhoud. De gemeente programmeert huisvestingsprojecten via het integraal huisvestingsplan (IHP) en voert herschikkingsgesprekken over de spreiding van scholen in de wijken. Scholen met minder dan 191 leerlingen (opheffingsnorm) zijn onderwerp van herschikking.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| PO-school | School voor primair onderwijs | — |
| VO-school | School voor voortgezet onderwijs | — |
| SO/SBO/VSO-school | School voor speciaal (basis/voortgezet) onderwijs | — |
| Buurtschool | Multifunctionele school met maatschappelijke partners in de wijk | — |
| Kindcentrum | Integrale voorziening onderwijs en kinderopvang 0-12 jaar | — |
| Multifunctionele accommodatie (MFA) | Gebouw waar meerdere maatschappelijke organisaties voorzieningen aanbieden; in gemeentelijk eigendom | — |

## GGM-bron

> "Gebouw in gebruik voor basis, middelbaar of hoger onderwijs." — GGM, entiteit School, beleidsdomein Onderwijs

- **Entiteit:** School
- **Beleidsdomein:** Onderwijs
- **Attributen:** naam
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving |
|---|---|---|---|---|
| [[Leerling]] | associatie | naar-dit-BO | 0..* | Leerling is ingeschreven bij school |
| [[Opleidingsinschrijving]] | associatie | van-dit-BO | 0..* | School heeft inschrijvingen |
| [[Verzuimmelding]] | associatie | van-dit-BO | 0..* | School meldt verzuim |
| [[Leerplichtvrijstelling]] | associatie | van-dit-BO | 0..* | Vrijstelling betreft school |
| [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/binnenlocatie\|Binnenlocatie]] | associatie | van-dit-BO | 0..* | School gebruikt gymzaal voor bewegingsonderwijs |

## Bedrijfsprocessen

- Onderwijshuisvesting — programmering en bekostiging schoolgebouwen
- Leerplichthandhaving — verzuimafhandeling en vrijstellingen

## Bedrijfsfuncties

- Onderwijsbeleid
- Vastgoedbeheer


## Subtypes

- **PO-school** — School voor primair onderwijs
- **VO-school** — School voor voortgezet onderwijs
- **SO/SBO/VSO-school** — School voor speciaal (basis/voortgezet) onderwijs
- **Buurtschool** — Multifunctionele school met maatschappelijke partners in de wijk
- **Kindcentrum** — Integrale voorziening onderwijs en kinderopvang 0-12 jaar
- **Multifunctionele accommodatie** — Gebouw waar meerdere (overwegend maatschappelijke) organisaties voorzieningen aanbieden

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/beleidsnota-onderwijshuisvesting-utrecht]]
- [[Wiki/Bronsamenvattingen/onderwijs/passend-onderwijs]]
- [[Wiki/Bronsamenvattingen/onderwijs/kindcentra]]
