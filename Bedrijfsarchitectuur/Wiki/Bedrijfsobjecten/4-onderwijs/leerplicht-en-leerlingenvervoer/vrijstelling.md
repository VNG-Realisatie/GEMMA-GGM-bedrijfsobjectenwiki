---
type: bedrijfsobject
naam: Vrijstelling
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vrijstelling
ggm_guid: EAID_B8584CD2_A54A_4a59_82B6_A597A0864CFA
ggm_uml_type: Class
ggm_beleidsdomein: Leerplicht en Leerlingenvervoer
ggm_taakveld: "4 Onderwijs"
ggm_diagram: [Diagram Beslissingen Leerplicht]
ggm_diagram_ids: [EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308]
ggm_definitie: "Een formeel besluit waarbij een leerling wordt ontheven van de leerplicht."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Vrijstelling
ggm_gemma_guid: e09e0c4d-1c6f-474b-8abc-7fd36f6fd699
ggm_gemma_definitie: "Een formeel besluit waarbij een leerling wordt ontheven van de leerplicht."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-e09e0c4d-1c6f-474b-8abc-7fd36f6fd699
ggm_gemma_bron:
ggm_gemma_alternate_name:

gemma_definitie: "Besluit waarbij een leerling geheel of gedeeltelijk wordt ontheven van de leerplicht."
relaties:
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Vrijstelling betreft leerling"
  - type: associatie
    bedrijfsobject: "[[School]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Vrijstelling heeft betrekking op school"
bedrijfsprocessen: [Leerplichthandhaving]
bedrijfsfuncties: [Leerplicht]
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Wettelijk instrument uit de Leerplichtwet waarmee een leerling wordt ontheven |
| Herkenbaar voor domeinexperts | ✅ Leerplichtambtenaren beoordelen en verlenen vrijstellingen |
| Heeft eigen bestaan | ✅ Formeel besluit met eigen kenmerken (periode, grond, verzuimsoort) |
| Kan in meervoud bestaan | ✅ Meerdere vrijstellingen per gemeente, ook meerdere per leerling mogelijk |
| Heeft eigen levenscyclus | ✅ Aanvraag → beoordeling → toekenning/afwijzing → eventueel beeindiging |
| Heeft relaties met andere concepten | ✅ Leerling, school, leerplichtambtenaar |

**6/6 criteria van toepassing.**

## Beschrijving

Een vrijstelling is een formeel besluit waarbij een leerling geheel of gedeeltelijk wordt ontheven van de leerplicht. De Leerplichtwet kent verschillende gronden voor vrijstelling, zoals lichamelijke of psychische ongeschiktheid, het volgen van onderwijs in het buitenland, of bezwaren tegen de richting van het beschikbare onderwijs. De gemeente registreert en beoordeelt de vrijstellingen als onderdeel van de leerplichthandhaving.

## GGM-bron

> "Een formeel besluit waarbij een leerling wordt ontheven van de leerplicht."
> — GGM-entiteit: Vrijstelling, beleidsdomein: Leerplicht en Leerlingenvervoer

**Matchsterkte: exact.** De GGM-entiteit beschrijft hetzelfde concept.

**GGM-attributen:** datumStart, datumEinde, aanvraagToegekend, verzuimsoort, buitenlandseSchoollocatie.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Leerling]] | associatie | ← | 1 | GGM |
| [[School]] | associatie | ← | 1 | GGM |

## Bedrijfsprocessen

- **Leerplichthandhaving** — beoordeling en registratie van vrijstellingsaanvragen

## Bedrijfsfuncties

- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/beleidsnota-onderwijshuisvesting-utrecht]]
- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
