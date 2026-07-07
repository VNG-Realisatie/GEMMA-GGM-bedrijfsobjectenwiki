---
type: analyse
titel: "Entiteitendekking: 2 Verkeer, Vervoer en Waterstaat"
datum: 2026-07-07
taakveld: "2 Verkeer, Vervoer en Waterstaat"
beleidsdomeinen:
  - Mobiliteit
  - Parkeren
totaal_entiteiten: 20
totaal_bo: 29
totaal_matches: 13
totaal_hiaten: 16
---

# Entiteitendekking: 2 Verkeer, Vervoer en Waterstaat

## Beoordeling

2 beleidsdomeinen, 20 GGM-entiteiten, volledige dekking (20/20, 100%) en geen "niet gedekt"-gevallen. De 7 entiteiten zonder eigen BO volgen een herkenbaar patroon: 3× classificatie (Productgroep, Productsoort, Straatsectie — administratieve typering/indeling van Parkeervergunning resp. Parkeervlak) en 4× detail (Strooidag, StrooirouteUitvoering, VLogInfo, Belprovider — uitvoerings- en sensordata die te operationeel/technisch zijn om als zelfstandig bedrijfsobject te gelden). Geen van deze entiteiten introduceert een functioneel hiaat; ze zijn allemaal terug te voeren op een bestaand BO.

Het opvallende patroon zit aan de andere kant: 16 BO's zonder GGM-entiteit tegenover slechts 13 matches — de grootste onbalans van alle taakvelden met 100% dekking. Vrijwel alle 16 zijn procesobjecten rond stedelijke mobiliteit en logistiek: OV- en fietsvoorzieningen (Halte, OV-lijn, OV-knooppunt, Hoofdfietsroute, P+R-locatie), laad- en overslaginfrastructuur (Laadpaal, Laad- en Losplaats, Overslagpunt, Stadsdistributiepunt, Mobiliteitshub, Logistieke Route, Bouwlogistiek Centrum) en twee governance-objecten voor mobiliteitstransitie (Voetgangersgebied, Zero-emissiezone). Dit wijst erop dat het GGM de klassieke verkeers- en parkeerprocessen (NDW/RDW-achtige gegevens: telling, stremming, vergunning, boete) goed dekt, maar de nieuwere beleidsthema's rond stadslogistiek, laadinfrastructuur en emissievrije zones nog niet heeft gemodelleerd. Dit zijn kandidaten om als hiaat aan het GGM-team terug te melden, al zijn het merendeel procesobjecten (geen data-objecten) waarvoor formele terugmelding minder dwingend is.

Er zijn in dit taakveld geen naamconflicten of hernoemingen gesignaleerd (kolom Naamoverlap is overal leeg); alle matches zijn exact.

## Mobiliteit

7 entiteiten, 4 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/mobiliteit\|Stremming]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/stremming\|Stremming]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/mobiliteit\|Strooiroute]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/strooiroute\|Strooiroute]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/mobiliteit\|Verkeersbesluit]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/verkeersbesluit\|Verkeersbesluit]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/mobiliteit\|Verkeerstelling]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/verkeerstelling\|Verkeerstelling]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/mobiliteit\|Strooidag]] | detail | via StrooirouteUitvoering → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/strooiroute\|Strooiroute]] | Te operationeel, onderdeel van gladheidsbestrijdingsproces |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/mobiliteit\|StrooirouteUitvoering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/strooiroute\|Strooiroute]] | Te operationeel, uitvoeringsniveau |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/mobiliteit\|VLogInfo]] | detail | via Sensor → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/verkeerstelling\|Verkeerstelling]] | Te technisch/operationeel voor bedrijfsniveau |

## Parkeren

13 entiteiten, 9 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|MulderFeit]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/mulderfeit\|MulderFeit]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Naheffing]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/naheffing\|Naheffing]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Parkeergarage]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeergarage\|Parkeergarage]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Parkeerrecht]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht\|Parkeerrecht]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Parkeerscan]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerscan\|Parkeerscan]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Parkeervergunning]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Parkeervlak]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervlak\|Parkeervlak]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Parkeerzone]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerzone\|Parkeerzone]] ✅ | — |  | Exact match |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Voertuig]] | [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig\|Voertuig]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Productgroep]] | classificatie | typering [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] | Administratieve classificatie |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Productsoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] | Administratieve classificatie |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Straatsectie]] | classificatie | typering [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervlak\|Parkeervlak]] | Administratieve indeling, geen zelfstandig object |
| [[Wiki/GGM/2-verkeer-vervoer-en-waterstaat/parkeren\|Belprovider]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | Te technisch/operationeel, geen herkenbaar bedrijfsobject |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/bouwlogistiek-centrum\|Bouwlogistiek Centrum]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerkaart\|Gehandicaptenparkeerkaart]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerplaats\|Gehandicaptenparkeerplaats]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte\|Halte]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/hoofdfietsroute\|Hoofdfietsroute]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laad-en-losplaats\|Laad- en Losplaats]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laadpaal\|Laadpaal]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route\|Logistieke Route]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/mobiliteitshub\|Mobiliteitshub]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-knooppunt\|OV-knooppunt]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-lijn\|OV-lijn]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/overslagpunt\|Overslagpunt]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/p-r-locatie\|P+R-locatie]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/stadsdistributiepunt\|Stadsdistributiepunt]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/voetgangersgebied\|Voetgangersgebied]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/zero-emissiezone\|Zero-emissiezone]] | nee | governance-object | **Alleen GEMMA-BO** |
