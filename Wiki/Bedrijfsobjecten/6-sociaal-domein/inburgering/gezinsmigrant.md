---
type: bedrijfsobject
naam: Gezinsmigrant
domein: [Asiel en Integratie]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Gezinsmigrant en Overige migrant"
ggm_guid: EAID_526489DC_4D57_4e6d_8338_5F7C898162F6
ggm_uml_type: Class
ggm_beleidsdomein: "Inburgering"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Inburgering, Relaties Sociaal Domein tot Kern]
ggm_diagram_ids: [EAID_96927C60_9F7B_4e67_806A_02EE0191983D, EAID_D7287848_8118_4aab_8823_D555A599063C]
ggm_definitie: "Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant.

Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en Overige Migrant zoals bijvoorbeeld: object Aanvraag Sociale Lening. Hetzelfde geldt ook voor object Asielstatushouder, deze heeft overigens wel kenmerken."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Gezinsmigrant en Overige migrant"
ggm_gemma_guid: ""
ggm_gemma_definitie: "Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant.

Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-61601c33-5b61-4bab-9191-e7eb1b1bca07"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Inburgeringsplichtige die verblijf heeft op grond van gezinshereniging of andere migratiereden, niet zijnde asiel."
bronnen: ["Bronsamenvattingen/Asiel en Integratie/vng-inburgering.md", "Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer.md"]
relaties:
  - type: associatie
    bedrijfsobject: Brede Intake
    richting: "van-dit-BO"
    kardinaliteit: 1
    beschrijving: Doorloopt een brede intake
  - type: associatie
    bedrijfsobject: PIP
    richting: "van-dit-BO"
    kardinaliteit: 1
    beschrijving: Krijgt een persoonlijk plan inburgering en participatie
  - type: associatie
    bedrijfsobject: Inburgeringsplicht
    richting: "van-dit-BO"
    kardinaliteit: 1
    beschrijving: Heeft een inburgeringsplicht
---

# Gezinsmigrant

Inburgeringsplichtige die verblijf heeft op grond van gezinshereniging of andere migratiereden, niet zijnde asiel.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant. Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en Overige Migrant.

- **Entiteit:** Gezinsmigrant en Overige migrant
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** *(geen)*
- **Overerving:** Inburgeraar (abstract) → Gezinsmigrant en Overige migrant
- **Matchsterkte:** exact

## Relaties

- → [[brede-intake]] — doorloopt een brede intake [1]
- → [[pip]] — krijgt een PIP vastgesteld [1]
- → [[inburgeringsplicht]] — heeft een inburgeringsplicht [1]
