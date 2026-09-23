---
type: element
naam: Aanwezige Deelnemer
onderwerp: [bestuur]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Aanwezige Deelnemer
ggm_guid: EAID_F1E55DC7_0F33_40ea_8713_2E1AC3D7EE8D
ggm_uml_type: Class
ggm_beleidsdomein: Griffie
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_definitie: "iemand die meedoet aan eencollege- of raadsvergadering"
ggm_herkomst: GGM
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Aanwezige Deelnemer** als directe tegenhanger.
bo_definitie: "Iemand die deelneemt aan een college- of raadsvergadering."
bo_toelichting:
element_tegenhangers:
  - element: "[[Wiki/Rollen/aanwezige-deelnemer|Aanwezige Deelnemer (rol)]]"
    archimate_type: business-role
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige rol."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/vergadering|Vergadering]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Elke aanwezigheid hoort bij precies één vergadering
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/raadslid|Raadslid]]"
    richting: bidirectioneel
    kardinaliteit: "0..1"
    beschrijving: Een aanwezige deelnemer kan een raadslid zijn
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/collegelid|Collegelid]]"
    richting: bidirectioneel
    kardinaliteit: "0..1"
    beschrijving: Een aanwezige deelnemer kan een collegelid zijn
---

# Aanwezige Deelnemer

De vastgelegde gegevens over de aanwezigheid van een deelnemer bij een college- of raadsvergadering: naam, rol, vertegenwoordigde organisatie en aanvang/einde van de aanwezigheid.

De handelende kant van dit begrip is vastgelegd als rol [[Wiki/Rollen/aanwezige-deelnemer|Aanwezige Deelnemer (rol)]].

## BO-criteria toetsing

6/6 criteria: herkenbaar begrip met eigen registratie (aanvangAanwezigheid, eindeAanwezigheid, rol, vertegenwoordigtOrganisatie, naam), meervoud, eigen levenscyclus en relaties binnen het domein.

## GGM-bron

> "iemand die meedoet aan eencollege- of raadsvergadering"

- **Entiteit:** Aanwezige Deelnemer
- **Beleidsdomein:** Griffie (taakveld 0 Bestuur, Politiek en Ondersteuning)
- **Attributen:** aanvangAanwezigheid, eindeAanwezigheid, rol, vertegenwoordigtOrganisatie, naam
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Toelichting |
|---|---|---|
| Hoort bij | [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/vergadering\|Vergadering]] | Elke aanwezigheid is geregistreerd bij één vergadering (GGM: associatie) |
| Kan zijn | [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/raadslid\|Raadslid]] | GGM: "is" |
| Kan zijn | [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/collegelid\|Collegelid]] | GGM: "is" |

**Openstaand:** het GGM legt ook een relatie met **NatuurlijkPersoon** (0..1/0..1, "is") — voor aanwezigen die geen raadslid of collegelid zijn (bijv. een insprekend inwoner). NatuurlijkPersoon heeft nog geen eigen wiki-pagina in dit onderwerp; niet beoordeeld in deze sessie.

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst]] — Gemeentewet art. 17-24 (vergadering: quorum, agenda, aanwezigheid)