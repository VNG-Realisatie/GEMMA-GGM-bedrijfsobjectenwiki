# AI-richtlijnen

Hoe een LLM in dit project werkt, ongeacht de gebruikte tool.

## Getrapt autonomiemodel

1. **Bronniveau: altijd eerst bespreken.** Vóór het schrijven de kernpunten van een bron met de gebruiker doornemen (wat is rijk, wat niet, welke begrippen springen eruit).
2. **Begripniveau: zelfstandig bij eenduidigheid.** Een begrip wordt zonder tussenstap afgehandeld wanneer alle drie gelden:
   - begripstype `object`, `actor`, `rol` of `doelgroep`, én abstractieniveau operationeel;
   - minstens 5 van de 6 BO-criteria van toepassing;
   - GGM-matchsterkte `exact` of `sterk`.
3. **Twijfelgevallen: per stuk voorleggen** (niet in batch). Altijd voorleggen: governance-instrumenten, minder dan 5 criteria, matchsterkte `partieel`/`zwak`, generalisatiekeuzes en elke GGM-terugmelding.

## Vaste werkgewoonten

- **Begin bij de index.** `Wiki/index.md` is het startpunt om te vinden wat er al is; werk incrementeel verder op bestaande pagina's.
- **Sluit af met index en log.** Elke taak die pagina's wijzigt eindigt met het bijwerken van `Wiki/index.md` en één samenvattende entry in `Wiki/log.md`.
- **Kennis bouwt zich op.** Goede antwoorden worden teruggeschreven naar de wiki (zie [../workflows/vragen-beantwoorden.md](../workflows/vragen-beantwoorden.md)).
- **Verifieer na scripts en delegatie.** Na een scriptrun of het uitbesteden van deelwerk: terugmeldingen, tellingen en de versiestatus (bijv. `git status`) controleren op onverwachte wijzigingen buiten de eigen scope.

## GGM-data gebruiken

- **Domeinbegrip** (entiteiten, definities, relaties): lees `Wiki/GGM/{taakveld}/`.
- **Technische metadata** (GUIDs, GEMMA-tags, diagram-IDs): lees `Sources/GGM-repository/ggm_parsed.json`.
- **XMI nooit direct lezen** — alleen via de parser, bij een nieuwe GGM-release.
- **`Wiki/GGM/` nooit handmatig bewerken** — altijd regenereren via de pipeline.

## Modeladvies

Sommige taken zijn read-only analyse zonder redeneerwerk; die draaien prima (en goedkoper) op een **licht model**. De kop van elke prompt in [../prompts/](../prompts/) vermeldt `licht` of `standaard`. Hoe je een model kiest verschilt per tool — zie [../adapters/](../adapters/).

## Parallellisatie

Grote sweeps (bijv. audits over tientallen onderwerpen) mogen in batches parallel worden uitgevoerd als de tool subagents of parallelle sessies ondersteunt; anders sequentieel. De prompt vermeldt het waar relevant. Meld na elke batch een tussenstand.
