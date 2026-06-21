---
type: bedrijfsobject
naam: Voorschriftengebied
domein: [gevaarlijke-stoffen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Gebiedsaanwijzing"
ggm_guid: EAID_503BD06E_E063_46f2_8B43_BF75A143D6C4
ggm_uml_type: Class
ggm_beleidsdomein: "Omgevingswet"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Omgevingswet Verzoek Activiteit op Locatie, Omgevingswet Juridische Regels (CIMOW)]
ggm_diagram_ids: [EAID_30B09C29_F649_4248_97FC_35A5F9331BBF, EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0]
ggm_definitie: "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
ggm_toelichting: "Voorbeeld: bebouwde kom. In spreektaal: dit gebied is aangewezen als bebouwde kom en dit is de functie van dit gebied. Informatiekundig: een aangewezen gebied met de naam bebouwde kom heeft een locatieaanduiding naar een locatie/gebied. Deze locatieaandui"
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Gebiedsaanwijzing"
ggm_gemma_guid: "8ffff080-afa5-43cf-a1dc-1ab2052f20ac"
ggm_gemma_definitie: "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
ggm_gemma_toelichting: "Voorbeeld: bebouwde kom. In spreektaal: dit gebied is aangewezen als bebouwde kom en dit is de functie van dit gebied. Informatiekundig: een aangewezen gebied met de naam bebouwde kom heeft een locatieaanduiding naar een locatie/gebied. Deze locatieaandui"
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-8ffff080-afa5-43cf-a1dc-1ab2052f20ac"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "In het omgevingsplan aangewezen deel van een aandachtsgebied waarbinnen aanvullende bouweisen gelden voor nieuwbouw ter bescherming tegen brand en/of explosie."
bedrijfsprocessen: ""
bedrijfsfuncties: ""
relaties:
  - type: compositie
    bedrijfsobject: "[[Aandachtsgebied]]"
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Een voorschriftengebied is een (deel van een) aandachtsgebied
  - type: associatie
    bedrijfsobject: "[[Risicobron]]"
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Een voorschriftengebied hoort bij een risicobron
---

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Wettelijk instrument voor bouwkundige bescherming |
| Is herkenbaar voor domeinexperts | ✅ | Begrip uit het Bkl (art. 5.14) |
| Heeft een eigen bestaan | ✅ | Wordt expliciet aangewezen in het omgevingsplan met geometrische begrenzing |
| Kan in meervoud bestaan | ✅ | Meerdere voorschriftengebieden per gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanwijzen, wijzigen, opheffen via omgevingsplan |
| Heeft relaties met andere concepten | ✅ | Aandachtsgebied, risicobron, omgevingsplan, bouweisen |

## Beschrijving

Een voorschriftengebied is een in het omgevingsplan aangewezen locatie binnen een aandachtsgebied waarbinnen aanvullende bouweisen gelden voor nieuwbouw. Deze bouweisen beschermen mensen binnenshuis tegen de effecten van een brand of explosie bij een incident met gevaarlijke stoffen.

De aanvullende bouweisen staan in de artikelen 4.90 tot en met 4.96 van het Besluit bouwwerken leefomgeving (Bbl) en betreffen brandwerendheid van gebouwen, vluchtroutes en scherfwerking van glas. Bij de omgevingsvergunning bouw wordt getoetst of gebouwen aan deze eisen voldoen.

De gemeente kan afwijken van aanwijzing als de omgevingsveiligheidssituatie daartoe aanleiding geeft. Voor locaties waar zeer kwetsbare gebouwen zijn toegestaan is aanwijzing verplicht.

### Specialisaties

| Subtype | Omschrijving | GGM-attribuut |
|---|---|---|
| Brandvoorschriftengebied | Aanvullende bouweisen tegen brandgevaar | — |
| Explosievoorschriftengebied | Aanvullende bouweisen tegen explosiegevaar | — |

### Beleidskeuzes Utrecht per risicobrontype

| Risicobrontype | Brandvoorschriftengebied | Explosievoorschriftengebied |
|---|---|---|
| Bedrijven | Ja | Ja |
| Transportroutes (weg/spoor) | Ja | Ja |
| Transportroutes (water) | Nee | Nee |
| Buisleidingen | Nee | n.v.t. |

## GGM-bron

> "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
> — GGM, Gebiedsaanwijzing (EAID_503BD06E), beleidsdomein Omgevingswet

**Matchsterkte: partieel.** Gebiedsaanwijzing is het generieke GGM-concept. Een voorschriftengebied is een specifiek type gebiedsaanwijzing dat in het omgevingsplan wordt vastgelegd met bijbehorende bouweisen. Zelfde GGM-entiteit als [[Aandachtsgebied]] maar met een ander doel en een ander juridisch regime.

## BO-definitie

De GEMMA-definitie wijkt af van de GGM-definitie:
- **GGM**: "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
- **GEMMA**: "In het omgevingsplan aangewezen deel van een aandachtsgebied waarbinnen aanvullende bouweisen gelden voor nieuwbouw ter bescherming tegen brand en/of explosie."

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|---|
| [[Aandachtsgebied]] | compositie | ← | 1 | Een voorschriftengebied is een (deel van een) aandachtsgebied | Beleidsnota §2.4.4 |
| [[Risicobron]] | associatie | ← | 1 | Een voorschriftengebied hoort bij een risicobron | Beleidsnota §2.4.4 |

## Bedrijfsprocessen

- **Opstellen omgevingsplan** — voorschriftengebieden worden aangewezen met geometrische begrenzing in het omgevingsplan.
- **Toetsing omgevingsvergunning bouw** — bij de omgevingsvergunning wordt getoetst of nieuwbouw voldoet aan de aanvullende bouweisen van het voorschriftengebied.

## Terugmelding GGM

Voorschriftengebied deelt dezelfde GGM-entiteit (Gebiedsaanwijzing) als [[Aandachtsgebied]]. Het zijn conceptueel verwante maar verschillende objecten: het aandachtsgebied is een kenmerk van de activiteit, het voorschriftengebied is een actieve aanwijzing in het omgevingsplan. Overweeg of het GGM hiervoor specialisaties van Gebiedsaanwijzing zou moeten kennen. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
