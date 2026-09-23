---
type: element
naam: Subsidiebeschikking
onderwerp: [recht]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Subsidiebeschikking
ggm_guid: EAID_F8BD6D83_D3F8_4dd3_B12E_22A991D1A0A2
ggm_uml_type: Class
ggm_beleidsdomein: Subsidies
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Subsidies]
ggm_diagram_ids: [EAID_F408BDED_51D4_4204_9B95_F0C6C2474DC3]
ggm_definitie: "Besluit over het al dan niet toekennen van een subsidie"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Subsidiebeschikking
ggm_gemma_guid: "0cbc6488-2932-4634-b226-a741ba030a46"
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-0cbc6488-2932-4634-b226-a741ba030a46"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Subsidiebeschikking** als directe tegenhanger.
bo_definitie: "Besluit over het al dan niet toekennen van een subsidie."
bo_toelichting:
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidie|Subsidie]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "besluit dat de subsidie toekent of afwijst"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidieaanvraag|Subsidieaanvraag]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "volgt op de beoordeling van de aanvraag"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Het formele besluit dat een subsidieproces afsluit of vervolgt |
| Is herkenbaar voor domeinexperts | ✅ Kernbegrip uit de Awb-beschikkingssystematiek, toegepast op subsidies |
| Heeft een eigen bestaan | ✅ Bestaat als zelfstandig besluit-document, met eigen kenmerk/beschikkingsnummer |
| Kan in meervoud bestaan | ✅ Elke aanvraag kan tot een eigen beschikking leiden; ook wijzigings- en vaststellingsbeschikkingen zijn mogelijk |
| Heeft een eigen levenscyclus | ✅ Opgesteld → verzonden → onherroepelijk of aangevochten (bezwaar/beroep) |
| Heeft relaties met andere concepten | ✅ Met Subsidieaanvraag en Subsidie |

Score: 6/6

## Beschrijving

De subsidiebeschikking is het besluit waarmee de gemeente een subsidieaanvraag toe- of afwijst. Volgens de bron kan een niet volgens de subsidieregels berekende (bijvoorbeeld incomplete) aanvraag tot afwijzing leiden — de beschikking is daarmee de formele uitkomst van de beoordeling die op de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidieaanvraag|Subsidieaanvraag]] volgt.

De GGM-naam "Beschikking" komt ook voor als generieke bestuursrechtelijke entiteit in de beleidsdomeinen Generiek Jeugd en Wmo en Diensten (zie [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]). Dit is geen duplicaat: het zijn twee apart gemodelleerde GGM-entiteiten zonder generalisatierelatie, elk met een eigen scope. Omdat de BO-naam hier al "Subsidiebeschikking" is (niet kaal "Beschikking"), is er geen naamcollisie en geen disambiguatie nodig.

## GGM-bron

> "Besluit over het al dan niet toekennen van een subsidie."
> — GGM, entiteit *Subsidiebeschikking*, beleidsdomein Subsidies (taakveld 9 Interne Organisatie)

**Matchsterkte:** exact.

**Attributen (GGM):** beschiktBedrag, ontvangen, kenmerk, internKenmerk, besluit, beschikkingsnummer, opmerkingen.

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidie\|Subsidie]] | besluit dat de subsidie toekent of afwijst | Subsidiebeschikking → Subsidie | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidieaanvraag\|Subsidieaanvraag]] | volgt op de beoordeling van | Subsidieaanvraag → Subsidiebeschikking | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Recht/subsidierecht]]
