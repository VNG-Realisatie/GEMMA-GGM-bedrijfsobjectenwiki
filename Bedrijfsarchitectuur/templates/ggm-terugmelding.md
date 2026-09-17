# Template: GGM-terugmelding

Locatie: `Wiki/Analyses/ggm-terugmeldingen.md` (één doorlopend bestand, niet per onderwerp)

Wordt aangevuld door `/write-element` stap 9 bij elke afwijking of elk hiaat tussen GGM en GEMMA-bedrijfsobjectenmodel. Nooit een nieuw bestand aanmaken — altijd een regel toevoegen aan het bestaande overzicht.

## Frontmatter

```yaml
---
type: analyse
titel: GGM Terugmeldingen
datum: {datum eerste aanmaak}
aanleiding: Centraal overzicht van bevindingen uit BO-toetsing die aan het GGM-team teruggekoppeld moeten worden
---
```

## Overzicht-tabel

| # | Domein | Entiteit | Type | Bevinding | Status |
|---|---|---|---|---|---|
| {volgnummer} | {beleidsdomein} | {GGM-entiteitnaam of — bij ontbrekend concept} | {type} | {korte beschrijving van de afwijking, met onderbouwing} | {status} |

## Typen

| Type | Betekenis |
|---|---|
| **hiaat** | Concept ontbreekt volledig in het GGM |
| **definitie** | Entiteit bestaat maar definitie is onjuist, onvolledig of geen begripsdefinitie |
| **structuur** | Modellering is onhandig (verkeerde overerving, ontbrekende relatie, verkeerde granulariteit) |
| **scope** | Entiteit hoort niet in dit beleidsdomein of ontbreekt in een ander |
| **duplicaat** | Dezelfde entiteit (zelfde concept) bestaat met meerdere GUIDs in verschillende beleidsdomeinen → advies: samenvoegen |
| **homoniem** | Dezelfde entiteitnaam wordt in verschillende beleidsdomeinen voor een ander concept gebruikt → advies: hernoemadvies |

## Status

| Status | Betekenis |
|---|---|
| **open** | Bevinding vastgesteld, nog niet teruggekoppeld |
| **gemeld** | Teruggekoppeld aan GGM-beheerteam |
| **opgelost** | Verwerkt in een nieuwe GGM-release |
| **afgewezen** | Teruggekoppeld maar niet overgenomen, met reden |
