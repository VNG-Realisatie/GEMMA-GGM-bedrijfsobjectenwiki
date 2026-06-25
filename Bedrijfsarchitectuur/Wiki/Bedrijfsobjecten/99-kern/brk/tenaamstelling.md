---
type: bedrijfsobject
naam: Tenaamstelling
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Tenaamstelling
ggm_guid: EAID_2651D6E0_6AC8_43a8_A4F6_4706209BAC8E
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "BRK"
  - "TENAAMSTELLING"
  - "ZAKELIJK RECHT"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten met attributen"
ggm_diagram_ids:
  - EAID_DF9CEAAD_E574_40b3_970B_DC558AB579D0
  - EAID_BAB7CC48_0969_4064_98B6_6C4F51207155
  - EAID_A308855C_FB69_43cf_AA98_12555468AAAE
  - EAID_0A286E07_9DEF_46a8_AC66_469F5A70564E
  - EAID_FF8B8883_467A_422e_A894_C513307057AF
ggm_definitie: "Een TENAAMSTELLING vormt de relatie tussen een Recht en een Persoon en geeft aan welk recht, met uitzondering van hypotheek en beslag, door een Persoon wordt uitgeoefend op een Kadastraal object."
ggm_toelichting: "Een tenaamstelling heeft betrekking op de eigendom van die Persoon van één Kadastraal object of op een beperkt recht van die Persoon op één Kadastraal object."
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: Tenaamstelling
ggm_gemma_guid: 429cbd2f-a86d-49d9-9c8a-0de67a7e7d3e
ggm_gemma_definitie: "Een TENAAMSTELLING vormt de relatie tussen een Recht en een Persoon en geeft aan welk recht, met uitzondering van hypotheek en beslag, door een Persoon wordt uitgeoefend op een Kadastraal object."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-429cbd2f-a86d-49d9-9c8a-0de67a7e7d3e"
ggm_gemma_bron: "BRK"
ggm_gemma_alternate_name: ""

ggm_duplicaat_entiteiten: []

gemma_definitie: "De vastlegging van welke persoon welk zakelijk recht uitoefent op welk kadastraal object."
relaties:
  - type: associatie
    bedrijfsobject: "[[Zakelijk Recht]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een tenaamstelling hoort bij precies één zakelijk recht"
  - type: associatie
    bedrijfsobject: "[[Ingeschreven Persoon]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een tenaamstelling is ten name van een persoon (natuurlijk persoon via BRP)"
  - type: associatie
    bedrijfsobject: "[[Stukdeel]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een tenaamstelling is gebaseerd op een of meer stukdelen"
bedrijfsprocessen:
  - WOZ-beschikking
  - OZB-aanslag
  - Eigendomsverificatie
bedrijfsfuncties:
  - Belastingheffing
  - Handhaving
---

## BO-criteria toetsing

6/6 criteria. Tenaamstelling is een zelfstandig objecttype met eigen identificatie, eigen levenscyclus (ontstaat bij vestiging recht, beëindigd bij overdracht), meervoudig (meerdere tenaamstellingen per kadastraal object), en relaties met zakelijke rechten en personen. Essentieel voor de gemeente om te bepalen wie eigenaar/rechthebbende is.

## Beschrijving

Een tenaamstelling legt vast welke persoon welk recht uitoefent op welk kadastraal object. Het is de koppeling tussen [[Zakelijk Recht]] en een persoon ([[Ingeschreven Persoon]] via BRP, of een niet-natuurlijk persoon via het Handelsregister). De gemeente gebruikt tenaamstellingen om te bepalen aan wie WOZ-beschikkingen en OZB-aanslagen worden verzonden, wie vergunninghouder kan zijn, en wie aan te spreken bij handhaving.

Bij gezamenlijk eigendom kan een persoon een aandeel in het recht hebben (bijv. 1/2 eigendom). De burgerlijke staat ten tijde van verkrijging is relevant voor de goederenrechtelijke positie.

## GGM-bron

> "Een TENAAMSTELLING vormt de relatie tussen een Recht en een Persoon en geeft aan welk recht, met uitzondering van hypotheek en beslag, door een Persoon wordt uitgeoefend op een Kadastraal object."

- **Entiteit:** Tenaamstelling
- **Beleidsdomein:** RSGBPlus (99 Kern)
- **Attributen:** identificatieTenaamstelling, aandeelInRecht, verkregenNamensSamenwerkingsverband, exploitantcode, datumBeginGeldigheid, datumEindeGeldigheid, burgerlijkeStaatTenTijdeVanVerkrijging, verklaringInzakeDerdenBescherming
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| hoort bij | van-dit-BO | [[Zakelijk Recht]] | 1 | GGM |
| ten name van | van-dit-BO | [[Ingeschreven Persoon]] | 1 | GGM + BRK Catalogus |
| gebaseerd op | van-dit-BO | [[Stukdeel]] | 1..* | BRK Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]
