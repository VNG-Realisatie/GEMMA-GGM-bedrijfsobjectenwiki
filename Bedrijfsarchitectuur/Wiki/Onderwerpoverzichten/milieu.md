---
type: domein
naam: Milieu
status: in-behandeling
verwerkingsdatum: 2026-06-21
bronnen_count: 10
begrippen_count: 68
bo_count: 34
---

Gemeentelijk domein voor milieubeheer in brede zin. Omvat vier subdomeinen:

1. **Bodem, grondwater en ondergrond** — beheer van bodemkwaliteit, aanpak verontreinigingen, grondwaterbeheer, hergebruik van grond en duurzaam gebruik van de ondergrond (waaronder bodemenergie). De gemeente is bevoegd gezag voor bodemtaken.
2. **Afval en circulaire economie** — inzameling en verwerking van huishoudelijk en bedrijfsafval, grondstoffenscheiding, circulair hergebruik van materialen. De gemeente heeft wettelijke zorgplicht voor afvalinzameling (Wet Milieubeheer) en stuurt op de transitie naar een circulaire economie (doel: 2050 volledig circulair).
3. **Luchtkwaliteit** — beleid voor verbetering van de luchtkwaliteit gericht op EU-grenswaarden en WHO-advieswaarden. De gemeente neemt maatregelen op drie hoofdbronnen van luchtverontreiniging: wegverkeer, houtstook en mobiele werktuigen.
4. **Water en riolering** — beheer van het water- en rioleringssysteem (afvalwater, hemelwater, grondwater, oppervlaktewater) en gebruik van het stadswater (varen, zwemmen, goederenvervoer). De gemeente heeft drie wettelijke zorgplichten (afvalwater, hemelwater, grondwater) en beheert ~246 km watergangen. BO's vallen onder BOR (taakveld 8).

## Begrippentabel

| Begrip                                                                                                  | Type          | Omschrijving                                                 | BO? | Data-object | Reden                                                        | Voorbeelden                             | GGM |
| ------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------ | --- | ----------- | ------------------------------------------------------------ | --------------------------------------- | --- |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemkwaliteitskaart\|Bodemkwaliteitskaart]] | instrument    | Kaart met vastgestelde bodemkwaliteit per zone               | ✅   | nee         | 6/6 criteria, wettelijk instrument, GGM-hiaat                | Ontgravingskaart, toepassingskaart      | nee |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging\|Bodemverontreiniging]] | object        | Geregistreerde verontreinigingslocatie met type en status    | ✅   | ja          | 6/6 criteria, registratie bevoegd gezag, GGM-hiaat           | VOCl-pluim centrum, PFAS-locatie        | nee |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/saneringsplan\|Saneringsplan]]               | object        | Plan voor aanpak verontreiniging met maatregelen en fasering | ✅   | ja          | 6/6 criteria, wettelijk verplicht, GGM-hiaat                 | Gevalgericht saneringsplan, gebiedsplan | nee |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondwatermeetpunt\|Grondwatermeetpunt]]     | object        | Fysiek meetpunt in monitoringsnetwerk                        | ✅   | ja          | 6/6 criteria, registratie beheerder, GGM-hiaat               | Peilbuis, monitoringsput                | nee |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondverzet\|Grondverzet]]                   | object        | Registratie van grondverplaatsing met kwaliteit en volume    | ✅   | ja          | 6/6 criteria, meldingsplicht, GGM-hiaat                      | Grondtransport bouwproject              | nee |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemenergiesysteem\|Bodemenergiesysteem]]   | object        | WKO-installatie in de ondergrond                             | ✅   | ja          | 6/6 criteria, vergunningsplichtig, GGM-hiaat                 | Open WKO kantoorgebouw                  | nee |
| dynamische zone                                                                                         | classificatie | Kerngebied met vermengde grondwaterverontreinigingen         | ❌   | ja          | Ruimtelijke aanduiding, classificatie van beheergebied       | Centrum Utrecht                         | nee |
| bufferzone                                                                                              | classificatie | Overgangszone rondom de dynamische zone                      | ❌   | ja          | Ruimtelijke aanduiding, classificatie van beheergebied       | Ring rond centrum                       | nee |
| lokale maximale waarden                                                                                 | instrument    | Gebiedsspecifieke normen die afwijken van landelijk beleid   | ❌   | nee         | Norm/drempel, eigenschap van beleid, geen zelfstandig object | PCB-norm Leidsche Rijn                  | nee |
| bodemfunctieklassenkaart                                                                                | instrument    | Kaart die bodemfunctie per zone aangeeft                     | ❌   | nee         | Afgeleid van bestemmingsplan, geen zelfstandig BO            | Wonen, landbouw, industrie              | nee |
| gebiedsgerichte aanpak                                                                                  | thema         | Integrale benadering vermengde verontreinigingen             | ❌   | nee         | Proces/methode, geen object                                  | —                                       | nee |
| bodemsanering                                                                                           | thema         | Proces van opschonen verontreinigde bodem/grondwater         | ❌   | nee         | Proces, geen object                                          | —                                       | nee |
| bodembeheer                                                                                             | thema         | Overkoepelend beheer van bodemkwaliteit                      | ❌   | nee         | Overkoepelend procesgebied                                   | —                                       | nee |
| grondwaterbeheer                                                                                        | thema         | Beheer van grondwaterkwaliteit en -kwantiteit                | ❌   | nee         | Overkoepelend procesgebied                                   | —                                       | nee |

