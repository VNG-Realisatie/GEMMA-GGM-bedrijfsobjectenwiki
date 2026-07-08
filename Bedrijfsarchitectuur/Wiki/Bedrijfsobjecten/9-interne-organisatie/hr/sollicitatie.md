---
type: bedrijfsobject
naam: Sollicitatie
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Sollicitatie
ggm_guid: EAID_3BD1368C_23F1_4f42_99DB_C81581A646A0
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Sollicitaties]
ggm_diagram_ids: [EAID_542C38C9_B92F_48de_87F1_F90F64FB5913]
ggm_definitie: "Verzoek om in een functie te worden aangesteld."
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
  Dit BO heeft de GGM-entiteit **Sollicitatie** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Sollicitant** (detail) — Detailgegeven (geassocieerd met BO)
  - **Sollicitatiegesprek** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Verzoek om in een functie te worden aangesteld."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Vacature]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Sollicitatie op vacature"
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Werknemer solliciteert intern"
bedrijfsprocessen: [Werving en selectie]
bedrijfsfuncties: [Personeelsbeheer]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Kern van het wervingsproces |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip |
| Heeft eigen bestaan binnen het domein | ✅ Elk verzoek is een afzonderlijk record |
| Kan in meervoud bestaan | ✅ Tientallen tot honderden per vacature |
| Heeft eigen levenscyclus | ✅ Ontvangen → in behandeling → gesprek → aangenomen/afgewezen |
| Heeft relaties met andere concepten | ✅ Vacature, Sollicitant, Sollicitatiegesprek |

Score: **6/6**

## Beschrijving

Een sollicitatie is het verzoek van een kandidaat (intern of extern) om aangesteld te worden op een vacature. Het GGM modelleert de sollicitant als aparte entiteit (Sollicitant, erft van NatuurlijkPersoon) en het sollicitatiegesprek als apart object (Sollicitatiegesprek). Deze zijn niet als aparte BO's opgenomen maar als onderdeel van het sollicitatieproces.

## GGM-bron

> "Verzoek om in een functie te worden aangesteld."

- **Entiteit:** Sollicitatie
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datum
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Sollicitatie op [[Vacature]] | van dit BO | 1 | GGM |
| [[Werknemer]] solliciteert | naar dit BO | 0..1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/po-beleid]]
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsmarktkrapte-aanpak-gemeenten]]
