---
type: bedrijfsobject
naam: Evenementenvergunning
domein: [evenementen]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
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

gemma_definitie: "Toestemming van de gemeente aan een organisator om een evenement te organiseren op een specifieke locatie en datum."
gemma_toelichting: "Wordt aangevraagd na plaatsing op de reserveringskalender. Plaatsing garandeert geen vergunning; de aanvraag moet aan vergunningseisen voldoen. Naast de evenementenvergunning kan ook een omgevingsvergunning vereist zijn."
bronnen:
  - [[Wiki/Bronsamenvattingen/Evenementen/locatiebeleid-evenementen]]
relaties:
  - type: associatie
    bedrijfsobject: [[Evenement]]
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Vergunning wordt verleend voor een specifiek evenement"
  - type: associatie
    bedrijfsobject: [[Evenementenlocatie]]
    richting: van-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Vergunning is gebonden aan een specifieke locatie"
bedrijfsprocessen:
  - Vergunningaanvraag
  - Vergunningverlening
  - Toezicht en handhaving
bedrijfsfuncties:
  - Vergunningverlening
  - Evenementenbeheer
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

⚠️ **Ter discussie**: op termijn zou een generiek BO **Vergunning** moeten komen dat domeinoverstijgend werkt. De evenementenvergunning is voorlopig als apart BO opgenomen omdat het vergunningslandschap in het GGM gefragmenteerd is en er geen generiek vergunnings-BO bestaat.

> "Zodra de kalender is vastgesteld, kunnen organisatoren een evenementenvergunning aanvragen. Een plek op de kalender betekent niet automatisch dat de aanvrager een vergunning krijgt. De vergunningsaanvraag moet voldoen aan de vergunningseisen."

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Evenement]] | associatie | ← | 1..1 | Beleidsnota: vergunning voor een specifiek evenement |
| [[Evenementenlocatie]] | associatie | → | 1..1 | Beleidsnota: vergunning gebonden aan locatie |

## Bedrijfsprocessen

- **Vergunningaanvraag** — organisator dient aanvraag in na plaatsing op reserveringskalender
- **Vergunningverlening** — gemeente beoordeelt aanvraag tegen vergunningseisen en locatieprofiel
- **Toezicht en handhaving** — naleving vergunningsvoorwaarden tijdens evenement

## Terugmelding GGM

**Generiek vergunningsconcept ontbreekt.** Het GGM kent vergunningen alleen als domeinspecifieke entiteiten (Omgevingsvergunning, Parkeervergunning, Ligplaatsontheffing) zonder overkoepelend concept. Een evenementenvergunning past in geen van deze. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
