---
type: bedrijfsobject
naam: Verzuim
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Verzuim
ggm_guid: EAID_610B18E6_B675_4cc0_A883_BAB9D384C668
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53]
ggm_definitie: "Een afwezigheid van een werknemer van werk."
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

bo_definitie: "Een afwezigheid van een werknemer van werk."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Werknemer heeft verzuim"
bedrijfsprocessen: [Verzuimregistratie, Verzuimbegeleiding, Re-integratie]
bedrijfsfuncties: [Personeelsbeheer, Arbobeleid]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Wettelijk verplichte registratie (Wet Poortwachter) |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip in HR |
| Heeft eigen bestaan binnen het domein | ✅ Elk verzuimgeval is een afzonderlijk record |
| Kan in meervoud bestaan | ✅ Honderden per jaar per gemeente |
| Heeft eigen levenscyclus | ✅ Ziekmelding → begeleiding → herstelmelding of WIA |
| Heeft relaties met andere concepten | ✅ Werknemer, Verzuimsoort |

Score: **6/6**

## Beschrijving

Verzuim is de afwezigheid van een werknemer, doorgaans wegens ziekte. De gemeente is als werkgever verantwoordelijk voor verzuimregistratie, -begeleiding en re-integratie conform de Wet Poortwachter. Bij langdurig verzuim volgt een WIA-beoordeling. Gemeenten zijn eigen risicodrager voor de WW en vaak ook voor de Ziektewet, wat verzuimbeheer financieel extra relevant maakt.

Verzuimsoorten (ziekte, arbeidsongeval, etc.) worden als enumeratie vastgelegd via Verzuimsoort.

## GGM-bron

> "Een afwezigheid van een werknemer van werk."

- **Entiteit:** Verzuim
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datumtijdStart, datumtijdEinde
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Werknemer]] heeft verzuim | naar dit BO | 1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
