---
type: element
naam: Raadslid
onderwerp: [bestuur]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Raadslid
ggm_guid: EAID_5772BEBB_97FA_42a9_B70D_DB55EAD6D1EE
ggm_uml_type: Class
ggm_beleidsdomein: Griffie
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_definitie: "Iemand die behoort de gemeenteraad"
ggm_herkomst: GGM
ggm_duplicaat_entiteiten: []
bo_definitie: "Iemand die behoort tot de gemeenteraad."
bo_toelichting:
element_tegenhangers:
  - element: "[[Wiki/Rollen/raadslid|Raadslid (rol)]]"
    archimate_type: business-role
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige rol."
---

# Raadslid

De vastgelegde gegevens over een raadslid in het raadsinformatiesysteem: naam, titel, fractie en datum van aanstelling en uittreding.

De handelende kant van dit begrip is vastgelegd als rol [[Wiki/Rollen/raadslid|Raadslid (rol)]].

## BO-criteria toetsing

6/6 criteria: herkenbaar begrip met eigen registratie (voornaam, achternaam, titel, fractie, datumAanstelling, datumUittreding), meervoud, eigen levenscyclus en relaties binnen het domein.

## GGM-bron

> "Iemand die behoort de gemeenteraad"

- **Entiteit:** Raadslid
- **Beleidsdomein:** Griffie (taakveld 0 Bestuur, Politiek en Ondersteuning)
- **Attributen:** voornaam, achternaam, titel, fractie, datumAanstelling, datumUittreding
- **Matchsterkte:** exact

## Bronnen

- [[Wiki/Analyses/entiteitendekking/0-bestuur-politiek-en-ondersteuning|Entiteitendekking-rapport]] — kandidaat gesignaleerd via /audit-actoren track 1
