---
type: element
naam: Hardware
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Hardware
ggm_guid: EAID_6C92F0F8_BC92_428c_B729_1A10D515DAEF
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items Diversen]
ggm_diagram_ids: [EAID_A255BB0C_A1DB_43a5_88B1_C638F6E64B0B]
ggm_definitie: "Alle fysieke componenten of onderdelen die in een computer een rol spelen."
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
  Dit BO heeft de GGM-entiteit **Hardware** als directe tegenhanger.
bo_definitie: "Fysieke IT-componenten of onderdelen die in een computer of netwerk een rol spelen."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server|Server]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Server is een specifiek type hardware"
bedrijfsprocessen: [Infrastructuurbeheer, Assetmanagement]
bedrijfsfuncties: [ICT-beheer]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Fysieke IT-componenten; de tastbare basis van de infrastructuur |
| Herkenbaarheid | "werkstations", "printers", "thin clients", "opslagapparatuur" |
| Eigen bestaan | Subtype van CMDB-item; eigen financiële waarde en afschrijving |
| Meervoud | Honderden per gemeente |
| Levenscyclus | Aanschaf → installatie → gebruik → onderhoud → vervanging/afvoer |
| Relaties | Server (specialisatie), Netwerkcomponent (sibling) |

Resultaat: 5/6 — BO. Geen eigen attributen in GGM maar voldoende criteria.

## Beschrijving

Hardware omvat alle fysieke IT-componenten: werkstations, laptops, printers, opslagapparatuur, monitors en randapparatuur. In het GGM is Hardware een subtype van CMDB-item, naast [[Software]], [[Licentie]], [[Netwerkcomponent]] en andere subtypes.

[[Server]] is in het GGM een apart objecttype (via Linkbaar CMDB-item), maar is in de praktijk ook hardware. Hardware heeft een eigen financiële levenscyclus (aanschaf, afschrijving, vervanging) die los staat van de software die erop draait.

## GGM-bron

> "Alle fysieke componenten of onderdelen die in een computer een rol spelen."
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Hardware | Matchsterkte: **exact** | Attributen: *(geen in GGM)*

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] | van-dit-BO | Server is een specifiek type hardware |

## Bedrijfsprocessen

- **Infrastructuurbeheer** — installatie, onderhoud, vervanging
- **Assetmanagement** — tracking van fysieke IT-assets, afschrijving

## Bedrijfsfuncties

- **ICT-beheer** — beheer van fysieke IT-infrastructuur

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer|CMDB & Informatiebeheerplan]]
