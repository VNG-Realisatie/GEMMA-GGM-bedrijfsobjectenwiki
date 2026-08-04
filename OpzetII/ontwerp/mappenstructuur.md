# Mappenstructuur

## Wiki

De locatie van de wiki-root is een nog te nemen besluit (bijvoorbeeld een nieuwe map naast de bestaande `Bedrijfsarchitectuur/Wiki/`); dit ontwerp schrijft `{wiki-root}` waar die locatie bedoeld wordt. De bestaande wiki blijft onaangeroerd onder de oude werkwijze.

```
{wiki-root}/
├── AGENTS.md          entrypoint voor LLM-sessies (of symlink naar OpzetII/AGENTS.md)
├── bronnen/           source-pagina's — één per bronbestand in Sources/
├── onderwerpen/       topic-pagina's — één per domein/onderwerp
├── kandidaten/        element-candidate-pagina's — plat, één per begrip
├── export/            gegenereerde exportbestanden, per run een datummap (afgeleid)
├── log.md             append-only logboek (zie onder)
└── voortgang.md       gegenereerd statusoverzicht (afgeleid — nooit handmatig bewerken)
```

Daarnaast, buiten de wiki:

- `Sources/` — de immutabele bronbestanden; bestaande werkafspraak, geldt onverkort.
- `OpzetII/` — dit ontwerp: documentatie, typekaders, templates en prompts. Documentatie en uitvoering blijven gescheiden: de wiki bevat inhoud, OpzetII beschrijft de werkwijze.

## Naamgeving

- Bestandsnamen lowercase-kebab-case, max 60 tekens; de slug van een kandidaatpagina is de begripsnaam (`omgevingsvergunning.md`).
- `kandidaten/` is bewust plat: de onderwerpkoppeling staat in de frontmatter, een mappenhiërarchie zou een tweede, te onderhouden indeling zijn.
- Eén begrip = één bestand, ook bij meerdere ArchiMate-typen (zie [paginamodel.md](paginamodel.md)).

## Logboek en voortgang

De blijvende werkafspraak is logboek-discipline; OpzetII kiest daarvoor deze vorm:

- **`log.md`** — append-only journaal, nieuwste datum bovenaan, onder een datumkop één regel per inhoudelijke mutatie: `- {pagina}: {wat er gebeurde} ({prompt})`. Zie [../voorbeelden/log.md](../voorbeelden/log.md).
- **Geen handmatige index.** Alles wat een index zou tonen (welke kandidaten, welke status, welke onderwerpen) staat al in frontmatter; een met de hand bijgehouden index zou dubbele vastlegging zijn. In plaats daarvan genereert de prompt [status.md](../prompts/status.md) het overzicht `voortgang.md` uit de frontmatter — weggooibaar en altijd reproduceerbaar.
- **Afgeleide bestanden** (`voortgang.md`, `export/`) worden niet gelogd; het logboek betreft inhoudelijke pagina's.
