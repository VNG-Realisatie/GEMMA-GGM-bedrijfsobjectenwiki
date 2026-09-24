---
type: onderwerp
naam: Basisregistraties
status: afgerond
verwerkingsdatum: 2026-09-23
bronnen_count: 9
begrippen_count: 106
bo_count: 48
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
| Ingezetene | specialisatie | BRP | Ingeschreven bij een gemeente, volledige PL | ❌ | specialisatie van Ingeschreven Persoon | ja |
| Niet-ingezetene | specialisatie | BRP | Ingeschreven in de RNI, beperkte PL | ❌ | specialisatie van Ingeschreven Persoon | nee |
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
| grondwatermonitoringput (GMW) | specialisatie | BRO | Fysieke constructie met buizen en filters | ❌ | specialisatie van Constructie | nee |
| grondwatermonitoringnet (GMN) | object | BRO | Logische groepering meetpunten | ❌ | geen wettelijk objecttype, wel BRO-registratieobject | nee |
| grondwaterstandonderzoek (GLD) | specialisatie | BRO | Meetreeksen waterstand per monitoringbuis | ❌ | specialisatie van Verkenning | nee |
| grondwatersamenstellingsonderzoek (GAR) | specialisatie | BRO | Monitoring grondwaterkwaliteit | ❌ | specialisatie van Verkenning | nee |

### BGT — Basisregistratie Grootschalige Topografie

