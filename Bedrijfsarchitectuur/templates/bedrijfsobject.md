# Template: Bedrijfsobject

Locatie: `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/{naam}.md`

## Frontmatter

```yaml
---
type: bedrijfsobject
naam: {naam}
onderwerp: [{onderwerp(en)}]
archimate_type: {business-object | contract | product}
grondslag: {ggm-entiteit | ggm-afgeleid | procesobject | governance-object}

# GGM-velden — uit het XMI, beheerd door de GGM-community
ggm_entiteit: {naam van GGM-entiteit, leeg als niet van toepassing}
ggm_guid: {EA GUID van de GGM-entiteit, bijv. EAID_F9B2A863_...}
ggm_uml_type: {Class | Enumeration}
ggm_beleidsdomein: {GGM beleidsdomein}
ggm_taakveld: {GGM taakveld, bijv. "6 Sociaal Domein"}
ggm_diagram: [{namen van GGM-diagrammen waarop deze entiteit staat}]
ggm_diagram_ids: [{EA GUIDs van die diagrammen}]
ggm_definitie: {letterlijke GGM-definitie uit het XMI}
ggm_toelichting: {GGM-toelichting uit XMI-tag}
ggm_synoniemen: {GGM-synoniemen uit XMI-tag}
ggm_herkomst: {basisregistratie/standaard waaruit de entiteit afkomstig is}

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

# GGM-duplicaten — entiteiten met dezelfde naam in andere beleidsdomeinen die hetzelfde concept vertegenwoordigen
ggm_duplicaat_entiteiten: []
#  - entiteit: {naam}
#    guid: {EA GUID}
#    beleidsdomein: {beleidsdomein}
#    taakveld: {taakveld}
#    afwijkende_attributen: {korte beschrijving van attribuutverschillen, leeg als identiek}

# GEMMA-velden — beheerd door het GEMMA-team via deze wiki
gemma_definitie: {GEMMA-definitie op bedrijfsniveau, of "gelijk aan GGM" als er geen afwijking is}
gemma_subtypes: []                  # DEPRECATED — subtypes staan in de body-sectie ## Subtypes. Leeg laten bij nieuwe BO's.
relaties:
  - type: {associatie | compositie | generalisatie}
    bedrijfsobject: [[gerelateerd-bedrijfsobject]]
    richting: {van-dit-BO | naar-dit-BO | bidirectioneel}
    kardinaliteit: {bijv. "1..*"}
    beschrijving: {korte omschrijving van de relatie}
bedrijfsprocessen: [{bedrijfsprocessen die dit object gebruiken/produceren}]
bedrijfsfuncties: [{bedrijfsfuncties}]
---
```

### Linkconventie frontmatter

- **relaties.bedrijfsobject:** wiki-link naar het gerelateerde BO (bijv. `[[Verkiezing]]`)

### Drie naamvelden

Elk veld bestaat in een GGM-, GGM-GEMMA- en GEMMA-variant:

| Veld | GGM (XMI-bron) | GGM-GEMMA (referentie) | GEMMA (wiki/export) |
|---|---|---|---|
| naam | `ggm_entiteit` | `ggm_gemma_naam` | `naam` |
| definitie | `ggm_definitie` | `ggm_gemma_definitie` | `gemma_definitie` |
| toelichting | `ggm_toelichting` | `ggm_gemma_toelichting` | *(toekomstig)* |
| synoniemen | `ggm_synoniemen` | `ggm_gemma_synoniemen` | *(toekomstig)* |

Bij een nieuwe GGM-release worden de `ggm_*` velden bijgewerkt uit het nieuwe XMI en de `ggm_gemma_*` velden uit de GEMMA-tags in dat XMI. De wiki `gemma_*` velden worden alleen gewijzigd als het team besluit dat de nieuwe GGM-waarden een update rechtvaardigen.

### Status

BO-pagina's hebben geen apart goedkeuringsmoment. Als het proces is doorlopen en de onderbouwing klopt, is het BO vastgesteld. Markeer alleen als `ter discussie` in de body wanneer een specifieke keuze (bijv. generalisatieniveau, GGM-afwijking) niet eenduidig is en teambespreking vereist.

### Grondslag

Geeft aan waarop het bedrijfsobject is gebaseerd. Het GGM modelleert data-objecten maar niet processen of governance (zie [[ggm-dekkingspatroon]]). Er zal daarom altijd een klasse bedrijfsobjecten zijn zonder GGM-grondslag.

| Grondslag | Betekenis | GGM-relatie | Voorbeeld |
|---|---|---|---|
| **ggm-entiteit** | 1:1 of n:1 mapping op een GGM-entiteit | Directe match; definitie en attributen uit GGM | WOZ-object, Begroting, Debiteur |
| **ggm-afgeleid** | Afleidbaar uit bestaande GGM-objecten | Geen eigen entiteit, wel berekbaar | *(toekomstig: solvabiliteitsratio als BO)* |
| **procesobject** | Artefact dat in een proces ontstaat, niet in GGM gemodelleerd | Structureel hiaat — GGM dekt processen niet | *(toekomstig: belastingaanslag, kadernota)* |
| **governance-object** | Juridisch of beleidsmatig kader dat processen aanstuurt | Structureel hiaat — GGM dekt governance niet | *(toekomstig: belastingverordening)* |

