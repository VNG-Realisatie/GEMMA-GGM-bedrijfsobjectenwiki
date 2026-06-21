---
type: bedrijfsobject
naam: Stil gebied
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
gemma_definitie: "Afgebakend gebied in de gemeente dat de gemeente beschermt vanwege de relatieve rust en afwezigheid van nadrukkelijk omgevingsgeluid."
bedrijfsprocessen: [actieplan geluid, geluidkartering, ruimtelijke planvorming]
bedrijfsfuncties: [milieubeheer, groenbeheer, ruimtelijke ordening]
relaties:
  - type: associatie
    bedrijfsobject: "[[Geluidgevoelig gebouw]]"
    richting: "naar-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Geluidgevoelige gebouwen profiteren van stille gebieden
  - type: associatie
    bedrijfsobject: "[[Geluidbron]]"
    richting: "van-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Stille gebieden worden bedreigd door geluidbronnen
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen het domein | Ja — bescherming van stille gebieden is expliciet beleidsdoel |
| Herkenbaar voor domeinexperts | Ja — wettelijk begrip uit EU-richtlijn omgevingslawaai, gebruikt in actieplannen |
| Eigen bestaan | Ja — een stil gebied bestaat onafhankelijk als afgebakend gebied met eigen kwaliteiten |
| Meervoud | Ja — de gemeente heeft meerdere stille gebieden (parken, hofjes, groengebieden) |
| Eigen levenscyclus | Ja — worden aangewezen, beschermd, uitgebreid of kunnen hun status verliezen |
| Relaties | Ja — met geluidbronnen, geluidgevoelige gebouwen, actieplannen |

## Beschrijving

Een stil gebied is een afgebakend gebied in de gemeente dat de gemeente koestert vanwege de relatieve rust. Stilte in een stad is geen absolute stilte maar de afwezigheid van nadrukkelijke omgevingsgeluiden zoals verkeer. De gemeente hanteert de aanpak "koesteren, verbeteren en uitbreiden" voor stille gebieden.

De ambitie is dat iedereen binnen 10 minuten loopafstand van huis een stil gebied kan bereiken. Stille gebieden dragen bij aan gezondheid (herstel van stress), biodiversiteit (schuil- en rustplaatsen voor dieren) en leefbaarheid.

Stille hofjes in de binnenstad kennen aanvullende bescherming: geen terrassen, 10 dB lagere geluidnormen voor bedrijven dan de standaardwaarde.

> "We koesteren plekken waar het stil of rustig is. [...] We streven ernaar dat iedereen binnen 10 minuten loopafstand van huis een stil gebied zoals een park of hofje kan vinden." (Beleidsnota, samenvatting)

De EU-richtlijn omgevingslawaai verplicht gemeenten om in actieplannen aandacht te besteden aan stille gebieden. De gemeente combineert dit met soundscaping: het verbeteren van de geluidsbeleving door logische ordening van functies en inzet van groen.

## Procesbron

Artefact dat in het EU-geluidbeleid en het gemeentelijke actieplan centraal staat. Het GGM modelleert fysieke terreinen en groenvoorzieningen maar niet de beleidsmatige aanduiding als "stil gebied" met bijbehorende beschermingsregime. Zie [[Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen|Beleidsnota Geluid en Trillingen]].

## Relaties

- Bedreigd door → [[Geluidbron]] (bronnen bepalen of een gebied stil kan zijn/blijven)
- Beschermt → [[Geluidgevoelig gebouw]] (gebouwen nabij stille gebieden profiteren)

## Terugmelding GGM

Potentieel hiaat: het GGM kent terreindelen en groenvoorzieningen, maar niet de aanduiding "stil gebied" als beleidsobject met beschermingsregime. Het is de vraag of dit een apart dataobject is of een attribuut op bestaande gebiedsentiteiten.
