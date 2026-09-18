---
type: element
naam: Ontheffing
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Ontheffing
ggm_guid: EAID_8EE515EA_11F9_4f56_B9AA_F7B0904B39E7
ggm_uml_type: Class
ggm_beleidsdomein: Werk
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Detaildiagram Werk]
ggm_diagram_ids: [EAID_F93A23D7_BF68_46e0_A6D4_96508ACED81E]
ggm_definitie: "Een formele vrijstelling van verplichtingen rond arbeidsparticipatie, zoals beschikbaarheid of tegenprestatie, op basis van persoonlijke of juridische gronden."
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
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Ontheffing** als directe tegenhanger.
bo_definitie: "Een formele vrijstelling van verplichtingen rond arbeidsparticipatie, zoals beschikbaarheid of tegenprestatie, op basis van persoonlijke of juridische gronden."
bo_toelichting: "Grondslag: art. 9, tweede lid, Participatiewet (ontheffing bij dringende redenen, waaronder zorgtaken, van de arbeids- of tegenprestatieverplichting) en art. 9a (aparte, eenmalige ontheffing voor de alleenstaande ouder met een kind tot vijf jaar, geldig tot het kind de leeftijd van vijf jaar bereikt of ten hoogste vijf jaar, met heronderzoek door het college elke zes maanden)."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen:
- bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/ontheffing|Ontheffing (Inburgering)]]"
  ggm_entiteit: Ontheffing
  ggm_guid: EAID_3F5932BD_C721_402d_8154_74A1CE097825
  ggm_beleidsdomein: Inburgering
  toelichting: Ontheffing van de inburgeringsplicht (Wi2021) is een ander concept dan ontheffing van arbeidsverplichtingen (Participatiewet)
element_tegenhangers: []
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende|Werkzoekende]]"
  richting: naar-dit-BO
  kardinaliteit: "0..1"
  beschrijving: Een werkzoekende heeft op enig moment ten hoogste één (actieve) ontheffing van arbeidsverplichtingen
bedrijfsprocessen: [beoordeling ontheffingsaanvraag, herziening ontheffing]
bedrijfsfuncties: [arbeidsparticipatie, re-integratie]
---

# Ontheffing

Formele vrijstelling van verplichtingen rond arbeidsparticipatie (zoals beschikbaarheid voor werk of tegenprestatie), verleend aan een werkzoekende op persoonlijke of juridische gronden.

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Herkenbaar besluit binnen de Participatiewet-uitvoering |
| Herkenbaar voor domeinexperts | ✅ Klantmanagers Werk en Inkomen kennen ontheffing van arbeidsverplichtingen |
| Eigen bestaan | ✅ Eigen aanvraag, besluit en motivatie, los van het werkprofiel van de werkzoekende |
| Meervoud | ✅ Meerdere werkzoekenden kunnen een ontheffing hebben; een werkzoekende kan na afloop opnieuw een ontheffing aanvragen |
| Levenscyclus | ✅ Aanvraag → beoordeling → besluit → (periodieke) herziening → einddatum |
| Relaties | ✅ Relatie met Werkzoekende |

Score: **6/6**

## Beschrijving

Een werkzoekende die valt onder de Participatiewet heeft in beginsel arbeidsverplichtingen, zoals beschikbaarheid voor werk of het verrichten van een tegenprestatie. Een ontheffing stelt een werkzoekende geheel of gedeeltelijk vrij van deze verplichtingen, op basis van een aanvraag met een reden (`RedenAanvraag`), een besluit met motivatie, een geldigheidsperiode (ingangs- en einddatum) en een mogelijke latere herziening.

## Naamkeuze

De naam "Ontheffing" is een homoniem — dezelfde naam wordt in GGM-beleidsdomein Inburgering gebruikt voor een ander concept. Dit BO blijft **Ontheffing** heten; disambiguatie gebeurt via de domeinmap (`werk/` vs. `inburgering/`), niet via een afwijkende BO-naam, analoog aan hoe de Inburgering-tegenhanger dit al deed. In verwijzingen vanuit andere domeinen wordt de kwalificatie "(Werk)" als linktekst gebruikt.

**Verschil met [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/ontheffing|Ontheffing]] (Inburgering):**
- **Ontheffing (Werk):** vrijstelling van arbeidsverplichtingen (beschikbaarheid, tegenprestatie) onder de Participatiewet. Relatie: Werkzoekende.
- **Ontheffing (Inburgering):** vrijstelling van onderdelen van de inburgeringsplicht (Wi2021) op medische of bijzondere individuele gronden. Relatie: Inburgeringsplicht, Examen.

## GGM-bron

> Een formele vrijstelling van verplichtingen rond arbeidsparticipatie, zoals beschikbaarheid of tegenprestatie, op basis van persoonlijke of juridische gronden.

- **Entiteit:** Ontheffing
- **Beleidsdomein:** Werk (taakveld 6 — Sociaal Domein)
- **Attributen:** RedenAanvraag, AanvraagdatumOntheffing, Ontheffingsbesluit, MotivatieOntheffingsbesluit, SoortOntheffing, IngangsdatumOntheffing, EinddatumOntheffing, ResultaatInstrumentbeoordeling, OntheffenVerplichtingen, VersieNummerAanvraag, BijlagenBijAanvraag, BijlagenBijOntheffingsbesluit, HerzieningsdatumOntheffing, MotivatieHerzieningsbesluit, BijlagenBijHerzieningsbesluit
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Een werkzoekende heeft op enig moment ten hoogste één (actieve) ontheffing |

## Bronnen

De GGM-definitie (matchsterkte exact) is inhoudelijk bevestigd door de wettelijke grondslag:

> 2 Indien daarvoor dringende redenen aanwezig zijn, kan het college in individuele gevallen tijdelijk ontheffing verlenen van een verplichting als bedoeld in het eerste lid, onderdelen a en c. Zorgtaken kunnen als dringende redenen worden aangemerkt, voorzover hiermee geen rekening kan worden gehouden door middel van een voorziening als bedoeld in artikel 7, eerste lid, onderdeel a.
> (bron: `Sources/Onderwerpen/Werk en Inkomen/participatiewet-bwbr0015703.md`, art. 9 lid 2)

> 1 Onverminderd artikel 9, tweede lid, verleent het college aan een alleenstaande ouder die de volledige zorg heeft voor een tot zijn last komend kind tot vijf jaar op diens verzoek ontheffing van de verplichting, bedoeld in artikel 9, eerste lid, onderdeel a.
> (bron: `Sources/Onderwerpen/Werk en Inkomen/participatiewet-bwbr0015703.md`, art. 9a lid 1)

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]

## Terugmelding GGM

Onderdeel van het bredere hiaat "GGM mist generiek Ontheffing-concept" ([[Wiki/Analyses/ggm-terugmeldingen|#44]], [[Wiki/Analyses/ggm-terugmeldingen|#50]]) en nu expliciet als homoniem gemeld ([[Wiki/Analyses/ggm-terugmeldingen|#94]]) t.o.v. Ontheffing (Inburgering).
