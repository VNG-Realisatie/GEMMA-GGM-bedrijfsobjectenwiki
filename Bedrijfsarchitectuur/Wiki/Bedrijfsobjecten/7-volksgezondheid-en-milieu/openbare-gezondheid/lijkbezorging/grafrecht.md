---
type: element
naam: Grafrecht
onderwerp: [openbare gezondheid]
archimate_type: business-object
grondslag: governance-object

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

ggm_duplicaat_entiteiten: []

bo_definitie: "Uitsluitend recht op een particulier graf, waarbij de rechthebbende bepaalt wie erin wordt begraven; schriftelijk gevestigd voor onbepaalde tijd of ten minste tien jaar."
bo_toelichting: "Geen registergoed (art. 28 lid 1 Wlb) — nadrukkelijk geen zakelijk recht in de zin van het Burgerlijk Wetboek/de Basisregistratie Kadaster, ondanks de gelijkenis in naam."
bo_subtypes: []
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/begraafplaats|Begraafplaats]]"
    richting: van-dit-BO
    kardinaliteit: "0..* → 1"
    beschrijving: "Het grafrecht rust op een graf op een specifieke begraafplaats"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon|Natuurlijk Persoon]]"
    richting: van-dit-BO
    kardinaliteit: "0..* → 1"
    beschrijving: "De rechthebbende op het grafrecht"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| # | Criterium | Toepassing |
|---|---|---|
| 1 | Betekenis binnen onderwerp | Kernbegrip van begraafplaatsbeheer; bepaalt zeggenschap over een graf |
| 2 | Herkenbaar voor domeinexperts | Standaardterm bij begraafplaatsbeheerders en burgerzaken |
| 3 | Eigen bestaan | Bestaat los van het fysieke graf — kan worden gevestigd, overgedragen, verlengd of vervallen onafhankelijk van de grafinhoud |
| 4 | Meervoud | Duizenden particuliere grafrechten per gemeente |
| 5 | Eigen levenscyclus | Vestiging → (herhaalde) verlenging → kennisgeving bij verstrijken termijn → verval bij verwaarlozing of einde termijn |
| 6 | Relaties | Graf/begraafplaats, rechthebbende (natuurlijk of rechtspersoon) |

Score: 6/6.

## Beschrijving

Begraving geschiedt in een algemeen graf — waarbij de houder van de begraafplaats bepaalt wie erin wordt begraven — of in een particulier graf, waarop een **uitsluitend recht** rust: de rechthebbende bepaalt wie daarin wordt begraven (art. 23 lid 2 Wlb). Dit uitsluitend recht — het grafrecht — kan alleen schriftelijk worden gevestigd, voor onbepaalde tijd of voor een bepaalde tijd van ten minste tien jaar (art. 28 lid 1). Een recht voor bepaalde tijd wordt op tijdig verzoek telkens verlengd, met een door de houder van de begraafplaats te bepalen verlengingsperiode van vijf tot twintig jaar.

De wet legt de houder van de begraafplaats specifieke informatieplichten op: uiterlijk een jaar voor het verstrijken van de termijn een schriftelijke mededeling aan de rechthebbende (art. 28 lid 2), en bij verwaarloosd onderhoud een vastgelegde procedure van schriftelijke waarschuwing en — bij uitblijven van reactie — bekendmaking bij het graf, voordat het recht na maximaal vijf jaar (of, bij een recht van nog geen tien jaar oud, na tien jaar) vervalt (art. 28 lid 4-7).

Nadrukkelijk **geen registergoed**: het grafrecht is uitgezonderd van het generieke zakelijke-rechtenstelsel van het Burgerlijk Wetboek en de Basisregistratie Kadaster (BRK) — het bestaande BO [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht|Zakelijk Recht]] is dus geen match, ook geen generalisatie.

## Juridische bron

Wettelijke basis: Wet op de lijkbezorging, art. 23, 27a en 28. Zie [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst|Wet op de lijkbezorging — volledige wettekst]].

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/begraafplaats\|Begraafplaats]] | compositie | → | 0..* → 1 | Art. 23, 28 Wlb |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]] | associatie | → | 0..* → 1 | Art. 28 Wlb (rechthebbende) |

## Bronnen

- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst]]

## Terugmelding GGM

GGM-hiaat: geen GGM-entiteit voor het grafrecht. Expliciet géén zakelijk recht (art. 28 lid 1 Wlb sluit registergoed-status uit), dus geen aansluiting bij het bestaande BRK-domein. Zie #120 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
