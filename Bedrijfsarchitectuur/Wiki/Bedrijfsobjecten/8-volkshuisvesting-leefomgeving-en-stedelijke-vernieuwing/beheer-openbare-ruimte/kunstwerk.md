---
type: bedrijfsobject
naam: Kunstwerk
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Kunstwerk"
ggm_guid: EAID_71BCDE9D_88C2_4519_8105_028E40898AB
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: [EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3]
ggm_definitie: "Civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen en niet bedoeld voor permanent menselijk verblijf."
ggm_toelichting: ""
ggm_synoniemen: ""
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
bo_definitie: "Civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen en niet bedoeld voor permanent menselijk verblijf."
bo_toelichting: ''
bo_subtypes:
  - naam: "Brug"
    omschrijving: "Kunstwerk over een waterweg, bestaande uit een brugdek gesteund door pijlers en/of landhoofden"
    ggm_entiteit: Brug
    ggm_guid: EAID_B56B8C37_AA54_4266_B96B_C466946D1C3
    ggm_attribuut: generalisatie
  - naam: "Viaduct"
    omschrijving: "Kunstwerk over een weg of spoorweg, bestaande uit een dek gesteund door pijlers en/of landhoofden"
    ggm_entiteit: Viaduct
    ggm_guid: EAID_4824C467_3BF6_45C2_BD8B_03F04CEBCA9
    ggm_attribuut: generalisatie
  - naam: "Flyover"
    omschrijving: Viaductvormig kunstwerk waarmee een verkeersstroom over ongelijkvloerse kruisingen wordt geleid
    ggm_entiteit: Flyover
    ggm_guid: EAID_12F592F4_8E38_49B7_8DEF_F9B84A874BB
    ggm_attribuut: generalisatie
  - naam: "Kademuur"
    omschrijving: Verticale wand ter scheiding van land en water
    ggm_entiteit: Kademuur
    ggm_guid: EAID_22C76A86_D969_464E_87CD_53466BD75FC
    ggm_attribuut: generalisatie
  - naam: "Keermuur"
    omschrijving: "Muur die door vorm, gewicht en fundering de grond keert"
    ggm_entiteit: Keermuur
    ggm_guid: EAID_D629609F_088E_4504_99BB_C45F0EA633F
    ggm_attribuut: generalisatie
  - naam: "Sluis"
    omschrijving: Waterbouwkundig kunstwerk voor het overbruggen van niveauverschillen in vaarwegen
bo_relaties:
  - type: generalisatie
    bedrijfsobject: Beheerobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Kunstwerk is een specialisatie van Beheerobject
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/verhardingsobject|Verhardingsobject]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: Verharding loopt over/langs kunstwerken
bedrijfsprocessen: [Inspectie civiele constructies, Groot onderhoud kunstwerken, Vervanging kunstwerken, Conservering]
bedrijfsfuncties: [Beheer openbare ruimte, Civiel beheer]
ggm_gemma_naam: "Kunstwerk"
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel voor bereikbaarheid en waterbeheer van de stad |
| Is herkenbaar voor domeinexperts | ✅ | Bruggen, viaducten, kademuren — standaardterminologie in civiel beheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elk kunstwerk individueel geregistreerd met naam, nummer, conditiescore |
| Kan in meervoud bestaan | ✅ | Honderden bruggen, viaducten en kademuren in de gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanleg → conservering → groot onderhoud → renovatie → vervanging; levensduur 50-70 jaar |
| Heeft relaties met andere concepten | ✅ | Verharding, inspectie, melding, overbruggingsobject, fundament |

Score: 6/6.

## Beschrijving

Een kunstwerk is een civiel-technische constructie in de openbare ruimte: bruggen, viaducten, kademuren, keermuren, tunnels en flyovers. De gemeente registreert elk kunstwerk met objectnaam, objectnummer, constructietype, materiaal, conditiescore en vervangingswaarde. De levensduur varieert: bruggen 60-70 jaar, kademuren vergelijkbaar.

