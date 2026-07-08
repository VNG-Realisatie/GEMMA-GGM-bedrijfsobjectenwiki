---
type: element
naam: Sloopregeling
domein: [milieu]
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

bo_definitie: "Subsidieregeling waarmee inwoners een financiële bijdrage krijgen voor het vervangen van een voertuig dat door milieuzone-aanscherping niet meer is toegelaten."
bo_toelichting: ''
bo_subtypes:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Milieuzone]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een sloopregeling wordt gekoppeld aan een milieuzone-aanscherping"
bedrijfsprocessen: [subsidiebeheer, luchtkwaliteitsbeleid]
bedrijfsfuncties: [milieubeheer, financieel-beheer]
---

⚠️ **Ter discussie** — Begripstype is *instrument*. Voldoet aan 6/6 BO-criteria maar is functioneel een subsidieregeling. Relatie met het generieke GGM-domein Subsidies (Subsidie, Subsidieaanvraag, Subsidiebeschikking) moet worden onderzocht.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel flankerend beleid bij milieuzones |
| Is herkenbaar voor domeinexperts | ✅ | Ambtenaren en inwoners kennen de sloopregeling |
| Heeft een eigen bestaan | ✅ | Zelfstandige regeling met eigen budget en voorwaarden |
| Kan in meervoud bestaan | ✅ | Meerdere regelingen: milieuzone, brom/snor, toekomstige aanscherpingen |
| Heeft een eigen levenscyclus | ✅ | Openstellen → aanvragen → toekennen → uitbetalen → afsluiten |
| Heeft relaties met andere concepten | ✅ | Met milieuzone, voertuig, budget, inwoner |

Score: **6/6** — BO, maar begripstype *instrument* → voorgelegd aan team.

## Beschrijving

Een sloopregeling is een gemeentelijke subsidieregeling die inwoners een financiële bijdrage biedt voor het vervangen van een voertuig dat door aanscherping of uitbreiding van de milieuzone niet meer is toegelaten. De regeling wordt uiterlijk 6 maanden voor de aanscherping opengesteld.

Utrecht heeft eerder een sloopsubsidie aangeboden bij invoering van de groene milieuzone (2021). Bij de uitbreiding naar heel Utrecht (2027) wordt opnieuw een sloopregeling aangeboden. De subsidiebedragen en voorwaarden kunnen variëren naar inkomensklasse en voertuigleeftijd.

Functioneel is de sloopregeling een specialisatie van het generieke subsidieconcept uit het GGM (Model Subsidies: Subsidie, Subsidieaanvraag, Subsidiebeschikking).

## GGM-bron

Geen directe GGM-entiteit. Het GGM bevat onder Model Subsidies (taakveld 9):
- **Subsidie** — generiek subsidieconcept
- **Subsidieaanvraag** — aanvraagproces
- **Subsidiebeschikking** — besluit op aanvraag
- **Subsidieprogramma** — overkoepelend programma

De sloopregeling zou als een **Subsidieprogramma** met bijbehorende **Subsidieaanvragen** en **Subsidiebeschikkingen** gemodelleerd kunnen worden.

## Procesbron

Beschreven in [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025|Beleidsnota Luchtkwaliteit – Gezonde lucht voor iedereen 2025-2030]].

> "We bieden een sloopregeling aan voor inwoners met een personenauto die niet meer toegestaan is. Hiermee kunnen inwoners een financiële bijdrage krijgen van de gemeente voor het vervangen van een auto die niet meer is toegestaan in de milieuzone."
> (bron: Beleidsnota Luchtkwaliteit, paragraaf 6.2.3)

## Relaties

| Gerelateerd BO | Type | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| [[Milieuzone]] | associatie | van-dit-BO | Sloopregeling is gekoppeld aan milieuzone-aanscherping | Beleidsnota §6.2.3 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025]]
