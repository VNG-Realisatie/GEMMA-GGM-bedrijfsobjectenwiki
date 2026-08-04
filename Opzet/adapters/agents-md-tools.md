# Adapter: AGENTS.md-tools (Codex, Cursor, Aider, OpenCode, …)

Tools die de open AGENTS.md-standaard ondersteunen vinden [../AGENTS.md](../AGENTS.md) automatisch zodra die in de projectroot staat (zie het migratieplan: een kopie of symlink in de root).

## Per tool

- **Codex / OpenCode** — lezen `AGENTS.md` in de repo-root automatisch; verder niets nodig.
- **Cursor** — leest `AGENTS.md`; als alternatief kun je de kernregels uit AGENTS.md opnemen in `.cursor/rules/` (project rules), met verwijzing naar `Opzet/context/` voor de rest.
- **Aider** — voeg de context toe met `--read`: `aider --read Opzet/AGENTS.md --read Opzet/context/regels.md`. Conventies kun je vastzetten in `.aider.conf.yml` (`read:`-lijst).
- **VS Code AI-extensies (bijv. Copilot)** — gebruik `.github/copilot-instructions.md` met dezelfde dunne verwijzing naar `Opzet/AGENTS.md`, of plak AGENTS.md in de instructie-instelling van de extensie.

## Taken uitvoeren

Open het promptbestand in [../prompts/](../prompts/), vul de `{{parameters}}` in en geef de prompttekst als opdracht. De kop van de prompt vermeldt welke bestanden de tool moet kunnen lezen.
