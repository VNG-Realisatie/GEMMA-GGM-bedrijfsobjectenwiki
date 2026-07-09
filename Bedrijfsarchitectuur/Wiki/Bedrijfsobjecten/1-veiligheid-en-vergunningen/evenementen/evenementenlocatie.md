---
type: element
naam: Evenementenlocatie
onderwerp: [evenementen]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein:
ggm_guid:
ggm_uml_type:
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
bo_definitie: "Aangewezen fysieke locatie in de openbare ruimte waar evenementen mogen plaatsvinden, met vastgestelde kaders voor gebruik."
bo_toelichting:
bedrijfsprocessen: []
bedrijfsfuncties: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Evenement]]"
    richting: "naar-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Evenementen vinden plaats op evenementenlocaties
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Locaties zijn het ruimtelijke fundament van het evenementenbeleid |
| Herkenbaar voor domeinexperts | ✅ | Tien benoemde locaties met eigen profielen |
| Heeft een eigen bestaan | ✅ | Locatie bestaat onafhankelijk van individuele evenementen |
| Kan in meervoud bestaan | ✅ | Tien locaties met profielen, daarnaast andere locaties in de stad |
| Heeft een eigen levenscyclus | ✅ | Aanwijzing → profilering → gebruik → evaluatie → herijking (vierjaarlijks) |
| Heeft relaties met andere concepten | ✅ | Evenementen, locatieprofielen, reserveringskalender, flora/fauna/bodem |

**6/6 criteria van toepassing.**

## Beschrijving

Een evenementenlocatie is een aangewezen fysieke plek in de openbare ruimte — park of plein — waar evenementen mogen plaatsvinden. De gemeente werkt met locatieprofielen die per locatie kaders vastleggen voor:

- Aantal evenementendagen per jaar
- Maximale omvang (bezoekers) per categorie
- Duur van het evenement en op-/afbouwtijd
- Maximaal geluidsniveau
- Rustperiode tussen evenementen (12 dagen verhard, 18 dagen onverhard)
- Winterbeperking op groene locaties (1 november–31 maart, vanaf 2027)

Locaties worden gecategoriseerd op basis van omvang, functie en type ondergrond. Voor vergelijkbare locaties gelden vergelijkbare criteria. Drie onderzoeken (flora/fauna, bodem/bomen, geluid) liggen ten grondslag aan de kaders per locatie.

## Procesbron

Dit BO heeft geen GGM-grondslag. Het GGM kent generieke `Locatie`-entiteiten in diverse domeinen (Onderwijs, Sport, Afval, Kern) maar geen specifieke evenementenlocatie. De generieke `Locatie` in Kern is te breed en mist de domeinspecifieke kenmerken (locatieprofiel, rustperiode, geluidsnorm).

Het BO is afgeleid uit de [[Wiki/Bronsamenvattingen/Evenementen/locatiebeleid-evenementen|Beleidsnota Locatiebeleid evenementen — Passende ruimte voor evenementen 2024-2030]] waarin locaties met hun profielen het fundament vormen van het beleid.

> "Locatieprofielen bieden duidelijke richtlijnen voor organisatoren, bezoekers en bewoners. Ze geven per locatie aan hoeveel evenementendagen er op jaarbasis mogen plaatsvinden."

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Evenement]] | associatie | ← | \*..\* | Beleidsnota: evenementen vinden plaats op locaties |

## Bedrijfsprocessen

- **Opstellen locatieprofielen** — per locatie kaders vastleggen op basis van onderzoek en participatie
- **Reserveringskalender beheren** — evenementen toewijzen aan locaties en data
- **Onderzoek** — vierjaarlijks flora/fauna, bodem/bomen en geluidsonderzoek per locatie
- **Onderhoud en verbetering** — groene energie-/wateraansluitingen, verplaatsbaar stadsmeubilair


## Bronnen

- [[Wiki/Bronsamenvattingen/Evenementen/locatiebeleid-evenementen]]

## Terugmelding GGM

**Evenementenlocatie ontbreekt als entiteit.** Het GGM kent geen specifieke locatie-entiteit voor evenementen. De generieke Locatie (Kern) mist domeinspecifieke kenmerken. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
