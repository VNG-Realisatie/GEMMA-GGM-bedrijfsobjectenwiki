---
type: element
naam: Lijkschouw
onderwerp: [openbare gezondheid]
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

ggm_duplicaat_entiteiten: []

bo_definitie: "Onderzoek van een lijk door de behandelende arts of de gemeentelijke lijkschouwer naar de doodsoorzaak, resulterend in een verklaring van overlijden of een verslag aan de officier van justitie."
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon|Natuurlijk Persoon]]"
    richting: van-dit-BO
    kardinaliteit: "1 → 1"
    beschrijving: "De overledene op wie de schouwing betrekking heeft"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/verlof-tot-begraving-of-crematie|Verlof tot begraving of crematie]]"
    richting: van-dit-BO
    kardinaliteit: "1 → 1"
    beschrijving: "De verklaring van overlijden uit de lijkschouw is voorwaarde voor het verlof"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| # | Criterium | Toepassing |
|---|---|---|
| 1 | Betekenis binnen onderwerp | Verplichte stap voorafgaand aan elke begraving of crematie |
| 2 | Herkenbaar voor domeinexperts | Standaardbegrip bij burgerzaken, artsen en forensische geneeskunde |
| 3 | Eigen bestaan | Elke schouwing is een zelfstandig geval met eigen formulieren en registratienummer |
| 4 | Meervoud | Bij elk overlijden in de gemeente |
| 5 | Eigen levenscyclus | Schouwing → verklaring van overlijden (natuurlijke dood) of melding aan officier van justitie/regionale toetsingscommissie (niet-natuurlijk of bijzonder geval) → eventueel nader onderzoek |
| 6 | Relaties | Overledene, behandelende arts of gemeentelijke lijkschouwer, officier van justitie, ambtenaar burgerlijke stand, CBS (doodsoorzaakstatistiek) |

Score: 6/6.

## Beschrijving

Lijkschouwing geschiedt zo spoedig mogelijk na het overlijden, door de behandelende arts of door een gemeentelijke lijkschouwer (art. 3 Wlb). Is de schouwer overtuigd van een natuurlijke doodsoorzaak, dan geeft deze een verklaring van overlijden af (art. 7 lid 1). In een aantal gevallen volgt een afwijkende procedure:

- **levensbeëindiging op verzoek of hulp bij zelfdoding** — de behandelende arts geeft geen verklaring van overlijden af, maar meldt de zaak aan de gemeentelijke lijkschouwer, die op zijn beurt verslag uitbrengt aan de regionale toetsingscommissie (art. 7 lid 2, art. 10 lid 2);
- **twijfel over de doodsoorzaak** — de schouwer brengt verslag uit aan de officier van justitie en waarschuwt de ambtenaar van de burgerlijke stand (art. 10 lid 1);
- **overleden minderjarige** — extra overlegverplichting tussen behandelende arts en gemeentelijke lijkschouwer, met mogelijkheid tot nader onderzoek door de lijkschouwer (art. 10a).

Na afgifte van de verklaring van overlijden doet de schouwer opgave van de doodsoorzaak aan het Centraal Bureau voor de Statistiek (art. 12a) — deze doodsoorzaakstatistiek staat los van de verklaring van overlijden zelf en bevat medisch-inhoudelijke informatie. De stukken worden bij de akte van overlijden gevoegd (art. 13).

De lijkschouw is een activiteit van de [[Wiki/Rollen/gemeentelijk-lijkschouwer|gemeentelijk lijkschouwer]] (of de behandelende arts), maar het resultaat — de verklaring van overlijden of het verslag aan de officier van justitie — is een zelfstandig, in het proces geproduceerd document met eigen vervolgstappen. Vergelijkbaar met hoe [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/infectieziektemelding|Infectieziektemelding]] is vastgelegd: het schouwingsproces zelf blijft buiten scope, het resulterende object wordt vastgelegd.

## Juridische bron

Wettelijke basis: Wet op de lijkbezorging, hoofdstuk II § 1 (art. 3-10a). Zie [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst|Wet op de lijkbezorging — volledige wettekst]].

## Relaties

| Gerelateerd object | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]] | overledene | → | 1 → 1 | Art. 2-3 Wlb |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/verlof-tot-begraving-of-crematie\|Verlof tot begraving of crematie]] | voorwaarde voor | → | 1 → 1 | Art. 12 Wlb |

## Bronnen

- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst]]

## Terugmelding GGM

GGM-hiaat: het GGM kent OverlijdenIngeschrevenPersoon (BRP-domein, overlijdensfeit als attribuut van de persoon) maar geen entiteit voor het lijkschouwproces zelf — de verklaring van overlijden, de melding aan de officier van justitie en de doodsoorzaakopgave aan het CBS. Zie #122 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
