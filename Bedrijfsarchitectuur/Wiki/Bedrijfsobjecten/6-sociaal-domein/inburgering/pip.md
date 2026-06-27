---
type: bedrijfsobject
naam: PIP
domein:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: PIP
ggm_guid: EAID_94EB7844_F863_4330_A15A_06ED4D1401E0
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
- Leerroute
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
- EAID_1B629406_49FC_4622_9F65_EF0B8F33CCF8
ggm_definitie: <font color="#0e0e0e">Het </font><font color="#0e0e0e"><b>Persoonlijk Plan Inburgering en Participatie (PIP)</b></font><font color="#0e0e0e"> is een individueel plan dat door de gemeente
  wordt vastgesteld in overleg met de inburgeringsplichtige, waarin het leerrouteadvies, het inburgeringsaanbod, het hoofddoel en de begeleidingsafspraken zijn vastgelegd, met als doel het succesvol afronden
  van de inburgering binnen de gestelde termijn.</font>
ggm_toelichting: "•\tHet PIP wordt opgesteld na de brede intake en op basis van onder meer de leerbaarheidstoets, diplomawaardering en persoonlijke omstandigheden (artikel 17 van de Wet inburgering 2021)."
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: PIP
ggm_gemma_guid: a1f148c2-d310-45c0-aee9-33e2c641ce37
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-a1f148c2-d310-45c0-aee9-33e2c641ce37
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
bo_definitie: Persoonlijk plan Inburgering en Participatie met de leerroute, verplichtingen en doelen van de inburgeraar.
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake|Brede Intake]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Wordt opgesteld naar aanleiding van de brede intake
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|Leerroute]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Bevat de afgesproken leerroute
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstraject|Inburgeringstraject]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Stuurt het inburgeringstraject aan
---

# PIP

Persoonlijk Plan Inburgering en Participatie — individueel plan vastgesteld door de gemeente met de inburgeraar, bevat leerrouteadvies, inburgeringsaanbod, hoofddoel en begeleidingsafspraken.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Het Persoonlijk Plan Inburgering en Participatie (PIP) is een individueel plan dat door de gemeente wordt vastgesteld in overleg met de inburgeringsplichtige, waarin het leerrouteadvies, het inburgeringsaanbod, het hoofddoel en de begeleidingsafspraken zijn vastgelegd, met als doel het succesvol afronden van de inburgering binnen de gestelde termijn.

- **Entiteit:** PIP
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** DagtekeningInitielePIP, DagtekeningPIP, NaamContactPersoon, EmailContactPersoon, IndicatorMagOpleidingAfmaken
- **Matchsterkte:** exact

## Relaties

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake|brede-intake]] — wordt opgesteld naar aanleiding van de brede intake [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|leerroute]] — bevat de afgesproken leerroute [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstraject|inburgeringstraject]] — stuurt het inburgeringstraject aan [1]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
