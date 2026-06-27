---
type: bedrijfsobject
naam: Aanbieding
onderwerp: [inkoop]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Inschrijving
ggm_guid: EAID_2902E8D6_FF16_45d6_A0A4_47E2857D2D19
ggm_uml_type: Class
ggm_beleidsdomein: Inkoop
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Inschrijving op een nationale of Europese aanbesteding"
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

bo_homoniemen:
  - bedrijfsobject: "[[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/opleidingsinschrijving|Opleidingsinschrijving]]"
    ggm_entiteit: "Inschrijving"
    ggm_guid: "EAID_CFFD5F20_5FA9_4d93_AD34_6867D64A58B9"
    ggm_beleidsdomein: "Onderwijs"
    toelichting: "Deelname aan een opleiding bij een onderwijsinstelling — ander concept dan aanbieding op een aanbesteding"

bo_definitie: "Formele deelname van een ondernemer aan een nationale of Europese aanbesteding van de gemeente."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Aanbesteding]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft"
  - type: associatie
    bedrijfsobject: "[[Leverancier]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "ingediend door"
  - type: associatie
    bedrijfsobject: "[[Gunning]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "kan leiden tot"
bedrijfsprocessen: [Selecteren]
bedrijfsfuncties: [Inkoopfunctie]
---

## BO-criteria toetsing

1. **Heeft betekenis binnen het onderwerp** — ja, formele deelname aan een aanbesteding
2. **Is herkenbaar voor domeinexperts** — ja, inkopers werken met aanbiedingen bij openbare aanbestedingen
3. **Heeft een eigen bestaan** — beperkt: altijd gekoppeld aan een aanbesteding, maar heeft eigen attributen
4. **Kan in meervoud bestaan** — ja, per aanbesteding meerdere aanbiedingen
5. **Heeft een eigen levenscyclus** — ja: ingediend → beoordeeld → gescoord → gegund/afgewezen
6. **Heeft relaties met andere concepten** — ja: Aanbesteding, Leverancier, Gunning

Score: 5/6

## Beschrijving

Een aanbieding is de formele deelname van een ondernemer aan een nationale of Europese aanbesteding. Anders dan een offerte (bij onderhandse procedures) is een aanbieding gebonden aan de formele eisen van de Aanbestedingswet: tijdige indiening, voldoen aan uitsluitingsgronden en geschiktheidseisen, en scoring op gunningscriteria.

## Naamkeuze

De GGM-entiteit heet "Inschrijving". Hernoemd naar "Aanbieding" ter disambiguatie van de GGM-homoniem "Inschrijving" in beleidsdomein Onderwijs (deelname aan een opleiding). Overwogen alternatieven: Inschrijving (aanbesteding), Aanbestedingsinschrijving.

## GGM-bron

> "Inschrijving op een nationale of Europese aanbesteding" (GGM, beleidsdomein Inkoop)

**Matchsterkte:** exact — GGM-entiteit en BO zijn hetzelfde concept.

**Attributen:** datum, prijs, score

Teruggemeld als #80 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Aanbesteding\|Aanbesteding]] | betreft | ← | 1 | GGM |
| [[Leverancier\|Leverancier]] | ingediend door | ← | 1 | GGM |
| [[Gunning\|Gunning]] | kan leiden tot | → | 0..1 | GGM |

## Bedrijfsprocessen

- **Selecteren** — ontvangen, beoordelen en scoren van aanbiedingen

## Bedrijfsfuncties

- **Inkoopfunctie** — beoordeling aanbiedingen bij openbare aanbestedingen

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]
