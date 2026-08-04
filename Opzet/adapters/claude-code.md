# Adapter: Claude Code

Claude Code leest automatisch een `CLAUDE.md` in de projectroot en slash-commands uit `.claude/commands/`.

## Instructies laden

Maak een dunne `CLAUDE.md` die naar deze opzet verwijst:

```markdown
# GEMMA Bedrijfsobjecten Wiki

Volg de instructies in Opzet/AGENTS.md. Alle projectkennis staat in Opzet/context/,
processen in Opzet/workflows/, taakprompts in Opzet/prompts/.
```

Claude Code ondersteunt AGENTS.md-conventies ook steeds breder; een symlink `CLAUDE.md → Opzet/AGENTS.md` kan volstaan.

## Prompts als slash-commands

Elke prompt in [../prompts/](../prompts/) wordt een slash-command door het bestand naar `.claude/commands/{naam}.md` te kopiëren of te symlinken en de `{{parameter}}`-placeholder te vervangen door `$ARGUMENTS`. De kopregels (Doel/Parameters/…) mogen blijven staan; alleen het `## Prompt`-blok is functioneel.

## Tool-specifieke extra's

- **Modeladvies:** prompts met `licht` kun je in de frontmatter van het command markeren met `model: haiku`.
- **Parallellisatie:** de batches in [../prompts/audit-actoren.md](../prompts/audit-actoren.md) kunnen via subagents (Agent-tool) in golven van 3-4.
- **Permissions:** sta in de projectsettings minimaal lees/schrijf-toegang en `python3`-uitvoering toe.
