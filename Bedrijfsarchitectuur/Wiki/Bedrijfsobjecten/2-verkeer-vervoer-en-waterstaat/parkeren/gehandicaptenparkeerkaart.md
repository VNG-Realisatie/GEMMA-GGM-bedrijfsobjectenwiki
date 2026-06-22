---
type: bedrijfsobject
naam: Gehandicaptenparkeerkaart
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "procesobject"
ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
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
gemma_definitie: "Europese kaart die het recht geeft om te parkeren op gehandicaptenparkeerplaatsen, uitgegeven door de gemeente op basis van medisch advies."
gemma_toelichting: "De GPK wordt uitgegeven als bestuurderskaart, passagierskaart, combinatiekaart of instellingskaart. Maximale geldigheid is 5 jaar. In Utrecht geldt dat GPK-houders gratis mogen parkeren in de openbare ruimte."
gemma_subtypes:
  - naam: "Bestuurderskaart"
    omschrijving: "GPK voor een bestuurder met loopbeperking"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: "Passagierskaart"
    omschrijving: "GPK voor een passagier die niet zelf rijdt"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: "Combinatiekaart"
    omschrijving: "GPK voor zowel bestuurder als passagier"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
  - naam: "Instellingskaart"
    omschrijving: "GPK voor een zorginstelling"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
bronnen: [Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid]
relaties:
  - type: associatie
    bedrijfsobject: "[[Gehandicaptenparkeerplaats]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: GPK geeft recht tot gebruik van gehandicaptenparkeerplaatsen
  - type: associatie
    bedrijfsobject: "[[Parkeervergunning]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: In Utrecht wordt een gratis parkeervergunning gekoppeld aan een GPK
  - type: associatie
    bedrijfsobject: "[[Voertuig]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: GPK (bestuurderskaart) is gekoppeld aan een voertuig
bedrijfsprocessen: [Gehandicaptenparkeerkaart aanvragen, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid, Vergunningverlening]
---

# Gehandicaptenparkeerkaart

Europese kaart die het recht geeft om te parkeren op gehandicaptenparkeerplaatsen, uitgegeven door de gemeente op basis van medisch advies.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — centraal document in het toegankelijkheidsbeleid
- ✅ Is herkenbaar voor domeinexperts — Europese standaard, elke parkeermedewerker kent het
- ✅ Heeft een eigen bestaan — zelfstandig document, onafhankelijk van parkeerplaats of vergunning
- ✅ Kan in meervoud bestaan — duizenden GPK's in Utrecht
- ✅ Heeft een eigen levenscyclus — aanvraag → medisch advies → uitgifte → verlenging (max 5 jaar) → intrekking
- ✅ Heeft relaties — met persoon, voertuig, parkeervergunning, gehandicaptenparkeerplaats

## Beschrijving

De Gehandicaptenparkeerkaart (GPK) is een Europees document waarmee mensen met een loopbeperking (maximaal 100 meter kunnen overbruggen) mogen parkeren op alle gehandicaptenparkeerplaatsen in de Europese Unie. De gemeente geeft de kaart uit op basis van medisch advies van een arts.

In Utrecht geldt dat GPK-houders gratis mogen parkeren op reguliere betaalde parkeerplekken in de openbare ruimte. Hiervoor krijgen zij een gratis [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning|parkeervergunning]]. Utrecht werkt aan het landelijk delen van GPK-parkeerrechten tussen gemeenten.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Bestuurderskaart | GPK voor een bestuurder met loopbeperking | — |
| Passagierskaart | GPK voor een passagier die niet zelf rijdt | — |
| Combinatiekaart | GPK voor zowel bestuurder als passagier | — |
| Instellingskaart | GPK voor een zorginstelling | — |

## Procesbron

Dit BO heeft geen GGM-grondslag. Het ontstaat in het proces "Gehandicaptenparkeerkaart aanvragen" op basis van de landelijke regelgeving (Reglement Verkeersregels en Verkeerstekens, artikel 85) en het VN-verdrag Handicap (2016).

Bron: [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid|Uitwerking Parkeren en toegankelijkheid]]

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerplaats|Gehandicaptenparkeerplaats]] — GPK geeft recht tot gebruik
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning|Parkeervergunning]] — in Utrecht wordt gratis parkeervergunning aan GPK gekoppeld
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig|Voertuig]] — bestuurderskaart gekoppeld aan kenteken

## Terugmelding GGM

> **Gehandicaptenparkeerkaart (GPK)** — Europees document dat gemeenten uitgeven op basis van medisch advies, met eigen levenscyclus (aanvraag, uitgifte, verlenging, intrekking) en relaties naar persoon, voertuig en parkeerrechten. Past in GGM beleidsdomein Parkeren als zelfstandige entiteit. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
