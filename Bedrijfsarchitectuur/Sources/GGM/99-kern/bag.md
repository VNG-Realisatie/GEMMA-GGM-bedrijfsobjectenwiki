---
type: ggm-beleidsdomein
naam: BAG
definitie: "Het subdomein dat gegevens omvat over adressen en gebouwen in Nederland, gebaseerd op het Informatiemodel BAG (IMBAG), waarbij uitsluitend die elementen zijn opgenomen die relevant zijn voor gemeenten en andere lagere overheden."
taakveld: "99 Kern"
aantal_entiteiten: 13
---

# GGM Beleidsdomein: BAG

Beleidsdomein binnen taakveld "99 Kern" (zie ../structuur-ggm.md).

## Entiteiten

### BAG

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AdresseerbaarObject** | Een adresseerbaar object is een object waaraan formeel adressen kunnen en moeten worden toegekend: een verblijfsobject, standplaats of ligplaats. Toelichting: Een object dat een adres heeft of krijgt. Adresseerbare objecten zijn: een verblijfsobject, een standplaats en een ligplaats. | identificatie, versie, typeAdresseerbaarObject | Nee | IMBAG |
| **Buurt** | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | code, naam, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, status, datumEinde, versie, Geconstateerd | Nee | IMBAG |
| **Gemeente** | Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet. | gemeentecode, gemeentenaam, gemeentenaam NEN, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, datumEinde, versie, Geconstateerd | Nee | Door KING toegevoegd objecttype,ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie). |
| **Ligplaats** | Definitie Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object Beschrijving Een plaats in het water met soms ook een (deel van een) terrein op de oever. Deze plaats moet kunnen worden gebruikt door een drijvend object dat langere tijd daar wordt vastgemaakt. Het drijvende object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Bijvoorbeeld een woonboot. De gemeente mag zeggen of er voor de BAG ergens een ligplaats komt. | identificatie, geconstateerd, status, documentdatum, documentnummer, versie, geometrie, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde | Nee | GGM |
| **Nummeraanduiding** | Een nummeraanduiding is een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een verblijfsobject, een standplaats of een ligplaats. | huisletter, huisnummer, huisnummertoevoeging, postcode, beginGeldigheid, eindeGeldigheid, status, geconstateerd, identificatie, typeAdresseerbaarObject, datumIngang, datumEinde, versie, geometrie, documentdatum, documentnummer | Ja | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **OpenbareRuimte** | Een openbare ruimte is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen &#233;&#233;n woonplaats is gelegen. Beschrijving: Een buitenruimte die door de gemeente als openbare ruimte is aangewezen en waaraan de gemeente een naam heeft gegeven. Een openbare ruimte ligt binnen 1 woonplaats. De BAG kent 7 soorten openbare ruimten: weg, water, spoorbaan, terrein, kunstwerk, landschappelijk gebied en administratief gebied. Een openbare ruimte is meestal een straat(naam). | identificatie, status, naamOpenbareruimte, geconstateerd, typeOpenbareruimte, straatnaam, Huisnummerrange even nummers, Huisnummerrange oneven nummers, Huisnummerrange even en oneven nummers, labelNaam, geometrie, wegsegment, begingeldigheid, eindGeldigheid, straatcode, versie, datumIngang, datumEinde, documentdatum, documentnummer | Nee | IMBAG |
| **Pand** | Een pand is een kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is. Beschrijving: Een zelfstandig bouwwerk, zowel zelfstandig in de manier hoe het is gebouwd als waarvoor het is bedoeld om te gebruiken. Een pand voldoet ook aan de volgende eisen: een pand is direct en voor lange tijd met de aarde verbonden (een pand is niet makkelijk te verplaatsen) en een pand kun je binnengaan en afsluiten. Een eenheid kan alleen een pand zijn als het voldoet aan alle eisen uit de Catalogus BAG 2018. | identificatie, status, statusVoortgangBouw, oorspronkelijkBouwjaar, oppervlakte, brutoInhoudPand, geconstateerd, hoogsteBouwlaag, laagsteBouwlaag, geometrieBovenaanzicht, geometrieMaaiveld, relatieveHoogteligging, documentnummer, documentdatum, beginGeldigheid, eindGeldigheid, geometriePunt, datumIngang, versie, datumEinde | Nee | IMBAG |
| **Standplaats** | Een standplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte. Beschrijving: Een terrein of een deel daarvan dat moet kunnen worden gebruikt om langere tijd een object neer te zetten. Dit object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Het moet verplaatsbaar zijn en mag dus niet helemaal vastgemaakt worden aan de grond. Bijvoorbeeld een woonwagen of strandtent. De gemeente mag zeggen of er voor de BAG ergens een standplaats komt. | Identificatie, Geconstateerd, Status, Versie, Geometrie, documentdatum, documentnummer, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde | Nee | GGM |
| **Verblijfsobject** | Een verblijfsobject is een kleinste binnen &#233;&#233;n of meer panden gelegen en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is. Beschrijving: Een verblijfsobject is een ruimte in 1 of meer panden en voldoet aan de volgende eisen: kan worden gebruikt om in te wonen, een bedrijf in te hebben of om voor plezier in te verblijven, is bereikbaar via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, kan worden gekocht en verkocht, kan helemaal zelf worden gebruikt voor het doel dat ervoor is gegeven. Deze eisen voor verblijfsobjecten worden toegelicht in de Catalogus BAG 2018. Een verblijfsobject krijgt een adres. | identificatie, status, geconstateerd, hoogsteBouwlaag, laagsteBouwlaag, toegangBouwlaag, soortWoonobject, aantalKamers, ontsluitingVerdieping, documentnummer, documentdatum, geometrie, Versie, gebruiksdoel, beginGeldigheid, eindGeldigheid, datumEinde, datumIngang, oppervlakte | Nee | GGM |
| **Wijk** | Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken. | wijkcode, wijknaam, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, status, datumEinde, versie, Geconstateerd | Nee | IMBAG |
| **Woonplaats** | Een woonplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente Beschrijving: Een stuk grond binnen de gemeente dat als woonplaats is aangewezen en waaraan de gemeente ook een naam heeft gegeven. | identificatie, woonplaatsnaam, woonplaatsnaamNEN, geconstateerd, status, geometrie, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde, versie, documentnummer, documentdatum, voorkomen, tijdstipRegistratie, eindRegistratie, tijdstipActief | Nee | IMBAG |