## Body

De BO-pagina is een **beslisdocument**: het onderbouwt waarom dit een bedrijfsobject is, hoe het zich verhoudt tot het GGM, en welke metadata naar het ArchiMate-model gaat.

### Linkconventie body

- **Verwijzingen naar gerelateerde BO's:** `[[bedrijfsobject-naam]]` (bijv. `[[Stembureau]]`, `[[Begroting]]`)
- **Verwijzingen naar bronsamenvattingen:** `[[Wiki/Bronsamenvattingen/{onderwerp}/{slug}}|display-tekst]` (bijv. `[[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda|Verkiezingen en referenda]]`)
- **Verwijzingen naar analyses:** `[[Wiki/Analyses/analyse-slug|display-tekst]]` (bijv. `[[Wiki/Analyses/ggm-dekkingspatroon]]`)
- **Citaten uit bronnen:** platte tekst (geen links)

### Secties

- **BO-criteria toetsing**: welke criteria zijn van toepassing, waarom is dit een BO
- **Beschrijving**: het bedrijfsobject op het niveau waarop er in de gemeente over wordt gepraat
- **Generalisatie** (optioneel): als dit BO onderdeel is van een conceptuele hiërarchie met andere BO's die dezelfde structuur delen (bijv. gebiedsindelingen, locatietypen). Beschrijft de hiërarchie en wat dit niveau onderscheidt. Zie [format hieronder](#generalisatie-format).
- **Specialisaties** (optioneel): als dit BO een overkoepelend concept is met specialisaties die wél aparte BO's zijn (bijv. Sportlocatie → Sportpark, Binnenlocatie). Tabel met links naar de specialisatie-BO's. Zie [format hieronder](#specialisaties-format).
- **Subtypes** (optioneel): herkende specialisaties die geen apart BO zijn maar wel herkenbaar in de praktijk. Gevonden in bronnen én/of GGM. Gestructureerd als lijst met vetgedrukte naam en toelichting. Zie [format hieronder](#subtypes-en-ggm-componenten-format).
- **GGM-componenten** (optioneel): GGM-entiteiten die onderdeel zijn van dit BO (procesfasen, deelregistraties) maar geen zelfstandig bedrijfsobject. Alleen uit GGM, niet noodzakelijk gevonden in bronnen. Zelfde format als Subtypes. Zie [format hieronder](#subtypes-en-ggm-componenten-format).
- **GGM-bron** (bij grondslag `ggm-entiteit`): letterlijke GGM-definitie als blockquote, entiteitnaam, beleidsdomein, attributen, matchsterkte
- **GGM-duplicaten** (optioneel): wanneer dezelfde entiteitnaam in meerdere GGM-beleidsdomeinen voorkomt en hetzelfde concept vertegenwoordigt (bijv. BAG en RSGBPlus). Beschrijft welke duplicaten bestaan, waarom de primaire GUID is gekozen, en eventuele attribuutverschillen. Zie [format hieronder](#ggm-duplicaten-format). **Niet** gebruiken voor homoniemen (zelfde naam, ander concept).
- **BO-definitie**: alleen als de eigen definitie afwijkt van de GGM-definitie — beide opnemen zodat het verschil terugkoppelbaar is
- **Afleiding** (bij grondslag `ggm-afgeleid`): welke GGM-objecten, welke berekening/aggregatie
- **Procesbron** (bij grondslag `procesobject`): uit welk proces, welke beleidsbron beschrijft dit — **link naar de bronsamenvatting**
- **Juridische bron** (bij grondslag `governance-object`): welke wet/verordening, welke beleidsbron — **link naar de bronsamenvatting**
- **Relaties**: afgeleid van GGM-associaties (bij GGM-grondslag) of uit beleidsbronnen (bij overige grondslagen), vereenvoudigd naar bedrijfsniveau. Noteer de bron van elke relatie — wiki-links naar gerelateerde BO's, in tabellen met `\|`-escaped alias (bijv. `[[Wiki/.../boom\|Boom]]`)
- **Bedrijfsprocessen**: welke processen dit object gebruiken of produceren
- **Bedrijfsfuncties**: welke functies dit object raken
- **Bronnen**: wiki-links naar bronsamenvattingen waaruit dit BO is afgeleid (bijv. `[[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda]]`). Geen alias — het pad maakt expliciet wat voor soort bestand de bron is.
- **Terugmelding GGM** (indien van toepassing): correcties, ontbrekende entiteiten, afwijkende definities — **link naar [[Wiki/Analyses/ggm-terugmeldingen]]**

### Generalisatie format

Gebruik `## Generalisatie` wanneer het BO onderdeel is van een hiërarchie van BO's die dezelfde structuur delen maar elk een eigen BO zijn. Dit is het omgekeerde van Specialisaties: het beschrijft de positie van dit BO in een opwaartse hiërarchie.

```markdown
## Generalisatie

{BO-naam} is onderdeel van de {hiërarchie-naam}: [[Parent]] → [[Sibling]] → **{BO-naam}** → [[Child]]. Alle niveaus delen {gedeelde kenmerken}. {BO-naam} onderscheidt zich door {onderscheidend kenmerk}.
```

Voorbeeld: Buurt beschrijft dat het het laagste niveau is van Gemeente → Woonplaats → Wijk → Buurt, met als gedeeld patroon: code, naam, geometrie, geldigheidsperiode.

### Specialisaties format

Gebruik `## Specialisaties` wanneer het BO een overkoepelend concept is met specialisaties die **wél aparte BO's** zijn. Het parent-BO heeft `generalisatie`-relaties in frontmatter (`richting: van-dit-BO`); elk child-BO heeft een `generalisatie`-relatie terug (`richting: naar-dit-BO`).

```markdown
## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Child-BO]] | Korte omschrijving | [GGM-naam](Wiki/GGM/...) |
```

Voorbeeld: Sportlocatie heeft Specialisaties met Sportpark en Binnenlocatie als aparte BO's.

### Subtypes en GGM-componenten format

Beide secties gebruiken hetzelfde format: een inleidende zin, gevolgd door een lijst met vetgedrukte GGM-entiteitnaam en toelichting. De coverage- en export-tools parsen de vetgedrukte namen.

```markdown
## Subtypes

Herkende specialisaties van {BO-naam}. Gevonden in bronnen en/of GGM. Geen apart BO.

- **{GGM-entiteitnaam}** — {korte toelichting}
- **{GGM-entiteitnaam}** — {korte toelichting}
```

```markdown
## GGM-componenten

GGM-entiteiten die onderdeel zijn van {BO-naam}. Gemodelleerd als aparte entiteiten in het GGM ({reden, bijv. "voor DDAS-rapportage"}) maar vormen geen zelfstandig bedrijfsobject.

- **{GGM-entiteitnaam}** — {korte toelichting}
- **{GGM-entiteitnaam}** — {korte toelichting}
```

**Overzicht hiërarchiesecties:**

| Sectie | Richting | Children zijn BO? | Relatietype frontmatter | Coverage-label |
|---|---|---|---|---|
| **Generalisatie** | opwaarts (dit BO → parent) | ja (zelfstandige BO's) | `associatie` of `generalisatie` | *(geen — alle niveaus zijn BO)* |
| **Specialisaties** | neerwaarts (dit BO → children) | ja (aparte BO's) | `generalisatie` (van-dit-BO) | *(geen — alle niveaus zijn BO)* |
| **Subtypes** | neerwaarts (dit BO → children) | nee (geen apart BO) | — | `↓ subtype van {BO}` |
| **GGM-componenten** | neerwaarts (dit BO → parts) | nee (geen apart BO) | — | `◆ onderdeel van {BO}` |

### GGM-duplicaten format

Gebruik `## GGM-duplicaten` wanneer dezelfde GGM-entiteitnaam in meerdere beleidsdomeinen voorkomt en hetzelfde concept vertegenwoordigt. De primaire GUID staat in `ggm_guid`; de duplicaten staan in `ggm_duplicaat_entiteiten` (frontmatter) en worden hier toegelicht.

**Twee soorten duplicaten (voor terugmelding):**
- **Echte duplicaten** — zelfde concept, twee GUIDs (bijv. BAG en RSGBPlus) → terugmelding type `duplicaat`: "samenvoegen"
- **Homoniemen** — zelfde naam, ander concept (bijv. Standplaats BAG vs Standplaats Musea) → terugmelding type `homoniem`: "hernoemadvies"

Homoniemen worden **niet** in `ggm_duplicaat_entiteiten` opgenomen (het is een ander concept), maar wél in de body vermeld als waarschuwing.

```markdown
## GGM-duplicaten

De GGM-entiteit "{naam}" komt voor in {n} beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **{primair beleidsdomein}** | `{GUID}` | **primair** — gekozen als canonieke mapping omdat {motivatie} |
| {secundair beleidsdomein} | `{GUID}` | duplicaat — {toelichting, bijv. "identieke attributen"} |

{Optioneel: beschrijving van attribuutverschillen}

**Homoniem:** de GGM-entiteit "{naam}" in beleidsdomein {domein} is een ander concept ({korte uitleg}). Zie [[BO-van-dat-concept]] / niet te verwarren.

Teruggemeld als #{nr} in [[Wiki/Analyses/ggm-terugmeldingen]].
```
