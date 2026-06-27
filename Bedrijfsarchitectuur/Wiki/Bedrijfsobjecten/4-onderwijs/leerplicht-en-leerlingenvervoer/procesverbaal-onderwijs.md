---
type: bedrijfsobject
naam: Procesverbaal Onderwijs
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Procesverbaal Onderwijs
ggm_guid: EAID_697F1730_B439_4b35_8799_1B2E9AB04548
ggm_uml_type: Class
ggm_beleidsdomein: Leerplicht en Leerlingenvervoer
ggm_taakveld: "4 Onderwijs"
ggm_diagram: [Diagram Beslissingen Leerplicht]
ggm_diagram_ids: [EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308]
ggm_definitie: "Een officieel document dat een overtreding van de leerplichtwet vastlegt."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: ProcesverbaalOnderwijs
ggm_gemma_guid: aa2cb2d9-8482-473c-a5bf-c042cb39352a
ggm_gemma_definitie: "Een officieel document dat een overtreding van de leerplichtwet vastlegt."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-aa2cb2d9-8482-473c-a5bf-c042cb39352a
ggm_gemma_bron:
ggm_gemma_alternate_name:

bo_definitie: "Een officieel document dat een overtreding van de leerplichtwet vastlegt."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Procesverbaal betreft leerling"
bedrijfsprocessen: [Leerplichthandhaving]
bedrijfsfuncties: [Leerplicht]
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Juridisch instrument voor handhaving van de leerplichtwet |
| Herkenbaar voor domeinexperts | ✅ Leerplichtambtenaren maken processen-verbaal op bij overtredingen |
| Heeft eigen bestaan | ✅ Officieel document met eigen kenmerken (reden, sanctie, uitspraak) |
| Kan in meervoud bestaan | ✅ Meerdere processen-verbaal per gemeente per jaar |
| Heeft eigen levenscyclus | ✅ Opmaken → inlichten → zitting → uitspraak → afhandeling |
| Heeft relaties met andere concepten | ✅ Leerling, ouder/verzorger, leerplichtambtenaar |

**6/6 criteria van toepassing.**

## Beschrijving

Een procesverbaal onderwijs is een officieel document waarmee de leerplichtambtenaar een overtreding van de Leerplichtwet vastlegt. Het procesverbaal wordt opgemaakt wanneer een ouder of verzorger niet voldoet aan de verplichtingen uit de leerplichtwet, bijvoorbeeld bij langdurig ongeoorloofd verzuim. Na het opmaken volgt een zitting bij de rechter, die kan leiden tot een geldboete of een proeftijd.

## GGM-bron

> "Een officieel document dat een overtreding van de leerplichtwet vastlegt."
> — GGM-entiteit: Procesverbaal Onderwijs, beleidsdomein: Leerplicht en Leerlingenvervoer

**Matchsterkte: exact.** De GGM-entiteit beschrijft hetzelfde concept.

**GGM-attributen:** reden, opmerkingen, datumIngelicht, sanctiesoort, uitspraak, proeftijd, geldboete, verzuimsoort, datumZitting, datumAfgehandeld, datumUitspraak, datumEindeProeftijd, geldboeteVoorwaardelijk.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Leerling]] | associatie | ← | 1 | GGM |

**GGM-relaties zonder BO-equivalent:**
- Ouder Of Verzorger — procesverbaal wordt opgemaakt tegen de ouder/verzorger
- Leerplichtambtenaar — ambtenaar die het procesverbaal opmaakt

## Bedrijfsprocessen

- **Leerplichthandhaving** — opmaken procesverbaal bij overtreding leerplichtwet, opvolging zitting en uitspraak

## Bedrijfsfuncties

- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/beleidsnota-onderwijshuisvesting-utrecht]]
- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
