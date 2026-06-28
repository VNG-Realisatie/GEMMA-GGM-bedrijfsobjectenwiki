---
type: bedrijfsobject
naam: Verbonden Partij
onderwerp: [Financien]
archimate_type: "business-object"
grondslag: "procesobject"
ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
bo_definitie: "Privaatrechtelijke of publiekrechtelijke organisatie waarin de gemeente een bestuurlijk en een financieel belang heeft."
bo_toelichting: "Gemeenten rapporteren verplicht over verbonden partijen in een begrotingsparagraaf (BBV art. 15). Per partij: belang, vermogen, resultaat en risico's."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Begroting]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Verplichte paragraaf verbonden partijen in de begroting"
  - type: associatie
    bedrijfsobject: "[[Jaarrekening]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Verantwoording in de paragraaf verbonden partijen"
bedrijfsprocessen: [Begrotingscyclus, Jaarrekening]
bedrijfsfuncties: [Planning en control, Financieel beheer]
---

# Verbonden Partij

Privaatrechtelijke of publiekrechtelijke organisatie waarin de gemeente een bestuurlijk en een financieel belang heeft.

## BO-criteria toetsing

6/6 criteria: betekenisvol (verplicht rapportageobject BBV), herkenbaar (elke gemeente heeft verbonden partijen), eigen bestaan (externe organisatie), meervoud (tientallen per gemeente), levenscyclus (aangaan, wijzigen belang, beëindigen), relaties (begroting, jaarrekening, deelnemingen).

## Beschrijving

Een verbonden partij is een organisatie waarin de gemeente zowel bestuurlijk belang (zeggenschap) als financieel belang (risico bij faillissement) heeft. De begroting moet een verplichte paragraaf verbonden partijen bevatten (BBV art. 15) met per partij: de aard van het belang, verwachte omvang eigen/vreemd vermogen, financieel resultaat en risico's.

## Subtypes

Herkende specialisaties van Verbonden Partij. Geen apart BO.

- **Gemeenschappelijke regeling** — samenwerkingsverband op grond van de Wgr
- **Deelneming** — participatie in BV/NV waarin de gemeente aandelen heeft (BBV art. 1 sub e)
- **Vennootschap of coöperatie** — privaatrechtelijke rechtspersoon
- **Stichting of vereniging** — privaatrechtelijke rechtspersoon

## Procesbron

Uit het begrotings- en verantwoordingsproces. De gemeente rapporteert jaarlijks over alle verbonden partijen in begroting en jaarverslag.

## Relaties

| Gerelateerd BO | Relatie | Bron |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] | Verplichte paragraaf verbonden partijen | BBV art. 15 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/jaarrekening\|Jaarrekening]] | Verantwoording in jaarverslag | BBV art. 26 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/besluit-begroting-en-verantwoording]]
- [[Wiki/Bronsamenvattingen/Financien/begrippenlijst-gemeentebegroting]]

## Terugmelding GGM

Verbonden partij ontbreekt als entiteit in het GGM-beleidsdomein Financien. Verplicht rapportageobject (BBV art. 15) met eigen paragraaf in begroting en jaarverslag. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
