Leg vast als bedrijfsobject: $ARGUMENTS

Input: BO-naam (reeds beoordeeld via `/assess-bo`), of "domein X" voor alle BO's in een domein.

Verwacht een begrip dat al is beoordeeld als BO. Doet zelf géén BO-criteria of domeinbepaling.

## Stap 1: Grondslag bepalen

Bepaal de grondslag van het BO via deze cascade:

| Stap | Vraag | Grondslag |
|---|---|---|
| 1 | Is er een directe GGM-entiteit? | `ggm-entiteit` |
| 2 | Geen entiteit, wel afleidbaar uit bestaande GGM-objecten? | `ggm-afgeleid` |
| 3 | Geen GGM-basis, wel een artefact dat in een gemeentelijk proces ontstaat? | `procesobject` |
| 4 | Geen GGM-basis, juridisch/beleidsmatig kader? | `governance-object` |

Het ontbreken van een GGM-grondslag is voor procesobjecten en governance-objecten **structureel** — het GGM modelleert data, niet processen of governance.

## Stap 2: GGM-match zoeken

Zoek in `Sources/GGM/` naar kandidaat-entiteiten:
- Naam-match (exact of synoniem)
- Definitie-match (vergelijkbare scope)
- Domein-match (zelfde beleidsdomein/taakveld)

## Stap 3: Matchsterkte beoordelen

| Matchsterkte | Betekenis | Actie |
|---|---|---|
| **exact** | GGM-entiteit en BO zijn hetzelfde concept, definitie klopt | Overnemen, definitie uit GGM |
| **sterk** | Zelfde concept, maar definitie of scope wijkt licht af | Overnemen, afwijking documenteren en terugmelden |
| **partieel** | GGM-entiteit dekt een deel van het BO, of BO is aggregatie van meerdere entiteiten | Overnemen met toelichting, overweeg terugmelding |
| **zwak** | Verwant concept maar wezenlijk andere scope of granulariteit | Relatie noteren, niet als grondslag gebruiken |

## Stap 4: Mapping-regels

- Bij voorkeur **1-op-1 mapping** (beheerbaarheid, herkenbaarheid).
- **Aggregatie** toegestaan als het GGM te granulair is — noteer welke GGM-entiteiten zijn samengevoegd.
- Als een GGM-entiteit in **meerdere beleidsdomeinen** voorkomt: maak één bedrijfsobject met alle GGM-bronnen.

## Stap 5: GGM-velden ophalen

Lees het geparsede GGM uit `Sources/GGM-repository/ggm_parsed.json` (bij nieuwe GGM-release: `python3 tools/parse_ggm_xmi.py`).

Zoek op entiteitnaam en vul het volledige frontmatter-schema:

**GGM-velden uit XMI:**
- `ggm_entiteit`: naam van de GGM-entiteit
- `ggm_guid`: EA GUID uit het XMI (entities[id].id)
- `ggm_uml_type`: Class of Enumeration
- `ggm_beleidsdomein`: beleidsdomein uit package-hiërarchie
- `ggm_taakveld`: taakveld uit package-hiërarchie
- `ggm_diagram`: lijst van diagramnamen (entities[id].diagram_names)
- `ggm_diagram_ids`: lijst van diagram-GUIDs (entities[id].diagram_ids)
- `ggm_definitie`: letterlijke GGM-definitie (entities[id].documentation)
- `ggm_toelichting`: tag Toelichting
- `ggm_synoniemen`: tag Synoniemen
- `ggm_herkomst`: tag Herkomst

**GEMMA-waarden uit GGM XMI (referentie):**
- `ggm_gemma_naam`, `ggm_gemma_guid`, `ggm_gemma_definitie`, `ggm_gemma_toelichting`, `ggm_gemma_synoniemen`, `ggm_gemma_type`, `ggm_gemma_url`, `ggm_gemma_bron`, `ggm_gemma_alternate_name`
- Haal uit entities[id].gemma_tags

**GEMMA-velden (wiki-eigen):**
- `gemma_definitie`: bepaal op basis van vergelijking:
  - Als `ggm_gemma_definitie` niet leeg is en inhoudelijk klopt: neem die over
  - Als `ggm_definitie` klopt op bedrijfsniveau: "gelijk aan GGM"
  - Anders: formuleer een eigen GEMMA-definitie en documenteer de afwijking

## Stap 6: Subtypes vastleggen

Wanneer een BO herkende subtypes heeft die **geen apart BO** zijn (uitwisselbaar, zelfde register en processen):

**Frontmatter:** `gemma_subtypes` met per subtype:
- `naam`, `omschrijving`
- `ggm_entiteit`, `ggm_guid`, `ggm_attribuut` (verplicht bij GGM-match)

**Body:** Specialisaties-tabel met kolommen: Subtype, Omschrijving, GGM-attribuut.
GGM-attribuut bevat een markdown-link naar de GGM-entiteit in het bronbestand gevolgd door `→ attribuutnaam`. Geen GUID in de tabel — die staat in de frontmatter.

## Stap 7: BO-relaties afleiden

BO-relaties worden afgeleid van GGM-associaties maar vereenvoudigd naar bedrijfsniveau:

| Actie | Wanneer |
|---|---|
| **Overnemen** | Herkenbaar in de bedrijfspraktijk → 1-op-1 |
| **Inkorten** | GGM-relatie via tussenliggende entiteit die geen BO wordt → directe BO-relatie |
| **Samenvoegen** | Meerdere GGM-associaties op bedrijfsniveau niet onderscheidbaar |
| **Weglaten** | Puur technische relaties (referentietabellen, enumeraties) |
| **Toevoegen** | Relatie bestaat op bedrijfsniveau maar niet in GGM → hiaat-relatie |

## Stap 8: BO-pagina aanmaken

Vul het volledige frontmatter-schema in volgens `templates/bedrijfsobject.md`, inclusief `bronnen` (verwijzend naar relevante bronsamenvattingen).

Plaats in `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` — folderstructuur volgt de GGM-indeling (bijv. `7-volksgezondheid-en-milieu/milieu/`).

Body-secties volgens template:
- **BO-criteria toetsing**: welke criteria zijn van toepassing
- **Beschrijving**: het BO op het niveau waarop de gemeente erover praat
- **Specialisaties** (optioneel): tabel met subtypes
- **GGM-bron** (bij grondslag `ggm-entiteit`): letterlijke GGM-definitie als blockquote, matchsterkte
- **BO-definitie**: alleen als eigen definitie afwijkt van GGM
- **Relaties**: afgeleid van GGM-associaties of beleidsbronnen
- **Bedrijfsprocessen** en **Bedrijfsfuncties**
- **Terugmelding GGM** (indien van toepassing)

## Stap 9: Terugmeldingen

Bij afwijkingen of hiaten: voeg een regel toe aan `Wiki/Analyses/ggm-terugmeldingen.md`.
Typen: hiaat | definitie | structuur | scope. Status: open.

Bij geen match en data-object=ja: signaleer als potentieel GGM-hiaat (conform `/assess-bo` stap 10).

## Stap 10: Grondslag zonder GGM

Bij BO zonder GGM-grondslag: vul de `ggm_*` en `ggm_gemma_*` velden met lege waarden.

Voeg de juiste body-sectie toe:
- Bij `procesobject`: **Procesbron** — uit welk proces, link naar bronsamenvatting
- Bij `governance-object`: **Juridische bron** — welke wet/verordening, link naar bronsamenvatting
