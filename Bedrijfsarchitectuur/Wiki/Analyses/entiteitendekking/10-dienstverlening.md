---
type: analyse
titel: "Entiteitendekking: 10 Dienstverlening"
datum: 2026-07-07
taakveld: "10 Dienstverlening"
beleidsdomeinen:
  - 10 Dienstverlening
totaal_entiteiten: 16
totaal_bo: 13
totaal_matches: 3
totaal_hiaten: 10
---

# Entiteitendekking: 10 Dienstverlening

## Beoordeling

1 beleidsdomeinen, 16 GGM-entiteiten. Dekking: 15 van 16 (94%) — 3 met BO, 12 ondersteunend, 1 niet gedekt. 10 BO's zonder GGM-entiteit.

Niet-BO entiteiten: 1× classificatie, 1× component, 11× detail.

Het grootste deel van de niet-BO entiteiten hangt direct aan de drie herkende BO's: Aanvraagdata, Onderwerp, MOR-AanvraagOfMelding en Formuliersoort/Formuliersoortveld beschrijven [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]]; Afspraakstatus hoort bij [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]]; Telefoontje, Telefoonstatus en Telefoononderwerp bij [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]]; Klantbeoordeling en Klantbeoordelingreden bij Organisatorische eenheid. Formuliersoortveld is hier het enige structurele geval: het is geen kenmerk van een aanvraag maar een velddefinitie die bij een Formuliersoort hoort ("heeft velden"-relatie) — dus een component van de classificatie-entiteit Formuliersoort, niet een detail van de aanvraag zelf. MOR-AanvraagOfMelding laat een tweede patroon zien: een kanaal-specifieke variant (Meldingen Openbare Ruimte) van dezelfde BO, wat wijst op hergebruik van één BO voor meerdere invoerkanalen in plaats van aparte deelmodellen.

Functioneel is de dekking hoog (94%), op Artikel na dat als enige geen BO bereikbaar heeft (⚠️) — een entiteit met weinig attributen zonder duidelijke associatie, wat er op wijst dat hier ofwel een BO ontbreekt (bijvoorbeeld rond wet- en regelgevingreferenties) ofwel dat Artikel eigenlijk overbodig/onderbenut is in het model. Van de 10 BO's zonder GGM-tegenhanger is er één expliciet als ggm-hiaat gemarkeerd: Informatieobject, een generiek documentbegrip dat in de wiki wel als zelfstandig BO is vastgelegd maar in het GGM ontbreekt — een reële modelleerlacune. De overige negen (Algoritmeregister, DPIA, Datalek, Grondrechteneffectbeoordeling, Vergunningen en ontheffingen, Verwerkersovereenkomst, Verwerkingsactiviteit, Klacht, Woo-verzoek) zijn procesobjecten of governance-objecten die horen bij wettelijke verantwoordingsverplichtingen (AVG, Woo) rond dienstverlening, niet bij de primaire dienstverleningsdata zelf — het GGM legt terecht de nadruk op het aanvraag/klantcontact-datamodel en niet op deze compliance-processen.

Naamconflicten doen zich niet voor via de Naamoverlap-kolom, maar wel via de Entiteitstype-kolom bij de BO-matches: AanvraagOfMelding en ProductOfDienst zijn in de wiki hernoemd naar leesbare Nederlandse namen ("Aanvraag of melding", "Product of dienst") — een naamsverschil, geen inhoudelijk conflict.

## 10 Dienstverlening

16 entiteiten, 3 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|AanvraagOfMelding]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] ✅ | synoniem |  | BO hernoemd: Aanvraag of melding |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Balieafspraak]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]] ✅ | — |  | Exact match |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|ProductOfDienst]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|Product of dienst]] ✅ | synoniem |  | BO hernoemd: Product of dienst |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Formuliersoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Typering/referentietabel |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Aanvraagdata]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Afspraakstatus]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Artikel]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|ExterneBron]] | detail | via Batch → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Formuliersoortveld]] | component | via Aanvraagdata → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Component (veld behorend bij Formuliersoort) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Klantbeoordeling]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Klantbeoordelingreden]] | detail | via Klantbeoordeling → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|MOR-AanvraagOfMelding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Onderwerp]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Telefoononderwerp]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Telefoonstatus]] | detail | via Telefoontje → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Telefoontje]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Detailgegeven (geassocieerd met BO) |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/algoritmeregister\|Algoritmeregister]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia\|DPIA]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/datalek\|Datalek]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling\|Grondrechteneffectbeoordeling]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/informatieobject\|Informatieobject]] | nee | ggm-hiaat | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen\|Vergunningen en ontheffingen]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkersovereenkomst\|Verwerkersovereenkomst]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit\|Verwerkingsactiviteit]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klacht\|klacht]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/woo-verzoek\|woo-verzoek]] | nee | procesobject | **Alleen GEMMA-BO** |
