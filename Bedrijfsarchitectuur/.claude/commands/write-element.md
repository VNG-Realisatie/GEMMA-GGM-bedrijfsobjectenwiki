Leg vast als element (bedrijfsobject, actor, rol, bedrijfsfunctie of bedrijfsproces): $ARGUMENTS

Input: elementnaam (reeds beoordeeld via `/assess-element`), of "onderwerp X" voor alle elementen in een onderwerp.
Output: `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/`, `Wiki/Actoren/`, `Wiki/Rollen/`, `Wiki/Bedrijfsfuncties/{taakveld}/{beleidsdomein}/` of `Wiki/Bedrijfsprocessen/{taakveld}/{beleidsdomein}/`.

Verwacht een begrip dat al is beoordeeld. Doet zelf géén criteria-toetsing of domeinbepaling.

**Elementtype bepaalt de route:** bedrijfsobjecten (business-object/contract/product) volgen alle stappen hieronder. Actor- en rol-pagina's volgen Stap 11. Bedrijfsfunctie- en bedrijfsproces-pagina's volgen Stap 12. Bij het twee-pagina-patroon (begrip is actor/rol én BO, zie `/assess-element` Stap 2b; of, als uitzondering, bedrijfsfunctie/-proces én BO, zie `/assess-element` Stap 2c): maak beide pagina's en koppel ze via `element_tegenhangers`.

## Stap 0: Naamgeving en disambiguatie

Elke BO-naam moet op zichzelf ondubbelzinnig zijn, ongeacht grondslag. Een naamcollisie kan blijken uit:
- **Wiki-collisie** — de naam wordt al door een ander BO gebruikt (grep op de naam in `Wiki/Bedrijfsobjecten/`). Geldt voor elke grondslag.
- **GGM-homoniem** — stap 4b vindt dezelfde GGM-entiteitnaam voor een ander concept in een ander beleidsdomein. Geldt alleen bij `grondslag: ggm-entiteit`; meld ook terug als `homoniem` (stap 4b/9).

**Bij een collisie:** stel 2-3 alternatieve namen voor, leg de keuze voor aan de gebruiker.
- Domein-prefix: bijv. "Onderwijs-inschrijving"
- Samengesteld woord: bijv. "Onderwijsinschrijving"
- Functionele naam: bijv. "Aanbestedings-inschrijving" (gericht op wat het concept doet)

Gebruik **niet** de GEMMA `ggm_gemma_alternate_name`-conventie (bijv. "Inschrijving (Onderwijs)") als bestandsnaam — haakjes in bestandsnamen zijn ongewenst. Documenteer de keuze in `## Naamkeuze` (zie template).

**Bij een GGM-homoniem specifiek:** `ggm_entiteit` blijft de originele GGM-naam (behoudt herleidbaarheid naar het GGM); `naam` en `ggm_gemma_naam` krijgen de nieuw gekozen, ondubbelzinnige naam. De originele GGM-naam mag als synoniem in `bo_synoniemen` (GGM-namen kunnen synoniem zijn); het homoniem zelf wordt gedocumenteerd in `bo_homoniemen` (stap 4b).

## Stap 1: Grondslag bepalen

Bepaal de grondslag van het BO via deze cascade:

| Stap | Vraag | Grondslag |
|---|---|---|
| 1 | Is er een directe GGM-entiteit? | `ggm-entiteit` |
| 2 | Geen entiteit, wel afleidbaar uit bestaande GGM-objecten? | `ggm-afgeleid` |
| 3 | Geen GGM-basis, wel een artefact dat in een gemeentelijk proces ontstaat? | `procesobject` |
| 4 | Geen GGM-basis, juridisch/beleidsmatig kader? | `governance-object` |

Het ontbreken van een GGM-grondslag is voor procesobjecten en governance-objecten normaal: het GGM dekt deze doorgaans niet compleet (geen categorische uitsluiting; zie `/assess-element` Stap 10).

## Stap 2: GGM-match zoeken

Zoek in `ggm_parsed.json` naar kandidaat-entiteiten:
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

**Naam bij sterk/partieel-match met een bredere GGM-entiteit** ([BO4]–[BO11]): de BO-naam blijft het gemeentelijke beleidsbegrip; leg de afwijking vast in `## GGM-bron`, niet in `## Naamkeuze`; hernoemen alleen bij een uitzondering en nooit in bulk.

## Stap 4: Mapping-regels

