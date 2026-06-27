---
type: bedrijfsobject
naam: Terras
domein: [Economie]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
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
bo_definitie: "Tijdelijk gebruik van openbare ruimte door een horecabedrijf voor het plaatsen van tafels en stoelen, gereguleerd via de beleidsregel terrassen."
bo_toelichting: ''
bedrijfsprocessen: [terrasvergunningverlening, handhaving terrassen]
bedrijfsfuncties: [vergunningverlening, handhaving, beheer openbare ruimte]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Horecabedrijf]]"
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Een terras hoort bij een horecabedrijf
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Apart gereguleerd via beleidsregel terrassen |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip voor vergunningverleners en horecaondernemers |
| Heeft een eigen bestaan | ✅ | Fysieke locatie in openbare ruimte met eigen afmetingen en regels |
| Kan in meervoud bestaan | ✅ | Honderden terrassen in een gemeente |
| Heeft een eigen levenscyclus | ✅ | Vergunning → seizoensopenstelling → dagelijks opbouwen/afbreken |
| Heeft relaties met andere concepten | ✅ | Horecabedrijf, openbare ruimte, vergunning |

6/6 criteria — BO.

## Beschrijving

Een terras is het tijdelijk gebruik van openbare ruimte door een horecabedrijf voor het plaatsen van tafels en stoelen. De grond blijft eigendom van de gemeente. De beleidsregel terrassen regelt locatie (vrije doorgang, loopruimte, maximale breedte), inrichting (geen vast meubilair, geen versterkt geluid) en gebruik (opruimen na sluiting, verlengde openingstijden bij warm weer).

Het terras mag niet breder zijn dan de gevel van het horecabedrijf en direct zicht vanuit het bedrijf is verplicht.

## Procesbron

Het terras ontstaat uit het vergunningproces voor horecaexploitatie in de openbare ruimte. De beleidsregel terrassen (2024) is de juridische grondslag, vastgesteld op basis van de Verordening horeca gemeente Utrecht.

> "Gebruik van openbare ruimte is tijdelijk gebruik. De grond blijft eigendom van de gemeente." — [[Wiki/Bronsamenvattingen/Economie/beleidsregels-terrassen-utrecht|Beleidsregel Terrassen Gemeente Utrecht]]

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Horecabedrijf]] | associatie | Horecabedrijf → Terras | 1 | Beleidsregel terrassen |


## Bronnen

- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-terrassen-utrecht]]

## Terugmelding GGM

**Terras** — Registratieobject voor tijdelijk gebruik van openbare ruimte door horecabedrijven (locatie, afmetingen, openingstijden, inrichting). Dataobject met concrete registreerbare eigenschappen. Zou onder taakveld 3 Economie kunnen, of onder taakveld 8 (Beheer Openbare Ruimte) gezien de ruimtelijke component.
