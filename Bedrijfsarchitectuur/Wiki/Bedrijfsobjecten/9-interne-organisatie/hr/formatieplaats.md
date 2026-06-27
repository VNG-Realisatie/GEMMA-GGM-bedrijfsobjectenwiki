---
type: bedrijfsobject
naam: Formatieplaats
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Formatieplaats
ggm_guid: EAID_81EFBDCE_E500_4090_A37A_D3F799517866
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects, Bezetting en Formatie]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53, EAID_0B1C1CCE_E0D1_413d_A38B_7A9B03A21610]
ggm_definitie: "Uitgangspunt is het vastgestelde formatieplan, dus niet de werkelijke bezetting. Het gaat hier om de toegestane formatie in fte van het ambtelijk apparaat van uw organisatie voor het begrotingsjaar."
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

bo_definitie: "Vastgestelde eenheid in het formatieplan, uitgedrukt in fte, gekoppeld aan een functie en organisatorische eenheid."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Functie]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Functie van formatieplaats"
  - type: associatie
    bedrijfsobject: "[[Dienstverband]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Formatieplaats toegewezen aan dienstverband"
bedrijfsprocessen: [Formatiebeheer, Begrotingscyclus]
bedrijfsfuncties: [Personeelsbeheer, Organisatieontwikkeling]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Basis van het formatieplan |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip in formatiebeheer |
| Heeft eigen bestaan binnen het domein | ✅ Bestaat los van bezetting |
| Kan in meervoud bestaan | ✅ Honderden per gemeente |
| Heeft eigen levenscyclus | ✅ Vaststellen → wijzigen → opheffen |
| Heeft relaties met andere concepten | ✅ Functie, Dienstverband, OrganisatorischeEenheid |

Score: **6/6**

## Beschrijving

Een formatieplaats is een goedgekeurde positie in het formatieplan van de gemeente, uitgedrukt in fte. Het formatieplan beschrijft de toegestane bezetting, niet de werkelijke. Een formatieplaats is gekoppeld aan een functie en een organisatorische eenheid. Het verschil tussen formatie en bezetting is een belangrijke stuurindicator in de bedrijfsvoering.

## GGM-bron

> "Uitgangspunt is het vastgestelde formatieplan, dus niet de werkelijke bezetting. Het gaat hier om de toegestane formatie in fte van het ambtelijk apparaat van uw organisatie voor het begrotingsjaar."

- **Entiteit:** Formatieplaats
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** uren per week
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Formatieplaats heeft [[Functie]] | van dit BO | 1..* | GGM |
| Formatieplaats toegewezen aan [[Dienstverband]] | van dit BO | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
