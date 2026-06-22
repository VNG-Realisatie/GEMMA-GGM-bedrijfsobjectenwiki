---
type: domein
naam: Asiel en Integratie
status: afgerond
verwerkingsdatum: 2026-06-19
bronnen_count: 6
begrippen_count: 11
bo_count: 15
---

# Domein: Asiel en Integratie

Dit domein beschrijft het gemeentelijk perspectief op de asielketen: van opvang van asielzoekers tot inburgering van statushouders. De scope is wat de gemeente ziet, doet en registreert. Processen van ketenpartners (COA, IND, DT&V, AVIM, Nidos) worden benoemd als context maar niet als eigen bedrijfsobject uitgewerkt.

## Conclusie

15 bedrijfsobjecten vastgesteld: 13 met GGM-grondslag (exact match, beleidsdomein Inburgering), 2 zonder GGM (asielopvangfase). Het GGM modelleert het Wi2021-inburgeringstraject zeer gedetailleerd (35 entiteiten); daarvan zijn 13 bedrijfsobjecten, 18 zijn geaggregeerd als attributen/details, en 4 zijn classificaties of abstracte entiteiten. De asielopvangfase valt structureel buiten het GGM — dit is een hiaatbevinding.

## Twee fasen

1. **Asielopvang** — de gemeente faciliteert opvanglocaties en kan bij duurzame gemeentelijke opvang ook exploiteren. **2 BO's, geen GGM-dekking.**
2. **Inburgering** — na vergunningverlening begeleidt de gemeente de inburgeraar conform Wi2021. **13 BO's, volledige GGM-dekking.**

## Bedrijfsobjecten

### Inburgering (GGM beleidsdomein Inburgering, taakveld 6)

| BO | GGM-entiteit | Matchsterkte |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Asielstatushouder | exact |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/gezinsmigrant\|Gezinsmigrant]] | Gezinsmigrant en Overige migrant | exact |
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

### Asielopvang (geen GGM)

| BO | Grondslag | Reden geen GGM |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/opvanglocatie\|Opvanglocatie]] | procesobject | Asielopvang structureel niet gemodelleerd in GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/bestuursovereenkomst\|Bestuursovereenkomst]] | governance-object | Governance-objecten vallen buiten GGM-scope |

## GGM-dekkingsanalyse

**35 GGM-entiteiten beoordeeld:**
- 13 → BO (zie tabel hierboven)
- 4 → classificatie/abstract: Inburgeraar (abstract, specialisaties zijn BO), Vreemdeling (te generiek), B1-route (type van Leerroute), Z-route (type van Leerroute)
- 18 → attribuut/detail van ander BO: Aandachtspunt, Ontwikkelwens, Subdoel Aandachtspunt, Subdoel Ontwikkelwens, Hoofddoel, Taalvaardigheid, ICT-Vaardigheid (→ details van PIP/Brede Intake); Examenonderdeel (→ detail van Examen); Ontheffing, Vrijstelling, Verlengingsgrond (→ status van Inburgeringsplicht); Aanvraag verlenging Inburgeringstermijn (→ processtap); Diplomawaardering, Educatie, Werk, Training (→ achtergrondinformatie); Verblijfplaats AZC (→ locatiegegeven); Introductiemodule (→ onderdeel Voorbereiding)

**Generalisatiekeuze:** Inburgeraar (abstract) → twee aparte BO's: Asielstatushouder en Gezinsmigrant. Reden: verschillende instroom, ander voortraject (voorinburgering alleen bij asiel), andere koppelingsroute.

**Terugmelding GGM:** asielopvangfase ontbreekt volledig — opvanglocatie, bestuursovereenkomst en exploitatievorm zijn niet gemodelleerd.

## Begrippen

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| asielopvang | thema | Overkoepelend thema voor opvang van asielzoekers | ❌ | Thema, geen object | — | nee |
| inburgering | thema | Het formele traject na vergunningverlening | ❌ | Thema, geen object | — | nee |
| spreidingswet | instrument | Wettelijke taak gemeenten voor opvangplekken | ❌ | Instrument, geen object | — | nee |
| duurzame gemeentelijke opvang | instrument | Exploitatievorm waarbij gemeente begeleiding overneemt | ❌ | Instrument, geen object | — | nee |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/bestuursovereenkomst\|Bestuursovereenkomst]] | instrument | Formele afspraken COA-gemeente per locatie | ✅ | Governance-object, eigen levenscyclus | BOK Zeist | nee |
| voorinburgering | instrument | Voorbereiding op inburgering in de opvangfase | ❌ | Onderdeel van inburgeringstraject | — | nee |
| meedoenbalie | instrument | Loket voor participatie en arbeidstoeleiding | ❌ | Instrument, geen object | — | nee |
| kansrijke koppeling | instrument | Koppeling statushouder aan gemeente op basis van profiel | ❌ | Instrument/procedure | — | nee |
| statushouder | doelgroep | Persoon met verblijfsvergunning | ❌ | Doelgroep, geen object | — | nee |
| alleenstaande minderjarige vreemdeling | doelgroep | Jongere zonder ouder/begeleider | ❌ | Doelgroep, geen object | — | nee |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/opvanglocatie\|Opvanglocatie]] | object | Fysieke locatie voor opvang, in diverse vormen | ✅ | 6/6 criteria, procesobject | AZC, noodopvang | nee |
| inhuisregistratie | object | Wekelijkse aanwezigheidscontrole op locatie | ❌ | Eigenschap/proces van opvanglocatie | — | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer|Asielopvangwijzer: alle informatie voor gemeenten]] — COA portaalpagina voor gemeenten
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids|COA Dienstverleningsgids voor gemeenten (januari 2026)]] — COA taakverdeling en dienstverlening (januari 2026)
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang|Asielopvang]] — VNG onderwerpenpagina asielopvang
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering|Inburgering]] — VNG onderwerpenpagina inburgering
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine|Opvang Oekraïense ontheemden]] — VNG onderwerpenpagina Oekraïense ontheemden
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel|Rubriek Asiel tot integratie]] — VNG rubriekpagina asiel tot integratie

## Raakvlakken

- **Werk en Inkomen** — inburgering richt zich op arbeidstoeleiding; MAP als BO raakt arbeidsmarktbeleid
- **Maatschappelijke Ondersteuning** — Brede Intake raakt ook Wmo-ondersteuning
- **Openbare Orde en Veiligheid** — opvanglocaties raken openbare orde
