# Adapters: deze opzet laden in een LLM-tool

De opzet is tool-onafhankelijk: [AGENTS.md](AGENTS.md) is het entrypoint, [prompts/](prompts/) bevat de taakprompts met `{{parameter}}`-placeholders. Het laden is een dun laagje per tool; het patroon is gelijk aan de adapters van de oude opzet — zie [../Opzet/adapters/](../Opzet/adapters/) voor uitgewerkte varianten per tool.

Samengevat:

- **Tools die AGENTS.md automatisch lezen** (Codex, Cursor, Aider, …): niets nodig zodra AGENTS.md in de wiki-root staat (of daarheen gesymlinkt is).
- **Claude Code:** een dunne `CLAUDE.md` die naar AGENTS.md verwijst; prompts worden slash-commands door ze naar `.claude/commands/` te kopiëren en `{{parameter}}` te vervangen door `$ARGUMENTS`.
- **Chat-tools zonder bestandstoegang:** AGENTS.md plus de bestanden onder "Benodigde context" uit de promptkop meegeven of plakken; de ingevulde prompt als bericht.
- **API / lokale modellen:** AGENTS.md als systeeminstructie; ingevulde prompt en context als gebruikersbericht.

**Modeladvies:** prompts met aanbevolen model `licht` zijn read-only analyse zonder redeneerwerk — een klein/goedkoop model volstaat. `standaard` is het reguliere projectmodel.
