---
type: element
naam: Verlof
onderwerp: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Verlof
ggm_guid: EAID_D04135BF_C2F0_46dd_B332_F1BE36C358EF
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53]
ggm_definitie: "Een periode waarin iemand toestemming heeft om iets te doen, in het bijzonder om afwezig te zijn."
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

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Verlof** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Verlofsoort** (classificatie) — Typering/referentietabel
bo_definitie: "Een periode waarin iemand toestemming heeft om iets te doen, in het bijzonder om afwezig te zijn."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Werknemer heeft verlof"
bedrijfsprocessen: [Verlofregistratie, Personeelsadministratie]
bedrijfsfuncties: [Personeelsbeheer]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Standaardproces in elke gemeente |
| Herkenbaar voor domeinexperts | ✅ Iedereen kent verlofaanvragen |
| Heeft eigen bestaan binnen het domein | ✅ Elk verlof is een afzonderlijk record |
| Kan in meervoud bestaan | ✅ Duizenden per jaar per gemeente |
| Heeft eigen levenscyclus | ✅ Aanvraag → goedkeuring → opname |
| Heeft relaties met andere concepten | ✅ Werknemer, Verlofsoort |

Score: **6/6**

## Beschrijving

Verlof is een goedgekeurde periode van afwezigheid van een werknemer. Verlofsoorten (vakantie, bijzonder verlof, ouderschapsverlof, etc.) worden als enumeratie vastgelegd via Verlofsoort in het GGM, niet als aparte BO's.

## GGM-bron

> "Een periode waarin iemand toestemming heeft om iets te doen, in het bijzonder om afwezig te zijn."

- **Entiteit:** Verlof
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datumtijdStart, datumtijdEinde, goedgekeurd, datumAanvraag, datumToekenning
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Werknemer]] heeft verlof | naar dit BO | 1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsvoorwaarden]]
