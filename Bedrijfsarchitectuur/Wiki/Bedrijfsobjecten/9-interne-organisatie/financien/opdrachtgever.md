---
type: element
naam: Opdrachtgever
onderwerp: [financien]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Opdrachtgever
ggm_guid: EAID_C2520FC3_622B_4edf_B911_C661B0D710FE
ggm_uml_type: Class
ggm_beleidsdomein: Financien
ggm_taakveld: "9 Interne Organisatie"
ggm_definitie: "Persoon die een opdracht verstrekt."
ggm_herkomst: GGM
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Opdrachtgever** als directe tegenhanger.
bo_definitie: "Persoon die een opdracht verstrekt."
bo_toelichting:
element_tegenhangers:
  - element: "[[Wiki/Rollen/opdrachtgever|Opdrachtgever (rol)]]"
    archimate_type: business-role
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige rol."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling|Doelstelling]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Doelstellingen hebben deze Opdrachtgever
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product|Product]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Opdrachtgever kan opdrachtgever zijn van meerdere Producten
---

# Opdrachtgever

De vastgelegde gegevens over een opdrachtgever in de financiële administratie: naam, omschrijving, nummer en clustercode.

De handelende kant van dit begrip is vastgelegd als rol [[Wiki/Rollen/opdrachtgever|Opdrachtgever (rol)]].

## BO-criteria toetsing

6/6 criteria: herkenbaar begrip met eigen registratie (naam, omschrijving, nummer, clustercode, clusterOmschrijving), meervoud, eigen levenscyclus en relaties binnen het domein.

## GGM-bron

> "Persoon die een opdracht verstrekt."

- **Entiteit:** Opdrachtgever
- **Beleidsdomein:** Financien (taakveld 9 Interne Organisatie)
- **Attributen:** naam, omschrijving, nummer, clustercode, clusterOmschrijving
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Toelichting |
|---|---|---|
| Opdrachtgever van | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling\|Doelstelling]] | Elke doelstelling heeft precies één Opdrachtgever (GGM: "is opdrachtgever") |
| Opdrachtgever van | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product\|Product]] | Een Opdrachtgever kan opdrachtgever zijn van meerdere Producten (GGM: "is opdrachtgever") |

BW art. 400-413 (zie Bronnen) beschrijft de wederkerige rechtsverhouding met de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/opdrachtnemer\|Opdrachtnemer]]: loonverschuldigdheid, opzeggingsrecht en informatieplicht over en weer. Het GGM modelleert deze wederkerigheid niet als eigen relatie tussen Opdrachtgever en Opdrachtnemer; beide staan los gekoppeld aan Doelstelling/Product/Kostenplaats.

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/bw7-opdracht]] — BW Boek 7, Titel 7, Afdeling 1: wettelijke grondslag opdrachtgever (art. 400-413)