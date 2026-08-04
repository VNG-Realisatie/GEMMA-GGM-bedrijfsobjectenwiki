# Adapter: lokale modellen (Ollama, LM Studio)

Lokale modellen hebben doorgaans een kleinere context; laad selectief.

## Systeemprompt

- **Ollama** — maak een Modelfile met [../AGENTS.md](../AGENTS.md) als `SYSTEM`-blok:
  ```
  FROM llama3.1
  SYSTEM """
  {inhoud van Opzet/AGENTS.md}
  """
  ```
  en bouw het model met `ollama create gemma-wiki -f Modelfile`.
- **LM Studio** — plak AGENTS.md in het system-promptveld van de preset en sla de preset op.

## Contextbudget

Minimale set per sessie: `AGENTS.md` + [../context/regels.md](../context/regels.md) + het `## Prompt`-blok van de taak + alleen de bestanden waarop de taak werkt. De grote referentiebestanden ([../templates/element.md](../templates/element.md), GGM-data) alleen toevoegen wanneer de taak erom vraagt, en dan alleen het relevante deel.

## Geschikte taken

Read-only en klein-model-taken werken goed lokaal: [domain-status](../prompts/domain-status.md), [lint](../prompts/lint.md) (met beperkte scope), [audit-duplicaten](../prompts/audit-duplicaten.md), samenvatten van één bron. Zware beoordelingstaken (assess-element, write-element) vragen een capabel model — lokaal alleen met een groot model, anders via API of chat-tool.

## Bestanden wijzigen

Kale Ollama/LM Studio-chats schrijven geen bestanden. Combineer met een agent-frontend (bijv. Open WebUI met tools, Aider met een lokale provider, of een eigen script via de lokale API — zie [api.md](api.md)) om de wiki daadwerkelijk bij te werken.
