---
type: bedrijfsobject
naam: Grondstofstroom
domein: [Milieu]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Fractie"
ggm_guid: EAID_80A7D18F_7C7E_4ee6_9F07_055559BCEF9F
ggm_uml_type: Class
ggm_beleidsdomein: "Afval"
ggm_taakveld: "7 Volksgezondheid en Milieu"
ggm_diagram: [Diagram Afval Ophalen, Diagram Afval Milieustraat, Diagram Afval Meldingen]
ggm_diagram_ids: [EAID_D98AA96C_2EB0_4b46_9E9C_09D55E02FE38, EAID_A00B8121_71AC_466f_B391_E16881240477, EAID_157F610A_619E_4d1a_BB45_5C1F55178944]
ggm_definitie: "Onderdeel, deeltje"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Fractie"
ggm_gemma_guid: "5b29c1f2-feeb-4e72-9b70-7a0a8bb374cc"
ggm_gemma_definitie: "Onderdeel, deeltje"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-5b29c1f2-feeb-4e72-9b70-7a0a8bb374cc"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
bo_definitie: "Afzonderlijke afval- of grondstofstroom met eigen inzamel- en verwerkingsstrategie."
bo_toelichting: ''
bedrijfsprocessen: [Afvalinzameling, Afvalverwerking, Grondstofscheiding, Kwaliteitsmonitoring]
bedrijfsfuncties: [Afvalbeheer]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Container]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: ingezameld via containers
  - type: associatie
    bedrijfsobject: "[[Milieustraat]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: inzamelpunt op milieustraat
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Elke stroom heeft eigen beleid en doelstellingen |
| Herkenbaar voor domeinexperts | ✅ GFT, papier, glas zijn standaardbegrippen |
| Heeft eigen bestaan | ✅ Elke grondstofstroom is een zelfstandig beheerobject |
| Kan in meervoud bestaan | ✅ GFT, PBP, papier/karton, glas, textiel, luiers, grof afval |
| Heeft eigen levenscyclus | ✅ Inzameling → verwerking → hergebruik |
| Heeft relaties met andere concepten | ✅ Containers, milieustraten, verwerkingscontracten, tarieven |

**6/6 criteria van toepassing.**

## Beschrijving

Een grondstofstroom is een afzonderlijke afval- of materiaalstroom die de gemeente beheert met een eigen inzamel- en verwerkingsstrategie. Elke grondstofstroom heeft eigen doelstellingen (kg/inwoner, scheidingspercentage), kwaliteitsmonitoring (sorteeranalyses), verwerkingscontracten en een eigen financieel model. De Grondstoffennota 2020 definieert per stroom het beleid, waaronder GFT (groente/fruit/tuin), PBP (plastic/blik/pak), papier/karton, glas, textiel en luiers.

> "Utrecht wil de komende 10 jaar toe naar 130 kg restafval per inwoner per jaar door meer grondstoffen gescheiden in te zamelen." (bron: [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020|Grondstoffennota 2020]])

## GGM-bron

> **Fractie**: Onderdeel, deeltje
> — *GGM, Afval (taakveld 7 Volksgezondheid en Milieu)*

**Entiteit:** Fractie
**Matchsterkte:** sterk — zelfde concept, maar het GGM gebruikt de technische term "Fractie" waar gemeenten spreken van "grondstofstroom" of "afvalstroom". De GGM-definitie "Onderdeel, deeltje" is generiek; het gemeentelijk concept is rijker en omvat beleid, doelstellingen en verwerkingsstrategie.

## BO-definitie

Het bedrijfsobject **Grondstofstroom** wijkt af van de GGM-entiteit **Fractie**. Het GGM definieert Fractie generiek als "Onderdeel, deeltje". Het BO voegt de bestuurlijke en operationele dimensie toe: elke grondstofstroom heeft een eigen inzamelstrategie, verwerkingsketen, kwaliteitsnormen en financieel model.

De naamkeuze "Grondstofstroom" sluit aan bij het gemeentelijk taalgebruik — de transitie van "afval" naar "grondstoffen" weerspiegelt het circulaire beleid.


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020]]

## Terugmelding GGM

De definitie van Fractie ("Onderdeel, deeltje") is te generiek voor de gemeentelijke context. Suggestie: verrijken naar een definitie die verwijst naar afval- en grondstofstromen, bijvoorbeeld: "Afzonderlijke afval- of grondstofstroom die gescheiden wordt ingezameld en verwerkt." Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

- **[[Container]]** — grondstofstromen worden ingezameld via specifieke containers (per fractie een containertype)
- **[[Milieustraat]]** — milieustraten zijn inzamelpunten voor meerdere grondstofstromen

## Bedrijfsprocessen

- **Afvalinzameling** — gescheiden ophalen van grondstofstromen bij de bron
- **Afvalverwerking** — verwerking per stroom (compostering, sortering, verbranding)
- **Grondstofscheiding** — nascheiding en handmatige sortering
- **Kwaliteitsmonitoring** — sorteeranalyses om vervuilingsgraad per stroom te meten

## Bedrijfsfuncties

- Afvalbeheer
