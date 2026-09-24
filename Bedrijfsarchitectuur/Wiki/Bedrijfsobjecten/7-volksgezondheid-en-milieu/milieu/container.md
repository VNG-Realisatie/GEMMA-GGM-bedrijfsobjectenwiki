---
type: element
naam: Container
onderwerp: [Milieu]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Container"
ggm_guid: EAID_7D3D98F0_664C_4605_9D95_F68C88ECBA9A
ggm_uml_type: Class
ggm_beleidsdomein: "Afval"
ggm_taakveld: "7 Volksgezondheid en Milieu"
ggm_diagram: [Diagram Afval Ophalen]
ggm_diagram_ids: [EAID_D98AA96C_2EB0_4b46_9E9C_09D55E02FE38]
ggm_definitie: "Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Container"
ggm_gemma_guid: "a9b50546-d72d-4e60-8da5-184a27a626c5"
ggm_gemma_definitie: "Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-a9b50546-d72d-4e60-8da5-184a27a626c5"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Container** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Containertype** (classificatie) — Typering/referentietabel
  - **Ophaalmoment** (detail) — Detailgegeven (geassocieerd met BO)
  - **Rit** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Vuilniswagen** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Vulgraadmeting** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen"
bo_toelichting:
bo_via_kandidaten:
  - ggm_entiteit: "Rit"
    ggm_guid: "EAID_832DA9A0_0E64_4d41_8266_38418B095919"
    reden: "Een inzamelrit is gekoppeld aan het legen van containers."
bedrijfsprocessen: [Afvalinzameling, Containerbeheer, Het Nieuwe Inzamelen]
bedrijfsfuncties: [Afvalbeheer]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: geschikt voor één fractie
  - type: associatie
    bedrijfsobject: "[[Milieustraat]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: staat op milieustraat
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Kernobject in afvalbeheer (inzamelinfrastructuur) |
| Herkenbaar voor domeinexperts | ✅ Elke gemeente beheert containers voor gescheiden inzameling |
| Heeft eigen bestaan | ✅ Fysieke voorziening met eigen locatie en registratie |
| Kan in meervoud bestaan | ✅ Utrecht heeft 1.750+ ondergrondse containers alleen al |
| Heeft eigen levenscyclus | ✅ Plaatsing → gebruik → onderhoud → vervanging |
| Heeft relaties met andere concepten | ✅ Routes, fracties, locaties, vulgraadmetingen |

**6/6 criteria van toepassing.**

## Beschrijving

Fysieke containers die de gemeente plaatst en beheert voor de gescheiden inzameling van huishoudelijk afval. Het containerpark omvat ondergrondse containers (voor restafval en grondstoffen in de openbare ruimte), kliko's (minicontainers aan huis voor GFT, papier of PBP) en citybins (draagbare afvalemmers voor GFE-inzameling bij hoogbouw). Onderdeel van Het Nieuwe Inzamelen, het systeem waarbij de gemeente steeds meer afvalstromen gescheiden ophaalt. Ondergrondse containers zijn uitgerust met sensoren voor vulgraadmeting, zodat ophaalroutes kunnen worden geoptimaliseerd.

> "Met Het Nieuwe Inzamelen zamelen we meer grondstoffen gescheiden in bij de bron." (bron: [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020|Grondstoffennota 2020]])

## Specialisaties

Herkende subtypes van container. Geen aparte BO's — het zijn waarden van het attribuut `naam` op [Containertype](afval.md).

| Specialisatie | Omschrijving | GGM-attribuut |
|---|---|---|
| Ondergrondse container | Ingegraven container voor restafval of grondstoffen | [Containertype](afval.md) → `naam` |
| Kliko | Minicontainer aan huis voor GFT, papier of PBP | [Containertype](afval.md) → `naam` |
| Citybin | Draagbare afvalemmer voor GFE-inzameling bij hoogbouw | [Containertype](afval.md) → `naam` |

## GGM-bron

> **Container**: Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen
> — *GGM, Afval (taakveld 7 Volksgezondheid en Milieu)*

**Entiteit:** Container
**Matchsterkte:** exact — zelfde concept, compatibele definitie.

## Relaties

- **[[Grondstofstroom]]** — elke container is geschikt voor één fractie (GFT, restafval, papier, etc.)
- **[[Milieustraat]]** — containers staan ook op de milieustraat voor brengstromen
- **Vulgraadmeting** — GGM-entiteit (geen BO); sensor die de vulgraad van ondergrondse containers meet

## Bedrijfsprocessen

- **Afvalinzameling** — ophalen van afval uit containers volgens routes
- **Containerbeheer** — plaatsing, onderhoud en vervanging van containers
- **Het Nieuwe Inzamelen** — transitie naar meer gescheiden inzameling aan de bron

## Bedrijfsfuncties

- Afvalbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020]]
