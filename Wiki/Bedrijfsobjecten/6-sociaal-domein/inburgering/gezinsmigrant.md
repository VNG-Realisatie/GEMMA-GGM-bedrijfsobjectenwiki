---
type: bedrijfsobject
naam: Gezinsmigrant
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Gezinsmigrant en Overige migrant
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant. Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en Overige Migrant zoals bijvoorbeeld: object Aanvraag Sociale Lening. Hetzelfde geldt ook voor object Asielstatushouder, deze heeft overigens wel kenmerken."
gemma_definitie: "Inburgeringsplichtige die verblijf heeft op grond van gezinshereniging of andere migratiereden, niet zijnde asiel."
gerelateerde_begrippen: [statushouder]
relaties:
  - type: associatie
    bedrijfsobject: Brede Intake
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Doorloopt een brede intake"
  - type: associatie
    bedrijfsobject: PIP
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Krijgt een persoonlijk plan inburgering en participatie"
  - type: associatie
    bedrijfsobject: Inburgeringsplicht
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Heeft een inburgeringsplicht"
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
