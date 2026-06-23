# GEMMA Bedrijfsobjectenwiki

| Eigenaar | Ingevuld door |
|---------|----------------|
| Kennis Centrum Architectuur | Mark Backer |

Werkinstrument van het GEMMA-team voor het onderbouwd opbouwen en onderhouden van het GEMMA bedrijfsobjectenmodel. Het huidige bedrijfsobjectenmodel is een gefilterde kopie van het GGM — op basis van deze wiki wordt de filtering opnieuw gedaan met expliciete criteria en herleidbare onderbouwing vanuit beleidsbronnen.
## Werkwijze

### Kernidee: LLM-wiki (Karpathy)

De aanpak volgt [Karpathy's LLM-wiki patroon](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): kennis wordt niet bij elke vraag opnieuw opgezocht, maar stap voor stap opgebouwd in een wiki. Elke bron die je toevoegt wordt gelezen, samengevat en verwerkt in bestaande pagina's — met verwijzingen, tegenstrijdigheden en samenhang. Zo groeit een kennisbank die steeds completer wordt. De mens kiest de bronnen en stelt de vragen; de LLM doet het samenvatten, linken en bijhouden.

### Bottom-up proces: Bronnen → Bedrijfsobjecten

Per domein wordt het volgende proces doorlopen:

1. **Bronnen ophalen** — Beleidsdocumenten, proposities, verordeningen worden opgehaald, naar markdown geconverteerd en opgeslagen in `Sources/` (immutabel)
2. **Bronsamenvattingen maken** — uit gelezen documenten worden kernpunten geëxtraheerd en samengevat in `Wiki/Bronsamenvattingen/`
3. **Domeinoverzicht opbouwen** — uit samenvattingen worden begrippen geïdentificeerd, getypeerd (ArchiMate-concepten) en in een tabel vastgesteld
4. **BO-beoordeling** — elk begrip wordt getoetst aan expliciete criteria (herkenbaarheid, eigen bestaan, levenscyclus, relaties); dit bepaalt BO-kandidaten
5. **GGM-matching** — BO-kandidaten worden gematcht op bestaande GGM-entiteiten; matchsterkte bepaalt hoe grondvast de BO is
6. **Hiaten signaleren** — GGM-entiteiten zonder BO-grondslag, of BO-kandidaten zonder GGM-entiteit worden gesignaleerd richting GGM-team

Het resultaat per domein: **BO-pagina's met volledige onderbouwing** (bron → begrip → criteria → GGM-match) die als eigenschappen naar het GEMMA ArchiMate-model gaan.

### GGM als **dekking en validatie**

Het GGM is tegelijkertijd invoer en checklist:
- **Invoer** — het GGM definieert beleidsdomeinen en geeft kandidaat-entiteiten
- **Validatie** — elke wiki-afgeleide BO moet GGM-grondslag hebben; zonder GGM-entiteit is het een gat (terugmelding naar VNG)
- **Dekking** — via `/coverage` analyseren we per GGM-beleidsdomein: welke entiteiten hebben wiki-onderliggende BO's, welke ontbreken

Dit sluit de feedback-loop: van gemeentelijke bron naar GGM en terug.

## Structuur

**Immutabele invoer** (`Sources/`):
- Beleidsdocumenten per gemeentelijk onderwerp
- GGM-representatie: leesbare conversie van het XMI-bronbestand (definitie, taakvelden, relaties)

**Afgeleide kennisbasis** (`Wiki/`):
- `Bronsamenvattingen/` — kernpunten uit Sources per domein
- `Domeinen/` — domeinoverzichten met begrippentabellen (beleid → ArchiMate-type → BO-criteria)
- `Bedrijfsobjecten/` — volledig onderbouwde BO-pagina's (bron → GGM-match → metadata)
- `Analyses/` — query-resultaten, syntheses, GGM-dekkingsrapporten

**Automatisering** (`.claude/commands/`):
- 9 skills: `/ingest` (orchestrator), `/assess-bo` (beoordeling), `/write-bo` (BO-pagina), `/coverage` (GGM-dekking), `/domain-status`, `/lint`, `/fetch`, `/clip`, `/export-ggm`

Schema en conventies: zie `CLAUDE.md`.

## Licentie

EUPL 1.2 (European Union Public Licence).
