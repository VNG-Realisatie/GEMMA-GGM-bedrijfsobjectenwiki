---
type: bronsamenvatting
titel: "Gegevenscatalogus Handelsregister (NHR)"
onderwerp: [Basisregistraties, NHR]
datum_ingest: 2026-06-25
---

## Samenvatting

De Gegevenscatalogus Handelsregister (versie 3.0.4, september 2020) beschrijft de samenhang en structuur van informatie in de Basisregistratie Handelsregister (NHR). Het Handelsregister is een authentieke gegevensbron voor alle ondernemers, rechtspersonen en gemeenten in Nederland. Bronhouder en beheerder is de Kamer van Koophandel (KvK), opdrachtgever is het Ministerie van Economische Zaken en Klimaat.

Het wettelijk kader bestaat uit de **Handelsregisterwet 2007** (registratieplicht, definities, authentieke gegevens) en het **Handelsregisterbesluit 2008** (gegevens per objecttype). De catalogus vertaalt dit naar een informatiemodel met drie hoofdobjecttypen:

1. **Persoon** — NatuurlijkPersoon (koppeling BRP) of NietNatuurlijkPersoon (organisaties)
2. **[[Maatschappelijke Activiteit]]** — verband tussen personen en activiteiten, geïdentificeerd met KVK-nummer; manifesteert zich eventueel als onderneming
3. **[[Vestiging]]** — fysieke locatie waar activiteiten worden uitgeoefend; commercieel (bij onderneming) of niet-commercieel (bij rechtspersoon)

Een Persoon heeft nul of één maatschappelijke activiteit. Een maatschappelijke activiteit kan zich manifesteren als onderneming. Een onderneming bestaat uit één of meer vestigingen (commercieel). Een [[Niet-Natuurlijk Persoon]] kan ook activiteiten uitoefenen in niet-commerciële vestigingen. Alle in artikelen 9-14 Handelsregisterwet genoemde gegevens zijn **authentieke gegevens** met wettelijk gezag.

## Kernbegrippen

- **[[Maatschappelijke Activiteit]]** — een verband tussen personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (onderneming) dan wel een activiteit van een niet-natuurlijk persoon die registratieplichtig is. Geïdentificeerd met KVK-nummer, RSIN, statutaire naam, rechtsvorm. Authentiek gegeven.
- **[[Niet-Natuurlijk Persoon]]** — een ingeschreven niet-natuurlijk persoon of een ander buitenlands niet-natuurlijk persoon. Omvat BV, NV, stichting, vereniging, coöperatie, publiekrechtelijke rechtspersoon. Geïdentificeerd met NNPID, KVK-nummer, RSIN. Complement van [[Ingeschreven Persoon]] (BRP).
- **[[Vestiging]]** — een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt. Geïdentificeerd met vestigingsnummer, gekoppeld aan BAG-adres (Nummeraanduiding). Authentiek gegeven.
- **Onderneming** — een door een natuurlijk persoon, een rechtspersoon of een samenwerkingsverband uitgeoefende economische activiteit (art. 1 Handelsregisterwet). In het informatiemodel geen apart objecttype maar een kwalificatie van Maatschappelijke Activiteit (indicatieEconomischActief).
- **Rechtspersoon** — abstract type, generalisatie van NatuurlijkPersoon en NietNatuurlijkPersoon. Juridische entiteit met rechtsbevoegdheid. Heeft KVK-nummer, rechtsvorm, identificatie.
- **Handelsnaam** — naam waaronder een onderneming of vestiging handelt. Gegevensgroep (meervoudig), geen zelfstandig object.
- **SBI-code** — Standaard Bedrijfsindeling: classificatie van bedrijfsactiviteiten per vestiging. Referentietabel.
- **UBO** (uiteindelijk belanghebbende) — persoon met economisch belang >25% in vennootschap. Registratieplichtig sinds 2020 (art. 15a Handelsregisterwet). Compliance-gegeven, niet gemeentelijk geregistreerd.

## Relevantie voor bedrijfsarchitectuur

Het NHR is voor de gemeente een kernregistratie die dwars door alle domeinen snijdt:

- **Belastingen**: OZB-aanslagen worden gekoppeld aan eigenaren via Tenaamstelling (BRK) en Rechtspersoon (NHR). Reclamebelasting, BIZ-bijdrage en precariobelasting verwijzen naar NHR-vestigingen.
- **Vergunningen**: horecavergunningen, evenementenvergunningen en omgevingsvergunningen worden verleend aan rechtspersonen en/of vestigingen.
- **Economie**: werklocatiebeleid, detailhandelsbeleid en horecabeleid gebruiken vestigingsgegevens en SBI-codes. [[Horecabedrijf]] en [[Hotel]] zijn specialisaties van Vestiging.
- **VTH**: toezicht en handhaving richten zich op vestigingen en hun activiteiten.
- **Schuldhulpverlening**: [[Schuldeiser]] is een specialisatie van Rechtspersoon.
- **Dienstverlening**: [[Aanvraag of Melding]] koppelt aan Rechtspersoon als melder/aanvrager.

De NHR-entiteiten vormen samen met de BRP (personen), BAG (adressen) en BRK (onroerend goed) het fundament van de gemeentelijke informatiehuishouding.

## Citaten

> "Een verband tussen één of meer personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (i.g.v. een onderneming) dan wel een in een organisatorisch verband, dat toebehoort aan een niet-natuurlijk persoon welke registratieplichtig is, uitgeoefende activiteit" (Gegevenscatalogus HR, definitie MaatschappelijkeActiviteit)

> "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt." (Handelsregisterwet 2007, art. 1)

> "Ofschoon de definitie in het NHR doet vermoeden dat het hier om een ruimtelijk object gaat, beschouwen we een VESTIGING in het RSGB als een specialisatie van SUBJECT." (GGM-toelichting bij Vestiging)

## Bronnen
- [[Sources/Standaarden/catalogus-nhr]]
