---
type: bedrijfsobject
naam: Declaratie
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Declaratie
ggm_guid: EAID_E611CEB2_F4FA_49e2_AA6B_B380BC1918AC
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53]
ggm_definitie: "Een opgave van te vergoeden kosten."
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

gemma_definitie: "Een opgave van te vergoeden kosten ingediend door een werknemer."
relaties:
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Werknemer dient declaratie in"
bedrijfsprocessen: [Declaratieverwerking, Salarisadministratie]
bedrijfsfuncties: [Personeelsbeheer, Financieel beheer]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Standaardproces in personeelsadministratie |
| Herkenbaar voor domeinexperts | ✅ Elke werknemer kent declaraties |
| Heeft eigen bestaan binnen het domein | ✅ Elke declaratie is een afzonderlijk record |
| Kan in meervoud bestaan | ✅ Duizenden per jaar |
| Heeft eigen levenscyclus | ✅ Indiening → beoordeling → uitbetaling/afwijzing |
| Heeft relaties met andere concepten | ✅ Werknemer, Declaratiesoort |

Score: **6/6**

## Beschrijving

Een declaratie is een opgave van kosten die een werknemer ter vergoeding indient bij de werkgever. Declaratiesoorten (reiskosten, verblijfkosten, studiekosten, etc.) worden als enumeratie vastgelegd via Declaratiesoort.

NB: Het GGM heeft ook een entiteit "Declaratie" in beleidsdomein Generiek Jeugd en Wmo (taakveld 6). Dit BO betreft de HR-variant.

## GGM-bron

> "Een opgave van te vergoeden kosten."

- **Entiteit:** Declaratie
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datumIndiening, datumDeclaratie, betreft, omschrijving, bedrag
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Werknemer]] dient declaratie in | naar dit BO | 1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/financiele-arbeidsvoorwaarden]]
