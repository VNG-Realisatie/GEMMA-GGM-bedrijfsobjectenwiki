---
type: bedrijfsobject
naam: Instrument
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Een beschikbare dienst of tool voor toeleiding naar werk of participatie, geregistreerd in een instrumentengids."
bo_toelichting: "Gemeenten vullen instrumentengidsen (Dennis & Eva) met lokale en regionale instrumenten. Dennis ondersteunt werkgeversdienstverlening, Eva ondersteunt begeleiding van werkzoekenden. Het onderscheid met Re-integratievoorziening: instrument = catalogus-item (wat is beschikbaar), re-integratievoorziening = toekenning (ingezet voor specifieke persoon)."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Re-integratievoorziening]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "re-integratievoorziening is toekenning van een instrument"
  - type: associatie
    bedrijfsobject: "[[Werkzoekende]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "instrument beschikbaar voor werkzoekenden"
bedrijfsprocessen: [instrumentbeheer, werkgeversdienstverlening, arbeidstoeleiding]
bedrijfsfuncties: [arbeidsparticipatie, re-integratie, werkgeversdienstverlening]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Beschikbare dienst/tool voor arbeidstoeleiding en participatie |
| Herkenbaar voor domeinexperts | ✅ Gemeenteprofessionals vullen Dennis & Eva actief met instrumenten |
| Eigen bestaan | ✅ Catalogus-item dat onafhankelijk van specifieke casus bestaat |
| Meervoud | ✅ Tientallen lokale en regionale instrumenten per gemeente |
| Levenscyclus | ✅ Aangemaakt → beschikbaar → verouderd/ingetrokken |
| Relaties | ✅ Aanbieder, uitvoeringslocatie, Re-integratievoorziening, Werkzoekende |

Score: **6/6**

## Beschrijving

Een instrument is een beschikbare dienst, tool of programma dat gemeenten inzetten voor toeleiding naar werk of duurzame participatie. Gemeenten registreren hun lokale en regionale instrumenten in de instrumentengidsen Dennis (werkgeversdienstverlening) en Eva (begeleiding werkzoekenden). Deze instrumenten zijn vervolgens zichtbaar in alle instrumentengidsen, net als landelijke instrumenten.

Per instrument worden geregistreerd: de aanbieder, uitvoeringslocatie(s), doelgroep, type dienst en beschikbaarheidsperiode.

Het onderscheid met [[Re-integratievoorziening]]: een instrument is het catalogus-item (wat is beschikbaar voor inzet), een re-integratievoorziening is de concrete toekenning aan een specifieke [[Werkzoekende]] (met registratienummer, start- en einddatum).

## Procesbron

Het instrument is afgeleid uit het SGR 19.0 (BKWI), conceptueel gegevensdeelmodel van de instrumentengidsen Dennis & Eva. Gemeenten vullen deze gidsen zelf met lokale en regionale instrumenten. Zie [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr|Wet SUWI en SGR]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| toekenning als [[Re-integratievoorziening\|Re-integratievoorziening]] | naar dit BO | 0..* | SGR |
| beschikbaar voor [[Werkzoekende]] | naar dit BO | 0..* | SGR |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr]]

## Terugmelding GGM

GGM-hiaat: het GGM Werk-domein modelleert Reintegratievoorziening als toekenning maar heeft geen catalogus-/typeniveau voor beschikbare instrumenten. Teruggemeld als #86 in [[Wiki/Analyses/ggm-terugmeldingen]].
