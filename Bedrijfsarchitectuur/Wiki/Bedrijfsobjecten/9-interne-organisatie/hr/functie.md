---
type: bedrijfsobject
naam: Functie
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Functie
ggm_guid: EAID_F29C11C1_477C_4b90_985C_43F94D08230A
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Financien Personen, Domain Objects, Sollicitaties, Bezetting en Formatie]
ggm_diagram_ids: [EAID_CB1E27F6_9539_4037_8A93_07CC937D5D2E, EAID_891372E6_27FB_442d_9CC4_08C2659E8C53, EAID_542C38C9_B92F_48de_87F1_F90F64FB5913, EAID_0B1C1CCE_E0D1_413d_A38B_7A9B03A21610]
ggm_definitie: "Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden."
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

bo_definitie: "Het samenstel van feitelijk opgedragen taken en werkzaamheden, gewaardeerd via het functiehuis (HR21)."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Dienstverband]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Dienstverband conform functie"
  - type: associatie
    bedrijfsobject: "[[Formatieplaats]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Functie van formatieplaats"
  - type: associatie
    bedrijfsobject: "[[Vacature]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Vacature bij functie"
bedrijfsprocessen: [Formatiebeheer, Functiewaardering, Werving en selectie]
bedrijfsfuncties: [Personeelsbeheer, Organisatieontwikkeling]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Structureel element van het functiehuis |
| Herkenbaar voor domeinexperts | ✅ HR21 is standaard functiewaarderingssysteem |
| Heeft eigen bestaan binnen het domein | ✅ Bestaat onafhankelijk van wie de functie vervult |
| Kan in meervoud bestaan | ✅ Tientallen tot honderden per gemeente |
| Heeft eigen levenscyclus | ✅ Aanmaken → herwaarderen → opheffen |
| Heeft relaties met andere concepten | ✅ Formatieplaats, Dienstverband, Vacature, NormProfiel |

Score: **6/6**

## Beschrijving

Een functie beschrijft het samenstel van taken en werkzaamheden op een bepaald schaalniveau. Elke functie is gebaseerd op een NormProfiel uit het HR21-functiewaarderingssysteem. Een functie bestaat onafhankelijk van of er iemand op werkt — het is de structurele positie in het functiehuis.

## GGM-bron

> "Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden."

- **Entiteit:** Functie
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** Naam, Omschrijving, Taken, Schaal, Code
- **Matchsterkte:** exact

NB: Het GGM heeft ook een entiteit "Functie" in beleidsdomein Omgevingswet (taakveld 8) met een andere betekenis (ruimtelijke functie). Dit BO betreft de HR-variant.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Dienstverband]] conform functie | naar dit BO | 0..* | GGM |
| [[Formatieplaats]] heeft functie | naar dit BO | 1..* | GGM |
| [[Vacature]] bij functie | naar dit BO | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsvoorwaarden]]
