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
    afwijkende_attributen:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Contactpersoon** als directe tegenhanger. Daarnaast is **Contactpersoon** (beleidsdomein Vroegsignalering) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **AanleverendeOrganisatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **ContactpersoonRol** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
bo_definitie: "Contactpersoon van een organisatie."
bo_toelichting:
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

## GGM-duplicaten

De GGM-entiteit "Contactpersoon" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **Schuldhulpverlening** | `EAID_B9287881_AD66_4396_A629_ED5FE9196316` | **primair** — gekozen omdat dit BO vanuit het schuldhulpverleningsproces is afgeleid |
| Vroegsignalering | `EAID_A629ED5F_E919_6316_A279_92891F2325BB` | duplicaat — geen waarneembaar attribuutverschil |

Beide dekken dezelfde generieke RGBZ-rol: een contactpersoon namens een betrokkene, met naam, functie, telefoonnummer en e-mailadres.

Teruggemeld als #97 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Bedrijfsobject | Toelichting |
|---|---|---|
| Contactpersoon van | *(Schuldhulporganisatie)* | GGM: "heeft" (1..*/0..*) — Schuldhulporganisatie heeft nog geen eigen wiki-pagina; niet beoordeeld in deze sessie |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]] — RGBZ 1.0 definieert Contactpersoon als rol namens een betrokkene, met naam, functie, telefoonnummer en e-mailadres