Bronhouder-organisatie (meestal gemeente) is **bronhouder**. Beheerder LV: Kadaster. Modelleert dezelfde fysieke werkelijkheid als de IMBOR-beheerobjecten in Beheer Openbare Ruimte, maar op registratie- in plaats van beheerniveau — zie [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2|Gegevenscatalogus BGT 1.2]] §Relevantie voor bedrijfsarchitectuur.

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/wegdeel\|Wegdeel]] | object | BGT | Kleinste homogene stuk weg, primair voor weg-/spoor-/vliegverkeer | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/ondersteunend-wegdeel\|OndersteunendWegdeel]] | object | BGT | Deel van de weg niet primair voor verkeer (berm, trottoirband) | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/spoorbaan\|Spoorbaan]] | object | BGT | De as van het spoor waarover trein/tram/sneltram rijdt | ✅ | exact match; homoniem met Archeologie "Spoor" (#102) | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/onbegroeid-terreindeel\|OnbegroeidTerreindeel]] | object | BGT | Kleinste stukje terrein zonder aaneengesloten vegetatie | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/begroeid-terreindeel\|BegroeidTerreindeel]] | object | BGT | Kleinste stukje terrein met aaneengesloten vegetatie | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/waterdeel\|Waterdeel]] | object | BGT | Kleinste stukje permanent water | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/ondersteunend-waterdeel\|OndersteunendWaterdeel]] | object | BGT | Periodiek (deels) met water bedekt object t.b.v. waterhuishouding | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/pand\|Pand]] | object | BGT/BAG | Kleinste bouwkundig zelfstandige eenheid | ✅ | al vastgelegd via BAG, RSGBPlus/BGT is duplicaat | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/overig-bouwwerk\|OverigBouwwerk]] | object | BGT | Duurzaam bouwwerk, geen pand of kunstwerk | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/overbruggingsdeel\|Overbruggingsdeel]] | object | BGT | Essentieel onderdeel van een brugconstructie | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/tunneldeel\|Tunneldeel]] | object | BGT | Essentieel onderdeel van een tunnelconstructie | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/bgt/kunstwerkdeel\|Kunstwerkdeel]] | object | BGT | Onderdeel civieltechnisch werk (weg/water/spoor/kering/leiding) | ✅ | exact match | ja |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/scheiding\|Scheiding]] | object | BGT/Beheer OR | Kunstmatig, lineair obstakel met werende functie | ✅ | duplicaat (#100), primair in Beheer Openbare Ruimte | ja |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/functioneel-gebied\|FunctioneelGebied]] | object | BGT/Beheer OR | Begrensd en benoemd gebied van een functionele eenheid | ✅ | duplicaat (#101), primair in Beheer Openbare Ruimte | ja |
| IMGeo-Object | object | BGT | Abstract: gemeenschappelijke eigenschappen van elk BGT-object | ❌ | abstract | ja |
| OverigeConstructie | object | BGT | Abstract: gebouwd object, geen NEN 3610-gebouw | ❌ | abstract, specialisaties (met eigen pagina) zijn de BO's | ja |
| OpenbareRuimteLabel | object | BGT | Naam/plaatsingspunt van een Openbare Ruimte, t.b.v. visualisatie | ❌ | cartografisch label van bestaande BO [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] | ja |
| Plaatsbepalingspunt | object | BGT | Ingemeten punt, onderdeel begrenzing BGT-objecten | ❌ | meettechnisch kwaliteitsobject, geen bedrijfsbetekenis | ja |

### RSGBPlus — generalisaties en detailentiteiten (RSGB Deel II)

RSGB Deel II (Specificaties) is de bron voor de generalisaties en detailentiteiten die het RSGB toevoegt bovenop de basisregistraties zelf (zie [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]). Batch 1: generalisaties met exacte GGM-match. Batch 2: overige detailentiteiten/referentietabellen. Ingezetene, Niet-ingezetene, Nationaliteit en Verblijfstitel zijn al in de BRP-sectie hierboven beoordeeld (zelfde GGM-entiteiten, andere herkomstregistratie) en hier niet herhaald.

| Begrip | Type | Registratie | Omschrijving | BO? | Reden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon\|Rechtspersoon]] | object | RSGBPlus | Natuurlijke of niet-natuurlijke persoon met wie de gemeente contact onderhoudt | ✅ | exact match, generalisatiewortel voor ~20 domeinrollen (Eigenaar, Huurder, Schuldeiser, Debiteur, e.a.); herzien t.o.v. eerdere NHR-beoordeling ("te abstract") | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]] | object | RSGBPlus | Persoonskant-specialisatie van Rechtspersoon; Ingeschreven Persoon dekt de BRP-ingeschrevenen | ✅ | exact match; sluit asymmetrie met bestaande Niet-Natuurlijk Persoon | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishouden\|Huishouden]] | object | RSGBPlus | Duurzame samenlevingsvorm binnen één verblijfsobject/stand-/ligplaats | ✅ | exact match, bewust los van BRP-verblijfsrelaties gemodelleerd | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishoudenlid\|Huishoudenlid]] | object | RSGBPlus | Positie van een ingeschreven persoon binnen een huishouden (hoofd/partner/kind/overig lid) | ✅ | ggm-afgeleid (associatie Huishouden→IngeschrevenPersoon + RSGB-attribuutspecificatie); RSGB-naam "Huishoudenrelatie" vervangen door herkenbaarder begrip | nee |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/ouderschap\|Ouderschap]] | object | BRP/RSGBPlus | Juridisch verband tussen kind en ouder | ✅ | ggm-afgeleid (attributen ouder1/ouder2/gezinsrelatie op IngeschrevenPersoon); RSGB-naam "Ouder-kind-relatie" vervangen door de in het Logisch Ontwerp BRP gebruikte term | nee |
| [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-gebouwd-object\|Overig Gebouwd Object]] | object | RSGBPlus | Niet-authentiek gebouwd object zonder verblijfsfunctie (tankstation, parkeergarage, zendmast) | ✅ | exact match, parallel aan Verblijfsobject | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-terrein\|Overig Terrein]] | object | RSGBPlus | Niet-authentiek terrein (autosloperij, volkstuincomplex, sportveld zonder opstal) | ✅ | exact match, parallel aan Standplaats/Ligplaats | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/woz-belang\|WOZ-belang]] | object | Vastgoed | Aanwijzing van rechtspersoon als belanghebbende eigenaar/gebruiker van een WOZ-object | ✅ | exact match, koppelt WOZ-object aan Rechtspersoon | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/gemeentelijke-openbare-ruimte\|Gemeentelijke Openbare Ruimte]] | object | RSGBPlus | Geo-object voor het gemeentelijk aangewezen openbaar gebied, kan meerdere woonplaatsen overspannen | ✅ | ggm-afgeleid (aggregatie van BAG-Openbare Ruimte); geen eigen GGM-entiteit, als mogelijk hiaat teruggemeld | nee |
| Benoemd Object | object | RSGBPlus | Abstract: Gebouwd Object of Benoemd Terrein ("alle objecten met een adres") | ❌ | abstract, zwak op eigen bestaan/herkenbaarheid — geen exemplaar bestaat los van een specialisatie | ja |
| Gebouwd Object | object | RSGBPlus | Abstract: Verblijfsobject of Overig Gebouwd Object | ❌ | abstract, specialisatie van Benoemd Object | ja |
| Benoemd Terrein | object | RSGBPlus | Abstract: Standplaats, Ligplaats of Overig Terrein | ❌ | abstract, specialisatie van Benoemd Object | ja |
| Adresseerbaar Object | object | BAG | Abstract: Verblijfsobject, Standplaats of Ligplaats | ❌ | pure BAG-referentie, geen eigen attributen/relaties (bron zelf: "enkel opgenomen als referentie") | ja |
| Subject | object | RSGBPlus | Abstract: Rechtspersoon of Vestiging | ❌ | geen eigen GGM-entiteit; komt niet als aparte entiteit in het GGM voor | nee |
| Aard recht verkort | attribuut | BRK | EDI-code en verkorte omschrijving van de aard van een zakelijk recht | ❌ | referentietabel (bron zelf: "modelleren we met dit objecttype" een BRK-attribuuttabel) | ja |
| Aard verkregen recht | attribuut | BRK | Aanduiding en omschrijving van de aard van een verkregen zakelijk recht | ❌ | referentietabel, zelfde patroon als Aard recht verkort | ja |
| Academische titel | attribuut | RSGBPlus | Opsomming van academische titels | ❌ | referentietabel (code/naam/geldigheid) | ja |
| Adresseerbaar object aanduiding | object | RSGBPlus | Generalisatie van Verblijfsobject/Standplaats/Ligplaats/Overig Gebouwd Object als adresdrager | ❌ | abstract, zelfde patroon als Benoemd Object (batch 1); specialisaties zijn al eigen BO's | ja |
| Ander Natuurlijk Persoon | specialisatie | RSGBPlus | Natuurlijk persoon van belang voor de gemeente, niet ingeschreven in de BRP | ❌ | specialisatie van [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]], geen eigen GGM-entiteit | nee |
| Ander Niet-Natuurlijk Persoon | specialisatie | RSGBPlus | Organisatie van belang voor de gemeente, niet ingeschreven in het NHR | ❌ | specialisatie van [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]], geen eigen GGM-entiteit | nee |
| Functionaris | object | NHR | Verband tussen een niet-natuurlijk persoon en de rechtspersonen die namens haar optreden | ❌ | bron zelf: "relatie-objecttype... kan niet zelfstandig bestaan" | nee |
| Ingeschreven Niet-Natuurlijk Persoon | specialisatie | NHR | NHR-ingeschreven niet-natuurlijk persoon | ❌ | dekt al door bestaande [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] (die exact deze definitie draagt), geen eigen GGM-entiteit | nee |
| Inrichtingselement | object | RSGBPlus (IMGeo) | Generieke catch-all voor overige geo-objecten die de omgeving inrichten (straatmeubilair e.d.) | ❌ | subklassen niet als aparte objecttypen gemodelleerd (bron zelf), geen relaties | ja |
| Kadastrale gemeente | object | BRK | Gedeelte van het grondgebied volgens het Kadaster | ❌ | referentietabel (bron zelf: "zgn. tabel-objecttype") | ja |
| Kadastrale onroerende zaak | object | BRK | Abstract: Kadastraal Perceel of Appartementsrecht | ❌ | abstract, al gedekt door specialisaties (net als Benoemd Object-familie) | ja |
| Kadastrale onroerende zaak aantekening | object | BRK | Aantekening bij een kadastraal object | ❌ | al gedekt door de bestaande generieke rij "Aantekening" (BRK-sectie) | ja |
| Kadastrale onroerende zaak historie relatie | object | BRK | Afstammingsverwantschap tussen oude en nieuwe kadastrale objecten | ❌ | technische mutatiehistorie, geen bedrijfsbegrip | ja |
| Land | attribuut | RSGBPlus | Landcode/-naam | ❌ | referentietabel; blijft bestaande entiteitendekking-hiaat (zie `Wiki/log.md` 2026-07-07) | ja |
| Overige adresseerbaar object aanduiding | object | RSGBPlus | Officieel adres van een Overig Gebouwd Object of Overig Terrein | ❌ | bron zelf: "heeft dientengevolge geen specifieke gegevens" — puur koppelobject | ja |
| Reisdocumentsoort | attribuut | BRP | Opsomming van modellen Nederlandse reisdocumenten | ❌ | referentietabel (bron zelf: "zgn. tabel-objecttype") | ja |
| Zakelijk recht aantekening | object | BRK | Aantekening bij een zakelijk recht | ❌ | al gedekt door de bestaande generieke rij "Aantekening" (BRK-sectie) | ja |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018|Catalogus BAG 2018]]
- [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1|Logisch Ontwerp BRP 2025.Q1]]
- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-en-informatiemodellen|RSGB 2.02 Deel I en VNG Informatiemodellen]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk|Catalogus BRK 2020]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-nhr|Gegevenscatalogus NHR 3.0.4]]
- [[Wiki/Bronsamenvattingen/Standaarden/wet-bro|Wet basisregistratie ondergrond]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bro-gld|BRO Catalogus Grondwaterstandonderzoek (GLD)]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2|Gegevenscatalogus BGT 1.2 (IMGeo)]]
- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties|RSGB 2.02 Deel II: Specificaties]]

