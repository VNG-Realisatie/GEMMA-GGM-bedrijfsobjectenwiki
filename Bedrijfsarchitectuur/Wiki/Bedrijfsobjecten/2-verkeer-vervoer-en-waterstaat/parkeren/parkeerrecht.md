---
type: element
naam: Parkeerrecht
onderwerp: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Parkeerrecht"
ggm_guid: EAID_9E0936E5_6B50_4205_BA5D_FEB80486D6F1
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Parkeerrecht"
ggm_gemma_guid: "ae658af8-46be-4d41-ba95-c5e24cec7598"
ggm_gemma_definitie: "Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-ae658af8-46be-4d41-ba95-c5e24cec7598"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Parkeerrecht** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Belprovider** (detail) — Te technisch/operationeel, geen herkenbaar bedrijfsobject
bo_definitie: "Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren."
bo_toelichting:
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Parkeerzone]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..1"
    beschrijving: Parkeerrecht geldt binnen een parkeerzone
  - type: associatie
    bedrijfsobject: "[[Voertuig]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..1"
    beschrijving: Parkeerrecht is gekoppeld aan een voertuig
  - type: associatie
    bedrijfsobject: "[[Parkeervergunning]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: Parkeerrecht kan voortkomen uit een parkeervergunning
---

# Parkeerrecht

Het recht om een voertuig te parkeren op een daartoe aangewezen plek, ontstaan door betaling of vergunning.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — juridische basis voor rechtmatig parkeren en handhaving
- ✅ Is herkenbaar voor domeinexperts — handhavers toetsen elk geparkeerd voertuig aan een parkeerrecht
- ✅ Heeft een eigen bestaan binnen het domein — zelfstandig recht met eigen geldigheid, zone en voertuig
- ✅ Kan in meervoud bestaan — dagtarief, uurtarief, P+R-tarief, vergunningsrecht
- ✅ Heeft een eigen levenscyclus — ontstaan (betaling/verlening), geldig, verlopen
- ✅ Heeft relaties met andere concepten — gekoppeld aan parkeerzone, voertuig en parkeervergunning

## Beschrijving

Een parkeerrecht is het recht om een voertuig te parkeren op een daartoe aangewezen plek, ontstaan door betaling van parkeerbelasting of via een vergunning. Het verbindt parkeerder, voertuig en zone. Bij handhaving wordt getoetst of een geldig parkeerrecht aanwezig is.

## GGM-bron

> "Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren." — GGM, Parkeerrecht (EAID_9E0936E5)

**Matchsterkte: exact.**

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerzone|Parkeerzone]] — parkeerrecht geldt binnen een parkeerzone
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig|Voertuig]] — parkeerrecht is gekoppeld aan een voertuig
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning|Parkeervergunning]] — parkeerrecht kan voortkomen uit een parkeervergunning

## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-fiets-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-auto-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/module-parkeernormen]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/rapportage-routekaart-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-fietsparkeren]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeren-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid]]
- [[Wiki/Bronsamenvattingen/mobiliteit/parkeervisie]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitvoeringsprogramma-betaald-parkeren]]
