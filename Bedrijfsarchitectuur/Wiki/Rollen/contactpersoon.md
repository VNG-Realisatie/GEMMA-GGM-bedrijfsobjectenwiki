---
type: element
naam: Contactpersoon
onderwerp: [schulden en armoede]
archimate_type: business-role
grondslag: ggm-entiteit
ggm_entiteit: Contactpersoon
ggm_guid: EAID_B9287881_AD66_4396_A629_ED5FE9196316
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "6 Sociaal Domein"
ggm_duplicaat_entiteiten:
  - entiteit: Contactpersoon
    guid: EAID_A629ED5F_E919_6316_A279_92891F2325BB
    beleidsdomein: Vroegsignalering
    taakveld: "6 Sociaal Domein"
    afwijkende_attributen:
bo_definitie: "De hoedanigheid van aanspreekpunt namens een organisatie in het contact met de gemeente."
bo_toelichting:
element_tegenhangers:
  - element: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpersoon|Contactpersoon (bedrijfsobject)]]"
    archimate_type: business-object
    toelichting: "De gegevens over deze rol worden vastgelegd als bedrijfsobject."
---

# Contactpersoon (rol)

Contactpersoon is de rol van aanspreekpunt namens een organisatie, bijvoorbeeld bij een signaalpartner in de vroegsignalering of een organisatie in de schuldhulpverlening. De rol is gebonden aan de functie, niet aan de persoon.

De gegevens over deze rol worden vastgelegd als bedrijfsobject [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpersoon|Contactpersoon]].

## Criteria-toetsing (Business Role)

| Vraag | Antwoord |
|---|---|
| Verantwoordelijkheid i.p.v. entiteit? | Ja — aanspreekpunt-zijn is een hoedanigheid |
| Door meerdere actoren vervulbaar? | Ja — door verschillende medewerkers van de organisatie |
| Eén actor kan meerdere rollen tegelijk vervullen? | Ja — een contactpersoon kan meerdere organisaties vertegenwoordigen |
| Gekoppeld aan taken/bevoegdheden/verantwoordelijkheden? | Ja — het onderhouden van contact namens de organisatie |
| Geen eigen identiteit, door actor vervuld? | Ja — vervuld door een medewerker |
| Actor expliciet toewijsbaar? | Ja — per organisatie aangewezen |

## GGM-bron

> "Contactpersoon van een organisatie"

- **Entiteit:** Contactpersoon
- **Beleidsdomein:** Schuldhulpverlening (taakveld 6 Sociaal Domein)
- **Matchsterkte:** exact

## Bronnen

- [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]] — kandidaat gesignaleerd via /audit-actoren track 1
