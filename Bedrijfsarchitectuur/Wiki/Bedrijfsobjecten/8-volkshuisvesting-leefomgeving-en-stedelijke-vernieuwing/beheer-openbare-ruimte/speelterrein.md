---
type: element
naam: Speelterrein
onderwerp: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Speelterrein"
ggm_guid: EAID_941A17C1_A2B2_4CD1_8991_08B0EBCF0C2
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "Geheel van begroeiing verharding opstallen en speelwerktuigen bedoeld als speelplaats voor kinderen."
ggm_toelichting:
ggm_synoniemen: "Speelplek, Speelgelegenheid"
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
  Dit BO heeft de GGM-entiteit **Speelterrein** als directe tegenhanger.
bo_definitie: "Geheel van begroeiing verharding opstallen en speelwerktuigen bedoeld als speelplaats voor kinderen."
bo_toelichting:
bo_subtypes:
  - naam: Buurtplek
    omschrijving: "Speelterrein van ≥3.000 m² voor de hele buurt, ingericht voor alle leeftijden met ontmoetingsfunctie"
    ggm_entiteit: Speelterrein
    ggm_guid: EAID_941A17C1_A2B2_4CD1_8991_08B0EBCF0C2
    ggm_attribuut: type
  - naam: Blokplek
    omschrijving: "Speelterrein van ≥500 m² voor direct omwonenden, gericht op kinderen tot 12 jaar"
    ggm_entiteit: Speelterrein
    ggm_guid: EAID_941A17C1_A2B2_4CD1_8991_08B0EBCF0C2
    ggm_attribuut: type
  - naam: Speelhoekje
    omschrijving: "Klein speelterrein met beperkte inrichting, aanvulling op het netwerk van buurt- en blokplekken"
    ggm_entiteit: Speelterrein
    ggm_guid: EAID_941A17C1_A2B2_4CD1_8991_08B0EBCF0C2
    ggm_attribuut: type
  - naam: Stedelijke sportplek
    omschrijving: "Buurtoverstijgende voorziening voor specifieke doelgroep: skatepark, freerunbaan, calisthenics, danceground"
    ggm_entiteit: Speelterrein
    ggm_guid: EAID_941A17C1_A2B2_4CD1_8991_08B0EBCF0C2
    ggm_attribuut: type
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "FunctioneelGebied (GGM)"
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Speelterrein is een specialisatie van FunctioneelGebied in het GGM
  - type: associatie
    bedrijfsobject: "[[Speeltoestel]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een speelterrein bevat nul of meer speeltoestellen
  - type: associatie
    bedrijfsobject: "[[Groenobject]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een speelterrein bevat groenvoorzieningen (beplanting, bomen, gras)
  - type: associatie
    bedrijfsobject: "[[Verhardingsobject]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een speelterrein bevat verhardingen en valondergronden
bedrijfsprocessen: [Speelruimtescan, Herinrichting speelterrein, Onderhoud speelterrein, Inspectie speeltoestellen, Gebiedsontwikkeling]
bedrijfsfuncties: [Beheer openbare ruimte, Spelen en bewegen, Gebiedsontwikkeling]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Kernbegrip in speelruimtebeleid en beheer openbare ruimte |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in IMBOR en gemeentelijk beheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elk speelterrein is een afgebakend terrein met eigen locatie, inrichting en kenmerken |
| Kan in meervoud bestaan | ✅ | Honderden speelterreinen per gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanleg → speelruimtescan → herinrichting → eventueel opheffing |
| Heeft relaties met andere concepten | ✅ | [[Speeltoestel]], [[Groenobject]], [[Verhardingsobject]], FunctioneelGebied |

Score: 6/6.

## Beschrijving

Een speelterrein is een afgebakende openbare ruimte die is ingericht als speelplaats voor kinderen. Het omvat het geheel van begroeiing, verharding, opstallen en speelwerktuigen op die locatie. De gemeente beheert speelterreinen als functionele gebieden met een eigen leeftijdsdoelgroep, kwaliteitsbeoordeling en herinrichtingscyclus.

