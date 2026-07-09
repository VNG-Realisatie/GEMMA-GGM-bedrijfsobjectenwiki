---
type: domein
naam: Asiel en Integratie
status: afgerond
verwerkingsdatum: 2026-06-27
bronnen_count: 8
begrippen_count: 12
bo_count: 17
---

# Domein: Asiel en Integratie

Dit domein beschrijft het gemeentelijk perspectief op de asielketen: van opvang van asielzoekers tot inburgering van statushouders. De scope is wat de gemeente ziet, doet en registreert. Processen van ketenpartners (COA, IND, DT&V, AVIM, Nidos) worden benoemd als context maar niet als eigen bedrijfsobject uitgewerkt.

## Conclusie

17 bedrijfsobjecten vastgesteld: 15 met GGM-grondslag (exact match, beleidsdomein Inburgering), 2 zonder GGM (asielopvangfase). Het GGM modelleert het Wi2021-inburgeringstraject zeer gedetailleerd (35 entiteiten); daarvan zijn 15 bedrijfsobjecten, 16 zijn geaggregeerd als attributen/details, en 4 zijn classificaties of abstracte entiteiten. De asielopvangfase valt structureel buiten het GGM — dit is een hiaatbevinding.

## Twee fasen

1. **Asielopvang** — de gemeente faciliteert opvanglocaties en kan bij duurzame gemeentelijke opvang ook exploiteren. **2 BO's, geen GGM-dekking.**
2. **Inburgering** — na vergunningverlening begeleidt de gemeente de inburgeraar conform Wi2021. **15 BO's, volledige GGM-dekking.**

## Bedrijfsobjecten

### Inburgering (GGM beleidsdomein Inburgering, taakveld 6)

| BO | GGM-entiteit | Matchsterkte |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Asielstatushouder | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/gezinsmigrant-en-overige-migrant\|Gezinsmigrant]] | Gezinsmigrant en Overige migrant | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake\|Brede Intake]] | Brede Intake | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip\|PIP]] | PIP | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstraject\|Inburgeringstraject]] | Inburgeringstraject | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute\|Leerroute]] | Leerroute | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht\|Inburgeringsplicht]] | Inburgeringsplicht | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen\|Examen]] | Examen | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] | InburgeringsAanbod | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstermijn\|Inburgeringstermijn]] | Inburgeringstermijn | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/map\|MAP]] | MAP | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pvt\|PVT]] | PVT | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/voorbereiding-op-inburgering\|Voorbereiding op Inburgering]] | Voorbereiding op Inburgering | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/vrijstelling\|Vrijstelling]] | Vrijstelling | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/ontheffing\|Ontheffing]] | Ontheffing | exact |

### Asielopvang (geen GGM)

| BO | Grondslag | Reden geen GGM |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/opvanglocatie\|Opvanglocatie]] | procesobject | Asielopvang structureel niet gemodelleerd in GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/bestuursovereenkomst\|Bestuursovereenkomst]] | governance-object | Governance-objecten vallen buiten GGM-scope |

## Begrippen

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|asielopvang|thema|Overkoepelend thema voor opvang van asielzoekers| ❌ | nee |Thema, geen object|—|nee|
|inburgering|thema|Het formele traject na vergunningverlening| ❌ | nee |Thema, geen object|—|nee|
|spreidingswet|instrument|Wettelijke taak gemeenten voor opvangplekken| ❌ | nee |Instrument, geen object|—|nee|
|duurzame gemeentelijke opvang|instrument|Exploitatievorm waarbij gemeente begeleiding overneemt| ❌ | nee |Instrument, geen object|—|nee|
|[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/bestuursovereenkomst\|Bestuursovereenkomst]]|instrument|Formele afspraken COA-gemeente per locatie| ✅ | nee |Governance-object, eigen levenscyclus|BOK Zeist|nee|
|voorinburgering|instrument|Voorbereiding op inburgering in de opvangfase| ❌ | nee |Onderdeel van inburgeringstraject|—|nee|
|meedoenbalie|instrument|Loket voor participatie en arbeidstoeleiding| ❌ | nee |Instrument, geen object|—|nee|
|kansrijke koppeling|instrument|Koppeling statushouder aan gemeente op basis van profiel| ❌ | nee |Instrument/procedure|—|nee|
|statushouder|doelgroep|Persoon met verblijfsvergunning| ❌ | nee |Doelgroep, geen object|—|nee|
|alleenstaande minderjarige vreemdeling|doelgroep|Jongere zonder ouder/begeleider| ❌ | nee |Doelgroep, geen object|—|nee|
|[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/opvanglocatie\|Opvanglocatie]]|object|Fysieke locatie voor opvang, in diverse vormen| ✅ | ja |6/6 criteria, procesobject|AZC, noodopvang|nee|
|inhuisregistratie|object|Wekelijkse aanwezigheidscontrole op locatie| ❌ | ja |Eigenschap/proces van opvanglocatie|—|nee|

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer|Asielopvangwijzer: alle informatie voor gemeenten]] — COA portaalpagina voor gemeenten
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids|COA Dienstverleningsgids voor gemeenten (januari 2026)]] — COA taakverdeling en dienstverlening (januari 2026)
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang|Asielopvang]] — VNG onderwerpenpagina asielopvang
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering|Inburgering]] — VNG onderwerpenpagina inburgering
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine|Opvang Oekraïense ontheemden]] — VNG onderwerpenpagina Oekraïense ontheemden
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel|Rubriek Asiel tot integratie]] — VNG rubriekpagina asiel tot integratie
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/regeling-inburgering-2021|Regeling inburgering 2021]] — Ministeriële uitvoeringsregeling Wi2021 (vrijstellingen, ontheffingen, examens, lening)

## Raakvlakken

- **Werk en Inkomen** — inburgering richt zich op arbeidstoeleiding; MAP als BO raakt arbeidsmarktbeleid
- **Maatschappelijke Ondersteuning** — Brede Intake raakt ook Wmo-ondersteuning
- **Openbare Orde en Veiligheid** — opvanglocaties raken openbare orde
