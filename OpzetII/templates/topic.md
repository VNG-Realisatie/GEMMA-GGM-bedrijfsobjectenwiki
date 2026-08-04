# Template: topic-pagina

Locatie: `{wiki-root}/onderwerpen/{slug}.md` — slug lowercase-kebab-case.

Een topic-pagina groepeert bronnen rond een domein of onderwerp en bakent de werkeenheid voor type-extractie af. **Geen definitieve elementdefinities** en geen kandidaat-analyse — een topic verwijst.

## Frontmatter

```yaml
---
type: topic
naam: 
relevante_typen: []         # type-slugs uit typen/ die in dit onderwerp verwacht worden
---
```

## Body-secties

- **Omschrijving** — wat dit onderwerp omvat en waar de grens ligt met aangrenzende onderwerpen.
- **Gekoppelde bronnen** — tabel: source-pagina (link) | relevantie voor dit onderwerp.
- **Relevante termen** — termen uit de bronnen die bij extractie aandacht verdienen, met eventuele synoniemen; géén beoordeling (dat doet stap 5).
- **Uitgevoerde extracties** — tabel: datum | elementtype | resultaat (aantal nieuwe/aangevulde kandidaten, bijzonderheden). Dit is de werkstatus van het onderwerp: welke typen zijn gedaan, welke staan nog open ten opzichte van `relevante_typen`.

Welke kandidaten bij dit onderwerp horen wordt níet hier bijgehouden — dat staat in de frontmatter van de kandidaatpagina's en verschijnt in het gegenereerde `voortgang.md`.

Ingevuld voorbeeld: [../voorbeelden/onderwerpen/vergunningverlening-toezicht-handhaving.md](../voorbeelden/onderwerpen/vergunningverlening-toezicht-handhaving.md).
