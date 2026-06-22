---
type: bedrijfsobject
naam: Groenobject
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Groenobject"
ggm_guid: EAID_B4935E75_46CA_414D_949D_30A8B801FD5
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: [EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3]
ggm_definitie: "Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten vegetatie."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Groenobject"
ggm_gemma_guid: "360b8000-41ce-453f-bed8-b0cc7fa21164"
ggm_gemma_definitie: "Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten vegetatie."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-360b8000-41ce-453f-bed8-b0cc7fa21164"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Afgebakend stuk terrein met aaneengesloten vegetatie dat de gemeente beheert als onderdeel van de stedelijke groenstructuur."
bedrijfsprocessen: [Groenbeheer, Groencompensatie, Toetsing omgevingsvergunning, Meerjarengroenprogramma]
bedrijfsfuncties: [Groenbeheer, Openbare ruimte, Ruimtelijke ordening]
relaties:
  - type: generalisatie
    bedrijfsobject: Beheerobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit: 
    beschrijving: Groenobject is een specialisatie van Beheerobject
  - type: associatie
    bedrijfsobject: "[[Boom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een groenobject kan meerdere bomen bevatten
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Kernobject van het groenbeleid; visiekaart definieert welke groenobjecten beschermd zijn |
| Herkenbaar voor domeinexperts | ✅ | Groenbeheerders, stedenbouwkundigen en ecologen werken dagelijks met groenobjecten |
| Heeft eigen bestaan | ✅ | Fysiek afgebakend terrein met vegetatie, onafhankelijk van processen |
| Kan in meervoud bestaan | ✅ | Duizenden groenobjecten in de gemeente geregistreerd (parken, plantsoenen, gazons, hagen) |
| Heeft eigen levenscyclus | ✅ | Aanleg → inrichting → beheer → herinrichting → eventueel verwijdering |
| Heeft relaties met andere concepten | ✅ | Bevat [[Boom\|bomen]], ligt in de groenstructuur, is onderdeel van beheergebied |

**Conclusie:** 6/6 criteria van toepassing. Groenobject is een bedrijfsobject.

## Beschrijving

Een Groenobject is een afgebakend stuk terrein met aaneengesloten vegetatie dat de gemeente beheert. Het varieert van kleine groenstroken en hagen tot grote stadsparken en landgoederen. De gemeente Utrecht beheert groenobjecten als onderdeel van de stedelijke groenstructuur, die is vastgelegd op de visiekaart van het Groenstructuurplan.

Groenobjecten worden op verschillende niveaus beheerd:
- **Operationeel**: maaifrequentie, snoeischema, ecologisch beheer
- **Tactisch**: kwaliteitsniveau actueel en gewenst, beplantingsplan
- **Strategisch**: bescherming via de groenstructuur, groencompensatie bij aantasting

Sinds de actualisatie van het Groenstructuurplan (2018) worden groenobjecten ook beoordeeld op hun bijdrage aan gezonde verstedelijking en klimaatadaptatie (verkoeling, waterberging, biodiversiteit).

## GGM-bron

> "Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten vegetatie."

- **Entiteit:** Groenobject
- **Beleidsdomein:** Beheer Openbare Ruimte
- **Overerving:** specialisatie van Beheerobject
- **Matchsterkte:** exact
- **Attributen:** aantalObstakels, bereikbaarheid, bergendVermogen, cultuurhistorischWaardevol, ecologischBeheer, herplantplicht, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, maaifrequentie, objectnummer, oppervlakte, type, typePlus, typePlus2, veiligheidsklasseBoom (46 attributen totaal)

Het attribuut `cultuurhistorischWaardevol` weerspiegelt de cultuurhistorische samenhang die het Groenstructuurplan beschrijft. Het attribuut `ecologischBeheer` sluit aan bij de Nature Based Solutions uit de actualisatie.

## BO-definitie

De GGM-definitie richt zich op het technische niveau (NEN 3610 objecttype Terrein). De GEMMA-definitie legt de nadruk op het beheerperspectief van de gemeente en de beleidscontext van de groenstructuur.

## Relaties

| Gerelateerd BO | Type | Richting | Beschrijving |
|---|---|---|---|
| [[Boom]] | associatie | naar-dit-BO | Een groenobject kan meerdere bomen bevatten |
| Beheerobject (GGM) | generalisatie | van-dit-BO | Groenobject erft beheerattributen (status, eigenaar, gemeente, wijk) |

## Bedrijfsprocessen

- **Groenbeheer** — dagelijks onderhoud, maaien, snoeien, ecologisch beheer
- **Groencompensatie** — bij aantasting van de groenstructuur moet elders groen worden gerealiseerd
- **Toetsing omgevingsvergunning** — gemeente toetst of een plan in de groenstructuur ligt (visiekaart)
- **Meerjarengroenprogramma** — jaarlijkse programmering van groeninvesteringen

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
