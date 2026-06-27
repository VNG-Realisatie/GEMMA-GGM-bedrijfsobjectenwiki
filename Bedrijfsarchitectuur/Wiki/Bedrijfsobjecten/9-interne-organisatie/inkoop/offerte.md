---
type: bedrijfsobject
naam: Offerte
onderwerp: [inkoop]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Offerte
ggm_guid: EAID_BF21FFA3_3EA6_410a_BC65_7BE5547646B6
ggm_uml_type: Class
ggm_beleidsdomein: Inkoop
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs."
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

ggm_duplicaat_entiteiten:
  - entiteit: Offerte
    guid: EAID_EF55544A_F59B_4411_A3D2_9C1A2BA2663C
    beleidsdomein: Inkoop
    taakveld: "9 Interne Organisatie"
    afwijkende_attributen: "Niet op een diagram geplaatst"
  - entiteit: Offerte
    guid: EAID_B259BE5F_AC3A_4e0f_A149_D1F165277CC2
    beleidsdomein: Inkoop
    taakveld: "9 Interne Organisatie"
    afwijkende_attributen: "Niet op een diagram geplaatst"

bo_definitie: "Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs."
bo_toelichting: ''
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

1. **Heeft betekenis binnen het onderwerp** — ja, het aanbod van een leverancier
2. **Is herkenbaar voor domeinexperts** — ja, inkopers beoordelen offertes dagelijks
3. **Heeft een eigen bestaan** — ja, een offerte is een formeel document met eigen prijs en datum
4. **Kan in meervoud bestaan** — ja, per aanbesteding meerdere offertes
5. **Heeft een eigen levenscyclus** — ja: aangevraagd → ingediend → beoordeeld → gegund/afgewezen
6. **Heeft relaties met andere concepten** — ja: Aanbesteding, Leverancier, Gunning

Score: 6/6

## Beschrijving

Een offerte is een formeel aanbod van een leverancier met een prijsopgave voor de gevraagde goederen, diensten of werken. Bij onderhandse aanbestedingen (enkelvoudig of meervoudig) is de offerte het primaire beoordelingsdocument. De gemeente beoordeelt offertes op basis van de vastgestelde gunningscriteria.

## GGM-bron

> "Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs." (GGM, beleidsdomein Inkoop)

**Matchsterkte:** exact — GGM-entiteit en BO zijn hetzelfde concept.

**Attributen:** prijs, datumOfferte, naam, omschrijving

## GGM-duplicaten

De GGM-entiteit "Offerte" komt voor met 3 GUIDs:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **Inkoop** | `EAID_BF21FFA3_3EA6_410a_BC65_7BE5547646B6` | **primair** — gekozen als canonieke mapping omdat deze op het Inkoop-diagram staat |
| Inkoop | `EAID_EF55544A_F59B_4411_A3D2_9C1A2BA2663C` | duplicaat — niet op een diagram geplaatst |
| Inkoop | `EAID_B259BE5F_AC3A_4e0f_A149_D1F165277CC2` | duplicaat — niet op een diagram geplaatst |

Teruggemeld als #79 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Aanbesteding\|Aanbesteding]] | betreft | ← | 1 | GGM |
| [[Leverancier\|Leverancier]] | ingediend door | ← | 1 | GGM |
| [[Gunning\|Gunning]] | kan leiden tot | → | 0..1 | GGM |

## Bedrijfsprocessen

- **Selecteren** — ontvangen, beoordelen en rangschikken van offertes

## Bedrijfsfuncties

- **Inkoopfunctie** — beoordeling offertes

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]
