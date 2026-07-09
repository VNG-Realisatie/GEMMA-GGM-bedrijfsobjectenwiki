---
type: element
naam: SociaalTeamDossier
onderwerp:
- maatschappelijke ondersteuning
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: SociaalTeamDossier
ggm_guid: EAID_A22B8038_3C04_44a7_8E75_90A3A5E2615B
ggm_uml_type: Class
ggm_beleidsdomein: Sociale Teams
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Sociale team:Domeinmodel
ggm_diagram_ids:
- EAID_50F1F1BC_5866_45b9_A062_4C41F0C7766C
ggm_definitie: SociaalTeamDossier is een dossier-entiteit die de geïntegreerde registratie van gegevens over ondersteuning, gesprekken, interventies en casusontwikkeling van een sociaal team voor een inwoner
  of gezin omvat.
ggm_toelichting: In het Model Sociale Teams van het gemeentelijke gegevenslandschap representeert SociaalTeamDossier de centrale registratie van alle relevante informatie rondom een casus die door een sociaal
  team wordt behandeld.
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
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **SociaalTeamDossier** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Behandelsoort** (classificatie) — Typering/referentietabel
  - **Bijzonderheid** (detail) — Detailgegeven (geassocieerd met BO)
  - **Bijzonderheidsoort** (classificatie) — Typering/referentietabel
  - **SociaalteamDossiersoort** (classificatie) — Typering/referentietabel
bo_definitie: "SociaalTeamDossier is een dossier-entiteit die de geïntegreerde registratie van gegevens over ondersteuning, gesprekken, interventies en casusontwikkeling van een sociaal team voor een inwoner of gezin omvat."
bo_toelichting:
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
  richting: naar-dit-BO
  kardinaliteit: "1"
  beschrijving: behoort bij een cliënt
- type: associatie
  bedrijfsobject: "Clientbegeleider"
  richting: naar-dit-BO
  kardinaliteit: "1"
  beschrijving: wordt beheerd door een cliëntbegeleider
- type: associatie
  bedrijfsobject: "Behandeling"
  richting: van-dit-BO
  kardinaliteit: "0..*"
  beschrijving: bevat behandeling(en)
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling|Doelstelling]]"
  richting: van-dit-BO
  kardinaliteit: "0..*"
  beschrijving: heeft doelstelling(en)
- type: associatie
  bedrijfsobject: "SociaalteamDossiersoort"
  richting: van-dit-BO
  kardinaliteit: "1"
  beschrijving: is van een bepaald dossiersoort
bedrijfsprocessen:
- casusregistratie sociaal team
- ondersteuningsplan opstellen
- voortgang monitoren
bedrijfsfuncties:
- sociaal team
- wijkteam
---

# SociaalTeamDossier

Dossier van een sociaal team (buurtteam) met de geïntegreerde registratie van ondersteuning, interventies en casusontwikkeling voor een inwoner of gezin.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | Het sociaal team registreert per casus een dossier met start- en einddatum, status en omschrijving |
| Meervoud | Honderden tot duizenden actieve dossiers per gemeente |
| Levenscyclus | Aangemaakt → actief → vastgesteld → afgesloten |
| Eigendom | Het sociaal team beheert het dossier namens de gemeente |
| Gemeentelijk belang | Kern van de wijkgerichte ondersteuning; wordt gerapporteerd in beleidsinformatie |
| Bronnen | Beleidsnota Jeugd Utrecht |

## Beschrijving

Het SociaalTeamDossier is de centrale registratie van een casus die door een sociaal team (buurtteam, wijkteam) wordt behandeld. In gemeenten als Utrecht werken buurtteams als eerste lijn: zij voeren gesprekken met inwoners, stellen ondersteuningsplannen op en coördineren interventies. Het dossier bundelt alle gegevens over de ondersteuning, de betrokken behandelingen en de afgesproken doelstellingen.

Elk dossier hoort bij precies een cliënt en wordt beheerd door een cliëntbegeleider. De dossiersoort (via SociaalteamDossiersoort) classificeert het type ondersteuningsvraag.

## GGM-bron

> SociaalTeamDossier is een dossier-entiteit die de geïntegreerde registratie van gegevens over ondersteuning, gesprekken, interventies en casusontwikkeling van een sociaal team voor een inwoner of gezin omvat.

- **Entiteit:** SociaalTeamDossier
- **Beleidsdomein:** Sociale Teams (taakveld 6 — Sociaal Domein)
- **Attributen:** datumStart, omschrijving, datumEinde, status, datumVaststelling
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Richting | Kardinaliteit |
|---|---|---|---|
| Behoort bij cliënt | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 |
| Beheerd door begeleider | Clientbegeleider | ← | 1 |
| Bevat behandeling(en) | Behandeling | → | 0..* |
| Heeft doelstelling(en) | Doelstelling | → | 0..* |
| Is van dossiersoort | SociaalteamDossiersoort | → | 1 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
