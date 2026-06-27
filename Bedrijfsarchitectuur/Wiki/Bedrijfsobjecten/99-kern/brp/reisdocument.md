---
type: bedrijfsobject
naam: Reisdocument
onderwerp: [Basisregistraties, BRP]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Reisdocument
ggm_guid: EAID_CA9BC1BB_D572_4e47_BECF_17CFD379BD6A
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Burgerzaken, REISDOCUMENT]
ggm_diagram_ids: []
ggm_definitie: "Een document dat vereist is voor reizen naar het buitenland"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GGM"

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

bo_definitie: "Een document dat vereist is voor reizen naar het buitenland"
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Ingeschreven Persoon]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Verstrekt aan persoon (BRP categorie 12)"
bedrijfsprocessen: [Aanvraag reisdocument, Uitgifte reisdocument, Inhouding/vermissing reisdocument]
bedrijfsfuncties: [Burgerzakenloket, Bevolkingsadministratie]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in dagelijks werk | ✅ | Aanvraag en uitgifte paspoort/ID-kaart is een veelvoorkomend burgerzakenproces |
| Eigenaar/houder | ✅ | Gemeente geeft uit en registreert in BRP |
| Levenscyclus | ✅ | Uitgifte → geldig → verlopen/ingehouden/vermist; na bewaartermijn verwijderd van PL |
| Meervoudig | ✅ | Een persoon kan meerdere reisdocumenten hebben (cat. 12 is 0,n) |
| Gegevens | ✅ | Soort, documentnummer, datum uitgifte, autoriteit, geldigheidsperiode, inhouding/vermissing |
| Relaties met andere BO's | ✅ | [[Ingeschreven Persoon]] (houder) |

## Beschrijving

Een Reisdocument is een Nederlands paspoort of Nederlandse identiteitskaart dat door de gemeente wordt uitgegeven en geregistreerd in de BRP. BRP-categorie 12 bevat per document: het soort document, documentnummer, datum uitgifte, autoriteit van afgifte, geldigheidsperiode en eventuele inhouding of vermissing.

Een persoon kan meerdere reisdocumenten tegelijk bezitten (bijv. een paspoort en een ID-kaart). Vervallen documenten worden na een vastgestelde bewaartermijn van de PL verwijderd. De BRP kent ook de signalering van reisdocumenten (groep 36): een melding dat een document als vervallen of gestolen is geregistreerd.

## GGM-bron

> "Een document dat vereist is voor reizen naar het buitenland"

- **GGM-entiteit:** Reisdocument
- **Beleidsdomein:** RSGBPlus
- **Attributen (8):** soort, reisdocumentnummer, datumUitgifte, autoriteitVanAfgifte, datumIngangDocument, datumEindeGeldigheidDocument, datumInhoudingOfVermissing, aanduidingInhoudingVermissing
- **Matchsterkte:** exact — 1:1 match met BRP-categorie 12

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | ← | 0..* | Verstrekt aan persoon | GGM/BRP cat. 12 |

## Bedrijfsprocessen

- Aanvraag reisdocument (burger doet aanvraag bij burgerzakenloket)
- Uitgifte reisdocument (productie en verstrekking)
- Inhouding of vermissing (registratie op PL, signalering)
- Verwijdering vervallen documenten (na bewaartermijn)

## Terugmelding GGM

De GGM-definitie "Een document dat vereist is voor reizen naar het buitenland" dekt niet de Nederlandse identiteitskaart, die in de BRP ook als reisdocument wordt geregistreerd maar primair dient als identiteitsbewijs. Suggestie: "Een door de overheid uitgegeven identiteits- of reisdocument."

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1]]
