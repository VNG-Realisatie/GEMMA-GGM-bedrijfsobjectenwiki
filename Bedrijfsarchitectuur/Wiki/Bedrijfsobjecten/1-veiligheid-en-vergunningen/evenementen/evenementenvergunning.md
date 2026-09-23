---
type: element
naam: Evenementenvergunning
onderwerp: [evenementen]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein:
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
bo_definitie: "Toestemming van de gemeente aan een organisator om een evenement te organiseren op een specifieke locatie en datum."
bo_toelichting:
bedrijfsprocessen: []
bedrijfsfuncties: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Vergunningen en ontheffingen]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: Evenementenvergunning is een specialisatie van Vergunningen en ontheffingen
  - type: associatie
    bedrijfsobject: "[[Evenement]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..1"
    beschrijving: Vergunning wordt verleend voor een specifiek evenement
  - type: associatie
    bedrijfsobject: "[[Evenementenlocatie]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..1"
    beschrijving: Vergunning is gebonden aan een specifieke locatie
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Vergunning is de formele toestemming die het evenement mogelijk maakt |
| Herkenbaar voor domeinexperts | ✅ | Elke organisator kent het vergunningenproces |
| Heeft een eigen bestaan | ✅ | Vergunning bestaat als juridisch document, los van het evenement zelf |
| Kan in meervoud bestaan | ✅ | Honderden vergunningen per jaar |
| Heeft een eigen levenscyclus | ✅ | Aanvraag → beoordeling → verlening/weigering → eventueel intrekking |
| Heeft relaties met andere concepten | ✅ | Evenement, locatie, organisator, APV-regels |

**6/6 criteria van toepassing.**

## Beschrijving

Een evenementenvergunning is de formele toestemming van de gemeente aan een organisator om een evenement te organiseren op een specifieke locatie en datum. Het vergunningenproces verloopt in twee stappen: eerst plaatsing op de reserveringskalender (burgemeester stelt vast), daarna de vergunningaanvraag die aan de vergunningseisen moet voldoen.

De locatieprofielen (vastgelegd in de APV) bepalen de kaders waarbinnen de vergunning wordt verleend. Naast de evenementenvergunning kan ook een omgevingsvergunning vereist zijn. Het beleid voorziet in de mogelijkheid van meerjarige vergunningen, zodat terugkerende evenementen meer zekerheid en investeringsruimte krijgen.

## Procesbron

Dit BO heeft geen directe GGM-grondslag. Het GGM kent diverse vergunninggerelateerde entiteiten (VOMAanvraagOfMelding, VTHzaak, Omgevingsvergunning, Parkeervergunning, Ligplaatsontheffing) maar geen overkoepelend vergunningsconcept en geen specifieke evenementenvergunning.

Dit BO is een specialisatie van [[Vergunningen en ontheffingen]], het domeinoverstijgende parent BO voor alle gemeentelijke vergunningen en ontheffingen.

> "Zodra de kalender is vastgesteld, kunnen organisatoren een evenementenvergunning aanvragen. Een plek op de kalender betekent niet automatisch dat de aanvrager een vergunning krijgt. De vergunningsaanvraag moet voldoen aan de vergunningseisen."

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Vergunningen en ontheffingen]] | generalisatie | ↑ | — | Specialisatie |
| [[Evenement]] | associatie | ← | 1..1 | Beleidsnota: vergunning voor een specifiek evenement |
| [[Evenementenlocatie]] | associatie | → | 1..1 | Beleidsnota: vergunning gebonden aan locatie |

## Bedrijfsprocessen

- **Vergunningaanvraag** — organisator dient aanvraag in na plaatsing op reserveringskalender
- **Vergunningverlening** — gemeente beoordeelt aanvraag tegen vergunningseisen en locatieprofiel
- **Toezicht en handhaving** — naleving vergunningsvoorwaarden tijdens evenement


## Bronnen

- [[Wiki/Bronsamenvattingen/evenementen/locatiebeleid-evenementen]]
- [[Wiki/Bronsamenvattingen/evenementen/evenementenbeleid-utrecht]]

## Terugmelding GGM

**Evenementenvergunning ontbreekt in GGM.** Het GGM kent geen entiteit voor evenementenvergunningen. Het generieke hiaat (ontbreken van een overkoepelend vergunningsconcept) is vastgelegd bij [[Vergunningen en ontheffingen]]. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
