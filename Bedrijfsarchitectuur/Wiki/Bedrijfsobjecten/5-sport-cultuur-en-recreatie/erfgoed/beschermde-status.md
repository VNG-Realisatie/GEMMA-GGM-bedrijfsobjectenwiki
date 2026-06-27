---
type: bedrijfsobject
naam: Beschermde Status
domein: [Erfgoed]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Beschermde Status
ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
ggm_uml_type: Class
ggm_beleidsdomein: Monumenten
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Diagram Monumenten, Diagram Monumenten Detail]
ggm_diagram_ids: [EAID_7429E175_1CBE_4336_BF92_6C5029395E69, EAID_58EA4966_DBC2_4359_94C4_ABC774DBE5E2]
ggm_definitie: "Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente,"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: BeschermdeStatus
ggm_gemma_guid: 4ebf7f05-0ff1-4d2e-aa62-879be7565dd7
ggm_gemma_definitie: "Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-arc"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-4ebf7f05-0ff1-4d2e-aa62-879be7565dd7"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Status van de bescherming van een monument."
bo_toelichting: "Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks-, provinciaal of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente."
bo_subtypes:
  - naam: Rijksmonument
    omschrijving: "Monument beschermd op grond van de Erfgoedwet door het Ministerie van OCW"
    ggm_entiteit: Beschermde Status
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: type
  - naam: Gemeentelijk monument
    omschrijving: "Monument beschermd op grond van de gemeentelijke monumentenverordening"
    ggm_entiteit: Beschermde Status
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: type
  - naam: Beschermd stadsgezicht
    omschrijving: "Ruimtelijk en cultuurhistorisch waardevol gebied beschermd krachtens de Erfgoedwet"
    ggm_entiteit: Beschermde Status
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: type
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Pand]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Pand kan een beschermde status hebben"
  - type: associatie
    bedrijfsobject: "[[Kadastrale Onroerende Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Kadastraal object met beschermde status"
bedrijfsprocessen: [monumentenzorg, vergunningverlening, handhaving]
bedrijfsfuncties: [erfgoedbeheer, vergunningverlening]
---

## BO-criteria toetsing

| Criterium | Score |
|-----------|-------|
| Heeft betekenis binnen het domein | ✅ Kernbegrip in monumentenzorg en erfgoedbeheer |
| Herkenbaar voor domeinexperts | ✅ Wettelijk begrip uit de Erfgoedwet |
| Eigen bestaan | ✅ Bestaat onafhankelijk — een aanwijzingsbesluit kent de status toe |
| Meervoud | ✅ Meerdere beschermde statussen per gemeente |
| Eigen levenscyclus | ✅ Aanwijzing, wijziging, intrekking |
| Relaties | ✅ Pand, kadastrale zaak, omgevingsvergunning |

Score: 6/6.

## Beschrijving

Een beschermde status is de formele aanwijzing waarmee een monument, erfgoed of stadsgezicht wettelijke bescherming krijgt. De bescherming kan op drie niveaus worden toegekend: door het Rijk (rijksmonument), de provincie (provinciaal monument) of de gemeente (gemeentelijk monument). Bij beschermde stadsgezichten gaat het om een gebiedsaanwijzing voor ruimtelijk en cultuurhistorisch waardevolle gebieden.

De beschermde status heeft directe gevolgen voor het welstandsbeleid: bij rijks- of gemeentelijke monumenten en in beschermde stadsgezichten gelden geen standaard welstandscriteria maar vindt maatwerk plaats door de Commissie Welstand en Monumenten. Vergunningvrij bouwen is bij monumenten en in beschermde stadsgezichten sterk beperkt.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---------|-------------|--------------|
| Rijksmonument | Beschermd op grond van de Erfgoedwet door het Ministerie van OCW | [Beschermde Status](monumenten.md) |
| Gemeentelijk monument | Beschermd op grond van de gemeentelijke monumentenverordening | [Beschermde Status](monumenten.md) |
| Beschermd stadsgezicht | Ruimtelijk en cultuurhistorisch waardevol gebied, beschermd krachtens de Erfgoedwet | [Beschermde Status](monumenten.md) |

De GGM modelleert alle subtypes als waarden van het `type`-attribuut op de entiteit Beschermde Status. Het attribuut `gezichtscode` is specifiek voor beschermde stadsgezichten.

## GGM-bron

> "Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente,"
> — GGM entiteit: Beschermde Status, beleidsdomein: Monumenten

**Matchsterkte:** exact. De GGM-entiteit beschrijft hetzelfde concept.

**GGM-attributen:** rijksmonumentcode, gemeentelijkMonumentCode, datumInschrijvingRegister, naam, type, gezichtscode, complex, opmerkingen, bronnen, omschrijving.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---------|----------|---------------|------|
| [[Pand]] | Beschermde Status → Pand | 0..* | GGM |
| [[Kadastrale Onroerende Zaak]] | Beschermde Status → KadastraleOnroerendeZaak | 0..* | GGM |
| Ambacht | Beschermde Status → Ambacht | 0..* | GGM |
| Bouwstijl | Beschermde Status → Bouwstijl | 0..* | GGM |
| Bouwtype | Beschermde Status → Bouwtype | 0..* | GGM |
| Bouwactiviteit | Beschermde Status → Bouwactiviteit | 0..* | GGM |
| Oorspronkelijke Functie | Beschermde Status → OorspronkelijkeFunctie | 0..* | GGM |
| Foto | Beschermde Status → Foto | 0..* | GGM |
| Openbare Ruimte | Beschermde Status → OpenbareRuimte | 0..* | GGM |

## Bedrijfsprocessen

- Monumentenzorg (aanwijzen, wijzigen, intrekken beschermde status)
- Vergunningverlening (monumentenvergunning, omgevingsvergunning bij beschermde objecten/gebieden)
- Handhaving (toezicht op naleving beschermingsregels)

## Bedrijfsfuncties

- Erfgoedbeheer
- Vergunningverlening


## Subtypes

- **Rijksmonument** — Monument beschermd op grond van de Erfgoedwet door het Ministerie van OCW
- **Gemeentelijk monument** — Monument beschermd op grond van de gemeentelijke monumentenverordening
- **Beschermd stadsgezicht** — Ruimtelijk en cultuurhistorisch waardevol gebied beschermd krachtens de Erfgoedwet

## Bronnen

- [[Wiki/Bronsamenvattingen/Cultuur/kunst-en-cultuur]]
- [[Wiki/Bronsamenvattingen/Cultuur/propositie-cultuur]]
- [[Wiki/Bronsamenvattingen/Cultuur/architectuur-en-erfgoed]]
- [[Wiki/Bronsamenvattingen/Cultuur/bibliotheekwerk]]
- [[Wiki/Bronsamenvattingen/Cultuur/toelichting-ringenmodel]]
- [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht]]
- [[Wiki/Bronsamenvattingen/Cultuur/visie-religieus-erfgoed-2025]]
- [[Wiki/Bronsamenvattingen/Cultuur/erfgoedbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Cultuur/bijlagen-visie-religieus-erfgoed]]
