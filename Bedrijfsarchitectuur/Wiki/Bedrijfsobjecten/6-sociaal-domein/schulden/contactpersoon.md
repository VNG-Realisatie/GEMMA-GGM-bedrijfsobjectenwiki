---
type: element
naam: Contactpersoon
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Contactpersoon
ggm_guid: EAID_B9287881_AD66_4396_A629_ED5FE9196316
ggm_uml_type: Class
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "6 Sociaal Domein"
ggm_definitie: "Contactpersoon van een organisatie"
ggm_herkomst: GGM
ggm_duplicaat_entiteiten:
  - entiteit: Contactpersoon
    guid: EAID_A629ED5F_E919_6316_A279_92891F2325BB
    beleidsdomein: Vroegsignalering
    taakveld: "6 Sociaal Domein"
    afwijkende_attributen: ""
bo_definitie: "Contactpersoon van een organisatie."
bo_toelichting: ""
element_tegenhangers:
  - element: "[[Wiki/Rollen/contactpersoon|Contactpersoon (rol)]]"
    archimate_type: business-role
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige rol."
---

# Contactpersoon

De vastgelegde gegevens over een contactpersoon: naam, telefoonnummer, e-mail en functietitel. Komt in het GGM voor bij schuldhulpverlening en vroegsignalering.

De handelende kant van dit begrip is vastgelegd als rol [[Wiki/Rollen/contactpersoon|Contactpersoon (rol)]].

## BO-criteria toetsing

6/6 criteria: herkenbaar begrip met eigen registratie (naam, telefoonnummer, email, functietitel), meervoud, eigen levenscyclus en relaties binnen het domein.

## GGM-bron

> "Contactpersoon van een organisatie"

- **Entiteit:** Contactpersoon
- **Beleidsdomein:** Schuldhulpverlening (taakveld 6 Sociaal Domein)
- **Attributen:** naam, telefoonnummer, email, functietitel
- **Matchsterkte:** exact

## Bronnen

- [[Wiki/Analyses/entiteitendekking/6-sociaal-domein|Entiteitendekking-rapport]] — kandidaat gesignaleerd via /audit-actoren track 1
