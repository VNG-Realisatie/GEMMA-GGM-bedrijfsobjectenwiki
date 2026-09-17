---
type: element
naam: Museumobject
onderwerp: [Cultuur]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Museumobject"
ggm_guid: EAID_BBCF9DBE_70AD_431c_B698_7F0D69D07050
ggm_uml_type: Class
ggm_beleidsdomein: "Musea"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Generieke entiteiten Erfgoed, Prinsenhof Collectie]
ggm_diagram_ids: [EAID_B7192738_00E7_4b65_902A_B8292E79261B, EAID_B2D890F1_6B7C_45df_9A70_8C40CE1B3611]
ggm_definitie: "Beschrijving van een fenomeen in de werkelijkheid met een zekere cultuurhistorische waarde die deel uitmaakt van de culthuurhistorisch object index. Een museum object kan gedifiniëerd worden als een object met betrekking tot gebouwd, archeologisch, roerend of cultuurlandschappelijk erfgoed. Denk hierbij bijvoorbeeld aan een gebouwd of archeologisch rijksmonument, een schilderij of een beschermd stads- of dorpsgezicht."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Museumobject"
ggm_gemma_guid: "e963434a-50be-4619-b041-58689adc00de"
ggm_gemma_definitie: "Beschrijving van een fenomeen in de werkelijkheid met een zekere cultuurhistorische waarde die deel uitmaakt van de culthuurhistorisch object index. Een museum object kan gedifiniëerd worden als een object met betrekking tot gebouwd, archeologisch, roeren"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-e963434a-50be-4619-b041-58689adc00de"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Museumobject** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Auteur** (detail) — Detailgegeven (weinig attributen)
  - **Bruikleen** (detail) — Operationeel contract, specifiek museaal; geen apart BO naast Museumobject
  - **Historisch Persoon** (detail) — Detailgegeven (geassocieerd met BO)
  - **Incident** (detail) — Detailgegeven (geassocieerd met BO)
  - **Lener** (detail) — Detailgegeven (weinig attributen)
  - **Standplaats** (detail) — Detailgegeven (geassocieerd met BO)
  - **Tentoonstelling** (detail) — Operationele activiteit van museum, geen gemeentelijk registratieobject
  - **Zaal** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Object met cultuurhistorische waarde dat deel uitmaakt van een museale collectie, beheerd door de gemeente of een gemeentelijk museum."
bo_toelichting:
bedrijfsprocessen: [Collectiebeheer, Verwerving en afstoting, Bruikleen]
bedrijfsfuncties: [Erfgoedbeheer, Collectiebeheer]
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "*(Erfgoed Object — abstract)*"
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Museumobject is een specialisatie van Erfgoed Object
  - type: associatie
    bedrijfsobject: "*(Collectie)*"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een collectie bevat museumobjecten
  - type: associatie
    bedrijfsobject: "*(Tentoonstelling)*"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een museumobject kan onderdeel zijn van tentoonstellingen
---

# Museumobject

Object met cultuurhistorische waarde dat deel uitmaakt van een museale collectie. Gemeenten die een museum beheren registreren museumobjecten met herkomst, afmeting, medium en verbindingen met historische personen en tentoonstellingen.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernobject in museaal collectiebeheer |
| Herkenbaar voor experts | ✅ | Conservator, collectiebeheerder kennen dit |
| Eigen bestaan | ✅ | Een museumobject bestaat onafhankelijk van collectie of tentoonstelling |
| Meervoud | ✅ | Museale collecties bevatten honderden tot duizenden objecten |
| Eigen levenscyclus | ✅ | Verwerving → registratie → beheer → eventueel afstoting of bruikleen |
| Relaties | ✅ | Met Collectie, Tentoonstelling, Historisch Persoon, Standplaats |

## GGM-bron

> **Museumobject**: Beschrijving van een fenomeen in de werkelijkheid met een zekere cultuurhistorische waarde die deel uitmaakt van de culthuurhistorisch object index. Een museum object kan gedifiniëerd worden als een object met betrekking tot gebouwd, archeologisch, roerend of cultuurlandschappelijk erfgoed. Denk hierbij bijvoorbeeld aan een gebouwd of archeologisch rijksmonument, een schilderij of een beschermd stads- of dorpsgezicht.
> — *GGM v2.5.1, Musea (taakveld 5 Sport, Cultuur en Recreatie)*

**Entiteit:** Museumobject
**Attributen:** verkrijging, medium, afmeting, bezitVanaf, bezitTot
**Matchsterkte:** exact

Museumobject erft in het GGM van **Erfgoed Object** (abstract). Het Musea-beleidsdomein is sterk gekleurd door het Prinsenhof (Delft) — de operationele entiteiten (Balieverkoop, Winkelvoorraaditem, Reservering, etc.) zijn specifiek voor dat museum en niet relevant op bedrijfsobjectniveau.

## Generalisatie

```
Erfgoed Object (abstract)
    ├── Archiefstuk  → BO [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|archiefstuk]]
    └── Museumobject → dit BO
```

Archiefstukken en museumobjecten zijn voor gemeenten herkenbaar verschillende dingen met eigen processen (archiefbeheer vs. collectiebeheer). Daarom aparte BO's, niet één abstract "Erfgoedobject" als BO.

## BO-definitie

De GGM-definitie beschrijft technische implementatiedetails in plaats van het concept zelf. De BO-definitie beschrijft het begrip vanuit de gemeentelijke praktijk.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Bevat in collectie | *(Collectie)* | Collectie → Museumobject [0..*..0..*] | Container, geen apart BO |
| Onderdeel van tentoonstelling | *(Tentoonstelling)* | Museumobject → Tentoonstelling [0..*..0..*] | Activiteit, geen apart BO |
| Heeft verbinding met | *(Historisch Persoon)* | Museumobject → Historisch Persoon [0..*..0..*] | Context, geen apart BO |
| Op standplaats | *(Standplaats)* | Museumobject → Standplaats [0..*..0..1] | Fysieke locatie in museum |
| Betreft bruikleen | *(Bruikleen)* | Museumobject → Bruikleen [0..*..0..1] | Operationeel |
| Specialisatie van | *(Erfgoed Object)* | Generalisatie | Abstract parent |

## Bedrijfsprocessen

- **Collectiebeheer**: registratie, documentatie, conservering van objecten
- **Verwerving en afstoting**: aankoop, schenking, ruil, of verantwoorde afstoting
- **Bruikleen**: uitlening aan of van andere instellingen

## Bedrijfsfuncties

- Erfgoedbeheer
- Collectiebeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/erfgoed/erfgoedwet]]
- [[Wiki/Bronsamenvattingen/Cultuur/kunst-en-cultuur]]
- [[Wiki/Bronsamenvattingen/Cultuur/architectuur-en-erfgoed]]
