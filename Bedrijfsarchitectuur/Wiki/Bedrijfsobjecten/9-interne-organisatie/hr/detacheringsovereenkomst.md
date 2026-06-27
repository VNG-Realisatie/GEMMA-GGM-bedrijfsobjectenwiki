---
type: bedrijfsobject
naam: Detacheringsovereenkomst
domein: [Arbeidszaken]
archimate_type: contract
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

bo_definitie: "Overeenkomst tussen een uitlenende en inlenende organisatie voor het tijdelijk ter beschikking stellen van een werknemer."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Detacheringsovereenkomst betreft een werknemer"
  - type: associatie
    bedrijfsobject: "[[Dienstverband]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Werknemer behoudt dienstverband bij uitlener"
bedrijfsprocessen: [Personeelsuitwisseling, Inhuur en detachering]
bedrijfsfuncties: [Personeelsbeheer, Intergemeentelijke samenwerking]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal instrument bij intergemeentelijke personele samenwerking |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip in HR bij overheidsorganisaties |
| Heeft eigen bestaan binnen het domein | ✅ Aparte overeenkomst naast het dienstverband |
| Kan in meervoud bestaan | ✅ Meerdere per gemeente |
| Heeft eigen levenscyclus | ✅ Sluiten → verlengen → beëindigen |
| Heeft relaties met andere concepten | ✅ Werknemer, Dienstverband, uitlener, inlener |

Score: **6/6**

## Beschrijving

De detacheringsovereenkomst is een contract tussen een uitlenende en inlenende organisatie (doorgaans gemeenten onderling) voor het tijdelijk ter beschikking stellen van een werknemer. De werknemer behoudt zijn dienstverband bij de uitlener. De overeenkomst regelt de werkzaamheden, duur, vergoeding (meestal brutoloonkosten, max 5% opslag voor btw-vrijstelling), ziektebegeleiding en beëindiging.

Bijzondere vormen: detachering in het kader van re-integratie (tweede spoor) en detachering voor loopbaanontwikkeling.

Bij collegiale uitlening zonder winstoogmerk is de Waadi niet van toepassing (art. 1, lid 3 sub c), wat betekent dat de inlenersbeloning niet wettelijk verplicht is.

## Procesbron

Dit BO komt voort uit het proces van intergemeentelijke personeelsuitwisseling. De [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet|Handreiking flexibele arbeidsinzet]] beschrijft uitgebreid de juridische kaders en bevat een model-detacheringsovereenkomst.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Betreft [[Werknemer]] | van dit BO | 1 | Handreiking |
| Werknemer behoudt [[Dienstverband]] bij uitlener | van dit BO | 1 | Handreiking |

## Terugmelding GGM

**Detacheringsovereenkomst** — Niet gemodelleerd in GGM. Relevant data-object bij intergemeentelijke samenwerking met eigen attributen (partijen, duur, vergoedingsmodel, re-integratie/loopbaanontwikkeling). Past in beleidsdomein HR, taakveld 9. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
