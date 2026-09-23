---
type: element
naam: Begraafplaats
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

bo_definitie: "Terrein waarop lijken worden begraven, gemeentelijk (wettelijk verplicht, minimaal één per gemeente) of bijzonder (kerkgenootschap of privaatrechtelijke rechtspersoon)."
bo_toelichting:
bo_subtypes:
  - naam: Gemeentelijke begraafplaats
    omschrijving: "Begraafplaats aangelegd en in stand gehouden door de gemeente; wettelijk verplicht (art. 33 Wlb)"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Bijzondere begraafplaats
    omschrijving: "Begraafplaats aangelegd en in stand gehouden door een kerkgenootschap, privaatrechtelijke rechtspersoon of natuurlijk persoon (art. 37 Wlb)"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/grafrecht|Grafrecht]]"
    richting: naar-dit-BO
    kardinaliteit: "1 → 0..*"
    beschrijving: "Een begraafplaats bevat de graven waarop een grafrecht kan rusten"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis|Gemeentebegrafenis]]"
    richting: naar-dit-BO
    kardinaliteit: "0..* → 1"
    beschrijving: "Een gemeentebegrafenis vindt plaats op een (gemeentelijke) begraafplaats"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/crematorium|Crematorium]]"
    richting: bidirectioneel
    kardinaliteit: "0..* → 0..*"
    beschrijving: "Een asbus kan worden bijgezet op een begraafplaats in plaats van bij het crematorium zelf"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| # | Criterium | Toepassing |
|---|---|---|
| 1 | Betekenis binnen onderwerp | Kernvoorziening van de lijkbezorging; wettelijk verplichte gemeentelijke taak |
| 2 | Herkenbaar voor domeinexperts | Standaardbegrip bij burgerzaken en beheer begraafplaatsen |
| 3 | Eigen bestaan | Fysiek en juridisch zelfstandig terrein, los van individuele graven |
| 4 | Meervoud | Elke gemeente heeft minimaal één, vaak meerdere begraafplaatsen (gemeentelijk én bijzonder) |
| 5 | Eigen levenscyclus | Aanleg/uitbreiding → in gebruik name → (evt.) sluiting → opheffing na 20 jaar grafrust |
| 6 | Relaties | Graven/grafrecht, houder, gemeenteraad (verordenende bevoegdheid), kerkgenootschap (bij bijzondere begraafplaats) |

Score: 6/6.

## Beschrijving

Elke gemeente heeft, alleen of samen met andere gemeenten, verplicht ten minste één gemeentelijke begraafplaats (art. 33 Wlb), tenzij gedeputeerde staten daarvan tijdelijk ontheffing hebben verleend. Naast gemeentelijke begraafplaatsen bestaan bijzondere begraafplaatsen, aangelegd en in stand gehouden door een kerkgenootschap, een privaatrechtelijke rechtspersoon of een natuurlijk persoon (art. 37).

De houder van een begraafplaats houdt een openbaar register bij van alle daar begraven lijken, met een nauwkeurige plaatsaanduiding (art. 27). Begraving vindt plaats in een algemeen graf (de houder bepaalt wie erin wordt begraven) of een particulier graf, waarop een [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/grafrecht|grafrecht]] rust.

Een begraafplaats kan worden gesloten (bij een gemeentelijke begraafplaats: besluit van burgemeester en wethouders) en na tien jaar zonder begraving ambtshalve gesloten worden verklaard. Na sluiting blijft de begraafplaats twintig jaar onaangeroerd liggen voordat de grond een andere bestemming kan krijgen (art. 43-48).

## GGM-controle

Geen GGM-entiteit gevonden voor Begraafplaats, Graf of aanverwante begrippen (gecontroleerd in `ggm_parsed.json` op "begraaf", "graf", "crematorium", "lijkschouw", "asbus"). Ook het onderwerp Beheer Openbare Ruimte (IMBOR) modelleert geen begraafplaatsen. Dit is dus een onbezet GGM-hiaat, niet een bestaande maar over het hoofd geziene entiteit.

## Subtypes

Herkende specialisaties van Begraafplaats. Gevonden in bronnen. Geen apart BO — beide subtypes delen register, ligging op graven en sluitingsprocedure; het onderscheid zit in eigenaarschap en governance, niet in proces of attributen.

- **Gemeentelijke begraafplaats** — aangelegd en in stand gehouden door de gemeente; wettelijk verplicht, minimaal één per gemeente
- **Bijzondere begraafplaats** — aangelegd en in stand gehouden door een kerkgenootschap, privaatrechtelijke rechtspersoon of natuurlijk persoon; gebruik behoeft toestemming van burgemeester en wethouders

## Juridische bron

Wettelijke basis: Wet op de lijkbezorging, hoofdstuk III (art. 23-48). Zie [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst|Wet op de lijkbezorging — volledige wettekst]].

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/grafrecht\|Grafrecht]] | compositie | → | 1 → 0..* | Art. 23, 28 Wlb |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | associatie | ← | 0..* → 1 | Art. 20-22 Wlb |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/crematorium\|Crematorium]] | associatie | ↔ | 0..* → 0..* | Art. 62 Wlb (bijzetting asbus) |

## Bronnen

- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst]]

## Terugmelding GGM

GGM-hiaat: het GGM modelleert geen begraafplaatsen, graven of grafrechten — noch onder taakveld 7 (Volksgezondheid en Milieu), noch onder Beheer Openbare Ruimte/IMBOR. Wettelijk verplichte gemeentelijke voorziening (art. 33 Wlb) met eigen register (art. 27). Zie #119 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
