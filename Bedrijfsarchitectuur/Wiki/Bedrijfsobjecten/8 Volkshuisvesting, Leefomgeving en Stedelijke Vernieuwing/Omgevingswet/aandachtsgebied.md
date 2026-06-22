---
type: bedrijfsobject
naam: Aandachtsgebied
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
gemma_definitie: "Ruimtelijk gebied rond een risicobron dat zichtbaar maakt waar mensen binnenshuis onvoldoende beschermd zijn tegen de gevolgen van een incident met gevaarlijke stoffen."
bedrijfsprocessen: ""
bedrijfsfuncties: ""
bronnen: [Wiki/Bronsamenvattingen/gevaarlijke-stoffen/beleidsnota-omgevingsveiligheid]
relaties:
  - type: associatie
    bedrijfsobject: "[[Risicobron]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Een aandachtsgebied hoort bij een risicobron
  - type: compositie
    bedrijfsobject: "[[Voorschriftengebied]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: Een voorschriftengebied is een (deel van een) aandachtsgebied
---

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal instrument voor afweging omgevingsveiligheid |
| Is herkenbaar voor domeinexperts | ✅ | Wettelijk begrip in het Bkl (art. 5.15) |
| Heeft een eigen bestaan | ✅ | Ruimtelijk afgebakend gebied met geometrische begrenzing |
| Kan in meervoud bestaan | ✅ | Drie typen per risicobron; meerdere risicobronnen per gemeente |
| Heeft een eigen levenscyclus | ✅ | Ontstaat met de activiteit, wijzigt bij verandering risicobron |
| Heeft relaties met andere concepten | ✅ | Risicobron, voorschriftengebied, kwetsbare gebouwen, omgevingsplan |

## Beschrijving

Een aandachtsgebied is een ruimtelijk gebied rond een risicobron dat zichtbaar maakt waar mensen binnenshuis, zonder aanvullende maatregelen, onvoldoende beschermd zijn tegen de gevolgen van een incident met gevaarlijke stoffen. Binnen een aandachtsgebied moeten maatregelen worden overwogen om mensen te beschermen.

Er zijn drie typen aandachtsgebieden, corresponderend met de drie typen gevaren:
- **Brandaandachtsgebied** — warmtestraling
- **Explosieaandachtsgebied** — overdruk
- **Gifwolkaandachtsgebied** — concentratie giftige stoffen

Aandachtsgebieden zijn een kenmerk van een activiteit met externe veiligheidsrisico's. Ze gelden vanaf het begin van de activiteit en hoeven niet eerst in het omgevingsplan te worden aangewezen.

### Specialisaties

| Subtype | Omschrijving | GGM-attribuut |
|---|---|---|
| Brandaandachtsgebied | Gebied waarbinnen mensen slachtoffer kunnen worden van warmtestraling | — |
| Explosieaandachtsgebied | Gebied waarbinnen mensen slachtoffer kunnen worden van overdruk | — |
| Gifwolkaandachtsgebied | Gebied waarbinnen mensen slachtoffer kunnen worden van giftige stoffen | — |

## GGM-bron

> "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
> — GGM, Gebiedsaanwijzing (EAID_503BD06E), beleidsdomein Omgevingswet

**Matchsterkte: partieel.** Gebiedsaanwijzing is het generieke GGM-concept voor alle gebiedsaanwijzingen in de Omgevingswet (bebouwde kom, stiltegebied, etc.). Een aandachtsgebied is een specifiek type gebiedsaanwijzing voor omgevingsveiligheid. De GGM-entiteit is breder; het BO is een specialisatie.

## BO-definitie

De GEMMA-definitie wijkt af van de GGM-definitie:
- **GGM**: "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
- **GEMMA**: "Ruimtelijk gebied rond een risicobron dat zichtbaar maakt waar mensen binnenshuis onvoldoende beschermd zijn tegen de gevolgen van een incident met gevaarlijke stoffen."

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|---|
| [[Risicobron]] | associatie | ← | 1 | Een aandachtsgebied hoort bij één risicobron | Beleidsnota §2.4 |
| [[Voorschriftengebied]] | compositie | → | 0..1 | Een voorschriftengebied is een (deel van een) aandachtsgebied | Beleidsnota §2.4.4 |

## Bedrijfsprocessen

- **Advisering ruimtelijke ontwikkelingen** — binnen aandachtsgebieden worden maatregelen afgewogen bij nieuwe bouwplannen.
- **Opstellen omgevingsplan** — aandachtsgebieden worden ruimtelijk weergegeven.
- **Afweging groepsrisico** — binnen aandachtsgebieden vindt de groepsrisico-afweging plaats (art. 5.15 Bkl).

## Terugmelding GGM

Het GGM kent geen specifiek objecttype voor aandachtsgebieden. Deze vallen onder de generieke Gebiedsaanwijzing. Overweeg of specialisatie zinvol is, gezien het belang van aandachtsgebieden in de Omgevingswet. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
