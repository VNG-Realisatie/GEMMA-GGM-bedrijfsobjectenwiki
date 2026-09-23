---
type: onderwerp
naam: Basisregistraties
status: in-behandeling
verwerkingsdatum: 2026-06-27
bronnen_count: 6
begrippen_count: 57
bo_count: 26
---

## Beschrijving

Dit onderwerp omvat de gemeentelijke basisregistraties en hun objecttypen. Het GGM modelleert deze onder taakveld 99 Kern in de beleidsdomeinen BAG en RSGBPlus. De BAG (Basisregistratie Adressen en Gebouwen) is als eerste verwerkt.

De BAG-objecttypen vormen het fundament van de gemeentelijke informatiehuishouding: alle andere registraties (WOZ, BRP, vergunningen) koppelen aan BAG-objecten. De gebiedsindelingen (Gemeente, Woonplaats, Wijk, Buurt) zijn geen formele BAG-objecttypen maar vormen de ruimtelijke hiërarchie waarbinnen BAG-objecten zijn gelokaliseerd.

De BRP (Basisregistratie Personen) registreert persoonsgegevens van ingezetenen en niet-ingezetenen. De persoonslijst bevat 13 categorieën (persoon, ouders, nationaliteit, huwelijk, overlijden, verblijfplaats, kinderen, verblijfstitel, gezagsverhouding, reisdocumenten, kiesrecht). De BRP koppelt personen aan BAG-objecten via de verblijfplaatsgegevens.

De BRK (Basisregistratie Kadaster) bevat de registratie van onroerende zaken, zakelijke rechten en de kadastrale kaart. Het Kadaster is bronhouder; de gemeente is verplicht gebruiker van authentieke BRK-gegevens en bronhouder voor publiekrechtelijke beperkingen (WKPB). De kern: een Zakelijk Recht rust op een Kadastraal Perceel of Appartementsrecht, en is via een Tenaamstelling gekoppeld aan een Persoon (BRP/HR). Alle rechtswijzigingen traceren naar Stukken/Stukdelen in de openbare registers.

Het NHR (Nationaal Handelsregister) is de basisregistratie voor ondernemers en rechtspersonen, beheerd door de KvK. Het informatiemodel kent drie hoofdobjecttypen: Maatschappelijke Activiteit (het centrale object, geïdentificeerd met KVK-nummer), Niet-Natuurlijk Persoon (organisaties — het complement van Ingeschreven Persoon uit de BRP) en Vestiging (locatie waar activiteiten worden uitgeoefend, gekoppeld aan BAG-adressen). Samen met BRP, BAG en BRK vormt het NHR het fundament van de gemeentelijke informatiehuishouding.

## Stelselrollen

Er is een stelselbreed rollenmodel. De relevante rollen voor de gemeente:

| Rol | Gemeentelijke context | Basisregistraties |
|---|---|---|
| [[Wiki/Rollen/bronhouder\|Bronhouder]] | Verantwoordelijk voor aanlevering en kwaliteit | BAG, BRP, BRO, WOZ |
| [[Wiki/Rollen/afnemer-basisregistraties\|Afnemer]] | Verplicht gebruiker van authentieke gegevens (gebruiksplicht) | BRK, NHR, alle overige |
| [[Wiki/Rollen/terugmelder\|Terugmelder]] | Plicht bij gerede twijfel over authentiek gegeven | Alle — melding bij bronhouder |
| [[Wiki/Rollen/dataleverancier\|Dataleverancier]] | Partij die namens bronhouder aanlevert | BRO (leveranciers), BAG (softwareleveranciers) |
| [[Wiki/Rollen/belanghebbende\|Belanghebbende]] | Rechthebbende/gebruiker van het object | WOZ (eigenaar, gebruiker) |

Per registratie zijn er ook niet-gemeentelijke rollen:

