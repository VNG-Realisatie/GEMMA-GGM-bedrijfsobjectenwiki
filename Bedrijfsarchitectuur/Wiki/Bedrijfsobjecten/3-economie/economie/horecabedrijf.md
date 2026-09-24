---
type: element
naam: Horecabedrijf
onderwerp: [Economie]
archimate_type: "business-object"
grondslag: ggm-afgeleid

# GGM-velden — geen directe entiteit; afgeleid via generalisatie van GGM-entiteit Vestiging
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
analyse_ggm_dekking: |
  Dit BO heeft geen directe GGM-entiteit; het is een specialisatie van GGM-entiteit **Vestiging**, vastgelegd als generalisatie-relatie naar [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging|Vestiging]].
bo_definitie: "Een onderneming die zich richt op het verstrekken van eten, drinken en/of logies."
bo_toelichting:
bedrijfsprocessen: [horecavergunningverlening, handhaving horeca, horecabeleid]
bedrijfsfuncties: [vergunningverlening, handhaving, economisch beleid]
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging|Vestiging]]"
    richting: "naar-dit-BO"
    kardinaliteit:
    beschrijving: Horecabedrijf is een specialisatie van Vestiging
  - type: associatie
    bedrijfsobject: "[[Hotel]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een horecabedrijf kan een hotel exploiteren
  - type: associatie
    bedrijfsobject: "[[Terras]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een horecabedrijf kan een terras exploiteren
  - type: associatie
    bedrijfsobject: "[[Bed-and-breakfast]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een horecabedrijf kan een B&B exploiteren"
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal begrip in Verordening horeca en Ontwikkelingskader |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip voor vergunningverleners en beleidsmakers |
| Heeft een eigen bestaan | ✅ | Exploitatie op een fysieke locatie met vergunning |
| Kan in meervoud bestaan | ✅ | Honderden horecabedrijven in een gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanvraag → vergunning → exploitatie → sluiting |
| Heeft relaties met andere concepten | ✅ | Hotel, terras, vergunning, hinderprofiel |

6/6 criteria — BO.

## Beschrijving

Een horecabedrijf is een onderneming die zich richt op het verstrekken van eten, drinken en/of logies. De gemeente reguleert horecabedrijven via de Verordening horeca, het Ontwikkelingskader Horeca en een vergunningenstelsel. Kernafwegingen zijn leefbaarheid (hinderprofiel), balans met detailhandel en wonen, en spreiding over de stad.

Het Utrechtse beleid stimuleert horeca buiten de historische binnenstad en beoordeelt horecaontwikkeling in het centrum kritisch.

## Specialisaties

| Specialisatie | Omschrijving | GGM-entiteit |
|---|---|---|
| Horecavergunning | Vergunning voor exploitatie van een horecabedrijf | — |

De horecavergunning is een subtype van vergunning, hier vastgelegd vanwege de directe koppeling met het horecabedrijf.

## Generalisatie

Horecabedrijf heeft geen eigen GGM-entiteit. Het is een specialisatie van GGM-entiteit **Vestiging** (RSGBPlus, Kern) — zie [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging|Vestiging]] voor de GGM-bron en matchsterkte. Het GGM kent geen specifieke horecaentiteit; horecabedrijf is herkenbaar via SBI-code. De GGM-entiteit Hotel is een aparte specialisatie van Vestiging.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | generalisatie | Horecabedrijf → Vestiging | — | GGM (overerving) |
| [[Hotel]] | associatie | Horecabedrijf → Hotel | 0..* | Beleid |
| [[Terras]] | associatie | Horecabedrijf → Terras | 0..* | Beleidsregel terrassen |
| [[Bed-and-breakfast]] | associatie | Horecabedrijf → B&B | 0..* | Beleid |

## Bronnen

- [[Wiki/Bronsamenvattingen/Economie/economie-speerpunten-vng]]
- [[Wiki/Bronsamenvattingen/Economie/ontwikkelingskader-detailhandel-2012]]
- [[Wiki/Bronsamenvattingen/Economie/detailhandel-utrecht-2015]]
- [[Wiki/Bronsamenvattingen/Economie/horecabeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/actualisatie-marktruimte-hotelnota]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-terrassen-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregel-hotels-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-short-stay-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsnota-werklocaties-2035]]
