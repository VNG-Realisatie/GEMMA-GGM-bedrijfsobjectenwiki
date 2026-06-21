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

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| gemeentefonds | instrument | Grootste inkomstenbron, vrij besteedbaar | ❌ | Instrument, geen object | — | nee |
| algemene uitkering | instrument | Hoofdcomponent gemeentefonds | ❌ | Instrument, geen object | — | nee |
| specifieke uitkering | instrument | Geoormerkt geld van het rijk voor medebewindstaken | ❌ | Instrument, geen object | — | nee |
| begrotingscyclus | thema | Kadernota → begroting → tussenrapportages → jaarrekening | ❌ | Proces, geen object | — | nee |
| budgetrecht | instrument | Raadsbevoegdheid om geld beschikbaar te stellen | ❌ | Instrument, geen object | — | nee |
| financiële verordening | instrument | Art. 212 Gemeentewet, lokale spelregels financieel beleid | ❌ | Instrument, geen object | — | nee |
| kadernota | object | Voorjaarsnota met kaders voor de begroting | ❌ | Procesobject, beperkte levenscyclus | Kadernota 2026 | nee |
| solvabiliteitsratio | object | Eigen vermogen / balanstotaal | ❌ | Kengetal, afgeleid gegeven | — | nee |
| netto-schuldquote | object | Netto schuld / baten | ❌ | Kengetal, afgeleid gegeven | — | nee |
| onbenutte belastingcapaciteit | object | Ruimte tot art. 12-tarief | ❌ | Kengetal, afgeleid gegeven | — | nee |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting]] | object | Overzicht verwachte ontvangsten en voorziene uitgaven | ✅ | 6/6 criteria, GGM exact | Programmabegroting 2026 | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats]] | object | Rekening waaraan boekingen worden toegeschreven | ✅ | 6/6 criteria, GGM exact | Afdeling, project | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/factuur]] | object | Schriftelijke rekening voor geleverde zaken of diensten | ✅ | 6/6 criteria, GGM exact | Inkoopfactuur, verkoopfactuur | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder]] | object | Opdracht voor levering van goederen en/of diensten | ✅ | 6/6 criteria, GGM exact | Bestelling materiaal | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur]] | object | Persoon die een bedrag verschuldigd is aan de gemeente | ✅ | 6/6 criteria, GGM exact | Huurder, belastingplichtige | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/taakveld]] | object | Samenhangend geheel van activiteiten en taken (IV3) | ✅ | 6/6 criteria, GGM exact | Taakveld 3 Economie | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling]] | object | Op korte of middellange termijn nagestreefde situatie | ✅ | 6/6 criteria, GGM exact | Begrotingsdoelstelling | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product]] | object | Resultaat van een proces dat in het economisch verkeer waarde bezit | ✅ | 6/6 criteria, GGM exact | Paspoort, bouwvergunning | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa]] | object | Bezittingen op de boekhoudkundige balans | ✅ | 6/6 criteria, GGM sterk | Grond, gebouw, inventaris | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/werkorder]] | object | Opdracht voor uitvoering van een activiteit | ✅ | 6/6 criteria, GGM exact | Onderhoudsopdracht | ja |

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

- [[Sources/Onderwerpen/Financien/raadgever-inkomstenbronnen-gemeenten]] — VNG Raadgever: vier inkomstenbronnen van gemeenten
- [[Sources/Onderwerpen/Financien/raadgever-gemeentebegroting-en-jaarrekening]] — VNG Raadgever: begrotingscyclus, budgetrecht, BBV
- [[Sources/Onderwerpen/Financien/raadgever-financiele-verordening]] — VNG Raadgever: art. 212, spelregels financieel beleid
- [[Sources/Onderwerpen/Financien/raadgever-financiele-conditie-gemeente]] — VNG Raadgever: balans, kengetallen, financiële gezondheid

## Raakvlakken

- **Belastingen** — gemeentelijke belastingen zijn een van de vier inkomstenbronnen; onbenutte belastingcapaciteit koppelt de domeinen
- **Dienstverlening** — inkoop en aanbesteding zijn de uitgavenkant van de begroting
