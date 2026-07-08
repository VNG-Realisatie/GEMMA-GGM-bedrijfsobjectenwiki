---
type: element
naam: Werklocatie
domein: [Economie]
archimate_type: "business-object"
grondslag: "procesobject"
ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
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
bo_definitie: "Aangewezen geografisch gebied in de gemeente waar bedrijvigheid, voorzieningen of andere werkfuncties zijn geconcentreerd, met een vastgesteld profiel voor gewenst gebruik en ontwikkeling."
bo_toelichting: ''
gemma_toelichting: "Werklocaties worden getypeerd als bedrijventerrein, kantoorlocatie, winkelgebied, innovatielocatie of wijkeconomie. De gemeente stelt per werklocatie een profiel vast met kaders voor milieucategorie, functiemenging en sturingsintensiteit."
bo_subtypes:
  - naam: Bedrijventerrein
    omschrijving: "Werklandschap bedoeld voor bedrijven die hinder veroorzaken (geluid, stof, gevaar, geur); milieucategorie-gestuurd."
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: "type"
  - naam: Kantoorlocatie
    omschrijving: "Gebied met kantoorbestemming waar meerdere kantoorgebouwen bij elkaar staan; gesegmenteerd in top-, midden- en ondersegment."
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: "type"
  - naam: Winkelgebied
    omschrijving: "Ruimtelijke concentratie van retailfuncties en publieksgerichte voorzieningen; onderdeel van de retailhoofdstructuur."
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: "type"
  - naam: Innovatielocatie
    omschrijving: "Locatie voor innovatieve en kennisgedreven bedrijven rondom maatschappelijke vraagstukken, vaak gemengd met onderwijs en onderzoek."
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: "type"
  - naam: Wijkeconomie
    omschrijving: "Alle werkplekken buiten de vier andere typen: solitaire bedrijfspanden, thuiswerken, voorzieningen in wijken."
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: "type"
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Vestiging]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een werklocatie bevat meerdere vestigingen"
bedrijfsprocessen: [werklocatiebeleid, profilering werklocaties, monitoring werklocaties, ruimtelijk-economisch programmeren]
bedrijfsfuncties: [economisch beleid, ruimtelijke ordening]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal begrip in ruimtelijk-economisch beleid; kernconcept van Beleidsnota Werklocaties 2035 |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip bij economische zaken, ruimtelijke ordening, vastgoedbeheer |
| Heeft een eigen bestaan | ✅ | Geografisch afgebakend gebied met vastgesteld profiel en eigen kenmerken |
| Kan in meervoud bestaan | ✅ | Utrecht telt 31 werklocaties plus 40 winkelgebieden en overige wijkeconomie |
| Heeft een eigen levenscyclus | ✅ | Aanwijzing → profilering → beheer → herontwikkeling/transformatie |
| Heeft relaties met andere concepten | ✅ | Bevat vestigingen, heeft een profiel, is onderdeel van ruimtelijke strategie |

6/6 criteria — BO.

## Beschrijving

Een werklocatie is een aangewezen geografisch gebied in de gemeente waar bedrijvigheid, voorzieningen of andere werkfuncties zijn geconcentreerd. De gemeente identificeert werklocaties, stelt per locatie een profiel vast en monitort de ontwikkeling op basis van indicatoren als leegstand, banengroei en diversiteit.

Utrecht onderscheidt vijf typen werklocaties:

- **Bedrijventerreinen** — werklandschappen voor bedrijven die hinder veroorzaken (geluid, stof, gevaar, geur), gestuurd op milieucategorie en ruimtegebruik
- **Kantoorlocaties** — gebieden met kantoorbestemming, gesegmenteerd in top-, midden- en ondersegment
- **Winkelgebieden** — ruimtelijke concentraties van retailfuncties, geordend in een retailhoofdstructuur
- **Innovatielocaties** — locaties voor kennisgedreven bedrijven en instellingen rondom maatschappelijke vraagstukken
- **Wijkeconomie** — alle werkplekken buiten de vier andere typen: solitaire bedrijfspanden, thuiswerken, voorzieningen

Per werklocatie hanteert de gemeente een profiel met kaderstellende uitspraken over gewenst gebruik, milieucategorie, functiemenging en de mate van sturing (meebewegen vs. sturen).

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Bedrijventerrein | Werklandschap voor hinderveroorzakende bedrijven; milieucategorie-gestuurd | — |
| Kantoorlocatie | Gebied met kantoorbestemming; top/midden/ondersegment | — |
| Winkelgebied | Concentratie retailfuncties; retailhoofdstructuur | — |
| Innovatielocatie | Kennisgedreven bedrijven; gemengd met onderwijs/onderzoek | — |
| Wijkeconomie | Overige werkplekken: solitaire panden, thuiswerk, voorzieningen | — |

## Procesbron

Dit BO heeft geen directe GGM-entiteit. Het GGM modelleert `Vestiging` (RSGB/NHR) als individueel gebouw of complex, maar niet het hogere abstractieniveau van werklocaties als geografisch afgebakende gebieden met een profiel.

De beleidsbron is de [[Wiki/Bronsamenvattingen/Economie/beleidsnota-werklocaties-2035|Beleidsnota Werklocaties 2035]], die 31 werklocaties en 40 winkelgebieden benoemt en profileert.

> "Werklocaties zijn alle plekken in de stad waar gewerkt wordt." (Beleidsnota Werklocaties 2035)

## Relaties

| Relatie | Richting | Bedrijfsobject | Toelichting |
|---|---|---|---|
| bevat | → | [[Vestiging]] | Een werklocatie bevat meerdere vestigingen (bedrijven, instellingen) |

## Bedrijfsprocessen

- **Werklocatiebeleid** — vaststellen en evalueren van beleidskaders per type werklocatie
- **Profilering** — per werklocatie een profiel opstellen met kaders voor gebruik en ontwikkeling
- **Monitoring** — indicatoren bijhouden: leegstand, banengroei, diversiteit, voorzieningen
- **Ruimtelijk-economisch programmeren** — kantoorprogrammering, bedrijventerreinenplanning



## Subtypes

- **Bedrijventerrein** — Werklandschap bedoeld voor bedrijven die hinder veroorzaken (geluid, stof, gevaar, geur); milieucategorie-gestuurd.
- **Kantoorlocatie** — Gebied met kantoorbestemming waar meerdere kantoorgebouwen bij elkaar staan; gesegmenteerd in top-, midden- en ondersegment.
- **Winkelgebied** — Ruimtelijke concentratie van retailfuncties en publieksgerichte voorzieningen; onderdeel van de retailhoofdstructuur.
- **Innovatielocatie** — Locatie voor innovatieve en kennisgedreven bedrijven rondom maatschappelijke vraagstukken, vaak gemengd met onderwijs en onderzoek.
- **Wijkeconomie** — Alle werkplekken buiten de vier andere typen: solitaire bedrijfspanden, thuiswerken, voorzieningen in wijken.

## Bronnen

- [[Wiki/Bronsamenvattingen/Economie/beleidsnota-werklocaties-2035]]

## Terugmelding GGM

**GGM-hiaat Werklocatie:** Het GGM kent geen entiteit voor werklocatie als geografisch afgebakend werkgebied. Vestiging (RSGB) modelleert individuele bedrijfslocaties, maar niet het hogere abstractieniveau van aangewezen gebieden met een profiel, type en beleidskaders. Dit is een structureel hiaat: gemeenten identificeren, profileren en monitoren werklocaties als zelfstandige eenheden in hun ruimtelijk-economisch beleid.
