---
type: bedrijfsobject
naam: Speeltoestel
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Speeltoestel"
ggm_guid: EAID_4EFB3A19_E491_469F_AA96_DEBED9C1BE4
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "Toestel en structuren, met inbegrip van componenten en constructieve onderdelen, waarmee of waarop kinderen binnen of buiten kunnen spelen, individueel of gezamenlijk, volgens hun eigen spelregels of beweegredenen, die te allen tijde kunnen worden gewijzigd."
ggm_toelichting: ""
ggm_synoniemen: "Speelvoorziening"
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Toestel of constructie in de openbare ruimte bestemd voor spel en beweging, met certificering en periodieke veiligheidsinspectie."
gemma_subtypes:
  - naam: Vast speeltoestel
    omschrijving: "Permanent geplaatst speeltoestel op een speelterrein (schommel, glijbaan, klimrek)"
    ggm_entiteit: Speeltoestel
    ggm_guid: EAID_4EFB3A19_E491_469F_AA96_DEBED9C1BE4
    ggm_attribuut: toestelgroep
  - naam: Sportcontainer
    omschrijving: "Modulaire container met sportvoorzieningen, verplaatsbaar naar andere locatie"
    ggm_entiteit: Speeltoestel
    ggm_guid: EAID_4EFB3A19_E491_469F_AA96_DEBED9C1BE4
    ggm_attribuut: toestelgroep
  - naam: Skatepark/freerunbaan
    omschrijving: "Modulair systeem van elementen voor skateboarden of freerunnen"
    ggm_entiteit: Speeltoestel
    ggm_guid: EAID_4EFB3A19_E491_469F_AA96_DEBED9C1BE4
    ggm_attribuut: toestelgroep
bronnen:
  - [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
relaties:
  - type: generalisatie
    bedrijfsobject: Meubilair (GGM)
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Speeltoestel is een specialisatie van Meubilair in het GGM
bedrijfsprocessen: [Inspectie speeltoestellen, Onderhoud speelplekken, Vervanging speeltoestellen, Herinrichting speelplekken]
bedrijfsfuncties: [Beheer openbare ruimte, Spelen]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Speeltoestellen zijn essentieel voor een kindvriendelijke openbare ruimte |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in beheer en Warenwetbesluit attractie- en speeltoestellen |
| Heeft een eigen bestaan binnen het domein | ✅ | Elk toestel individueel geregistreerd met serienummer, certificaat, veiligheidsklasse |
| Kan in meervoud bestaan | ✅ | Honderden speeltoestellen op speelplekken door de hele gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanschaf → plaatsing → periodieke inspectie → onderhoud → vervanging; afschrijvingstermijn 15 jaar |
| Heeft relaties met andere concepten | ✅ | Speelterrein, inspectie, valhoogte, certificering, groenobject |

Score: 6/6.

## Beschrijving

Een speeltoestel is een toestel of structuur in de openbare ruimte waarop kinderen kunnen spelen. De gemeente registreert elk toestel met toestelcode, certificaatnummer, certificeringsinstantie, catalogusprijs, technische levensduur en vrije valhoogte. Speeltoestellen worden vier keer per jaar geïnspecteerd op veiligheid en op B-niveau onderhouden.

De afschrijvingstermijn is 15 jaar. De Nota Beheer OR vermeldt dat er geen achterstallig onderhoud is bij speeltoestellen — de reguliere inspectie en onderhoudscyclus functioneert. Bij herinrichting van speelplekken past de gemeente ontwikkelend beheer toe: speelplekken worden vergroend en klimaatbestendig gemaakt, zodat ze ook bijdragen aan wateropvang en koele plekken in de buurt.

In het GGM is Speeltoestel een specialisatie van Meubilair. Het is gerelateerd aan Speelterrein (een FunctioneelGebied dat het geheel van begroeiing, verharding en speeltoestellen omvat).

## Specialisaties

| Subtype | Omschrijving | Bron |
|---|---|---|
| Vast speeltoestel | Permanent geplaatst toestel: schommel, glijbaan, klimrek, wipwap | Kadernota KOR (4.500 stuks) |
| Sportcontainer | Modulaire container met sportvoorzieningen, verplaatsbaar | Nota Beheer OR (voorbeeld flexibele openbare ruimte) |
| Skatepark/freerunbaan | Modulair systeem van elementen voor skateboarden of freerunnen | Nota Beheer OR (voorbeeld modulaire speelvoorziening) |

De nota noemt sportcontainers, skateparks en freerunbanen als voorbeelden van "flexibele, multifunctionele en modulaire openbare ruimte" die makkelijk verplaatsbaar zijn. In het GGM wordt het onderscheid geïmplementeerd via het attribuut `toestelgroep`.

## GGM-bron

> "Toestel en structuren, met inbegrip van componenten en constructieve onderdelen, waarmee of waarop kinderen binnen of buiten kunnen spelen, individueel of gezamenlijk, volgens hun eigen spelregels of beweegredenen, die te allen tijde kunnen worden gewijzigd."

- **Entiteit**: Speeltoestel
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Attributen** (23): catalogusprijs, certificaat, certificaatnummer, certificeringsinstantie, controlefrequentie, datumCertificaat, gemakkelijkToegankelijk, inspectievolgorde, installatiekosten, speelterrein, speeltoestelToestelonderdeel, technischeLevensduur, toestelcode, toestelgroep, toestelnaam, type, typenummer, typePlus, typePlus2, valruimteHoogte, valruimteOmvang, vrijeValhoogte

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Meubilair (GGM) | Speeltoestel → Meubilair | GGM |

## Bedrijfsprocessen

- **Inspectie speeltoestellen**: viermaal per jaar visuele en technische inspectie op veiligheid
- **Onderhoud speelplekken**: reparatie, vervanging onderdelen, ondergrondonderhoud
- **Vervanging speeltoestellen**: vervanging bij einde levensduur of veiligheidsproblemen
- **Herinrichting speelplekken**: vergroening, klimaatadaptatie, afstemming op leeftijdsdoelgroep wijk
