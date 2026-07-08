---
type: bedrijfsobject
naam: Asielstatushouder
domein:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Asielstatushouder
ggm_guid: EAID_598F7015_C6B5_4eed_80A6_139B62324678
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
- Relaties Sociaal Domein tot Kern
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
- EAID_D7287848_8118_4aab_8823_D555A599063C
ggm_definitie: De Inburgeringsplichtige die rechtmatig verblijf heeft
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: Asielstatushouder
ggm_gemma_guid: 3991c605-2abb-4185-b7ce-1adf5966e3c7
ggm_gemma_definitie: De Inburgeringsplichtige die rechtmatig verblijf heeft
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-3991c605-2abb-4185-b7ce-1adf5966e3c7
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Asielstatushouder** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Aandachtspunt** (detail) — Detailgegeven (weinig attributen)
  - **Diplomawaardering** (detail) — Detailgegeven (geassocieerd met BO)
  - **Educatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Hoofddoel** (detail) — Detailgegeven (weinig attributen)
  - **ICT-Vaardigheid** (detail) — Detailgegeven (geassocieerd met BO)
  - **Inburgeraar** (detail) — Detailgegeven (geassocieerd met BO)
  - **Ontwikkelwens** (detail) — Detailgegeven (weinig attributen)
  - **Subdoel Aandachtspunt** (detail) — Detailgegeven (weinig attributen)
  - **Subdoel Ontwikkelwens** (detail) — Detailgegeven (weinig attributen)
  - **Taalvaardigheid** (detail) — Detailgegeven
  - **Training** (detail) — Detailgegeven (geassocieerd met BO)
  - **Verblijfplaats AZC** (detail) — Detailgegeven
  - **Vreemdeling** (detail) — Detailgegeven (weinig attributen)
  - **Werk** (detail) — Detailgegeven
bo_definitie: Inburgeringsplichtige met verblijfsvergunning asiel die door de gemeente wordt gekoppeld aan een inburgeringstraject.
bo_toelichting: ''
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake|Brede Intake]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Doorloopt een brede intake na koppeling aan de gemeente
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|PIP]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Krijgt een persoonlijk plan inburgering en participatie
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/voorbereiding-op-inburgering|Voorbereiding op Inburgering]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Neemt deel aan voorbereiding op inburgering
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|Inburgeringsplicht]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Heeft een inburgeringsplicht
---

# Asielstatushouder

De inburgeringsplichtige die rechtmatig verblijf heeft als asielgerechtigde en door kansrijke koppeling aan een gemeente is toegewezen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> De Inburgeringsplichtige die rechtmatig verblijf heeft

- **Entiteit:** Asielstatushouder
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** Telefoonnummer verblijf AZC, Emailadres verblijf AZC, DigiD aangevraagd, Rijbewijs, Land Rijbewijs, Is gekoppeld aan
- **Overerving:** Inburgeraar (abstract) → Asielstatushouder
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie ("De Inburgeringsplichtige die rechtmatig verblijf heeft") is te vaag: ze noemt niet dat het om asielgerechtigden gaat en mist het koppelingsbegrip aan de gemeente. De bronnen (COA Dienstverleningsgids, Asielopvangwijzer) beschrijven asielstatushouders specifiek als statushouders die via kansrijke koppeling aan een gemeente worden toegewezen voor inburgering.

## Relaties

- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake|brede-intake]] — doorloopt een brede intake na koppeling aan de gemeente [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|pip]] — krijgt een PIP vastgesteld [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/voorbereiding-op-inburgering|voorbereiding-op-inburgering]] — neemt deel aan voorbereiding op inburgering [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|inburgeringsplicht]] — heeft een inburgeringsplicht [1]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
