# GEMMA Bedrijfsobjectenwiki

Werkinstrument van het GEMMA-team voor het onderbouwd ontwikkelen en onderhouden van het GEMMA-bedrijfsobjectenmodel. Het huidige bedrijfsobjectenmodel is een gefilterde kopie van het GGM. Met behulp van deze wiki wordt die filtering opnieuw uitgevoerd op basis van expliciete criteria en herleidbare onderbouwing uit beleidsbronnen.

Werkwijze, het bottom-up proces en de rol van het GGM: zie [documentatie.md](documentatie.md).

## Structuur

**Immutabele invoer** (`Sources/`):

* `Onderwerpen/` — beleidsdocumenten per gemeentelijk onderwerp, geconverteerd naar Markdown
* `Standaarden/` — catalogi en informatiemodellen (BAG, BRK, BRO, NHR, RGBZ, ZTC e.d.)
* `GEMMA/` — bronnen over het GEMMA-model
* `GGM-repository/` — het GGM XMI-bronbestand, geconverteerd naar `json`
* `Clippings/` (buiten `Sources/`) — ingang voor via Obsidian Web Clipper geclipte pagina's

**Afgeleide kennisbasis** (`Wiki/`):

* `Bronsamenvattingen/` — kernpunten uit bronnen per onderwerp
* `Onderwerpoverzichten/` — onderwerpoverzichten met begrippentabellen (beleid → ArchiMate-type → BO-criteria)
* `Bedrijfsobjecten/`, `Actoren/`, `Rollen/` — volledig uitgewerkte elementpagina's (bron → GGM-match → metadata)
* `GGM/` — gegenereerde GGM-pagina's per beleidsdomein
* `GEMMA/` — overzichten van het GEMMA-model (o.a. actoren en rollen)
* `Analyses/` — dekkingsrapportages en GGM-terugmeldingen
* `Vragen/` — vastgelegde antwoorden op ad-hoc vragen
* `index.md` en `log.md` — catalogus en chronologisch logboek

**Ondersteunend**:

* `templates/` — paginatemplates (element, bronsamenvatting, onderwerpoverzicht, GGM-terugmelding, vraag-antwoord, index, log)
* `tools/` — Python-scripts voor GGM-verwerking, dekkingsanalyse, lint en export
* `exports/` — gegenereerde GGM-GEMMA CSV's; formaat in [export_spec.md](export_spec.md)
* `ToDo/` — backlog en openstaande verbeterpunten

**Automatisering** (`.claude/commands/`):

Skills en tools, met welke wiki-pagina's ze lezen/schrijven: zie [documentatie.md](documentatie.md) §"Skills" en §"Tools".

Regels en conventies: zie [CLAUDE.md](CLAUDE.md) §"Regels". Generieke regels voor alle wiki's staan in `../agent/rules/`.

## Licentie
EUPL 1.2 (European Union Public Licence).
