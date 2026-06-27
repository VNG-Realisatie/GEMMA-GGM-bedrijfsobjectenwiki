---
type: bedrijfsobject
naam: Verwerkersovereenkomst
onderwerp: [Informatiesamenleving]
archimate_type: contract
grondslag: governance-object

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

gemma_definitie: "Overeenkomst met een externe verwerker die namens de gemeente persoonsgegevens verwerkt, met verplichte bepalingen over doel, beveiliging en datalekmelding (art. 28 AVG)."
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit|Verwerkingsactiviteit]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Regelt welke verwerkingsactiviteiten de verwerker uitvoert"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia|DPIA]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Hoog-risicoverwerkingen bij verwerker vereisen een DPIA"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/datalek|Datalek]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Verwerker is verplicht datalekken zonder onredelijke vertraging te melden"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Bij SaaS-applicaties die persoonsgegevens verwerken is een verwerkersovereenkomst verplicht"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier|Leverancier]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Verwerker is een externe partij (leverancier)"
bedrijfsprocessen: [Privacy-compliance, Leveranciersmanagement, Contractbeheer]
bedrijfsfuncties: [Privacy, Informatievoorziening, Inkoop]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | AVG-verplichte overeenkomst bij uitbesteding persoonsgegevensverwerking (art. 28) |
| Herkenbaarheid | FG, CISO en inkoopmedewerkers kennen dit als standaard compliance-document |
| Eigen bestaan | Zelfstandig document met 8 verplichte bepalingen (art. 28 lid 3 AVG) |
| Meervoud | Per leverancier/verwerker apart; IBD publiceert standaardtemplate (VWO) |
| Levenscyclus | Opstellen → afsluiten → wijzigen (bij nieuwe verwerkingen) → beëindigen |
| Relaties | Verwerkingsactiviteit, DPIA, Datalek, Leverancier, Applicatie |

Resultaat: 6/6 — BO.

## Beschrijving

Een verwerkersovereenkomst is een overeenkomst tussen de gemeente als verwerkingsverantwoordelijke en een externe verwerker die namens de gemeente persoonsgegevens verwerkt. Art. 28 AVG verplicht dat deze overeenkomst schriftelijk wordt vastgelegd met minimaal 8 bepalingen over:

1. Verwerking uitsluitend op basis van gedocumenteerde instructies
2. Vertrouwelijkheidsplicht medewerkers
3. Passende technische en organisatorische beveiligingsmaatregelen
4. Voorwaarden voor inschakeling sub-verwerkers
5. Bijstand bij verzoeken van betrokkenen
6. Bijstand bij DPIA en voorafgaande raadpleging
7. Verwijdering of teruggave gegevens na beëindiging
8. Medewerking aan audits en inspecties

De IBD (Informatiebeveiligingsdienst voor gemeenten) publiceert de Standaard Verwerkersovereenkomst Gemeenten (VWO) als template. In de praktijk wordt de verwerkersovereenkomst afgesloten bij elk contract met een leverancier die persoonsgegevens verwerkt, met name bij SaaS-applicaties.

## Juridische bron

Wettelijke grondslag: art. 28 Verordening (EU) 2016/679 (AVG). De verwerkersovereenkomst is verplicht zodra een externe partij namens de gemeente persoonsgegevens verwerkt.

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/avg-verwerkingsregister-dpia|AVG art. 30, 35, 36]] voor verwante bepalingen.

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit\|Verwerkingsactiviteit]] | van-dit-BO | Regelt welke verwerkingsactiviteiten de verwerker uitvoert |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia\|DPIA]] | van-dit-BO | Hoog-risicoverwerkingen bij verwerker vereisen een DPIA |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/datalek\|Datalek]] | van-dit-BO | Verwerker moet datalekken zonder onredelijke vertraging melden |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | Bij SaaS-applicaties die persoonsgegevens verwerken is VWO verplicht |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | naar-dit-BO | Verwerker is een externe partij |

## Bedrijfsprocessen

- **Privacy-compliance** — afsluiten en onderhouden verwerkersovereenkomsten
- **Leveranciersmanagement** — toezicht op naleving door verwerker
- **Contractbeheer** — onderdeel van inkoopproces bij ICT-aanbestedingen

## Bedrijfsfuncties

- **Privacy** — FG bewaakt naleving verwerkersovereenkomsten
- **Informatievoorziening** — applicaties met persoonsgegevens vereisen VWO
- **Inkoop** — GIBIT-voorwaarden verwijzen naar VWO

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/informatiebeleidsplan-nunspeet|Informatiebeleidsplan 2024-2028 Gemeente Nunspeet]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/avg-verwerkingsregister-dpia|AVG art. 30, 35, 36]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-datalekken-ibd|Factsheet Datalekken IBD]]

## Terugmelding GGM

Verwerkersovereenkomst ontbreekt als entiteit in het GGM. Potentieel hiaat: het GGM modelleert het ICT-domein (Applicatie, Koppeling, etc.) maar niet de privacy-gerelateerde contractvormen die bij applicatiebeheer horen. Zou passen in beleidsdomein ICT of een nieuw beleidsdomein Privacy/AVG.

Teruggemeld als #82 in [[Wiki/Analyses/ggm-terugmeldingen]].
