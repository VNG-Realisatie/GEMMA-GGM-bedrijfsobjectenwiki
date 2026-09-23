---
type: element
naam: Orgel
onderwerp: [Cultuur]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein: "Monumenten"
ggm_guid:
ggm_uml_type:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
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
bo_definitie: "Rijks- of gemeentelijk monumentaal muziekinstrument in een kerkgebouw, met eigen beschermingsstatus en eigen levenscyclus onafhankelijk van het gebouw."
bo_toelichting:
bedrijfsprocessen: [Monumentenaanwijzing, Erfgoedtoezicht, Herbestemming kerkgebouw]
bedrijfsfuncties: [Erfgoedbeheer]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument|Monument]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een monument (kerkgebouw) kan een of meer orgels bevatten
---

# Orgel

Rijks- of gemeentelijk monumentaal muziekinstrument in een kerkgebouw. Orgels kunnen een eigen monumentstatus hebben, los van het kerkgebouw waarin ze staan. De gemeente inventariseert en registreert orgels apart en stelt bij herbestemming van kerkgebouwen een eigen afwegingskader op voor het behoud van het orgel.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Orgels zijn een expliciet onderdeel van het Utrechtse erfgoedbeleid, met een eigen afwegingskader |
| Herkenbaar voor experts | ✅ | Erfgoedspecialisten kennen orgels als apart beschermingsobject |
| Eigen bestaan | ✅ | Een orgel kan fysiek verplaatst worden naar een ander gebouw; het bestaat onafhankelijk van het kerkgebouw |
| Meervoud | ✅ | Utrecht telt tientallen monumentale orgels |
| Eigen levenscyclus | ✅ | Bouw → plaatsing → restauratie → verplaatsing → eventueel verlies; onafhankelijk van de levenscyclus van het kerkgebouw |
| Relaties | ✅ | Met monument (kerkgebouw), orgelmaker, monumentstatus |

## GGM-hiaat

Er is geen GGM-entiteit voor orgel. Het GGM-beleidsdomein Monumenten bevat zes entiteiten (Beschermde Status, Ambacht, Bouwactiviteit, Bouwstijl, Bouwtype, OorspronkelijkeFunctie) — alle gericht op onroerend erfgoed. Orgels zijn roerend erfgoed met een eigen beschermingsstatus.

Dit is een dataobject-hiaat: orgels worden door gemeenten geregistreerd en geïnventariseerd, hebben registreerbare attributen (maker, bouwjaar, locatie, monumentstatus, bespeelbaarheid, dispositie) en passen in het GGM-beleidsdomein Monumenten.

## BO-definitie

Het bedrijfsobject **Orgel** is een registreerbaar roerend erfgoedobject. Het onderscheidt zich van het BO [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument|monument]] doordat:

1. Het een **roerend** object is dat fysiek verplaatsbaar is tussen gebouwen
2. Het een **eigen monumentstatus** kan hebben (rijks- of gemeentelijk monument), onafhankelijk van het kerkgebouw
3. Het een **eigen levenscyclus** heeft — orgels worden gebouwd, verplaatst, gerestaureerd en soms verloren, onafhankelijk van het lot van het gebouw
4. De gemeente een **eigen afwegingskader** voor orgels opstelt bij herbestemming van kerkgebouwen

> "De orgels in de kerkgebouwen zijn in vele gevallen beschermd als (rijks- of gemeentelijk) monument, meestal is die bescherming expliciet benoemd." (bron: visie religieus erfgoed 2025, hst. 3)

> "Naast het herbestemmingsprofiel stellen wij daarom een afwegingskader voor orgels op, om de monumentale waarden van het orgel (die mogelijk strijdig zijn met de wensen voor herbestemming van het kerkgebouw) in ogenschouw te nemen." (bron: visie religieus erfgoed 2025, hst. 5)

## Relaties

| Relatie | Bedrijfsobject | Bron | Toelichting |
|---|---|---|---|
| Staat in | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]] | Visie religieus erfgoed 2025 | Een orgel bevindt zich in een kerkgebouw (monument); bij verplaatsing kan dit wijzigen |

## Bedrijfsprocessen

- **Monumentenaanwijzing**: orgels kunnen apart worden aangewezen als rijks- of gemeentelijk monument
- **Erfgoedtoezicht**: gemeente inventariseert en monitort staat van orgels
- **Herbestemming kerkgebouw**: bij herbestemming wordt apart afgewogen of het orgel behouden, verplaatst of opgeslagen wordt

## Bedrijfsfuncties

- Erfgoedbeheer


## Bronnen

- [[Wiki/Bronsamenvattingen/Cultuur/kunst-en-cultuur]]
- [[Wiki/Bronsamenvattingen/Cultuur/propositie-cultuur]]
- [[Wiki/Bronsamenvattingen/Cultuur/architectuur-en-erfgoed]]
- [[Wiki/Bronsamenvattingen/Cultuur/bibliotheekwerk]]
- [[Wiki/Bronsamenvattingen/Cultuur/toelichting-ringenmodel]]
- [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht]]
- [[Wiki/Bronsamenvattingen/erfgoed/visie-religieus-erfgoed-2025]]
- [[Wiki/Bronsamenvattingen/Cultuur/erfgoedbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/erfgoed/bijlagen-visie-religieus-erfgoed]]

## Terugmelding GGM

**Orgel** — Registratieobject voor monumentale muziekinstrumenten in kerkgebouwen. Roerend erfgoed met eigen monumentstatus, geïnventariseerd door de gemeentelijke afdeling Erfgoed. Attributen: maker, bouwjaar, locatie (kerkgebouw), monumentstatus, bespeelbaarheid, dispositie. Past onder beleidsdomein Monumenten (taakveld 5 Sport, Cultuur en Recreatie).
