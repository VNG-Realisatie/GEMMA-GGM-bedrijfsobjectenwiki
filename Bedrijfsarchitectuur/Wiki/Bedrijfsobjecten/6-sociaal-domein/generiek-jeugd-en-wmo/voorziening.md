---
type: bedrijfsobject
naam: Voorziening
domein: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Voorziening
ggm_guid: EAID_EAAF2F59_6BC0_4243_B126_A8E604B32C5E
ggm_uml_type: Class
ggm_beleidsdomein: "Generiek Jeugd en Wmo"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: ["Sociaal Domein Beschikking en Voorziening: Domain Objects"]
ggm_diagram_ids: [EAID_5AE29494_3572_4924_B2B8_3206E55D71BB]
ggm_definitie: "Middel om services/maatregelen in te vullen."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: GGM

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

ggm_duplicaat_entiteiten:
  - "EAID_8D3666E3_F2DA_4cba_BF67_EFED9AAD97CC"

bo_definitie: "Middel waarmee de gemeente ondersteuning levert aan een cliënt onder de Wmo of Jeugdwet, variërend van hulpmiddelen tot intensieve jeugdhulp."
bo_toelichting: ''
bo_subtypes:
  - naam: Maatwerkvoorziening Wmo
    omschrijving: "Op de persoon afgestemde voorziening na individuele beoordeling (Wmo 2015)"
    ggm_entiteit: Voorzieningsoort
    ggm_attribuut: productcategorie
  - naam: Jeugdhulpvoorziening
    omschrijving: "Hulp aan jeugdigen of ouders bij opgroei- en opvoedproblemen (Jeugdwet)"
    ggm_entiteit: Voorzieningsoort
    ggm_attribuut: productcategorie
  - naam: Algemene voorziening
    omschrijving: "Toegankelijk aanbod zonder beschikking (bijv. informatie, advies)"
    ggm_entiteit: Voorzieningsoort
    ggm_attribuut: productcategorie
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "toegekend via beschikking (via Beschikte Voorziening)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing|Toewijzing]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "toegewezen aan zorgaanbieder (via Beschikte Voorziening)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering|Levering]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "geleverd als prestatie"
bedrijfsprocessen: [voorziening toekennen, voorziening leveren, voorziening evalueren]
bedrijfsfuncties: [voorzieningenbeheer, contractbeheer]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Kernbegrip in Wmo 2015 en Jeugdwet; gemeenten kennen voorzieningen toe |
| Besproken op bestuurlijk niveau | ✅ | Voorzieningenoverzichten in programmabegroting en beleidsnota's |
| Vastgelegd in systemen | ✅ | Productcatalogus en registratie in suite voor sociaal domein |
| Eigen attributen | ✅ | productcode, naam, omschrijving, wet, code, afhandelwijze |
| Relaties met andere objecten | ✅ | Beschikking, Toewijzing, Levering, Tarief |
| Levenscyclus | ✅ | Ingericht in productcatalogus, toegekend, geleverd, beëindigd |

## Beschrijving

Een voorziening is het middel waarmee de gemeente ondersteuning levert aan een cliënt. Onder de Wmo 2015 kan dit een maatwerkvoorziening zijn (huishoudelijke hulp, begeleiding, dagbesteding, beschermd wonen) of een algemene voorziening (vrij toegankelijk, zonder beschikking). Onder de Jeugdwet betreft het jeugdhulpvormen variërend van ambulante begeleiding tot specialistische GGZ of gesloten jeugdzorg. De voorziening wordt gespecificeerd in de beschikking en via toewijzing aan een zorgaanbieder doorgezet.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Maatwerkvoorziening Wmo | Op de persoon afgestemde voorziening na individuele beoordeling (Wmo 2015) | Voorzieningsoort (productcategorie) |
| Jeugdhulpvoorziening | Hulp aan jeugdigen of ouders bij opgroei- en opvoedproblemen (Jeugdwet) | Voorzieningsoort (productcategorie) |
| Algemene voorziening | Toegankelijk aanbod zonder beschikking (bijv. informatie, advies) | Voorzieningsoort (productcategorie) |

## GGM-bron

> "Middel om services/maatregelen in te vullen." — GGM Generiek Jeugd en Wmo

- **Entiteit:** Voorziening
- **Beleidsdomein:** Generiek Jeugd en Wmo
- **Attributen:** productcode, naam, omschrijving, wet, code, afhandelwijze
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | ← | 0..* | toegekend via beschikking (via Beschikte Voorziening) | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] | → | 0..1 | toegewezen aan zorgaanbieder (via Beschikte Voorziening) | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering\|Levering]] | ← | 0..* | geleverd als prestatie | GGM |

## Bedrijfsprocessen

- Voorziening toekennen
- Voorziening leveren
- Voorziening evalueren

## Bedrijfsfuncties

- Voorzieningenbeheer
- Contractbeheer


## Subtypes

- **Maatwerkvoorziening Wmo** — Op de persoon afgestemde voorziening na individuele beoordeling (Wmo 2015)
- **Jeugdhulpvoorziening** — Hulp aan jeugdigen of ouders bij opgroei- en opvoedproblemen (Jeugdwet)
- **Algemene voorziening** — Toegankelijk aanbod zonder beschikking (bijv. informatie, advies)

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/maatwerkvoorzieningen-wmo]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsregels-jeugdhulp-oost-gelre]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beschermd-thuis]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/vrijwilligerswerk-en-mantelzorgondersteuning]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015]]
