---
type: onderwerp
naam: Basisregistraties
status: in-behandeling
verwerkingsdatum: 2026-06-25
bronnen_count: 4
begrippen_count: 44
bo_count: 23
---

## Beschrijving

Dit onderwerp omvat de gemeentelijke basisregistraties en hun objecttypen. Het GGM modelleert deze onder taakveld 99 Kern in de beleidsdomeinen BAG en RSGBPlus. De BAG (Basisregistratie Adressen en Gebouwen) is als eerste verwerkt.

De BAG-objecttypen vormen het fundament van de gemeentelijke informatiehuishouding: alle andere registraties (WOZ, BRP, vergunningen) koppelen aan BAG-objecten. De gebiedsindelingen (Gemeente, Woonplaats, Wijk, Buurt) zijn geen formele BAG-objecttypen maar vormen de ruimtelijke hiërarchie waarbinnen BAG-objecten zijn gelokaliseerd.

De BRP (Basisregistratie Personen) registreert persoonsgegevens van ingezetenen en niet-ingezetenen. De persoonslijst bevat 13 categorieën (persoon, ouders, nationaliteit, huwelijk, overlijden, verblijfplaats, kinderen, verblijfstitel, gezagsverhouding, reisdocumenten, kiesrecht). De BRP koppelt personen aan BAG-objecten via de verblijfplaatsgegevens.

De BRK (Basisregistratie Kadaster) bevat de registratie van onroerende zaken, zakelijke rechten en de kadastrale kaart. Het Kadaster is bronhouder; de gemeente is verplicht gebruiker van authentieke BRK-gegevens en bronhouder voor publiekrechtelijke beperkingen (WKPB). De kern: een Zakelijk Recht rust op een Kadastraal Perceel of Appartementsrecht, en is via een Tenaamstelling gekoppeld aan een Persoon (BRP/HR). Alle rechtswijzigingen traceren naar Stukken/Stukdelen in de openbare registers.

Het NHR (Nationaal Handelsregister) is de basisregistratie voor ondernemers en rechtspersonen, beheerd door de KvK. Het informatiemodel kent drie hoofdobjecttypen: Maatschappelijke Activiteit (het centrale object, geïdentificeerd met KVK-nummer), Niet-Natuurlijk Persoon (organisaties — het complement van Ingeschreven Persoon uit de BRP) en Vestiging (locatie waar activiteiten worden uitgeoefend, gekoppeld aan BAG-adressen). Samen met BRP, BAG en BRK vormt het NHR het fundament van de gemeentelijke informatiehuishouding.

## Begrippentabel

### BAG — Adresobjecten

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] | object | Door de gemeente aangewezen en benoemd gedeelte van het grondgebied | ✅ | ja | 6/6 criteria, exact match | Utrecht, De Meern, Vleuten | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] | object | Benoemde buitenruimte binnen één woonplaats (straatnaam) | ✅ | ja | 6/6 criteria, exact match | Oudegracht, Biltstraat | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | object | Formeel adres: huisnummer + postcode | ✅ | ja | 6/6 criteria, exact match, universeel koppelpunt | Oudegracht 100, 3511 AX | ja |

### BAG — Gebouwobjecten

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bag/pand\|Pand]] | object | Bouwkundig-constructief zelfstandige eenheid | ✅ | ja | 6/6 criteria, exact match | Woonhuis, kantoorgebouw, flat | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject\|Verblijfsobject]] | object | Eenheid van gebruik binnen pand(en) | ✅ | ja | 6/6 criteria, exact match | Woning, kantoor, winkel | ja |

### BAG — Adresseerbare objecten

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats\|Ligplaats]] | object | Aangewezen plaats in het water voor drijvend object | ✅ | ja | 6/6 criteria, exact match, eerder BO | Woonbootligplaats | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats\|Standplaats (BAG)]] | object | Aangewezen terrein voor verplaatsbare ruimte (woonwagen) | ✅ | ja | 6/6 criteria, exact match | Woonwagenstandplaats | ja |
| Adresseerbaar object | object | Abstract type waarvan Verblijfsobject, Ligplaats, Standplaats overerven | ❌ | nee | Abstract, geen concreet object | — | ja |