In Utrecht bedraagt het achterstallig onderhoud voor civiele constructies €7,6 miljoen (90% zekerheidspercentage). De kwaliteit van oeverconstructies is nog niet volledig in beeld. Het uitstel van onderhoud bij kunstwerken kan leiden tot afsluitingen van bruggen, wat de bereikbaarheid van de stad in gevaar brengt.

De nota noemt de Dafne Schippersbrug als voorbeeld van toenemende complexiteit: een brug die tegelijk fietsdak en schooldak is, waardoor eenvoudig onderhoud niet volstaat.

In het GGM is Kunstwerk een abstract object met specialisaties Gemaal, Overstortconstructie en Uitlaatconstructie. Daarnaast zijn Brug, Viaduct, Flyover, Kademuur en Keermuur als aparte entiteiten gemodelleerd die via Overbruggingsobject gerelateerd zijn.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Brug | Kunstwerk over een waterweg, brugdek op pijlers/landhoofden | [Brug](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |
| Viaduct | Kunstwerk over een weg of spoorweg | [Viaduct](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |
| Flyover | Viaductvormig kunstwerk voor ongelijkvloerse verkeerskruising | [Flyover](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |
| Kademuur | Verticale wand ter scheiding van land en water | [Kademuur](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |
| Keermuur | Muur die door vorm/gewicht/fundering de grond keert | [Keermuur](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |
| Sluis | Waterbouwkundig kunstwerk voor het overbruggen van niveauverschillen in vaarwegen | — (GGM-hiaat) |

De subtypes zijn geen GGM-kinderen van Kunstwerk (die zijn: Gemaal, Overstortconstructie, Uitlaatconstructie — water-infra). In het GGM zijn Brug/Viaduct/Flyover kinderen van **Overbruggingsobject** en Kademuur/Keermuur kinderen van **Scheiding**. Vanuit beleidsperspectief groepeert de nota ze als "civiele constructies" onder één beheerregime.

## GGM-bron

> "Civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen en niet bedoeld voor permanent menselijk verblijf."

- **Entiteit**: Kunstwerk
- **Beleidsdomein**: Beheer Openbare Ruimte (Model IMBOR)
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Attributen** (30): aanleghoogte, antiGraffitiVoorziening, bereikbaarheid, breedte, constructietype, gewicht, hoogte, installateur, jaarConserveren, jaarOnderhoudUitgevoerd, jaarRenovatie, jaarVervanging, kilometreringBegin, kilometreringEinde, kleur, kunstwerkBereikbaarheidPlus, kunstwerkMateriaal, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, leverancier, looprichel, minimumConditiescore, monument, monumentnummer, objectnaam, objectnummer, onderhoudsregime, oppervlakte, orientatie, technischeLevensduur, typeFundering, typeMonument, vervangingswaarde, wegnummer

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Beheerobject (GGM) | Kunstwerk → Beheerobject | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/verhardingsobject\|Verhardingsobject]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Inspectie civiele constructies**: conditiebeoordeling, veiligheidsinspectie, oeverinspectie
- **Groot onderhoud kunstwerken**: conservering, voegwerk, betonreparatie
- **Vervanging kunstwerken**: vervanging bij einde levensduur of functionele noodzaak


## Subtypes

- **Brug** — Kunstwerk over een waterweg, bestaande uit een brugdek gesteund door pijlers en/of landhoofden
- **Viaduct** — Kunstwerk over een weg of spoorweg, bestaande uit een dek gesteund door pijlers en/of landhoofden
- **Flyover** — Viaductvormig kunstwerk waarmee een verkeersstroom over ongelijkvloerse kruisingen wordt geleid
- **Kademuur** — Verticale wand ter scheiding van land en water
- **Keermuur** — Muur die door vorm, gewicht en fundering de grond keert
- **Sluis** — Waterbouwkundig kunstwerk voor het overbruggen van niveauverschillen in vaarwegen

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
