---
type: element
naam: Licentie
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Licentie
ggm_guid: EAID_2E5F9AF9_D1BA_4dc0_9621_4101D24B8ABD
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items Diversen]
ggm_diagram_ids: [EAID_A255BB0C_A1DB_43a5_88B1_C638F6E64B0B]
ggm_definitie: "Een gebruiksrecht en autorisatie om van een product of dienst gebruik te maken binnen bepaalde voorwaarden"
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
  Dit BO heeft de GGM-entiteit **Licentie** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **CMDB-item** (detail) — Detailgegeven (weinig attributen)
  - **Inventaris** (detail) — Detailgegeven (weinig attributen)
  - **Log** (detail) — Detailgegeven (weinig attributen)
  - **Toegangsmiddel** (detail) — Detailgegeven (weinig attributen)
  - **Vervoersmiddel** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Gebruiksrecht op grond waarvan de gemeente bevoegd is een ICT-product of -dienst te gebruiken binnen overeengekomen voorwaarden."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Applicatie wordt gebruikt op basis van een of meer licenties"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/software|Software]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Software wordt gebruikt op basis van licenties"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract|Contract]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Licentie is onderdeel van een IT-contract"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier|Leverancier]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Licentie wordt verstrekt door een leverancier"
bedrijfsprocessen: [Licentiebeheer, Applicatiebeheer, Leveranciersmanagement]
bedrijfsfuncties: [Informatievoorziening, ICT-beheer, Inkoop]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Gebruiksrecht op ICT-producten; financieel en juridisch relevant |
| Herkenbaarheid | "Office-licenties", "Oracle-licentie", "per-user licentie" |
| Eigen bestaan | Subtype van CMDB-item; GIBIT definieert apart; eigen contractuele en financiële kenmerken |
| Meervoud | Honderden tot duizenden per gemeente |
| Levenscyclus | Aankoop → activering → gebruik → verlenging/opzegging → beëindiging |
| Relaties | Applicatie, Software, Contract, Leverancier |

Resultaat: 6/6 — BO.

## Beschrijving

Een licentie is het gebruiksrecht waarmee de gemeente bevoegd is een ICT-product of -dienst te gebruiken. Licenties hebben eigen financiële kenmerken (kosten, looptijd, verlengingsmomenten) en juridische voorwaarden (aantal gebruikers, verwerkingsbeperkingen).

De GIBIT 2025 definieert een licentie als "het gebruiksrecht op grond waarvan Opdrachtgever bevoegd is tot het gebruik van de ICT Prestatie binnen de kaders als gesteld in de Overeenkomst". Gemeenten beheren honderden licenties met verschillende modellen: per gebruiker, per installatie, site-licentie, of SaaS-abonnement.

Het GGM plaatst Licentie als subtype van CMDB-item. Licentie relateert aan [[Applicatie]] en [[Software]] (wat mag worden gebruikt) en aan [[Contract]] en [[Leverancier]] (onder welke voorwaarden).

## GGM-bron

> "Een gebruiksrecht en autorisatie om van een product of dienst gebruik te maken binnen bepaalde voorwaarden"
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Licentie | Matchsterkte: **exact** | Attributen: *(geen in GGM)*

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | Applicatie wordt gebruikt op basis van licenties |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/software\|Software]] | naar-dit-BO | Software wordt gebruikt op basis van licenties |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract\|Contract]] | naar-dit-BO | Licentie is onderdeel van een IT-contract |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | naar-dit-BO | Licentie wordt verstrekt door een leverancier |

## Bedrijfsprocessen

- **Licentiebeheer** — bijhouden van aantallen, verlengingen, compliance
- **Applicatiebeheer** — licenties als voorwaarde voor applicatiegebruik
- **Leveranciersmanagement** — contractuele afspraken over licentievoorwaarden

## Bedrijfsfuncties

- **Informatievoorziening** — licenties als randvoorwaarde voor de informatiehuishouding
- **ICT-beheer** — technisch licentiebeheer (activering, toewijzing)
- **Inkoop** — licentie-inkoop en -verlenging

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/gibit-2025|GIBIT 2025]]
- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer|CMDB & Informatiebeheerplan]]