De Utrechtse speelvisie hanteert een netwerk van buurtplekken (≥3.000 m², actieradius 400 meter, alle leeftijden) en blokplekken (≥500 m², actieradius 200 meter, tot 12 jaar). De ambitie is dat elk kind binnen 200 meter van de woning een speelterrein bereikt. De kwantitatieve norm stelt dat minimaal 3% (ambitie 5%) van de oppervlakte van een speelbuurt bespeelbaar moet zijn.

Bij herinrichting worden speelterreinen vergroend en klimaatbestendig gemaakt. Beoordelingscriteria op terreinniveau zijn: ligging en context, speelwaarde en verblijfswaarde, huidige staat, klimaatbestendigheid en inclusiviteit.

In het GGM is Speelterrein een specialisatie van FunctioneelGebied. [[Speeltoestel]] verwijst via het attribuut `speelterrein` naar het terrein waarop het staat.

## Specialisaties

| Subtype | Omschrijving | GGM |
|---|---|---|
| Buurtplek | ≥3.000 m², actieradius 400m, alle leeftijden, ontmoetingsfunctie | Speelterrein.type |
| Blokplek | ≥500 m², actieradius 200m, kinderen tot 12 jaar, direct omwonenden | Speelterrein.type |
| Speelhoekje | Klein terrein met beperkte inrichting, aanvulling op het netwerk | Speelterrein.type |
| Stedelijke sportplek | Buurtoverstijgend: skatepark, freerunbaan, calisthenics, danceground | Speelterrein.type |

De subtypes worden in het GGM geïmplementeerd via het attribuut `type`. De speelvisie beschrijft buurtplek en blokplek als de twee kerntypen van het netwerk; speelhoekjes en stedelijke sportplekken zijn aanvullend.

## GGM-bron

> "Geheel van begroeiing verharding opstallen en speelwerktuigen bedoeld als speelplaats voor kinderen."

- **Entiteit**: Speelterrein
- **Synoniemen**: Speelplek, Speelgelegenheid
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Attributen** (4): jaarHerinrichting, speelterreinLeeftijdDoelgroep, type, typePlus

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | FunctioneelGebied (GGM) | Speelterrein → FunctioneelGebied | GGM |
| associatie | [[Speeltoestel]] | Speeltoestel → Speelterrein | GGM (attribuut speelterrein) |
| associatie | [[Groenobject]] | Groenobject → Speelterrein | Beleid (vergroening speelplekken) |
| associatie | [[Verhardingsobject]] | Verhardingsobject → Speelterrein | Beleid (valondergronden, verharding) |

## Bedrijfsprocessen

- **Speelruimtescan**: wijkbrede inventarisatie van kwantiteit en kwaliteit speelterreinen, elke vijf jaar
- **Herinrichting speelterrein**: vernieuwing van inrichting, vergroening, klimaatadaptatie
- **Onderhoud speelterrein**: dagelijks en groot onderhoud van het terrein en de voorzieningen
- **Inspectie speeltoestellen**: viermaal per jaar controle van toestellen op het terrein (WAS)
- **Gebiedsontwikkeling**: inpassen van speelterreinen bij nieuwbouw en herontwikkeling (3-5% norm)

## Aandachtspunt: overlap met Maatschappelijke Voorziening

Het BO [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening|Maatschappelijke Voorziening]] bevat subtypes "Beheerde speeltuin" en "Speelplek". Nu Speelterrein een eigen BO is in het BOR-domein, is de verhouding:
- **Speelterrein** (BOR) = het fysieke terrein als beheerobject
- **Beheerde speeltuin** (Sociaal Domein) = de maatschappelijke functie met toezicht en activiteiten

Het subtype "Speelplek" bij Maatschappelijke Voorziening overlapt met Speelterrein en zou daar verwijderd kunnen worden, met een verwijzing naar dit BO. Dit is een aandachtspunt voor afstemming.


## Subtypes

- **Buurtplek** — Speelterrein van ≥3.000 m² voor de hele buurt, ingericht voor alle leeftijden met ontmoetingsfunctie
- **Blokplek** — Speelterrein van ≥500 m² voor direct omwonenden, gericht op kinderen tot 12 jaar
- **Speelhoekje** — Klein speelterrein met beperkte inrichting, aanvulling op het netwerk van buurt- en blokplekken
- **Stedelijke sportplek** — Buurtoverstijgende voorziening voor specifieke doelgroep: skatepark, freerunbaan, calisthenics, danceground

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
