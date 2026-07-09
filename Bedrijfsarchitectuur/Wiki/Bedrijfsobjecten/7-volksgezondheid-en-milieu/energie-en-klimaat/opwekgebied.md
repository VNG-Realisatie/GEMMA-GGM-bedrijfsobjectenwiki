---
type: element
naam: Opwekgebied
onderwerp: [Energie en Klimaat]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein:
ggm_guid:
ggm_uml_type:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
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
bo_definitie: "Door de gemeente aangewezen gebied waar grootschalige opwek van duurzame energie (zon en/of wind) is toegestaan."
bo_toelichting:
bo_subtypes:
  - naam: "Zonneveld"
    omschrijving: "Terrein met zonnepanelen voor grootschalige opwek van zonne-energie"
  - naam: "Windlocatie"
    omschrijving: "Locatie aangewezen voor plaatsing van windturbines"
bedrijfsprocessen: [ruimtelijke planning energieopwek, RES-uitvoering, vergunningverlening]
bedrijfsfuncties: [energiebeleid, ruimtelijke ordening]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/energie-en-klimaat/warmtenet|Warmtenet]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Opwekgebied kan warmtenet voeden; warmtenet kan warmte ontvangen uit opwekgebied
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen het domein | Centraal concept: de gemeente wijst opwekgebieden aan via beleidsnota |
| Herkenbaar voor domeinexperts | Ja — beleidsnota Opwekgebieden 2024-2030 benoemt ze expliciet |
| Eigen bestaan | Ja — een opwekgebied is een afgebakend gebied met eigen aanwijzingsbesluit |
| Meervoud | Ja — meerdere opwekgebieden in de gemeente (voor zon en/of wind) |
| Levenscyclus | Ja — aanwijzing, planvorming, realisatie, uitbreiding, herijking |
| Relaties | Ja — met omgevingsplan, RES, warmtenet, vergunningen |

6/6 criteria van toepassing.

## Beschrijving

Een opwekgebied is een door de gemeente aangewezen locatie waar grootschalige opwek van duurzame energie mag plaatsvinden. De aanwijzing gebeurt via beleid (beleidsnota Opwekgebieden voor schone energie 2024-2030) en wordt verankerd in het omgevingsplan. Opwekgebieden kunnen bestemd zijn voor zonne-energie (zonnevelden), windenergie (windmolens) of een combinatie.

De keuze voor opwekgebieden gebeurt in samenspraak met de Regionale Energiestrategie (RES U16). De gezamenlijke ambitie is 1,8 TWh duurzame elektriciteit in 2030; ongeveer de helft is al gerealiseerd of vergund.

> "Hernieuwbare energie opwekken gebeurt door elektriciteit en warmte te produceren uit onuitputtelijke bronnen. Voor gemeenten betekent dit een actieve rol in de ontwikkeling van projecten zoals zonneparken en windmolenvelden."
> (bron: [[Wiki/Bronsamenvattingen/Energie en Klimaat/opwekken-duurzame-energie|VNG — Opwekken duurzame energie]])

> "De afspraken in de RES leggen we vast in het omgevingsbeleid van onze gemeente."
> (bron: [[Wiki/Bronsamenvattingen/Energie en Klimaat/energiebeleid-utrecht|Energiebeleid gemeente Utrecht]])

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Zonneveld | Terrein met zonnepanelen voor grootschalige opwek van zonne-energie | — |
| Windlocatie | Locatie aangewezen voor plaatsing van windturbines | — |

Beide subtypes vallen onder hetzelfde aanwijzingsbesluit en beleidskader (beleidsnota Opwekgebieden). Het onderscheid is het type opwek; de processen (aanwijzing, vergunning, monitoring) zijn identiek.

## Procesbron

Opwekgebieden ontstaan uit het ruimtelijke planningsproces voor de energietransitie. De gemeente wijst gebieden aan op basis van de RES-afspraken en eigen beleidskeuzes, vastgelegd in de beleidsnota Opwekgebieden. De juridische verankering loopt via het omgevingsplan (Omgevingswet).

## Relaties

| Relatie | BO | Bron |
|---|---|---|
| wordt verankerd in | omgevingsplan (Omgevingswet-domein) | beleidsbron: RES-afspraken vastgelegd in omgevingsbeleid |
| kan voeden | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/energie-en-klimaat/warmtenet\|Warmtenet]] | beleidsbron: bronnenstrategie |
| valt binnen | RES-regio (regionaal, geen BO) | beleidsbron: RES U16 |

## Bedrijfsprocessen

- Ruimtelijke planning energieopwek — aanwijzen geschikte locaties
- RES-uitvoering — realisatie regionaal afgesproken opwekdoelen
- Vergunningverlening — beoordeling initiatieven binnen opwekgebieden

## Bedrijfsfuncties

- Energiebeleid
- Ruimtelijke ordening



## Subtypes

- **Zonneveld** — Terrein met zonnepanelen voor grootschalige opwek van zonne-energie
- **Windlocatie** — Locatie aangewezen voor plaatsing van windturbines

## Bronnen

- [[Wiki/Bronsamenvattingen/Energie en Klimaat/opwekken-duurzame-energie]]
- [[Wiki/Bronsamenvattingen/Energie en Klimaat/energiebeleid-utrecht]]

## Terugmelding GGM

**Opwekgebied** — Dataobject voor aangewezen locaties voor grootschalige energieopwek. Registreerbare eigenschappen: locatie (geometrie), type opwek (zon/wind/combinatie), capaciteit (MW), status (aangewezen, in ontwikkeling, operationeel), relatie met omgevingsplan, RES-regio. Wettelijke grondslag via Omgevingswet/omgevingsplan. Zou onder een nieuw beleidsdomein Energie (taakveld 7) kunnen. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
