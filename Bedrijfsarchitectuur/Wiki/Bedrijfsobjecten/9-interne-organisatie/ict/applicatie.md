---
type: element
naam: Applicatie
onderwerp: [Informatiesamenleving]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Applicatie
ggm_guid: EAID_A8945FD7_EA20_418e_8E7F_18F13F16E338
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items, Basismodel ICT Applicatie en Gegevens, Financien Verwerken Mutaties]
ggm_diagram_ids: [EAID_4F14E8D8_5502_4880_9E83_D912BE451EB1, EAID_A2831A97_91F6_4ed0_896E_3531219E69F0, EAID_B758018F_CB22_420e_B4E4_E17EB5F71EDA]
ggm_definitie: "Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Applicatie
ggm_gemma_guid: "f5c91145-fba4-47cb-aaf9-bb9c64e19a21"
ggm_gemma_definitie: "Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-f5c91145-fba4-47cb-aaf9-bb9c64e19a21"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Applicatie** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Attribuutsoort** (detail) — Detailgegeven
  - **Batch** (detail) — Detailgegeven (geassocieerd met BO)
  - **Classificatie** (detail) — Detailgegeven (weinig attributen)
  - **Externe Bron** (detail) — Detailgegeven (weinig attributen)
  - **ExterneBron** (detail) — Detailgegeven (weinig attributen)
  - **Gegeven** (detail) — Detailgegeven (geassocieerd met BO)
  - **Generalisatie** (detail) — Detailgegeven
  - **Linkbaar CMDB-item** (detail) — Detailgegeven (geassocieerd met BO)
  - **Notitie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Objecttype** (detail) — Detailgegeven
  - **Package** (detail) — Detailgegeven (geassocieerd met BO)
  - **Relatiesoort** (detail) — Detailgegeven
  - **Versie** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract|Contract]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Applicatie wordt geleverd onder een contract (GIBIT, SaaS-overeenkomst)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier|Leverancier]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Applicatie wordt geleverd en beheerd door een leverancier"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit|Verwerkingsactiviteit]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Applicatie verwerkt persoonsgegevens conform verwerkingsregister"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/koppeling|Koppeling]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Applicatie is verbonden met andere systemen via koppelingen"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database|Database]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Applicatie gebruikt een of meer databases"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server|Server]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Applicatie draait op een server (on-premises)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/licentie|Licentie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Applicatie wordt gebruikt op basis van licenties"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/sla|Service Level Agreement]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "SLA beschrijft het onderhoudsniveau voor de applicatie"
bedrijfsprocessen: [Applicatiebeheer, Leveranciersmanagement, ICT-projectmanagement]
bedrijfsfuncties: [Informatievoorziening, ICT-beheer]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Softwaretoepassing die bedrijfsprocessen ondersteunt; kerncomponent informatievoorziening |
| Herkenbaarheid | Elke medewerker kent "het zaaksysteem", "de BAG-applicatie", "het financieel systeem" |
| Eigen bestaan | 8 attributen in GGM (naam, categorie, beheerstatus, URL, etc.); eigen CMDB-item |
| Meervoud | Gemeente Nunspeet beheert circa 250 applicaties |
| Levenscyclus | Selectie → aanschaf → implementatie → onderhoud → uitfasering |
| Relaties | Versie, Koppeling, Database, Gegeven, Contract, Leverancier |

Resultaat: 6/6 — BO.

## Beschrijving

Een applicatie is een softwaretoepassing die de gemeente inzet om eindgebruikers te ondersteunen in hun werkprocessen. Gemeenten beheren doorgaans honderden applicaties, van het zaaksysteem en de BAG-applicatie tot het financieel pakket en de samenwerkingsomgeving. Elke applicatie heeft een eigen beheerstatus, versiehistorie en koppelingen met andere systemen.

Het GGM plaatst Applicatie in de CMDB-hiërarchie: CMDB-item → Linkbaar CMDB-item → Applicatie. Siblings zijn Database en Server. Deze drie vormen de kern van het gemeentelijk applicatielandschap.

De trend naar SaaS en Common Ground verandert het beheermodel: technisch beheer verschuift naar de leverancier, contractbeheer en regierol worden belangrijker. Contracten worden afgesloten onder GIBIT-voorwaarden (Gemeentelijke Inkoopvoorwaarden bij IT) en bevatten standaard een verwerkersovereenkomst (VWO) voor persoonsgegevens.

## GGM-bron

> "Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers."
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Applicatie | Matchsterkte: **exact** | Attributen: naam, categorie, beheerstatus, packagingstatus, applicatieURL, guid, omschrijving, beleidsdomein

## GGM-componenten

GGM-entiteiten die onderdeel zijn van het applicatiebeheer. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Versie** — versie-aanduiding met versienummer, status, datumEindeSupport, licentie, aantal, kosten
- **Package** — samengesteld bestand of directory; gekoppeld aan een project
- **Log** — registratie van gegevens met tijd en omschrijving

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract\|Contract]] | naar-dit-BO | Applicatie wordt geleverd onder een contract (GIBIT, SaaS) |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | naar-dit-BO | Applicatie wordt geleverd en beheerd door een leverancier |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit\|Verwerkingsactiviteit]] | van-dit-BO | Applicatie verwerkt persoonsgegevens conform verwerkingsregister |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/koppeling\|Koppeling]] | van-dit-BO | Applicatie is verbonden met andere systemen via koppelingen |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database\|Database]] | van-dit-BO | Applicatie gebruikt een of meer databases |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] | naar-dit-BO | Applicatie draait op een server (on-premises) |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/licentie\|Licentie]] | van-dit-BO | Applicatie wordt gebruikt op basis van licenties |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/sla\|Service Level Agreement]] | van-dit-BO | SLA beschrijft het onderhoudsniveau voor de applicatie |

## Bedrijfsprocessen

- **Applicatiebeheer** — functioneel en technisch beheer, updates, patches
- **Leveranciersmanagement** — contractbeheer, SLA-monitoring, regierol
- **ICT-projectmanagement** — selectie, implementatie, migratie, uitfasering

## Bedrijfsfuncties

- **Informatievoorziening** — applicatielandschap als kern van gemeentelijke IV
- **ICT-beheer** — technisch beheer, CMDB, koppelingen

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/informatiebeleidsplan-nunspeet|Informatiebeleidsplan 2024-2028 Gemeente Nunspeet]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/beleid-informatie-ict-bel-combinatie|Beleid Informatie en ICT 2020-2024 BEL Combinatie]]
