---
type: domein
naam: Cultuur
status: in opbouw
verwerkingsdatum: 2026-06-27
bronnen_count: 15
begrippen_count: 49
bo_count: 8
---

# Cultuur

Gemeentelijk domein voor kunst, cultuur en erfgoed. Gemeenten faciliteren culturele voorzieningen, voeren cultuurbeleid, en beheren erfgoed (monumenten, archieven, musea). Het cultuurbeleid is overwegend beleidsmatig; de concrete bedrijfsobjecten zitten in het erfgoeddomein.

In het GGM valt dit onder taakveld **5 Sport, Cultuur en Recreatie** met beleidsdomeinen **Erfgoed** (44 entiteiten) en **Musea** (32 entiteiten). Er is geen apart "Cultuur"-beleidsdomein in het GGM — cultuurbeleid wordt niet als data gemodelleerd.

## Begrippen

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]]|object|Beschermd onroerend erfgoed met rijks-, provinciaal of gemeentelijke status| ✅ | ja |6/6 criteria, exact match (Beschermde Status)|Rijksmonument, gemeentelijk monument, beschermd gezicht|ja|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]]|object|Gearchiveerde informatie ongeacht medium, beheerd door gemeentearchief; raakt zowel erfgoed als informatiebeheer| ✅ | ja |6/6 criteria, exact match|Raadsbesluit in archief, historisch document, digitaal bestand|ja|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/museumobject\|Museumobject]]|object|Object met cultuurhistorische waarde in museale collectie| ✅ | ja |6/6 criteria, exact match|Schilderij, archeologisch artefact, historisch gebruiksvoorwerp|ja|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vindplaats\|Archeologische vindplaats]]|object|Locatie met (verwachte) archeologische waarde| ✅ | ja |6/6 criteria, sterk match (GGM Vindplaats); gemeente is bevoegd gezag, beheert eigen beleidskaart|Opgraving binnenstad, Romeinse vondstlocatie|ja|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vondst\|Archeologische vondst]]|object|Overblijfsel of voorwerp uit het verleden| ✅ | ja |6/6 criteria, exact match (GGM Vondst + Artefact); gemeente beheert collectie in eigen depot|Romeins schip De Meern 1, middeleeuwse moerbalk|ja|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologisch-onderzoek\|Archeologisch onderzoek]]|object|Onderzoeksproject door/namens gemeente als bevoegd gezag| ✅ | ja |6/6 criteria, sterk match (GGM Project); gemeente voert en begeleidt onderzoek|Opgraving Prinses Maxima Centrum, opgravingsproject Domplein|ja|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/orgel\|Orgel]]|object|Rijks- of gemeentelijk monumentaal muziekinstrument in een kerkgebouw| ✅ | ja |6/6 criteria; eigen monumentstatus, eigen levenscyclus, apart geregistreerd; GGM-hiaat|Domorgel, Bätz-orgel Jacobikerk|nee (hiaat)|
|archiefbewaarplaats|locatie|Juridisch aangewezen locatie voor overgebrachte archiefbescheiden; fysiek (regionaal archief) of digitaal (e-depot)| ❌ | ja |GGM kent "Depot" (fysieke opslag) en "Archief" (verzameling + bewaarplaats); geen apart BO maar component van archiefbeheer. E-depot-variant ontbreekt in GGM.|Gemeentearchief, regionaal historisch centrum, e-depot|deels (Depot)|
|archiefruimte|locatie|Ruimte waar semi-statische archieven (afgesloten, niet overgebracht) worden bewaard vóór overbrenging naar archiefbewaarplaats| ❌ | nee |Fysieke ruimte met inrichtingseisen (art. 21 Aw); component van archiefbeheer, geen zelfstandig BO|Archiefkelder gemeentehuis, depotruimte|nee|
|archiefbescheiden|object|Informatiedragers van gemeentelijke organen onder de Archiefwet, "ongeacht hun vorm" (incl. digitaal)| ❌ | ja |Synoniem van [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]]; geen apart BO|Raadsdossier, vergunningdossier, digitaal bestand|ja|
|zorgdrager|governance|Overheidsorgaan met bestuurlijke verantwoordelijkheid voor archiefbescheiden (voor gemeente: B&W)| ❌ | nee |Governance-rol; onderscheid zorg (bestuurlijk) vs. beheer (operationeel)|—|nee|
|gemeentearchivaris|actor|Functionaris met wettelijke toezichtstaak op archiefbeheer| ❌ | nee |Rol/functie, geen gemeentelijk registratieobject|—|nee|
|overbrenging|proces|Formele overdracht van archiefbescheiden naar de archiefbewaarplaats na 20 jaar| ❌ | nee |Procesmoment; geen eigen bestaan als object. Sleutelmoment: na overbrenging geldt Archiefwet-openbaarheid i.p.v. Wob|Overbrenging na 20 jaar|nee|
|vernietigingslijst|instrument|Verplicht opgestelde lijst met te vernietigen archiefbescheiden en termijnen| ❌ | nee |Procesinstrument voor selectie en vernietiging; geen eigen levenscyclus als data-object|Vernietigingslijst gemeente 2024|nee|
|substitutie|proces|Vervanging van originele archiefbescheiden door reproducties (incl. digitaal), waarna originelen mogen worden vernietigd| ❌ | nee |Proces; basis voor digitalisering en e-depot|Verfilming, digitalisering|nee|
|werelderfgoed|object|UNESCO-werelderfgoedsite met internationaal beschermingsregime| ❌ | ja |Internationaal instrument, niet primair gemeentelijk; bescherming loopt via [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]]|Limes, NHW, Rietveld-Schröderhuis|nee|
|beschermd stadsgezicht|object|Rijks- of gemeentelijk beschermd stads- of dorpsgezicht| ❌ | ja |Onderdeel van [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]] (via attribuut gezichtscode in GGM)|Binnenstad Utrecht|ja|
|cultuurhistorische waardenkaart|instrument|Erfgoedwaarden in lagen en thema's, afwegingskader planvorming| ❌ | nee |Beleidsinstrument|—|nee|
|archeologische beleidskaart|instrument|Kaart met verwachte archeologische waarde en onderzoeksverplichtingen| ❌ | nee |Beleidsinstrument|—|nee|
|erfgoedverordening|instrument|Samenvoeging Monumenten- en Archeologieverordening, onderdeel omgevingsplan| ❌ | nee |Governance-instrument|—|nee|
|erfgoed effectrapportage|instrument|Analyse van gevolgen van ruimtelijke keuzes op erfgoed| ❌ | nee |Beleidsinstrument|—|nee|
|groen/blauw erfgoed|thema|Historische parken, waterlopen, bomenlanen als structurerend element| ❌ | nee |Categorie van bestaande objecten (parken, waterlopen), geen eigenstandig BO; erfgoedwaarde is een kwalificatie|Maliebaan, Zocherpark, singel|nee|
|immaterieel erfgoed|thema|Levende cultuuruitingen beleefd als erfgoed| ❌ | nee |Geen eigen bestaan als gemeentelijk concept; gemeente heeft nog geen structurele ondersteuning|Sint Maarten, Utrechts dialect|nee|
|culturele voorziening|object|Organisatie/faciliteit die cultuur faciliteert| ❌ | ja |Facilitaire/organisatorische entiteit, niet als erfgoedobject|Theater, podium, broedplaats, muziekschool|nee|
|bibliotheek|object|Gemeentelijke voorziening voor kennis en cultuur| ❌ | ja |Voorziening, geen eigen levenscyclus als erfgoedobject|Openbare bibliotheek, vestiging|nee|
|cultuurbeleid|thema|Gemeentelijk beleid voor cultureel aanbod| ❌ | nee |Beleidsmatig, geen object|Cultuurvisie, cultuuragenda|nee|
|cultuurwaarde|waarde|Intrinsieke, maatschappelijke en economische waarde van cultuur| ❌ | nee |Normatief concept|—|nee|
|cultuureducatie|thema|Cultureel onderwijs binnen en buiten school| ❌ | nee |Activiteit/proces|CmK, cultuur op school|nee|
|cultuurparticipatie|thema|Deelname aan culturele activiteiten| ❌ | nee |Activiteit/proces|Amateurkunst, koorlidmaatschap|nee|
|fair pay|instrument|Eerlijke beloning cultuurprofessionals| ❌ | nee |Beleidsinstrument|Fair Practice Code, culturele codes|nee|
|ringenmodel|instrument|Differentiatie culturele voorzieningen naar gemeenteomvang| ❌ | nee |Beleidsinstrument/classificatie|Kernachtig/uitgebreid/alomvattend pakket|nee|
|culturele centrumfunctie|thema|Mate waarin gemeente cultuur verzorgt voor regio| ❌ | nee |Classificatie van gemeenten|G40 als cultureel centrum|nee|
|creatieve cyclus|thema|Keten: leren → produceren → presenteren → interesseren| ❌ | nee |Conceptueel model|—|nee|
|culturele basisinfrastructuur|thema|Lokale voorzieningen voor cultuureducatie en -participatie| ❌ | nee |Strategisch concept|—|nee|
|basisinfrastructuur (bis)|instrument|Rijksinstrument voor meerjarige cultuursubsidies| ❌ | nee |Rijksinstrument, niet gemeentelijk|Rijksgesubsidieerde orkesten, musea|nee|
|Erfgoedwet|instrument|Integrale wetgeving (2016) voor erfgoed, musea, archeologie| ❌ | nee |Wet/governance|—|nee|
|cultuurfinanciering|thema|Systematiek van publieke bekostiging van cultuur| ❌ | nee |Beleidsmatig|Gemeentefonds-aandeel cultuur (€2 mrd)|nee|
|luidklok|object|Klok in kerktoren, deels met eigen monumentstatus| ❌ | ja |Onderdeel van kerkgebouw ([[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]]), geen zelfstandig BO|112 luidklokken in Utrecht|nee|
|[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/collectie\|Collectie]]|object|Samenhangende verzameling cultuurgoederen of museumobjecten, beheerd op grond van vastgestelde criteria| ✅ | ja |6/6 criteria, exact match; Erfgoedwet art. 2.8-2.11 geeft wettelijke grondslag via instellingsbesluiten|Keramiekcollectie, schilderijenverzameling, archeologische deelcollectie|ja|
|beschermd cultuurgoed|object|Roerend cultuurgoed aangewezen als onvervangbaar en onmisbaar voor het Nederlands cultuurbezit (Erfgoedwet art. 3.7)| ❌ | ja |Aanwijzing door Minister, niet door gemeente; gemeente is beheerder, niet bevoegd gezag|Nachtwacht, Mondriaan|nee|
|beschermde verzameling|object|Verzameling cultuurgoederen aangewezen als geheel (Erfgoedwet art. 3.7 lid 2)| ❌ | ja |Status op [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/collectie\|Collectie]], geen apart BO|Collectie Museum Prinsenhof|nee|
|ensemble|object|Rijksmonument tezamen met cultuurgoederen in onderlinge samenhang (Erfgoedwet art. 3.13)| ❌ | ja |Geen eigen bestaan los van individuele monumenten; cultuurhistorische samenhang is kenmerk|Kerk + pastorie + school|nee|
|eDepot|systeem|Digitale archiefbewaarplaats voor duurzame opslag van overgebrachte en uitgeplaatste archieven| ❌ | ja |Infrastructuur/systeem, geen zelfstandig registratieobject; GGM-hiaat (kent alleen fysiek Depot)|eDepot Westfries Archief|deels (Depot)|
|pre-eDepot|systeem|Digitale omgeving voor uitgeplaatste legacy-informatie vóór formele overbrenging| ❌ | nee |Tussenvorm tussen eigen beheer en overbrenging; facilitair concept|Pre-eDepot WFA|nee|
|tentoonstelling|activiteit|Uitstalling van museumobjecten voor publiek| ❌ | ja |Operationele activiteit van museum, geen gemeentelijk registratieobject|Vaste collectiepresentatie, wisseltentoonstelling|ja|
|bruikleen|overeenkomst|Overeenkomst voor tijdelijk gebruik van museumobject| ❌ | ja |Operationeel contract, specifiek museaal; geen apart BO naast [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/museumobject\|Museumobject]]|Bruikleen Rijksmuseum aan gemeentelijk museum|ja|
|kerkgebouw|object|Religieus gebouw met monumentstatus| ❌ | ja |Type van [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]], geen apart BO|Domkerk, Janskerk, Pieterskerk|ja|
|herbestemmingsprofiel|instrument|Bouwhistorisch onderzoek + waardestelling + transformatieruimte bij herbestemming| ❌ | nee |Beleidsinstrument|Profiel Westerkerk, profiel Josephkerk|nee|
|waardestelling|instrument|Vaststelling kernwaarden van een monument als uitgangspunt voor herbestemming| ❌ | nee |Beleidsinstrument|—|nee|
|carillon|object|Klokkenspel in kerktoren, eigendom gemeente| ❌ | ja |Specifiek type luidklok-ensemble; drie stuks, geen apart BO naast Monument|Hemony-beiaard Domtoren|nee|

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Cultuur/kunst-en-cultuur|Kunst en cultuur]] — VNG-overzicht cultuurbeleid
- [[Wiki/Bronsamenvattingen/Cultuur/propositie-cultuur|Propositie Samen cultuur borgen]] — VNG-propositie vier pijlers cultuurbeleid
- [[Wiki/Bronsamenvattingen/Cultuur/architectuur-en-erfgoed|Architectuur en erfgoed]] — VNG-overzicht erfgoed, monumenten, archeologie
- [[Wiki/Bronsamenvattingen/Cultuur/bibliotheekwerk|Bibliotheekwerk]] — VNG-overzicht bibliotheekwerk
- [[Wiki/Bronsamenvattingen/Cultuur/toelichting-ringenmodel|Toelichting ringenmodel — de culturele infrastructuur van gemeenten]] — VNG-actualisering ringenmodel 2.0
- [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht|Erfgoednota 'Utrechts erfgoed verbindt mensen en tijden']] — Gemeente Utrecht, erfgoedbeleid 2021: monumenten, archeologie, verduurzaming, klimaatadaptatie
- [[Wiki/Bronsamenvattingen/Cultuur/visie-religieus-erfgoed-2025|Utrechtse visie religieus erfgoed — Actualisatie en uitbreiding augustus 2025]] — Gemeente Utrecht, geactualiseerde visie op religieus erfgoed: kerkgebouwen, orgels, herbestemming
- [[Wiki/Bronsamenvattingen/Cultuur/erfgoedbeleid-utrecht|Erfgoedbeleid — omgevingsvisie Utrecht]] — Gemeente Utrecht, overzichtspagina erfgoedbeleid (secundaire bron)
- [[Wiki/Bronsamenvattingen/Cultuur/bijlagen-visie-religieus-erfgoed|Bijlagen Utrechtse visie religieus erfgoed (2017)]] — Gemeente Utrecht, referentiemateriaal: tabellen orgels, klokken, ensembles
- [[Wiki/Bronsamenvattingen/Cultuur/archiefverordening-wageningen|Archiefverordening Wageningen 2019]] — Modelverordening Archiefwet 1995: zorgplicht B&W, taken gemeentearchivaris, duale positionering archief (erfgoed + informatiebeheer)
- [[Wiki/Bronsamenvattingen/Cultuur/memorie-van-toelichting-archiefwet|Memorie van toelichting Archiefwet 1995]] — Parlementaire toelichting: definities, overbrengingstermijn 20 jaar, digitale informatiedragers, levenscyclus archieven
- [[Wiki/Bronsamenvattingen/erfgoed/erfgoedwet|Erfgoedwet (BWBR0037521)]] — Wettekst per 2026-01-01: definities, collectiebeheer, beschermd erfgoed, archeologische monumentenzorg
- [[Wiki/Bronsamenvattingen/erfgoed/gr-regionaal-archief-rivierenland|GR Regionaal Archief Rivierenland 2024]] — GR-regeling: taken regionaal archief, uitgeplaatst beheer, bestuursstructuur
- [[Wiki/Bronsamenvattingen/erfgoed/besluit-informatiebeheer-gr-cure|Besluit Informatiebeheer GR Cure 2021]] — Operationele voorschriften: metadata-eisen, selectie/vernietiging, informatiebeveiliging
- [[Wiki/Bronsamenvattingen/erfgoed/beleidsplan-westfries-archief|Beleidsplan Westfries Archief 2024-2027]] — eDepot, pre-eDepot, digitale archivering, Woo-publicatie, inspectie