### ONDERZOEK

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Onderzoek** | Basisinformatie zet een kenmerk, waarvan een formele terugmelding of correctieverzoek niet binnen twee werkdagen is afgehandeld, in de Basisregistratie adressen en gebouwen in onderzoek. | documentnummer, documentdatum, beginGeldigheid, eindGeldigheid, tijdstipRegistratie, eindRegistratie, identificatie, volgnummer, objecttype, inOnderzoek, datumActueelTot, kenmerk, objectIdentificatie | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **BinnenlandsAdres** | De adresaanduiding van het WOZ-OBJECT | straatnaam, gemeentenaam, huisnummer, huisletter, huisnummertoevoeging, postcode, BAGID | Nee | GGM |

## Overervingshiërarchie

```
AdresseerbaarObject (abstract)
    └── BenoemdTerrein
    └── Ligplaats
    └── OverigBenoemdTerrein
    └── OverigGebouwdObject
    └── Standplaats
    └── Verblijfsobject
```

```
Geo-Object (abstract)
    └── Pand
```

```
Nummeraanduiding (abstract)
    └── NADAanvullingBRP
    └── OverigeAdresseerbaarObjectAanduiding
```

```
Object (abstract)
    └── AdresseerbaarObject
```

## Relatiediagrammen

### BAG

