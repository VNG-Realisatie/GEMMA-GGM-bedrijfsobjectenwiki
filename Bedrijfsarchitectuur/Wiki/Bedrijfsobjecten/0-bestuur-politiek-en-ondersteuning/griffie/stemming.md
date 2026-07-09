---
type: element
naam: Stemming
onderwerp: [bestuur]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Stemming
ggm_guid: EAID_331C4A0B_1505_4945_A0B0_DCD8703AB50F
ggm_uml_type: Class
ggm_beleidsdomein: Griffie
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_diagram:
  - Diagram Griffie
ggm_diagram_ids:
  - EAID_A9F0B77B_05F3_4c36_96A0_8841BBAE47E0
ggm_definitie: "Stem (openbaring van iemands mening (voor of tegen)), uitbrengen bij verkiezingen of bij een vergadering"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM

ggm_gemma_naam: Stemming
ggm_gemma_guid: "857327b0-3ab3-4578-869d-7b390aa1e3d3"
ggm_gemma_definitie: "Stem (openbaring van iemands mening (voor of tegen)), uitbrengen bij verkiezingen of bij een vergadering"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-857327b0-3ab3-4578-869d-7b390aa1e3d3"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Stemming** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Agendapunt** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Stem (openbaring van iemands mening (voor of tegen)), uitbrengen bij verkiezingen of bij een vergadering"
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Raadsstuk]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "stemming betreft raadsstuk"
  - type: associatie
    bedrijfsobject: "[[Vergadering]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "stemming vindt plaats in vergadering (via agendapunt)"
bedrijfsprocessen:
  - Raadsbesluitvorming
bedrijfsfuncties:
  - Griffie
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Identificeerbaar | ✅ Elke stemming heeft resultaat en stemmingstype |
| Levenscyclus | ✅ Aankondiging → stemronde → telling → uitslag → registratie |
| Eigenschap-dragend | ✅ resultaat, stemmingstype |
| Relaties | ✅ Naar agendapunt en raadsstuk |
| Bedrijfsrelevantie | ✅ Formeel besluitvormingsmoment; registratie van democratische beslissingen |
| Gemeentelijk | ✅ Gemeentewet art. 27-32: stemregels, meerderheid, geheime stemming |

Score: **6/6**

## Beschrijving

Een stemming is het formele moment waarop de gemeenteraad een besluit neemt over een raadsstuk of agendapunt. De Gemeentewet onderscheidt twee vormen:

- **Hoofdelijke stemming** (art. 32) — bij mondelinge oproeping; onthouding niet mogelijk; absoluut meerderheidsvereiste (art. 30)
- **Geheime stemming** (art. 31) — bij personenverkiezingen; bij staking hersteming, bij hernieuwde staking loting

Raadsleden stemmen zonder last van kiezers (art. 27). Een raadslid dat persoonlijk betrokken is, onthoudt zich van deelneming (art. 28). De stemming is geldig bij deelneming van meer dan de helft van de niet-ontheven leden (art. 29).

Bij staking van stemmen in een niet-voltallige vergadering wordt het voorstel aangehouden; in een voltallige vergadering is het voorstel verworpen (art. 32).

## GGM-bron

> "Stem (openbaring van iemands mening (voor of tegen)), uitbrengen bij verkiezingen of bij een vergadering"
> — GGM, beleidsdomein Griffie, taakveld 0

**Entiteit:** Stemming
**Attributen:** resultaat, stemmingstype
**Matchsterkte:** exact — 1:1 mapping

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/raadsstuk\|Raadsstuk]] | associatie | van-dit-BO | 1 | stemming betreft raadsstuk | GGM |
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/vergadering\|Vergadering]] | associatie | naar-dit-BO | 0..* | stemming vindt plaats in vergadering (via agendapunt) | GGM |

## Bedrijfsprocessen

- **Raadsbesluitvorming** — stemming is het besluitvormingsmoment

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst]]