- Bij voorkeur **1-op-1 mapping** (beheerbaarheid, herkenbaarheid).
- **Aggregatie** toegestaan als het GGM te granulair is — noteer welke GGM-entiteiten zijn samengevoegd.
- Als een GGM-entiteit in **meerdere beleidsdomeinen** voorkomt als hetzelfde concept: maak één bedrijfsobject met de thematisch passende GUID als primair en de overige in `ggm_duplicaat_entiteiten`. Meld als `duplicaat` terug. Plaatsing per geval beoordelen (geen vaste domeinregel). De GEMMA-export genereert één rij per GUID, alle naar hetzelfde concept.
- Als een GGM-entiteitnaam in meerdere beleidsdomeinen een **ander concept** vertegenwoordigt: dit is een homoniem. Stel 2-3 alternatieve namen voor (zie stap 0) en leg de keuze voor aan de gebruiker. Meld als `homoniem` terug.

## Stap 4b: GGM-duplicaten detecteren

**Alleen van toepassing bij `grondslag: ggm-entiteit`.** Een homoniem is per definitie een naamcollisie tussen twee GGM-entiteiten — niet tussen twee wiki-BO's (zie stap 0). Heeft dit BO geen eigen `ggm_entiteit` (grondslag `procesobject`, `ggm-afgeleid` of `governance-object`), dan kan het geen homoniem hebben, ook niet als de BO-naam toevallig lijkt op een andere BO. `bo_homoniemen` blijft dan `[]`.

Na de GGM-match: zoek of dezelfde entiteitnaam in andere beleidsdomeinen voorkomt. Detectie is een signaal; de classificatie duplicaat/homoniem is een beslissing van de gebruiker.

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

Bij homoniem-detectie: kies een ondubbelzinnige naam volgens stap 0.

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

`bo_definitie` — vormcriteria: zie [VR3]. Bepaal de inhoud als volgt:

1. **GGM-definitie toetsen aan bronnen.** Vergelijk `ggm_definitie` (of `ggm_gemma_definitie` als die er is) inhoudelijk met de Sources-bestanden van dit onderwerp. Een GGM-definitie die leeg is, alleen een placeholder bevat (bijv. `~`, `-`, `?`, `TODO`) of geen inhoudelijke omschrijving geeft, telt als "geen definitie" — behandel als scenario 3 (zonder GGM-match).
2. **Drie scenario's:**
   - **GGM klopt qua strekking** → neem de GGM-definitie over als `bo_definitie`. Niet inhoudelijk aanpassen. Wel opschonen: taalfouten corrigeren (tikfouten, afbrekingen, ontbrekende spaties), HTML-tags en HTML-entities verwijderen (bijv. `<font>`, `<b>`, `&#243;` → ó), en opsommingen, voorbeelden of uitweidingen verplaatsen naar `bo_toelichting`. De definitie bevat de kernomschrijving; de toelichting bevat de uitleg. Dit is geen afwijking en hoeft niet gedocumenteerd te worden.
   - **GGM wijkt inhoudelijk af van bronnen** → maak een eigen definitie gebaseerd op de bronnen. Als een bron een definitie bevat: neem die letterlijk over. Anders: afleiden uit hoe het begrip in de bronnen wordt gebruikt. Toon de brontekst en de voorgestelde definitie aan de gebruiker ter verificatie. Documenteer de afwijking in de body-sectie **BO-definitie**.
   - **GGM klopt maar is onvolledig** → neem de GGM-definitie letterlijk over als `bo_definitie`. Zet de aanvulling (uitleg, voorbeelden, verdere context) in `bo_toelichting`.
3. **Zonder GGM-match:** maak een definitie uit de bronnen. Bron-definitie letterlijk overnemen als die er is, anders afleiden.
4. **`bo_toelichting`:** aanvullingen, uitleg en voorbeelden — ook gebaseerd op bronnen, niet vrij verzonnen. Leeg laten als de definitie volstaat.
5. **Algemeen:** gebruik alleen informatie uit de Sources-bestanden van het onderwerp. Een eigen definitie is alleen gerechtvaardigd bij inhoudelijke afwijking van de bronnen en moet verifieerbaar zijn. De definitie beschrijft wat het ding is, niet waar het staat (geen registr*-taal, [BO1]).

### Disambiguatie (BO-naam ≠ GGM-entiteitnaam)

