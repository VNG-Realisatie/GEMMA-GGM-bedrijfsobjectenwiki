---
type: bedrijfsobject
naam: Warmtenet
domein: [Energie en Klimaat]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
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
bo_definitie: "Infrastructuur van leidingen, warmtebronnen en afleverstations voor de levering van warmte aan gebouwen in een bepaald gebied."
bo_toelichting: ''
bedrijfsprocessen: [warmtetransitie, buurtaanpak aardgasvrij, verduurzaming stadsverwarming]
bedrijfsfuncties: [energiebeleid, gebiedsontwikkeling]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/energie-en-klimaat/opwekgebied|Opwekgebied]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Warmtenet kan warmte ontvangen uit opwekgebieden; opwekgebied kan warmtenet voeden
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen het domein | Centraal concept in het energiebeleid; beleidsnota Warmte gaat hierover |
| Herkenbaar voor domeinexperts | Ja — iedereen in het domein kent warmtenetten |
| Eigen bestaan | Ja — een warmtenet is een zelfstandig fysiek en juridisch ding |
| Meervoud | Ja — meerdere warmtenetten in de stad (stadsverwarming Eneco, toekomstige lokale netten) |
| Levenscyclus | Ja — aanleg, uitbreiding, verduurzaming (warmtepompen, warmtebuffers), afstoten |
| Relaties | Ja — met gebouwen, warmtebronnen, opwekgebieden, warmteprogramma |

6/6 criteria van toepassing.

## Beschrijving

Een warmtenet is een netwerk van leidingen waarmee warmte wordt getransporteerd van een of meer warmtebronnen naar gebouwen. De gemeente Utrecht heeft een samenwerkingsovereenkomst (SOK) met Eneco en gemeente Nieuwegein voor de verduurzaming van de Utrechtse stadsverwarming. In 2023 is een warmtepomp op de rioolwaterzuiveringsinstallatie van Overvecht afgerond, in 2024 warmtebuffers en electroboilers op Lage Weide.

De Collectieve Warmtewet (Wcw) regelt de tarieven en gemeentelijke governance van warmtenetten. De Wet gemeentelijke instrumenten warmtetransitie (Wgiw) geeft gemeenten de regie over de buurt-voor-buurt overstap op duurzame warmte.

> "We stappen buurt voor buurt over op duurzame manieren van koken en verwarmen. Daarvoor leggen we samen met onze partners warmtenetten aan en versterken we het elektriciteitsnetwerk."
> (bron: [[Wiki/Bronsamenvattingen/Energie en Klimaat/energiebeleid-utrecht|Energiebeleid gemeente Utrecht]])

> "De Collectieve Warmtewet (Wcw) regelt de tarieven en gemeentelijke governance van warmtenetten."
> (bron: [[Wiki/Bronsamenvattingen/Energie en Klimaat/verduurzaming-gebouwde-omgeving|VNG — Verduurzaming gebouwde omgeving]])

## Procesbron

Warmtenetten ontstaan in het warmtetransitieproces en worden juridisch verankerd via het warmteprogramma en de Wcw. De gemeente heeft geen eigendom maar wel governance: via de SOK met Eneco en via de wettelijke bevoegdheden uit de Wcw.

## Relaties

| Relatie | BO | Bron |
|---|---|---|
| voorziet van warmte | gebouwen (BAG) | beleidsbron: buurt-voor-buurt aansluiting |
| ontvangt warmte uit | warmtebronnen (geen BO, te granulair) | beleidsbron: warmtepomp RWZI, electroboilers |
| ruimtelijke samenhang | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/energie-en-klimaat/opwekgebied\|Opwekgebied]] | beleidsbron: bronnenstrategie |

## Bedrijfsprocessen

- Warmtetransitie — buurt-voor-buurt overstap op duurzame warmte
- Verduurzaming stadsverwarming — uitbreiding warmtebronnen (warmtepompen, warmtebuffers, electroboilers)

## Bedrijfsfuncties

- Energiebeleid
- Gebiedsontwikkeling


## Bronnen

- [[Wiki/Bronsamenvattingen/Energie en Klimaat/energiebeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Energie en Klimaat/verduurzaming-gebouwde-omgeving]]

## Terugmelding GGM

**Warmtenet** — Dataobject voor fysieke warmte-infrastructuur. Registreerbare eigenschappen: locatie (tracé), capaciteit, eigenaar/exploitant, aangesloten gebouwen, warmtebronnen, status (in aanleg, operationeel, uitbreiding). Relevant voor het warmteprogramma dat elke gemeente verplicht is. Zou onder een nieuw beleidsdomein Energie (taakveld 7) kunnen. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
