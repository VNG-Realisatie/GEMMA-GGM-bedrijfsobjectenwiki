---
type: domein
naam: Mobiliteit
status: in-behandeling
verwerkingsdatum: 2026-06-20
bronnen_count: 2
begrippen_count: 30
bo_count: 26
---

# Mobiliteit

Het mobiliteitsdomein omvat verkeer en vervoer van personen en goederen, gericht op het faciliteren van efficiënte en duurzame mobiliteit in de gemeente. Dit domein dekt GGM-taakveld "2 Verkeer, Vervoer en Waterstaat" met de beleidsdomeinen Mobiliteit en Parkeren.

## Begrippentabel

### Fiets

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[Hoofdfietsroute]] | object | Aangewezen fietsroute met kwaliteitseisen in het stedelijk hoofdfietsnetwerk | ✅ | 6/6 criteria; fijnmazig netwerk, eigen levenscyclus, relaties met knooppunten | Route Vredenburg, route 'om de noord' | nee |
| snelfietsroute | object | Regionale fietsroute voor langere afstanden | ❌ | Subtype van Hoofdfietsroute, provinciale verantwoordelijkheid | Van Dam tot Dom, route naar Woerden | nee |
| fietsenstalling | object | Voorziening voor het stallen van fietsen | ❌ | Reeds in GGM als Fietsparkeervoorziening (BOR) | Stationsplein, inpandige stallingen | ja (BOR) |

### OV

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[OV-knooppunt]] | object | Multimodaal overstappunt op kruising van wiel- en spaakverbindingen | ✅ | 6/6 criteria; benoemde locaties, eigen levenscyclus, relaties | Overvecht, Lunetten-Koningsweg, USP | nee |
| [[OV-lijn]] | object | Tram- of buslijn met dienstregeling, route en frequentie | ✅ | 6/6 criteria; meervoud, eigen levenscyclus | Uithoflijn, Merwedelijn, buslijn 28 | nee |
| [[Halte]] | object | Fysieke OV-voorziening waar reizigers in- en uitstappen | ✅ | 6/6 criteria; meervoud, eigen levenscyclus, relaties met OV-lijnen | Halte Vaartsche Rijn, CS Centrumzijde | nee |
| Wiel met Spaken | instrument | Netwerkconcept voor OV-structuur met ring en radiale verbindingen | ❌ | Beleidsinstrument, niet een zelfstandig object | — | nee |

### Multimodaal

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[P+R-locatie]] | object | Parkeer-en-reisvoorziening voor overstap auto naar OV/fiets | ✅ | 6/6 criteria; benoemde locaties, eigen levenscyclus | P+R Westraven, P+R USP | nee |
| [[Mobiliteitshub]] | object | Multimodaal overstappunt met deelvoertuigen en voorzieningen | ✅ | 6/6 criteria; meervoud, eigen levenscyclus, relaties | Hub Papendorp XL, buurthub | nee |
| [[Laadpaal]] | object | Oplaadvoorziening voor elektrische voertuigen in de openbare ruimte | ✅ | 6/6 criteria; meervoud, eigen levenscyclus | Laadpaal Laan van Soestbergen | nee |
| deelvoertuig | object | Gedeeld vervoermiddel (auto, fiets, scooter) | ❌ | Eigendom/beheer bij private partij; gemeente vergunningverleent | Deelauto, deelfiets, e-scooter | nee |
| MaaS | instrument | Mobility as a Service — dienstverleningsconcept voor multimodale reis | ❌ | Dienstverleningsconcept, geen zelfstandig object | MaaS-app Gaiyo | nee |

