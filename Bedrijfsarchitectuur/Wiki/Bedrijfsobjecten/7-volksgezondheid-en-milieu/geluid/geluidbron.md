---
type: bedrijfsobject
naam: Geluidbron
domein: [geluid]
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
gemma_definitie: "Object dat geluid veroorzaakt in de leefomgeving, ingedeeld naar bronsoort zoals wegverkeer, railverkeer, industrieterrein of scheepvaart."
bedrijfsprocessen: [geluidkartering, maatregelenonderzoek, actieplan geluid]
bedrijfsfuncties: [milieubeheer, ruimtelijke ordening]
bronnen: [Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen]
relaties:
  - type: associatie
    bedrijfsobject: "[[Geluidgevoelig gebouw]]"
    richting: "naar-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Geluidbron belast geluidgevoelig gebouw
  - type: associatie
    bedrijfsobject: "[[Geluidscherm]]"
    richting: "naar-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Geluidscherm vermindert geluid van bron
  - type: associatie
    bedrijfsobject: "[[Geluidzone]]"
    richting: "van-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Industriële geluidbronnen liggen binnen een geluidzone
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen het domein | Ja — centraal concept in geluidbeleid; normen worden per bronsoort vastgesteld |
| Herkenbaar voor domeinexperts | Ja — geluidadviseurs en planologen werken dagelijks met geluidbronnen |
| Eigen bestaan | Ja — een geluidbron is een zelfstandig identificeerbaar object (weg, spoorlijn, bedrijf) |
| Meervoud | Ja — de gemeente beheert tientallen geluidbronnen per bronsoort |
| Eigen levenscyclus | Ja — bronnen ontstaan (aanleg weg), wijzigen (verkeersintensiteit) en verdwijnen (sluiting bedrijf) |
| Relaties | Ja — met geluidgevoelige gebouwen, geluidzones, geluidschermen, actieplannen |

## Beschrijving

Een geluidbron is elk object dat geluid veroorzaakt in de leefomgeving. De Beleidsnota Geluid en Trillingen onderscheidt vijf bronsoorten: gemeentelijk wegverkeer, rijks- en provinciale wegen, railverkeer, industrieterreinen en scheepvaart. Per bronsoort gelden eigen standaardwaarden, ambitiewaarden en grenswaarden.

De gemeente berekent elke vijf jaar de geluidbelasting per bron via geluidkartering (EU-richtlijn omgevingslawaai). Bij nieuwe ruimtelijke ontwikkelingen wordt per geluidbron beoordeeld of de grenswaarden worden overschreden en welke maatregelen nodig zijn (bronmaatregelen zoals stil asfalt of snelheidsverlaging, of overdrachtsmaatregelen zoals schermen).

> "Geluidbeperkende maatregelen worden in aanmerking genomen als die financieel doelmatig zijn en er geen overwegende bezwaren van stedenbouwkundige, verkeerskundige, vervoerskundige, landschappelijke of technische aard bestaan." (Beleidsnota §1.1)

## Procesbron

Artefact dat in het geluidbeleid en de geluidkartering centraal staat. Het GGM modelleert fysieke objecten (wegen, spoorlijnen) maar niet hun classificatie als geluidbron met bijbehorende normen en bronsoort. Zie [[Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen|Beleidsnota Geluid en Trillingen]].

## Relaties

- Belast → [[Geluidgevoelig gebouw]] (geluid raakt gevels van gevoelige gebouwen)
- Afgeschermd door → [[Geluidscherm]] (scherm vermindert overdracht)
- Binnen → [[Geluidzone]] (industriële bronnen liggen binnen een zone)
- Nabij → [[Stil gebied]] (bronnen bepalen of een gebied stil kan zijn)

## Terugmelding GGM

Potentieel hiaat: het GGM modelleert wegen en spoorlijnen als fysieke objecten, maar niet hun classificatie als geluidbron met bronsoort en bijbehorende normen. Nader te beoordelen of dit een dataobject is of een beleidsmatige classificatie van bestaande objecten.
