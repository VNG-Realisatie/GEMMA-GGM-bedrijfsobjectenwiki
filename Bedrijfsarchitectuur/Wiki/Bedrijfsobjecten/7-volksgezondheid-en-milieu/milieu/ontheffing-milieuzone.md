---
type: element
naam: Ontheffing (milieuzone)
onderwerp: [milieu]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

bo_definitie: "Individuele uitzondering op milieuzoneregels waarmee een specifiek voertuig tijdelijk toegang krijgt tot de milieuzone."
bo_toelichting:
bo_subtypes:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Vergunningen en ontheffingen]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Ontheffing milieuzone is een specialisatie van Vergunningen en ontheffingen"
  - type: associatie
    bedrijfsobject: "[[Milieuzone]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een ontheffing geldt voor een specifieke milieuzone"
bedrijfsprocessen: [vergunningverlening, milieuhandhaving]
bedrijfsfuncties: [milieubeheer, vergunningverlening]
---

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel instrument bij milieuzones voor uitzonderingssituaties |
| Is herkenbaar voor domeinexperts | ✅ | Ambtenaren en aanvragers spreken over "ontheffing milieuzone" |
| Heeft een eigen bestaan | ✅ | Individueel document/besluit per voertuig |
| Kan in meervoud bestaan | ✅ | Meerdere ontheffingen per zone en per voertuigcategorie |
| Heeft een eigen levenscyclus | ✅ | Aanvragen → beoordelen → toekennen/weigeren → verlopen |
| Heeft relaties met andere concepten | ✅ | Met milieuzone, voertuig, aanvrager |

Score: **6/6** — BO.

## Beschrijving

Een ontheffing (milieuzone) is een individuele uitzondering waarmee een voertuig dat niet aan de emissieklasse-eisen voldoet tijdelijk toch in de milieuzone mag rijden. Ontheffingen worden verstrekt voor uitzonderingssituaties, bijvoorbeeld voor campers van inwoners (wettelijke vrijstelling) of specifieke voertuigcategorieën.

Dit BO is een specialisatie van [[Vergunningen en ontheffingen]], het domeinoverstijgende parent BO voor alle gemeentelijke vergunningen en ontheffingen.

## GGM-bron

Geen directe GGM-entiteit voor milieuzone-ontheffingen. Het GGM bevat:
- **VOMAanvraagOfMelding** (Model VTH) — generiek concept voor vergunningen, ontheffingen en meldingen
- **Ligplaatsontheffing** (Model VTH) — vergelijkbaar specialisatiepatroon voor een ander domein
- **Ontheffing** (Model Inburgering, Model Werk) — domeinspecifieke ontheffingen elders

## Procesbron

Beschreven in [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025|Beleidsnota Luchtkwaliteit – Gezonde lucht voor iedereen 2025-2030]].

> "(extra) ontheffingen voor bepaalde voertuigen"
> (bron: Beleidsnota Luchtkwaliteit, paragraaf 6.2.7)

## Relaties

| Gerelateerd BO | Type | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| [[Vergunningen en ontheffingen]] | generalisatie | ↑ | Specialisatie | — |
| [[Milieuzone]] | associatie | van-dit-BO | Ontheffing geldt voor een specifieke zone | Beleidsnota §6.2.7 |


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025]]

## Terugmelding GGM

**Ontheffing (milieuzone) ontbreekt in GGM.** Het GGM kent geen entiteit voor milieuzone-ontheffingen. Het generieke hiaat (ontbreken van een overkoepelend vergunnings-/ontheffingsconcept) is vastgelegd bij [[Vergunningen en ontheffingen]]. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
