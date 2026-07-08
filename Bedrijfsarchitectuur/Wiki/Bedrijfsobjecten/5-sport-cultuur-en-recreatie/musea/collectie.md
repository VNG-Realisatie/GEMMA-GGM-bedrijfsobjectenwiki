---
type: element
naam: Collectie
domein: [Cultuur]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Collectie
ggm_guid: EAID_6DC28A18_DF54_4b92_A592_5F717935CA67
ggm_uml_type: Class
ggm_beleidsdomein: Musea
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Prinsenhof Collectie]
ggm_diagram_ids: [EAID_B2D890F1_6B7C_45df_9A70_8C40CE1B3611]
ggm_definitie: "Een verzameling van verworven voorwerpen die is samengesteld op grond van vastgestelde criteria."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: Collectie
ggm_gemma_guid: 65fad3a5-bce6-4c9f-814e-23e42d0f91fd
ggm_gemma_definitie: "Een verzameling van verworven voorwerpen die is samengesteld op grond van vastgestelde criteria."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-65fad3a5-bce6-4c9f-814e-23e42d0f91fd"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Collectie** als directe tegenhanger.
bo_definitie: "Samenhangende verzameling cultuurgoederen of museumobjecten, beheerd door een gemeentelijk museum of erfgoedinstelling op grond van vastgestelde criteria."
bo_toelichting: ""
bedrijfsprocessen: [Collectiebeheer, Verwerving en afstoting, Collectieplan]
bedrijfsfuncties: [Erfgoedbeheer, Collectiebeheer]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/museumobject|Museumobject]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een collectie bevat museumobjecten
---

# Collectie

Samenhangende verzameling cultuurgoederen of museumobjecten, beheerd door een gemeentelijk museum of erfgoedinstelling. Collecties worden samengesteld op grond van inhoudelijke criteria (type, periode, thema) en vormen de basis voor collectiebeleid, tentoonstellingen en bruiklenen.

De Erfgoedwet (art. 2.8-2.11) regelt dat de Minister instellingen kan belasten met collectiebeheer via een instellingsbesluit, met planmatig beleid als voorwaarde. De "beschermde verzameling" (art. 3.7 lid 2) is een bijzondere variant met formele beschermingsstatus.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernbegrip in museaal collectiebeheer |
| Herkenbaar voor experts | ✅ | Conservator, collectiebeheerder kennen dit |
| Eigen bestaan | ✅ | Een collectie bestaat onafhankelijk van individuele objecten |
| Meervoud | ✅ | Musea hebben meerdere deelcollecties (keramiek, schilderijen, etc.) |
| Eigen levenscyclus | ✅ | Vorming → instellingsbesluit → planmatig beheer → eventueel intrekking |
| Relaties | ✅ | Met [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/museumobject\|Museumobject]] (m:n), met beheerinstelling |

## GGM-bron

> **Collectie**: Een verzameling van verworven voorwerpen die is samengesteld op grond van vastgestelde criteria.
> — *GGM v2.5.1, Musea (taakveld 5 Sport, Cultuur en Recreatie)*

**Entiteit:** Collectie
**Attributen:** naam, omschrijving
**Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Bevat museumobjecten | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/museumobject\|Museumobject]] | Collectie → Museumobject [0..*..0..*] | Geen |
| Beschermd als | *(Beschermde verzameling)* | — | Erfgoedwet art. 3.7 lid 2; geen apart GGM-concept |

## Bedrijfsprocessen

- **Collectiebeheer**: registratie, documentatie, conservering van de collectie als geheel
- **Verwerving en afstoting**: toevoegen of verwijderen van objecten aan/uit de collectie
- **Collectieplan**: planmatig beleid voor behoud en ontwikkeling (Erfgoedwet art. 2.10)

## Bedrijfsfuncties

- Erfgoedbeheer
- Collectiebeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/erfgoed/erfgoedwet|Erfgoedwet (BWBR0037521)]]
- [[Wiki/Bronsamenvattingen/Cultuur/kunst-en-cultuur]]
