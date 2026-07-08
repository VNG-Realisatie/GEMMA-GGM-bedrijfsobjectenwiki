---
type: bedrijfsobject
naam: Moratorium
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Moratorium
ggm_guid: EAID_5FC12BE5_75F0_4dd9_8DA7_993C03F3700A
ggm_uml_type: Class
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "Schulden"
ggm_diagram: [Schuldhulpproces]
ggm_definitie: "Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter. Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is."
ggm_herkomst: GGM

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Moratorium** als directe tegenhanger.
bo_definitie: "Verzoek aan de rechter om schuldeisers tijdelijk te blokkeren tijdens een lopende aanvraag voor een minnelijke schuldregeling."
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[schuldhulptraject]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een traject kan meerdere moratoria bevatten"
bedrijfsprocessen: [schuldhulpverlening]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Juridisch instrument met eigen levenscyclus (aanvraag → goedkeuring → start → eind), maximaal 6 maanden. Meerdere mogelijk per traject. Eigen rechtsgronslag (art. 287b Fw).

## Beschrijving

Een moratorium is een tijdelijke opschorting van inningsmogelijkheden door schuldeisers, op verzoek aan de rechter. Het beschermt de inwoner tegen gedwongen woningontruiming, beëindiging van energie/water of opzegging van de zorgverzekering, terwijl de minnelijke schuldregeling in behandeling is. Maximale duur: zes maanden.

## GGM-bron

> "Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt."

- **Entiteit:** Moratorium
- **Beleidsdomein:** Schuldhulpverlening
- **Attributen:** datumAanvraag, datumGoedkeuring, startdatum, einddatum
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie beschrijft technische implementatiedetails ("het gaat hier om de datum waarop een verzoek tot een moratorium is ingediend") in plaats van het concept zelf. De bron (Beleidsplan Schuldhulpverlening Den Haag) definieert moratorium als verzoek aan de rechter om schuldeisers tijdelijk te blokkeren.

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[schuldhulptraject\|Schuldhulptraject]] | 0..* | Onderdeel van traject |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
