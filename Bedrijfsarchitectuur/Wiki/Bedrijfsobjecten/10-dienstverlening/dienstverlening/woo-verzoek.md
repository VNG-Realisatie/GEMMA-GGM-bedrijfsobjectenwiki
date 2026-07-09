---
type: element
naam: woo-verzoek
onderwerp: [informatiesamenleving, dienstverlening]
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

bo_definitie: "Verzoek van eenieder aan een bestuursorgaan om openbaarmaking van publieke informatie op grond van de Wet open overheid."
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[aanvraag-of-melding]]"
    richting: naar-dit-BO
    kardinaliteit:
    beschrijving: Woo-verzoek is een specialisatie van Aanvraag of Melding
  - type: associatie
    bedrijfsobject: "[[zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Woo-verzoek wordt behandeld als zaak
  - type: associatie
    bedrijfsobject: "[[document]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Woo-verzoek leidt tot verstrekking van documenten
bedrijfsprocessen: [Behandelen Woo-verzoek, Actieve openbaarmaking]
bedrijfsfuncties: [Informatievoorziening, Juridische zaken]
---

# Woo-verzoek

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — uniek verzoek met verzoeker, ontvangstdatum, aangelegenheid |
| Eigen attributen | Ja — beslistermijn, verdaging, uitzonderingsgronden, deelbesluiten, besluit, verstrekte documenten |
| Levenscyclus | Ja — ontvangst → precisering → zoekslag → beoordeling → besluit → verstrekking → actieve openbaarmaking |
| Gemeentelijk eigendom | Ja — gemeente is bestuursorgaan dat beslist |
| Wettelijke grondslag | Ja — Wet open overheid (art. 4.1) |
| Registratieverplichting | Ja — besluit en verstrekte informatie moeten actief openbaar (art. 3.3 lid 2 sub i), jaarlijkse verantwoording in begroting (art. 3.5) |

Score: 6/6 criteria.

## Beschrijving

Een Woo-verzoek is een verzoek van eenieder aan een bestuursorgaan om openbaarmaking van publieke informatie. De verzoeker hoeft geen belang te stellen. Het verzoek kan schriftelijk, mondeling of elektronisch worden ingediend.

De gemeente behandelt het verzoek als een zaak met vaste processtappen: ontvangstbevestiging, vaststellen bevoegd bestuursorgaan, eventuele precisering bij te algemene verzoeken, zoekslag naar relevante documenten, beoordeling per document tegen de uitzonderingsgronden, besluitvorming (geheel/gedeeltelijk openbaar of afwijzing), en verstrekking van de documenten.

De beslistermijn is vier weken, met mogelijkheid tot verdaging van twee weken. Bij omvangrijke verzoeken kan in deelbesluiten worden beslist. Het Woo-verzoek, het besluit en de verstrekte informatie moeten zelf ook actief openbaar worden gemaakt.

## Subtypes

Herkende specialisaties van Woo-verzoek. Geen apart BO.

- **Omvangrijk verzoek** — verzoek dat niet binnen de beslistermijn kan worden afgehandeld; vereist overleg met verzoeker over prioritering (art. 4.2a)
- **Herhaald verzoek** — verzoek over dezelfde aangelegenheid waarover eerder is beslist
- **Misbruikverzoek** — verzoek met kennelijk ander doel dan het verkrijgen van publieke informatie (art. 4.6)

## Procesbron

Wettelijke grondslag: Wet open overheid (Woo), met name hoofdstuk 4 (Passieve openbaarmaking).

Procesgang gedocumenteerd in [[Wiki/Bronsamenvattingen/Informatiesamenleving/handreiking-woo-gemeentelijke-praktijk|Handreiking Woo in de gemeentelijke praktijk]] (VNG/Pels Rijcken 2025), inclusief vier stroomschema's:
1. Het in behandeling nemen van een verzoek
2. De inhoudelijke beoordeling van informatie
3. De afronding van de besluitvorming en de informatieverstrekking
4. Actieve openbaarmaking

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| generalisatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of Melding]] | ← | Specialisatie: Woo-verzoek is een type aanvraag |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | ← | Wordt behandeld als zaak |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | → | Leidt tot verstrekking van documenten |

## Bedrijfsprocessen

- **Behandelen Woo-verzoek** — ontvangst, precisering, zoekslag, beoordeling, besluitvorming, verstrekking
- **Actieve openbaarmaking** — het verzoek, besluit en verstrekte documenten worden zelf actief openbaar gemaakt (art. 3.3 lid 2 sub i)

## Bronnen
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/handreiking-woo-gemeentelijke-praktijk]]

## Terugmelding GGM

GGM-hiaat: de Woo is de belangrijkste transparantiewet voor gemeenten. Het Woo-verzoek is een wettelijk verplicht procesobject dat elke gemeente behandelt, maar ontbreekt in het GGM. Mogelijk te modelleren als specialisatie van AanvraagOfMelding met Woo-specifieke attributen (uitzonderingsgronden, verdaging, deelbesluiten).

Teruggemeld als #66 in [[Wiki/Analyses/ggm-terugmeldingen]].
