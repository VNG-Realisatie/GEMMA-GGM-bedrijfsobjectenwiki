---
type: domein
naam: Mobiliteit
status: in-behandeling
verwerkingsdatum: 2026-06-21
bronnen_count: 12
begrippen_count: 57
bo_count: 29
---

# Mobiliteit

Het mobiliteitsdomein omvat verkeer en vervoer van personen en goederen, gericht op het faciliteren van efficiënte en duurzame mobiliteit in de gemeente. Dit domein dekt GGM-taakveld "2 Verkeer, Vervoer en Waterstaat" met de beleidsdomeinen Mobiliteit en Parkeren.

## Begrippentabel

### Voetganger

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/voetgangersgebied]] | object | Aangewezen gebied waar de voetganger hoofdgebruiker is en gemotoriseerd verkeer beperkt is | ✅ | ja | 6/6 criteria; meervoud (binnenstad, USP, LRC), eigen levenscyclus, relaties met verkeersbesluiten | Binnenstad Utrecht, Utrecht Science Park | nee (hiaat) |
| voetgangersnetwerk | instrument | Fijnmazig netwerk van looproutes per wijk en op stedelijk niveau | ❌ | nee | Beleidskader/planningsconcept, geen zelfstandig object | Wijknetwerk Overvecht, stedelijk netwerk | nee |

### Fiets

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/hoofdfietsroute]] | object | Aangewezen fietsroute met kwaliteitseisen in het stedelijk hoofdfietsnetwerk | ✅ | ja | 6/6 criteria; fijnmazig netwerk, eigen levenscyclus, relaties met knooppunten | Route Vredenburg, route 'om de noord' | nee |
| snelfietsroute | object | Regionale fietsroute voor langere afstanden | ❌ | ja | Subtype van Hoofdfietsroute, provinciale verantwoordelijkheid | Van Dam tot Dom, route naar Woerden | nee |
| fietsenstalling | object | Voorziening voor het stallen van fietsen | ❌ | ja | Reeds in GGM als Fietsparkeervoorziening (BOR) | Stationsplein, inpandige stallingen | ja (BOR) |

### OV

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-knooppunt]] | object | Multimodaal overstappunt op kruising van wiel- en spaakverbindingen | ✅ | ja | 6/6 criteria; benoemde locaties, eigen levenscyclus, relaties | Overvecht, Lunetten-Koningsweg, USP | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-lijn]] | object | Tram- of buslijn met dienstregeling, route en frequentie | ✅ | ja | 6/6 criteria; meervoud, eigen levenscyclus | Uithoflijn, Merwedelijn, buslijn 28 | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte]] | object | Fysieke OV-voorziening waar reizigers in- en uitstappen | ✅ | ja | 6/6 criteria; meervoud, eigen levenscyclus, relaties met OV-lijnen | Halte Vaartsche Rijn, CS Centrumzijde | nee |
| Wiel met Spaken | instrument | Netwerkconcept voor OV-structuur met ring en radiale verbindingen | ❌ | nee | Beleidsvisie/structuurconcept; geen meervoud, niet operationeel door gemeente beheerd | — | nee |

### Multimodaal

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/p-r-locatie]] | object | Parkeer-en-reisvoorziening voor overstap auto naar OV/fiets | ✅ | ja | 6/6 criteria; benoemde locaties, eigen levenscyclus | P+R Westraven, P+R USP | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/mobiliteitshub]] | object | Multimodaal overstappunt met deelvoertuigen en voorzieningen | ✅ | ja | 6/6 criteria; meervoud, eigen levenscyclus, relaties | Hub Papendorp XL, buurthub | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laadpaal]] | object | Oplaadvoorziening voor elektrische voertuigen in de openbare ruimte | ✅ | ja | 6/6 criteria; meervoud, eigen levenscyclus | Laadpaal Laan van Soestbergen | nee |
| deelvoertuig | object | Gedeeld vervoermiddel (auto, fiets, scooter) | ❌ | ja | Eigendom/beheer bij private partij; gemeente vergunningverleent | Deelauto, deelfiets, e-scooter | nee |
| MaaS | instrument | Mobility as a Service — dienstverleningsconcept voor multimodale reis | ❌ | nee | 3/6 criteria; concept zonder meervoud, eigen levenscyclus of operationeel beheer | MaaS-app Gaiyo | nee |

