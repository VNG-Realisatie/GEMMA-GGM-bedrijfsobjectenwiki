Vergelijk GGM-entiteiten met bronbegrippen voor onderwerp: $ARGUMENTS

Doel: leg voor een wiki-onderwerp de GGM-entiteiten en de in de bronnen gevonden begrippen/BO's naast elkaar in een gestructureerde vergelijking.

## Werkwijze

De vergelijking is grotendeels geautomatiseerd via `tools/ggm_vergelijking_prep.py`. Het script doet het zware werk (matching, classificatie, dekking-traceren), de LLM reviewt en verrijkt.

### Stap 1: Script draaien

```bash
python3 tools/ggm_vergelijking_prep.py --onderwerp {onderwerp}
# of voor alle onderwerpen tegelijk:
python3 tools/ggm_vergelijking_prep.py --all
```

Het script:
- Leest `ggm_parsed.json`, alle BO-frontmatters, en de begrippentabel
- Matcht GGM-entiteiten op BO's (via GUID) en bronbegrippen (via naam)
- Classificeert ongematchte entiteiten als abstract/classificatie/detail/component/proces/rol/cross-cutting
- Traceert dekkingsketens (pad naar dichtstbijzijnde BO)
- Genereert draft analyse-pagina's in `Wiki/Analyses/ggm-vergelijking/`
- Schrijft review-overzicht naar `ggm-vergelijking-review.md`

### Stap 2: Review

Lees het review-overzicht (`Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-review.md`). Dit bevat:
- Samenvattingstabel per onderwerp (GGM, BO, matches, hiaten)
- Items met `confidence=low` die menselijke beoordeling nodig hebben

Per review-item: controleer of het gesuggereerde entiteitstype correct is. Pas aan in de draft als nodig.

### Stap 3: Beoordeling schrijven

De drafts hebben een `## Beoordeling` sectie met een `<!-- REVIEW -->` marker. Vervang deze met een inhoudelijke beoordeling:

- Samenvatting van de dekking (X van Y BO's hebben GGM-match)
- Structurele patronen (welke typen entiteiten worden geen BO en waarom)
- Analyse van de hiaten (hoe ernstig, lacune of modelleerkeuze)
- BO-hiaten: welke concepten ontbreken als BO; suggesties voor bronnen
- Naamverschillen en hun motivatie (homoniemen, synoniemen)
- Bewuste abstractiekeuzes

### Stap 4: Cross-check en afronden

1. **Verificatie**: tel aantallen in tabellen en vergelijk met frontmatter-counts.
2. **Consistentie**: check of elke BO uit het onderwerpoverzicht in precies één tabel voorkomt.
3. Update `Wiki/index.md` met de nieuwe analyse-pagina.
4. Voeg entry toe aan `Wiki/log.md`.
5. Update `Wiki/Analyses/ggm-vergelijkingen.md` — het centrale overzicht.

## Entiteitstype-referentie

Het script classificeert automatisch; gebruik deze tabel om classificaties te reviewen:

| Entiteitstype | Omschrijving | Script-heuristiek |
|---|---|---|
| **abstract** | Boventype waarvan subtypes erven | `is_abstract=True` in GGM |
| **classificatie** | Typering/soort; referentietabel | Naam begint met Soort/Aard/Reden of code+omschrijving+datum patroon |
| **detail** | Beschrijft een grotere entiteit | Naam bevat bekende patronen (Geboorte, Naam, Adres, etc.) of associatie met BO |
| **component** | Deel van een groter BO | Naam bevat Ontbinding/Sluiting/Regel/Deel |
| **proces** | Activiteit of processtap | Naam bevat Onderzoek/Aanmelding/Verwerking |
| **rol** | Functie/verantwoordelijkheid | Naam eindigt op -begeleider/-medewerker/-functionaris |
| **cross-cutting** | BO in ander domein | Entiteit heeft BO in ander beleidsdomein |
| **synoniem** | Verschillende namen, zelfde concept | BO-naam ≠ GGM-naam bij match |

## Relatie met andere skills

| Skill | Relatie |
|---|---|
| `/coverage` | Coverage telt per beleidsdomein; deze skill vergelijkt per wiki-onderwerp |
| `/bo-coverage` | Bo-coverage beoordeelt structureel per entiteit; deze skill toont de match met bronnen |
| `/assess-bo` | Assess-bo levert de BO-beoordelingen; deze skill visualiseert het resultaat |
| `/ingest` | Ingest genereert de input (begrippentabel, BO's); deze skill maakt de vergelijking achteraf |
