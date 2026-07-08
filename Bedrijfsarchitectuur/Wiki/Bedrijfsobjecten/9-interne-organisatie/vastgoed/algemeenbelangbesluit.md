---
type: element
naam: Algemeenbelangbesluit
onderwerp: [Vastgoed]
archimate_type: contract
grondslag: governance-object

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
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

bo_definitie: "Raadsbesluit op grond van de Wet markt en overheid dat voor aangewezen economische activiteiten verhuur onder de kostprijs mogelijk maakt."
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Vastgoedcontract]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een algemeenbelangbesluit maakt verhuur onder de kostprijs mogelijk voor specifieke contracten"
  - type: associatie
    bedrijfsobject: "[[Vastgoedobject]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Het besluit wijst vastgoedobjecten of gebruiksfuncties aan"
bedrijfsprocessen: [huurprijsbepaling, verhuur gemeentelijk vastgoed]
bedrijfsfuncties: [vastgoedexploitatie, vastgoedbeleid]
---

## BO-criteria toetsing

1. **Heeft betekenis** — juridisch instrument dat de huurprijssystematiek verankert in de Wet markt en overheid
2. **Herkenbaar** — elke gemeente die vastgoed onder de kostprijs verhuurt moet een algemeenbelangbesluit nemen
3. **Eigen bestaan** — het besluit is een zelfstandig raadsbesluit, los van individuele huurcontracten
4. **Meervoud** — meerdere besluiten mogelijk (per gebruiksfunctie, per situatie); ook herzieningen
5. **Levenscyclus** — ontwerp → vaststelling door raad → geldig → herzien/ingetrokken
6. **Relaties** — naar [[Vastgoedcontract]], [[Vastgoedobject]], gebruiksfuncties

## Beschrijving

Een algemeenbelangbesluit is een raadsbesluit op grond van artikel 25h, vijfde lid, van de Mededingingswet (Wet markt en overheid). Het wijst economische activiteiten aan waarvoor de gemeente onder de kostprijs mag verhuren, omdat het algemeen belang zwaarder weegt dan het belang van private verhuurders. Zonder dit besluit is de gemeente verplicht minimaal kostprijsdekkend te verhuren.

Het besluit vereist een marktverkenning en motivering waaruit blijkt dat de markt niet wordt verstoord. Het kan betrekking hebben op categorieën (gebruiksfuncties) of individuele panden. Het besluit is dynamisch en wordt periodiek herzien.

> "Het college heeft bij het besluit over de huurprijssystematiek de wens geformuleerd om het maatschappelijk vastgoed zoveel mogelijk onder een algemeenbelangbesluit te scharen." (bron: Vastgoedstrategie Amsterdam)

> "Een verhuring onder de kostprijs kan alleen bij uitzondering plaatsvinden indien geen marktverstoring plaatsvindt of als er rechtvaardiging bestaat voor marktverstoring vanwege het algemeen belang." (bron: Vastgoedstrategie Amsterdam)

## Juridische bron

Artikel 25h, vijfde lid, Mededingingswet (Wet markt en overheid). De wet verplicht overheden bij economische activiteiten de integrale kosten door te berekenen, tenzij een algemeenbelangbesluit is genomen. Zie [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam|Vastgoedstrategie Amsterdam]] §5.2 voor de uitwerking.

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] | van-dit-BO | 0..* | Maakt verhuur onder kostprijs mogelijk | bronnen |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | van-dit-BO | 0..* | Wijst vastgoedobjecten of functies aan | bronnen |

## Bedrijfsprocessen

- Huurprijsbepaling bij nieuwe verhuringen
- Vaststelling en herziening van het algemeenbelangbesluit
- Marktverkenning voor onderbouwing

## Bronnen

- [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam]]
