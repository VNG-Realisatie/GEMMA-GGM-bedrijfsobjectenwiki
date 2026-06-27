---
type: bedrijfsobject
naam: Disciplinaire Maatregel
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Disciplinaire Maatregel
ggm_guid: EAID_50F3F931_38F4_4ff0_8CE4_8A51056767E0
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53]
ggm_definitie: "Een besluit dat wordt opgelegd wanneer een persoon zijn verplichtingen niet of niet op de juiste wijze nakomt, of zich op andere wijze misdraagt."
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

bo_definitie: "Formeel besluit van de werkgever jegens een werknemer bij plichtsverzuim of wangedrag."
bo_subtypes:
  - naam: Schriftelijke waarschuwing
    omschrijving: "Formele waarschuwing of berisping"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Schorsing
    omschrijving: "Tijdelijke non-actiefstelling"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Inhouding periodieke verhoging
    omschrijving: "Geen schaalverhoging als sanctie"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Ontslag
    omschrijving: "Beëindiging dienstverband als zwaarste maatregel"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Werknemer heeft disciplinaire maatregel"
bedrijfsprocessen: [Integriteitshandhaving, Personeelsbeheer]
bedrijfsfuncties: [Personeelsbeheer, Juridische zaken]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Formeel arbeidsrechtelijk instrument |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip in HR en juridisch |
| Heeft eigen bestaan binnen het domein | ✅ Elk besluit is een zelfstandig record |
| Kan in meervoud bestaan | ✅ Meerdere per gemeente per jaar |
| Heeft eigen levenscyclus | ✅ Geconstateerd → opgelegd → afgehandeld |
| Heeft relaties met andere concepten | ✅ Werknemer, SoortDisciplinaireMaatregel |

Score: **6/6**

## Beschrijving

Een disciplinaire maatregel is het formele besluit dat de werkgever oplegt wanneer een werknemer zijn verplichtingen niet nakomt of zich misdraagt. Sinds de normalisering (Wnra, 2020) valt dit onder het private arbeidsrecht, maar de Ambtenarenwet 2017 stelt bijzondere eisen aan de integriteit van ambtenaren. De maatregel wordt vastgelegd met datum constatering, datum oplegging, reden en omschrijving.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Schriftelijke waarschuwing | Formele waarschuwing of berisping | — |
| Schorsing | Tijdelijke non-actiefstelling | — |
| Inhouding periodieke verhoging | Geen schaalverhoging als sanctie | — |
| Ontslag | Beëindiging dienstverband als zwaarste maatregel | — |

Soorten worden in het GGM vastgelegd via enumeratie SoortDisciplinaireMaatregel.

## GGM-bron

> "Een besluit dat wordt opgelegd wanneer een persoon zijn verplichtingen niet of niet op de juiste wijze nakomt, of zich op andere wijze misdraagt."

- **Entiteit:** Disciplinaire Maatregel
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datumGeconstateerd, datumOpgelegd, omschrijving, reden
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Werknemer]] heeft disciplinaire maatregel | naar dit BO | 1 | GGM |


## Subtypes

- **Schriftelijke waarschuwing** — Formele waarschuwing of berisping
- **Schorsing** — Tijdelijke non-actiefstelling
- **Inhouding periodieke verhoging** — Geen schaalverhoging als sanctie
- **Ontslag** — Beëindiging dienstverband als zwaarste maatregel

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/integriteit]]
