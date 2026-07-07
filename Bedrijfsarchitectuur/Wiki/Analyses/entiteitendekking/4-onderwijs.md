---
type: analyse
titel: "Entiteitendekking: 4 Onderwijs"
datum: 2026-07-07
taakveld: "4 Onderwijs"
beleidsdomeinen:
  - Leerplicht en Leerlingenvervoer
  - Onderwijs
totaal_entiteiten: 27
totaal_bo: 11
totaal_matches: 10
totaal_hiaten: 1
---

# Entiteitendekking: 4 Onderwijs

## Beoordeling

2 beleidsdomeinen, 27 GGM-entiteiten, dekking 93% (25/27). De niet-BO entiteiten volgen het gebruikelijke patroon: 2× actor (Leerplichtambtenaar, Vervoerder — medewerkers-/leveranciersrollen, geen zelfstandig bedrijfsobject) en 15× detail. De detailentiteiten in Leerplicht en Leerlingenvervoer zijn grotendeels subtypen van [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] (AanvraagVrijstelling, Verlofaanvraag) of granulaire gebeurtenissen rond een leerling (Beslissing, Doorgeleiding OM, HALT-verwijzing, Klacht Leerlingenvervoer, Ziekmelding Leerlingenvervoer) die terecht op detailniveau blijven. In Onderwijs zijn de details vooral classificaties en loopbaanstappen die als attribuut bij Leerling of School horen (Loopbaanstap, Onderwijsloopbaan, Onderwijssoort, Startkwalificatie).

De 2 niet-gedekte entiteiten (Leerjaar, Onderwijsniveau) zijn beide classificatie-achtige codelijsten zonder eigen attributen — ze horen logisch als waardelijst bij Leerling/School maar zijn in het GGM niet expliciet aan een BO-keten gekoppeld, waardoor ze als "⚠️ geen BO bereikbaar" naar voren komen. Dit is eerder een modelleringshiaat in de GGM-structuur (ontbrekende associatie) dan een inhoudelijk gemis. Functioneel is de dekking dus vrijwel compleet.

Slechts 1 BO zonder GGM-entiteit: [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/kinderopvangvoorziening\|Kinderopvangvoorziening]]. Dit is een reëel hiaat: kinderopvangvoorzieningen worden door gemeenten geregistreerd en getoetst (Landelijk Register Kinderopvang, Wet Kinderopvang), dus dit BO verdient een terugmelding aan het GGM-team ook al is het als procesobject geclassificeerd.

Twee naamconflicten zijn zichtbaar via hernoeming. GGM-entiteit Vrijstelling is vastgelegd als [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/leerplichtvrijstelling\|Leerplichtvrijstelling]] — een verduidelijking om verwarring met andere vrijstellingsbegrippen elders in de wiki te voorkomen. Belangrijker is GGM-entiteit Inschrijving, vastgelegd als [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/opleidingsinschrijving\|Opleidingsinschrijving]]: de Naamoverlap-kolom wijst naar [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbieding|Aanbieding]] in het inkoopdomein. "Inschrijving" is in het Nederlands ook de gangbare term voor een aanbestedingsbod (tender-inschrijving), dus dit is een echt homoniem tussen het onderwijsdomein en het inkoopdomein — de hernoeming naar Opleidingsinschrijving is nodig om beide begrippen uit elkaar te houden.

## Leerplicht en Leerlingenvervoer

15 entiteiten, 5 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Aanvraag Leerlingenvervoer]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/aanvraag-leerlingenvervoer\|Aanvraag Leerlingenvervoer]] ✅ | — |  | Exact match |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Beschikking Leerlingenvervoer]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/beschikking-leerlingenvervoer\|Beschikking Leerlingenvervoer]] ✅ | — |  | Exact match |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Procesverbaal Onderwijs]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/procesverbaal-onderwijs\|Procesverbaal Onderwijs]] ✅ | — |  | Exact match |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Verzuimmelding]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/verzuimmelding\|Verzuimmelding]] ✅ | — |  | Exact match |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Vrijstelling]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/leerplichtvrijstelling\|Leerplichtvrijstelling]] ✅ | synoniem |  | BO hernoemd: Leerplichtvrijstelling |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Leerplichtambtenaar]] | actor | n.v.t. | Medewerkerrol, geen zelfstandig BO |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Vervoerder]] | actor | n.v.t. | Leveranciersrol; subtype Leverancier |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|AanvraagOfMelding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|AanvraagVrijstelling]] | detail | via AanvraagOfMelding → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Subtype AanvraagOfMelding; te granulair |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Beslissing]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Doorgeleiding OM]] | detail | via Beslissing → [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Te specifiek; justitie-subtype |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|HALT-verwijzing]] | detail | via Beslissing → [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Te specifiek; justitie-subtype |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Klacht Leerlingenvervoer]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Te granulair; subtype klacht |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Verlofaanvraag]] | detail | via AanvraagOfMelding → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Subtype AanvraagOfMelding; te granulair |
| [[Wiki/GGM/4-onderwijs/leerplicht-en-leerlingenvervoer\|Ziekmelding Leerlingenvervoer]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Te granulair; operationeel detail |

## Onderwijs

12 entiteiten, 5 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/4-onderwijs/onderwijs\|Inschrijving]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/opleidingsinschrijving\|Opleidingsinschrijving]] ✅ | synoniem | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbieding|Aanbieding]] | BO hernoemd: Opleidingsinschrijving |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Leerling]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] ✅ | — |  | Exact match |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Ouder Of Verzorger]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/ouder-of-verzorger\|Ouder Of Verzorger]] ✅ | — |  | Exact match |
| [[Wiki/GGM/4-onderwijs/onderwijs\|School]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/school\|School]] ✅ | — |  | Exact match |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Uitschrijving]] | [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/uitschrijving\|Uitschrijving]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/4-onderwijs/onderwijs\|Leerjaar]] | detail | ⚠️ geen BO bereikbaar | Classificatie; attribuut van Leerling |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Locatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | Generiek kern-concept (Vastgoedobject); cross-domein |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Loopbaanstap]] | detail | via Onderwijsloopbaan → [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Te granulair; onderdeel van onderwijsloopbaan |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Onderwijsloopbaan]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Aggregatie zonder eigen attributen; gemeente beheert niet direct |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Onderwijsniveau]] | detail | ⚠️ geen BO bereikbaar | Classificatie; geen eigen attributen |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Onderwijssoort]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/school\|School]] | Classificatie; attribuut van School |
| [[Wiki/GGM/4-onderwijs/onderwijs\|Startkwalificatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling\|Leerling]] | Eigenschap van Leerling; relatie [0..1] |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/kinderopvangvoorziening\|Kinderopvangvoorziening]] | nee | procesobject | **Alleen GEMMA-BO** |