Wanneer een BO een andere naam krijgt dan de GGM-entiteit (bijv. door naamconflict of verduidelijking):
- `naam`: de GEMMA-naam (bijv. "Marktstandplaats")
- `ggm_entiteit`: de originele GGM-entiteitnaam (bijv. "Standplaats") — behoudt de herleidbaarheid naar het GGM
- `ggm_gemma_naam`: de GEMMA-naam (bijv. "Marktstandplaats") — de naam waarmee dit BO naar het ArchiMate-model en GEMMA Online wordt geëxporteerd

Dit patroon geldt ook wanneer er geen GGM-match is maar het BO wel een herkenbare GEMMA-naam heeft: vul dan alleen `ggm_gemma_naam` met de GEMMA-naam en laat `ggm_entiteit` leeg.

## Stap 6: Hiërarchie vastleggen (generalisatie, specialisaties)

Twee patronen, afhankelijk van de richting:

### 6a. Generalisatie (opwaarts — dit BO is onderdeel van een hiërarchie)

Gebruik `## Generalisatie` wanneer het BO onderdeel is van een conceptuele hiërarchie met andere BO's die dezelfde structuur delen (bijv. Gemeente → Woonplaats → Wijk → Buurt). Elk niveau is een zelfstandig BO.

**Body:** `## Generalisatie`-sectie met:
- De hiërarchie als keten met wiki-links (bijv. `[[Gemeente]] → [[Woonplaats]] → [[Wijk]] → **Buurt**`)
- Welke kenmerken alle niveaus delen
- Wat dit niveau onderscheidt

**Frontmatter:** de relaties naar andere niveaus worden als `associatie` of `generalisatie` opgenomen in `bo_relaties:`.

### 6b. Specialisaties (neerwaarts — dit BO heeft herkende specialisaties, met of zonder eigen BO-pagina)

Gebruik `## Specialisaties` wanneer het BO een overkoepelend concept is met herkende specialisaties. Eén sectie, ongeacht of een specialisatie een eigen pagina krijgt — dat verschil blijkt uit de rij zelf, niet uit een aparte sectie.

**Met eigen pagina** (bijv. Sportlocatie → Sportpark, Binnenlocatie): de specialisatie haalt zelf de 6 BO-criteria (eigen processen/relaties).
- **Body:** rij is een `[[wiki-link]]` naar de eigen BO-pagina.
- **Frontmatter:** `generalisatie`-relatie in `bo_relaties:` met `richting: van-dit-BO`. Het child-BO heeft er zelf een terug (`richting: naar-dit-BO`).

**Zonder eigen pagina** (bijv. Woning → Sociale huurwoning): uitwisselbaar, zelfde register en processen als de ouder — haalt de 6 criteria niet zelfstandig.
- **Body:** rij is platte tekst (geen link).
- **Frontmatter:** `bo_subtypes` met per item `naam`, `omschrijving`, `ggm_entiteit`, `ggm_guid` (de GGM-entiteit waar dit bij hoort — dat kan het parent-BO zijn als het een attribuutwaarde is, of een aparte entiteit), `ggm_attribuut` (het GGM-attribuut dat de specialisatie draagt, leeg als het een aparte entiteit is).

**Specialisaties zonder eigen pagina identificeren uit drie bronnen:**

1. **Beleidsbronnen** — welke typen, categorieën of voorbeelden noemen de bronnen als aparte groep? Denk aan materiaaltypen (asfalt/beton/klinkers), functietypes (rijbaan/fietspad/voetpad), of specifieke modellen (Steegarmatuur). Als de bron het als apart type benoemt met eigen kenmerken (levensduur, inspectieregime, beheeraanpak), dan is het zo'n specialisatie.
2. **GGM type-attributen** — entiteiten met `type`, `typePlus`, `toestelgroep`, `materiaal`, of vergelijkbare classificatie-attributen hebben per definitie specialisaties. Het GGM implementeert ze als attribuutwaarden — dat is een implementatiekeuze, geen reden om ze niet te benoemen.
3. **GGM generalisatie-relaties** — aparte GGM-entiteiten die via generalisatie aan het BO-concept gerelateerd zijn. Let op: de GGM-hiërarchie kan afwijken van het beleidsperspectief (bijv. Brug zit onder Overbruggingsobject, niet onder Kunstwerk). Documenteer afwijkingen.