### Afval en circulaire economie

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]]|object|Voorziening voor gescheiden inzameling huishoudelijk afval| ✅ | ja |6/6 criteria, GGM exact (Container)|Ondergrondse container, kliko, citybin|ja|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstofstroom\|Grondstofstroom]]|object|Afzonderlijke afval-/grondstofstroom met eigen beleid| ✅ | ja |6/6 criteria, GGM sterk (Fractie)|GFT, PBP, papier, glas, textiel|ja|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/milieustraat\|Milieustraat]]|object|Voorziening voor gescheiden aanbieden grof afval| ✅ | ja |6/6 criteria, GGM exact (Milieustraat)|Tractieweg, Lunetten|ja|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/afvalstoffenheffing\|Afvalstoffenheffing]]|object|Gemeentelijke belasting voor afvalbeheerkosten| ✅ | ja |6/6 criteria, GGM partieel (Prijsafspraak)|Jaarlijkse heffing per huishouden|ja|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/verwerkingscontract\|Verwerkingscontract]]|object|Overeenkomst met verwerker voor afvalverwerking| ✅ | ja |6/6 criteria, procesobject|AVU-contract restafval, AVR nascheiding|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/inzamelcontract\|Inzamelcontract]]|object|Overeenkomst gemeente-bedrijf voor bedrijfsafval| ✅ | ja |6/6 criteria, procesobject|Contract horeca binnenstad|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/upcyclecentrum\|Upcyclecentrum]]|object|Voorziening voor hergebruik grof huishoudelijk afval| ✅ | ja |6/6 criteria, procesobject, GGM-hiaat|Tractieweg, Lunetten (gepland)|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstoffendepot\|Grondstoffendepot]]|object|Opslag vrijkomende materialen voor hergebruik| ✅ | ja |6/6 criteria, procesobject, GGM-hiaat|Lage Weide|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/materiaalpasspoort\|Materiaalpasspoort]]|instrument|Digitale vastlegging materialen in gebouw/object| ✅ ⚠️ | ja |5/6 criteria, instrument — ter discussie|Paspoort kantoorgebouw|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/afvalstoffenverordening\|Afvalstoffenverordening]]|instrument|Gemeentelijke verordening voor afvalinzameling| ✅ ⚠️ | nee |5/6 criteria, governance — ter discussie|Opt-in systeem reclamedrukwerk|nee|
|Het Nieuwe Inzamelen (HNI)|thema|Inzamelsysteem met gescheiden ophalen en brengen restafval| ❌ | nee |Proces/systeem, geen zelfstandig object|—|nee|
|nascheiding|thema|Machinale scheiding van PBP uit restafval| ❌ | nee |Verwerkingsproces, geen object|—|nee|
|circulaire economie|concept|Economisch systeem gericht op grondstoffenbehoud| ❌ | nee |Beleidsconcept, geen object|—|nee|
|sorteeranalyse|activiteit|Kwaliteitsmeting van ingezamelde grondstoffen| ❌ | nee |Meetactiviteit, geen zelfstandig object|—|nee|

