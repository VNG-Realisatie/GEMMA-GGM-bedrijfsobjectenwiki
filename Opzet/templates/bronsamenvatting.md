# Template: Bronsamenvatting

Locatie: `Wiki/Bronsamenvattingen/{onderwerp}/{slug}.md`

De bronsamenvatting is het **schakelstuk** in de herleidbaarheidsketen: ze verwijst naar het bronbestand (via `## Bronnen`) en wordt zelf gerefereerd door elementpagina's (via hún `## Bronnen`-sectie).

## Frontmatter

```yaml
---
type: bronsamenvatting
titel: {titel van het document}
onderwerp: [{onderwerp(en)}]
datum_ingest: {datum van verwerking}
---
```

## Body

- **Samenvatting** van de bron (max 500 woorden)
- **Kernbegrippen** met korte toelichting — begrippen met een eigen wiki-pagina als wiki-link
- **Relevantie voor bedrijfsarchitectuur**
- **Citaten** die begrippen of objecten definiëren — altijd met bronverwijzing

### Linkconventie

- BO's en begrippen met pagina: `[[naam]]` (bijv. `[[Verkiezing]]`)
- Andere wiki-pagina's: met pad en alias, bijv. `[[Wiki/Onderwerpoverzichten/financien|financien]]`
- Andere bronsamenvattingen: `[[andere-bronsamenvatting|display-tekst]]`
- Citaten en blockquotes uit externe bronnen: platte tekst, geen links

### Bronnen-sectie

Aan het eind van de body:

```markdown
## Bronnen
- [[Sources/Onderwerpen/{onderwerp}/{bestand}]]
```

Links in `## Bronnen` krijgen géén alias — het pad maakt expliciet wat voor soort bestand de bron is (dezelfde regel als bij elementpagina's).