Bij twee onafhankelijke classificatie-assen (bijv. Woning naar marktsegment én naar bouwvorm): subkopjes `### Naar {as}`, elk met een eigen tabel. Bij afwijking tussen beleids- en GGM-hiërarchie: toelichting onder de tabel.

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

Vul het volledige frontmatter-schema in volgens `templates/element.md`.

Regels voor wiki-content ([WC7]–[WC11]): geen verwijzingen naar `CLAUDE.md`, `templates/`, `tools/` of skills; geen absolute taal ("structureel buiten scope", "per definitie") zonder domeinspecifieke onderbouwing.

Plaats in `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` — folderstructuur volgt de GGM-indeling (bijv. `7-volksgezondheid-en-milieu/milieu/`).

Body-secties volgens template:
- **BO-criteria toetsing**: welke criteria zijn van toepassing
- **Beschrijving**: het BO op het niveau waarop de gemeente erover praat
- **Generalisatie** (optioneel): positie in opwaartse hiërarchie van BO's met gedeelde structuur
- **Specialisaties** (optioneel): tabel met herkende specialisaties — `[[wiki-link]]` bij een eigen BO-pagina, platte tekst zonder
- **GGM-bron** (bij grondslag `ggm-entiteit`): letterlijke GGM-definitie als blockquote, matchsterkte
- **Naamkeuze** (optioneel): wanneer stap 0 een naamkeuze heeft opgeleverd. Overwogen namen en motivatie. Zie `templates/element.md` voor format.
- **GGM-duplicaten** (optioneel): wanneer stap 4b duplicaten of homoniemen heeft gevonden. Tabel met primaire keuze, duplicaten en attribuutverschillen. Zie `templates/element.md` voor format.
- **BO-definitie**: alleen als eigen definitie afwijkt van GGM
- **Relaties**: afgeleid van GGM-associaties of beleidsbronnen
- **Bedrijfsprocessen** en **Bedrijfsfuncties**
- **Bronnen**: wiki-links naar bronsamenvattingen waaruit dit BO is afgeleid
- **Terugmelding GGM** (indien van toepassing)

## Stap 9: Terugmeldingen

Bij afwijkingen of hiaten: voeg een regel toe aan `Wiki/Analyses/ggm-terugmeldingen.md` conform `templates/ggm-terugmelding.md`.
Typen: hiaat | definitie | structuur | scope | duplicaat | homoniem (zie `templates/ggm-terugmelding.md`). Status: open.

Bij geen match en data-object=ja: signaleer als potentieel GGM-hiaat (conform `/assess-element` stap 10).

## Stap 10: Grondslag zonder GGM

Bij BO zonder GGM-grondslag: vul de `ggm_*` en `ggm_gemma_*` velden met lege waarden.

Voeg de juiste body-sectie toe:
- Bij `procesobject`: **Procesbron** — uit welk proces, link naar bronsamenvatting
- Bij `governance-object`: **Juridische bron** — welke wet/verordening, link naar bronsamenvatting

## Stap 11: Actor- en rol-pagina's

Voor begrippen die via `/assess-element` Stap 2b als actor of rol zijn beoordeeld (definities en criteria: `templates/elementtype-criteria.md` §Actor en rol).

**Locatie en frontmatter:**
- Actor: `Wiki/Actoren/{naam}.md` met `archimate_type: business-actor`
- Rol: `Wiki/Rollen/{naam}.md` met `archimate_type: business-role`
- Beide mappen zijn plat — geen taakveld-substructuur; het taakveld/onderwerp staat in de frontmatter.
- Gebruik hetzelfde frontmatter-schema als `templates/element.md` (`type: element`). Niet alle velden worden gevuld: `grondslag` en de `bo_*`-velden gelden ook hier, maar GGM-velden blijven leeg zonder GGM-match.

**GGM-match:** doorloop Stap 2-5 zoals bij een BO. Bij een match: vul `ggm_entiteit`/`ggm_guid` zoals gebruikelijk — de dekkingsanalyse matcht hierop. Zonder match: velden leeg laten; rollen zonder GGM-match zijn vaak governance-hiaten (Stap 9-terugmelding overwegen).

**Twee-pagina-patroon:** haalt het begrip óók de 6 BO-criteria (er worden gegevens over vastgelegd), maak dan daarnaast de reguliere BO-pagina in `Wiki/Bedrijfsobjecten/`. Koppel beide pagina's:
- frontmatter: `element_tegenhangers` op beide pagina's (zie `templates/element.md`)
- body: een cross-link met één zin over de relatie (bijv. "De gegevens over deze actor worden vastgelegd als bedrijfsobject [[...]].")
- beide pagina's mogen dezelfde `ggm_guid` dragen; elke pagina heeft een **eigen definitie** vanuit het eigen perspectief (wie handelt vs. welke gegevens worden vastgelegd).

