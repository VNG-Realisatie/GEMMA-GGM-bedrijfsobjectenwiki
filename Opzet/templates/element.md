# Template: Element

Locatie:

- Bedrijfsobjecten: `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/{naam}.md` (`archimate_type`: business-object, contract of product)
- Actoren: `Wiki/Actoren/{naam}.md` (`archimate_type`: business-actor) — platte map
- Rollen: `Wiki/Rollen/{naam}.md` (`archimate_type`: business-role) — platte map

Zie `Wiki/GEMMA/actoren-en-rollen.md` voor het onderscheid actor/rol en de criteria. Bij actor-/rolpagina's blijven GGM-velden leeg zonder GGM-match; de overige structuur is gelijk.

## Frontmatter-stijl

- **Lege waarde:** niets na de dubbele punt (`ggm_guid:`) — nooit `""`, `''` of `~`.
- **Niet-lege tekstwaarde:** dubbele quotes wanneer nodig of voorgeschreven — altijd bij `bo_definitie` en bij `bo_relaties.bedrijfsobject`/`kardinaliteit`; bij overige velden alleen bij YAML-speciale tekens. Nooit enkele quotes.
- **Lege lijst:** `[]` (bijv. `bedrijfsprocessen: []`).
- **`bo_relaties.bedrijfsobject`:** altijd een gequote wiki-link, bijv. `"[[Wiki/.../vestiging|Vestiging]]"` — ongequote `[[...]]` breekt de YAML-parse (wordt een geneste lijst in plaats van een string).
- Wiki-brede normalisatie: `python3 tools/migrate_frontmatter_style.py`.

## Frontmatter

```yaml
---
type: element
naam: {naam}
onderwerp: [{onderwerp(en)}]
archimate_type: {business-object | contract | product | business-actor | business-role}
grondslag: {ggm-entiteit | ggm-afgeleid | procesobject | governance-object}

# GGM-velden — uit het XMI, beheerd door de GGM-community
ggm_entiteit: {naam van GGM-entiteit, leeg als niet van toepassing}
ggm_guid: {EA GUID, bijv. EAID_F9B2A863_...}
ggm_uml_type: {Class | Enumeration}
ggm_beleidsdomein: {GGM-beleidsdomein}
ggm_taakveld: {GGM-taakveld, bijv. "6 Sociaal Domein"}
ggm_diagram: [{namen van GGM-diagrammen met deze entiteit}]
ggm_diagram_ids: [{EA GUIDs van die diagrammen}]
ggm_definitie: {letterlijke GGM-definitie uit het XMI}
ggm_toelichting: {GGM-toelichting uit XMI-tag}
ggm_synoniemen: {GGM-synoniemen uit XMI-tag}
ggm_herkomst: {basisregistratie/standaard van herkomst}

# GEMMA-waarden zoals gevonden in het GGM XMI — referentie van eerdere import-cycli
ggm_gemma_naam: {GEMMA-naam in het GGM}
ggm_gemma_guid: {GEMMA-guid in het GGM}
ggm_gemma_definitie: {GEMMA-definitie in het GGM}
ggm_gemma_toelichting: {GEMMA-toelichting in het GGM}
ggm_gemma_synoniemen: {GEMMA-synoniemen in het GGM}
ggm_gemma_type: {GEMMA ArchiMate-type in het GGM, altijd "business-object"}
ggm_gemma_url: {GEMMA Online URL in het GGM}
ggm_gemma_bron: {GEMMA-bron in het GGM}
ggm_gemma_alternate_name: {GEMMA alternate name in het GGM}

# GGM-duplicaten — zelfde naam én zelfde concept in andere beleidsdomeinen
ggm_duplicaat_entiteiten: []
#  - entiteit: {naam}
#    guid: {EA GUID}
#    beleidsdomein: {beleidsdomein}
#    taakveld: {taakveld}
#    afwijkende_attributen: {korte beschrijving, leeg als identiek}

# Analyse-veld — scriptberekend door tools/entiteitendekking_sync_bo.py (stap 5 van de
# entiteitendekking-taak). Wordt bij elke sync herschreven — nooit handmatig bewerken.
analyse_ggm_dekking: ""

# Wiki-velden — het uit bronnen afgeleide BO-model, beheerd door het GEMMA-team
bo_definitie: {definitie op bedrijfsniveau — kort, bij voorkeur 1 zin ≤160 tekens; langer alleen letterlijk uit GGM of bron}
bo_toelichting: {aanvulling, uitleg of voorbeelden — ook op bronnen gebaseerd; leeg als de definitie volstaat}
bo_subtypes: []                     # DEPRECATED — subtypes staan in de body-sectie ## Subtypes; leeg laten bij nieuwe elementen
bo_via_kandidaten: []
#  - ggm_entiteit: {GGM-entiteit die "ter discussie" stond}
#    ggm_guid: {EA GUID}
#    reden: {waarom dit BO de juiste dekking is}
bo_synoniemen: []
#  - naam: {alternatieve naam}
#    context: {waar deze naam wordt gebruikt, bijv. "GGM", "beleidsdocumenten"}
bo_homoniemen: []
#  - bedrijfsobject: {wiki-link naar het andere BO}
#    ggm_entiteit: {GGM-entiteitnaam}
#    ggm_guid: {EA GUID van het andere concept}
#    ggm_beleidsdomein: {beleidsdomein van het andere concept}
#    toelichting: {waarom het een ander concept is}
element_tegenhangers: []            # cross-link bij het twee-pagina-patroon (actor/rol ↔ BO); beide pagina's mogen dezelfde ggm_guid dragen
#  - element: {wiki-link naar de tegenhanger-pagina}
#    archimate_type: {elementtype van de tegenhanger}
#    toelichting: {bijv. "de gegevens over deze actor worden vastgelegd als bedrijfsobject"}
bo_relaties:
  - type: {associatie | compositie | generalisatie}
    bedrijfsobject: "[[gerelateerd-bedrijfsobject]]"
    richting: {van-dit-BO | naar-dit-BO | bidirectioneel}
    kardinaliteit: {bijv. "1..*"}
    beschrijving: {korte omschrijving van de relatie}
bedrijfsprocessen: [{processen die dit object gebruiken/produceren}]
bedrijfsfuncties: [{bedrijfsfuncties}]
---
```

