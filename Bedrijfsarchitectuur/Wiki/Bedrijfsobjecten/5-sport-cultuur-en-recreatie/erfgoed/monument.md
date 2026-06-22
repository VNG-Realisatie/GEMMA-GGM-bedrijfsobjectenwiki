---
type: bedrijfsobject
naam: Monument
domein: [Cultuur]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Beschermde Status"
ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
ggm_uml_type: Class
ggm_beleidsdomein: "Monumenten"
ggm_taakveld: "Erfgoed"
ggm_diagram: [Diagram Monumenten, Diagram Monumenten Detail]
ggm_diagram_ids: [EAID_7429E175_1CBE_4336_BF92_6C5029395E69, EAID_58EA4966_DBC2_4359_94C4_ABC774DBE5E2]
ggm_definitie: "Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente,"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "BeschermdeStatus"
ggm_gemma_guid: "4ebf7f05-0ff1-4d2e-aa62-879be7565dd7"
ggm_gemma_definitie: "Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-arc"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-4ebf7f05-0ff1-4d2e-aa62-879be7565dd7"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Beschermd onroerend erfgoed (rijks-, provinciaal of gemeentelijk) waarvan de cultuurhistorische waarde is vastgesteld en dat is ingeschreven in het monumentenregister."
gemma_subtypes:
  - naam: kerkgebouw
    omschrijving: "Religieus gebouw (kapittels, parochiekerken, kloosters)"
    ggm_entiteit: "Beschermde Status"
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: "type"
  - naam: beschermd stadsgezicht
    omschrijving: "Rijks- of gemeentelijk beschermd stads- of dorpsgezicht"
    ggm_entiteit: "Beschermde Status"
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: "gezichtscode"
  - naam: synagoge
    omschrijving: "Joods gebedshuis"
    ggm_entiteit: "Beschermde Status"
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: "type"
  - naam: klooster
    omschrijving: "Kloostergebouw of -complex"
    ggm_entiteit: "Beschermde Status"
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: "type"
  - naam: woonhuis
    omschrijving: "Beschermd woonhuis of grachtenpand"
    ggm_entiteit: "Beschermde Status"
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: "type"
  - naam: verdedigingswerk
    omschrijving: "Fort, muur of ander militair erfgoed (Waterlinie, Limes)"
    ggm_entiteit: "Beschermde Status"
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: "type"
  - naam: openbare ruimte
    omschrijving: "Beschermd park, plantsoen of singel (Zocherplantsoen)"
    ggm_entiteit: "Beschermde Status"
    ggm_guid: EAID_32C02923_EE3A_4553_B94B_31E0C273A829
    ggm_attribuut: "type"
  - naam: luidklok
    omschrijving: "Klok in kerktoren, deels met eigen monumentstatus"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: ""
bedrijfsprocessen: [Monumentenaanwijzing, Monumentenvergunning, Erfgoedtoezicht]
bedrijfsfuncties: [Erfgoedbeheer, Vergunningverlening]
bronnen: [Wiki/Bronsamenvattingen/Cultuur/kunst-en-cultuur, Wiki/Bronsamenvattingen/Cultuur/propositie-cultuur, Wiki/Bronsamenvattingen/Cultuur/architectuur-en-erfgoed, Wiki/Bronsamenvattingen/Cultuur/bibliotheekwerk, Wiki/Bronsamenvattingen/Cultuur/toelichting-ringenmodel, Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht, Wiki/Bronsamenvattingen/Cultuur/visie-religieus-erfgoed-2025, Wiki/Bronsamenvattingen/Cultuur/erfgoedbeleid-utrecht, Wiki/Bronsamenvattingen/Cultuur/bijlagen-visie-religieus-erfgoed]
relaties:
  - type: associatie
    bedrijfsobject: "*(Pand — BAG)*"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een monument betreft een of meer panden
  - type: associatie
    bedrijfsobject: "*(KadastraleOnroerendeZaak — Kadaster)*"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een monument betreft een of meer kadastrale objecten
  - type: associatie
    bedrijfsobject: "*(OpenbareRuimte — BAG)*"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een beschermd gezicht betreft een of meer openbare ruimten
---

# Monument

Beschermd onroerend erfgoed waarvan de cultuurhistorische waarde formeel is vastgesteld door een overheid. Gemeenten wijzen zelf gemeentelijke monumenten en beschermde stads- en dorpsgezichten aan en houden het gemeentelijk monumentenregister bij.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernregistratie in het erfgoeddomein |
| Herkenbaar voor experts | ✅ | Elke gemeente kent het monumentenregister |
| Eigen bestaan | ✅ | Een monument bestaat onafhankelijk van processen eromheen |
| Meervoud | ✅ | Gemeenten hebben tientallen tot duizenden monumenten |
| Eigen levenscyclus | ✅ | Aanwijzing → inschrijving register → eventueel intrekking |
| Relaties | ✅ | Met Pand (BAG), KadastraleOnroerendeZaak, OpenbareRuimte |