**Body-secties** (lichter dan een BO-pagina):
- **Beschrijving**: de actor/rol op het niveau waarop de gemeente erover praat
- **Criteria-toetsing**: uitkomst van de actor-/rol-vragen (Stap 2b)
- **Rollen** (bij een actor, optioneel): welke rollen deze actor vervult, als wiki-links
- **Vervuld door** (bij een rol, optioneel): welke actoren deze rol typisch vervullen, als wiki-links
- **Relaties**: naar andere elementen
- **Bronnen**: wiki-links naar bronsamenvattingen
- **GGM-bron** (bij GGM-match): letterlijke GGM-definitie als blockquote, matchsterkte

Nazorg is gelijk aan BO-pagina's: `Wiki/index.md`, `Wiki/log.md` en het onderwerpoverzicht bijwerken.

## Stap 12: Bedrijfsfunctie- en bedrijfsprocespagina's

Voor begrippen die via `/assess-element` Stap 2c als bedrijfsfunctie of bedrijfsproces zijn beoordeeld (definities en criteria: `templates/elementtype-criteria.md` §Bedrijfsfunctie en bedrijfsproces).

**Locatie en frontmatter:**
- Bedrijfsfunctie: `Wiki/Bedrijfsfuncties/{taakveld}/{beleidsdomein}/{naam}.md` met `archimate_type: business-function`
- Bedrijfsproces: `Wiki/Bedrijfsprocessen/{taakveld}/{beleidsdomein}/{naam}.md` met `archimate_type: business-process`
- Anders dan Actoren/Rollen volgen beide mappen dezelfde taakveld/beleidsdomein-substructuur als Bedrijfsobjecten (besluit 2026-09-23).
- Gebruik hetzelfde frontmatter-schema als `templates/element.md` (`type: element`). GGM-velden blijven doorgaans leeg (zie GGM-verwachting hieronder).

**GGM-match:** doorloop Stap 2-5 zoals bij een BO, maar verwacht doorgaans geen match — het GGM modelleert functies/processen niet compleet (zelfde voorbehoud als grondslag `procesobject`/`governance-object`). Bij toch een match: vul `ggm_entiteit`/`ggm_guid` zoals gebruikelijk. Zonder match: velden leeg laten, geen terugmelding als hiaat (zie `templates/elementtype-criteria.md` §GGM-verwachting).

**Twee-pagina-patroon (uitzondering, niet de regel):** alleen als de 6 BO-criteria ook zelfstandig slagen, maak dan daarnaast de reguliere BO-pagina in `Wiki/Bedrijfsobjecten/`. Koppel beide pagina's zoals bij actor/rol: `element_tegenhangers` op beide pagina's, een cross-link in de body, eventueel dezelfde `ggm_guid`.

**Terugverwijzing vanuit BO's:** een BO dat deze functie/dit proces gebruikt of produceert, verwijst ernaar via het `bedrijfsprocessen`/`bedrijfsfuncties`-veld in zijn eigen frontmatter (wiki-link, zie `templates/element.md`) — niet andersom. Werk bij het aanmaken van deze pagina de BO's bij die er al in vrije tekst naar verwezen (gesignaleerd door `/lint`, zie `.claude/commands/lint.md`).

**Body-secties** (lichter dan een BO-pagina, analoog aan actor/rol):
- **Beschrijving**: de functie/het proces op het niveau waarop de gemeente erover praat
- **Criteria-toetsing**: uitkomst van de functie-/proces-vragen (Stap 2c)
- **Gebruikt door** (optioneel): welke BO's deze functie/dit proces gebruiken of produceren, als wiki-links (spiegelbeeld van het `bedrijfsprocessen`/`bedrijfsfuncties`-veld op die BO's)
- **Relaties**: naar andere elementen
- **Bronnen**: wiki-links naar bronsamenvattingen
- **GGM-bron** (bij uitzonderlijke GGM-match): letterlijke GGM-definitie als blockquote, matchsterkte

Nazorg is gelijk aan BO-pagina's: `Wiki/index.md`, `Wiki/log.md` en het onderwerpoverzicht bijwerken.