### Luchtkwaliteit

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/milieuzone\|Milieuzone]]|object|Afgebakend gebied met toegangsbeperkingen op basis van emissieklasse| ✅ | ja |6/6 criteria, GGM-hiaat|Milieuzone diesel personenauto, nul-emissiezone bestel/vracht|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/vuurwerkvrije-zone\|Vuurwerkvrije zone]]|object|Aangewezen zone met vuurwerkverbod| ✅ | ja |6/6 criteria, GGM-hiaat|150 zones jaarwisseling 2022-2024|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/luchtkwaliteitsmeetpunt\|Luchtkwaliteitsmeetpunt]]|object|Fysieke meetlocatie in het gemeentelijk luchtkwaliteitsmeetnet| ✅ | ja |6/6 criteria, GGM-hiaat|64 NO2-meetpunten, 3 RIVM-stations|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/rookvrije-zone\|Rookvrije zone]]|object|Aangewezen zone waar roken niet is toegestaan| ✅ | ja |6/6 criteria, GGM-hiaat|Bushaltes, speelplekken, sportlocaties, USP|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/ontheffing-milieuzone\|Ontheffing (milieuzone)]]|object|Individuele uitzondering op milieuzoneregels| ✅ | ja |6/6 criteria, GGM-hiaat|Ontheffing camper, ontheffing oldtimer|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/walstroompunt\|Walstroompunt]]|object|Fysiek aansluitpunt voor walstroom aan scheepvaart| ✅ | ja |6/6 criteria, GGM-hiaat|Ca. 50 punten in Utrecht|nee|
|[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/sloopregeling\|Sloopregeling]]|instrument|Subsidieregeling voor vervanging voertuig bij milieuzone-aanscherping| ✅ ⚠️ | ja |6/6 criteria, instrument — ter discussie|Sloopsubsidie milieuzone, inruilregeling brom/snor|nee|
|houtstookverbod|governance|Regulerend kader voor verbod op houtstook| ❌ | nee |Governance-instrument, geen zelfstandig object|Buitenstookverbod 2025, binnenstookverbod 2030|nee|
|Schone Lucht Akkoord (SLA)|governance|Landelijk akkoord Rijk-provincies-gemeenten| ❌ | nee |Extern akkoord, geen gemeentelijk object|—|nee|
|convenant SEB|governance|Landelijk convenant Schoon en Emissieloos Bouwen| ❌ | nee |Externe samenwerkingsafspraak|—|nee|
|emissieklasse|classificatie|Classificatie van voertuigemissies (Euro 1-6)| ❌ | ja |Eigenschap van voertuig, geen eigen bestaan|Euro 4, Euro 6|nee|
|luchtverontreinigende stof|referentiegegeven|Stoffen die worden gemeten (NO2, PM2.5, PM10)| ❌ | nee |Referentieclassificatie, geen levenscyclus|NO2, PM2.5, PM10, roet, ultrafijnstof|nee|
|WHO-advieswaarden|referentiegegeven|Advieswaarden Wereldgezondheidsorganisatie| ❌ | nee |Externe normstelling|WHO 2021: NO2 10 µg/m3, PM2.5 5 µg/m3|nee|
|EU-grenswaarden|referentiegegeven|Wettelijk verplichte maximumconcentraties| ❌ | nee |Externe normstelling|EU 2030: NO2 20 µg/m3, PM2.5 10 µg/m3|nee|

