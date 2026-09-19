---
type: element
naam: Beperking
onderwerp: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Beperking
ggm_guid: EAID_F110608E_9C6A_4d66_BDCB_F4B2465E3CFD
ggm_uml_type: Class
ggm_beleidsdomein: "Generiek Jeugd en Wmo"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Beperkingen]
ggm_diagram_ids: [EAID_9B278A50_862A_4085_B362_C41392101916]
ggm_definitie: "Een stoornis of conditie – lichamelijk, zintuiglijk en/of geestelijk – die een normaal maatschappelijk functioneren belemmert en nadelige sociale gevolgen met zich meebrengt."
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

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Beperking** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Beperkingscategorie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Beperkingscore** (detail) — Detailgegeven (geassocieerd met BO)
  - **Beperkingscoresoort** (classificatie) — Typering/referentietabel
bo_definitie: "Een stoornis of conditie – lichamelijk, zintuiglijk en/of geestelijk – die het normaal maatschappelijk functioneren van een cliënt belemmert."
bo_toelichting: "De formeel vastgestelde beperking is de inhoudelijke grondslag waarop het college een maatwerkvoorziening toekent (Wmo 2015 art. 2.3.5 lid 3). Een beperking kan al bestaan vóórdat er een beschikking is — bijvoorbeeld tijdens het onderzoek naar aanleiding van een melding (art. 2.3.2) — en wordt pas achteraf gekoppeld aan de beschikking die erop is gebaseerd."
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "is gebaseerd op (indien de beperking tot een beschikking heeft geleid)"
bedrijfsprocessen: [onderzoek naar ondersteuningsbehoefte, beschikking afgeven]
bedrijfsfuncties: [toegang sociaal domein, beschikkingenbeheer]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Wettelijke grondslag voor toekenning van een maatwerkvoorziening (Wmo 2015 art. 2.3.5 lid 3) |
| Besproken op bestuurlijk niveau | ✅ | Aard en omvang van beperkingen sturen doelgroepenbeleid en de Wmo-monitor |
| Vastgelegd in systemen | ✅ | Geregistreerd tijdens het onderzoek/de intake in de Wmo/Jeugd-applicatie |
| Eigen attributen | ✅ | duur, categorie, commentaar, wet |
| Levenscyclus | ✅ | Vastgesteld tijdens onderzoek, kan wijzigen, heeft een geldigheidsduur (`duur`) |
| Relaties met andere objecten | ✅ | Beperkingscategorie, Beperkingscore, Beschikking |

## Beschrijving

Een beperking is een stoornis of conditie — lichamelijk, zintuiglijk en/of geestelijk — die het normaal maatschappelijk functioneren van een cliënt belemmert. De gemeente stelt de beperking vast tijdens het onderzoek naar aanleiding van een melding (Wmo 2015 art. 2.3.2) en gebruikt die vaststelling als grondslag voor de beslissing over een maatwerkvoorziening (art. 2.3.5 lid 3): het college beslist tot verstrekking "ter compensatie van de beperkingen in de zelfredzaamheid of participatie die de cliënt ondervindt".

De beperking bestaat onafhankelijk van de beschikking — ze kan al zijn vastgesteld voordat een beschikking wordt afgegeven — en wordt pas gekoppeld aan een beschikking zodra die erop is gebaseerd.

## GGM-componenten

GGM-entiteiten die de beperking nader typeren of kwantificeren, maar geen zelfstandig bedrijfsobject zijn.

- **Beperkingscategorie** — categorisering van de beperking (GGM: "lichamelijk, zintuiglijk en/of geestelijk" volgens de definitie van Beperking zelf)
- **Beperkingscore** — getalsmatige duiding van de ernst van de beperking

## GGM-bron

> "Een stoornis of conditie ‚ lichamelijk, zintuiglijk en-of geestelijk ‚ die een normaal maatschappelijk functioneren belemmert en nadelige sociale gevolgen met zich meebrengt." — GGM Generiek Jeugd en Wmo (spelling opgeschoond in bo_definitie)

- **Entiteit:** Beperking
- **Beleidsdomein:** Generiek Jeugd en Wmo
- **Attributen:** duur, categorie, commentaar, wet
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | → | 0..1 | is gebaseerd op (indien de beperking tot een beschikking heeft geleid) | GGM |

## Bedrijfsprocessen

- Onderzoek naar ondersteuningsbehoefte
- Beschikking afgeven

## Bedrijfsfuncties

- Toegang sociaal domein
- Beschikkingenbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015]]
