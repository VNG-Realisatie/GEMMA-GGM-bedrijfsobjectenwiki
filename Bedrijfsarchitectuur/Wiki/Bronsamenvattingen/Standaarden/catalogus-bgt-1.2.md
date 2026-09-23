---
type: bronsamenvatting
titel: "Gegevenscatalogus BGT 1.2 (IMGeo)"
onderwerp: [Basisregistraties, BGT]
datum_ingest: 2026-09-23
---

## Samenvatting

De Gegevenscatalogus BGT 1.2 (Geonovum, vastgesteld 1 juli 2020) beschrijft het informatiemodel IMGeo van de Basisregistratie Grootschalige Topografie: de digitale kaart van Nederland op de grootste schaal, met de werkelijkheid op straatniveau (wegen, water, terrein, gebouwen, kunstwerken). Gemeenten (en andere overheden) zijn bronhouder van hun eigen grondgebied.

De catalogus definieert **18 objecttypen**, waarvan 1 abstract (IMGeo-Object, de gemeenschappelijke basis) en 1 abstract subtype (OverigeConstructie). Objecttypen zijn ondergebracht in vijf groepen:

- **Wegen/spoor:** [[Wegdeel]] (rijbanen, fietspaden e.d.), [[OndersteunendWegdeel]] (bermen, trottoirbanden), [[Spoorbaan|Spoor]] (spoorbaan-as)
- **Terrein:** [[OnbegroeidTerreindeel]], [[BegroeidTerreindeel]] (vlakvormig groen)
- **Water:** [[Waterdeel]] (permanent water), [[OndersteunendWaterdeel]] (periodiek water, waterhuishouding)
- **Bouwwerken:** [[Pand]] (BAG-gedeeld), OverigeConstructie (abstract), [[OverigBouwwerk]], [[Overbruggingsdeel]], [[Tunneldeel]], [[Kunstwerkdeel]], [[Scheiding]]
- **Overig:** [[FunctioneelGebied]], OpenbareRuimteLabel (cartografisch label), Plaatsbepalingspunt (meettechnisch kwaliteitsobject)

## Kernbegrippen

- **Wegdeel** — kleinste functioneel onafhankelijk stukje van een NEN 3610 Weg, primair bedoeld voor weg-, spoor- of vliegverkeer te land. Eigen attributen: functie, fysiek voorkomen, talud.
- **OndersteunendWegdeel** — deel van de weg niet primair bedoeld voor verkeer (berm, trottoirband).
- **Spoor** (BO: [[Spoorbaan]]) — de as van het spoor: het midden van twee stalen staven waarover trein, tram of sneltram rijdt. **Homoniem** met de GGM-entiteit "Spoor" in beleidsdomein Archeologie ("een blijk van eerdere aanwezigheid") — ander concept, zelfde naam.
- **OnbegroeidTerreindeel / BegroeidTerreindeel** — kleinste functioneel onafhankelijk stukje terrein binnen NEN 3610 Terrein, resp. zonder en met aaneengesloten vegetatie.
- **Waterdeel** — kleinste functioneel onafhankelijk stukje water, permanent met water bedekt. **OndersteunendWaterdeel** — periodiek (deels) met water bedekt object t.b.v. waterhuishouding.
- **Pand** — al vastgelegd als BO via de BAG-catalogus ([[Wiki/Bedrijfsobjecten/99-kern/bag/pand]]); BGT/RSGBPlus is een GGM-duplicaat van dezelfde entiteit.
- **OverigeConstructie** — abstract objecttype voor gebouwde objecten die geen NEN 3610-gebouw zijn. Concrete subtypes: OverigBouwwerk, Overbruggingsdeel, Tunneldeel, Kunstwerkdeel, Scheiding.
- **OverigBouwwerk** — duurzaam met de aarde verbonden bouwwerk, geen pand of kunstwerk.
- **Overbruggingsdeel** — onderdeel van een (beweegbare) verbinding tussen twee door water/weg gescheiden punten, essentieel voor de constructie.
- **Tunneldeel** — onderdeel van een kunstmatige, kokervormige onderdoorgang, essentieel voor de constructie.
- **Kunstwerkdeel** — onderdeel van een civieltechnisch werk voor infrastructuur (wegen, water, spoor, waterkeringen, leidingen).
- **Scheiding** — kunstmatig obstakel met een werende functie (bijv. hekwerk, muur). **Duplicaat**: identiek gemodelleerd in RSGBPlus én in Beheer Openbare Ruimte (zelfde definitie, twee GUIDs).
- **FunctioneelGebied** — begrensd en benoemd gebied beschreven door een functionele eenheid. **Duplicaat**: identiek gemodelleerd in RSGBPlus én in Beheer Openbare Ruimte.
- **OpenbareRuimteLabel** — naam en plaatsingspunten van een in de BAG geregistreerde Openbare Ruimte, t.b.v. visualisatie. Geen zelfstandig object — cartografisch label van [[Openbare Ruimte]].
- **Plaatsbepalingspunt** — ingemeten punt dat onderdeel is van de begrenzing van BGT-objecten, geregistreerd t.b.v. kwaliteitsdoeleinden. Meettechnisch, geen zelfstandige bedrijfsbetekenis.
- **IMGeo-Object** — abstract supertype: gemeenschappelijke eigenschappen (identificatie, objectBeginTijd/EindTijd, tijdstipRegistratie, bronhouder, status) van elk grootschalig topografisch object.

## Relevantie voor bedrijfsarchitectuur

De BGT is, net als BAG/BRP/BRK/NHR/BRO, een basisregistratie waarvoor de gemeente bronhoudertaken heeft. Ze modelleert dezelfde fysieke werkelijkheid als de IMBOR-beheerobjecten in het domein Beheer Openbare Ruimte ([[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/verhardingsobject|Verhardingsobject]], [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject|Waterobject]] e.a.), maar op een ander niveau: BGT/RSGBPlus is de topografische basisregistratie (wat op de kaart staat, wettelijk verplicht bij te houden), IMBOR is de beheerlaag (wat de gemeente onderhoudt). Dit zijn twee complementaire, niet-overlappende GGM-beleidsdomeinen voor hetzelfde stuk fysieke werkelijkheid.

> "De basisregistratie grootschalige topografie bevat gegevens over alle fysieke objecten die vanuit een gemeenschappelijk gebruik gezien worden als: wegen, waterlopen, terreinen, spoorbanen en gebouwen."

## Bronnen

- [[Sources/Standaarden/catalogus-bgt-1.2]]
