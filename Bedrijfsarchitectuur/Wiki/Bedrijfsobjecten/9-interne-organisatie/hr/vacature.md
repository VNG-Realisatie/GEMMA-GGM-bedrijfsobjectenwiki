---
type: bedrijfsobject
naam: Vacature
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vacature
ggm_guid: EAID_DC978807_5F36_4148_B816_D6886D026DD8
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Sollicitaties]
ggm_diagram_ids: [EAID_542C38C9_B92F_48de_87F1_F90F64FB5913]
ggm_definitie: "Een arbeidsplaats binnen een bedrijf of organisatie die nog gevuld dient te worden door werkzoekenden."
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

bo_definitie: "Een arbeidsplaats binnen een bedrijf of organisatie die nog gevuld dient te worden door werkzoekenden."
bo_toelichting: "In de context van dit BO: de gemeente als werkgever die eigen personeel zoekt via werving & selectie."
bo_homoniemen:
  - bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt|Vacature (arbeidsmarkt)]]"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_beleidsdomein: Werk
    toelichting: "Vacature (arbeidsmarkt) is de gemeente als arbeidsmarktbemiddelaar die werkzoekenden matcht aan vacatures van werkgevers in de regio (VUM). Ander proces, andere relaties."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Arbeidsfunctie]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Vacature bij functie"
  - type: associatie
    bedrijfsobject: "[[Sollicitatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Sollicitatie op vacature"
bedrijfsprocessen: [Werving en selectie]
bedrijfsfuncties: [Personeelsbeheer]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Startpunt van het wervingsproces |
| Herkenbaar voor domeinexperts | ✅ Iedereen kent vacatures |
| Heeft eigen bestaan binnen het domein | ✅ Bestaat als openstaande positie |
| Kan in meervoud bestaan | ✅ Tientallen gelijktijdig per gemeente |
| Heeft eigen levenscyclus | ✅ Opengesteld → in behandeling → gesloten/vervuld |
| Heeft relaties met andere concepten | ✅ Functie, Sollicitatie |

Score: **6/6**

## Beschrijving

Een vacature is een openstaande arbeidsplaats gekoppeld aan een functie. Vacatures kunnen intern of extern worden opengesteld, voor deeltijd of voltijd, en voor een vast of tijdelijk dienstverband. In de context van arbeidsmarktkrapte is het vacaturebeheer een centraal sturingsinstrument.

## GGM-bron

> "Een arbeidsplaats binnen een bedrijf of organisatie die nog gevuld dient te worden door werkzoekenden."

- **Entiteit:** Vacature
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datumOpengesteld, datumGesloten, intern, extern, deeltijd, vastedienst
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Vacature bij [[Arbeidsfunctie]] | van dit BO | 1 | GGM |
| [[Sollicitatie]] op vacature | naar dit BO | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsmarktkrapte-aanpak-gemeenten]]
