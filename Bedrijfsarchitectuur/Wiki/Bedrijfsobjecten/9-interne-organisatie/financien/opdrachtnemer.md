---
type: element
naam: Opdrachtnemer
onderwerp: [financien]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Opdrachtnemer
ggm_guid: EAID_9ABE303F_1E8D_407c_BBB8_E7DAC383E0C3
ggm_uml_type: Class
ggm_beleidsdomein: Financien
ggm_taakveld: "9 Interne Organisatie"
ggm_definitie: "Partij die een opdracht aanvaardt."
ggm_herkomst: GGM
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Opdrachtnemer** als directe tegenhanger.
bo_definitie: "Partij die een opdracht aanvaardt."
bo_toelichting:
element_tegenhangers:
  - element: "[[Wiki/Rollen/opdrachtnemer|Opdrachtnemer (rol)]]"
    archimate_type: business-role
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige rol."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats|Kostenplaats]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Kostenplaatsen hebben deze Opdrachtnemer als budgetverantwoordelijke
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product|Product]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Opdrachtnemer kan opdrachtnemer zijn van meerdere Producten
---

# Opdrachtnemer

De vastgelegde gegevens over een opdrachtnemer in de financiële administratie: naam, omschrijving, nummer en clustercode.

De handelende kant van dit begrip is vastgelegd als rol [[Wiki/Rollen/opdrachtnemer|Opdrachtnemer (rol)]].

## BO-criteria toetsing

6/6 criteria: herkenbaar begrip met eigen registratie (naam, omschrijving, nummer, clustercode, clustercodeOmschrijving), meervoud, eigen levenscyclus en relaties binnen het domein.

## GGM-bron

> "Partij die een opdracht aanvaardt."

- **Entiteit:** Opdrachtnemer
- **Beleidsdomein:** Financien (taakveld 9 Interne Organisatie)
- **Attributen:** naam, omschrijving, nummer, clustercode, clustercodeOmschrijving
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Toelichting |
|---|---|---|
| Budgetverantwoordelijk voor | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] | Elke kostenplaats heeft precies één budgetverantwoordelijke Opdrachtnemer (GGM: "is budgetverantwoordelijk") |
| Opdrachtnemer van | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product\|Product]] | Een Opdrachtnemer kan opdrachtnemer zijn van meerdere Producten (GGM: "is opdrachtnemer") |

BW art. 400-413 (zie Bronnen) beschrijft de wederkerige rechtsverhouding met de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/opdrachtgever\|Opdrachtgever]]: zorgplicht, opvolgen van aanwijzingen en verantwoordingsplicht. Het GGM modelleert deze wederkerigheid niet als eigen relatie tussen Opdrachtgever en Opdrachtnemer; beide staan los gekoppeld aan Product/Doelstelling/Kostenplaats.

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/bw7-opdracht]] — BW Boek 7, Titel 7, Afdeling 1: wettelijke grondslag opdrachtnemer (art. 400-413)
