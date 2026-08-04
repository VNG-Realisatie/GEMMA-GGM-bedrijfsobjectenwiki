---
type: element-candidate
naam: Omgevingsvergunning
status: goedgekeurd
onderwerpen: [vergunningverlening-toezicht-handhaving]
typen:
  - type: business-object
    besluit: gekozen
synoniemen: [vergunning, toestemming]
definitie: "Toestemming van het bevoegd gezag voor het uitvoeren van een of meer activiteiten die gevolgen kunnen hebben voor de fysieke leefomgeving."
toelichting: 
relaties:
  - type: associatie
    element: toezichthouder
    element_in: kandidaten
    beschrijving: "toezichthouder controleert de naleving van de vergunningvoorschriften"
export:
  datum: 2026-07-10
  bestand: export/2026-07-10/elementen.csv
---

# Omgevingsvergunning

## Context

De toestemming die het bevoegd gezag (meestal de gemeente) verleent voor activiteiten in de fysieke leefomgeving, zoals bouwen of milieubelastende activiteiten. Centraal registratieobject in het VTH-domein.

## Bronanalyse

**[vth-beleidsplan](../bronnen/vth-beleidsplan.md)**

- §2.1: registratie van kenmerk, activiteiten, voorschriften en looptijd in het VTH-systeem; de gemeente beslist als bevoegd gezag op aanvragen.
- §2.3: levenscyclus — aanvraag, beoordeling, verlening/weigering, wijziging, intrekking.
- Termen: omgevingsvergunning; in de bron ook kortweg "vergunning" en "toestemming".

## Typeanalyse

### business-object

| # | Criterium | Oordeel | Onderbouwing |
|---|---|---|---|
| 1 | Informatie | ja | kenmerk, activiteiten, voorschriften en looptijd worden geregistreerd (§2.1) |
| 2 | Identiteit | ja | iedere vergunning heeft een kenmerk (§2.1) |
| 3 | Levenscyclus | ja | aanvraag → verlening/weigering → wijziging/intrekking (§2.3) |
| 4 | Eigenschappen | ja | activiteiten, voorschriften, looptijd (§2.1) |

## Alternatieve typen

- **product** — de vergunning is óók het resultaat van gemeentelijke dienstverlening aan de aanvrager. Afgevallen: in deze bron staat de informatieregistratie centraal, niet het dienstenaanbod (afbakeningsregel in [business-object](../../typen/business-object.md)).

## Modelleerbesluit

Business object, gekozen. Alle vier de criteria zijn met bronpassages onderbouwd; het begrip is het centrale registratieobject van het VTH-domein. Teambesluit 2026-07-09: goedgekeurd.

## Voorgestelde definitie

"Toestemming van het bevoegd gezag voor het uitvoeren van een of meer activiteiten die gevolgen kunnen hebben voor de fysieke leefomgeving." — eigen synthese op basis van §2.1; de bron geeft zelf geen definitie.

## Voorgestelde relaties

| Relatietype | Element | Beschrijving | Bron |
|---|---|---|---|
| associatie | [toezichthouder](toezichthouder.md) | controleert de naleving van de vergunningvoorschriften | §4.1 |

*Exportnotitie:* deze relatie staat op de wachtlijst van de exportrun 2026-07-10 — het doel (toezichthouder) is nog niet goedgekeurd en gaat mee met een latere run.
