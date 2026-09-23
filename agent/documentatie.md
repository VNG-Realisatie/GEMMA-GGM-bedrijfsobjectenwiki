# Documentatie — generiek (alle wiki's)

Generieke achtergrond en skills, voor alle wiki's in deze repo. Wiki-specifieke documentatie staat in de eigen submap (bijv. [Bedrijfsarchitectuur/documentatie.md](../Bedrijfsarchitectuur/documentatie.md)). Generieke regels staan in [rules/werkwijze.md](rules/werkwijze.md).

## Kernidee: LLM-wiki (Karpathy)

De aanpak volgt het [LLM-wiki-patroon van Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): kennis wordt niet telkens opnieuw verzameld, maar stapsgewijs opgebouwd in een wiki. Elke nieuwe bron wordt gelezen, samengevat en verwerkt in bestaande pagina's, inclusief verwijzingen, verbanden en eventuele tegenstrijdigheden. Zo ontstaat een kennisbasis die gaandeweg rijker en consistenter wordt. De mens selecteert de bronnen en formuleert de vragen; de LLM ondersteunt bij het samenvatten, verbinden en onderhouden van de kennis.

## Skills

Generieke skills, projectlokaal in `.claude/commands/` op repo-root (niet in een wiki-submap).

| Skill | Functie | In | Uit |
|---|---|---|---|
| **crawl**<br>`/crawl {URL}` | Spidering/scraping van website voor bronverzameling<br>Tool: `agent/tools/crawl4ai/` | URL(s) | chat (optioneel `Sources/`-bestand op verzoek) |
| **setup-omgeving**<br>`/setup-omgeving` | Lokale omgeving inrichten zodat de commands werken (Linux of Windows), idempotent | geen | checklist (chat) |
