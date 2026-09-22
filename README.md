
| Eigenaar                    | Ingevuld door |
| --------------------------- | ------------- |
| Kennis Centrum Architectuur | Mark Backer   |

# llm-wikis

Repository met LLM-gedreven wiki's voor het Kennis Centrum Architectuur. Elke wiki bouwt kennis stapsgewijs op uit bronnen, volgens het [LLM-wiki-patroon van Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): de mens selecteert bronnen en stelt vragen, de LLM vat samen, verbindt en onderhoudt.

## Inhoud

| Map | Inhoud |
|---|---|
| [Bedrijfsarchitectuur/](Bedrijfsarchitectuur/readme.md) | De huidige, werkende wiki: GEMMA Bedrijfsobjectenwiki (Obsidian-vault, ook bewerkt in VS Code). Bevat `Sources/`, `Wiki/`, `templates/`, `tools/` en `exports/` |
| [Opzet/](Opzet/README.md) | Vendor-neutrale documentatie van de huidige wiki-werkwijze (AGENTS.md, context, workflows, prompts, adapters). Nooit aanpassen vanuit OpzetII-werk |
| [OpzetII/](OpzetII/README.md) | Nieuw, greenfield ontwerp: ArchiMate-model als bron van waarheid, type-gerichte analyse, kandidaatpagina's met statuscyclus. Bouwen vanuit [overdracht.md](OpzetII/overdracht.md) |
| [agent/](agent/) | Generieke regels ([rules/werkwijze.md](agent/rules/werkwijze.md)) en tools ([tools/crawl4ai/](agent/tools/crawl4ai/)) voor alle wiki's |
| [documentatie/](documentatie/) | Achtergrondmateriaal: ArchiMate-modellering, criteria voor bedrijfs- en data-objecten, LLM-wiki-patroon |
| [.claude/commands/](.claude/commands/) | Slash-commands voor Claude Code (`crawl`, `setup-omgeving` en de wiki-commands via `BAlink`) |

## Aan de slag

1. Open de repo in VS Code of de map `Bedrijfsarchitectuur/` als vault in Obsidian.
2. Laat de agent [CLAUDE.md](CLAUDE.md) laden; die verwijst naar de generieke regels in `agent/rules/`. Wiki-specifieke afspraken staan in de eigen submap.
3. Richt de lokale omgeving in met het command `/setup-omgeving` (Linux of Windows).
4. Voor de werkwijze van de huidige wiki: begin bij [Bedrijfsarchitectuur/readme.md](Bedrijfsarchitectuur/readme.md); voor het nieuwe ontwerp bij [OpzetII/README.md](OpzetII/README.md).
