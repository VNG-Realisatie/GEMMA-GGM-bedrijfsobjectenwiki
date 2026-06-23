---
type: bedrijfsobject
naam: Dakloosheid
domein: [maatschappelijke ondersteuning]
archimate_type: "business-object"
grondslag: "ggm-entiteit"

ggm_entiteit: "Dakloosheid"
ggm_guid: EAID_A0F8E790_518A_4717_88C2_1143DE9F944A
ggm_uml_type: Class
ggm_beleidsdomein: "Dak- en thuislozen"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Diagram Dakloosheid]
ggm_diagram_ids: [EAID_7699CCFC_3358_48d0_A60C_F5D044D58F87]
ggm_definitie: "Informatie met betrekking tot dakloosheid"
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

gemma_definitie: "Registratie van de dakloosheidsstatus van een cliënt, inclusief toestemming voor briefadres en nachtopvang."
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "behoort bij een cliënt"
bedrijfsprocessen: [registratie dakloosheid, toewijzing maatschappelijke opvang, briefadres verstrekken]
bedrijfsfuncties: [maatschappelijke opvang, beschermd wonen]
---

# Dakloosheid

Registratie van de dakloosheidsstatus van een cliënt, inclusief toestemming voor briefadres en nachtopvang.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | De gemeente registreert per cliënt de dakloosheidsstatus met start-/einddatum, toestemmingen en gemeente van oorsprong |
| Meervoud | Honderden registraties per centrumgemeente |
| Levenscyclus | Geregistreerd → actief (opvang/begeleiding) → beëindigd (uitstroom naar woning) |
| Eigendom | De gemeente registreert en beheert de dakloosheidsstatus als onderdeel van de Wmo-taak |
| Gemeentelijk belang | Centraal in het Nationaal Actieplan Dakloosheid en gemeentelijke opvangbeleid |
| Bronnen | Aanpak dakloosheid |

## Beschrijving

Dakloosheid legt de status van een cliënt vast die dak- of thuisloos is. De gemeente registreert wanneer de dakloosheid begint en eindigt, of de cliënt toestemming geeft voor een gemeentelijk briefadres, of nachtopvang gewenst is en uit welke gemeente de persoon oorspronkelijk komt. Deze informatie is essentieel voor de toegang tot maatschappelijke opvang en beschermd wonen.

Het Nationaal Actieplan Dakloosheid verplicht gemeenten tot een integrale aanpak, waarbij registratie van de dakloosheidsstatus een voorwaarde is voor het bieden van ondersteuning. Centrumgemeenten hebben hierin een coördinerende rol.

## GGM-bron

> Informatie met betrekking tot dakloosheid

- **Entiteit:** Dakloosheid
- **Beleidsdomein:** Dak- en thuislozen (taakveld 6 — Sociaal Domein)
- **Attributen:** datumStart, datumEind, toestemmingGemeentelijkBriefadres, toestemmingNachtopvang, gemeenteOorsprong
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Richting | Kardinaliteit |
|---|---|---|---|
| Behoort bij cliënt | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/aanpak-dakloosheid]]
