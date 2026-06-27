---
type: bedrijfsobject
naam: Kinderbeschermingsmaatregel
onderwerp: [Maatschappelijke Ondersteuning]
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

bo_definitie: "Door de rechter opgelegde maatregel ter bescherming van een minderjarige, bestaande uit ondertoezichtstelling of (voorlopige) voogdij, waarvan de gemeente de uitvoering organiseert."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft jeugdige"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding|Zorgmelding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "kan voortkomen uit zorgmelding"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan|Hulpverleningsplan]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "uitvoering via plan van aanpak"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/machtiging-gesloten-jeugdhulp|Machtiging Gesloten Jeugdhulp]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "kan leiden tot machtiging gesloten jeugdhulp"
bedrijfsprocessen: [kinderbeschermingsmaatregel uitvoeren, verzoek tot onderzoek indienen, jeugdhulp organiseren]
bedrijfsfuncties: [jeugdbescherming, toegang sociaal domein]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Kernbegrip in jeugdbescherming; OTS en voogdij zijn veelgebruikte termen |
| Besproken op bestuurlijk niveau | ✅ | Aantallen in raadsinformatie, financieel substantieel |
| Vastgelegd in systemen | ✅ | Geregistreerd in jeugd-applicatie met type, start, einde |
| Eigen attributen | ✅ | Type (OTS, voorlopige OTS, voogdij, voorlopige voogdij), begin-/einddatum, rechterlijke uitspraak |
| Relaties met andere objecten | ✅ | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding\|Zorgmelding]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan\|Hulpverleningsplan]] |
| Levenscyclus | ✅ | Raadsonderzoek → verzoek → uitspraak → uitvoering → beëindiging |

## Beschrijving

Een kinderbeschermingsmaatregel is een door de rechter opgelegde maatregel om de veiligheid en ontwikkeling van een minderjarige te waarborgen. De Jeugdwet definieert kinderbeschermingsmaatregelen als: voogdij en voorlopige voogdij op grond van Boek 1 BW, ondertoezichtstelling en voorlopige ondertoezichtstelling (art. 1.1).

De gemeente legt de maatregel niet zelf op — dat doet de rechter op verzoek van de Raad voor de Kinderbescherming — maar is verantwoordelijk voor de uitvoering (art. 2.4 lid 2). Dit houdt in dat het college voorziet in een toereikend aanbod van gecertificeerde instellingen en de benodigde jeugdhulp inzet.

Het college doet een verzoek tot onderzoek bij de Raad voor de Kinderbescherming zodra het van oordeel is dat een maatregel overwogen moet worden (art. 2.4 lid 1). De maatregel wordt uitsluitend uitgevoerd door een gecertificeerde instelling (art. 3.2).

## Subtypes

Herkende specialisaties van Kinderbeschermingsmaatregel. Gevonden in de Jeugdwet art. 1.1. Geen apart BO.

- **Ondertoezichtstelling (OTS)** — rechterlijke maatregel waarbij een gecertificeerde instelling toezicht houdt op de opvoeding (art. 255 lid 1 Boek 1 BW)
- **Voorlopige ondertoezichtstelling** — spoedvariant van OTS (art. 257 lid 1 Boek 1 BW)
- **Voogdij** — gezagsoverdracht aan een gecertificeerde instelling of derde (Boek 1 BW)
- **Voorlopige voogdij** — spoedvariant bij acute situaties (Boek 1 BW)

## Procesbron

De kinderbeschermingsmaatregel ontstaat in de keten: zorgmelding → onderzoek Raad voor de Kinderbescherming → verzoek aan rechter → uitspraak → uitvoering door gecertificeerde instelling. De gemeente is verantwoordelijk voor meerdere schakels in deze keten.

> "Zodra het college tot het oordeel komt dat een maatregel met betrekking tot het gezag over een minderjarige die zijn woonplaats heeft binnen zijn gemeente overwogen moet worden, doet het college een verzoek tot onderzoek bij de raad voor de kinderbescherming." (art. 2.4 lid 1)

> "Het college is ten behoeve van een jeugdige die zijn woonplaats heeft binnen zijn gemeente verantwoordelijk voor de uitvoering van de kinderbeschermingsmaatregelen" (art. 2.4 lid 2)

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | betreft jeugdige | naar dit BO | Jeugdwet art. 1.1 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding\|Zorgmelding]] | kan voortkomen uit zorgmelding | naar dit BO | Jeugdwet art. 3.1 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan\|Hulpverleningsplan]] | uitvoering via plan van aanpak | van dit BO | Jeugdwet art. 4.1.3 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/machtiging-gesloten-jeugdhulp\|Machtiging Gesloten Jeugdhulp]] | kan leiden tot machtiging | van dit BO | Jeugdwet art. 6.1.2 lid 3 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | bekostiging jeugdhulp via beschikking | gerelateerd | Jeugdwet art. 2.4, 3.5 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/kindermishandeling-en-huiselijk-geweld]]

## Terugmelding GGM

Het GGM-beleidsdomein Jeugdbescherming en reclassering bevat Zorgmelding en Zorgelijke Situatie, maar modelleert de kinderbeschermingsmaatregel zelf niet als entiteit. OTS, voogdij en gezagsbeëindiging ontbreken. Dit was al eerder gesignaleerd in het onderwerpoverzicht als openstaande vraag. De Jeugdwet geeft nu een heldere wettelijke grondslag: de gemeente is verantwoordelijk voor de uitvoering en registreert de maatregel.
