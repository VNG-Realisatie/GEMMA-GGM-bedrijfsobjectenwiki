---
type: element
naam: Stukdeel
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: ggm-entiteit

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

ggm_duplicaat_entiteiten: []

bo_definitie: "Een onderdeel van een ingeschreven stuk dat een rechtsfeit beschrijft op basis waarvan de BRK wordt bijgewerkt."
bo_toelichting: ''
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Stuk]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een stukdeel is onderdeel van precies één stuk"
  - type: associatie
    bedrijfsobject: "[[Zakelijk Recht]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een stukdeel kan de grondslag zijn voor een of meer zakelijke rechten"
  - type: associatie
    bedrijfsobject: "[[Tenaamstelling]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een stukdeel kan de grondslag zijn voor een of meer tenaamstellingen"
  - type: associatie
    bedrijfsobject: "[[Zekerheidsrecht]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een stukdeel kan de grondslag zijn voor een zekerheidsrecht"
bedrijfsprocessen:
  - Kadastrale recherche
  - Eigendomsverificatie
bedrijfsfuncties:
  - Vastgoedbeheer
---

## BO-criteria toetsing

5/6 criteria (eigen bestaan is zwakker: altijd onderdeel van een [[Stuk]]). Stukdeel bevat de rechtsfeiten die de bijwerking van de BRK bepalen. Eigen attributen (aard stukdeel: overdracht, hypotheek, splitsing), meervoudig (een stuk bevat een of meer stukdelen), en relaties met zakelijke rechten, tenaamstellingen en zekerheidsrechten.

## Beschrijving

Een stukdeel is een onderdeel van een [[Stuk|ingeschreven stuk]] dat een specifiek rechtsfeit beschrijft. Het stukdeel bepaalt welke bijwerking van de BRK plaatsvindt. Voorbeelden van rechtsfeiten: overdracht van eigendom, vestiging van hypotheek, appartementsrechtsplitsing, beëindiging van een beperkt recht. Alle objecten in de BRK (zakelijk recht, tenaamstelling, kadastraal object, zekerheidsstelling) traceren naar het stukdeel op basis waarvan ze zijn ontstaan of gewijzigd.

## GGM-bron

Geen GGM-match gevonden. Stukdeel is een **GGM-hiaat**.

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| onderdeel van | naar-dit-BO | [[Stuk]] | 1 | BRK Catalogus |
| grondslag voor | naar-dit-BO | [[Zakelijk Recht]] | 0..* | BRK Catalogus |
| grondslag voor | naar-dit-BO | [[Tenaamstelling]] | 0..* | BRK Catalogus |
| grondslag voor | naar-dit-BO | [[Zekerheidsrecht]] | 0..* | BRK Catalogus |
| grondslag voor | naar-dit-BO | [[Kadastraal Perceel]] | 0..* | BRK Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]

## Terugmelding GGM

Stukdeel ontbreekt als objecttype in het GGM. Component van Stuk (compositie) met eigen attributen (aard stukdeel). Alle BRK-objecten traceren naar stukdelen als grondslag. Past in beleidsdomein RSGBPlus (99 Kern). Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
