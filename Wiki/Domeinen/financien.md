---
type: domein
naam: Financien
status: in-behandeling
verwerkingsdatum: 2026-06-19
bronnen_count: 4
begrippen_count: 10
bo_count: 10
---

# Domein: Financiën

Gemeentelijke financiën — inkomstenbronnen, begrotingscyclus, financieel beheer en financiële gezondheid.

## Begrippen

### Inkomstenbronnen
- [[gemeentefonds]] — grootste inkomstenbron, vrij besteedbaar
- [[algemene-uitkering]] — hoofdcomponent gemeentefonds
- [[specifieke-uitkering]] — geoormerkt geld van het rijk voor medebewindstaken

### Begrotingscyclus en governance
- [[begrotingscyclus]] — kadernota → begroting → tussenrapportages → jaarrekening
- [[budgetrecht]] — raadsbevoegdheid om geld beschikbaar te stellen
- [[financiele-verordening]] — art. 212 Gemeentewet, lokale spelregels financieel beleid
- [[kadernota]] — voorjaarsnota met kaders voor de begroting

### Financiële kengetallen
- [[solvabiliteitsratio]] — eigen vermogen / balanstotaal (schuldbelasting bezit)
- [[netto-schuldquote]] — netto schuld / baten (schuldhoogte)
- [[onbenutte-belastingcapaciteit]] — ruimte tot art. 12-tarief (brug naar belastingdomein)

## Bedrijfsobjecten

| Begrip | Status | GGM-grondslag | Matchsterkte |
|---|---|---|---|
| [[begroting]] | ✅ BO | Begroting (Financien) | exact |
| [[kostenplaats]] | ✅ BO | Kostenplaats (Financien) | exact |
| [[factuur]] | ✅ BO | Factuur (Financien) | exact |
| [[inkooporder]] | ✅ BO | Inkooporder (Financien) | exact |
| [[debiteur]] | ✅ BO | Debiteur (Financien) | exact |
| [[taakveld]] | ✅ BO | Taakveld (IV3) | exact |
| [[doelstelling]] | ✅ BO | Doelstelling (Financien) | exact |
| [[product]] | ✅ BO | Product (Financien) | exact |
| [[activa]] | ✅ BO | Activa (Financien) | sterk |
| [[werkorder]] | ✅ BO | Werkorder (Financien) | exact |

## GGM-dekkingsanalyse

Het GGM modelleert beleidsdomein Financien onder taakveld 9 (Interne Organisatie) met 24 entiteiten.

| GGM-domein | Entiteiten | Status |
|---|---|---|
| **Taakveld 9 Interne Organisatie / Financien** | Begroting, Kostenplaats, Factuur, Inkooporder, Debiteur, Taakveld, Doelstelling, Product, Activa, Werkorder (24 entiteiten totaal) | 10 → BO (boekhoudkundige kern is goed gedekt) |

**Hiaten in GGM:**
- De begrotingscyclus als proces (kadernota → begroting → tussenrapportage → jaarrekening)
- Financiële kengetallen als afgeleide informatie (solvabiliteitsratio, netto-schuldquote)
- De inkomstenbronstructuur (gemeentefonds, specifieke uitkering)

## Verwerkte bronnen

- [[Sources/Onderwerpen VNG/Financien/raadgever-inkomstenbronnen-gemeenten]] — VNG Raadgever: vier inkomstenbronnen van gemeenten
- [[Sources/Onderwerpen VNG/Financien/raadgever-gemeentebegroting-en-jaarrekening]] — VNG Raadgever: begrotingscyclus, budgetrecht, BBV
- [[Sources/Onderwerpen VNG/Financien/raadgever-financiele-verordening]] — VNG Raadgever: art. 212, spelregels financieel beleid
- [[Sources/Onderwerpen VNG/Financien/raadgever-financiele-conditie-gemeente]] — VNG Raadgever: balans, kengetallen, financiële gezondheid

## Raakvlakken

- **Belastingen** — gemeentelijke belastingen zijn een van de vier inkomstenbronnen; [[onbenutte-belastingcapaciteit]] koppelt de domeinen
- **Dienstverlening** — inkoop en aanbesteding zijn de uitgavenkant van de begroting