| Rol               | Type  | Omschrijving                                                     | Andere partijen                         |
| ----------------- | ----- | ---------------------------------------------------------------- | --------------------------------------- |
| registratiehouder | actor | Minister of wettelijk aangewezen partij die de registratie houdt | BZK (BRO, BRP), BZK (BAG)               |
| beheerder (LV)    | actor | Operationeel beheerder van de landelijke voorziening             | Kadaster (LV BAG, WOZ, BRK), PDOK (BRO) |

Dit zijn allemaal actoren, geen BO's zelf. Maar ze horen als cross-cutting begrippen in dit onderwerpoverzicht, omdat ze de verantwoordelijkheidsverdeling vastleggen die bij elke basisregistratie terugkomt.

## Begrippentabel

### BAG — Basisregistratie Adressen en Gebouwen

Gemeente is **bronhouder**. Beheerder LV: Kadaster.

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] | object | BAG | Door de gemeente aangewezen en benoemd gedeelte van het grondgebied | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] | object | BAG | Benoemde buitenruimte binnen één woonplaats (straatnaam) | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | object | BAG | Formeel adres: huisnummer + postcode | ✅ | exact match, universeel koppelpunt | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/pand\|Pand]] | object | BAG | Bouwkundig-constructief zelfstandige eenheid | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject\|Verblijfsobject]] | object | BAG | Eenheid van gebruik binnen pand(en) | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats\|Ligplaats]] | object | BAG | Aangewezen plaats in het water voor drijvend object | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats\|Standplaats (BAG)]] | object | BAG | Aangewezen terrein voor verplaatsbare ruimte (woonwagen) | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] | object | gebiedsindeling | Grondwettelijk ingesteld gedeelte van Nederland | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] | object | gebiedsindeling | Gebiedsdeel begrensd op sociaal-geografische kenmerken | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt\|Buurt]] | object | gebiedsindeling | Gebiedsdeel begrensd op topografische elementen | ✅ | exact match | ja |
| Adresseerbaar object | object | BAG | Abstract type: Verblijfsobject, Ligplaats, Standplaats | ❌ | abstract | ja |
| Gebruiksdoel | waarde | BAG | Categorisering vergund gebruik verblijfsobject | ❌ | attribuut | ja (enum) |

### BRP — Basisregistratie Personen

Gemeente is **bronhouder** (bijhoudingsautoriteit). Systeemverantwoordelijke: Minister BZK.

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | object | BRP | Persoon met persoonslijst in de BRP | ✅ | exact match, kern gemeentelijke dienstverlening | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk\|Huwelijk]] | object | BRP | Geregistreerd huwelijk of geregistreerd partnerschap | ✅ | eigen levenscyclus (sluiting→ontbinding) | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] | object | BRP | Nederlands paspoort of identiteitskaart | ✅ | fysiek object, eigen levenscyclus | ja |
| Ingezetene | subtype | BRP | Ingeschreven bij een gemeente, volledige PL | ❌ | subtype Ingeschreven Persoon | ja |
| Niet-ingezetene | subtype | BRP | Ingeschreven in de RNI, beperkte PL | ❌ | subtype Ingeschreven Persoon | nee |
| Nationaliteit | attribuut | BRP | Hoedanigheid van tot een natie te behoren | ❌ | eigenschap van persoon | ja |
| Verblijfstitel | attribuut | BRP | Verblijfsrechtelijke status vreemdeling | ❌ | koppelgegeven (IND) | ja |
| Gezagsverhouding | attribuut | BRP | Gezag over minderjarige of curatele | ❌ | juridische status | ja |
| Kiesrecht | attribuut | BRP | Europees kiesrecht en uitsluiting | ❌ | statusattribuut | ja |
| Overlijden | gebeurtenis | BRP | Overlijdensdatum, -plaats en -land | ❌ | eenmalige gebeurtenis | ja |

### BRK — Basisregistratie Kadaster