### Goederenvervoer

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[Logistieke Route]] | object | Voorkeursroute voor goederenvervoer met kwaliteitseisen | ✅ | 6/6 criteria; meervoud (I/II), 3-jaarlijkse update, relaties | Franciscusdreef (I), Zamenhofdreef (II) | nee |
| [[Laad- en Losplaats]] | object | Aangewezen locatie voor het laden en lossen van goederen | ✅ | 6/6 criteria; meervoud, eigen levenscyclus | Binnenstad, winkelcentra | nee |
| [[Stadsdistributiepunt]] | object | Overslaglocatie voor bundeling en distributie van goederen naar de stad | ✅ | 6/6 criteria; benoemde locaties, eigen functie | Lage Weide, Liesbosch, Laagraven | nee |
| [[Zero-emissiezone]] | object | Aangewezen zone waar alleen emissieloze voertuigen mogen opereren | ✅ | 6/6 criteria; eigen levenscyclus (2025-2030), relaties | Binnenstad Utrecht (2025) | nee |
| [[Overslagpunt]] | object | Locatie voor overslag van goederen tussen weg, water en/of spoor | ✅ | 6/6 criteria; meervoud, eigen levenscyclus | Zeehavenkade, Grifthoek | nee |
| [[Bouwlogistiek Centrum]] | object | Hub voor gebundelde aanvoer van bouwmaterialen en -personeel | ✅ | 6/6 criteria; meervoud, eigen levenscyclus (tijdelijk) | — | nee |
| Kwaliteitsnet Goederenvervoer | instrument | Samenhangend routenetwerk met kwaliteitseisen voor goederenvervoer | ❌ | Beleidsinstrument (één netwerk), niet een object | — | nee |
| venstertijd | regel | Tijdvenster waarbinnen bevoorrading is toegestaan | ❌ | Eigenschap van een zone/locatie, geen zelfstandig object | Ochtend venstertijd binnenstad | nee |

### Auto en verkeersmanagement

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| stedelijke verbindingsweg | classificatie | Wegcategorie voor hoofdroutes naar wijken en Ring | ❌ | Classificatie op bestaand Wegdeel (GGM BOR), geen apart object | Europalaan, Cartesiusweg | ja (BOR) |
| stadsboulevard | classificatie | Herinrichtingsconcept voor stedelijke verbindingswegen (50 km/u) | ❌ | Eigenschap/inrichtingsvorm van bestaande weg | 't Goylaan, Brailledreef | nee |
| doseerlocatie | locatie | Punt waar autoverkeer wordt gedoseerd richting Ring | ❌ | Operationele maatregel op bestaand kruispunt | Toegang 't Goylaan | nee |

### Parkeren (GGM-verificatie)

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[parkeerzone]] | object | Afgebakend gebied met specifieke parkeerregels | ✅ | GGM: bevestigd door Mobiliteitsplan — betaald parkeren, uitbreiding | Zone Binnenstad, zone Lombok | ja |
| [[parkeergarage]] | object | Gebouwde parkeervoorziening | ✅ | GGM: bevestigd — binnenstadsgarages, P+R-garages | Jaarbeurs, Springweg | ja |
| [[parkeervergunning]] | object | Toestemming om op bepaalde plek te parkeren | ✅ | GGM: bevestigd — bewonersvergunning, nieuwe deelmobiliteitsvergunning | Bewonersvergunning, bezoekersvergunning | ja |
| [[parkeerrecht]] | object | Recht om te parkeren onder bepaalde voorwaarden | ✅ | GGM: bevestigd — betaald parkeren | Dagtarief, uurtarief | ja |
| [[parkeervlak]] | object | Parkeergelegenheid langs de weg | ✅ | GGM: bevestigd — transformatie naar groen/fietsstalling | Straatparkeerplaats | ja |
| [[parkeerscan]] | object | Waarneming van parkeeractie door scanauto | ✅ | GGM: bevestigd (impliciet via handhaving) | Scanresultaat | ja |
| [[voertuig]] | object | Vervoermiddel voor wegverkeer | ✅ | GGM: bevestigd — onderscheid elektrisch/fossiel relevant | Auto, bestelbus | ja |
| [[naheffing]] | object | Achteraf vordering te weinig betaalde belasting | ✅ | GGM: niet in Mobiliteitsplan maar operationeel relevant | Parkeernaheffing | ja |
| [[mulderfeit]] | object | Administratieve parkeerovertreding (WAHV) | ✅ | GGM: niet in Mobiliteitsplan maar operationeel relevant | Parkeerboete | ja |
| Belprovider | object | Leverancier van mobiele beldiensten voor parkeren | ❌ | Te technisch/operationeel, geen herkenbaar bedrijfsobject | — | ja |
| Productgroep | classificatie | Groepering van parkeerproducten | ❌ | Administratieve classificatie | — | ja |
| Productsoort | classificatie | Typologie van parkeerproduct | ❌ | Administratieve classificatie | — | ja |
| Straatsectie | classificatie | Gedeelte van een straat voor parkeerbeheer | ❌ | Administratieve indeling, geen zelfstandig object | — | ja |

