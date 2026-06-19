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
| [[asielstatushouder]] | Asielstatushouder | exact |
| [[gezinsmigrant]] | Gezinsmigrant en Overige migrant | exact |
| [[brede-intake]] | Brede Intake | exact |
| [[pip]] | PIP | exact |
| [[inburgeringstraject]] | Inburgeringstraject | exact |
| [[leerroute]] | Leerroute | exact |
| [[inburgeringsplicht]] | Inburgeringsplicht | exact |
| [[examen]] | Examen | exact |
| [[inburgeringsaanbod]] | InburgeringsAanbod | exact |
| [[inburgeringstermijn]] | Inburgeringstermijn | exact |
| [[map]] | MAP | exact |
| [[pvt]] | PVT | exact |
| [[voorbereiding-op-inburgering]] | Voorbereiding op Inburgering | exact |

### Asielopvang (geen GGM)

| BO | Grondslag | Reden geen GGM |
|---|---|---|
| [[opvanglocatie]] | procesobject | Asielopvang structureel niet gemodelleerd in GGM |
| [[bestuursovereenkomst]] | governance-object | Governance-objecten vallen buiten GGM-scope |

## GGM-dekkingsanalyse

**35 GGM-entiteiten beoordeeld:**
- 13 → BO (zie tabel hierboven)
- 4 → classificatie/abstract: Inburgeraar (abstract, specialisaties zijn BO), Vreemdeling (te generiek), B1-route (type van Leerroute), Z-route (type van Leerroute)
- 18 → attribuut/detail van ander BO: Aandachtspunt, Ontwikkelwens, Subdoel Aandachtspunt, Subdoel Ontwikkelwens, Hoofddoel, Taalvaardigheid, ICT-Vaardigheid (→ details van PIP/Brede Intake); Examenonderdeel (→ detail van Examen); Ontheffing, Vrijstelling, Verlengingsgrond (→ status van Inburgeringsplicht); Aanvraag verlenging Inburgeringstermijn (→ processtap); Diplomawaardering, Educatie, Werk, Training (→ achtergrondinformatie); Verblijfplaats AZC (→ locatiegegeven); Introductiemodule (→ onderdeel Voorbereiding)

**Generalisatiekeuze:** Inburgeraar (abstract) → twee aparte BO's: Asielstatushouder en Gezinsmigrant. Reden: verschillende instroom, ander voortraject (voorinburgering alleen bij asiel), andere koppelingsroute.

**Terugmelding GGM:** asielopvangfase ontbreekt volledig — opvanglocatie, bestuursovereenkomst en exploitatievorm zijn niet gemodelleerd.

## Begrippen

### Thema's
- [[asielopvang]] — overkoepelend thema voor opvang van asielzoekers
- [[inburgering]] — het formele traject na vergunningverlening

### Instrumenten
- [[spreidingswet]] — wettelijke taak gemeenten voor opvangplekken
- [[duurzame-gemeentelijke-opvang]] — exploitatievorm waarbij gemeente begeleiding overneemt
- [[bestuursovereenkomst]] — formele afspraken COA-gemeente per locatie
- [[voorinburgering]] — voorbereiding op inburgering in de opvangfase
- [[meedoenbalie]] — loket voor participatie en arbeidstoeleiding
- [[kansrijke-koppeling]] — koppeling statushouder aan gemeente op basis van profiel

### Doelgroepen
- [[statushouder]] — persoon met verblijfsvergunning
- [[alleenstaande-minderjarige-vreemdeling]] — jongere zonder ouder/begeleider

### Objecten
- [[opvanglocatie]] — fysieke locatie voor opvang, in diverse vormen
- [[inhuisregistratie]] — wekelijkse aanwezigheidscontrole op locatie

## Verwerkte bronnen

- [[asielopvangwijzer]] — COA portaalpagina voor gemeenten
- [[coa-dienstverleningsgids]] — COA taakverdeling en dienstverlening (januari 2026)
- [[vng-asielopvang]] — VNG onderwerpenpagina asielopvang
- [[vng-inburgering]] — VNG onderwerpenpagina inburgering
- [[vng-opvang-oekraine]] — VNG onderwerpenpagina Oekraïense ontheemden
- [[vng-rubriek-asiel]] — VNG rubriekpagina asiel tot integratie

## Raakvlakken

- **Werk en Inkomen** — inburgering richt zich op arbeidstoeleiding; MAP als BO raakt arbeidsmarktbeleid
- **Maatschappelijke Ondersteuning** — Brede Intake raakt ook Wmo-ondersteuning
- **Openbare Orde en Veiligheid** — opvanglocaties raken openbare orde