Kadaster is **bronhouder**. Gemeente is **afnemer** (gebruiksplicht) en **bronhouder publiekrechtelijke beperkingen** (WKPB).

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | object | BRK | Begrensd deel grondgebied met kadastrale aanduiding | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] | object | BRK | Aandeel in gesplitst gebouw met exclusief gebruiksrecht | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | object | BRK | Eigendom of beperkt recht op onroerende zaak | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling\|Tenaamstelling]] | object | BRK | Koppeling recht↔persoon | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/zekerheidsrecht\|Zekerheidsrecht]] | object | BRK | Hypotheek of beslag op onroerende zaak | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/publiekrechtelijke-beperking\|Publiekrechtelijke Beperking]] | object | BRK (WKPB) | Beperkingsbesluit van bestuursorgaan op onroerende zaak | ✅ | gemeente is bronhouder | nee (hiaat) |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stuk\|Stuk]] | object | BRK | Brondocument in openbare registers (akte, kadasterstuk) | ✅ | authentieke gegevens | nee (hiaat) |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stukdeel\|Stukdeel]] | object | BRK | Onderdeel van stuk met rechtsfeiten | ✅ | compositie van Stuk | nee (hiaat) |
| Kadastraal Object | object | BRK | Abstract: Perceel en Appartementsrecht | ❌ | abstract | ja |
| Onroerende Zaak | object | BRK | Abstract: Perceel, Appartementsrecht, Leidingnetwerk | ❌ | abstract | ja |
| Leidingnetwerk | object | BRK | Kadastraal object voor leidinginfrastructuur | ❌ | nutsbedrijf-scope | ja |
| Aantekening | object | BRK | Bijzonderheid bij kadastraal object of recht | ❌ | procesnotitie | ja |
| Kadastrale kaart | object | BRK | Landelijke kaart met perceelsgrenzen | ❌ | informatieproduct | nee |
| notaris | actor | BRK | Aanbieder van stukken aan openbare registers | ❌ | externe actor | nee |

### NHR — Nationaal Handelsregister

KvK is **bronhouder**. Gemeente is **afnemer** (gebruiksplicht).

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit\|Maatschappelijke Activiteit]] | object | NHR | Activiteit van persoon of organisatie, KVK-nummer | ✅ | exact match, kern NHR | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | object | NHR | Organisatie met rechtspersoonlijkheid | ✅ | exact match, complement van Ingeschreven Persoon | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | object | NHR | Locatie waar activiteiten worden uitgeoefend | ✅ | exact match, koppelpunt beleid↔locatie | ja |
| Onderneming | classificatie | NHR | Economische activiteit die aan wettelijke criteria voldoet | ❌ | kwalificatie van MA | nee |
| Rechtspersoon | object | NHR | Generalisatie NatuurlijkPersoon/NietNatuurlijkPersoon | ❌ | abstract | ja |
| Handelsnaam | attribuut | NHR | Naam waaronder onderneming of vestiging handelt | ❌ | groepattribuut | ja |
| SBI-code | classificatie | NHR | Standaard Bedrijfsindeling | ❌ | referentietabel | ja |
| UBO | attribuut | NHR | Uiteindelijk belanghebbende >25% | ❌ | compliance, niet gemeentelijk | nee |
| Functionaris | rol | NHR | Bestuurlijke of vertegenwoordigingsfunctie | ❌ | rol (relatie) | nee |
| Faillissement | status | NHR | Bijzondere rechtstoestand | ❌ | attribuut | nee |

### WOZ — Waardering Onroerende Zaken

Gemeente is **bronhouder**. Beheerder LV: Kadaster. Heffingsambtenaar stelt waarde vast.

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | object | WOZ | Onroerende zaak waarvan de WOZ-waarde wordt vastgesteld | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo\|WOZ-waarde]] | object | WOZ | Vastgestelde waarde per waardepeildatum | ✅ | eigen levenscyclus (jaarlijks) | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/woz-deelobject\|WOZ-deelobject]] | object | WOZ | Afzonderlijk element voor onderbouwing waarde | ✅ | compositie van WOZ-object | ja |
| [[Wiki/Rollen/belanghebbende\|Belanghebbende]] | rol | WOZ | Eigenaar of gebruiker van WOZ-object (WOZ-specifieke voorkeursvolgorde) | ❌ | rol — degene die beschikking ontvangt; vastgelegd als rol-pagina | nee |
| [[Wiki/Rollen/heffingsambtenaar\|Heffingsambtenaar]] | rol | WOZ | Gemeentelijk ambtenaar die WOZ-waarde vaststelt | ❌ | rol — namens college; vastgelegd als rol-pagina | nee |
| taxateur | actor | WOZ | Uitvoerder van waardebepaling (intern of extern) | ❌ | actor — dataleverancier-equivalent | nee |

