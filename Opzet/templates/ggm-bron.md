# Template: GGM-bronbestand

Locatie: `Sources/GGM/{taakveld-nr}-{taakveld-naam}/{beleidsdomein}.md` — gegenereerd door de GGM-pipeline (zie de prompt generate-ggm), niet handmatig aangemaakt.

Elk GGM-bronbestand bevat wat nodig is om (1) te matchen op begrippen, (2) te bepalen of een entiteit een bedrijfsobject is, en (3) het bedrijfsobject te definiëren.

## Granulariteit

- Per **beleidsdomein** zolang dat ≤ ~80 entiteiten bevat; grote taakvelden opsplitsen per beleidsdomein of logische groep.

## Frontmatter

```yaml
---
type: ggm-beleidsdomein | ggm-taakveld
naam: {naam}
taakveld: "{nr} {taakveldnaam}"
definitie: "{korte definitie}"
aantal_entiteiten: {n}   # ALLEEN stereotype=Objecttype tellen
# alleen op taakveld-niveau:
beleidsdomeinen: [{lijst}]
---
```

**Telregel `aantal_entiteiten`:** tel alleen entiteiten met `stereotype == 'Objecttype'` in `ggm_parsed.json`. Niet meetellen: **Enumeratie** (waardelijst) en **Class zonder stereotype** (diagramcontainer in Enterprise Architect). Bij een parent-beleidsdomein: som van de Objecttype-tellingen van de kinderen.

## Verplichte secties per entiteitsgroep

### 1. Entiteitstabel

| Kolom | Verplicht | Toelichting |
|---|---|---|
| Entiteit | Ja | Naam van de entiteit |
| Definitie | Ja | Letterlijke definitie uit het GGM |
| Attributen | Ja | Alle attributen |
| Abstract | Ja | `Ja` als abstract (geen BO; alleen de concrete specialisaties worden BO) |
| Herkomst | Ja | Basisregistratie of standaard (BRP, BRK, BRWOZ, BAG, BGT/IMGeo, NHR, iWmo, iJw, …) |

### 2. Overervingshiërarchie

Bij abstracte entiteiten expliciet noteren: `Overervingshiërarchie: Ouder → Kind1; Ouder → Kind2.`

### 3. Relatiediagrammen

De belangrijkste relaties als ASCII-diagram, met multipliciteiten waar bekend; focus op procescontext.

```
Entiteit_A [1] ──── Entiteit_B [1..*]
    │
    ├── Entiteit_C [0..*]
    └── Entiteit_D [1]
```

### 4. Observaties

Feitelijke constateringen: wat valt op aan structuur of omvang; welke entiteiten overspannen meerdere packages; waar zitten hiaten of modelleringskeuzes die de wiki-mapping raken.

### 5. Relevantie

Per domeinperspectief: welke entiteiten zijn relevant, wat ontbreekt, verwijzingen naar relevante analyses.

## Waarom elk element nodig is

| Element | Nodig voor | Reden |
|---|---|---|
| Definitie | Begrip-matching | Koppelt GGM-entiteit aan beleidsbegrip |
| Attributen | BO-definitie | Bepaalt scope en inhoud |
| Abstract-vlag | BO-bepaling | Abstract wordt geen BO; specialisaties wel |
| Overerving | BO-bepaling | Voorkomt dubbele BO's (ouder + kind) |
| Relatiediagram | BO-relaties | Toont samenwerking in processen en functies |
| Herkomst | Herleidbaarheid | Welke basisregistratie is de bron van waarheid |
| Relevantie | Hiaten | Wat is er en wat ontbreekt per domein |