## Drie naamvelden

Elk kernveld bestaat in drie varianten:

| Veld | GGM (XMI-bron) | GGM-GEMMA (referentie) | Wiki (BO-model) |
|---|---|---|---|
| naam | `ggm_entiteit` | `ggm_gemma_naam` | `naam` |
| definitie | `ggm_definitie` | `ggm_gemma_definitie` | `bo_definitie` |
| toelichting | `ggm_toelichting` | `ggm_gemma_toelichting` | `bo_toelichting` |
| synoniemen | `ggm_synoniemen` | `ggm_gemma_synoniemen` | `bo_synoniemen` |

Bij een nieuwe GGM-release worden de `ggm_*`- en `ggm_gemma_*`-velden bijgewerkt uit het XMI; de `bo_*`-velden wijzigen alleen na een teambesluit.

## `analyse_ggm_dekking`

Beantwoordt per BO-pagina de omgekeerde vraag van de dekkingsrapporten: *welke GGM-entiteiten dekt dit BO?* Introzin over de eigen `ggm_entiteit`/`ggm_guid`-tegenhanger, gevolgd door bullets per indirect gedekte entiteit (detail/classificatie/component/duplicaat) met reden. **Volledig scriptgegenereerd** — nooit handmatig bewerken; BO's zonder GGM-betrokkenheid krijgen dit veld niet.

## Status

Elementpagina's kennen geen apart goedkeuringsmoment: is het proces doorlopen en klopt de onderbouwing, dan is het element vastgesteld. Markeer alleen `ter discussie` in de body wanneer een specifieke keuze teambespreking vereist.

## Grondslag

Het GGM modelleert data-objecten, geen processen of governance — er is dus altijd een klasse bedrijfsobjecten zonder GGM-grondslag.

| Grondslag | Betekenis | Voorbeeld |
|---|---|---|
| **ggm-entiteit** | 1:1- of n:1-mapping op een GGM-entiteit; definitie en attributen uit GGM | WOZ-object, Begroting |
| **ggm-afgeleid** | Geen eigen entiteit, wel afleidbaar uit GGM-objecten | solvabiliteitsratio |
| **procesobject** | Artefact dat in een proces ontstaat — structureel GGM-hiaat | belastingaanslag |
| **governance-object** | Juridisch/beleidsmatig kader — structureel GGM-hiaat | belastingverordening |

## Body

De elementpagina is een **beslisdocument**: waarom is dit een element, hoe verhoudt het zich tot het GGM, en welke metadata gaat naar het ArchiMate-model.

### Linkconventie body

- Gerelateerde BO's: `[[bedrijfsobject-naam]]` (bijv. `[[Stembureau]]`)
- Bronsamenvattingen: `[[Wiki/Bronsamenvattingen/{onderwerp}/{slug}|display-tekst]]`
- Analyses: `[[Wiki/Analyses/{slug}|display-tekst]]`
- In tabellen: escaped pipe — `[[pad\|alias]]`
- Citaten uit bronnen: platte tekst, geen links

### Secties

