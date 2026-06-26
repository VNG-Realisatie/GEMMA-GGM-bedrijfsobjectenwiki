---
type: bronsamenvatting
titel: "Handleiding Publicatiestandaard Algoritmeregister"
onderwerp: [Informatiesamenleving]
datum_ingest: 2026-06-26
---

# Handleiding Publicatiestandaard Algoritmeregister

Handleiding van het Ministerie van BZK met toelichting op alle velden van de Publicatiestandaard van het Algoritmeregister van de Nederlandse Overheid. Beschrijft per veld het invoertype, de helptekst, instructies en voorbeelden.

## Samenvatting

Het Algoritmeregister is het centrale register waarin overheidsorganisaties hun algoritmes publiceren. De Publicatiestandaard definieert welke informatie per algoritme wordt vastgelegd, verdeeld over 4 secties met ~25 velden.

### 2.1 Algemene informatie

| Veld | Invoertype | Tonen |
|---|---|---|
| **Naam** | Tekst (<100 tekens) | Verplicht |
| **Korte omschrijving** | Tekst (<350 tekens) | Verplicht |
| **Organisatie** | Tekst (<100 tekens, TOOI-waardelijst) | Verplicht |
| **Thema** | Lijst (OWMS-waardelijst) | Ja |
| **Status** | Keuze: In gebruik / In ontwikkeling / Buiten gebruik | Verplicht |
| **Begindatum** | yyyy-mm | Ja |
| **Einddatum** | yyyy-mm | Nee |
| **Contactgegevens** | URL of e-mail | Verplicht |
| **Link naar publiekspagina** | URL | Nee |
| **Publicatiecategorie** | Keuze: Hoog-risico AI / Impactvol / Overig | Verplicht |
| **Link naar bronregistratie** | URL (decentraal register) | Nee |

### 2.2 Verantwoord gebruik

| Veld | Invoertype | Tonen |
|---|---|---|
| **Doel en impact** | Tekst (<2500 tekens, B1) | Ja |
| **Afwegingen** | Tekst (<2500 tekens, B1) | Ja |
| **Menselijke tussenkomst** | Tekst (<2500 tekens, B1) | Ja |
| **Risicobeheer** | Tekst (<2500 tekens) | Ja |
| **Wettelijke basis** | Tekst (<2500 tekens) | Nee |
| **Link naar wettelijke basis** | URL | Nee |
| **Titel van wettelijke basis** | Tekst | Nee |
| **Link naar verwerkingsregister** | URL | Nee |
| **Impactoetsen** | Tekst | Nee |
| **Link naar impactoets** | URL | Nee |
| **Toelichting op impactoetsen** | Tekst | Nee |

### 2.3 Werking

| Veld | Invoertype | Tonen |
|---|---|---|
| **Gegevens** | Tekst | Nee |
| **Link naar gegevensbronnen** | URL | Nee |
| **Titel van gegevensbron** | Tekst | Nee |
| **Technische werking** | Tekst | Nee |
| **Leverancier** | Tekst | Nee |
| **Link naar broncode** | URL | Nee |

### 2.4 Metadata

| Veld | Invoertype | Tonen |
|---|---|---|
| **Taal** | Tekst | Nee |
| **Schema** | Tekst | Nee |
| **Bron-ID** | Tekst | Nee |
| **Zoektermen** | Tekst | Nee |

### Publicatiecategorie (driedeling)

- **Categorie A: Hoog-risico AI-systeem** — zoals gedefinieerd in de AI-verordening
- **Categorie B: Impactvolle algoritmes** — niet AI-verordening hoog-risico, maar wel maatschappelijke impact
- **Categorie C: Overige algoritmes** — vrijwillige publicatie

### Versiebeheer

Het register ondersteunt bewerkingsgeschiedenis per registratie.

## Kernbegrippen

- **Algoritmeregister** — vastlegging van een algoritme in het Algoritmeregister met ~25 velden over doel, werking, verantwoording en metadata. Eigen levenscyclus (in ontwikkeling → in gebruik → buiten gebruik).
- **Publicatiestandaard** — het schema dat definieert welke velden per algoritme worden vastgelegd. In ontwikkeling, beheerd door BZK.
- **Publicatiecategorie** — driedeling van algoritmes: hoog-risico AI (A), impactvol (B), overig (C). Bepaalt welke velden verwacht worden.
- **Algoritmeregister** — centraal register op algoritmes.overheid.nl. Decentrale registers mogelijk met link naar bronregistratie.

## Relevantie voor bedrijfsarchitectuur

Deze bron levert de definitieve grondslag voor **Algoritmeregister** als BO:
- ~25 velden met gedefinieerde invoertypes
- Eigen levenscyclus met statuswaarden (in ontwikkeling, in gebruik, buiten gebruik)
- Versiebeheer met bewerkingsgeschiedenis
- Relaties met [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit|Verwerkingsactiviteit]] (link verwerkingsregister), [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia|DPIA]] (link impactoets), [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling|Grondrechteneffectbeoordeling]] (categorie A = hoog-risico AI)

De publicatiecategorie koppelt direct aan de AI-verordening: categorie A = hoog-risico AI-systeem → verplichtingen art. 26-27 AI-verordening.

## Citaten

> "Deze handleiding bevat een toelichting op de velden van de Publicatiestandaard van het Algoritmeregister van de Nederlandse Overheid." (bron: BZK handleiding)

> "Tot welke categorie een algoritme behoort: Hoog-risico AI-systeem (Categorie A), Impactvolle algoritmes (Categorie B), Overige algoritmes (Categorie C)" (bron: BZK handleiding, veld Publicatiecategorie)

## Bronnen
- [[Sources/Onderwerpen/Informatiesamenleving/handleiding-publicatiestandaard-algoritmeregister]]
