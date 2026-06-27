---
type: bedrijfsobject
naam: Marktconsultatie
onderwerp: [inkoop]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
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

ggm_duplicaat_entiteiten: []

bo_definitie: "Voorbereidend onderzoek waarmee de gemeente de markt verkent voorafgaand aan een mogelijke aanbesteding."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Aanbesteding]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "kan leiden tot"
bedrijfsprocessen: [Inkopen]
bedrijfsfuncties: [Inkoopfunctie]
---

## BO-criteria toetsing

1. **Heeft betekenis binnen het onderwerp** — ja, voorbereidend instrument in het inkoopproces
2. **Is herkenbaar voor domeinexperts** — ja, inkopers en beleidsmedewerkers kennen marktconsultaties
3. **Heeft een eigen bestaan** — ja, kan plaatsvinden zonder dat er een aanbesteding volgt (no-go)
4. **Kan in meervoud bestaan** — ja, gemeente voert meerdere marktconsultaties per jaar uit
5. **Heeft een eigen levenscyclus** — ja: voorbereiding → aankondiging (TenderNed) → uitvoering → resultaat (go/no-go)
6. **Heeft relaties met andere concepten** — ja: Aanbesteding, Leverancier (deelnemers)

Score: 6/6

## Beschrijving

Een marktconsultatie is een voorbereidend instrument waarmee de gemeente de markt verkent voordat zij besluit een aanbesteding te starten. Het doel is inzicht te krijgen in beschikbare oplossingen (waaronder duurzame en innovatieve opties), marktomstandigheden, machtsverhoudingen en de haalbaarheid van randvoorwaarden.

De marktconsultatie staat los van de aanbestedingsprocedure: het resultaat kan leiden tot een aanbesteding maar ook tot een no-go (de markt kan niet leveren, de kosten zijn te hoog, of de behoefte wordt anders ingevuld). Marktconsultaties kunnen worden aangekondigd op TenderNed of de gemeentelijke website.

## Procesbron

Alle drie de bronnen beschrijven marktconsultatie als losstaand voorbereidend instrument:

> "Een marktconsultatie is een instrument dat de gemeente kan inzetten voor het verkrijgen van deze kennis. De gemeente kan onderzoeken welke duurzame en innovatieve oplossingen beschikbaar zijn op de markt." (bron: vng-model-inkoop-en-aanbestedingsbeleid)

> "Een productanalyse leidt tot inzicht in de aard van het 'product' en de relevante markt(vorm). Een marktanalyse leidt tot het inzicht in de relevante markt(vorm), de Ondernemers die daarop opereren en hoe de markt- en mogelijke machtsverhoudingen zijn." (bron: inkoop-aanbestedingsbeleid-over-gemeenten)

Zie [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid|Inkoop- en aanbestedingsbeleid]].

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Aanbesteding\|Aanbesteding]] | kan leiden tot | → | 0..1 | bronnen |

## Bedrijfsprocessen

- **Inkopen** — voortraject: product- en marktanalyse

## Bedrijfsfuncties

- **Inkoopfunctie** — marktverkenning en haalbaarheidstoets

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]

## Terugmelding GGM

Marktconsultatie ontbreekt als entiteit in het GGM beleidsdomein Inkoop. Het is een voorbereidend procesobject dat in de praktijk wordt geregistreerd (aankondiging op TenderNed, verslag, deelnemerslijst) en een eigen uitkomst heeft (go/no-go). Past als objecttype in het Inkoop-beleidsdomein, gerelateerd aan Aanbesteding.

Teruggemeld als #81 in [[Wiki/Analyses/ggm-terugmeldingen]].
