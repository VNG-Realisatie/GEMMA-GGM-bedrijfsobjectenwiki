---
type: bedrijfsobject
naam: Urgentverklaring
domein: [Wonen]
archimate_type: business-object
grondslag: governance-object

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein: Bouwen en Wonen
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram:
ggm_diagram_ids:
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

gemma_definitie: "Een beschikking waarmee een woningzoekende voorrang krijgt bij de toewijzing van een sociale huurwoning op grond van urgente omstandigheden."
gemma_subtypes:
  - naam: Medische urgentie
    omschrijving: "Urgentie op medische gronden"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Herhuisvestingsurgentie
    omschrijving: "Urgentie bij sloop, renovatie of groot onderhoud"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Mantelzorgurgentie
    omschrijving: "Urgentie voor het verlenen of ontvangen van mantelzorg"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Urgentie dreigend dakloos
    omschrijving: "Urgentie bij dreigende dakloosheid"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Financiële urgentie
    omschrijving: "Urgentie bij financiële problemen die de woonsituatie bedreigen"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Relationele urgentie
    omschrijving: "Urgentie bij relatiebeëindiging"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Statushouderurgentie
    omschrijving: "Urgentie voor vergunninghouders met taakstelling"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bronnen: [Wiki/Bronsamenvattingen/Wonen/huisvestingsverordening-utrecht]
relaties:
  - type: associatie
    bedrijfsobject: "[[Woning]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een urgentverklaring geeft voorrang bij toewijzing van een woning"
bedrijfsprocessen: [Woonruimteverdeling, Urgentieverlening]
bedrijfsfuncties: [Volkshuisvesting, Woonbeleid]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal instrument in woonruimteverdeling |
| Herkenbaar voor domeinexperts | ✅ Gedefinieerd in Huisvestingsverordening |
| Heeft een eigen bestaan | ✅ Individuele beschikking per woningzoekende |
| Kan in meervoud bestaan | ✅ Toenemend aantal per jaar |
| Heeft een eigen levenscyclus | ✅ Aangevraagd → beoordeeld → verleend/geweigerd → benut/verlopen |
| Heeft relaties met andere concepten | ✅ Woning, woningzoekende, woningcorporatie |

Score: **6/6** — BO.

## Beschrijving

Een urgentverklaring is een beschikking van de gemeente waarmee een woningzoekende voorrang krijgt bij de toewijzing van een sociale huurwoning. De Huisvestingsverordening Utrecht definieert negen urgentiecategorieën: dreigende dakloosheid, relatiebeëindiging, financiële problemen, medische gronden, mantelzorg, volkshuisvestelijke gronden, maatschappelijke gronden, statushouders en aanbodsysteemgedupeerden.

Het aantal urgenties neemt toe en zal naar verwachting verder stijgen door de aanwijzing van verplichte urgentiecategorieën in het wetsvoorstel Versterking regie volkshuisvesting. De beleidsnota stelt dat de toenemende vraag naar urgentieverklaringen de slagingskans voor reguliere woningzoekenden verkleint — een blijvend verdeeldilemma.

## Specialisaties

| Subtype | Omschrijving |
|---|---|
| Medische urgentie | Op medische gronden |
| Herhuisvestingsurgentie | Bij sloop, renovatie of groot onderhoud |
| Mantelzorgurgentie | Voor verlenen of ontvangen mantelzorg |
| Urgentie dreigend dakloos | Bij dreigende dakloosheid |
| Financiële urgentie | Bij financiële problemen die woonsituatie bedreigen |
| Relationele urgentie | Bij relatiebeëindiging |
| Statushouderurgentie | Voor vergunninghouders met taakstelling |

## Juridische bron

De urgentverklaring is gedefinieerd in de Huisvestingsverordening gemeente Utrecht (geldend vanaf 11 juli 2024). De nadere regel specificeert urgentie op volkshuisvestelijke gronden (stadsurgentie, regio-urgentie, terugkeervoorrang).

> "Urgentverklaringen zijn mogelijk bij dreigende dakloosheid, relatiebeëindiging, financiële problemen, medische gronden, mantelzorg, volkshuisvestelijke gronden, maatschappelijke gronden, statushouders en aanbodsysteemgedupeerden." — [[Wiki/Bronsamenvattingen/Wonen/huisvestingsverordening-utrecht|Huisvestingsverordening gemeente Utrecht]]

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Geeft voorrang bij toewijzing van [[Woning]] | van Urgentverklaring | 0..* | Huisvestingsverordening |

## Bedrijfsprocessen

- **Urgentieverlening** — Beoordeling en verlening van urgentverklaringen
- **Woonruimteverdeling** — Urgentverklaringen beïnvloeden de rangorde in het aanbodmodel

## Terugmelding GGM

> **Urgentverklaring** — Ontbreekt in het GGM. Een urgentverklaring is een beschikking met eigen levenscyclus (aangevraagd, verleend, benut, verlopen), categorieën en relatie tot woningzoekende en woning. Zou passen in beleidsdomein Bouwen en Wonen als nieuw objecttype, gerelateerd aan Gebouw.
