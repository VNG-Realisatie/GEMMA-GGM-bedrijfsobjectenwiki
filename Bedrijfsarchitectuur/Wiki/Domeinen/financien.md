---
type: domein
naam: Financien
status: in-behandeling
verwerkingsdatum: 2026-06-19
bronnen_count: 4
begrippen_count: 20
bo_count: 10
---

# Domein: Financiën

Gemeentelijke financiën — inkomstenbronnen, begrotingscyclus, financieel beheer en financiële gezondheid.

## Begrippen

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|gemeentefonds|instrument|Grootste inkomstenbron, vrij besteedbaar| ❌ | nee |Instrument, geen object|—|nee|
|algemene uitkering|instrument|Hoofdcomponent gemeentefonds| ❌ | nee |Instrument, geen object|—|nee|
|specifieke uitkering|instrument|Geoormerkt geld van het rijk voor medebewindstaken| ❌ | nee |Instrument, geen object|—|nee|
|begrotingscyclus|thema|Kadernota → begroting → tussenrapportages → jaarrekening| ❌ | nee |Proces, geen object|—|nee|
|budgetrecht|instrument|Raadsbevoegdheid om geld beschikbaar te stellen| ❌ | nee |Instrument, geen object|—|nee|
|financiële verordening|instrument|Art. 212 Gemeentewet, lokale spelregels financieel beleid| ❌ | nee |Instrument, geen object|—|nee|
|kadernota|object|Voorjaarsnota met kaders voor de begroting| ❌ | ja |Procesobject, beperkte levenscyclus|Kadernota 2026|nee|
|solvabiliteitsratio|object|Eigen vermogen / balanstotaal| ❌ | ja |Kengetal, afgeleid gegeven|—|nee|
|netto-schuldquote|object|Netto schuld / baten| ❌ | ja |Kengetal, afgeleid gegeven|—|nee|
|onbenutte belastingcapaciteit|object|Ruimte tot art. 12-tarief| ❌ | ja |Kengetal, afgeleid gegeven|—|nee|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]]|object|Overzicht verwachte ontvangsten en voorziene uitgaven| ✅ | ja |6/6 criteria, GGM exact|Programmabegroting 2026|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]]|object|Rekening waaraan boekingen worden toegeschreven| ✅ | ja |6/6 criteria, GGM exact|Afdeling, project|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/factuur\|Factuur]]|object|Schriftelijke rekening voor geleverde zaken of diensten| ✅ | ja |6/6 criteria, GGM exact|Inkoopfactuur, verkoopfactuur|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder\|Inkooporder]]|object|Opdracht voor levering van goederen en/of diensten| ✅ | ja |6/6 criteria, GGM exact|Bestelling materiaal|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur\|Debiteur]]|object|Persoon die een bedrag verschuldigd is aan de gemeente| ✅ | ja |6/6 criteria, GGM exact|Huurder, belastingplichtige|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/taakveld\|Taakveld]]|object|Samenhangend geheel van activiteiten en taken (IV3)| ✅ | ja |6/6 criteria, GGM exact|Taakveld 3 Economie|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling\|Doelstelling]]|object|Op korte of middellange termijn nagestreefde situatie| ✅ | ja |6/6 criteria, GGM exact|Begrotingsdoelstelling|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product\|Product]]|object|Resultaat van een proces dat in het economisch verkeer waarde bezit| ✅ | ja |6/6 criteria, GGM exact|Paspoort, bouwvergunning|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa\|Activa]]|object|Bezittingen op de boekhoudkundige balans| ✅ | ja |6/6 criteria, GGM sterk|Grond, gebouw, inventaris|ja|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/werkorder\|Werkorder]]|object|Opdracht voor uitvoering van een activiteit| ✅ | ja |6/6 criteria, GGM exact|Onderhoudsopdracht|ja|

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

- [Raadgever inkomstenbronnen gemeenten](../../Sources/Onderwerpen/Financien/raadgever-inkomstenbronnen-gemeenten.md) — VNG Raadgever: vier inkomstenbronnen van gemeenten
- [Raadgever gemeentebegroting en jaarrekening](../../Sources/Onderwerpen/Financien/raadgever-gemeentebegroting-en-jaarrekening.md) — VNG Raadgever: begrotingscyclus, budgetrecht, BBV
- [Raadgever financiele verordening](../../Sources/Onderwerpen/Financien/raadgever-financiele-verordening.md) — VNG Raadgever: art. 212, spelregels financieel beleid
- [Raadgever financiele conditie gemeente](../../Sources/Onderwerpen/Financien/raadgever-financiele-conditie-gemeente.md) — VNG Raadgever: balans, kengetallen, financiële gezondheid

## Raakvlakken

- **Belastingen** — gemeentelijke belastingen zijn een van de vier inkomstenbronnen; onbenutte belastingcapaciteit koppelt de domeinen
- **Dienstverlening** — inkoop en aanbesteding zijn de uitgavenkant van de begroting