### Goederenvervoer

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route]] | object | Voorkeursroute voor goederenvervoer met kwaliteitseisen | ✅ | ja | 6/6 criteria; meervoud (I/II), 3-jaarlijkse update, relaties | Franciscusdreef (I), Zamenhofdreef (II) | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laad-en-losplaats]] | object | Aangewezen locatie voor het laden en lossen van goederen | ✅ | ja | 6/6 criteria; meervoud, eigen levenscyclus | Binnenstad, winkelcentra | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/stadsdistributiepunt]] | object | Overslaglocatie voor bundeling en distributie van goederen naar de stad | ✅ | ja | 6/6 criteria; benoemde locaties, eigen functie | Lage Weide, Liesbosch, Laagraven | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/zero-emissiezone]] | object | Aangewezen zone waar alleen emissieloze voertuigen mogen opereren | ✅ | ja | 6/6 criteria; eigen levenscyclus (2025-2030), relaties | Binnenstad Utrecht (2025) | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/overslagpunt]] | object | Locatie voor overslag van goederen tussen weg, water en/of spoor | ✅ | ja | 6/6 criteria; meervoud, eigen levenscyclus | Zeehavenkade, Grifthoek | nee |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/bouwlogistiek-centrum]] | object | Hub voor gebundelde aanvoer van bouwmaterialen en -personeel | ✅ | ja | 6/6 criteria; meervoud, eigen levenscyclus (tijdelijk) | — | nee |
| Kwaliteitsnet Goederenvervoer | instrument | Samenhangend routenetwerk met kwaliteitseisen voor goederenvervoer | ❌ | nee | Instrument, herbeoordeeld: 4/6 criteria; faalt op meervoud (één netwerk per regio). Individuele routes zijn reeds BO (Logistieke Route) | — | nee |
| venstertijd | regel | Tijdvenster waarbinnen bevoorrading is toegestaan | ❌ | nee | Eigenschap van een zone/locatie, geen zelfstandig object | Ochtend venstertijd binnenstad | nee |

### Auto en verkeersmanagement

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| stedelijke verbindingsweg | classificatie | Wegcategorie voor hoofdroutes naar wijken en Ring | ❌ | ja | Classificatie op bestaand Wegdeel (GGM BOR), geen apart object | Europalaan, Cartesiusweg | ja (BOR) |
| stadsboulevard | classificatie | Herinrichtingsconcept voor stedelijke verbindingswegen (50 km/u) | ❌ | nee | Eigenschap/inrichtingsvorm van bestaande weg | 't Goylaan, Brailledreef | nee |
| doseerlocatie | locatie | Punt waar autoverkeer wordt gedoseerd richting Ring | ❌ | nee | Operationele maatregel op bestaand kruispunt | Toegang 't Goylaan | nee |
| compartimenteringszone | instrument | Gebiedsindeling binnenstad waar doorgaand autoverkeer wordt geweerd | ❌ | nee | 4/6 criteria; verkeersmanagementstrategie, geen zelfstandig geregistreerd object; wordt geëffectueerd via Verkeersbesluiten | Binnenstad oost/west | nee |

### Parkeren (GGM-verificatie)

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerzone]] | object | Afgebakend gebied met specifieke parkeerregels | ✅ | ja | GGM: bevestigd — betaald parkeren, zones A1/A2/B1/B2/C1/C2, uitbreiding tot 2034 | Zone Binnenstad, zone Lombok | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeergarage]] | object | Gebouwde parkeervoorziening | ✅ | ja | GGM: bevestigd — binnenstadsgarages, P+R-garages, loopafstanden per zone | Jaarbeurs, Springweg | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning]] | object | Toestemming om op bepaalde plek te parkeren | ✅ | ja | GGM: bevestigd — bewoners-/bezoekers-/bedrijfsvergunning, plafond per gebied, geen recht bij bouwontwikkeling | Bewonersvergunning, bezoekersvergunning | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht]] | object | Recht om te parkeren onder bepaalde voorwaarden | ✅ | ja | GGM: bevestigd — betaald parkeren, GPK-houders gratis | Dagtarief, uurtarief | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervlak]] | object | Parkeergelegenheid langs de weg | ✅ | ja | GGM: bevestigd — jaarlijks 0,5-1% opheffen, transformatie naar groen | Straatparkeerplaats | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerscan]] | object | Waarneming van parkeeractie door scanauto | ✅ | ja | GGM: bevestigd — digitale handhaving op kenteken | Scanresultaat | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig]] | object | Vervoermiddel voor wegverkeer | ✅ | ja | GGM: bevestigd — onderscheid elektrisch/fossiel relevant | Auto, bestelbus | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/naheffing]] | object | Achteraf vordering te weinig betaalde belasting | ✅ | ja | GGM: operationeel relevant | Parkeernaheffing | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/mulderfeit]] | object | Administratieve parkeerovertreding (WAHV) | ✅ | ja | GGM: operationeel relevant | Parkeerboete | ja |
| Belprovider | object | Leverancier van mobiele beldiensten voor parkeren | ❌ | ja | Te technisch/operationeel, geen herkenbaar bedrijfsobject | — | ja |
| Productgroep | classificatie | Groepering van parkeerproducten | ❌ | ja | Administratieve classificatie | — | ja |
| Productsoort | classificatie | Typologie van parkeerproduct | ❌ | ja | Administratieve classificatie | — | ja |
| Straatsectie | classificatie | Gedeelte van een straat voor parkeerbeheer | ❌ | ja | Administratieve indeling, geen zelfstandig object | — | ja |

