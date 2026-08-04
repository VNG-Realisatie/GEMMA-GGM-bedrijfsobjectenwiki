# Opzet — vendor-neutrale AI-projectstructuur

Dit is de LLM-onafhankelijke opzet van de **GEMMA Bedrijfsobjecten Wiki**: alle projectkennis, werkafspraken, workflows en taakprompts, bruikbaar met elke LLM-tool (ChatGPT, Claude, Gemini, OpenAI API, OpenRouter, Ollama, LM Studio, Open WebUI, Aider, Cursor, VS Code-extensies en toekomstige tools).

Deze map vervangt op termijn de Claude-specifieke configuratie (`CLAUDE.md` en `.claude/commands/`). Hoe die overgang verloopt staat in [migratie/migratieplan.md](migratie/migratieplan.md).

## Het project in één alinea

De wiki is het werkinstrument van het GEMMA-team om het GEMMA-bedrijfsobjectenmodel onderbouwd op te bouwen. Het huidige model is een gefilterde kopie van het GGM (Gemeentelijk Gegevensmodel), maar zonder expliciete criteria. De wiki voert die filtering opnieuw uit: beleidsbronnen lezen → begrippen beoordelen aan vaste criteria → bedrijfsobjecten vastleggen met volledige onderbouwing → hiaten terugmelden aan het GGM-team. Elke bewering is herleidbaar: `Sources/ → Bronsamenvattingen/ → Bedrijfsobjecten/`.

## Structuur van deze map

| Map/bestand | Inhoud | Wanneer lezen |
|---|---|---|
| [AGENTS.md](AGENTS.md) | Kerninstructies voor elke LLM — het startpunt | Altijd (laden als systeeminstructie) |
| [context/](context/) | Projectkennis in 8 kleine bestanden | Bij elke werksessie de relevante bestanden |
| [workflows/](workflows/) | De 4 processen: ingest, vragen beantwoorden, lint, onderhoud | Bij het uitvoeren van dat proces |
| [prompts/](prompts/) | 15 uitvoerbare taakprompts (voorheen slash-commands) | Bij het starten van een taak |
| [templates/](templates/) | De 5 paginatemplates van de wiki | Bij het aanmaken van pagina's |
| [tools/](tools/README.md) | Catalogus van de Python-scripts | Bij GGM-verwerking en analyses |
| [adapters/](adapters/) | Per LLM-tool: hoe je deze opzet laadt | Eenmalig per tool |
| [presentatie.md](presentatie.md) | Kennissessie-presentatie (±30 slides) | Om de werkwijze uit te leggen |
| [migratie/](migratie/) | Analyse, mapping, migratieplan, aanbevelingen | Bij de overgang van de oude structuur |

## Leesvolgorde

**Nieuw teamlid (mens):** [presentatie.md](presentatie.md) → [context/project.md](context/project.md) → [context/architectuur.md](context/architectuur.md) → [workflows/ingest.md](workflows/ingest.md).

**LLM-sessie starten:** [AGENTS.md](AGENTS.md) laden (verwijst zelf naar de rest). Voor tools met beperkte context: minimaal AGENTS.md + [context/regels.md](context/regels.md) + de prompt van de taak.

**Taak uitvoeren:** open de prompt in [prompts/](prompts/); de kop van elke prompt vermeldt welke context-bestanden nodig zijn.

## Ontwerpprincipes van deze opzet

- **Drie lagen:** *kennis* (context/ — altijd beschikbaar), *proces* (workflows/ — het wat en waarom), *taak* (prompts/ — het uitvoerbare hoe). Zo hoeft een tool met een kleine context alleen te laden wat de taak vraagt.
- **AGENTS.md als entrypoint** — een open standaard die tools als Codex, Cursor en Aider automatisch lezen; voor alle andere tools is het gewoon het eerste bestand dat je meegeeft.
- **Geen vendor-aannames:** prompts gebruiken `{{parameter}}`-placeholders, modeladvies is beschreven als "licht/standaard" in plaats van productnamen, en parallellisatie is optioneel beschreven.
- **Scripts blijven bij het project** (`Bedrijfsarchitectuur/tools/`) — Python is al vendor-neutraal; [tools/README.md](tools/README.md) documenteert ze.
