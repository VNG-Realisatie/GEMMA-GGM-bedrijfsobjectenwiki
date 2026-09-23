---
type: element
naam: Spoorbaan
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Spoor
ggm_guid: EAID_B0EA89D8_EE32_410b_B683_8CA937E5009D
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "SPOOR"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_F09830F5_0257_4381_A3F8_A10545BE42AC"]
ggm_definitie: "De as van het spoor, dat wil zeggen het midden van twee stalen staven op een onderling vaste afstand, waarover trein, tram, of sneltram rijdt."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: "IMGeo 1.0"

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

bo_homoniemen:
  - bedrijfsobject: "nog geen BO-pagina — erfgoed/archeologie is nog niet ge-ingest"
    ggm_entiteit: Spoor
    ggm_guid: EAID_14939C33_2DCE_41bf_A2BE_FF1EDD292FE7
    ggm_beleidsdomein: Archeologie
    toelichting: "In Archeologie is 'Spoor' een blijk van eerdere menselijke aanwezigheid (bijv. een paalgat of greppelvulling bij een opgraving) — een geheel ander concept dan de spoorbaan-as in RSGBPlus."

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Spoor** (beleidsdomein RSGBPlus) als directe tegenhanger.
bo_definitie: "De as van het spoor: het midden van twee stalen staven op een onderling vaste afstand, waarover trein, tram of sneltram rijdt."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (eigen objecttype voor railinfrastructuur), herkenbaar voor domeinexperts (spoorbaan-as van tram/trein/sneltram), eigen bestaan (zelfstandig geregistreerde lijn met identificatie), meervoud (meerdere sporen per traject/gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (functie, geometrie).

## Beschrijving

Een spoorbaan is de as van een spoor: het midden van twee stalen staven op vaste afstand waarover trein, tram of sneltram rijdt. Het is een van de 18 BGT-objecttypen en wordt door de gemeente (of een andere bronhouder) als lijnvormig topografisch object geregistreerd.

## Naamkeuze

De GGM-entiteitnaam "Spoor" is een homoniem — dezelfde naam wordt in beleidsdomein Archeologie gebruikt voor een ander concept (een blijk van eerdere menselijke aanwezigheid, bijv. een paalgat bij een opgraving). Dit BO heet **Spoorbaan**.

**Overwogen namen:**
- **Spoorbaan** — functionele naam, ondubbelzinnig, sluit aan bij gangbaar spraakgebruik voor railinfrastructuur; geen haakjes nodig in de bestandsnaam
- Spoor — de GGM-naam zelf, maar botst met het archeologische begrip zodra dat wordt vastgelegd
- Spoor (BGT) — GEMMA-alternate-name-conventie, expliciet afgeraden voor bestandsnamen (haakjes)

## GGM-bron

> "De as van het spoor, dat wil zeggen het midden van twee stalen staven op een onderling vaste afstand, waarover trein, tram, of sneltram rijdt." (GGM, entiteit Spoor, beleidsdomein RSGBPlus)

- **Entiteit:** Spoor
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatieSpoor, statusSpoor, relatieveHoogteliggingSpoor, geometrieSpoor, datumBeginGeldigheidSpoor, datumEindeGeldigheidSpoor
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