### Water en riolering

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal\|Gemaal]]|object|Constructie voor het verpompen van water in het rioleringssysteem| ✅ | ja |6/6 criteria, GGM exact (Gemaal)|Rioolgemaal Kardinaal de Jongweg, minigemalen, eindgemalen|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kolk\|Kolk]]|object|Reservoir voor opvang hemelwater en afvoer naar riool of ondergrond| ✅ | ja |6/6 criteria, GGM exact (Kolk)|Straatkolk, amfibievriendelijke kolk|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/overstortconstructie\|Overstortconstructie]]|object|Constructie die bij zware neerslag verdund afvalwater loost op oppervlaktewater| ✅ | ja |6/6 criteria, GGM exact (Overstortconstructie)|156 gemengde overstorten in Utrecht|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/bergingsbassin\|Bergingsbassin]]|object|Gesloten reservoir achter overstort voor tijdelijke opvang overstortwater| ✅ | ja |6/6 criteria, GGM exact (Bergingsbassin)|18 bergbezinkbassins in Utrecht|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject\|Waterobject]]|object|Functioneel stuk oppervlaktewater dat de gemeente beheert| ✅ | ja |6/6 criteria, GGM exact (Waterobject)|Watergangen, vijvers, grachten, kanalen, vaarwater|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]]|gebied|Administratief beheersgebied van het rioolstelsel| ✅ | ja |6/6 criteria, GGM exact (Rioleringsgebied)|Zuiveringsgebied rwzi Brailledreef|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/put\|Put]]|object|Verticale constructie voor inspectie en onderhoud van riolering| ✅ | ja |6/6 criteria, GGM exact (Put), subtypes Drainageput/Filterput/Infiltratieput|Rioolput, drainageput|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/buitenzwemplek\|Buitenzwemplek]]|object|Locatie in open water waar buiten gezwommen wordt| ✅ | ja |6/6 criteria, GGM-hiaat|Haarrijnseplas, Strijkviertelplas, Muntsluis|nee|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats\|Ligplaats]]|object|Aangewezen plek in het water voor permanent afmeren van drijvend object| ✅ | ja |6/6 criteria, GGM: Ligplaats (BAG, exact)|482 recreatief + 334 woonboten|ja|
|[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolheffing\|Rioolheffing]]|object|Gemeentelijke belasting voor water- en rioleringsbeheer| ✅ | ja |6/6 criteria, GGM-hiaat, vergelijkbaar met [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/afvalstoffenheffing\|Afvalstoffenheffing]]|€254/jaar eigenarenheffing|nee|
|sluis|subtype|Waterbouwkundig kunstwerk voor niveauverschillen in vaarwegen| ✅ subtype | ja |Subtype van [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kunstwerk\|Kunstwerk]], GGM-hiaat|Weerdsluis, Muntsluis|nee|
|pomp|onderdeel|Technische installatie voor watertransport onder druk| ❌ | nee |Onderdeel van [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal\|Gemaal]], te granulair|—|ja|
|uitlaatconstructie|onderdeel|Eindpunt rioolleiding naar oppervlaktewater| ❌ | nee |Te granulair voor BO-niveau|—|ja|
|persleiding|onderdeel|Riolering met kunstmatig drukverschil| ❌ | nee |Type riolering, eigenschap van systeem|150 km in Utrecht|nee|
|hemelwaterriool|onderdeel|Apart leidingstelsel voor hemelwater| ❌ | nee |Type riolering, eigenschap van gescheiden stelsel|—|nee|
|wadi|voorziening|Bovengrondse greppel voor hemelwaterinfiltratie| ❌ | nee |Type infiltratievoorziening, te specifiek|Wadi's Leidsche Rijn|nee|
|havenverordening|governance|Gemeentelijke verordening met vaarregels| ❌ | nee |Governance-instrument, geen zelfstandig object|Havenverordening Utrecht 2015|nee|
|havenatlas|instrument|Digitale kaart met ligplaatszones en functies| ❌ | nee |Registratie/kaartproduct, geen zelfstandig BO|—|nee|
|ligplaatsvergunning|vergunning|Vergunning voor innemen ligplaats| ❌ | nee |VTH-vergunning, valt onder generiek vergunningconcept|482 uitgegeven|nee|
|exploitatievergunning|vergunning|Vergunning voor commercieel vaarverkeer| ❌ | nee |VTH-vergunning, valt onder generiek vergunningconcept|286 uitgegeven|nee|
|havengeld|heffing|Vergoeding voor gebruik stadswater| ❌ | nee |Te dun voor apart BO, onderdeel havenbeheer|—|nee|
|ecoscan|meetmethode|Methode voor toetsing ecologische waterkwaliteit| ❌ | nee |Meetmethode, geen object|Eenmaal per 3 jaar|nee|
|WRIS|informatiesysteem|Water- en Rioleringsinformatiesysteem| ❌ | nee |Informatiesysteem, geen bedrijfsobject|—|nee|
|Waterproof030|programma|Stimuleringsprogramma klimaatadaptatie| ❌ | nee |Programma/proces, geen object|Tegeltaxi, NK-tegelwippen|nee|
|afkoppelen|activiteit|Scheiden hemelwater van afvalwater| ❌ | nee |Proces/activiteit, geen object|15-19 ha/jaar doelstelling|nee|
|baggeren|activiteit|Groot onderhoud oppervlaktewater| ❌ | nee |Onderhoudsactiviteit, geen object|30 km/jaar, 30.000 m³|nee|

