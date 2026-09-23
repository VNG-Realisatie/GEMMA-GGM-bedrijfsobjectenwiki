---
type: element
naam: Crematorium
onderwerp: [openbare gezondheid]
archimate_type: business-object
grondslag: governance-object

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

ggm_duplicaat_entiteiten: []

bo_definitie: "Voorziening waarin crematie plaatsvindt, gemeentelijk of bijzonder (kerkgenootschap of privaatrechtelijke rechtspersoon)."
bo_toelichting:
bo_subtypes:
  - naam: Gemeentelijk crematorium
    omschrijving: "Crematorium in stand gehouden door de gemeente"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Bijzonder crematorium
    omschrijving: "Crematorium gevestigd en in werking gehouden door een kerkgenootschap, privaatrechtelijke rechtspersoon of natuurlijk persoon (art. 52 Wlb); behoeft vergunning van burgemeester en wethouders"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/begraafplaats|Begraafplaats]]"
    richting: bidirectioneel
    kardinaliteit: "0..* → 0..*"
    beschrijving: "Een asbus kan worden bijgezet op een begraafplaats in plaats van bij het crematorium zelf"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis|Gemeentebegrafenis]]"
    richting: naar-dit-BO
    kardinaliteit: "0..* → 1"
    beschrijving: "Een gemeentebegrafenis kan ook een crematie zijn (art. 21 Wlb, tenzij tot ontleding bestemd)"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| # | Criterium | Toepassing |
|---|---|---|
| 1 | Betekenis binnen onderwerp | Kernvoorziening voor crematie, wettelijk gereguleerd naast begraving |
| 2 | Herkenbaar voor domeinexperts | Standaardbegrip bij burgerzaken en uitvaartbranche |
| 3 | Eigen bestaan | Fysiek zelfstandige voorziening, los van individuele crematies |
| 4 | Meervoud | Meerdere crematoria per regio, gemeentelijk en bijzonder |
| 5 | Eigen levenscyclus | Vestiging (met vergunning bij bijzonder crematorium) → in werking → eventuele sluiting |
| 6 | Relaties | Houder, register van gecremeerde lijken, asbus, begraafplaats (bijzetting) |

Score: 6/6.

## Beschrijving

Crematie geschiedt in een crematorium (art. 49 Wlb). Net als begraafplaatsen worden crematoria onderscheiden in gemeentelijke en bijzondere (art. 51): een bijzonder crematorium kan alleen worden gevestigd en in werking gehouden door een kerkgenootschap, een privaatrechtelijke rechtspersoon of een natuurlijk persoon, en behoeft een vergunning van burgemeester en wethouders (art. 52-53). Vestiging van een gemeentelijk crematorium of vergunningverlening voor een bijzonder crematorium wordt pas besloten nadat het voornemen minimaal dertig dagen vooraf openbaar bekend is gemaakt (art. 54).

De houder van een crematorium houdt een openbaar register bij van alle daar gecremeerde lijken en van de bestemming die aan de as is gegeven (art. 50). Na crematie bergt de houder de as in een of meer asbussen; deze worden vervolgens bijgezet (eventueel op een begraafplaats), verstrooid, aan een nabestaande ter beschikking gesteld, of naar het buitenland verzonden (art. 58-59).

## Juridische bron

Wettelijke basis: Wet op de lijkbezorging, hoofdstuk IV (art. 49-66b). Zie [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst|Wet op de lijkbezorging — volledige wettekst]].

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/begraafplaats\|Begraafplaats]] | associatie | ↔ | 0..* → 0..* | Art. 62 Wlb (bijzetting asbus) |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | associatie | ← | 0..* → 1 | Art. 21 Wlb |

## Bronnen

- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst]]

## Terugmelding GGM

GGM-hiaat: geen GGM-entiteit voor crematorium of de bergings-/bestemmingsregels van de as. Zie #121 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
