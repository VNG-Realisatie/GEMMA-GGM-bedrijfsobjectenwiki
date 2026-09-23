---
type: element
naam: Verlof tot begraving of crematie
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

bo_definitie: "Schriftelijk, kosteloos document van de ambtenaar van de burgerlijke stand, zonder hetwelk geen begraving of crematie mag plaatsvinden."
bo_toelichting: "Geen vergunning in de zin van het bestaande BO Vergunningen en ontheffingen: er is geen discretionaire beoordeling — het verlof wordt kosteloos afgegeven zodra een verklaring van overlijden of een verklaring van geen bezwaar van de officier van justitie aanwezig is (art. 12 Wlb)."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/lijkschouw|Lijkschouw]]"
    richting: naar-dit-BO
    kardinaliteit: "1 → 1"
    beschrijving: "De verklaring van overlijden uit de lijkschouw is voorwaarde voor afgifte van het verlof"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon|Natuurlijk Persoon]]"
    richting: van-dit-BO
    kardinaliteit: "1 → 1"
    beschrijving: "De overledene op wie het verlof betrekking heeft"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| # | Criterium | Toepassing |
|---|---|---|
| 1 | Betekenis binnen onderwerp | Verplichte voorwaarde voor elke begraving of crematie |
| 2 | Herkenbaar voor domeinexperts | Standaardbegrip bij burgerzaken |
| 3 | Eigen bestaan | Zelfstandig document, los van de verklaring van overlijden waarop het is gebaseerd |
| 4 | Meervoud | Bij elke begraving of crematie |
| 5 | Eigen levenscyclus | Aangevraagd (door wie in de lijkbezorging voorziet) → afgegeven (kosteloos, binnen de wettelijke termijn) → gebruikt bij begraving/crematie |
| 6 | Relaties | Overledene, verklaring van overlijden, ambtenaar burgerlijke stand, officier van justitie (bij verklaring van geen bezwaar) |

Score: 6/6.

## Beschrijving

Geen begraving of crematie van een lijk geschiedt zonder schriftelijk verlof van de ambtenaar van de burgerlijke stand, dat kosteloos wordt afgegeven (art. 11 Wlb). Het verlof wordt alleen verleend als de ambtenaar beschikt over een verklaring van overlijden (afgegeven door de behandelende arts of een gemeentelijke lijkschouwer) óf een verklaring van geen bezwaar van de officier van justitie tegen begraving of crematie (art. 12). Begraving of crematie geschiedt niet eerder dan 36 uur en niet later dan de zesde werkdag na het overlijden (art. 16); de burgemeester kan hiervan afwijken (art. 17).

Bevoegd zijn de officier van justitie en de ambtenaar van de burgerlijke stand van de plaats waar de overlijdensakte is ingeschreven, of — bij ontbreken van een akte — van de plaats van begraving of crematie (art. 14).

**Geen vergunning:** in tegenstelling tot het bestaande, overkoepelende BO [[Vergunningen en ontheffingen]] kent dit verlof geen discretionaire beoordeling. Het wordt kosteloos en (behoudens de in art. 12 genoemde uitzonderingen) automatisch afgegeven zodra de vereiste verklaring aanwezig is. Daarom is dit een eigen BO, geen specialisatie van Vergunningen en ontheffingen.

## Juridische bron

Wettelijke basis: Wet op de lijkbezorging, hoofdstuk II § 2-3 (art. 11-17). Zie [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst|Wet op de lijkbezorging — volledige wettekst]].

## Relaties

| Gerelateerd object | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/lijkschouw\|Lijkschouw]] | voorwaarde | ← | 1 → 1 | Art. 12 Wlb |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]] | overledene | → | 1 → 1 | Art. 11 Wlb |

## Bronnen

- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst]]

## Terugmelding GGM

GGM-hiaat: geen GGM-entiteit voor dit verlof. Ook geen aansluiting bij het generieke governance-object [[Vergunningen en ontheffingen]] (procesboverstijgend geen discretionaire beoordeling). Zie #123 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
