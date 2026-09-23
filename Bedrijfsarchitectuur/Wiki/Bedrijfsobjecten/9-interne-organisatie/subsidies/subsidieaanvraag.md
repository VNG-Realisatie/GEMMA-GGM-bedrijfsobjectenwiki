---
type: element
naam: Subsidieaanvraag
onderwerp: [recht]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Subsidieaanvraag
ggm_guid: EAID_26C0D33A_B15A_4256_A5BF_5382A4E03539
ggm_uml_type: Class
ggm_beleidsdomein: Subsidies
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Subsidies]
ggm_diagram_ids: [EAID_F408BDED_51D4_4204_9B95_F0C6C2474DC3]
ggm_definitie: "Aanvraag voor een subsidie"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Subsidieaanvraag
ggm_gemma_guid: "4e5cd8a8-0110-4038-9b91-1f0562401398"
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-4e5cd8a8-0110-4038-9b91-1f0562401398"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Subsidieaanvraag** als directe tegenhanger.
bo_definitie: "Aanvraag van een (rechts)persoon voor een subsidie."
bo_toelichting: "Subsidieaanvragen moeten schriftelijk worden ingediend; digitale indiening is mogelijk als de gemeente dit faciliteert."
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidie|Subsidie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "aanvraag die kan leiden tot een subsidie"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidiebeschikking|Subsidiebeschikking]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "wordt beoordeeld en resulteert in een beschikking"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Startpunt van elk subsidieproces |
| Is herkenbaar voor domeinexperts | ✅ Herkenbaar document/verzoek voor aanvragers en behandelaars |
| Heeft een eigen bestaan | ✅ Bestaat als apart stuk, los van de subsidie die er (eventueel) uit voortkomt |
| Kan in meervoud bestaan | ✅ Per subsidieregeling en per aanvrager kunnen meerdere aanvragen bestaan |
| Heeft een eigen levenscyclus | ✅ Indiening → ontvangstbevestiging → beoordeling → resulteert in een beschikking |
| Heeft relaties met andere concepten | ✅ Met Subsidie en Subsidiebeschikking |

Score: 6/6

## Beschrijving

De subsidieaanvraag is het schriftelijke verzoek waarmee een (rechts)persoon een subsidie aanvraagt bij de gemeente. Volgens de Model Algemene subsidieverordening (ASV) moet een aanvraag schriftelijk worden ingediend, waarbij digitale indiening mogelijk is als de gemeente dit faciliteert. Het college kan in subsidieregels standaardberekeningswijzen vastleggen, bijvoorbeeld voor uurtarieven; aanvragers moeten zich daaraan houden, en niet-naleving kan leiden tot afwijzing van een incomplete aanvraag.

De aanvraag wordt beoordeeld door de gemeente en leidt tot een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidiebeschikking|Subsidiebeschikking]]: het besluit dat de subsidie toekent of afwijst.

## GGM-bron

> "Aanvraag voor een subsidie."
> — GGM, entiteit *Subsidieaanvraag*, beleidsdomein Subsidies (taakveld 9 Interne Organisatie)

**Matchsterkte:** exact — de GGM-entiteit dekt precies het in de bron beschreven aanvraagproces.

**Attributen (GGM):** datumIndiening, aangevraagdBedrag, ontvangstbevestiging, verwachteBeschikking, kenmerk.

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidie\|Subsidie]] | aanvraag die kan leiden tot een subsidie | Subsidieaanvraag → Subsidie | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidiebeschikking\|Subsidiebeschikking]] | wordt beoordeeld en resulteert in | Subsidieaanvraag → Subsidiebeschikking | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Recht/subsidierecht]]
