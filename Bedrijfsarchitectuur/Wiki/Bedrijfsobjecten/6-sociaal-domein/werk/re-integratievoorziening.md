---
type: bedrijfsobject
naam: Re-integratievoorziening
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Reintegratievoorziening
ggm_guid: EAID_6B1C7773_77F8_47a5_8C4E_E7E129148ADB
ggm_uml_type: Class
ggm_beleidsdomein: Werk
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Detaildiagram Werk]
ggm_diagram_ids: [EAID_F93A23D7_BF68_46e0_A6D4_96508ACED81E]
ggm_definitie: "Een voorziening of dienst die wordt ingezet om de kansen van een persoon op arbeidsparticipatie te vergroten."
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

gemma_definitie: "Een door de gemeente ingezette voorziening of dienst gericht op het vergroten van de kansen van een werkzoekende op arbeidsparticipatie, zoals scholing, werkervaring, bemiddeling of jobcoaching."
relaties:
  - type: associatie
    bedrijfsobject: "[[Loonkostensubsidie]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Re-integratievoorziening kan gepaard gaan met loonkostensubsidie"
  - type: associatie
    bedrijfsobject: "[[Client]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Client (werkzoekende) ontvangt re-integratievoorziening"
bedrijfsprocessen: [re-integratiebeoordeling, toekenning voorziening, uitvoering voorziening, evaluatie en beëindiging]
bedrijfsfuncties: [arbeidsparticipatie, re-integratie]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Identificeerbaar | ✅ Eigen registratienummer, type, start- en einddatum |
| Levenscyclus | ✅ Voorlopige toekenning → start → ingebruikname → verwacht einde → einde (of verlengde beslistermijn) |
| Eigendom/verantwoordelijkheid | ✅ Gemeente bepaalt welke voorzieningen worden ingezet; grote beleidsvrijheid |
| Bestuurlijk relevant | ✅ Re-integratie is een van de vier kostencategorieën in cluster Participatie (€4,0 mld totaal); gemeente bepaalt inzet en intensiteit |
| Relaties | ✅ Met Werkzoekende/Client, Loonkostensubsidie, DoelReintegratievoorziening |
| Persistent | ✅ Geregistreerd in gemeentelijke administratie, CBS re-integratiestatistiek |

## Beschrijving

Een re-integratievoorziening is een door de gemeente ingezette voorziening of dienst gericht op het vergroten van de arbeidskansen van een werkzoekende. Gemeenten hebben grote beleidsvrijheid bij de invulling: zij bepalen zelf welke voorzieningen worden aangeboden, aan wie, en met welke intensiteit.

Re-integratiekosten zijn specifiek gericht op het ontwikkelen en aan het werk helpen van mensen. Voorbeelden zijn scholing en opleiding, opdoen van werkervaring, stages, vrijwilligerswerk, coaching, jobhunting, werkgeverssubsidies (anders dan loonkostensubsidie), reiskosten en kinderopvang. Re-integratie onderscheidt zich van begeleiding: bij re-integratie gaat het om de kosten om mensen aan de slag te *krijgen*, bij begeleiding om de kosten om mensen aan de slag te *houden*.

De financiering loopt via het cluster Participatie in de algemene uitkering van het gemeentefonds. Het basisbedrag per bijstandsontvanger en per loonkostensubsidie-ontvanger (elk €7.355 inclusief uitkeringsfactor in 2024) dekt zowel uitvoerings- als re-integratiekosten. Een re-integratievoorziening kan gepaard gaan met een loonkostensubsidie wanneer de werkzoekende bij een werkgever aan de slag gaat met beperkte loonwaarde.

## GGM-bron

> "Een voorziening of dienst die wordt ingezet om de kansen van een persoon op arbeidsparticipatie te vergroten."
> — GGM, entiteit *Reintegratievoorziening*, beleidsdomein Werk

**Matchsterkte:** exact — de GGM-entiteit beschrijft precies het concept van een ingezette re-integratievoorziening.

**Attributen (GGM):** RegistratienummerReintegratievoorziening, DatumStartVoorlopigeToekenning, DatumStart, DatumVerwachtEinde, DatumEinde, DatumIngebruikname, DatumInname, DatumEindeVerlengdeBeslistermijn, CodeType, Omschrijving, OmschrijvingType, ToelichtingOmschrijving

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/loonkostensubsidie\|Loonkostensubsidie]] | kan gepaard gaan met | Re-integratievoorziening → Loonkostensubsidie | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ontvangt | Client → Re-integratievoorziening | GGM (via Werkzoekende) |

## Bedrijfsprocessen

- **Re-integratiebeoordeling**: vaststelling welke voorziening passend is voor de werkzoekende
- **Toekenning voorziening**: formele toekenning met registratienummer, type en verwachte duur
- **Uitvoering voorziening**: scholing, werkervaring, bemiddeling, coaching
- **Evaluatie en beëindiging**: beoordeling resultaat, eventuele verlenging of beëindiging

## Bedrijfsfuncties

- Arbeidsparticipatie
- Re-integratie

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/handreiking-explicitering-budgetten-participatiewet-wsw]]