### Gebiedsindeling

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] | object | Grondwettelijk ingesteld gedeelte van Nederland | ✅ | ja | 6/6 criteria, exact match | Utrecht, Amersfoort | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] | object | Gebiedsdeel begrensd op sociaal-geografische kenmerken | ✅ | ja | 6/6 criteria, exact match | Binnenstad, Overvecht | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt\|Buurt]] | object | Gebiedsdeel begrensd op topografische elementen | ✅ | ja | 6/6 criteria, exact match | Lombok, Wittevrouwen | ja |

### BAG — Overig

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| Gebruiksdoel | waarde | Categorisering van vergund gebruik verblijfsobject | ❌ | nee | Attribuut van Verblijfsobject, geen object | Wonen, kantoor, winkel | ja (enum) |
| Hoofdadres / nevenadres | thema | Onderscheid primair en secundair adres | ❌ | nee | Relatie-eigenschap, geen object | — | nee |

### BRP — Personen

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | object | Persoon met persoonslijst in de BRP | ✅ | ja | 6/6 criteria, exact match, kern van gemeentelijke dienstverlening | Inwoner met BSN | ja |
| Ingezetene | subtype | Ingeschreven bij een gemeente, volledige PL | ❌ | nee | Subtype van Ingeschreven Persoon | — | ja |
| Niet-ingezetene | subtype | Ingeschreven in de RNI, beperkte PL | ❌ | nee | Subtype van Ingeschreven Persoon | — | nee |

### BRP — Verbintenissen en documenten

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk\|Huwelijk]] | object | Geregistreerd huwelijk of geregistreerd partnerschap | ✅ | ja | 6/6 criteria, eigen levenscyclus (sluiting→ontbinding), meervoudig | Huwelijk, geregistreerd partnerschap | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] | object | Nederlands paspoort of identiteitskaart | ✅ | ja | 6/6 criteria, fysiek object, eigen levenscyclus, meervoudig | Paspoort, ID-kaart | ja |

### BRP — Persoonsgegevens (geen apart BO)

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| Nationaliteit | attribuut | Hoedanigheid van tot een natie te behoren | ❌ | nee | Eigenschap van persoon, geen zelfstandig object | Nederlandse, Turkse | ja |
| Verblijfstitel | attribuut | Verblijfsrechtelijke status van vreemdeling | ❌ | nee | Koppelgegeven (aangeleverd door IND) | Regulier bepaalde tijd | ja |
| Gezagsverhouding | attribuut | Gezag over minderjarige of curatele | ❌ | nee | Juridische status, geen object | Ouderlijk gezag, voogdij | ja |
| Kiesrecht | attribuut | Europees kiesrecht en uitsluiting | ❌ | nee | Statusattributen van persoon | — | ja |
| Overlijden | gebeurtenis | Overlijdensdatum, -plaats en -land | ❌ | nee | Eenmalige gebeurtenis, attribuut van persoon | — | ja |

### BRK — Kadastrale objecten

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | object | Begrensd deel van het grondgebied met kadastrale aanduiding | ✅ | ja | 6/6 criteria, exact match | Perceel UTN00-A-1234 | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] | object | Aandeel in gesplitst gebouw met exclusief gebruiksrecht | ✅ | ja | 6/6 criteria, exact match | Appartement in gesplitst pand | ja |
| Kadastraal Object | object | Abstract: generalisatie van Perceel en Appartementsrecht | ❌ | ja | Abstract type, geen concreet object | — | ja (abstract) |
| Onroerende Zaak | object | Abstract: groupering van Perceel, Appartementsrecht, Leidingnetwerk | ❌ | ja | Abstract type | — | ja (abstract) |
| Leidingnetwerk | object | Kadastraal object voor leidinginfrastructuur | ❌ | ja | Nutsbedrijf-scope, niet gemeentelijk | Gasleiding, waterleiding | ja |

### BRK — Rechten en tenaamstelling

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | object | Eigendom of beperkt recht op een onroerende zaak | ✅ | ja | 6/6 criteria, exact match | Eigendom, erfpacht, opstal | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling\|Tenaamstelling]] | object | Koppeling recht↔persoon: wie oefent welk recht uit | ✅ | ja | 6/6 criteria, exact match | Eigenaar van perceel X | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/zekerheidsrecht\|Zekerheidsrecht]] | object | Hypotheek of beslag op een onroerende zaak | ✅ | ja | 6/6 criteria, exact match | Hypotheek, fiscaal beslag | ja |
| Aantekening | object | Bijzonderheid bij kadastraal object of recht | ❌ | ja | Procesnotitie, geen zelfstandig object | Erfdienstbaarheid, einddatum recht | ja |

