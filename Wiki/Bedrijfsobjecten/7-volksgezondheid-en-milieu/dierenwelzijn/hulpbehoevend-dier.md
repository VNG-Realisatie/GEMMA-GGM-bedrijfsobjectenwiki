---
type: bedrijfsobject
naam: Hulpbehoevend dier
domein: [Dierenwelzijn]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
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
gemma_definitie: "Wild of gehouden dier dat gevonden, gewond of anderszins hulpbehoevend is en waarvoor de gemeente wettelijk verplicht opvang en vervoer organiseert."
bronnen:
  - "[[Wiki/Bronsamenvattingen/Dierenwelzijn/nota-dierenwelzijn]]"
relaties:
  - type: associatie
    bedrijfsobject: "[[kinderboerderij]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Hulpbehoevend dier kan afkomstig zijn van of herplaatst worden naar een kinderboerderij
---

# Hulpbehoevend dier

Wild of gehouden dier dat gevonden, gewond of anderszins hulpbehoevend is en waarvoor de gemeente wettelijk verplicht opvang en vervoer organiseert.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — kernbegrip van de wettelijke gemeentelijke taak
- ✅ Is herkenbaar voor domeinexperts — "dit hulpbehoevende dier" is standaardtaal
- ✅ Heeft een eigen bestaan — elk dier is een individueel geval met eigen kenmerken
- ✅ Kan in meervoud bestaan — honderden per jaar (Stichts Asyl vangt jaarlijks 700+ katten op)
- ✅ Heeft een eigen levenscyclus — gevonden → vervoerd → opgevangen → herplaatst/terug naar eigenaar/terug naar natuur
- ✅ Heeft relaties met andere concepten — opvanginstelling, vindlocatie, eigenaar, diersoort

## GGM-bron

Geen GGM-match. Het GGM kent geen beleidsdomein voor dierenwelzijn. Onder taakveld 7 (Volksgezondheid en Milieu) bestaat alleen het beleidsdomein Afval. De opvang van hulpbehoevende dieren is een wettelijke gemeentelijke taak (BW 5:8 lid 3) die structureel niet in het GGM is gemodelleerd.

## Procesbron

Wettelijke grondslag: Burgerlijk Wetboek art. 5:8 lid 3 (gevonden dieren) en Algemene Wet Bestuursrecht (dieren bij huisontruimingen, opvangtermijn max. 13 weken).

De gemeente organiseert opvang en vervoer via een contract met de Dierenbescherming. Onderaannemers: Stichts Asyl voor Dieren (honden/katten), Dierenambulance Utrecht (vervoer), Vogelopvang Utrecht (wilde vogels), Dierenbeschermingscentrum Amersfoort (konijnen/knaagdieren).

> "Gemeente Utrecht kiest ervoor om opvang en vervoer van alle hulpbehoevende dieren uit de gemeente Utrecht - zowel wilde als gehouden dieren – structureel te regelen met een organisatie die reeds een sterke rol heeft in deze activiteit." (bron: [[Wiki/Bronsamenvattingen/Dierenwelzijn/nota-dierenwelzijn|Nota Dierenwelzijn]])

## Relaties

- ↔ [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/dierenwelzijn/kinderboerderij|kinderboerderij]] — hulpbehoevend dier kan afkomstig zijn van of herplaatst worden naar een kinderboerderij

## Bedrijfsprocessen

- Melding en vervoer hulpbehoevend dier
- Opvang en verzorging
- Herplaatsing of teruggave aan eigenaar
- Noodopvang bij huisontruimingen en calamiteiten
