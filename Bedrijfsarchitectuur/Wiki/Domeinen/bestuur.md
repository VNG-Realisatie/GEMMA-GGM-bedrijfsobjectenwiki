---
type: domein
naam: Bestuur
status: afgerond
verwerkingsdatum: 2026-06-19
bronnen_count: 9
begrippen_count: 7
bo_count: 4
---

# Bestuur

Dit domein omvat de lokale politieke en bestuurlijke processen van gemeenten: verkiezingen, raadsvergaderingen, bestuurlijke samenwerking met andere overheden, en initiatieven voor democratische vernieuwing. Het is geen onderwerp van gemeentelijk beleid, maar de structuur en organisatie van het lokale bestuur zelf.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/verkiezing]] | object | Periodieke vervangingskeuze van gekozen ambtsdragers (raadsleden, burgemeester) | ✅ | 6/6 criteria; gemeentelijke organisatieverplichting; eigen levenscyclus | Raadsverkiezing 2026, Kamerverkiezing maart 2026 | **nee** (hiaat) |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/referendum]] | object | Volksstemming over een onderwerp, ingesteld door gemeente of raad | ✅ | 6/6 criteria; aparte organisatorische verantwoordelijkheid | Lokaal referendum over bouwplaats | **nee** (hiaat) |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/stembureau]] | object | Fysieke locatie waar kiezers hun stem uitbrengen; registratie van adres, capaciteit, toegankelijkheid | ✅ | 6/6 criteria; operationeel object met eigenschappen en relaties | Basisschool De Toekomst (stembureaunummer 42), Wijkcentrum Noord | **nee** (hiaat) |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/gemeenschappelijke-regeling]] | object | Publiekrechtelijke samenwerkingsconstructie tussen gemeenten, provincies, waterschappen (grondslag: Wgr) | ✅ | 6/6 criteria; juridische entiteit met eigen bestuur/begroting | GGD, RUD, woningmarktregeling, jeugdzorgregeling | **nee** (hiaat) |
| lokale omroep | actor | Publieke mediaorganisatie op gemeentelijk niveau (externe partij) | ❌ | Externe organisatie; gemeente heeft relatie (bekostiging, advies) maar omroep is niet gemeentelijk object | Omroep Amsterdam, RTV Rijnmond | nee |
| gemeenteraad | governance | Gekozen vertegenwoordigend lichaam; besluiten over beleid en begroting | ❌ | Governance-structuur; rol/functie, geen aparte dingen | — | nee |
| college | governance | Dagelijks bestuur, collegeleden voeren raadsbesluit uit | ❌ | Governance-structuur; organisatorische rol | — | nee |

## GGM-dekkingsanalyse

**Bevinding: Scope-verschil tussen procesobjecten en dataobjecten.**

Het GGM modelleert **dataobjecten** (wat gemeenten registreren), niet **processen** (hoe werk verloopt). Dit verklaart waarom sommige BO's geen GGM-grondslag hebben:

| BO | Grondslag | Type | GGM-status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/verkiezing]] | procesobject | **Proces** | Niet in GGM — geen database met "verkiezingen"; gemeenten registreren uitslagen (data), niet het proces |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/referendum]] | procesobject | **Proces** | Niet in GGM — ook een proces, niet een registratieobject |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/stembureau]] | procesobject | **Data** ⚠️ | **Potentiële hiaat** — fysieke locaties (adres, capaciteit, toegankelijkheid) zouden als registratieobject kunnen passen |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/gemeenschappelijke-regeling]] | governance-object | **Data** ⚠️ | **Potentiële hiaat** — juridische entiteit met registreerbare eigenschappen (deelnemers, personeelssterkte, begroting) |

**Terugmelding-logica:**
- Verkiezing en Referendum: **Geen terugmelding** — dit zijn processen, structureel buiten GGM-scope
- Stembureau en Gemeenschappelijke Regeling: **Wel terugmelden** — dit zijn registratieobjecten die passen in GGM-data-laag

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/alv-jaarcongres-en-bestuurdersdag|ALV, Jaarcongres en Bestuurdersdag]] — VNG-niveau; relevantie voor gemeentelijke raadsvergaderingen
- [[Wiki/Bronsamenvattingen/Bestuur/gemeentelijke-samenwerking|Gemeentelijke Samenwerking]] — Wgr-grondslag voor samenwerking
- [[Wiki/Bronsamenvattingen/Bestuur/gemeenteraadsverkiezingen-2026|Gemeenteraadsverkiezingen 2026]] — Gemeentelijke organisatietaken rond verkiezingen
- [[Wiki/Bronsamenvattingen/Bestuur/lokale-omroepen|Lokale omroepen]] — Gemeentelijke rol en relatie met externe omroepen
- [[Wiki/Bronsamenvattingen/Bestuur/rubriek-bestuur|Rubriek Bestuur]] — Governance-raamwerk en visie op bestuurlijke organisatie
- [[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda|Verkiezingen en referenda]] — Gemeentelijke verantwoordelijkheid voor alle verkiezingen en referenda
- [[Wiki/Bronsamenvattingen/Bestuur/versterking-lokale-democratie|Versterking lokale democratie]] — Governance-principes en democratische experimenten
- [[Wiki/Bronsamenvattingen/Bestuur/vng-inzet-kabinet|VNG-inzet kabinet]] — VNG-level advocacy; context
- [[Wiki/Bronsamenvattingen/Bestuur/vng-raadgevers|VNG Raadgevers]] — Informatieresources; context

## Nog te verwerken

Geen; alle 9 Sources/Onderwerpen/Bestuur-bestanden zijn verwerkt.

## Designkeuzes

1. **Verkiezing als abstract object**: Eén BO "Verkiezing" met aparte instanties voor elke verkiezingstype (raad, kamer, water, europa). Granulariteit: gemeentelijke organisatie-verantwoordelijkheid.
2. **Referendum als apart BO**: Aparte organisatie (Wgr voor GR, geen Wgr voor referendum) → aparte BO.
3. **Stembureau als operationeel object**: Fysieke locatie met registratie (adres, capaciteit, toegankelijkheid) → sterke BO.
4. **Gemeenschappelijke Regeling als governance-object**: Juridische construct (Wgr) met eigen rechtspersoonlijkheid → sterke BO, maar grondslag is governance, niet GGM-data.

## Terugmeldingen naar GGM-community

| BO | Type melding | Status |
|---|---|---|
| Verkiezing | Hiaat: procesobject | Open — proposal: Taakveld 0, Politiek beleidsdomein |
| Referendum | Hiaat: procesobject | Open — proposal: Taakveld 0, Politiek beleidsdomein |
| Stembureau | Hiaat: procesobject | Open — proposal: Taakveld 0, Politiek beleidsdomein of ondersteunend |
| Gemeenschappelijke Regeling | Hiaat: governance-object | Open — proposal: Taakveld 0 of 9, nieuw/uitgebreid beleidsdomein |
