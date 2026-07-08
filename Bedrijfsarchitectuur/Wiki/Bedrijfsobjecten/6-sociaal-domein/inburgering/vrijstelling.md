---
type: element
naam: Vrijstelling
onderwerp:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Vrijstelling
ggm_guid: EAID_C31D4A7E_1F25_4b85_B49C_AEC45EB3DB54
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
ggm_definitie: Een Vrijstelling is een formeel besluit waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt ontheven van specifieke onderdelen van de inburgeringsplicht, omdat deze reeds op andere wijze zijn behaald of niet van toepassing zijn, zoals bedoeld in artikel 7.2 van de Wet inburgering 2021.
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
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Vrijstelling** als directe tegenhanger.
bo_definitie: Formeel besluit waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt vrijgesteld van de inburgeringsplicht op grond van behaalde diploma's of certificaten.
bo_toelichting: Zes categorieën bewijsstukken geven recht op vrijstelling (Nederlandstalige opleidingen, buitenlandse equivalenten, Internationaal/Europees onderwijs). Gedeeltelijke vrijstelling is mogelijk per examenonderdeel op niveau B1 of A2. Aanvraag bij de Minister, beschikking binnen 8 weken, kosten €90.
bo_synoniemen: []
bo_homoniemen:
- bedrijfsobject: "[[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/vrijstelling|Vrijstelling (Leerplicht)]]"
  ggm_entiteit: Vrijstelling
  ggm_guid: EAID_B8584CD2_A54A_4a59_82B6_A597A0864CFA
  ggm_beleidsdomein: Leerplicht en Leerlingenvervoer
  toelichting: Vrijstelling van de leerplicht is een ander concept dan vrijstelling van de inburgeringsplicht
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|Inburgeringsplicht]]'
  richting: naar-dit-BO
  kardinaliteit: 0..*
  beschrijving: Inburgeringsplicht kan leiden tot vrijstelling(en)
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen|Examen]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Vrijstelling geldt voor specifiek examenonderdeel
bedrijfsprocessen:
- Beoordeling vrijstellingsaanvraag inburgering
bedrijfsfuncties:
- Inburgering
---

# Vrijstelling

Formeel besluit waarmee een inburgeringsplichtige geheel of gedeeltelijk wordt vrijgesteld van onderdelen van de inburgeringsplicht, op grond van eerder behaalde diploma's, getuigschriften of certificaten.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus (aanvraag → beoordeling → beschikking)
- ✅ Heeft relaties met andere concepten

Een inburgeringsplichtige kan meerdere gedeeltelijke vrijstellingen hebben (per examenonderdeel). De vrijstelling wijzigt de scope van de [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|Inburgeringsplicht]] en is daarom een zelfstandig besluitobject, niet slechts een status.

## GGM-bron

> Een Vrijstelling is een formeel besluit waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt ontheven van specifieke onderdelen van de inburgeringsplicht, omdat deze reeds op andere wijze zijn behaald of niet van toepassing zijn, zoals bedoeld in artikel 7.2 van de Wet inburgering 2021.

- **Entiteit:** Vrijstelling
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** EindoordeelVrijstelling, DatumVrijstelling
- **Matchsterkte:** exact

## Beschrijving

De Regeling inburgering 2021 onderscheidt twee vormen:

**Gehele vrijstelling** (art. 2.1): op grond van een inburgeringsdiploma, Nederlandstalig diploma (wo, hbo, vwo, havo, vmbo, mbo-2+), equivalent uit Aruba/Curaçao/Sint Maarten/Suriname/België, of diploma van erkende Internationale/Europese school met Nederlands op B1-niveau.

**Gedeeltelijke vrijstelling** (art. 3.12–3.13): per examenonderdeel op niveau B1 of A2, op grond van Staatsexamen NT2, certificaat voortgezet onderwijs, Certificaat Nederlands als Vreemde Taal, of buitenlands certificaat op B1-niveau. Beoordeling buitenlandse diploma's door Nuffic of SBB.

Tijdelijke vrijstelling (art. 2.2) geldt gedurende de inschrijving voor een opleiding die tot een vrijstellend diploma leidt.

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht\|Inburgeringsplicht]] | Inburgeringsplicht kan leiden tot vrijstelling(en) |
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen\|Examen]] | Gedeeltelijke vrijstelling geldt voor specifiek examenonderdeel |

## Bronnen

- [[Wiki/Bronsamenvattingen/Asiel en Integratie/regeling-inburgering-2021]]
