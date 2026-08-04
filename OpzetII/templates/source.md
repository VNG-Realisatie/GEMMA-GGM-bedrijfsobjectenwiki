# Template: source-pagina

Locatie: `{wiki-root}/bronnen/{slug}.md` — slug lowercase-kebab-case, max 60 tekens. Eén source-pagina per bronbestand in `Sources/`.

Een source-pagina ontsluit de bron: metadata, samenvatting, relevante passages, onderwerpkoppeling. **Geen ArchiMate-analyse** — die hoort op kandidaatpagina's. De bron zelf blijft immutabel in `Sources/`.

## Frontmatter

```yaml
---
type: source
titel: 
bronbestand:                # pad naar de immutabele kopie in Sources/
oorsprong:                  # oorspronkelijke URL of vindplaats
brontype:                   # wet | beleidsnota | raadsstuk | rapport | website | ...
organisatie:                # opsteller/uitgever van de bron
datum_bron:                 # datering van de bron zelf (jjjj-mm-dd of jjjj)
datum_intake:               # jjjj-mm-dd
onderwerpen: []             # slugs van gekoppelde topic-pagina's
---
```

Frontmatter-stijl: lege waarde = blanco (niets na de dubbele punt), dubbele quotes alleen waar YAML dat vereist, lege lijst = `[]`.

## Body-secties

- **Samenvatting** — kort, in eigen woorden: wat is deze bron en waarom is hij relevant.
- **Relevante passages** — letterlijke citaten als blockquote, elk met plaatsaanduiding (hoofdstuk/paragraaf/pagina). Selectief: alleen passages die analyse kunnen dragen — geen tweede kopie van de bron.
- **Onderwerpen** — links naar de gekoppelde topic-pagina's, met per link één regel waarom de bron daar relevant is.

Ingevuld voorbeeld: [../voorbeelden/bronnen/vth-beleidsplan.md](../voorbeelden/bronnen/vth-beleidsplan.md).
