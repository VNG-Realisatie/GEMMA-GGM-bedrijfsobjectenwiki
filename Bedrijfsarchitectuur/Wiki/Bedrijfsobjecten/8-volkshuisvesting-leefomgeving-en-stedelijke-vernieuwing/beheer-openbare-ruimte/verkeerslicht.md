---
type: bedrijfsobject
naam: Verkeerslicht
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Verkeerslicht"
ggm_guid: EAID_620FF102_974C_43a6_A6A0_79BB71E8580D
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "Lichten die aangeven dat je moet stoppen, dat je mag doorrijden, of die je waarschuwen voor gevaar."
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
bo_definitie: "Verkeersregelinstallatie in de openbare ruimte die het verkeer regelt op kruispunten en oversteekplaatsen."
bo_relaties:
  - type: generalisatie
    bedrijfsobject: Beheerobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Verkeerslicht is een beheerobject in de openbare ruimte
bedrijfsprocessen: [Onderhoud verkeersregelinstallaties, Vervanging VRI, Storingsdienst verkeerslichten]
bedrijfsfuncties: [Beheer openbare ruimte, Verkeer en mobiliteit]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel voor verkeersveiligheid en doorstroming |
| Is herkenbaar voor domeinexperts | ✅ | Verkeersregelinstallatie (VRI) — standaardbegrip in verkeersbeheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elke VRI individueel geregistreerd met locatie, type, besturing |
| Kan in meervoud bestaan | ✅ | Honderden verkeerslichten in de gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanleg → onderhoud → vervanging; afschrijvingstermijn 10 jaar |
| Heeft relaties met andere concepten | ✅ | Installatie, sensor, kast, verharding, storing |

Score: 6/6.

## Beschrijving

Een verkeerslicht (verkeersregelinstallatie, VRI) is een installatie in de openbare ruimte die het verkeer regelt op kruispunten en oversteekplaatsen. De gemeente registreert elke installatie met locatie, type besturing en onderhoudsstatus.

De afschrijvingstermijn is 10 jaar, de kortste van alle objectsoorten in de openbare ruimte. De Nota Beheer OR vermeldt dat er geen achterstallig onderhoud is bij VRI's — het zekerheidspercentage is 95-100%.

In het GGM is Verkeerslicht een entiteit binnen het beleidsdomein Beheer Openbare Ruimte. De brede GGM-definitie ("lichten die aangeven dat je moet stoppen...") beschrijft het concept vanuit de weggebruiker; de GEMMA-definitie benadrukt het gemeentelijke beheer- en registratieperspectief.

## BO-definitie

De GEMMA-definitie benadrukt het gemeentelijke perspectief: het gaat om de verkeersregelinstallatie als beheerd object, niet om het verkeerslicht als visueel signaal voor de weggebruiker.

## GGM-bron

> "Lichten die aangeven dat je moet stoppen, dat je mag doorrijden, of die je waarschuwen voor gevaar."

- **Entiteit**: Verkeerslicht
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Attributen**: *(geen attributen op de entiteit zelf)*

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Beheerobject (GGM) | Verkeerslicht → Beheerobject | GGM |

## Bedrijfsprocessen

- **Onderhoud verkeersregelinstallaties**: preventief onderhoud, softwareupdates, lampvervanging
- **Vervanging VRI**: vervanging complete installatie bij einde levensduur
- **Storingsdienst verkeerslichten**: 24/7 beschikbaar voor meldingen van defecte VRI's

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
