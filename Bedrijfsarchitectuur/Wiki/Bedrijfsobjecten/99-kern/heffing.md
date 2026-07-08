---
type: bedrijfsobject
naam: "Heffing"
domein: [Belastingen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Heffing"
ggm_guid: EAID_B3371695_97AD_49d2_9AF1_15591B422007
ggm_uml_type: Class
ggm_beleidsdomein: "RGBZPlus"
ggm_taakveld: "99 Kern"
ggm_diagram: [Diagram Vergunningen en Meldingen, Verkamering en Woonoverlast, Entiteiten Dienstverlening]
ggm_diagram_ids: [EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267, EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF, EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78]
ggm_definitie: "Een door de overheid opgelegde verplichting tot betaling"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Heffing"
ggm_gemma_guid: "ff9366e3-dd65-48ce-9051-9d6b01b2c6db"
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Heffing** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Heffingskorting** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Individuele vaststelling van het belastingbedrag door de heffingsambtenaar, resulterend in een betalingsverplichting."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/heffinggrondslag|Heffinggrondslag]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een heffing is gebaseerd op een heffinggrondslag"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening|Heffingsverordening]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een heffing is gebaseerd op een heffingsverordening (via heffinggrondslag)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "OZB-heffingen zijn gebaseerd op een WOZ-object"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo|WOZ-waarde]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Het belastingbedrag wordt berekend op basis van de WOZ-waarde"
bedrijfsprocessen: [belastingheffing, aanslagoplegging, bezwaarbehandeling, invordering]
bedrijfsfuncties: [Belastingheffing, Invordering]
---

# Heffing

Individuele vaststelling van het belastingbedrag door de heffingsambtenaar, resulterend in een betalingsverplichting voor de belastingplichtige.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | De gemeente registreert elke aanslag met bedrag, belastingplichtige, grondslag, status |
| Meervoud | Tienduizenden aanslagen per gemeente per jaar (OZB, afvalstoffenheffing, etc.) |
| Levenscyclus | Opgelegd → betwist/bezwaar → onherroepelijk → betaald/kwijtgescholden |
| Eigendom | De heffingsambtenaar legt de aanslag op namens de gemeente |
| Gemeentelijk belang | Kern van de gemeentelijke inkomstenverwerving |
| Bronnen | VNG-bronnen, beleidsregels DFM, alle belastingtype-bronnen |

## GGM-bron

> **Heffing**: Een door de overheid opgelegde verplichting tot betaling
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Heffing
**Attributen:** bedrag, code, inrekening, gefactureerd, runnummer, datumIndiening, nummer
**Matchsterkte:** sterk — de GGM-entiteit "Heffing" is generiek; het begrip "belastingaanslag" uit de beleidsbronnen is specifieker maar valt er volledig onder.

## BO-definitie

De GGM-definitie is bewust generiek ("verplichting tot betaling"). In de gemeentelijke praktijk gaat het om de **belastingaanslag**: de formele beschikking waarmee de heffingsambtenaar het verschuldigde bedrag vaststelt op basis van de belastingverordening. De aanslag specificeert de belastingplichtige, het belastbare feit, de heffingsmaatstaf en het tarief.

Het begrip "heffing" omvat ook leges en retributies — de GGM-entiteit is breed genoeg voor alle gemeentelijke heffingsvormen.

## Subtypes

Herkende specialisaties van Heffing. Elke gemeente heft een selectie van deze belastingtypen; individuele aanslagen zijn instanties van Heffing. Geen apart BO.

**Algemene belastingen** (opbrengst naar algemene middelen):
- **OZB (onroerendezaakbelasting)** — belasting op eigendom/gebruik onroerende zaken, grootste eigen inkomstenbron; heffingsmaatstaf is WOZ-waarde
- **Roerende-zaakbelasting** — OZB-variant voor woonboten en drijvende bedrijfsruimten
- **Hondenbelasting** — belasting voor het houden van een hond
- **Reclamebelasting** — belasting op openbare aankondigingen, vaak besteed via ondernemersfonds
- **Precariobelasting** — belasting voor voorwerpen op/onder/boven openbare gemeentegrond (GGM-entiteit: Precario)
- **Parkeerbelasting** — belasting op parkeren; instanties als [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht|Parkeerrecht]], [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/naheffing|Naheffing]]

**Bestemmingsheffingen** (opbrengst voor specifieke taken):
- **Afvalstoffenheffing** — bestemmingsheffing voor inzameling huishoudelijk afval
- **Riool- en waterzorgheffing** — heffing voor gemeentelijke watertaken
- **BIZ-bijdrage** — bestemmingsbelasting op verzoek ondernemers voor bedrijveninvesteringszone

**Toeristische heffingen**:
- **Toeristenbelasting** — heffing op verblijf niet-ingezetenen
- **Forensenbelasting** — heffing op langdurig verblijf niet-ingezetenen (>90 dagen)
- **Watertoeristenbelasting** — variant gekoppeld aan ligplaatsen

**Retributies** (vergoeding voor individueel voordeel):
- **Leges** — retributie voor gemeentelijke dienstverlening (vergunningen, documenten)
- **Reinigingsrecht** — retributie voor niet-verplichte afvalinzameling (bedrijven)
- **Marktgeld** — retributie voor standplaats op dag-/weekmarkten
- **Havengeld** — retributie voor gebruik waterwegen, havens, bruggen, sluizen
- **Lijkbezorgingsrechten** — retributie voor gebruik begraafplaats of crematorium
- **Vermakelijkhedenretributie** — retributie voor vermakelijkheden die gemeentelijke voorzieningen gebruiken

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Heeft grondslag | [[Wiki/Bedrijfsobjecten/99-kern/heffinggrondslag\|Heffinggrondslag]] | Heffing → Heffinggrondslag | — |
| Gebaseerd op verordening | [[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening\|Heffingsverordening]] | Heffingsverordening → Heffinggrondslag ← Heffing | Via Heffinggrondslag |
| Betreft WOZ-object | [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Via Zaak | Bij OZB/rioolheffing |
| Gekoppeld aan zaak | *(Zaak)* | Zaak → Heffing [1] | Zaak niet als apart BO in dit domein |
| Heeft vorderingregel | *(Vorderingregel)* | Heffing → Vorderingregel [0..1] | Financieel tussenobject |

## Bedrijfsprocessen

- **Aanslagoplegging**: heffingsambtenaar stelt aanslag vast op basis van verordening en feiten
- **Bezwaarbehandeling**: belastingplichtige maakt bezwaar tegen aanslag of WOZ-waarde
- **Invordering**: invorderingsambtenaar int het verschuldigde bedrag
- **Ambtshalve vermindering**: correctie van onjuiste aanslag zonder bezwaar

## Bedrijfsfuncties

- Belastingheffing
- Invordering

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/beleidsregels-gemeentelijke-belastingen-dfm]]
- [[Wiki/Bronsamenvattingen/Belastingen/belastingverordening]]
- [[Wiki/Bronsamenvattingen/Belastingen/bevoegdhedenverdeling]]
- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding]]
- [[Wiki/Bronsamenvattingen/Belastingen/onroerendezaakbelastingen]]
- [[Wiki/Bronsamenvattingen/Belastingen/parkeerbelastingen]]
