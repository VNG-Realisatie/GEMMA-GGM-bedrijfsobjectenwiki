---
type: bedrijfsobject
naam: Milieuzone
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

gemma_definitie: "Afgebakend gebied waarbinnen toegangsbeperkingen gelden voor voertuigen op basis van emissieklasse en brandstofsoort, ingesteld ter verbetering van de luchtkwaliteit."
gemma_subtypes:
  - naam: Nul-emissiezone
    omschrijving: "Zone waarbinnen uitsluitend uitstootvrije voertuigen zijn toegelaten"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bronnen: [Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025]
  - "[[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025]]"
relaties:
  - type: associatie
    bedrijfsobject: "[[Ontheffing (milieuzone)]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een milieuzone kan ontheffingen hebben voor specifieke voertuigen"
  - type: associatie
    bedrijfsobject: "[[Sloopregeling]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Bij aanscherping of uitbreiding wordt een sloopregeling aangeboden"
bedrijfsprocessen: [verkeersregulering, milieuhandhaving, luchtkwaliteitsbeleid]
bedrijfsfuncties: [milieubeheer, verkeersbeheer]
---

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal instrument in luchtkwaliteitsbeleid |
| Is herkenbaar voor domeinexperts | ✅ | Ambtenaren en inwoners spreken over "de milieuzone" |
| Heeft een eigen bestaan | ✅ | Zelfstandig afgebakend gebied met eigen regels |
| Kan in meervoud bestaan | ✅ | Meerdere zones: diesel personenauto, vracht/bus, brom/snor, nul-emissie bestel/vracht |
| Heeft een eigen levenscyclus | ✅ | Instellen → uitbreiden → aanscherpen → opheffen |
| Heeft relaties met andere concepten | ✅ | Met ontheffing, sloopregeling, verkeersbesluit, voertuigcategorie |

Score: **6/6** — BO.

## Beschrijving

Een milieuzone is een door de gemeente ingesteld gebied waarbinnen voertuigen die niet aan bepaalde emissienormen voldoen niet mogen rijden. De gemeente Utrecht kent meerdere milieuzones voor verschillende voertuigcategorieën (personenauto's, bestelauto's, vrachtauto's, autobussen, brom- en snorfietsen), elk met eigen emissieklasse-eisen en invoerdata.

De zones worden juridisch ingesteld via verkeersbesluiten en vastgelegd in de APV. Handhaving vindt plaats via een cameranetwerk.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Nul-emissiezone | Zone waarbinnen uitsluitend uitstootvrije voertuigen zijn toegelaten. Strenger dan een milieuzone met emissieklasse-eisen. | — |

Utrecht heeft een nul-emissiezone voor bestel- en vrachtauto's (ingevoerd 2025 in het huidige milieuzonegebied, uitbreiding naar heel Utrecht gepland 2030) en streeft naar een nul-emissiezone voor brom- en snorfietsen (2030).

## GGM-bron

Geen GGM-entiteit. Het GGM bevat wel **Parkeerzone** (Model Parkeren) als vergelijkbaar zoneconcept en **Verkeersbesluit** (Model Mobiliteit) als juridische grondslag waarmee milieuzones worden ingesteld.

## Procesbron

De milieuzone ontstaat uit het luchtkwaliteitsbeleid en wordt juridisch geformaliseerd via een verkeersbesluit. Beschreven in [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025|Beleidsnota Luchtkwaliteit 2025-2030]].

> "We breiden de milieuzone vanaf 2027 geografisch uit naar de gemeentegrenzen van Utrecht, voor de volgende voertuigen op diesel: personenauto's en bestelauto's tot en met emissieklasse 4, en de milieuzone voor vrachtauto's en autobussen tot en met emissieklasse 5."
> (bron: Beleidsnota Luchtkwaliteit, paragraaf 6.2.3)

## Relaties

| Gerelateerd BO | Type | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| [[Ontheffing (milieuzone)]] | associatie | naar-dit-BO | Individuele uitzonderingen op zone-regels | Beleidsnota §6.2.7 |
| [[Sloopregeling]] | associatie | naar-dit-BO | Subsidieregeling bij aanscherping | Beleidsnota §6.2.7 |

## Terugmelding GGM

**Milieuzone** — Dataobject voor het afgebakend gebied met emissieklasse-eisen per voertuigcategorie. Vergelijkbaar met Parkeerzone (Model Parkeren) maar gericht op luchtkwaliteit in plaats van parkeerregulering. Zou onder Mobiliteit (taakveld 2) of een nieuw beleidsdomein Luchtkwaliteit (taakveld 7) kunnen. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
