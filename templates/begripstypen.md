# Begripstypen en abstractieniveaus

Begrippen in de domeinoverzichttabel hebben twee onafhankelijke classificaties: **begripstype** (kolom "Type") en **abstractieniveau** (impliciet in de beoordeling). Samen bepalen ze of een begrip een BO-kandidaat is en of een GGM-match verwacht wordt.

## Begripstypen (gemapt op ArchiMate)

| Begripstype | Omschrijving | ArchiMate-elementtype | BO-kandidaat? | GGM-match? |
|---|---|---|---|---|
| **object** | Concreet ding dat in processen wordt gebruikt/geproduceerd/geregistreerd | Business Object | Ja | Verwacht |
| **instrument** | Regeling, programma, wet, maatregel, verordening | Contract / Product | Ja | Nee (governance-hiaat GGM) |
| **actor** | Rol, organisatie, samenwerkingsverband | Business Actor / Role | Mogelijk | Deels (RSGB) |
| **doelgroep** | Groep waarop beleid of uitvoering gericht is | Business Actor (als rol) | Mogelijk | Deels (RSGB) |
| **thema** | Werkgebied dat doelen, actoren en instrumenten bundelt | Grouping | Nee | Nee |
| **doel** | Nagestreefde situatie of uitkomst | Goal / Outcome | Nee | Nee |
| **waarde** | Maatschappelijk ideaal, richtinggevend principe | Driver / Principle | Nee | Nee |

**BO-filterlogica:**
- **object** en **instrument** → BO-kandidaten (passive structure)
- **actor** en **doelgroep** → mogelijk BO (active structure)
- **thema**, **doel**, **waarde** → geen BO, wel context voor onderbouwing

**GGM-terugmeldlogica:**
- GGM-match verwacht maar afwezig → hiaat, terugmelden aan GGM
- GGM-match niet verwacht → structureel buiten GGM-scope, geen terugmelding

## Abstractieniveaus

| Niveau | Kernvraag |
|---|---|
| **operationeel** | Wordt dit concreet gebruikt/geregistreerd in processen? |
| **beleidsmatig** | Is dit richtinggevend/strategisch? |

De twee dimensies versterken elkaar:
- `object` + `operationeel` → sterke BO-kandidaat, GGM-match verwacht
- `instrument` + `operationeel` → BO-kandidaat (governance-object), GGM-hiaat verwacht
- `object` + `beleidsmatig` → ongewone combinatie, nader bekijken
- `doel` + `beleidsmatig` → verwacht, geen BO
