# Workflow: onderhoudscyclus

Na de initiële opbouw wordt het model onderhouden langs drie sporen.

## 1. Nieuwe GGM-release

```
nieuw XMI → parse → Wiki/GGM regenereren → BO-frontmatter verversen → dekking herberekenen
```

Uitvoeren via [../prompts/generate-ggm.md](../prompts/generate-ggm.md) (pipeline met dry-runs en gebruikersakkoord per stap) en daarna [../prompts/entiteitendekking.md](../prompts/entiteitendekking.md). Gewijzigde GUIDs of definities kunnen wijzen op homoniemen of verplaatste entiteiten — nooit blind toepassen.

## 2. Nieuwe onderwerpen en bronnen

Bronnen toevoegen ([../prompts/fetch.md](../prompts/fetch.md) / [../prompts/clip.md](../prompts/clip.md)) en verwerken via de [ingest-workflow](ingest.md). De ingest-backlog (`ToDo/ingest-backlog.md`) is de werkvoorraad.

## 3. Kwaliteit bewaken

- **Dekkingsanalyse** — [../prompts/entiteitendekking.md](../prompts/entiteitendekking.md): per taakveld/beleidsdomein welke GGM-entiteiten gedekt zijn, welke niet, en welke BO's geen GGM-grondslag hebben. Vervangt de oudere coverage-, bo-coverage- en ggm-vergelijking-analyses.
- **Lint** — [lint.md](lint.md): periodieke consistentiecheck.
- **Audits** — gerichte sweeps op definities, naamconflicten en ontbrekende actor-/rolpagina's ([../prompts/](../prompts/)).
- **Voortgang** — [../prompts/domain-status.md](../prompts/domain-status.md) per onderwerp.

## Terugmeldingen aan het GGM-team

Hiaten, duplicaten, homoniemen en definitieverschillen worden geregistreerd in `Wiki/Analyses/ggm-terugmeldingen.md` (typen: hiaat | definitie | structuur | scope | duplicaat | homoniem; status: open). De export naar CSV's voor de GGM-GEMMA-uitwisseling loopt via [../prompts/export-ggm.md](../prompts/export-ggm.md).
