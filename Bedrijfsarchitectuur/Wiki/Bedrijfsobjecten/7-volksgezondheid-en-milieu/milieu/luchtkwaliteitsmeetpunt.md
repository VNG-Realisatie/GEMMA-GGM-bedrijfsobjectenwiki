---
type: bedrijfsobject
naam: Luchtkwaliteitsmeetpunt
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

bo_definitie: "Fysieke locatie in het gemeentelijk meetnet waar luchtverontreinigende stoffen worden gemeten."
bo_toelichting: ''
bo_subtypes:
bo_relaties: []
bedrijfsprocessen: [luchtkwaliteitsmonitoring, beleidsverantwoording]
bedrijfsfuncties: [milieubeheer]
---

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel voor monitoring en beleidsverantwoording |
| Is herkenbaar voor domeinexperts | ✅ | "64 meetlocaties" worden als concreet ding benoemd |
| Heeft een eigen bestaan | ✅ | Fysiek meetpunt op een specifieke locatie |
| Kan in meervoud bestaan | ✅ | 64 gemeentelijke + 3 RIVM-meetpunten |
| Heeft een eigen levenscyclus | ✅ | Installeren → kalibreren → meten → onderhouden → verplaatsen/verwijderen |
| Heeft relaties met andere concepten | ✅ | Met locatie, stoffen (NO2, PM), meetreeksen |

Score: **6/6** — BO.

## Beschrijving

Een luchtkwaliteitsmeetpunt is een fysieke locatie in het gemeentelijk meetnet waar concentraties van luchtverontreinigende stoffen worden gemeten. Utrecht heeft 64 eigen meetlocaties voor NO2 en gebruikt daarnaast 3 RIVM-meetstations. De meetdata worden gepubliceerd in de jaarlijkse Monitoringsrapportage Luchtkwaliteit en vormen de basis voor beleidsverantwoording.

Vergelijkbaar met [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondwatermeetpunt|Grondwatermeetpunt]] qua opzet: fysiek punt met meetreeksen, locatie en beheerder.

## GGM-bron

Geen GGM-entiteit. Het GGM bevat wel **Sensor** en **Verkeerstelling** (Model Mobiliteit) als gerelateerde meetconcepten, maar niet specifiek voor luchtkwaliteit.

## Procesbron

Beschreven in [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025|Beleidsnota Luchtkwaliteit – Gezonde lucht voor iedereen 2025-2030]].

> "Met 64 Utrechtse meetlocaties voor NO2 en 3 meetlocaties van het RIVM binnen de stad hebben we adequate instrumenten om de luchtkwaliteit over de hele stad in kaart te brengen."
> (bron: Beleidsnota Luchtkwaliteit, hoofdstuk 8)


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-luchtkwaliteit-2025]]

## Terugmelding GGM

**Luchtkwaliteitsmeetpunt** — Registratieobject voor fysieke meetlocaties met type meting, locatie en meetreeksen. Vergelijkbaar met Verkeerstelling (Mobiliteit) qua opzet maar voor een ander domein. Zou onder een nieuw beleidsdomein Luchtkwaliteit (taakveld 7) of als generiek Meetpunt kunnen. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
