---
type: bronsamenvatting
titel: Wet SUWI en Gegevensregister SUWI (SGR 19.0)
onderwerp: [werk en inkomen]
datum_ingest: 2026-06-27
---

## Samenvatting

De **Wet structuur uitvoeringsorganisatie werk en inkomen** (Wet SUWI, 2001) richt UWV en SVB op als zelfstandige bestuursorganen en regelt hun samenwerking met gemeenten bij de uitvoering van sociale zekerheidswetten. De wet verplicht UWV, SVB en gemeenten tot gezamenlijke dienstverlening, gegevensuitwisseling via de Gezamenlijke Elektronische Voorzieningen SUWI (GeVS/Suwinet), en cliëntenparticipatie. De Nederlandse Arbeidsinspectie houdt toezicht.

Het **Gegevensregister SUWI (SGR) 19.0** (BKWI, bijlage XII bij de Regeling SUWI) is de uitwerking: een conceptueel gegevensmodel met ~260 klassen en ~930 attributen dat definieert welke gegevens de SUWI-partijen uitwisselen. Het SGR is opgedeeld in deelmodellen:

- **Stamgegevens** — Client SUWI, identificatie, adres, leefsituatie, partner, kind
- **Arbeidsmarktkwalificaties** — opleiding, werkervaring, taalbeheersing, rijbewijs
- **Arbeidsgegevens** — arbeidsverhouding, loonperiode, werkgever, sector
- **Uitkeringsgegevens** — uitkeringsverhouding, aanvraag uitkering, maatregel, vordering, bezwaar en beroep
- **Arbeidstoeleidingsgegevens** — trajectplan, [[Re-integratievoorziening]] (GSD en UWV), bemiddeling, beschikbaarheid, vacatureverwijzing
- **VUM** (Verbeteren Uitwisseling Matchingsgegevens) — werkzoekendeprofiel en vacatureprofiel voor matching over regio- en organisatiegrenzen heen
- **Dennis & Eva** — instrumentengidsen voor werkgeversdienstverlening (Dennis) en toeleiding werkzoekenden (Eva); gemeenten vullen deze met lokale en regionale instrumenten
- **Ontsluiting externe bronnen** — gegevens uit BRP (persoons- en adresgegevens t.b.v. UWV/GSD/SVB/Nederlandse Arbeidsinspectie), Kadaster (vermogenstoets: eigendom cliënt in de vorm van een onroerende zaak, kadastrale aanduiding, zakelijk recht, aantekening kadastraal object), RDW (vermogenstoets: kenteken, kenmerken, eigenaarschap en verzekeringsgegevens van een voertuig), DUO (opleidingsgegevens deelname/resultaat — Studiefinanciering wordt alleen als afzonderlijk dossiernaam genoemd, zonder uitgewerkt deelmodel), Belastingdienst, Handelsregister. RDW/Kadaster expliciet t.b.v. **vermogenstoets Participatiewet** en fraudeonderzoek sociale recherche (§4.10-4.11 SGR).

Het berichtenregister toont per bericht welke partij levert en welke afneemt. De gemeente (GSD) is zowel leverancier (bijstandsregelingen, GSD dossier reintegratie) als afnemer (UWV-dossiers, externe bronnen).

## Kernbegrippen

