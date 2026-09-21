# Overdracht: bouw OpzetII

Startnotitie voor een nieuwe sessie. Geschreven 2026-07-19, na het interview waarin tot OpzetII is besloten.

## Opdracht

Bouw in deze map (`OpzetII/`) een nieuw wiki-ontwerp op basis van **[Opzet/opzet prompt.md](../Opzet/opzet%20prompt.md)** — dat ontwerpprompt is leidend. Deze notitie geeft alleen context en randvoorwaarden; ze bevat bewust géén ontwerpkeuzes.

Kern van het prompt: een LLM-onafhankelijke wiki als analyse- en curatieomgeving die uit beleidsbronnen GEMMA ArchiMate-elementen afleidt. Het GEMMA ArchiMate-model is de formele bron van waarheid; de wiki bevat kandidaten met statuscyclus (kandidaat → review → goedgekeurd/afgewezen), type-gerichte analyse per ArchiMate-elementtype, één centrale ElementCandidate-pagina, en export zonder dubbele vastlegging.

## Genomen besluiten (niet opnieuw uitvragen)

1. **OpzetII staat naast Opzet.** `Opzet/` documenteert de huidige, werkende wiki-aanpak en blijft onaangeroerd. OpzetII is het nieuwe ontwerp; een keuze tussen beide valt later.
2. **Greenfield.** De bestaande wiki-content (±319 BO-pagina's, 218 bronsamenvattingen, 34 onderwerpoverzichten onder `Bedrijfsarchitectuur/Wiki/`) blijft onder de oude werkwijze. OpzetII benoemt hooguit wát er te migreren valt; migratie is een apart, later besluit.
3. **GGM is buiten scope.** OpzetII ontwerpt puur de flow uit het prompt (bronnen → onderwerpen → type-extractie → kandidaten → beoordeling → export). De verhouding tot het GGM (Gemeentelijk Gegevensmodel: matching, dekkingsanalyse, terugmeldingen — nu een groot deel van de oude werkwijze) wordt een expliciet benoemd open punt, niet uitgewerkt.
4. **Vers ontwerpen.** Neem het oude model níet als uitgangspunt. Raadpleeg `Opzet/` alleen voor vormconventies (zie hieronder), niet voor het inhoudelijke paginamodel of proces.

## Feiten over de bestaande omgeving

- Repo-root: `/home/mark/Documents/GitHub/llm-wikis`. Het inhoudelijke project staat in `Bedrijfsarchitectuur/` (een Obsidian-vault, ook bewerkt in VS Code).
- `Bedrijfsarchitectuur/Sources/` — bronbestanden; de inhoud ervan is immutabel (werkafspraak, zie hieronder).
- `Bedrijfsarchitectuur/Wiki/` — de bestaande wiki volgens het oude model. Niet aanpassen vanuit OpzetII.
- `Bedrijfsarchitectuur/tools/` — Python-scripts van de oude werkwijze; `tools/export_ggm_csv.py` genereert 5 CSV's naar `Bedrijfsarchitectuur/exports/` voor de GGM-GEMMA-uitwisseling. Relevant als referentie bij de exportstap uit het prompt (er bestaat dus al een CSV-exportpad richting GEMMA); catalogus: [Opzet/tools/README.md](../Opzet/tools/README.md).
- `Opzet/` — de vendor-neutrale documentatie van de huidige werkwijze (46 bestanden, juli 2026).

## Herbruikbare vormconventies (aanbevolen, geen verplichting)

Deze zijn vendor-neutraal en staan los van het inhoudelijke model:

- **AGENTS.md als LLM-entrypoint** (open standaard) met dunne per-tool adapters: zie [Opzet/adapters/](../Opzet/adapters/).
- **Promptformat** met kop (Doel / Aanbevolen model licht|standaard / `{{parameters}}` / Benodigde context / Verwachte uitvoer) + promptblok + voorbeeld: zie [Opzet/prompts/README.md](../Opzet/prompts/README.md).
- **Linkconventie:** links moeten klikbaar werken in VS Code én Obsidian → relatieve markdown-links (vault-absolute `[[wiki-links]]` breken in VS Code).
- **Taal Nederlands**, bestandsnamen lowercase-kebab-case, kleine modulaire bestanden, documentatie en uitvoering gescheiden.
- **Frontmatter-stijl:** lege waarde = blanco, dubbele quotes waar nodig, lege lijst = `[]`.

## Blijvende werkafspraken (gelden ook onder OpzetII)

- **Sources-inhoud is immutabel** — nooit herschrijven/vertalen; ordenen (verplaatsen/hernoemen) en frontmatter-intake mogen.
- **Herleidbaarheid** — elke claim en elk voorgesteld element traceerbaar naar bronnen; onzeker = markeren, niet gokken.
- **Getrapte autonomie** — bespreken op bronniveau vóór schrijven; eenduidige gevallen zelfstandig; twijfelgevallen per stuk voorleggen.
- **Logboek-discipline** — wijzigingen naspeurbaar vastleggen (de oude wiki gebruikt hiervoor index.md + log.md; kies in OpzetII een eigen vorm).

## Open punten (benoemen in het ontwerp, niet oplossen)

1. **GGM-rol** — waar past matching/dekking/terugmelding later in het nieuwe procesmodel?
2. **Migratie bestaande content** — wat gebeurt er ooit met de bestaande elementpagina's en bronsamenvattingen?
3. **Exportmodel ↔ bestaande CSV-pijplijn** — sluit de nieuwe export aan op (of vervangt die) `export_ggm_csv.py`?
4. **Levenscyclus na goedkeuring** — het prompt eist "geen dubbele vastlegging": wat gebeurt er met een ElementCandidate-pagina na export naar GEMMA (bevriezen, archiveren, reduceren tot verwijzing)?

## Startinstructie nieuwe sessie

1. Lees [Opzet/opzet prompt.md](../Opzet/opzet%20prompt.md) — de opdracht.
2. Lees deze notitie — context, besluiten en randvoorwaarden.
3. Bouw het ontwerp in `OpzetII/`; wijzig niets in `Opzet/` of `Bedrijfsarchitectuur/`.
4. Raadpleeg `Opzet/` uitsluitend bij vormvragen; het oude paginamodel en proces zijn géén uitgangspunt.