### BRK — Publiekrechtelijke beperkingen

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brk/publiekrechtelijke-beperking\|Publiekrechtelijke Beperking]] | object | Beperkingsbesluit van bestuursorgaan op onroerende zaak (WKPB) | ✅ | ja | 6/6 criteria, gemeente is bronhouder, GGM-hiaat | Monument, milieubeperking, Wvg | nee (hiaat) |

### BRK — Brondocumenten

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stuk\|Stuk]] | object | Brondocument in openbare registers (akte, kadasterstuk) | ✅ | ja | 6/6 criteria, authentieke gegevens, GGM-hiaat | Notariële akte, WKPB-besluit | nee (hiaat) |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stukdeel\|Stukdeel]] | object | Onderdeel van stuk met rechtsfeiten | ✅ | ja | 5/6 criteria (compositie), GGM-hiaat | Overdracht, hypotheekvestiging | nee (hiaat) |

### BRK — Overig (geen BO)

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| Kadastrale kaart | object | Landelijke kaart met perceelsgrenzen en aanduidingen | ❌ | nee | Informatieproduct, geen registratieobject | — | nee |
| Terugmelding | proces | Melding van gerede twijfel over authentiek BRK-gegeven | ❌ | nee | Processtap, geen zelfstandig object | — | nee |

### NHR — Hoofdobjecten

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit\|Maatschappelijke Activiteit]] | object | Activiteit van een persoon of organisatie, geregistreerd met KVK-nummer | ✅ | ja | 6/6 criteria, exact match, kern NHR | Onderneming, stichting zonder winstoogmerk | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | object | Organisatie of samenwerkingsverband met rechtspersoonlijkheid | ✅ | ja | 6/6 criteria, exact match, complement van Ingeschreven Persoon | BV, NV, stichting, vereniging | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | object | Locatie waar een onderneming of rechtspersoon activiteiten uitoefent | ✅ | ja | 6/6 criteria, exact match, koppelpunt beleid↔locatie | Kantoor, winkel, fabriek | ja |

### NHR — Overig (geen BO)

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| Onderneming | classificatie | Economische activiteit die voldoet aan wettelijke criteria | ❌ | nee | Kwalificatie van MA (indicatieEconomischActief), geen apart objecttype | — | nee (attribuut) |
| Rechtspersoon | object | Generalisatie van NatuurlijkPersoon en NietNatuurlijkPersoon | ❌ | ja | Abstract type, te generiek voor BO | — | ja (abstract) |
| Handelsnaam | attribuut | Naam waaronder een onderneming of vestiging handelt | ❌ | nee | Gegevensgroep, meervoudig attribuut | "Albert Heijn" | ja (groepattribuut) |
| SBI-code | classificatie | Standaard Bedrijfsindeling: classificatie bedrijfsactiviteiten | ❌ | nee | Referentietabel, geen object | 47.11 — supermarkt | ja (groepattribuut) |
| UBO | attribuut | Uiteindelijk belanghebbende met economisch belang >25% | ❌ | nee | Compliance-gegeven, niet gemeentelijk geregistreerd | — | nee |
| Functionaris | rol | Persoon met bestuurlijke of vertegenwoordigingsfunctie | ❌ | nee | Rol (relatie), geen zelfstandig object | Bestuurder, commissaris | nee |
| Faillissement | status | Bijzondere rechtstoestand van persoon of MA | ❌ | nee | Attribuut (datumFaillisement) | — | nee (attribuut) |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018|Catalogus BAG 2018]]
- [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1|Logisch Ontwerp BRP 2025.Q1]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk|Catalogus BRK 2020]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-nhr|Gegevenscatalogus NHR 3.0.4]]

## Nog te verwerken

De volgende basisregistraties zijn nog niet verwerkt. Per registratie zijn geschikte bronnen gesuggereerd:

- **RSGBPlus overige entiteiten** — referentietabellen, detail-entiteiten, IMGeo/BGT

## Openstaande vragen

- **Standplaats-disambiguatie**: de GGM-entiteit "Standplaats" (RSGBPlus, EAID_B1C6CA45) was eerder foutief gematcht op [[Marktstandplaats]] (Economie). Nu gecorrigeerd: de GGM-entiteit hoort bij [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]]. De marktstandplaats is een GGM-hiaat.
