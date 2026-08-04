---
type: element-candidate
naam: Omgevingsdienst
status: review
onderwerpen: [vergunningverlening-toezicht-handhaving]
typen:
  - type: business-actor
    besluit: voorgesteld
  - type: business-object
    besluit: afgevallen
synoniemen: [uitvoeringsdienst, OD]
definitie: "Regionale uitvoeringsorganisatie, ingesteld als gemeenschappelijke regeling, die milieubasistaken en adviestaken in het VTH-domein uitvoert namens deelnemende gemeenten."
toelichting: 
relaties:
  - type: toewijzing
    element: toezichthouder
    element_in: kandidaten
    beschrijving: "inspecteurs van de omgevingsdienst vervullen de rol van toezichthouder"
export: 
---

# Omgevingsdienst

## Context

De regionale uitvoeringsorganisatie waaraan gemeenten wettelijke milieubasistaken hebben overgedragen. Werkt in opdracht van en namens de deelnemende gemeenten; in de bron treedt zij daarnaast op als adviseur bij complexe aanvragen.

## Bronanalyse

**[vth-beleidsplan](../bronnen/vth-beleidsplan.md)**

- §3.2: uitvoering van de milieubasistaken belegd bij de Omgevingsdienst Regio Voorbeeld, een gemeenschappelijke regeling; adviseert bij complexe aanvragen.
- §4.1: inspecteurs van de omgevingsdienst vervullen mede de rol van toezichthouder.
- Termen: omgevingsdienst; in de bron ook "uitvoeringsdienst" en de afkorting "OD".

*Open vraag:* de bron beschrijft alleen de relatie met deze gemeente; het generieke element betreft omgevingsdiensten als organisatievorm, niet deze ene dienst.

## Typeanalyse

### business-actor

| # | Criterium | Oordeel | Onderbouwing |
|---|---|---|---|
| 1 | Zelfstandigheid | ja | eigen organisatie op basis van een gemeenschappelijke regeling (§3.2) |
| 2 | Gedrag | ja | voert milieubasistaken uit, adviseert bij complexe aanvragen (§3.2) |
| 3 | Verantwoordelijkheid | ja | de milieubasistaken zijn bij de dienst belegd (§3.2) |

### business-object

| # | Criterium | Oordeel | Onderbouwing |
|---|---|---|---|
| 1 | Informatie | nee | de bron beschrijft geen registratie óver de omgevingsdienst, alleen haar handelen |

Verdere criteria niet getoetst: criterium 1 faalt al.

## Alternatieve typen

- **business-role** — afgevallen: de omgevingsdienst is een concrete, benoembare organisatie, geen hoedanigheid die door wisselende partijen wordt vervuld (afbakeningsregel in [business-actor](../../typen/business-actor.md)).

## Modelleerbesluit

Business actor, voorgesteld; business object afgevallen (er wordt in de bronnen geen informatie over de dienst als registratieobject vastgelegd). Wacht op teambesluit — *ter discussie:* modelleren we de organisatievorm "omgevingsdienst" of bestaat er in GEMMA al een verwant actor-element waarop dit moet aansluiten?

## Voorgestelde definitie

"Regionale uitvoeringsorganisatie, ingesteld als gemeenschappelijke regeling, die milieubasistaken en adviestaken in het VTH-domein uitvoert namens deelnemende gemeenten." — eigen synthese op basis van §3.2.

## Voorgestelde relaties

| Relatietype | Element | Beschrijving | Bron |
|---|---|---|---|
| toewijzing | [toezichthouder](toezichthouder.md) | inspecteurs van de omgevingsdienst vervullen de rol van toezichthouder | §4.1 |
