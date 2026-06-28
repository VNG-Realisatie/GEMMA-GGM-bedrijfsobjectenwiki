Voer een structurele BO-dekkingsbeoordeling uit: $ARGUMENTS

Doel: bepaal per GGM-entiteit of het een BO heeft, of met reden geen BO is, of nog beoordeeld moet worden. Identificeer beleidsdomeinen waar gericht zoeken naar bronnen de dekking kan verhogen.

**Uitvoering:**

### Stap 1: Python-script draaien

```
python3 tools/bo_coverage_assess.py
```

Het script classificeert alle 954 Objecttype-entiteiten:
- **Fase 1:** Al beoordeeld (BO, begrippentabel, wiki-subtypes/-componenten)
- **Fase 2:** Structureel niet-BO (GGM-subtypes, aggregatie-onderdelen, classificatie-entiteiten, abstract, cross-domein)
- **Fase 3:** Restant krijgt structurele indicatoren (attrs, relaties, definitie, bo-score-hint)

Output: `Wiki/Analyses/bo-dekking-data.json` + draft `Wiki/Analyses/bo-dekking.md`.

Toon de statistieken aan de gebruiker.

### Stap 2: LLM-beoordeling van resterende entiteiten

Lees `Wiki/Analyses/bo-dekking-data.json`. Voor elke entiteit met `status: "te-beoordelen"`:

1. Lees de GGM-definitie en structurele indicatoren uit het JSON.
2. Toets de 6 BO-criteria light (zonder bronnen, alleen op GGM-structuur):
   1. **Betekenisvol** — is dit herkenbaar binnen het beleidsdomein?
   2. **Herkenbaar** — weten domeinexperts wat dit is?
   3. **Zelfstandig bestaansrecht** — bestaat het onafhankelijk?
   4. **Meervoud** — meerdere exemplaren?
   5. **Eigen levenscyclus** — aangemaakt, gewijzigd, beëindigd?
   6. **Relaties** — relateert het aan andere concepten?
3. Classificeer als:
   - `bo-kandidaat` — structureel BO-waardig, bron nodig voor definitieve beoordeling
   - `niet-bo` — duidelijk geen BO op basis van structuur. Geef het **entiteitstype** aan uit de `/ggm-vergelijking` classificatie: classificatie, detail, component, proces, actor, rol, meetinstrument, of cross-cutting. Dit maakt de niet-bo motivatie uniform met de vergelijkingsanalyse.
   - `ter-discussie` — onduidelijk, inhoudelijke beoordeling via `/assess-bo` nodig
4. Motivatie: entiteitstype + 1-regel onderbouwing.

**Anti-patronen (uit /assess-bo):** gebruik NOOIT "registreerbaar", "eigendom", "systeembeheer" als criterium. Alleen de 6 criteria.

**Batch per beleidsdomein:** verwerk alle entiteiten van één beleidsdomein samen voor domeincontext.

### Stap 3: Rapport genereren

Update `Wiki/Analyses/bo-dekking.md`:
- Werk de samenvattingstabel bij met de LLM-beoordelingen
- Vul de **bronnen-opportuniteiten** tabel aan met een kolom "Suggestie bron" — welk type document zou helpen om de kandidaten in dit beleidsdomein te beoordelen
- In de hoofdtabel: vervang `te-beoordelen` statussen door de LLM-beoordeling

### Stap 4: Log bijwerken

Voeg entry toe aan `Wiki/log.md`.

### Relatie met andere skills

- `/coverage` — complementair: coverage telt, bo-coverage beoordeelt
- `/assess-bo` — onafhankelijk: assess-bo doet diepte-beoordeling met bronnen (begripstypen), bo-coverage doet structurele triage (entiteitstypen)
- `/ggm-vergelijking` — complementair: bo-coverage doet brede sweep over alle entiteiten, ggm-vergelijking doet diepte-analyse per onderwerp. Beide gebruiken dezelfde entiteitstype-classificatie.
- `/ingest` — bo-coverage output bepaalt waar bronnen gezocht moeten worden