```
Adresaanduiding [0..1] ──── Nummeraanduiding [0..1] (verwijst naar)
AdresseerbaarObject [1] ──── Nummeraanduiding [1] (Heeft als hoofdadres)
AdresseerbaarObject [1] ──── Nummeraanduiding [0..*] (Heeft als Nevenadres)
AdresseerbaarObject [1] ──── Winkelvloeroppervlak [0..1] (heeft)
Areaal [0..*] ──── Buurt [1..*] (ligt in)
Areaal [0..*] ──── Wijk [1..*] (valt binnen)
Asielstatushouder [0..*] ──── Gemeente [0..1] (is gekoppeld aan)
Beschermde Status [0..1] ──── OpenbareRuimte [0..*] (betreft)
Binnenlocatie [0..*] ──── Verblijfsobject [0..1] (is gevestigd in)
Binnenlocatie [0..*] ──── Wijk [1] (bedient)
Briefadres [0..*] ──── Nummeraanduiding [1]
Buurt [1..*] ──── Wijk [1] (ligt in)
Gebied [0..1] ──── Buurt [0..1] (komt overeen)
GeboorteIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (heeft plaatsgevonden in)
Gemeente [0..*] ──── Gemeente [0..*] (is overgegaan in)
Huishouden [0..*] ──── Nummeraanduiding [1] (heeft als adres)
IngeschrevenPersoon [0..*] ──── Nummeraanduiding [0..1] (heeft als adres)
Locatieonroerendezaak [0..*] ──── AdresseerbaarObject [1] (heeft Adresseerbaar object)
Nummeraanduiding [1] ──── Buurt [1] (Ligt in)
Nummeraanduiding [0..*] ──── Gebied [0..*] (ligt in)
Nummeraanduiding [0..1] ──── LocatieaanduidingWozObject [1] (verwijst naar)
Nummeraanduiding [0..*] ──── OpenbareRuimte [1] (Ligt aan)
Nummeraanduiding [1] ──── Vestiging [0..*] (heeft als locatie-adres)
Nummeraanduiding [0..*] ──── Woonplaats [0..1] (Ligt in)
Object [0..1] ──── Buurt [0..*] (is)
Object [0..1] ──── Ligplaats [0..*] (is)
Object [0..1] ──── OpenbareRuimte [0..*] (is)
Object [0..1] ──── Pand [0..*] (is)
Object [0..1] ──── Standplaats [0..*] (is)
Onderzoek [0..1] ──── Ligplaats [1] (objectidentificatie)
Onderzoek [0..1] ──── Nummeraanduiding [1] (objectidentificatie)
Onderzoek [0..1] ──── OpenbareRuimte [1] (objectidentificatie)
Onderzoek [0..1] ──── Pand [1] (objectidentificatie)
Onderzoek [0..1] ──── Standplaats [1] (objectidentificatie)
Onderzoek [0..1] ──── Verblijfsobject [1] (objectidentificatie)
Onderzoek [0..1] ──── Woonplaats [1] (objectidentificatie)
OntbindingHuwelijk/geregistreerdPartnerschap [0..*] ──── Woonplaats [0..1] (is ontbonden in)
OpenbareRuimte [1] ──── Buurt [1..*] (Ligt in)
OpenbareRuimte [1] ──── Buurt [1] (ligt in)
OpenbareRuimte [1..*] ──── Woonplaats [1] (Ligt in)
OverlijdenIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (heeft plaatsegevonden in)
Pand [0..*] ──── Buurt [0..1] (zonder verblijfsobject ligt in)
Pand [1] ──── Vastgoedobject [1] (heeft)
Postadres [0..*] ──── Woonplaats [1] (heeft als correspondentieadres postadres in)
Schuldhulptraject [0..*] ──── Gemeente [1] (onder verantwoordelijkheid van)
SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap [0..*] ──── Woonplaats [0..1] (is gesloten/aangegaan in)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── AdresseerbaarObject [0..1] (is ingeschreven op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Ligplaats [0..1] (verblijft op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Standplaats [0..1] (verblijft op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Verblijfsobject [0..1] (verblijft in)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (verblijft op)
Verblijfsobject [0..*] ──── Pand [1..*] (Maakt deel uit van)
Verblijfsobject [1] ──── Vastgoedobject [1] (heeft)
Vestiging [0..*] ──── AdresseerbaarObject [0..1] (heeft nevenlocatie in of op)
Vestiging [0..*] ──── AdresseerbaarObject [0..1] (heeft hoofdlocatie in of op)
Vroegsignaalzaak [0..*] ──── Gemeente [1] (opgepaktNamens)
WOZ-deelobject [1..*] ──── AdresseerbaarObject [0..1] (bestaat uit)
WOZ-deelobject [0..*] ──── Pand [0..1] (bestaat uit)
WOZ-object [0..*] ──── OpenbareRuimte [0..1] (ligt aan)
Wijk [1..*] ──── Woonplaats [1] (Ligt in)
Wijk [1..*] ──── Woonplaats [1] (ligt in)
Woonplaats [1..*] ──── Gemeente [1..] (Ligt in)
```

### ONDERZOEK

```
Onderzoek [0..1] ──── Ligplaats [1] (objectidentificatie)
Onderzoek [0..1] ──── Nummeraanduiding [1] (objectidentificatie)
Onderzoek [0..1] ──── OpenbareRuimte [1] (objectidentificatie)
Onderzoek [0..1] ──── Pand [1] (objectidentificatie)
Onderzoek [0..1] ──── Standplaats [1] (objectidentificatie)
Onderzoek [0..1] ──── Verblijfsobject [1] (objectidentificatie)
Onderzoek [0..1] ──── Woonplaats [1] (objectidentificatie)
```

## Observaties

- Dit beleidsdomein bevat 13 entiteiten.
- Entiteiten zijn gegroepeerd in 3 diagramgroepen: BAG (11), ONDERZOEK (1), Overig (1).
- Er zijn 11 generalisatierelaties aanwezig.
- 1 entiteit is abstract.