### Verkeersmanagement (GGM-verificatie)

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[verkeersbesluit]] | object | Besluit over plaatsen/wijzigen verkeersteken of fysieke maatregel | ✅ | GGM: bevestigd — 30 km/u-invoering, compartimentering | Instellen 30-zone, eenrichtingsverkeer | ja |
| [[stremming]] | object | Blokkering doorstroming wegverkeer door incident | ✅ | GGM: niet specifiek in Mobiliteitsplan maar operationeel relevant | Wegafsluiting, incident | ja |
| [[verkeerstelling]] | object | Onderzoek naar verkeershoeveelheid en -verdeling | ✅ | GGM: bevestigd — monitoring genoemd in §11 | Fietstelling, autotelling | ja |
| VLogInfo | object | Datalogging verkeersregelinstallatie | ❌ | Te technisch/operationeel voor bedrijfsniveau | — | ja |
| [[strooiroute]] | object | Traject voor gladheidsbestrijding | ✅ | GGM: niet in Mobiliteitsplan maar operationeel relevant | Winterdienstroute | ja |
| Strooidag | object | Dag waarop gestrooid wordt | ❌ | Te operationeel, onderdeel van gladheidsbestrijdingsproces | — | ja |
| StrooirouteUitvoering | object | Werkelijk gevolgde strooiroute | ❌ | Te operationeel, uitvoeringsniveau | — | ja |

## GGM-entiteitendekking

| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Mobiliteit | 11 | 4 | 7 | 0 | — |
| Parkeren | 15 | 9 | 6 | 0 | — |

### GGM-dekkingsanalyse

**Mobiliteit**: het GGM modelleert uitsluitend verkeersmanagement — stremmingen, gladheidsbestrijding, verkeersbesluiten en verkeerstellingen. De functionele mobiliteitslaag ontbreekt volledig: geen routes, knooppunten, haltes, zones of logistieke voorzieningen. Dit is een structureel hiaat. Alle 13 nieuwe BO-kandidaten uit het Mobiliteitsplan vallen buiten de huidige GGM-scope.

**Parkeren**: goed uitgewerkt met 13 entiteiten die het volledige parkeerbeheerproces dekken (zones, vlakken, rechten, vergunningen, handhaving). Het Mobiliteitsplan bevestigt de relevantie van de kernentiteiten. Aanvulling nodig voor laadinfrastructuur ([[Laadpaal]]).

**BOR-overlap**: fysieke assets (Wegdeel, Fietsparkeervoorziening, Verkeerslicht, Brug) zijn gemodelleerd in het BOR-domein (taakveld 8). De mobiliteitslaag bouwt hier functioneel bovenop — een [[Logistieke Route]] is een aanduiding op bestaande Wegdelen, een [[Halte]] is een functionele locatie op de openbare ruimte.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007|Kwaliteitsnet Goederenvervoer 2007]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040]]

## Nog te verwerken bronnen

Geen openstaande bronnen.

## Openstaande vragen of hiaten

- **Deelvoertuig**: gemeente introduceert vergunningenstelsel voor deelmobiliteit — wordt dit een registratieobject? Bij nadere uitwerking opnieuw beoordelen.
- **P+R vs. Parkeergarage**: overlap — P+R-locaties zijn deels parkeergarages maar met specifieke multimodale functie. Relatie vastleggen.
- **Bouwlogistiek Centrum**: tijdelijke voorzieningen — hoe modelleren als de levenscyclus per definitie eindig is?

## Terugmeldingen richting GGM

Alle 13 nieuwe BO-kandidaten zijn potentiële GGM-hiaten. Ze vallen in twee categorieën:

1. **Functionele mobiliteitslaag** (routes, knooppunten, haltes, hubs) — dataobjecten die gemeenten registreren/beheren maar die het GGM niet modelleert
2. **Logistieke voorzieningen** (laad-/losplaatsen, stadsdistributiepunten, overslagpunten, zero-emissiezones) — specifiek voor goederenvervoer

Zie [[Wiki/Analyses/ggm-terugmeldingen]] voor de volledige lijst.
