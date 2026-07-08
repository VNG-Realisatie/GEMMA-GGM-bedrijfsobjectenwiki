---
type: element
naam: Arbeidsfunctie
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

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Functie**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Functiehuis** (detail) — Detailgegeven (weinig attributen)
  - **NormProfiel** (detail) — Detailgegeven (geassocieerd met BO)
bo_homoniemen:
  - ggm_entiteit: "Functie"
    ggm_guid: "EAID_3BDD29C7_FBCD_4c90_A520_8187E2D9BD57"
    ggm_beleidsdomein: "Omgevingswet"
    toelichting: "Ruimtelijke gebiedsfunctie (centrumgebied, bedrijventerrein) — ander concept dan arbeidsfunctie"

bo_definitie: "Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden."
bo_toelichting: ''
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

Een arbeidsfunctie beschrijft het samenstel van taken en werkzaamheden op een bepaald schaalniveau. Elke arbeidsfunctie is gebaseerd op een NormProfiel uit het HR21-functiewaarderingssysteem. Een arbeidsfunctie bestaat onafhankelijk van of er iemand op werkt — het is de structurele positie in het functiehuis.

## Naamkeuze

De GGM-entiteit heet "Functie". Hernoemd naar "Arbeidsfunctie" ter disambiguatie van de GGM-homoniem "Functie" in beleidsdomein Omgevingswet (ruimtelijke gebiedsfunctie). Overwogen alternatieven: Functie (ongewijzigd).

## GGM-bron

> "Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden."

- **Entiteit:** Functie
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** Naam, Omschrijving, Taken, Schaal, Code
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Dienstverband]] conform arbeidsfunctie | naar dit BO | 0..* | GGM |
| [[Formatieplaats]] heeft arbeidsfunctie | naar dit BO | 1..* | GGM |
| [[Vacature]] bij arbeidsfunctie | naar dit BO | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsvoorwaarden]]
