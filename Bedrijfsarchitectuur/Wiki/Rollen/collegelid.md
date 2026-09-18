---
type: element
naam: Collegelid
onderwerp: [bestuur]
archimate_type: business-role
grondslag: ggm-entiteit
ggm_entiteit: Collegelid
ggm_guid: EAID_7B9EDDFD_57F7_4ff2_938F_FDFA3B503DA8
ggm_beleidsdomein: Griffie
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Collegelid** als directe tegenhanger.
bo_definitie: "Het lidmaatschap van het college van burgemeester en wethouders: de verantwoordelijkheid van dagelijks bestuur en portefeuillebeheer, vervuld door een benoemde persoon."
bo_toelichting:
element_tegenhangers:
  - element: "[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/collegelid|Collegelid (bedrijfsobject)]]"
    archimate_type: business-object
    toelichting: "De gegevens over deze rol worden vastgelegd als bedrijfsobject."
---

# Collegelid (rol)

Het collegelidmaatschap is de verantwoordelijkheid van het dagelijks bestuur van de gemeente, per portefeuille verdeeld. De rol begint met benoeming en eindigt met uittreding; de persoon die de rol vervult is de actor.

De gegevens over deze rol worden vastgelegd als bedrijfsobject [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/collegelid|Collegelid]].

## Criteria-toetsing (Business Role)

| Vraag | Antwoord |
|---|---|
| Verantwoordelijkheid i.p.v. entiteit? | De rol zelf niet; de vervullende persoon wel |
| Door meerdere actoren vervulbaar? | Ja — door verschillende benoemde personen |
| Eén actor kan meerdere rollen tegelijk vervullen? | Ja — collegelid kan meerdere portefeuilles dragen |
| Gekoppeld aan taken/bevoegdheden/verantwoordelijkheden? | Ja — dagelijks bestuur, portefeuilleverantwoordelijkheid (Gemeentewet) |
| Geen eigen identiteit, door actor vervuld? | Ja — het lidmaatschap wordt door een persoon vervuld |
| Actor expliciet toewijsbaar? | Ja — via benoeming (datumAanstelling/datumUittreding) |

## GGM-bron

> "Iemand die behoort het college van burgemeester en wethouders"

- **Entiteit:** Collegelid
- **Beleidsdomein:** Griffie (taakveld 0 Bestuur, Politiek en Ondersteuning)
- **Matchsterkte:** exact

## Bronnen

- [[Wiki/Analyses/entiteitendekking/0-bestuur-politiek-en-ondersteuning]] — kandidaat gesignaleerd via /audit-actoren track 1
