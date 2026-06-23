---
type: bedrijfsobject
naam: Vergunningen en ontheffingen
domein: [dienstverlening]
archimate_type: "business-object"
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

gemma_definitie: "Formeel besluit van de gemeente waarmee een inwoner of ondernemer toestemming krijgt voor een specifieke activiteit of een uitzondering op een verbod."
gemma_subtypes:
  - naam: Standplaatsvergunning
    omschrijving: "APV-vergunning voor het innemen van een standplaats in de openbare ruimte"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: Horecavergunning
    omschrijving: "Exploitatievergunning voor een horecabedrijf"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: Ligplaatsvergunning
    omschrijving: "Vergunning voor het innemen van een ligplaats"
    ggm_entiteit: "Ligplaatsontheffing"
    ggm_guid: EAID_872A0342_EA75_418e_9455_E51875BFD771
    ggm_attribuut: ""
  - naam: Exploitatievergunning (vaarverkeer)
    omschrijving: "Vergunning voor commercieel gebruik van vaartuig"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: Omgevingsvergunning
    omschrijving: "Vergunning als bedoeld in afdeling 5.1 van de Omgevingswet"
    ggm_entiteit: "Omgevingsvergunning"
    ggm_guid: EAID_053B594A_5E45_4413_9339_D2D026ECCE20
    ggm_attribuut: ""
relaties:
  - type: generalisatie
    bedrijfsobject: "[[Evenementenvergunning]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: "Evenementenvergunning is een specialisatie"
  - type: generalisatie
    bedrijfsobject: "[[Parkeervergunning]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: "Parkeervergunning is een specialisatie"
  - type: generalisatie
    bedrijfsobject: "[[Ontheffing (milieuzone)]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: "Ontheffing milieuzone is een specialisatie"
  - type: associatie
    bedrijfsobject: "[[Aanvraag of melding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Wordt aangevraagd via een aanvraag of melding"
bedrijfsprocessen: [Vergunningverlening, Ontheffingverlening, Bezwaar en beroep]
bedrijfsfuncties: [Vergunningverlening, Dienstverlening]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Vergunningen en ontheffingen zijn de kern van gemeentelijke regulering |
| Herkenbaar voor domeinexperts | ✅ | Elke gemeente kent het onderscheid vergunning (toestemming voor activiteit) en ontheffing (uitzondering op verbod) |
| Heeft een eigen bestaan | ✅ | Formeel besluit met eigen kenmerken, juridische status en geldigheidsduur |
| Kan in meervoud bestaan | ✅ | Duizenden vergunningen en ontheffingen per gemeente per jaar |
| Heeft een eigen levenscyclus | ✅ | Aanvraag → beoordeling → verlening/weigering → bezwaar → intrekking/verloop |
| Heeft relaties met andere concepten | ✅ | Aanvraag of melding, aanvrager, locatie, activiteit, toezicht |

**6/6 criteria van toepassing.**

## Beschrijving

Vergunningen en ontheffingen zijn formele besluiten waarmee de gemeente een inwoner of ondernemer toestemming verleent voor een specifieke activiteit (vergunning) of een uitzondering maakt op een algemeen verbod (ontheffing). In de Awb-terminologie zijn beide een beschikking — een besluit van een bestuursorgaan in een individueel geval.

Dit BO is het overkoepelende concept voor alle domeinspecifieke vergunningen en ontheffingen die de gemeente verleent. De specialisaties verschillen sterk in achterliggend proces, maar delen dezelfde structuur: een aanvraag leidt tot een beoordeling die uitmondt in een formeel besluit.

### Wat valt hieronder

- **Vergunningen** — toestemming om een activiteit uit te voeren (evenementenvergunning, parkeervergunning, horecavergunning, omgevingsvergunning, standplaatsvergunning)
- **Ontheffingen** — uitzondering op een verbod (ontheffing milieuzone, ligplaatsontheffing)

### Wat valt hier niet onder