### Parkeren (parkeerbeleid)

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerkaart]] | object | Europese kaart voor parkeren op gehandicaptenparkeerplaatsen | ✅ | ja | 6/6 criteria; eigen levenscyclus (aanvraag→uitgifte→verlenging→intrekking), relaties met persoon, voertuig, vergunning | GPK bestuurder, GPK passagier | nee (hiaat) |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerplaats]] | object | Parkeerplaats gereserveerd voor GPK-houders | ✅ | ja | 6/6 criteria; specialisatie Parkeervlak met eigen processen, beleidsregel, sensoren, kentekenkoppeling | Algemene GPP binnenstad, individuele GPP op kenteken | partieel (Parkeervlak.doelgroep) |
| Parkeernorm | regel | Minimum-/maximumnorm voor parkeerplaatsen per zone en functie | ❌ | nee | Beleidsregel/referentiedata, geen zelfstandig object | Norm woning A-gebied: 0,78 auto | nee |
| Deelautoplek | object | Gereserveerde parkeerplaats voor deelauto's met exploitatie-eisen | ❌ | ja | Subtype/eigenschap van Parkeervlak, beperkt als zelfstandig BO | Deelautoplek Papendorp | nee |
| Bereikbaarheidsfonds | instrument | Financieel instrument: bijdrage per niet-aangelegde parkeerplaats | ❌ | nee | 3/6 criteria; financieel mechanisme, geen meervoud, geen eigen levenscyclus als object | — | nee |
| Mobiliteitsbeheerplan | document | Verplicht document bij bouwontwikkelingen over mobiliteitsorganisatie | ❌ | nee | Procesdocument in vergunningenproces, niet zelfstandig herkenbaar als BO | Mobiliteitsbeheerplan woningbouw | nee |
| Fietsdepot | locatie | Opslaglocatie voor verwijderde fietsen | ❌ | ja | Operationele locatie, geen zelfstandig BO | — | nee |
| Fietsparkeerverbodzone | zone | Aangewezen zone waar fietsen alleen in vakken/stallingen mogen | ❌ | ja | Eigenschap van locatie/zone, geen zelfstandig object | Binnenstad | nee |
| Betaald parkeergebied | zone | Gebied waar parkeren gereguleerd is met tarief of vergunning | ❌ | ja | Eigenschap van bestaand BO Parkeerzone | Betaald parkeren Lombok | ja (Parkeerzone) |
| Mobiliteitslabel | product | Informatieproduct dat per adres parkeervoorzieningen toont | ❌ | nee | Informatieproduct, geen zelfstandig object | — | nee |
| Maatwerklocatie | aanwijzing | Aangewezen gebied met parkeerplafond en extra flexibiliteit | ❌ | nee | Beleidsaanwijzing, eigenschap van zone | Papendorp, Merwede | nee |

### Verkeersmanagement (GGM-verificatie)

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/verkeersbesluit]] | object | Besluit over plaatsen/wijzigen verkeersteken of fysieke maatregel | ✅ | ja | GGM: bevestigd — 30 km/u-invoering, compartimentering | Instellen 30-zone, eenrichtingsverkeer | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/stremming]] | object | Blokkering doorstroming wegverkeer door incident | ✅ | ja | GGM: niet specifiek in Mobiliteitsplan maar operationeel relevant | Wegafsluiting, incident | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/verkeerstelling]] | object | Onderzoek naar verkeershoeveelheid en -verdeling | ✅ | ja | GGM: bevestigd — monitoring genoemd in §11 | Fietstelling, autotelling | ja |
| VLogInfo | object | Datalogging verkeersregelinstallatie | ❌ | ja | Te technisch/operationeel voor bedrijfsniveau | — | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/strooiroute]] | object | Traject voor gladheidsbestrijding | ✅ | ja | GGM: niet in Mobiliteitsplan maar operationeel relevant | Winterdienstroute | ja |
| Strooidag | object | Dag waarop gestrooid wordt | ❌ | ja | Te operationeel, onderdeel van gladheidsbestrijdingsproces | — | ja |
| StrooirouteUitvoering | object | Werkelijk gevolgde strooiroute | ❌ | ja | Te operationeel, uitvoeringsniveau | — | ja |

