---
type: element
naam: Server
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Server
ggm_guid: EAID_3AFD7E5F_8061_4776_A332_334AF4125E7D
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items]
ggm_diagram_ids: [EAID_4F14E8D8_5502_4880_9E83_D912BE451EB1]
ggm_definitie: "Computer die in een netwerk een ondersteunende taak vervult."
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
  Dit BO heeft de GGM-entiteit **Server** als directe tegenhanger.
bo_definitie: "Computer die in een netwerk een ondersteunende taak vervult."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database|Database]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Server host een of meer databases"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Server draait applicaties (on-premises)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/netwerkcomponent|Netwerkcomponent]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Server is verbonden via netwerkcomponenten"
bedrijfsprocessen: [Infrastructuurbeheer, Capaciteitsbeheer, Wijzigingsbeheer]
bedrijfsfuncties: [ICT-beheer]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Kerncomponent van de IT-infrastructuur; host voor applicaties en databases |
| Herkenbaarheid | "de mailserver", "de databaseserver", "de webserver" |
| Eigen bestaan | 8 attributen in GGM (serverID, organisatie, servertype, IPAdres, vlan, serienummer, locatie, actief) |
| Meervoud | Tientallen tot honderden per gemeente |
| Levenscyclus | Aanschaf → inrichting → operationeel → onderhoud/patching → uitfasering |
| Relaties | Database, Applicatie, Netwerkcomponent, Koppeling |

Resultaat: 6/6 — BO.

## Beschrijving

Een server is een computer die in een netwerk een ondersteunende taak vervult: het hosten van applicaties, databases, bestandsopslag of netwerkdiensten. In het GGM is Server een subtype van Linkbaar CMDB-item (samen met [[Applicatie]] en [[Database]]).

Gemeenten beheren servers on-premises (in eigen datacenters of bij een hostingpartij) en in de cloud. De trend naar SaaS en Dienstverlening op Afstand vermindert het aantal fysieke servers, maar de gemeente blijft verantwoordelijk voor het beheer van haar serveromgeving en de data die erop draait.

## GGM-bron

> "Computer die in een netwerk een ondersteunende taak vervult."
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Server | Matchsterkte: **exact** | Attributen: serverID, organisatie, servertype, IPAdres, vlan, serienummer, locatie, actief

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database\|Database]] | van-dit-BO | Server host databases |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | van-dit-BO | Server draait applicaties (on-premises) |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/netwerkcomponent\|Netwerkcomponent]] | naar-dit-BO | Server is verbonden via netwerkcomponenten |

## Bedrijfsprocessen

- **Infrastructuurbeheer** — installatie, patching, monitoring van servers
- **Capaciteitsbeheer** — performance en schaalbaarheid bewaken
- **Wijzigingsbeheer** — impactanalyse bij serverwijzigingen

## Bedrijfsfuncties

- **ICT-beheer** — technisch serverbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/informatiesystemen/cmdb-en-informatiebeheer]]
- [[Wiki/Bronsamenvattingen/informatiesystemen/gibit-2025]]