## Nog te verwerken bronnen

- [Sources/Onderwerpen/Cultuur/sport.md](Sources/Onderwerpen%20VNG/Cultuur/sport.md) — apart domein, niet relevant voor cultuur

## Openstaande vragen

- **Musea-domein** — 22 van 30 GGM Musea-entiteiten zijn Prinsenhof-specifiek (Balieverkoop, Winkelvoorraaditem, etc.). Met de Erfgoedwet is Collectie nu BO; Tentoonstelling en Bruikleen beoordeeld als operationeel (geen BO).
- **Archief** — Depot, Kast, Plank, Stelling zijn opslaglogistiek (geen BO). eDepot ontbreekt in GGM (hiaat). Pre-eDepot/uitplaatsing zijn praktijkconcepten buiten de Archiefwet.
- **Monument/Beschermde Status** — duplicaat geconsolideerd (2026-06-27). Monument is het primaire BO, Beschermde Status verwijderd als apart BO. GGM-entiteitnaam is "Beschermde Status", wiki-naam is "Monument" (herkenbaarder).
- **Groen/blauw erfgoed** — potentieel bij bronnen over groenbeleid/openbare ruimte.

## Terugmeldingen richting GGM

- **Orgel** — Registratieobject voor monumentale muziekinstrumenten in kerkgebouwen ontbreekt in GGM-beleidsdomein Monumenten. Roerend erfgoed met eigen monumentstatus, geïnventariseerd door gemeentelijke afdeling Erfgoed. Attributen: maker, bouwjaar, locatie, monumentstatus, bespeelbaarheid. Past onder beleidsdomein Monumenten (taakveld 5).
- **eDepot** — Digitale archiefbewaarplaats ontbreekt als concept in GGM. Het GGM kent alleen fysiek "Depot". Meerdere GR-archieven (Westfries Archief, Rivierenland) gebruiken eDepot als kerninfrastructuur voor digitale archivering.

Het ontbreken van een cultuurbeleid-domein in het GGM is structureel (GGM modelleert data, niet governance).