## GGM-entiteitendekking

| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Mobiliteit | 11 | 4 | 7 | 0 | — |
| Parkeren | 15 | 9 | 6 | 0 | — |

### GGM-dekkingsanalyse

**Mobiliteit**: het GGM modelleert uitsluitend verkeersmanagement — stremmingen, gladheidsbestrijding, verkeersbesluiten en verkeerstellingen. De functionele mobiliteitslaag ontbreekt volledig: geen routes, knooppunten, haltes, zones of logistieke voorzieningen. Dit is een structureel hiaat. Alle 14 nieuwe BO-kandidaten uit het Mobiliteitsplan (inclusief Voetgangersgebied) vallen buiten de huidige GGM-scope.

**Parkeren**: goed uitgewerkt met 13 entiteiten die het volledige parkeerbeheerproces dekken (zones, vlakken, rechten, vergunningen, handhaving). Alle kernentiteiten bevestigd door parkeerbeleidsbronnen. Twee hiaten geïdentificeerd: [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerkaart|Gehandicaptenparkeerkaart (GPK)]] ontbreekt als entiteit, en [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerplaats|Gehandicaptenparkeerplaats]] wordt slechts als attribuut `doelgroep` op Parkeervlak gedekt, terwijl het eigen processen en beleidsregel heeft. Aanvulling nodig voor laadinfrastructuur ([[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laadpaal]]).

**BOR-overlap**: fysieke assets (Wegdeel, Fietsparkeervoorziening, Verkeerslicht, Brug) zijn gemodelleerd in het BOR-domein (taakveld 8). De mobiliteitslaag bouwt hier functioneel bovenop — een [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route]] is een aanduiding op bestaande Wegdelen, een [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte]] is een functionele locatie op de openbare ruimte.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007|Kwaliteitsnet Goederenvervoer 2007]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-fiets-2021|Beleidsregel parkeernormen fiets 2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-auto-2021|Beleidsregel parkeernormen auto 2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/module-parkeernormen|Module Parkeernormen fiets en auto]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeerhubs|Uitwerking Parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/rapportage-routekaart-parkeerhubs|Routekaart Parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-fietsparkeren|Uitwerking Fietsparkeren]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeren-openbare-ruimte|Uitwerking Parkeren openbare ruimte]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid|Uitwerking Parkeren en toegankelijkheid]]
- [[Wiki/Bronsamenvattingen/mobiliteit/parkeervisie|Parkeervisie Utrecht]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitvoeringsprogramma-betaald-parkeren|Uitvoeringsprogramma betaald parkeren 2025-2028]]

## Nog te verwerken bronnen

Geen openstaande bronnen.

## Openstaande vragen of hiaten

- **Deelvoertuig**: gemeente introduceert vergunningenstelsel voor deelmobiliteit — wordt dit een registratieobject? Bij nadere uitwerking opnieuw beoordelen.
- **P+R vs. Parkeergarage**: overlap — P+R-locaties zijn deels parkeergarages maar met specifieke multimodale functie. Relatie vastleggen.
- **Bouwlogistiek Centrum**: tijdelijke voorzieningen — hoe modelleren als de levenscyclus per definitie eindig is?

## Terugmeldingen richting GGM

Alle 14 nieuwe BO-kandidaten uit het Mobiliteitsplan zijn potentiële GGM-hiaten. Ze vallen in drie categorieën:

1. **Functionele mobiliteitslaag** (routes, knooppunten, haltes, hubs, voetgangersgebied) — dataobjecten die gemeenten beheren maar die het GGM niet modelleert
2. **Logistieke voorzieningen** (laad-/losplaatsen, stadsdistributiepunten, overslagpunten, zero-emissiezones) — specifiek voor goederenvervoer
3. **Verkeerszonering** (voetgangersgebied) — formeel aangewezen gebieden met specifieke verkeersregels

Uit de parkeerbeleidsbronnen komen twee aanvullende hiaten:

4. **Gehandicaptenparkeerkaart (GPK)** — Europees document met eigen levenscyclus, niet gemodelleerd in GGM Parkeren
5. **Gehandicaptenparkeerplaats** — specialisatie van Parkeervlak met eigen processen, beleidsregel en sensormonitoring; GGM dekt dit slechts als attribuut `doelgroep`

Zie [[Wiki/Analyses/ggm-terugmeldingen]] voor de volledige lijst.