- **BO-criteria toetsing** — welke criteria van toepassing zijn, waarom dit een element is
- **Beschrijving** — het element op het niveau waarop de gemeente erover praat
- **Generalisatie** (optioneel) — positie in een opwaartse hiërarchie van BO's met gedeelde structuur
- **Specialisaties** (optioneel) — tabel met children die wél aparte BO's zijn
- **Subtypes** (optioneel) — lijst met herkende specialisaties die géén apart BO zijn
- **GGM-componenten** (optioneel) — GGM-entiteiten die onderdeel zijn van dit BO maar geen zelfstandig element
- **GGM-bron** (bij grondslag ggm-entiteit) — letterlijke GGM-definitie als blockquote, entiteitnaam, beleidsdomein, attributen, matchsterkte
- **Naamkeuze** (optioneel) — wanneer de naam afwijkt van de GGM-entiteitnaam door disambiguatie
- **GGM-duplicaten** (optioneel) — duplicaten en homoniemen met de primaire GUID-keuze
- **BO-definitie** (alleen bij afwijking van GGM) — GGM-definitie als blockquote, eigen definitie eronder, motivatie
- **Afleiding** (bij ggm-afgeleid) — welke GGM-objecten, welke berekening
- **Procesbron** (bij procesobject) — uit welk proces, met link naar de bronsamenvatting
- **Juridische bron** (bij governance-object) — welke wet/verordening, met link naar de bronsamenvatting
- **Relaties** — vereenvoudigd naar bedrijfsniveau, met bron per relatie
- **Bedrijfsprocessen** en **Bedrijfsfuncties**
- **Bronnen** — links naar de bronsamenvattingen waaruit dit element is afgeleid; géén alias (het pad toont wat voor bestand de bron is)
- **Terugmelding GGM** (indien van toepassing) — met link naar `Wiki/Analyses/ggm-terugmeldingen`

Actor-/rolpagina's zijn lichter: beschrijving, criteria-toetsing, rollen (actor) of vervuld-door (rol), relaties, bronnen, GGM-bron bij match.

### Format: Generalisatie

Voor een BO dat deel is van een hiërarchie van BO's met gedeelde structuur (het omgekeerde van Specialisaties).

```markdown
## Generalisatie

{BO-naam} is onderdeel van de {hiërarchie-naam}: [[Parent]] → [[Sibling]] → **{BO-naam}** → [[Child]].
Alle niveaus delen {gedeelde kenmerken}. {BO-naam} onderscheidt zich door {onderscheidend kenmerk}.
```

### Format: Specialisaties

Voor een overkoepelend BO met children die wél aparte BO's zijn. Parent: `generalisatie`-relaties met `richting: van-dit-BO`; elk child: dezelfde relatie terug met `richting: naar-dit-BO`.

```markdown
## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Child-BO]] | Korte omschrijving | [GGM-naam](Wiki/GGM/...) |
```

### Format: Subtypes en GGM-componenten

Zelfde format: inleidende zin + lijst met vetgedrukte GGM-entiteitnaam en toelichting. De analyse- en exporttools parsen de vetgedrukte namen.

```markdown
## Subtypes

Herkende specialisaties van {BO-naam}. Gevonden in bronnen en/of GGM. Geen apart BO.

- **{GGM-entiteitnaam}** — {korte toelichting}
```

```markdown
## GGM-componenten

GGM-entiteiten die onderdeel zijn van {BO-naam}. Apart gemodelleerd in het GGM ({reden}) maar geen zelfstandig bedrijfsobject.

- **{GGM-entiteitnaam}** — {korte toelichting}
```

**Overzicht hiërarchiesecties:**

| Sectie | Richting | Children apart BO? | Relatietype frontmatter | Dekkingslabel |
|---|---|---|---|---|
| Generalisatie | opwaarts | ja | `associatie` of `generalisatie` | *(geen — alle niveaus BO)* |
| Specialisaties | neerwaarts | ja | `generalisatie` (van-dit-BO) | *(geen — alle niveaus BO)* |
| Subtypes | neerwaarts | nee | — | `↓ subtype van {BO}` |
| GGM-componenten | neerwaarts | nee | — | `◆ onderdeel van {BO}` |

### Format: GGM-duplicaten

Voor entiteitnamen die in meerdere beleidsdomeinen hetzelfde concept vertegenwoordigen. Primaire GUID in `ggm_guid`; duplicaten in `ggm_duplicaat_entiteiten` en hier toegelicht.

Twee soorten (voor terugmelding): **echte duplicaten** (zelfde concept, twee GUIDs → terugmelding `duplicaat`: samenvoegen) en **homoniemen** (zelfde naam, ander concept → terugmelding `homoniem`: hernoemadvies). Homoniemen horen **niet** in `ggm_duplicaat_entiteiten` maar in `bo_homoniemen` (frontmatter) plus een cross-link in de body.

```markdown
## GGM-duplicaten

De GGM-entiteit "{naam}" komt voor in {n} beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **{primair beleidsdomein}** | `{GUID}` | **primair** — canonieke mapping omdat {motivatie} |
| {secundair beleidsdomein} | `{GUID}` | duplicaat — {toelichting} |

**Homoniem:** de GGM-entiteit "{naam}" in beleidsdomein {domein} is een ander concept ({korte uitleg}). Zie [[BO-van-dat-concept]].

Teruggemeld als #{nr} in [[Wiki/Analyses/ggm-terugmeldingen|ggm-terugmeldingen]].
```

### Format: Naamkeuze

Wanneer de elementnaam afwijkt van de GGM-entiteitnaam, typisch door homoniem-disambiguatie.

```markdown
## Naamkeuze

De GGM-entiteitnaam "{originele naam}" is een homoniem — in beleidsdomein {ander domein} staat dezelfde naam voor een ander concept. Dit BO heet **{gekozen naam}**.

**Overwogen namen:**
- **{gekozen naam}** — {waarom gekozen}
- {alternatief 1} — {waarom niet}
- {alternatief 2} — {waarom niet}
```