Alle 10 water-BO's vallen onder GGM-taakveld 8 (BOR), niet onder taakveld 7 (Milieu). Vergelijkbaar met hoe groenbeleid-BO's onder BOR vallen maar vanuit milieu-bronnen worden afgeleid. Van de 10 BO's hebben 7 een directe GGM-grondslag (onder BOR); 3 zijn GGM-hiaten.

## Verwerkte bronnen

### Bodem, grondwater en ondergrond
- [[Wiki/Bronsamenvattingen/Milieu/beleid-bodem-grondwater-en-ondergrond|Beleid voor bodem, grondwater en ondergrond]] — overzichtspagina gemeente Utrecht
- [[Wiki/Bronsamenvattingen/Milieu/gebiedsplan-grondwaterbeheer|Gebiedsplan gebiedsgericht grondwaterbeheer en visie op duurzaam gebruik van de ondergrond]] — gebiedsgericht grondwaterbeheer (56 p., 2015)
- [[Wiki/Bronsamenvattingen/Milieu/nota-bodembeheer|Nota Bodembeheer 2017-2027 (Grondig Werken 4)]] — hergebruik grond en bodembeheer

### Afval en circulaire economie
- [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020|Grondstoffennota 2020]] — operationeel afvalbeleid per grondstofstroom (98 p., 2020)
- [[Wiki/Bronsamenvattingen/Milieu/visie-utrecht-circulair-2050|Visie Utrecht Circulair 2050]] — strategische visie circulaire stad (31 p., 2024)
- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-utrecht-circulair-2030|Beleidsnota Utrecht Circulair 2030]] — uitwerking visie in meetbare doelen (2024)

### Luchtkwaliteit
- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025|Beleidsnota Luchtkwaliteit – Gezonde lucht voor iedereen 2025-2030]] — Utrechts luchtkwaliteitsbeleid: milieuzones, houtstook, mobiele werktuigen (1267 regels, 2024)

### Water en riolering
- [[visie-water-riolering 1|Visie Water en Riolering Utrecht]] — beleidskader water- en rioleringssysteem, horizon 2050
- [[programma-water-riolering-2025-2029 1|Programma Water en Riolering Utrecht 2025-2029]] — jaarlijks uitvoeringsprogramma met budgetten en planningen
- [[beleidsnota-stadswater 1|Beleidsnota Stadswater]] — gebruik vaarwegen en buitenzwemwater, horizon 2040

## Groenbeleid (verwerkt → domein Beheer Openbare Ruimte)

