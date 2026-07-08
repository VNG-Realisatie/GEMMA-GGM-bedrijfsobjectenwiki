---
type: bedrijfsobject
naam: Schuld
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Schuld
ggm_guid: EAID_93E12A3E_71E3_431e_9871_BF6075EAAEF1
ggm_uml_type: Class
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "Schulden"
ggm_diagram: [Schuldhulp Client]
ggm_definitie: "Een schuld is een financiële verplichting waarbij een persoon nu of in de toekomst een bedrag moet betalen aan een derde. In het kader van schuldhulpverlening wordt over een schuld gesproken als de persoon niet aan deze verplichting kan voldoen."
ggm_herkomst: GGM

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Schuld** als directe tegenhanger.
bo_definitie: "Financiële verplichting van een inwoner aan een schuldeiser, waaraan de inwoner niet kan voldoen."
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[schuldhulptraject]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Schulden zijn onderdeel van een traject"
  - type: associatie
    bedrijfsobject: "[[schuldeiser]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Elke schuld is bij één schuldeiser"
bedrijfsprocessen: [schuldhulpverlening]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Financiële verplichting met eigen bedrag, peildatum en schuldsoort. Meerdere schulden per traject, elk bij een andere schuldeiser. Eigen levenscyclus (ontstaan → geïnventariseerd → gesaneerd/kwijtgescholden).

## Beschrijving

Een schuld is een individuele financiële verplichting van een inwoner aan een derde partij. Bij aanvang van het schuldhulptraject worden alle schulden geïnventariseerd. De gemiddelde totale schuld bij aanmelding in Den Haag is €42.900. Schulden worden onderscheiden naar schuldsoort (zakelijk/particulier) en kunnen formeel of informeel zijn.

## Subtypes

Herkende specialisaties van schuld. Geen apart BO.

- **Informele schuld** — schuld aan familie of vrienden, zonder formeel bewijs. Kan onder voorwaarden worden meegenomen in een schuldregeling.

## GGM-bron

> "Een schuld is een financiële verplichting waarbij een persoon nu of in de toekomst een bedrag moet betalen aan een derde."

- **Entiteit:** Schuld
- **Beleidsdomein:** Schuldhulpverlening
- **Attributen:** bedrag, peildatum, zakelijkeSchuld, schuldsoort
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie is generiek ("een persoon", "een derde"). De BO-definitie specificeert de gemeentelijke context: het gaat om een inwoner die niet aan een financiële verplichting kan voldoen.

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[schuldhulptraject\|Schuldhulptraject]] | 0..* | Onderdeel van traject |
| associatie | [[schuldeiser\|Schuldeiser]] | 1 | Schuld bij één schuldeiser |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
