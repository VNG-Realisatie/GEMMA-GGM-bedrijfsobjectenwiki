---
type: bedrijfsobject
naam: Inburgeringstraject
domein:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Inburgeringstraject
ggm_guid: EAID_F9B2A863_63C8_4229_906A_D0891BB4F021
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
ggm_definitie: Een Inburgeringstraject in de context van inburgering bij gemeenten is een persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen
  van de samenleving, en het ontwikkelen van vaardigheden om zelfstandig te participeren in de Nederlandse maatschappij. Het traject omvat doorgaans onderdelen zoals taallessen (NT2), kennis van de Nederlandse
  maatschappij (KNM), en participatieactiviteiten, zoals vrijwilligerswerk of een werkstage. Het inburgeringstraject wordt afgestemd op de behoeften, achtergrond en mogelijkheden van de nieuwkomer en heeft
  als doel hen te begeleiden naar maatschappelijke zelfredzaamheid en een actieve rol in de samenleving.
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: Inburgeringstraject
ggm_gemma_guid: e1620918-61a7-4cef-b0e2-6b8e206608c8
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-e1620918-61a7-4cef-b0e2-6b8e206608c8
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Inburgeringstraject** als directe tegenhanger.
bo_definitie: "Een Inburgeringstraject in de context van inburgering bij gemeenten is een persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving, en het ontwikkelen van vaardigheden om zelfstandig te participeren in de Nederlandse maatschappij."
bo_toelichting: "Het traject omvat doorgaans onderdelen zoals taallessen (NT2), kennis van de Nederlandse maatschappij (KNM), en participatieactiviteiten, zoals vrijwilligerswerk of een werkstage. Het inburgeringstraject wordt afgestemd op de behoeften, achtergrond en mogelijkheden van de nieuwkomer en heeft als doel hen te begeleiden naar maatschappelijke zelfredzaamheid en een actieve rol in de samenleving."
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|PIP]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Wordt aangestuurd door het PIP
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|Leerroute]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Bevat een leerroute
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen|Examen]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: Wordt afgesloten met examens
---

# Inburgeringstraject

Persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving en het ontwikkelen van vaardigheden voor zelfstandige participatie.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Een Inburgeringstraject in de context van inburgering bij gemeenten is een persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving, en het ontwikkelen van vaardigheden om zelfstandig te participeren in de Nederlandse maatschappij. Het traject omvat doorgaans onderdelen zoals taallessen (NT2), kennis van de Nederlandse maatschappij (KNM), en participatieactiviteiten, zoals vrijwilligerswerk of een werkstage. Het inburgeringstraject wordt afgestemd op de behoeften, achtergrond en mogelijkheden van de nieuwkomer en heeft als doel hen te begeleiden naar maatschappelijke zelfredzaamheid en een actieve rol in de samenleving.

- **Entiteit:** Inburgeringstraject
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** UitkomstLeerbaarheidstoets
- **Matchsterkte:** exact

## Relaties

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|pip]] — wordt aangestuurd door het PIP [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|leerroute]] — bevat een leerroute [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen|examen]] — wordt afgesloten met examens [0..*]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