- **[[Werkzoekende]]** — centraal object in het SUWI-datamodel; generiek werkprofiel met 25+ componenten (arbeidsmarktkwalificaties, bemiddeling, mobiliteit, taalbeheersing, beschikbaarheid). GGM exact match (abstract Objecttype, Werk).
- **Trajectplan** — overkoepelend plan dat re-integratieactiviteiten per werkzoekende organiseert. SGR modelleert dit als aparte klasse met eigen attributen (datum aanvang/einde, financiële afhandeling, contactcoach). Niet in GGM — GGM-hiaat.
- **Instrument (arbeidstoeleiding)** — catalogus-item in Dennis & Eva: een beschikbare dienst of tool voor toeleiding naar werk. Gemeenten registreren lokale en regionale instrumenten met aanbieder en uitvoeringslocatie. Niet in GGM — GGM-hiaat. Onderscheid met [[Re-integratievoorziening]]: instrument = wat beschikbaar is (catalogus), re-integratievoorziening = wat is ingezet voor een specifieke persoon (toekenning).
- **[[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt|Vacature (arbeidsmarkt)]]** — openstaande arbeidsplaats bij werkgever in de regio, gedeeld via VUM voor matching met werkzoekenden. GGM-hiaat in Werk-domein; homoniem van [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/vacature|Vacature]] (HR, gemeente als werkgever).
- **Client SUWI** — persoon met BSN die diensten ontvangt van UWV, SVB of gemeente. Superklasse van [[Werkzoekende]]. GGM: [[Client]] (al BO).
- **Suwinet/GeVS** — de gezamenlijke elektronische voorzieningen voor gegevensuitwisseling. Infrastructuur, geen data-object.
- **VUM** — programma voor transparantie in werkzoekenden- en vacaturebestand over organisatiegrenzen. Procesverbetering, geen data-object.
- **SuwiML** — XML-standaard voor elektronische gegevensuitwisseling in SUWI-domein. Technische standaard, geen data-object.
- **Vermogenstoets (RDW/Kadaster-deelmodellen)** — herbeoordeeld 2026-07-07: het SGR ontsluit expliciet voertuig- (RDW) en onroerendezaak-gegevens (Kadaster) t.b.v. de vermogenstoets Participatiewet. Dit bevestigt de zakelijke functie achter GGM's `Motorvoertuig` en `Onroerend goed` (subtypen van Vermogenscomponent, zie [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]/Vermogenscomponent-dekking in [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]]), maar levert geen aanvullende attributen op: de onderliggende Figuren 15-16 zijn OCR-garbled en niet bruikbaar als brontekst.
- **Onderhoudsplichtige** — géén zelfstandig begrip: SGR §7 lijst dit als rolnaam (Rolinstantie PERSOON, SuwiML-tag) in een adres/persoon-relatie, naast Garant/Rekeninghouder/Schuldenaar/Begunstigde. Geen eigen attributen of levenscyclus. Blijft een GGM/BO-hiaat zonder brongrondslag (GGM's `Onderhoudsplicht`/`Onderhoudsverhouding` in Sociaal Domein Generiek).
- **Studiefinanciering** — komt alleen voor als naam van een dossier ("DUO Dossier Studiefinanciering") in het berichtenoverzicht (§3); geen uitgewerkt deelmodel of attributen in dit document. Blijft een hiaat zonder brongrondslag.

## Relevantie voor bedrijfsarchitectuur

De Wet SUWI en het SGR leggen de **wettelijke en technische basis** voor de gegevensuitwisseling in de keten Werk en Inkomen. Voor de wiki levert dit:

1. **Vier nieuwe BO's:** [[Werkzoekende]] (GGM exact, specialisatie van [[Client]]), Trajectplan (GGM-hiaat, coördinatie-object boven [[Re-integratievoorziening]]), Instrument (GGM-hiaat, catalogusniveau), [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt|Vacature (arbeidsmarkt)]] (GGM-hiaat, homoniem HR-Vacature)
2. **Bevestiging bestaande BO's:** [[Re-integratievoorziening]], [[Loonkostensubsidie]], [[Inkomensvoorziening]] en [[Draagkracht]] worden bevestigd als kernobjecten in het SUWI-gegevensmodel
3. **Homoniem opgelost:** Vacature (HR) ↔ Vacature (arbeidsmarkt) — gemeente als werkgever vs. gemeente als arbeidsmarktbemiddelaar
4. **GGM-hiaat signalering:** Trajectplan, Instrument en Vacature (arbeidsmarkt) ontbreken in GGM Werk-domein
5. **Her-mining 2026-07-07:** vermogenstoets-deelmodellen (RDW/Kadaster) bevestigen de zakelijke context van Motorvoertuig/Onroerend goed maar leveren geen nieuwe attributen (diagrammen OCR-garbled); Onderhoudsplichtige en Studiefinanciering blijken bij nadere lezing dunner dan gedacht (resp. kale rolnaam, kale dossiernaam) — beide blijven een hiaat, een nieuwe bron is nodig, hermining van dit document lost het niet verder op

## Bronnen

- [[Sources/Onderwerpen/Werk en Inkomen/wet-suwi-bwbr0013060]]
- [[Sources/Onderwerpen/Werk en Inkomen/sgr-19-gegevensregister-suwi]]
