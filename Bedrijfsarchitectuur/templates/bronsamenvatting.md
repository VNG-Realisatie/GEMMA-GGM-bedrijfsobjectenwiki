# Template: Bronsamenvatting

Locatie: `Wiki/Bronsamenvattingen/{onderwerp}/{slug}.md`

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
- **Kernbegrippen** met korte toelichting — **als het begrip een BO is of naar een wiki-pagina verwijst: gebruik `[[wiki-link]]`**
- **Relevantie voor bedrijfsarchitectuur**
- **Citaten** die begrippen of objecten definiëren — **citeer altijd met bronverwijzing**

### Linkconventie

Alle verwijzingen naar wiki-pagina's en bedrijfsobjecten **moeten wiki-links zijn**:
- BO's: `[[bedrijfsobject-naam]]` (bijv. `[[Verkiezing]]`, `[[Begroting]]`)
- Begrippen met pagina: `[[begrip-naam]]` (bijv. `[[belastingmix]]`)
- Andere wiki-pagina's: `[[Wiki/Onderwerpen/financien]]`, `[[Wiki/Analyses/ggm-hiaten]]`
- Citaten uit bronsamenvattingen in body: `[[andere-bronsamenvatting|display-tekst]]`

**Uitzondering:** Citaten en blokkwoten uit externe bronnen (VNG-pagina's, etc.) zijn *plain text* — geen links.

### Bronnen-sectie

Aan het eind van de body: `## Bronnen` met wiki-links naar de source-bestanden waarop deze samenvatting is gebaseerd:
```markdown
## Bronnen
- [[Sources/{onderwerp}/{bestand}]]
```

De bronsamenvatting is het **schakelstuk** in de herleidbaarheidsketen: het verwijst naar het bronbestand (via `## Bronnen`) en wordt verwezen door de BO-pagina (via `## Bronnen` in de body).
