# Adapter: API-integraties (OpenAI API, OpenRouter, Anthropic API)

Voor eigen scripts of pipelines die een LLM via een API aanroepen.

## System prompt samenstellen

Bouw de system prompt uit deze opzet, in volgorde:

1. [../AGENTS.md](../AGENTS.md) — altijd
2. [../context/regels.md](../context/regels.md) — altijd
3. De overige `context/`-bestanden die de taak raakt (zie de kop van de prompt)

## Taakprompt

Lees het promptbestand uit [../prompts/](../prompts/), substitueer de `{{parameters}}` (simpele stringvervanging) en stuur het `## Prompt`-blok als user message. Voeg de bestanden onder **Benodigde context** toe aan de user message of via retrieval/tool-gebruik.

```python
prompt = open("Opzet/prompts/domain-status.md").read()
taak = extract_prompt_block(prompt).replace("{{onderwerp}}", "mobiliteit")
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": taak + "\n\n" + context_bestanden},
]
```

## Modelkeuze

- Prompts met **Aanbevolen model: licht** → een klein/goedkoop model (bij OpenRouter of Ollama vrij te kiezen).
- Prompts met **standaard** → het reguliere projectmodel.

## Aandachtspunten

- Taken die bestanden wijzigen hebben tool-gebruik (function calling) met lees/schrijf-functies nodig, of een agent-framework; anders alleen read-only taken (domain-status, lint-rapportage) automatiseren.
- Respecteer de regels uit [../context/regels.md](../context/regels.md) ook in pipelines: nooit `Sources/`-inhoud wijzigen, altijd index/log bijwerken na schrijfacties.
