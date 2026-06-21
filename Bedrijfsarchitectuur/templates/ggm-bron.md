# Template: GGM-bronbestand

Locatie: `Sources/GGM/{taakveld-nr}-{taakveld-naam}/{beleidsdomein}.md`

Alle GGM-bronbestanden volgen dit uniforme formaat. Het bevat de informatie die nodig is om (1) te matchen op begrippen, (2) te bepalen of een entiteit een bedrijfsobject is, en (3) het bedrijfsobject te definiëren.

## Granulariteit

- Per **beleidsdomein** als het beleidsdomein ≤ ~80 entiteiten bevat.
- Grote taakvelden worden opgesplitst in meerdere bestanden per beleidsdomein of logische groep.

## Frontmatter

```yaml
---
type: ggm-beleidsdomein | ggm-taakveld
naam: {naam}
taakveld: "{nr} {taakveldnaam}"
definitie: "{korte definitie}"
aantal_entiteiten: {n}
# alleen bij taakveld-niveau:
beleidsdomeinen: [{lijst}]
---
```

## Verplichte secties per entiteitsgroep

### 1. Entiteitstabel

| Kolom | Verplicht | Toelichting |
|---|---|---|
| Entiteit | Ja | Naam van de entiteit |
| Definitie | Ja | Letterlijke definitie uit het GGM |
| Attributen | Ja | Alle attributen van de entiteit |
| Abstract | Ja | `Ja` als de entiteit abstract is (geen bedrijfsobject; alleen de concrete specialisaties worden BO's) |
| Herkomst | Ja | Basisregistratie of standaard waaruit de entiteit afkomstig is (BRP, BRK, BRWOZ, BAG, BGT/IMGeo, NHR, iWmo, iJw, StUF, KING, etc.) |

### 2. Overervingshiërarchie

Als er abstracte entiteiten zijn, expliciet de hiërarchie noteren:

```
Overervingshiërarchie: Ouder → Kind1; Ouder → Kind2.
```

### 3. Relatiediagrammen

De belangrijkste relaties tussen entiteiten als ASCII-diagram:

```
Entiteit_A [1] ──── Entiteit_B [1..*]
    │
    ├── Entiteit_C [0..*]
    └── Entiteit_D [1]
```

Multipliciteiten noteren waar bekend. Focus op relaties die relevant zijn voor het begrijpen van de procescontext.

### 4. Observaties

Feitelijke constateringen over het model:

- Wat valt op aan de structuur of omvang?
- Welke entiteiten overspannen meerdere packages of beleidsdomeinen?
- Waar zitten mogelijke hiaten of modelleringskeuzes die de wiki-mapping beïnvloeden?

### 5. Relevantie-sectie

Per relevant domeinperspectief:

- Welke entiteiten zijn relevant voor welk gemeentelijk domein?
- Wat ontbreekt er vanuit dat domeinperspectief?
- Verwijzingen naar relevante analyse-pagina's in de wiki.

## Waarom elk element nodig is

| Element | Nodig voor | Reden |
|---|---|---|
| Definitie | Begrip-matching | Koppelt GGM-entiteit aan beleidsbegrip |
| Attributen | BO-definitie | Bepaalt de scope en inhoud van het bedrijfsobject |
| Abstract-vlag | BO-bepaling | Abstracte entiteiten worden geen BO; hun specialisaties wel |
| Overerving | BO-bepaling | Voorkomt dubbele BO's (ouder + kind) |
| Relatiediagram | BO-relaties, procescontext | Laat zien welke BO's samenwerken in processen en functies |
| Herkomst | BO-definitie, herleidbaarheid | Vertelt welke basisregistratie de bron van waarheid is |
| Relevantie | BO-bepaling, hiaten | Signaleert wat er is en wat er ontbreekt per domein |
