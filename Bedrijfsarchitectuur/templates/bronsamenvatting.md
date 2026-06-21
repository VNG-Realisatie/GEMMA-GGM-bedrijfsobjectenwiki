# Template: Bronsamenvatting

Locatie: `Wiki/Bronsamenvattingen/{domein}/{slug}.md`

## Frontmatter

```yaml
---
type: bronsamenvatting
bron: "[Sources/{domein}/{bestand}.md](Sources/{domein}/{bestand}.md)"
titel: {titel van het document}
domein: [{domein(en)}]
datum_ingest: {datum van verwerking}
---
```

**Opmerking:** Het `bron:` veld gebruikt een markdown-link `[tekst](pad)`, niet een wiki-link, omdat het naar een source-bestand verwijst (geen wiki-pagina).

## Body

- **Samenvatting** van de bron (max 500 woorden)
- **Kernbegrippen** met korte toelichting — **als het begrip een BO is of naar een wiki-pagina verwijst: gebruik `[[wiki-link]]`**
- **Relevantie voor bedrijfsarchitectuur**
- **Citaten** die begrippen of objecten definiëren — **citeer altijd met bronverwijzing**

### Linkconventie

Alle verwijzingen naar wiki-pagina's en bedrijfsobjecten **moeten wiki-links zijn**:
- BO's: `[[bedrijfsobject-naam]]` (bijv. `[[Verkiezing]]`, `[[Begroting]]`)
- Begrippen met pagina: `[[begrip-naam]]` (bijv. `[[belastingmix]]`)
- Andere wiki-pagina's: `[[Wiki/Domeinen/financien]]`, `[[Wiki/Analyses/ggm-hiaten]]`
- Citaten uit bronsamenvattingen in body: `[[andere-bronsamenvatting|display-tekst]]`

**Uitzondering:** Citaten en blokkwoten uit externe bronnen (VNG-pagina's, etc.) zijn *plain text* — geen links.

De bronsamenvatting is het **schakelstuk** in de herleidbaarheidsketen: het verwijst naar het bronbestand (Sources/) en wordt verwezen door de BO-pagina (via `bronnen` in frontmatter).
