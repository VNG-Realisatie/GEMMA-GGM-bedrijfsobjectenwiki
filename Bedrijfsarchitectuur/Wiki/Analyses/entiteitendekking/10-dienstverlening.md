---
type: analyse
titel: "Entiteitendekking: 10 Dienstverlening"
datum: 2026-06-29
taakveld: "10 Dienstverlening"
beleidsdomeinen:
  - 10 Dienstverlening
totaal_entiteiten: 16
totaal_bo: 12
totaal_matches: 3
totaal_hiaten: 9
---

# Entiteitendekking: 10 Dienstverlening

## Beoordeling

<!-- REVIEW: pas deze beoordeling aan met domeinkennis -->

1 beleidsdomeinen, 16 GGM-entiteiten. Dekking: 15 van 16 (94%) — 3 met BO, 12 ondersteunend, 1 niet gedekt. 9 BO's zonder GGM-entiteit.

Niet-BO entiteiten: 1× classificatie, 12× detail.

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
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Formuliersoortveld]] | detail | via Aanvraagdata → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Klantbeoordeling]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Klantbeoordelingreden]] | detail | via Klantbeoordeling → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|MOR-AanvraagOfMelding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Onderwerp]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Telefoononderwerp]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Telefoonstatus]] | detail | via Telefoontje → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/10-dienstverlening/10-dienstverlening\|Telefoontje]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Detailgegeven |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/algoritmeregister\|Algoritmeregister]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia\|DPIA]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/datalek\|Datalek]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling\|Grondrechteneffectbeoordeling]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen\|Vergunningen en ontheffingen]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkersovereenkomst\|Verwerkersovereenkomst]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit\|Verwerkingsactiviteit]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klacht\|klacht]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/woo-verzoek\|woo-verzoek]] | nee | procesobject | **Alleen GEMMA-BO** |