De groenbeleid-bronnen (Groenstructuurplan 2007 en Actualisatie 2018) zijn opgeslagen onder Sources/Onderwerpen/Milieu/ maar leveren BO's in het domein [[Wiki/Onderwerpoverzichten/beheer-openbare-ruimte|Beheer Openbare Ruimte]]: [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/groenobject|Groenobject]] en [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/faunapassage|Faunapassage]]. Zie de bronsamenvattingen:
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007|Groenstructuurplan Utrecht – Stad en land verbonden]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030|Actualisatie Groenstructuurplan Utrecht 2017-2030]]

## Nog te verwerken bronnen

- [Sources/Onderwerpen/Milieu/rubriek-milieu.md](Sources/Onderwerpen/Milieu/rubriek-milieu.md) — VNG-rubriek Milieu
- [Sources/Onderwerpen/Milieu/luchtkwaliteit.md](Sources/Onderwerpen/Milieu/luchtkwaliteit.md) — VNG: luchtkwaliteit
- [Sources/Onderwerpen/Milieu/asbest.md](Sources/Onderwerpen/Milieu/asbest.md) — VNG: asbest
- [Sources/Onderwerpen/Milieu/zeer-zorgwekkende-stoffen.md](Sources/Onderwerpen/Milieu/zeer-zorgwekkende-stoffen.md) — VNG: ZZS
- [Sources/Onderwerpen/Milieu/afval-en-circulaire-economie.md](Sources/Onderwerpen/Milieu/afval-en-circulaire-economie.md) — VNG: afval en circulaire economie
- Beleidsnota Ondergrond 2025-2035 (niet beschikbaar, achter authenticatie)

## Openstaande vragen

- De Beleidsnota Ondergrond 2025-2035 was niet downloadbaar (authenticatie vereist). Deze kan aanvullende objecten bevatten.
- Relatie met het Omgevingswet-domein: veel bodemtaken vallen onder de Omgevingswet. De BO's hier kunnen ook vanuit dat perspectief relevant zijn.
- ⚠️ **Materiaalpasspoort** en **Afvalstoffenverordening** zijn ter discussie: zijn instrumenten/governance-objecten BO's?
- ⚠️ **Sloopregeling** is ter discussie: instrument, functioneel een specialisatie van Subsidie (GGM Model Subsidies)
- De VNG-bron [afval-en-circulaire-economie.md](Sources/Onderwerpen/Milieu/afval-en-circulaire-economie.md) is nog niet verwerkt — kan aanvullende landelijke context bieden.

## Terugmeldingen richting GGM

16 niet-GGM BO's in dit domein zijn hiaten. Terugmeldingen:
- Het GGM mist een beleidsdomein voor bodem/grondwater onder taakveld 7.
- Het GGM mist een beleidsdomein voor luchtkwaliteit onder taakveld 7: milieuzones, meetpunten, zones zijn dataobjecten die gemeenten actief beheren.
- Het GGM mist een generiek herbruikbaar "Zone"-concept (vgl. Parkeerzone) dat ook voor milieuzones, rookvrije zones en vuurwerkvrije zones toepasbaar is.
- Het GGM mist een generiek "Ontheffing"-concept; nu zijn er domeinspecifieke varianten (Ligplaatsontheffing, Ontheffing Inburgering, Ontheffing Werk) zonder gemeenschappelijk supertype.
- Het GGM mist Buitenzwemplek als entiteit onder BOR — gemeenten beheren officiële en niet-officiële zwemlocaties met eigen monitoring en oeverinrichting.
- ~~Het GGM mist Ligplaats als entiteit onder BOR~~ — **Opgelost:** GGM BAG kent Ligplaats als adresseerbaar object (exact match). Niet onder BOR maar onder 99 Kern/BAG.
- Het GGM mist Rioolheffing — vergelijkbaar met hoe Afvalstoffenheffing ontbreekt maar wel BO is.
- Het GGM mist Sluis als subtype van Kunstwerk — waterbouwkundig kunstwerk dat gemeenten beheren.
Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
