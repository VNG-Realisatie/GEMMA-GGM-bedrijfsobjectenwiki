Leg vast als bedrijfsobject: $ARGUMENTS

Input: BO-naam (reeds beoordeeld via `/assess-bo`), of "onderwerp X" voor alle BO's in een onderwerp.

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
- Als een GGM-entiteit in **meerdere beleidsdomeinen** voorkomt als hetzelfde concept: maak één bedrijfsobject met de thematisch passende GUID als primair en de overige in `ggm_duplicaat_entiteiten`. Meld als `duplicaat` terug.
- Als een GGM-entiteitnaam in meerdere beleidsdomeinen een **ander concept** vertegenwoordigt: dit is een homoniem. Stel 2-3 alternatieve namen voor (zie stap 4c) en leg de keuze voor aan de gebruiker. Meld als `homoniem` terug.

## Stap 4b: GGM-duplicaten detecteren

Na de GGM-match: zoek of dezelfde entiteitnaam in andere beleidsdomeinen voorkomt.

1. **Zoek in `ggm_parsed.json`** naar alle entiteiten met dezelfde naam als de gematchte entiteit.
2. **Classificeer** elk voorkomen:
   - **Duplicaat** (zelfde concept, andere GUID) — typisch BAG vs RSGBPlus, of dezelfde entiteit in verwante domeinen
   - **Homoniem** (zelfde naam, ander concept) — bijv. Standplaats BAG vs Standplaats Musea (tentoonstellingsplek)
3. **Kies de primaire GUID** — het beleidsdomein waar het BO thematisch thuishoort. Leg de keuze voor aan de gebruiker.
4. **Vergelijk attributen** — als duplicaten afwijkende attributen hebben, beschrijf de verschillen.
5. **Vul frontmatter:**
   - `ggm_guid`: primaire GUID
   - `ggm_duplicaat_entiteiten`: lijst van duplicaten (niet homoniemen)
   - `bo_synoniemen`: andere namen voor hetzelfde concept (GGM-naam als die afwijkt, namen uit bronnen, dagelijks gebruik)
   - `bo_homoniemen`: bij homoniem-detectie — verwijzing naar de andere BO's met dezelfde GGM-entiteitnaam maar een ander concept. Elk item bevat: `bedrijfsobject` (wiki-link), `ggm_entiteit`, `ggm_guid`, `ggm_beleidsdomein`, `toelichting`
6. **Terugmelding:**
   - Duplicaten → type `duplicaat` in `Wiki/Analyses/ggm-terugmeldingen.md`
   - Homoniemen → type `homoniem` in `Wiki/Analyses/ggm-terugmeldingen.md`

## Stap 4c: Homoniem-naamkeuze

Bij homoniem-detectie (stap 4b): de BO-naam moet disambigueren. Stel **2-3 namen** voor en leg de keuze voor aan de gebruiker.

**Suggestiestrategieën:**
- Domein-prefix: bijv. "Onderwijs-inschrijving"
- Samengesteld woord: bijv. "Onderwijsinschrijving"
- Functionele naam: bijv. "Aanbestedings-inschrijving" (gericht op wat het concept doet)

**Regels:**
- Gebruik **niet** de GEMMA `ggm_gemma_alternate_name` conventie (bijv. "Inschrijving (Onderwijs)") als BO-naam — haakjes in bestandsnamen zijn ongewenst.
- De GGM-entiteitnaam wordt `ggm_entiteit`; de gekozen naam wordt `naam` en `ggm_gemma_naam`.
- Documenteer de naamkeuze in de body-sectie `## Naamkeuze` (zie template).
- Voeg de originele GGM-naam **niet** toe aan `bo_synoniemen` — bij een homoniem is de oude naam juist het probleem, geen synoniem. Het homoniem wordt gedocumenteerd in `bo_homoniemen` (zie stap 4b).

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

**Wiki-velden (BO-model):**

`bo_definitie` — kort, helder, goed leesbaar. Bij voorkeur 1 zin, max ~160 tekens. Langer mag alleen als de tekst letterlijk uit GGM of bron wordt overgenomen. Bepaal als volgt:

1. **GGM-definitie toetsen aan bronnen.** Vergelijk `ggm_definitie` (of `ggm_gemma_definitie` als die er is) inhoudelijk met de Sources-bestanden van dit onderwerp.
2. **Drie scenario's:**
   - **GGM klopt qua strekking** → neem de GGM-definitie letterlijk over als `bo_definitie`. Niet aanpassen.
   - **GGM wijkt inhoudelijk af van bronnen** → maak een eigen definitie gebaseerd op de bronnen. Als een bron een definitie bevat: neem die letterlijk over. Anders: afleiden uit hoe het begrip in de bronnen wordt gebruikt. Toon de brontekst en de voorgestelde definitie aan de gebruiker ter verificatie. Documenteer de afwijking in de body-sectie **BO-definitie**.
   - **GGM klopt maar is onvolledig** → neem de GGM-definitie letterlijk over als `bo_definitie`. Zet de aanvulling (uitleg, voorbeelden, verdere context) in `bo_toelichting`.
3. **Zonder GGM-match:** maak een definitie uit de bronnen. Bron-definitie letterlijk overnemen als die er is, anders afleiden.
4. **`bo_toelichting`:** aanvullingen, uitleg en voorbeelden — ook gebaseerd op bronnen, niet vrij verzonnen. Leeg laten als de definitie volstaat.

### Disambiguatie (BO-naam ≠ GGM-entiteitnaam)

