---
type: bedrijfsobject
naam: Archiefstuk
domein: [Cultuur]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Archiefstuk"
ggm_guid: EAID_369E453B_4C3A_48dc_9619_C36232B339D9
ggm_uml_type: Class
ggm_beleidsdomein: "Archief"
ggm_taakveld: "Erfgoed"
ggm_diagram: [Archief Model, Archief Aanvragen, Archief Model Indeling, Generieke entiteiten Erfgoed]
ggm_diagram_ids: [EAID_59241C4B_FD65_484b_88E5_83189334A510, EAID_8D468696_4B9D_40b4_92F0_3BED39502098, EAID_691E6481_68AC_4754_88F0_60D2877D1549, EAID_B7192738_00E7_4b65_902A_B8292E79261B]
ggm_definitie: "Bijeengebrachte informatie, ongeacht het medium, die wordt gecreëerd, ontvangen en gearchiveerd door een bureau, een instelling, een organisatie of een individu met het oog op het nakomen van wettelijke verplichtingen of het uitvoeren van zakelijke transacties.(AAT)"
ggm_toelichting: ""
ggm_synoniemen: "Archiefbescheiden"
ggm_herkomst: ""
ggm_gemma_naam: "Archiefstuk"
ggm_gemma_guid: "7b7d7585-b081-4bcc-a39e-cf6b3803799a"
ggm_gemma_definitie: "Bijeengebrachte informatie, ongeacht het medium, die wordt gecreëerd, ontvangen en gearchiveerd door een bureau, een instelling, een organisatie of een individu met het oog op het nakomen van wettelijke verplichtingen of het uitvoeren van zakelijke transa"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: "Archiefbescheiden"
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-7b7d7585-b081-4bcc-a39e-cf6b3803799a"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "gelijk aan GGM"
bedrijfsprocessen: [Archiefvorming, Archiefbeheer, Openbaarheid en inzage]
bedrijfsfuncties: [Informatiebeheer, Erfgoedbeheer]
relaties:
  - type: generalisatie
    bedrijfsobject: "*(Erfgoed Object — abstract)*"
    richting: "van-dit-BO"
    kardinaliteit: 
    beschrijving: Archiefstuk is een specialisatie van Erfgoed Object
  - type: associatie
    bedrijfsobject: "*(Archief)*"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een archiefstuk is onderdeel van een archief
---

# Archiefstuk

Gearchiveerde informatie die door de gemeente of haar voorgangers is gecreëerd, ontvangen of gearchiveerd in het kader van wettelijke verplichtingen of zakelijke transacties. Het gemeentearchief beheert archiefstukken conform de Archiefwet.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernobject in archiefbeheer |
| Herkenbaar voor experts | ✅ | Archivaris, informatiespecialist kennen dit |
| Eigen bestaan | ✅ | Een archiefstuk bestaat onafhankelijk |
| Meervoud | ✅ | Gemeentearchieven bevatten duizenden tot miljoenen stukken |
| Eigen levenscyclus | ✅ | Creatie → opname → bewaring → overdracht/vernietiging |
| Relaties | ✅ | Met Archief, Vindplaats, Periode, Ordeningsschema |

## GGM-bron

> **Archiefstuk**: Bijeengebrachte informatie, ongeacht het medium, die wordt gecreëerd, ontvangen en gearchiveerd door een bureau, een instelling, een organisatie of een individu met het oog op het nakomen van wettelijke verplichtingen of het uitvoeren van zakelijke transacties.(AAT)
> — *GGM v2.5.1, Archief (taakveld 5 Sport, Cultuur en Recreatie)*

**Entiteit:** Archiefstuk
**Attributen:** trefwoorden, openbaarheidsbeperking, inventarisnummer, omvang, beschrijving, uiterlijkeVorm
**Synoniemen:** Archiefbescheiden
**Matchsterkte:** exact

In het GGM erft Archiefstuk van zowel **Document** (abstract) als **Erfgoed Object** (abstract). Het is daarmee tegelijk een informatieobject en een erfgoedobject.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Onderdeel van archief | *(Archief)* | Archiefstuk → Archief [0..*..1] | Container, geen apart BO |
| Heeft digitaal bestand | *(DigitaalBestand)* | Archiefstuk → DigitaalBestand [1..0..*] | Technisch, geen apart BO |
| Stamt uit periode | *(Periode)* | Archiefstuk → Periode [0..*..1..*] | Classificatie |
| Heeft vindplaats | *(Vindplaats)* | Archiefstuk → Vindplaats [0..*..1] | Fysieke locatie in archief (depot/kast/plank) |
| Heeft ordeningsschema | *(Ordeningsschema)* | Archiefstuk → Ordeningsschema [0..*..0..*] | Classificatie |
| Specialisatie van | *(Erfgoed Object)* | Generalisatie | Abstract parent |
| Aangevraagd via | *(Aanvraag)* | Aanvraag → Archiefstuk [0..*..0..*] | Inzageverzoek |

## Bedrijfsprocessen

- **Archiefvorming**: selectie en opname van documenten in het archief
- **Archiefbeheer**: ordening, bewaring, conservering
- **Openbaarheid en inzage**: behandelen van inzageverzoeken, openbaarheidsbeperking

## Bedrijfsfuncties

- Informatiebeheer
- Erfgoedbeheer
