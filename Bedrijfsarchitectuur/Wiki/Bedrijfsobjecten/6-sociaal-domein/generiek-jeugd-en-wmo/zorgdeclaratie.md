---
type: bedrijfsobject
naam: Zorgdeclaratie
domein: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Declaratie
ggm_guid: EAID_5E542F35_E413_49c4_8FB7_335B6BE9667A
ggm_uml_type: Class
ggm_beleidsdomein: "Generiek Jeugd en Wmo"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: ["Sociaal Domein Beschikking en Voorziening: Domain Objects"]
ggm_diagram_ids: [EAID_5AE29494_3572_4924_B2B8_3206E55D71BB]
ggm_definitie: "Een opgave van te vergoeden kosten."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: GGM

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Declaratie**.
bo_definitie: "Maandelijkse opgave van een zorgaanbieder aan de gemeente van geleverde Wmo- of jeugdhulpproducten met de te vergoeden kosten."
bo_toelichting: ''
bo_via_kandidaten:
  - ggm_entiteit: "Declaratieregel"
    ggm_guid: "EAID_F73F6BFE_9CFE_4497_80E3_CADAA344CF69"
    reden: "Een declaratieregel legt het volume per product/prestatie vast binnen een zorgdeclaratie."
bo_synoniemen:
  - naam: Declaratie
    context: "iWmo/iJw-berichtenverkeer, GGM"
bo_homoniemen:
  - bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/declaratie|Declaratie (HR)]]"
    ggm_entiteit: Declaratie
    ggm_guid: EAID_E611CEB2_F4FA_49e2_AA6B_B380BC1918AC
    ggm_beleidsdomein: HR
    toelichting: "HR-declaratie betreft onkostenvergoeding van een werknemer; zorgdeclaratie betreft vergoeding van geleverde zorg door een aanbieder"
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing|Toewijzing]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "is op basis van toewijzing (via Declaratieregel)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering|Levering]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "productperiode past binnen levering"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "declaratieregel is voor beschikking"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "declaratieregel betreft cliënt"
bedrijfsprocessen: [declaratie ontvangen, declaratie beoordelen, declaratie betalen]
bedrijfsfuncties: [financieel beheer sociaal domein, contractbeheer]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Kern van de financiële afhandeling in het iWmo/iJw-berichtenverkeer |
| Besproken op bestuurlijk niveau | ✅ | Declaratievolumes en -bedragen in contractmonitoring, programmabegroting en jaarrekening |
| Vastgelegd in systemen | ✅ | Geregistreerd in suite voor sociaal domein, ontvangen via iWmo/iJw-berichtenverkeer |
| Eigen attributen | ✅ | declaratieBedrag, datumDeclaratie, declaratieStatus (GGM); declaratienummer, declaratieperiode, ingediend totaalbedrag, dagtekening (GIZO) |
| Relaties met andere objecten | ✅ | Toewijzing, Levering, Beschikking, Client (via Declaratieregel) |
| Levenscyclus | ✅ | Ingediend door aanbieder → ontvangen → beoordeeld (goedgekeurd/afgekeurd) → betaald |

## Beschrijving

Een zorgdeclaratie is de maandelijkse opgave waarmee een zorgaanbieder bij de gemeente de geleverde Wmo- of jeugdhulpproducten declareert. De declaratie bevat één of meer declaratieregels (prestaties), elk met een bedrag, productperiode en geleverd product. De gemeente beoordeelt de declaratie binnen 10 werkdagen en stuurt een declaratie-antwoordbericht met het totaal toegekend bedrag. Afgewezen prestaties kunnen gecorrigeerd worden heringediend.

Vanaf iWmo/iJw 3.1 is alleen de credit/debet-methode toegestaan voor correcties: de aanbieder crediteert de oorspronkelijke declaratieregel en dient een nieuwe in. Bij taakgerichte uitvoering vindt geen declaratie via het berichtenverkeer plaats.

## Naamkeuze

De GGM-entiteitnaam "Declaratie" is een homoniem — dezelfde naam wordt in beleidsdomein HR gebruikt voor onkostendeclaraties van werknemers. Dit BO heet **Zorgdeclaratie**.

**Overwogen namen:**
- **Zorgdeclaratie** — gekozen: duidelijk onderscheidend, gangbare term in het sociaal domein
- Declaratie (Wmo/Jw) — alternatief maar minder compact
- Declaratie Sociaal Domein — te breed, klinkt als GGM-technische naam

## GGM-bron

> "Een opgave van te vergoeden kosten." — GGM Generiek Jeugd en Wmo

- **Entiteit:** Declaratie
- **Beleidsdomein:** Generiek Jeugd en Wmo
- **Attributen:** declaratieBedrag, datumDeclaratie, declaratieStatus
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie ("Een opgave van te vergoeden kosten") is generiek en geldt ook voor de HR-variant. Dit BO specificeert het als de declaratie van een zorgaanbieder aan de gemeente voor geleverde Wmo/Jeugdwet-producten.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Zorgdeclaratie. Gemodelleerd als aparte entiteiten in het GGM (voor gedetailleerde berichtenverwerking) maar vormen geen zelfstandig bedrijfsobject.

- **Declaratieregel** — administratieve regel met het volume van één product/prestatie voor één cliënt binnen een declaratieperiode (code, bedrag, datumStart, datumEinde). Komt overeen met "Prestatie" in het GIZO.
- **Declaratiesoort** — typering van de declaratie

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] | ← | 1 | is op basis van toewijzing (via Declaratieregel) | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering\|Levering]] | ← | 1..* | productperiode past binnen levering | GIZO |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | ← | 1 | declaratieregel is voor beschikking | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 | declaratieregel betreft cliënt | GGM |

## Bedrijfsprocessen

- Declaratie ontvangen
- Declaratie beoordelen
- Declaratie betalen

## Bedrijfsfuncties

- Financieel beheer sociaal domein
- Contractbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/informatiemodel-gizo]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/procesbeschrijving-ijw-3.1]]
