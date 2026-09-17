---
type: element
naam: Database
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Database
ggm_guid: EAID_FFD22E11_7A3A_459a_B575_928C67E8D1F3
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items]
ggm_diagram_ids: [EAID_4F14E8D8_5502_4880_9E83_D912BE451EB1]
ggm_definitie: "Een applicatiecomponent die een dataset bevat."
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

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Database** als directe tegenhanger.
bo_definitie: "Applicatiecomponent die een gestructureerde dataset bevat."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server|Server]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Database draait op een server"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Database wordt gebruikt door applicaties"
bedrijfsprocessen: [Databasebeheer, Gegevensbeheer, Back-up en recovery]
bedrijfsfuncties: [ICT-beheer, Informatievoorziening]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Opslagcomponent voor gestructureerde data; basis van informatiesystemen |
| Herkenbaarheid | "de Oracle-database", "de SQL-database", "de productiedatabase" |
| Eigen bestaan | 7 attributen in GGM (databaseInstantie, omschrijving, DBMS, architectuur, OTAP, databaseVersie, vlan) |
| Meervoud | Tientallen per gemeente |
| Levenscyclus | Installeren → vullen → onderhouden → migreren → decommissioning |
| Relaties | Server, Applicatie, Koppeling |

Resultaat: 6/6 — BO.

## Beschrijving

Een database is een applicatiecomponent die een gestructureerde dataset bevat. In het GGM is Database een subtype van Linkbaar CMDB-item, naast [[Applicatie]] en [[Server]]. Een database draait op een [[Server]] en wordt gebruikt door een of meer [[Applicatie|applicaties]].

Gemeenten beheren tientallen databases met verschillende DBMS'en (Oracle, SQL Server, PostgreSQL). Elke database heeft een eigen OTAP-status (Ontwikkeling, Test, Acceptatie, Productie), versie en back-upregime.

## GGM-bron

> "Een applicatiecomponent die een dataset bevat."
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Database | Matchsterkte: **exact** | Attributen: databaseInstantie, omschrijving, DBMS, architectuur, OTAP, databaseVersie, vlan

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] | naar-dit-BO | Database draait op een server |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | Database wordt gebruikt door applicaties |

## Bedrijfsprocessen

- **Databasebeheer** — installatie, tuning, patching
- **Gegevensbeheer** — datakwaliteit, integriteit, migratie
- **Back-up en recovery** — back-upregime, hersteltests

## Bedrijfsfuncties

- **ICT-beheer** — technisch databasebeheer
- **Informatievoorziening** — databases als drager van gemeentelijke informatie

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer]]
- [[Wiki/Bronsamenvattingen/Informatiesystemen/gibit-2025]]
