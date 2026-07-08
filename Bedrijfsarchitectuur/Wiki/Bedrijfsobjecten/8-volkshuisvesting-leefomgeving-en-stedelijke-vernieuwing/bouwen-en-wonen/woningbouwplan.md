---
type: element
naam: Woningbouwplan
domein: [Wonen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Plan
ggm_guid: EAID_D857E285_1EA3_4ba3_9614_5FACAC8BA133
ggm_uml_type: Class
ggm_beleidsdomein: Bouwen en Wonen
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Woningbouwprojecten]
ggm_diagram_ids: [EAID_5B2022A2_1DAB_476d_BBCD_CD27F56F169F]
ggm_definitie: "Project waarin woningen worden gerealiseerd"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Plan
ggm_gemma_guid: e5933d4f-02b6-4851-a31e-8bc5b7cbaab6
ggm_gemma_definitie: "Project waarin woningen worden gerealiseerd"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-e5933d4f-02b6-4851-a31e-8bc5b7cbaab6"
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Plan**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Omgevingsvergunning** (detail) — Subtype van Vergunningen en ontheffingen
  - **Programma** (detail) — Component van Begroting
  - **Projectleider** (detail) — Detailgegeven (geassocieerd met BO)
  - **Projectontwikkelaar** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Project waarin woningen worden gerealiseerd"
bo_toelichting: ''
bo_subtypes:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Woning]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een woningbouwplan realiseert woningen"
bedrijfsprocessen: [Woningbouwprogrammering, Gebiedsontwikkeling]
bedrijfsfuncties: [Volkshuisvesting, Ruimtelijke ontwikkeling]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal in woningbouwprogrammering |
| Herkenbaar voor domeinexperts | ✅ |
| Heeft een eigen bestaan | ✅ Concreet plan met naam, nummer, fasering |
| Kan in meervoud bestaan | ✅ Tientallen plannen tegelijk in MPR |
| Heeft een eigen levenscyclus | ✅ Intentie → bestemming goedgekeurd → onherroepelijk → start bouw → oplevering |
| Heeft relaties met andere concepten | ✅ Woning, projectontwikkelaar, omgevingsvergunning |

Score: **6/6** — BO.

## Beschrijving

Een woningbouwplan is een project waarin woningen worden geprogrammeerd en gerealiseerd. De gemeente Utrecht streeft naar een bouwtempo van 3.000 woningen per jaar en monitort de plancapaciteit via het Meerjaren Perspectief Ruimte (MPR). Het streefpercentage is 75% betaalbare woningen in de nieuwbouw (40% sociale huur + 35% middensegment).

Plannen doorlopen het Utrechts Planproces Gebiedsontwikkeling (UPG): van intentiedocument via Nota van Uitgangspunten naar bestuurlijke vaststelling. De plancapaciteit onderscheidt harde (bestuurlijk vastgesteld) en zachte plannen.

## GGM-bron

> "Project waarin woningen worden gerealiseerd" — GGM-entiteit **Plan**, beleidsdomein Bouwen en Wonen

**Matchsterkte: exact.** De GGM-entiteit "Plan" komt direct overeen met het beleidsconcept.

**Attributen GGM:** naam, nummer, aardgasloos, gebiedstransformatie, intentie, bestemmingGoedgekeurd, onherroepelijk, eigendomGemeente, 70ProcentVerkocht, startVerkoop, startbouw, eersteOplevering, laatsteOplevering, percelen.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Realiseert [[Woning]]en | van Plan | 1..* | GGM (Plan → Gebouw) |

GGM-relaties: Omgevingsvergunning [0..*] → Plan [0..1], Programma [0..1] → Plan [0..*], Projectleider [0..1] → Plan [0..*], Projectontwikkelaar [1..*] → Plan [0..*].

## Bedrijfsprocessen

- **Woningbouwprogrammering** — Programmering, monitoring en rapportage van plancapaciteit via MPR
- **Gebiedsontwikkeling** — Ruimtelijke planontwikkeling via het UPG

## Bronnen

- [[Wiki/Bronsamenvattingen/Wonen/beleidsnota-wonen-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/huisvestingsverordening-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/nadere-regel-huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/beleidsregel-huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-betaalbare-koopwoningen]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-middenhuur]]
- [[Wiki/Bronsamenvattingen/Wonen/werkwijze-extra-woningen]]
- [[Wiki/Bronsamenvattingen/Wonen/woonboten-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/woonbotenbeleid-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Wonen/historische-schepen-utrecht-2015]]