Wanneer een BO een andere naam krijgt dan de GGM-entiteit (bijv. door naamconflict of verduidelijking):
- `naam`: de GEMMA-naam (bijv. "Marktstandplaats")
- `ggm_entiteit`: de originele GGM-entiteitnaam (bijv. "Standplaats") — behoudt de herleidbaarheid naar het GGM
- `ggm_gemma_naam`: de GEMMA-naam (bijv. "Marktstandplaats") — de naam waarmee dit BO naar het ArchiMate-model en GEMMA Online wordt geëxporteerd

Dit patroon geldt ook wanneer er geen GGM-match is maar het BO wel een herkenbare GEMMA-naam heeft: vul dan alleen `ggm_gemma_naam` met de GEMMA-naam en laat `ggm_entiteit` leeg.

## Stap 6: Hiërarchie vastleggen (generalisatie, specialisaties, subtypes)

Drie patronen, afhankelijk van de richting en of children aparte BO's zijn:

### 6a. Generalisatie (opwaarts — dit BO is onderdeel van een hiërarchie)

Gebruik `## Generalisatie` wanneer het BO onderdeel is van een conceptuele hiërarchie met andere BO's die dezelfde structuur delen (bijv. Gemeente → Woonplaats → Wijk → Buurt). Elk niveau is een zelfstandig BO.

**Body:** `## Generalisatie`-sectie met:
- De hiërarchie als keten met wiki-links (bijv. `[[Gemeente]] → [[Woonplaats]] → [[Wijk]] → **Buurt**`)
- Welke kenmerken alle niveaus delen
- Wat dit niveau onderscheidt

**Frontmatter:** de relaties naar andere niveaus worden als `associatie` of `generalisatie` opgenomen in `bo_relaties:`.

### 6b. Specialisaties (neerwaarts — dit BO heeft children die wél aparte BO's zijn)

Gebruik `## Specialisaties` wanneer het BO een overkoepelend concept is met specialisaties die elk een eigen BO-pagina hebben (bijv. Sportlocatie → Sportpark, Binnenlocatie).

**Body:** `## Specialisaties`-sectie met tabel (Subtype, Omschrijving, GGM-entiteit).

**Frontmatter:** `generalisatie`-relaties in `bo_relaties:` met `richting: van-dit-BO`. Elk child-BO heeft een corresponderende `generalisatie`-relatie met `richting: naar-dit-BO`.

### 6c. Subtypes (neerwaarts — children zijn géén apart BO)

Wanneer een BO herkende subtypes heeft die **geen apart BO** zijn (uitwisselbaar, zelfde register en processen):

**Subtypes identificeren uit drie bronnen:**

1. **Beleidsbronnen** — welke typen, categorieën of voorbeelden noemen de bronnen als aparte groep? Denk aan materiaaltypen (asfalt/beton/klinkers), functietypes (rijbaan/fietspad/voetpad), of specifieke modellen (Steegarmatuur). Als de bron het als apart type benoemt met eigen kenmerken (levensduur, inspectieregime, beheeraanpak), dan is het een subtype.
2. **GGM type-attributen** — entiteiten met `type`, `typePlus`, `toestelgroep`, `materiaal`, of vergelijkbare classificatie-attributen hebben per definitie subtypes. Het GGM implementeert subtypes als attribuutwaarden — dat is een implementatiekeuze, geen reden om subtypes niet te benoemen.
3. **GGM generalisatie-relaties** — aparte GGM-entiteiten die via generalisatie aan het BO-concept gerelateerd zijn. Let op: de GGM-hiërarchie kan afwijken van het beleidsperspectief (bijv. Brug zit onder Overbruggingsobject, niet onder Kunstwerk). Documenteer afwijkingen.

**Frontmatter:** `bo_subtypes` met per subtype:
- `naam`, `omschrijving`
- `ggm_entiteit`, `ggm_guid` (de GGM-entiteit waar dit subtype bij hoort — dat kan het parent-BO zijn als het subtype een attribuutwaarde is, of een aparte entiteit)
- `ggm_attribuut` (het GGM-attribuut dat het subtype draagt, leeg als het een aparte entiteit is)

**Body:** `## Subtypes`-sectie met lijst. Bij afwijking tussen beleids- en GGM-hiërarchie: toelichting onder de lijst.

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

Vul het volledige frontmatter-schema in volgens `templates/bedrijfsobject.md`.

Plaats in `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` — folderstructuur volgt de GGM-indeling (bijv. `7-volksgezondheid-en-milieu/milieu/`).

Body-secties volgens template:
- **BO-criteria toetsing**: welke criteria zijn van toepassing
- **Beschrijving**: het BO op het niveau waarop de gemeente erover praat
- **Generalisatie** (optioneel): positie in opwaartse hiërarchie van BO's met gedeelde structuur
- **Specialisaties** (optioneel): tabel met children-BO's (aparte BO-pagina's)
- **Subtypes** (optioneel): lijst met subtypes die geen apart BO zijn
- **GGM-bron** (bij grondslag `ggm-entiteit`): letterlijke GGM-definitie als blockquote, matchsterkte
- **Naamkeuze** (optioneel): wanneer stap 4c een homoniem-naamkeuze heeft opgeleverd. Overwogen namen en motivatie. Zie `templates/bedrijfsobject.md` voor format.
- **GGM-duplicaten** (optioneel): wanneer stap 4b duplicaten of homoniemen heeft gevonden. Tabel met primaire keuze, duplicaten en attribuutverschillen. Zie `templates/bedrijfsobject.md` voor format.
- **BO-definitie**: alleen als eigen definitie afwijkt van GGM
- **Relaties**: afgeleid van GGM-associaties of beleidsbronnen
- **Bedrijfsprocessen** en **Bedrijfsfuncties**
- **Bronnen**: wiki-links naar bronsamenvattingen waaruit dit BO is afgeleid
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
