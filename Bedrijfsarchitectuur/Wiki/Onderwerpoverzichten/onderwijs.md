---
type: domein
naam: Onderwijs
status: in-behandeling
verwerkingsdatum: 2026-06-22
bronnen_count: 10
begrippen_count: 31
bo_count: 11
---

# Domein: Onderwijs

Gemeenten zijn verantwoordelijk voor de huisvesting van scholen (primair, voortgezet en speciaal onderwijs), het handhaven van de leerplicht, het organiseren van leerlingenvervoer en het coördineren van onderwijs en zorg. De gemeente bekostigt schoolbouw en -renovatie, programmeert huisvestingsprojecten via het integraal huisvestingsplan (IHP) en houdt toezicht op de naleving van de leerplichtwet.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/school\|School]] | object | Instelling voor funderend onderwijs waarvoor de gemeente verantwoordelijk is voor de huisvesting | ✅ | ja | 6/6 criteria, exact match | Basisschool De Brug, CSG Vonk | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | object | Kind of jongere dat onderwijs volgt aan een school in de gemeente | ✅ | ja | 6/6 criteria, exact match | PO-leerling, VO-leerling | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/opleidingsinschrijving\|Opleidingsinschrijving]] | object | Deelname van iemand aan een opleiding bij een onderwijsinstelling | ✅ | ja | 6/6 criteria, exact match | Opleidingsinschrijving groep 1, overstap VO | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/uitschrijving\|Uitschrijving]] | object | Beëindiging van een inschrijving van een leerling bij een school | ✅ | ja | 6/6 criteria, exact match | Schoolverlater, verhuizing | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/ouder-of-verzorger\|Ouder Of Verzorger]] | actor | Persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind | ✅ | ja | 6/6 criteria, exact match | Ouder, voogd, pleegouder | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/verzuimmelding\|Verzuimmelding]] | object | Melding van een school aan de gemeente dat een leerling niet op school verschijnt | ✅ | ja | 6/6 criteria, exact match | Ongeoorloofd verzuim, luxeverzuim | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/leerplichtvrijstelling\|Leerplichtvrijstelling]] | object | Besluit waarbij een leerling geheel of gedeeltelijk wordt ontheven van de leerplicht | ✅ | ja | 6/6 criteria, exact match | Leerplichtvrijstelling art. 5a, 5b Lpw | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/procesverbaal-onderwijs\|Procesverbaal Onderwijs]] | object | Officieel document dat een overtreding van de leerplichtwet vastlegt | ✅ | ja | 6/6 criteria, exact match | PV bij absoluut verzuim | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/aanvraag-leerlingenvervoer\|Aanvraag Leerlingenvervoer]] | object | Verzoek van ouders aan de gemeente om een vervoersvoorziening voor hun kind | ✅ | ja | 6/6 criteria, exact match | Aanvraag taxivervoer SO | ja |
| [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/beschikking-leerlingenvervoer\|Beschikking Leerlingenvervoer]] | object | Gemeentelijk besluit over het toekennen of afwijzen van leerlingenvervoer | ✅ | ja | 6/6 criteria, exact match | Toekenning taxivervoer | ja |
| onderwijssoort | object | Typering van onderwijs (PO, VO, SO, SBO, VSO) | ❌ | ja | Classificatie; attribuut van School | PO, VO, SO | ja |
| onderwijsniveau | object | Hoogte van een soort onderwijs in relatie tot andere soorten | ❌ | nee | Classificatie; geen eigen attributen | — | ja |
| leerjaar | object | Codering van het jaar of niveau waarin de leerling onderwijs volgt | ❌ | ja | Classificatie; attribuut van Leerling | Groep 3, klas 2 | ja |
| loopbaanstap | object | Stap naar een volgende functie of klas | ❌ | ja | Te granulair; onderdeel van onderwijsloopbaan | — | ja |
| onderwijsloopbaan | object | Loopbaan als leerling in het onderwijs | ❌ | nee | Aggregatie zonder eigen attributen; gemeente beheert niet direct | — | ja |
| startkwalificatie | object | Diploma als minimale kwalificatie voor de arbeidsmarkt | ❌ | ja | Eigenschap van Leerling; relatie [0..1] | Havodiploma, mbo-2 | ja |
| locatie | object | Ruimtelijke afbakening van een schoolgebouw | ❌ | ja | Generiek kern-concept (Vastgoedobject); cross-domein | Schooladres | ja |
| verlofaanvraag | object | Verzoek om toestemming voor verlof (vakantie, studie) | ❌ | ja | Subtype AanvraagOfMelding; te granulair | Vakantieverlof | ja |
| aanvraagvrijstelling | object | Verzoek om vrijstelling van leerplicht | ❌ | ja | Subtype AanvraagOfMelding; te granulair | — | ja |
| klacht leerlingenvervoer | object | Uiting van ontevredenheid over leerlingenvervoer | ❌ | ja | Te granulair; subtype klacht | — | ja |
| ziekmelding leerlingenvervoer | object | Ziekmelding van leerling met recht op vervoer | ❌ | ja | Te granulair; operationeel detail | — | ja |
| doorgeleiding OM | object | Overdracht van leerplichtzaak aan Openbaar Ministerie | ❌ | ja | Te specifiek; justitie-subtype | — | ja |
| HALT-verwijzing | object | Verwijzing van jongere naar Halt-bureau | ❌ | ja | Te specifiek; justitie-subtype | — | ja |
| leerplichtambtenaar | actor | Ambtenaar die toezicht houdt op de leerplichtwet | ❌ | ja | Medewerkerrol, geen zelfstandig BO | — | ja |
| vervoerder | actor | Partij die leerlingenvervoer uitvoert | ❌ | ja | Leveranciersrol; subtype Leverancier | Taxibedrijf | ja |
| samenwerkingsverband | actor | Regionaal verband van scholen voor passend onderwijs | ❌ | nee | Ketenpartner; niet gemeentelijk beheerd | SWV Utrecht PO | nee |
| kindcentrum | object | Integrale voorziening onderwijs + kinderopvang 0-12 jaar | ❌ | nee | Subtype van School; vastgelegd als specialisatie | Utrechts Kindcentrum | nee |
| multifunctionele accommodatie (MFA) | object | Gebouw waar meerdere maatschappelijke organisaties voorzieningen aanbieden | ❌ | nee | Subtype van School; in gemeentelijk eigendom, 4 stuks in UVP | School + welzijn + sport | nee |
| kinderopvangvoorziening | object | Locatie waar kinderopvang wordt geboden, geregistreerd in LRK | ✅ | ja | 6/6 criteria, GGM-hiaat | KDV, BSO, gastouderopvang | nee |
| gymzaal | object | Sportvoorziening voor bewegingsonderwijs | ❌ | nee | Cross-domein: gedekt als [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/binnenlocatie\|Binnenlocatie]] (taakveld 5) | Schoolgymzaal, sportzaal | ja |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/beleidsnota-onderwijshuisvesting-utrecht|Beleidsnota Onderwijshuisvesting Utrecht 2026-2041]]
- [[Wiki/Bronsamenvattingen/onderwijs/uitvoeringsprogramma-ohv-utrecht|Uitvoeringsprogramma Onderwijshuisvesting Utrecht]]
- [[Wiki/Bronsamenvattingen/onderwijs/adviezen-duurzaamheid-ohv|Adviezen Duurzaamheid en Flexibele Huisvesting]]
- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer|Leerlingenvervoer]]
- [[Wiki/Bronsamenvattingen/onderwijs/passend-onderwijs|Passend onderwijs]]
- [[Wiki/Bronsamenvattingen/onderwijs/kindcentra|Kindcentra]]
- [[Wiki/Bronsamenvattingen/onderwijs/kinderopvang-toezicht|Kinderopvang — toezicht en handhaving]]
- [[Wiki/Bronsamenvattingen/onderwijs/onderwijsachterstand-vve|Onderwijsachterstand en VVE]]

## Nog te verwerken bronnen

- [utrecht-adviezen-duurzaamheid-ohv.md](Sources/Onderwerpen/Onderwijs/utrecht-adviezen-duurzaamheid-ohv.md) — verwerkt als context, geen nieuwe BO's

## Openstaande vragen of hiaten

Geen openstaande vragen. Alle drie eerder openstaande punten zijn opgelost:
- **Kinderopvangvoorziening** → opgenomen als BO (GGM-hiaat #51, procesobject)
- **Gymzaal** → cross-domein referentie naar [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/binnenlocatie|Binnenlocatie]] (taakveld 5), relatie vanuit School gelegd
- **MFA** → subtype van School

## Terugmeldingen richting GGM

- #51: Kinderopvangvoorziening ontbreekt in GGM (hiaat). Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
