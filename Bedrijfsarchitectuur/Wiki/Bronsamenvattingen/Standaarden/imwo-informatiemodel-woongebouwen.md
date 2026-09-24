---
type: bronsamenvatting
titel: "digiGO Informatiemodel Woongebouwen (IMWO)"
onderwerp: [Standaarden, Wonen]
datum_ingest: 2026-09-24
---

## Samenvatting

Het IMWO (v1.0, juli 2026) is een formeel conceptueel informatiemodel van digiGO voor woning en woongebouw, ontwikkeld door ketenpartners (VNG, Kadaster, Aedes, Rijksvastgoedbedrijf, Neprom, Techniek Nederland e.a.) die vaststelden dat gegevens over woningen niet goed uitwisselbaar zijn omdat elke partij eigen definities hanteert. Het IMWO is expliciet **een uitwerking van het GEBORA-bedrijfsobjectenmodel** ([[Wiki/Bronsamenvattingen/Standaarden/gebora-conceptueel-informatiemodel|GEBORA]]), specifiek van informatiedomein 1 (Bouwwerk). Het model is gebaseerd op de internationale standaarden IFC en CityGML en de nationale standaarden NEN 2660 en NEN 3610; voor zakelijke rechten wordt aangesloten op het Kadaster-informatiemodel IMKAD.

Het model bevat ~200 formeel gedefinieerde objecttypen (elk met schema, model, term, formele/informele definitie, bronterm, brondefinitie en identificatie/GUID) plus hun onderlinge relaties, verdeeld over submodellen:
- **Top** — abstracte metamodel-concepten (Object, Entiteit, Concept, FysiekObject, GeoObject, Ruimte-varianten) — generalisatiewortels, geen concrete objecten
- **Bouwwerken** — Bouwwerk, Gebouw, BouwComplex, Terrein, Verdieping, BrandCompartiment e.d.
- **Bouwcomponenten** — losse bouwkundige onderdelen (Kolom, Balk, Dak, Deur, Fundering, Wand, Vloer, ...)
- **Woonobjecten** — Woning, WoonGebouw, WoonObject, WoonEenheid(enObject), architecturale woningtypen (EengezinsWoning, MeergezinsWoning, VrijstaandeWoning, TweeOnderEenKapWoning, HoekWoning, TussenWoning, GalerijWoning, PortiekWoning, Maisonnette, Boven-/BenedenWoning, WoningBovenBedrijfsRuimte) en doelgroep-aanduidingen (Arbeidsmigranten, Asielzoekers, Studenten, Woongroepen, BewonersInZorgInstelling)
- **Woonobjectruimten** — kamerniveau (Keuken, Slaapkamer, Garage, Berging, Zolder, ...)
- **Installaties**, **Slimme woning**, **Binnenruimtenetwerk** — technische bouwwerkinstallaties en -sensoriek
- **Juridische objecten** — GemeenschappelijkeRuimte, PrivéRuimte (rechten, aansluitend op IMKAD)

De hiërarchie in het submodel Bouwwerken is: Bouwwerk (algemeen, elke constructie) → Gebouw (specialisatie: afsluitbaar, met verblijfsfunctie) → WoonGebouw (Gebouw met woonfunctie, kan meerdere wooneenheden bevatten) → WoonObject/Woning/WoonEenheid (individuele bewoonbare eenheid). Dit is fijnmaziger dan het huidige GGM, waar "Gebouw" (GGM-entiteit uit Model Wonen) direct is hernoemd tot de BO [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/bouwen-en-wonen/woning|Woning]] zonder aparte tussenlaag voor het pand/gebouw waarin de woning zich bevindt — die laag wordt in de wiki al gedekt door de bestaande BO's Pand (BAG) en Overig Gebouwd Object (RSGBPlus). GGM's eigen enumeratie `soortWoonobject` (Model BAG én RSGBPlus/Enumeratiesoort) staat wel in het model maar heeft in de geëxporteerde XMI **geen ingevulde literalen** — de architecturale woningtypen die IMWO wél expliciet benoemt, ontbreken dus feitelijk in het GGM.

