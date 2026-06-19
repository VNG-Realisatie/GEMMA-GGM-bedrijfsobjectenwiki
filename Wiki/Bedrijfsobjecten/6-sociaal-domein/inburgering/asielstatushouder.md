---
type: bedrijfsobject
naam: Asielstatushouder
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Asielstatushouder
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "De Inburgeringsplichtige die rechtmatig verblijf heeft"
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [statushouder, kansrijke-koppeling]
relaties:
  - type: associatie
    bedrijfsobject: Brede Intake
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Doorloopt een brede intake na koppeling aan de gemeente"
  - type: associatie
    bedrijfsobject: PIP
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Krijgt een persoonlijk plan inburgering en participatie"
  - type: associatie
    bedrijfsobject: Voorbereiding op Inburgering
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Neemt deel aan voorbereiding op inburgering"
  - type: associatie
    bedrijfsobject: Inburgeringsplicht
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Heeft een inburgeringsplicht"
---

# Asielstatushouder

De inburgeringsplichtige die rechtmatig verblijf heeft als asielgerechtigde en door kansrijke koppeling aan een gemeente is toegewezen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> De Inburgeringsplichtige die rechtmatig verblijf heeft

- **Entiteit:** Asielstatushouder
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** Telefoonnummer verblijf AZC, Emailadres verblijf AZC, DigiD aangevraagd, Rijbewijs, Land Rijbewijs, Is gekoppeld aan
- **Overerving:** Inburgeraar (abstract) → Asielstatushouder
- **Matchsterkte:** exact

## Relaties

- → [[brede-intake]] — doorloopt een brede intake na koppeling aan de gemeente [1]
- → [[pip]] — krijgt een PIP vastgesteld [1]
- → [[voorbereiding-op-inburgering]] — neemt deel aan voorbereiding op inburgering [1]
- → [[inburgeringsplicht]] — heeft een inburgeringsplicht [1]