- **Subsidies** — financieel product, structureel ander proces en ander GGM-domein
- **Belastingbeschikkingen** — eenzijdig opgelegd, geen aanvraag
- **Meldingen** — informatieoverdracht, geen toestemmingsbesluit (vallen onder [[Aanvraag of melding]])

## Specialisaties

De specialisaties laten zien hoe divers vergunningen en ontheffingen zijn qua proces, betrokken partijen, kosten en doelgroep.

### BO-specialisaties

| Specialisatie | Domein | Doorlooptijd | Ketenpartners | Kosten | Doelgroep |
|---|---|---|---|---|---|
| [[Evenementenvergunning]] | Evenementen | Weken-maanden (adviesronden) | Politie, brandweer, GGD, omwonenden | Variabel per omvang | Organisatoren (ondernemers/stichtingen) |
| [[Parkeervergunning]] | Parkeren | Dagen-weken (standaardproces) | Geen externe ketenpartners | Vast jaarlijks tarief | Inwoners, ondernemers |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/ontheffing-milieuzone\|Ontheffing (milieuzone)]] | Milieu | Dagen (geautomatiseerd/handmatig) | RDW (kentekencheck) | Geen of gering | Inwoners, ondernemers |

### Subtypes (geen apart BO)

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Standplaatsvergunning | APV-vergunning voor het innemen van een standplaats in de openbare ruimte | — |
| Horecavergunning | Exploitatievergunning voor een horecabedrijf | — |
| Ligplaatsvergunning | Vergunning voor het innemen van een ligplaats | [Ligplaatsontheffing](vth.md) |
| Exploitatievergunning (vaarverkeer) | Vergunning voor commercieel gebruik van vaartuig | — |
| Omgevingsvergunning | Vergunning als bedoeld in afdeling 5.1 van de Omgevingswet | [Omgevingsvergunning](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |

## Procesbron

Dit BO heeft geen directe GGM-grondslag. Het GGM modelleert vergunningen en ontheffingen uitsluitend als domeinspecifieke entiteiten (Omgevingsvergunning, Parkeervergunning, Ligplaatsontheffing) zonder gemeenschappelijk supertype. Op de proceskant kent het GGM wel VOMAanvraagOfMelding ("Vergunning, Ontheffing of Melding"), maar dat betreft de aanvraag, niet het verleende recht zelf.

Het concept is afgeleid uit gemeentelijke beleidsbronnen die elk hun eigen vergunningstype beschrijven, maar dezelfde processtructuur hanteren: aanvraag → beoordeling → verlening/weigering.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Evenementenvergunning]] | generalisatie | ↓ | — | Specialisatie |
| [[Parkeervergunning]] | generalisatie | ↓ | — | Specialisatie |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/ontheffing-milieuzone\|Ontheffing (milieuzone)]] | generalisatie | ↓ | — | Specialisatie |
| [[Aanvraag of melding]] | associatie | ← | 0..* | Procesingang |

## Bedrijfsprocessen

- **Vergunningverlening** — beoordeling van aanvragen en verlening of weigering van vergunningen
- **Ontheffingverlening** — beoordeling van verzoeken om uitzondering op een verbod
- **Bezwaar en beroep** — behandeling van bezwaren tegen vergunnings- of ontheffingsbesluiten

## Bronnen

- [[Wiki/Bronsamenvattingen/Evenementen/locatiebeleid-evenementen]]
- [[Wiki/Bronsamenvattingen/Evenementen/evenementenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]
- [[Wiki/Bronsamenvattingen/mobiliteit/parkeervisie]]
- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025]]
- [[Wiki/Bronsamenvattingen/Economie/horecabeleid-utrecht]]

## Terugmelding GGM

**Generiek vergunnings-/ontheffingsconcept ontbreekt.** Het GGM modelleert vergunningen en ontheffingen alleen als domeinspecifieke entiteiten (Omgevingsvergunning, Parkeervergunning, Ligplaatsontheffing) zonder gemeenschappelijk supertype. Op de proceskant bestaat VOMAanvraagOfMelding, maar dat betreft de aanvraag, niet het verleende recht. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