De submodellen Bouwcomponenten, Woonobjectruimten (kamerniveau), Installaties, Slimme woning en Binnenruimtenetwerk beschrijven bouwkundige/technische detaillering die buiten het gemeentelijk registratieperspectief valt ([WC4]/[WC5]) en is niet verder beoordeeld.

## Kernbegrippen

- **Bouwwerk, Gebouw** — generalisatiewortels; al gedekt door bestaande BO's [[Wiki/Bedrijfsobjecten/99-kern/bag/pand|Pand]] (BAG), [[Wiki/Bedrijfsobjecten/99-kern/bgt/overig-bouwwerk|Overig Bouwwerk]] (BGT) en [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-gebouwd-object|Overig Gebouwd Object]] (RSGBPlus) — vergelijkbaar met eerder afgewezen abstracte generalisaties (Benoemd Object, Gebouwd Object) bij de RSGB-ingest.
- **WoonGebouw** — Gebouw met woonfunctie dat meerdere wooneenheden kan bevatten; te vergelijken met [[Wiki/Bedrijfsobjecten/99-kern/bag/pand|Pand]] specifiek in woonfunctie-context.
- **WoonObject, WoonEenheid, WoonEenhedenObject** — generalisatielaag boven individuele woningen; komt overeen met de bestaande BO [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/bouwen-en-wonen/woning|Woning]] (hernoeming van GGM-entiteit Gebouw uit Model Wonen).
- **Architecturale woningtypen** (EengezinsWoning, MeergezinsWoning, VrijstaandeWoning, TweeOnderEenKapWoning, HoekWoning, TussenWoning, GalerijWoning, PortiekWoning, Maisonnette, Boven-/BenedenWoning, WoningBovenBedrijfsRuimte) — nieuwe classificatie-as naast de bestaande, huur/koop-gebaseerde `bo_subtypes` van [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/bouwen-en-wonen/woning|Woning]] (sociale huurwoning, middenhuurwoning, betaalbare koopwoning, studentenwoning).
- **Doelgroep-woonvormen** (Arbeidsmigranten, Asielzoekers, Studenten, Woongroepen, BewonersInZorgInstelling) — raakt het reeds ge-ingeste [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wonen-voor-aandachtsgroepen|wonen-voor-aandachtsgroepen]] (Maatschappelijke Ondersteuning-domein).
- **Terrein, BouwComplex, Verdieping** — Terrein komt overeen met [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-terrein|Overig Terrein]]; BouwComplex (cluster van gebouwen) en Verdieping hebben geen directe bestaande tegenhanger.

## Relevantie voor bedrijfsarchitectuur

Het IMWO bevestigt in hoofdlijnen het bestaande BAG/RSGBPlus/Wonen-model, met als belangrijkste concrete aanvulling: een expliciete, structurele lijst van architecturale woningtypen die het GGM zelf niet (met ingevulde literalen) modelleert. Dit is een kandidaat-verrijking voor `bo_subtypes` van de BO Woning en een kandidaat-terugmelding richting het GGM-beheer (lege enumeratie `soortWoonobject`).

> "IMWO is een uitwerking van het Bedrijfsobjectenmodel (domein Bouwwerk). Het IMWO is een conceptueel informatiemodel, dat de betekenis en de structuur van de relevante informatie beschrijft, onafhankelijk van het ontwerp van en de implementatie in systemen." (bron: imwo-informatiemodel-woongebouwen.md, Uitgangspunten)

> "Gebouw — specialisatie van Bouwwerk, waaraan iets toegevoegd wordt (zoals dat het afsluitbaar is en een verblijfsfunctie heeft)." (bron: imwo-informatiemodel-woongebouwen.md, Semantiek — parafrase van de formele definitie)

## Bronnen

- [[Sources/Standaarden/imwo-informatiemodel-woongebouwen]]
