# GEMMA Bedrijfsobjectenwiki

| Eigenaar                    | Ingevuld door |
| --------------------------- | ------------- |
| Kennis Centrum Architectuur | Mark Backer   |

Werkinstrument van het GEMMA-team voor het onderbouwd ontwikkelen en onderhouden van het GEMMA-bedrijfsobjectenmodel. Het huidige bedrijfsobjectenmodel is een gefilterde kopie van het GGM. Met behulp van deze wiki wordt die filtering opnieuw uitgevoerd op basis van expliciete criteria en herleidbare onderbouwing uit beleidsbronnen.

## Werkwijze

### Kernidee: LLM-wiki (Karpathy)

De aanpak volgt het [LLM-wiki-patroon van Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): kennis wordt niet telkens opnieuw verzameld, maar stapsgewijs opgebouwd in een wiki. Elke nieuwe bron wordt gelezen, samengevat en verwerkt in bestaande pagina's, inclusief verwijzingen, verbanden en eventuele tegenstrijdigheden. Zo ontstaat een kennisbasis die gaandeweg rijker en consistenter wordt. De mens selecteert de bronnen en formuleert de vragen; de LLM ondersteunt bij het samenvatten, verbinden en onderhouden van de kennis.

### Bottom-up proces: Bronnen → Bedrijfsobjecten

Per onderwerp wordt het volgende proces doorlopen:

1. **Bronnen ophalen** — beleidsdocumenten, proposities en verordeningen worden opgehaald, naar Markdown geconverteerd en opgeslagen in `Sources/` (immutabel)
2. **Bronsamenvattingen maken** — kernpunten uit de documenten worden geëxtraheerd en vastgelegd in `Wiki/Bronsamenvattingen/`
3. **Onderwerpoverzicht opbouwen** — begrippen uit de samenvattingen worden geïdentificeerd, getypeerd als ArchiMate-concepten en vastgelegd in een overzichtstabel
4. **BO-beoordeling** — elk begrip wordt getoetst aan expliciete criteria, zoals herkenbaarheid, eigen bestaan, levenscyclus en relaties; dit bepaalt de BO-kandidaten
5. **GGM-matching** — BO-kandidaten worden gematcht met bestaande GGM-entiteiten; de matchsterkte geeft inzicht in de mate van verankering
6. **Hiaten signaleren** — GGM-entiteiten zonder BO-grondslag en BO-kandidaten zonder GGM-entiteit worden gesignaleerd richting het GGM-team

Het resultaat per onderwerp bestaat uit **BO-pagina's met volledige onderbouwing** (bron → begrip → criteria → GGM-match). De vastgestelde eigenschappen worden vervolgens opgenomen in het GEMMA ArchiMate-model.

### GGM als **bron en validatie**

Het GGM vervult zowel de rol van invoerbron als validatiekader:

* **Invoer** — het GGM definieert beleidsdomeinen en bevat kandidaat-bedrijfsobjecten
* **Validatie** — voor elk in een bron geïdentificeerd BO wordt gecontroleerd of dit voorkomt in het GGM; ontbrekende entiteiten worden teruggekoppeld
* **Dekking** — met de skill `/coverage` wordt per GGM-beleidsdomein geanalyseerd welke entiteiten in een bron zijn aangetroffen en welke nog ontbreken

Hiermee ontstaat een gesloten feedbackloop tussen gemeentelijke bronnen, het GGM en het GEMMA-bedrijfsobjectenmodel.

## Structuur

**Immutabele invoer** (`Sources/`):

* Beleidsdocumenten per gemeentelijk onderwerp, geconverteerd naar Markdown
* GGM-repository: het GGM XMI-bronbestand, geconverteerd naar `json`

**Afgeleide kennisbasis** (`Wiki/`):

* `Bronsamenvattingen/` — kernpunten uit bronnen per onderwerp
* `Onderwerpen/` — onderwerpoverzichten met begrippentabellen (beleid → ArchiMate-type → BO-criteria)
* `Bedrijfsobjecten/` — volledig uitgewerkte BO-pagina's (bron → GGM-match → metadata)
* `Analyses/` — queryresultaten, syntheses en GGM-dekkingsrapportages

**Automatisering** (`.claude/commands/`):

Voor een reproduceerbare werkwijze zijn de volgende skills beschikbaar:

* 9 skills: `/ingest` (orchestrator), `/assess-bo` (beoordeling), `/write-bo` (BO-pagina), `/coverage` (GGM-dekking), `/domain-status`, `/lint`, `/fetch`, `/clip`, `/export-ggm`

Schema's en conventies: zie `CLAUDE.md`.

## Licentie
EUPL 1.2 (European Union Public Licence).