## GGM-bron

> **Beschermde Status**: Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente,
> — *GGM v2.5.1, Monumenten (taakveld 5 Sport, Cultuur en Recreatie)*

**Entiteit:** Beschermde Status
**Attributen:** rijksmonumentcode, gemeentelijkMonumentCode, datumInschrijvingRegister, naam, type, gezichtscode, complex, opmerkingen, bronnen, omschrijving
**Matchsterkte:** exact

## BO-definitie

Het bedrijfsobject **Monument** komt overeen met de GGM-entiteit **Beschermde Status**. De naamkeuze "Monument" sluit aan bij het gangbare gemeentelijke taalgebruik — men spreekt van "monumenten" en het "monumentenregister", niet van "beschermde statussen".

De entiteit omvat zowel individuele monumenten als beschermde stads- en dorpsgezichten (via het attribuut `gezichtscode`). Typen bescherming: rijksmonument, provinciaal monument, gemeentelijk monument.

De Erfgoedwet (2016) en de Omgevingswet vormen het wettelijk kader. Gemeenten zijn bevoegd tot aanwijzing van gemeentelijke monumenten en beschermde gezichten.

## Specialisaties

Herkende subtypes van monument. Geen aparte BO's — het zijn waarden van attributen op [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md).

| Subtype | Omschrijving | GGM-attribuut |
|---|---|---|
| kerkgebouw | Religieus gebouw (kapittels, parochiekerken, kloosters) | [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md) → `type` |
| beschermd stadsgezicht | Rijks- of gemeentelijk beschermd stads- of dorpsgezicht | [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md) → `gezichtscode` |
| synagoge | Joods gebedshuis | [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md) → `type` |
| klooster | Kloostergebouw of -complex | [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md) → `type` |
| woonhuis | Beschermd woonhuis of grachtenpand | [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md) → `type` |
| verdedigingswerk | Fort, muur of ander militair erfgoed (Waterlinie, Limes) | [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md) → `type` |
| openbare ruimte | Beschermd park, plantsoen of singel (Zocherplantsoen) | [Beschermde Status](Sources/GGM/5-sport-cultuur-en-recreatie/monumenten.md) → `type` |
| luidklok | Klok in kerktoren, deels met eigen monumentstatus | — |

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Betreft pand | *(Pand — BAG)* | Beschermde Status → Pand [0..*] | Geen — BAG-pand is basisregistratie, geen apart BO in deze wiki |
| Betreft kadastraal object | *(KadastraleOnroerendeZaak)* | Beschermde Status → KadastraleOnroerendeZaak [0..*] | Geen |
| Betreft openbare ruimte | *(OpenbareRuimte)* | Beschermde Status → OpenbareRuimte [0..*] | Voor beschermde gezichten |
| Heeft bouwstijl | *(Bouwstijl)* | Beschermde Status → Bouwstijl [0..*] | Classificatie, geen apart BO |
| Heeft bouwactiviteit | *(Bouwactiviteit)* | Beschermde Status → Bouwactiviteit [0..*] | Classificatie, geen apart BO |
| Heeft foto | *(Foto)* | Beschermde Status → Foto [0..*] | Documentatie, geen apart BO |

De erfgoednota Utrecht bevestigt en verrijkt dit BO met context over verduurzaming (CO2-reductie 40% 2030, monumenten aardgasvrij), herbestemming ("behoud door ontwikkeling"), en de relatie met ruimtelijke ontwikkeling (erfgoed als fundament voor gebiedsontwikkeling). Beschermde stads- en dorpsgezichten (rijks en gemeentelijk) vallen ook onder dit BO via het attribuut `gezichtscode`.

## Bedrijfsprocessen

- **Monumentenaanwijzing**: beoordeling en aanwijzing van gemeentelijke monumenten en beschermde gezichten
- **Monumentenvergunning**: vergunningverlening voor wijzigingen aan monumenten (in samenhang met Omgevingswet)
- **Erfgoedtoezicht**: toezicht op instandhouding en onderhoud
- **Verduurzaming monumenten**: adviseren en faciliteren van energiemaatregelen bij monumenten

## Bedrijfsfuncties

- Erfgoedbeheer
- Vergunningverlening
