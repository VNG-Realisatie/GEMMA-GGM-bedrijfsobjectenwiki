---
type: element
naam: Draagkracht
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Draagkracht
ggm_guid: EAID_9e03b696_a4f8_4486_a5d3_52483f259ed2
ggm_uml_type: Class
ggm_beleidsdomein: Sociaal Domein Generiek
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Diagram Inkomsten]
ggm_diagram_ids: [EAID_7683FAC9_3F9C_4e21_8D02_5B9FDEBC7D1F]
ggm_definitie: "Het gedeelte uit je inkomen of vermogen dat je zelf zou kunnen bijdragen in de kosten (?) voor de bijzondere bijstand(?).De draagkracht is de uitkomst van een ingewikkelde berekening maar wordt voor een jaar vastgesteld en gebruikt."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Draagkracht** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Draagkrachtregime** (onderdeel) — Onderdeel van Draagkracht
bo_definitie: "Het gedeelte uit je inkomen of vermogen dat je zelf zou kunnen bijdragen in de kosten (?) voor de bijzondere bijstand(?). De draagkracht is de uitkomst van een ingewikkelde berekening maar wordt voor een jaar vastgesteld en gebruikt."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Inkomensvoorziening]]"
    richting: van-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Draagkracht bepaalt recht op inkomensvoorziening"
  - type: associatie
    bedrijfsobject: "[[Client]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Client heeft vastgestelde draagkracht"
bedrijfsprocessen: [draagkrachtbeoordeling, bijzondere bijstandsverlening]
bedrijfsfuncties: [inkomensondersteuning]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Identificeerbaar | ✅ Per cliënt vastgesteld met start- en einddatum, geldig voor een jaar |
| Levenscyclus | ✅ Berekening → vaststelling → geldigheidsperiode → herberekening |
| Eigendom/verantwoordelijkheid | ✅ Gemeente stelt draagkracht vast; bepaalt zelf de berekeningswijze |
| Bestuurlijk relevant | ✅ Bepalend voor het recht op bijzondere bijstand; gemeentelijke beleidsvrijheid in berekening |
| Relaties | ✅ Met Client, Draagkrachtregime, Inkomensvoorziening |
| Persistent | ✅ Vastgelegd in cliëntdossier, geldig voor een periode |

## Beschrijving

Draagkracht is het berekende vermogen van een inwoner om zelf in bijzondere kosten te voorzien. Het is de uitkomst van een berekening waarbij de gemeente inkomen en vermogen van de aanvrager toetst tegen normbedragen. De draagkracht wordt voor een jaar vastgesteld en bepaalt of en in welke mate recht bestaat op bijzondere bijstand.

Gemeenten hebben aanzienlijke beleidsvrijheid bij de draagkrachtberekening:
- Wel of niet hanteren van een eigen bijdrage of drempelbedrag
- Vanaf welk inkomen draagkracht wordt verondersteld
- Welke inkomens- en vermogensbestanddelen meetellen
- Of reserveringsruimte in de bijstand wordt meegerekend
- Begin en duur van de inkomensperiode

> "Het komt voor dat via een gang naar de rechter mensen alsnog bijzondere bijstand krijgen toegekend" — wat aangeeft dat draagkrachtbeoordeling maatwerk is en juridisch toetsbaar.

## GGM-bron

> "Het gedeelte uit je inkomen of vermogen dat je zelf zou kunnen bijdragen in de kosten (?) voor de bijzondere bijstand(?). De draagkracht is de uitkomst van een ingewikkelde berekening maar wordt voor een jaar vastgesteld en gebruikt."
> — GGM, entiteit *Draagkracht*, beleidsdomein Sociaal Domein Generiek

**Matchsterkte:** exact — het GGM beschrijft hetzelfde concept, inclusief de jaarlijkse vaststelling.

**Attributen (GGM):** Einddatum, Startdatum

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | heeft vastgestelde draagkracht | Client → Draagkracht | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | bepaalt recht op | Draagkracht → Inkomensvoorziening | Bron |

## Bedrijfsprocessen

- **Draagkrachtbeoordeling**: inkomen en vermogen toetsen, normbedragen toepassen, draagkracht vaststellen
- **Bijzondere bijstandsverlening**: draagkracht als besliscriterium in de beschikking

## Bedrijfsfuncties

- Inkomensondersteuning

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/factsheet-bijzondere-bijstand]]

## Terugmelding GGM

De GGM-definitie bevat vraagtekens ("(?) voor de bijzondere bijstand(?)") en informeel taalgebruik ("een ingewikkelde berekening"). Voorgestelde correctie: "Het berekende deel van het inkomen en vermogen van een inwoner dat beschikbaar is om zelf in noodzakelijke kosten te voorzien, bepalend voor het recht op bijzondere bijstand. De draagkracht wordt periodiek vastgesteld."