### BRO — Basisregistratie Ondergrond

Gemeente is **bronhouder** (voor verkenningen, constructies en gebruiksrechten bij gemeentelijke taken). Dataleveranciers (ingenieursbureaus) leveren namens gemeente aan. Beheerder: PDOK/TNO. Registratiehouder: Minister BZK.

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bro/verkenning\|Verkenning]] | object | BRO | Waarneming opbouw ondergrond (art. 19 Wet BRO) | ✅ | wettelijk objecttype, gemeente is bronhouder | nee (hiaat) |
| [[Wiki/Bedrijfsobjecten/99-kern/bro/constructie\|Constructie]] | object | BRO | Werk in de ondergrond (art. 21 Wet BRO) | ✅ | wettelijk objecttype, gemeente is bronhouder | nee (hiaat) |
| [[Wiki/Bedrijfsobjecten/99-kern/bro/gebruiksrecht\|Gebruiksrecht]] | object | BRO | Besluit/melding winnen, opslaan, bodemkwaliteit (art. 20 Wet BRO) | ✅ | wettelijk objecttype, gemeente is bronhouder | nee (hiaat) |
| authentiek model | object | BRO | 2D/3D weergave ondergrond (4 typen) | ❌ | Minister is bronhouder, TNO is maker | nee |
| grondwatermonitoringput (GMW) | subtype | BRO | Fysieke constructie met buizen en filters | ❌ | specialisatie van Constructie | nee |
| grondwatermonitoringnet (GMN) | object | BRO | Logische groepering meetpunten | ❌ | geen wettelijk objecttype, wel BRO-registratieobject | nee |
| grondwaterstandonderzoek (GLD) | subtype | BRO | Meetreeksen waterstand per monitoringbuis | ❌ | specialisatie van Verkenning | nee |
| grondwatersamenstellingsonderzoek (GAR) | subtype | BRO | Monitoring grondwaterkwaliteit | ❌ | specialisatie van Verkenning | nee |
## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018|Catalogus BAG 2018]]
- [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1|Logisch Ontwerp BRP 2025.Q1]]
- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-en-informatiemodellen|RSGB 2.02 Deel I en VNG Informatiemodellen]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk|Catalogus BRK 2020]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-nhr|Gegevenscatalogus NHR 3.0.4]]
- [[Wiki/Bronsamenvattingen/Standaarden/wet-bro|Wet basisregistratie ondergrond]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bro-gld|BRO Catalogus Grondwaterstandonderzoek (GLD)]]

## Nog te verwerken

De volgende basisregistraties zijn nog niet verwerkt. Per registratie zijn geschikte bronnen gesuggereerd:

- **RSGBPlus overige entiteiten** — referentietabellen, detail-entiteiten, IMGeo/BGT
- **BGT** — Basisregistratie Grootschalige Topografie (https://docs.geostandaarden.nl/imgeo/catalogus/bgt/)

## Openstaande vragen

- **Standplaats-disambiguatie**: de GGM-entiteit "Standplaats" (RSGBPlus, EAID_B1C6CA45) was eerder foutief gematcht op [[Marktstandplaats]] (Economie). Nu gecorrigeerd: de GGM-entiteit hoort bij [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]]. De marktstandplaats is een GGM-hiaat.
- **BRO GGM-hiaat**: de BRO en haar objecttypen (Verkenning, Constructie, Gebruiksrecht) zijn niet in het GGM gemodelleerd.