## Nog te verwerken

Geen. RSGB 2.02 Deel II is volledig verwerkt in twee batches (2026-09-23): batch 1 (generalisaties: Rechtspersoon) en batch 2 (overige detailentiteiten: Natuurlijk Persoon, Huishouden, Huishoudenlid, Ouderschap, Overig Gebouwd Object, Overig Terrein, WOZ-belang, Gemeentelijke Openbare Ruimte). Zie §RSGBPlus hierboven voor de volledige begrippentabel, inclusief de ~19 begrippen die bewust geen BO zijn geworden (referentietabellen, koppelobjecten, abstracte generalisaties).

## Openstaande vragen

Geen. Eerdere vragen zijn opgelost:
- **Standplaats-disambiguatie**: de GGM-entiteit "Standplaats" (RSGBPlus, EAID_B1C6CA45) was eerder foutief gematcht op [[Marktstandplaats]] (Economie). Gecorrigeerd: de GGM-entiteit hoort bij [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]]. De marktstandplaats is een GGM-hiaat.
- **BRO GGM-hiaat**: de BRO en haar objecttypen (Verkenning, Constructie, Gebruiksrecht) zijn niet in het GGM gemodelleerd — gedocumenteerd, geen verdere actie nodig.
- **Rechtspersoon "te abstract"**: bij de NHR-ingest afgewezen als BO; bij de RSGB Deel II-ingest herzien (zie [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]]) — de relatie-rijkdom (~20 domeinrollen generaliseren ernaar in het GGM) en herkenbaarheid wogen zwaarder dan het abstracte karakter.

## Conclusie

Domein afgerond: alle 8 GGM-gemodelleerde basisregistraties zijn volledig verwerkt (BAG, BRP, BRK, NHR, WOZ, BRO, BGT, RSGBPlus), 48 BO's vastgelegd. RSGB 2.02 Deel II leverde in twee batches 9 nieuwe BO's op (Rechtspersoon, Natuurlijk Persoon, Huishouden, Huishoudenlid, Ouderschap, Overig Gebouwd Object, Overig Terrein, WOZ-belang, Gemeentelijke Openbare Ruimte) en herzag één eerdere afwijzing (Rechtspersoon). Twee kleine hiaten teruggemeld: Gemeentelijke Openbare Ruimte (geen GGM-entiteit) en het Huishouden-duplicaat (RSGBPlus/Sociaal Domein Generiek) — zie [[Wiki/Analyses/ggm-terugmeldingen]].
