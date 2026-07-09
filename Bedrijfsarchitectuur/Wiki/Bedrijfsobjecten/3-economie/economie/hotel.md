---
type: element
naam: Hotel
onderwerp: [Economie]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Hotel"
ggm_guid: EAID_5805FA72_C0CE_43c1_A53F_B81166AEFDD4
ggm_uml_type: Class
ggm_beleidsdomein: "3 Economie"
ggm_taakveld: "3 Economie"
ggm_diagram: [Diagram Economie]
ggm_diagram_ids: [EAID_21D78104_E6EA_4d5c_9DBE_AB71F7DC99E7]
ggm_definitie: "Gebouw waar je tegen betaling kunt logeren."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Hotel"
ggm_gemma_guid: "4b2cc303-de99-49c4-968f-836a71825814"
ggm_gemma_definitie: "Gebouw waar je tegen betaling kunt logeren."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-4b2cc303-de99-49c4-968f-836a71825814"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Hotel** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Hotelbezoek** (detail) — Meting/transactie, geen zelfstandig object
bo_definitie: "Verblijfsaccommodatie waar gasten tegen betaling kunnen overnachten, gereguleerd via de beleidsregel hotels met typeringen naar concept, doelgroep en omvang."
bo_toelichting:
bedrijfsprocessen: [hotelvergunningverlening, hotelbeleid, toeristenbelastingheffing]
bedrijfsfuncties: [vergunningverlening, economisch beleid]
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Vestiging]]"
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: "Hotel is een specialisatie van Vestiging (RSGB/GGM-overerving)"
  - type: associatie
    bedrijfsobject: "[[Hotelbezoek]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een hotel heeft hotelbezoeken (overnachtingen)
  - type: associatie
    bedrijfsobject: "[[Horecabedrijf]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: Een hotel is een type horecabedrijf
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal begrip in horecabeleid, apart gereguleerd |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in economisch en toeristisch beleid |
| Heeft een eigen bestaan | ✅ | Fysiek gebouw met eigen exploitatie |
| Kan in meervoud bestaan | ✅ | Utrecht telt 59 accommodaties / 30 logiesaccommodaties |
| Heeft een eigen levenscyclus | ✅ | Initiatief → vergunning → exploitatie → eventueel sluiting |
| Heeft relaties met andere concepten | ✅ | Vestiging, hotelbezoek, horecabedrijf, toeristenbelasting |

6/6 criteria — BO.

## Beschrijving

Een hotel is een verblijfsaccommodatie waar gasten tegen betaling kunnen overnachten. De gemeente Utrecht reguleert hotelvestiging via de beleidsregel hotels, die drie typeringen onderscheidt: concepthotels (thematisch), doelgroephotels (specifieke doelgroep) en minihotels (max 2 kamers). Het beleid is gericht op diversiteit in het aanbod en het voorkomen van massatoerisme.

Nieuwe hotelvestigingen vereisen een omgevingsvergunning bij afwijking van het omgevingsplan. Bestaande hotels mogen groeien met maximaal 20% van hun kamercapaciteit per 1 april 2020.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Concepthotel | Hotel met max 50 kamers rond een specifiek thema | — |
| Doelgroephotel | Hotel voor specifieke groepen (zorg, sport), max 50 kamers | — |
| Minihotel | Klein hotel met max 2 kamers | — |

De subtypes zijn beleidsmatige categorieën uit de beleidsregel hotels (2026), geen GGM-enumeratie.

## GGM-bron

> "Gebouw waar je tegen betaling kunt logeren." — GGM, Model Economie

- **Entiteit**: Hotel
- **Beleidsdomein**: 3 Economie
- **Attributen**: aantalKamers
- **Overerving**: Hotel → Vestiging (abstract)
- **Matchsterkte**: **exact** — GGM-entiteit en BO zijn hetzelfde concept

De GGM-definitie is summier maar correct. De beleidsregel voegt typeringen en voorwaarden toe die het GGM niet modelleert.

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Vestiging]] | generalisatie | Hotel → Vestiging | — | GGM (overerving) |
| [[Hotelbezoek]] | associatie | Hotel → Hotelbezoek | 1..* | GGM |
| [[Horecabedrijf]] | associatie | Horecabedrijf → Hotel | 1 | Beleid |

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
