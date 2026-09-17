---
type: element
naam: Netwerkcomponent
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Nertwerkcomponent
ggm_guid: EAID_DD277E82_0CA5_4460_918F_9178B5F01886
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items Diversen]
ggm_diagram_ids: [EAID_A255BB0C_A1DB_43a5_88B1_C638F6E64B0B]
ggm_definitie: "Een netwerkcomponent is een hardware- of softwareonderdeel dat een specifieke functie vervult binnen een netwerk om communicatie, gegevensuitwisseling of het beheer van netwerkverkeer mogelijk te maken."
ggm_toelichting:
ggm_synoniemen:
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

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Nertwerkcomponent**.
bo_definitie: "Hardware- of softwareonderdeel dat een specifieke functie vervult binnen een netwerk voor communicatie en gegevensuitwisseling."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server|Server]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Servers zijn verbonden via netwerkcomponenten"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/koppeling|Koppeling]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Koppelingen lopen over het netwerk"
bedrijfsprocessen: [Netwerkbeheer, Infrastructuurbeheer]
bedrijfsfuncties: [ICT-beheer]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Onderdeel van het netwerk dat communicatie en gegevensuitwisseling mogelijk maakt |
| Herkenbaarheid | "de firewall", "de switch", "de router", "de load balancer" |
| Eigen bestaan | Subtype van CMDB-item; functioneert onafhankelijk van specifieke applicaties |
| Meervoud | Tientallen per gemeente |
| Levenscyclus | Aanschaf → installatie → configuratie → onderhoud → vervanging |
| Relaties | Server, Koppeling |

Resultaat: 5/6 — BO. Geen eigen attributen in GGM maar voldoende criteria.

## BO-definitie

> "Een *netwerkcomponent* is een hardware- of softwareonderdeel dat een **specifieke functie vervult binnen een netwerk** om communicatie, gegevensuitwisseling of het beheer van netwerkverkeer mogelijk te maken."
> — GGM-definitie

De GGM-entiteitnaam bevat een typefout: "Nertwerkcomponent". Het BO heet **Netwerkcomponent**.

## Beschrijving

Een netwerkcomponent is een hardware- of softwareonderdeel dat een specifieke functie vervult binnen het gemeentelijk netwerk: switches, routers, firewalls, load balancers, access points. In het GGM is Netwerkcomponent een subtype van CMDB-item.

Netwerkcomponenten vormen de fysieke en logische verbindingslaag waarover [[Koppeling|koppelingen]] data uitwisselen en waarop [[Server|servers]] bereikbaar zijn.

## GGM-bron

> "Een netwerkcomponent is een hardware- of softwareonderdeel dat een specifieke functie vervult binnen een netwerk om communicatie, gegevensuitwisseling of het beheer van netwerkverkeer mogelijk te maken."
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Nertwerkcomponent (typo in GGM) | Matchsterkte: **exact** | Attributen: *(geen in GGM)*

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] | van-dit-BO | Servers zijn verbonden via netwerkcomponenten |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/koppeling\|Koppeling]] | van-dit-BO | Koppelingen lopen over het netwerk |

## Bedrijfsprocessen

- **Netwerkbeheer** — configuratie, monitoring, troubleshooting
- **Infrastructuurbeheer** — fysiek beheer van netwerkapparatuur

## Bedrijfsfuncties

- **ICT-beheer** — technisch netwerkbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer]]

## Terugmelding GGM

Typefout in GGM-entiteitnaam: "Nertwerkcomponent" → moet zijn "Netwerkcomponent". Teruggemeld in [[Wiki/Analyses/ggm-terugmeldingen]].
