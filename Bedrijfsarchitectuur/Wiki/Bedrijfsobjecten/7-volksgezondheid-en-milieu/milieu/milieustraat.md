---
type: element
naam: Milieustraat
domein: [Milieu]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Milieustraat"
ggm_guid: EAID_1638F2AF_F1E8_4360_BA47_D975F2135168
ggm_uml_type: Class
ggm_beleidsdomein: "Afval"
ggm_taakveld: "7 Volksgezondheid en Milieu"
ggm_diagram: [Diagram Afval Milieustraat]
ggm_diagram_ids: [EAID_A00B8121_71AC_466f_B391_E16881240477]
ggm_definitie: "Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Milieustraat"
ggm_gemma_guid: "0310645e-6873-4cb3-93ec-734f0ac3323e"
ggm_gemma_definitie: "Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-0310645e-6873-4cb3-93ec-734f0ac3323e"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Milieustraat** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Pas** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil."
bo_toelichting: ''
bo_via_kandidaten:
  - ggm_entiteit: "Storting"
    ggm_guid: "EAID_15910FE7_D323_45ff_AA7F_CE3C636CE953"
    reden: "Het zich ontdoen van stoffen (storten) gebeurt bij de milieustraat."
bedrijfsprocessen: [Afvalscheiding, Grofvuilinzameling, Bezoekersregistratie]
bedrijfsfuncties: [Afvalbeheer]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: inzamelpunt van fracties
  - type: associatie
    bedrijfsobject: "[[Upcyclecentrum]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: nabijgelegen upcyclecentrum
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Kernvoorziening voor gescheiden afvalinzameling |
| Herkenbaar voor domeinexperts | ✅ Elke gemeente beheert een of meer milieustraten |
| Heeft eigen bestaan | ✅ Fysieke locatie met eigen adres en infrastructuur |
| Kan in meervoud bestaan | ✅ Utrecht heeft er drie; elke gemeente heeft er minstens een |
| Heeft eigen levenscyclus | ✅ Opening → exploitatie → herinrichting → eventueel sluiting |
| Heeft relaties met andere concepten | ✅ Fracties, stortingen, toegangspassen, upcyclecentra |

**6/6 criteria van toepassing.**

## Beschrijving

Een milieustraat is een fysieke voorziening die de gemeente exploiteert waar inwoners gescheiden huishoudelijk afval en grofvuil kunnen aanbieden. Utrecht heeft drie milieustraten: Tractieweg, Lunetten (Het Zwarte Woud) en een derde locatie. In Utrecht ook bekend als "afvalscheidingsstation". Het aantal bezoekers steeg met 20% van 475.000 (2015) naar 567.000 (2019). Op een milieustraat worden tot 22 verschillende afvalsoorten geaccepteerd. Er wordt onderzocht of ook bedrijfsafval geaccepteerd kan worden. Milieustraten worden steeds vaker gekoppeld aan upcyclecentra voor hergebruik.

> "Het aantal bezoekers aan de afvalscheidingsstations is gestegen van 475.000 in 2015 naar 567.000 in 2019." (bron: [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020|Grondstoffennota 2020]])

## GGM-bron

> **Milieustraat**: Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil.
> — *GGM, Afval (taakveld 7 Volksgezondheid en Milieu)*

**Entiteit:** Milieustraat
**Matchsterkte:** exact — zelfde concept, compatibele definitie. Het GGM modelleert ook gerelateerde entiteiten Pas (toegangspas) en Storting (stortactiviteit) die aan Milieustraat zijn gekoppeld.

## Relaties

- **[[Grondstofstroom]]** — een milieustraat is inzamelpunt voor meerdere grondstofstromen (fracties)
- **[[Upcyclecentrum]]** — nabijgelegen upcyclecentrum voor hergebruik van nog bruikbare materialen
- **Pas** — GGM-entiteit (geen BO); toegangspas voor bezoekersregistratie
- **Storting** — GGM-entiteit (geen BO); registratie van een individuele aanbieding

## Bedrijfsprocessen

- **Afvalscheiding** — gescheiden inzameling van afvalstromen op de milieustraat
- **Grofvuilinzameling** — acceptatie van grof huishoudelijk afval
- **Bezoekersregistratie** — registratie van bezoekers via toegangspas

## Bedrijfsfuncties

- Afvalbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020]]
