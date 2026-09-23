---
type: element
naam: Zwembad
onderwerp: [Sport en Bewegen]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein: "Sport"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
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
bo_definitie: "Gemeentelijke voorziening voor zwemactiviteiten, met eigen capaciteitsbeleid en meerjarige investeringsplanning."
bo_toelichting:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Sportlocatie]]"
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: "Zwembad is een specialisatie van Sportlocatie"
  - type: associatie
    bedrijfsobject: "[[Sportvereniging]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Zwemverenigingen gebruiken zwembaden"
bedrijfsprocessen: [Capaciteitsplanning zwembadwater, Diplomazwemmen, Exploitatie zwembaden, Groot onderhoud en vervanging]
bedrijfsfuncties: [Sportaccommodatiebeheer, Sportbeleid]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis (centraal in sportbeleid, eigen capaciteitsbeleid), herkenbaar (Máximapark, Den Hommel, De Kwakel), eigen bestaan (fysieke voorziening), meervoud (meerdere zwembaden in Utrecht), levenscyclus (bouw, exploitatie, renovatie, vervanging — Den Hommel 2032, De Kwakel 2036), relaties met [[Sportvereniging]], Wijk.

## Beschrijving

Een zwembad is een gemeentelijke voorziening voor zwemactiviteiten. De gemeente exploiteert zwembaden, beheert de zwembadwatercapaciteit en stuurt op personeelsbezetting. Bij de verdeling van capaciteit hebben diplomazwemmen voor kinderen en verenigingsactiviteiten voorrang. De druk op zwembaden is groot door een tekort aan zwembadwater en personeelstekorten.

Genoemde zwembaden in het beleid: Máximapark (nieuwbouw, uitgesteld naar 2029), Den Hommel (vervanging 2032), De Kwakel (renovatie 2036).

## GGM-bron

Geen GGM-match. Zwembad komt niet voor als entiteit in het GGM-beleidsdomein Sport.

- **Matchsterkte:** geen


## Bronnen

- [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032]]
- [[Wiki/Bronsamenvattingen/Sport en Bewegen/uitvoeringsprogramma-sport-en-bewegen-2025]]

## Terugmelding GGM

> **Zwembad** — Gemeentelijke voorziening voor zwemactiviteiten (diplomazwemmen, verenigingsactiviteiten, recreatief zwemmen). Heeft eigen capaciteitsbeleid (zwembadwatercapaciteit), personeelsbeheer en meerjarige investerings- en vervangingsplanning. Speelt dezelfde structurele rol als de al gemodelleerde specialisaties [[Binnenlocatie]] en [[Sportpark]] van [[Sportlocatie]] — geen aanwijsbaar verschil in autonomie of levenscyclus dat een zelfstandig objecttype rechtvaardigt. Voorgesteld als derde specialisatie van Sportlocatie in het GGM beleidsdomein Sport.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Sportlocatie]] | is specialisatie van | | GGM (voorgesteld, zie terugmelding) |
| [[Sportvereniging]] | wordt gebruikt door | 0..* | beleidsnota |
| Wijk | bedient | 1..* | beleidsnota |
