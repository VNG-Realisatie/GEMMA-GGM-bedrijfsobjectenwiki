Voer een consistentiecheck uit op de wiki. Scope: $ARGUMENTS (leeg = hele wiki, anders = opgegeven domein).

**Voer uit op model: Haiku** (deze skill is read-only analyse, geen reasoning nodig).

### Bronnen & herleidbaarheid

- **BO zonder bronnen** — BO-pagina's zonder `## Bronnen`-sectie in de body. Elke BO moet traceerbaar zijn naar ten minste één bronsamenvatting.
- **Bronnen-sectie format** — elke bullet in `## Bronnen` moet een wiki-link zijn naar een bestaand bronsamenvatting- of source-bestand (bijv. `[[Wiki/Bronsamenvattingen/Economie/slug]]`). Geen alias — het pad maakt expliciet wat voor soort bestand het is.
- **Source zonder bronsamenvatting** — bronbestanden in `Sources/` zonder bronsamenvatting in `Wiki/Bronsamenvattingen/`.
- **Bronsamenvatting zonder bronnen** — bronsamenvattingen zonder `## Bronnen`-sectie met wiki-link naar het source-bestand.

### Domeinoverzichten & begrippentabel

- **Domeinoverzicht compleetheid** — begrippen in de tabel zonder BO-beoordeling (BO? kolom leeg). BO's in `Wiki/Bedrijfsobjecten/` die niet in een domeinoverzicht staan.
- **Tegenstrijdige definities** — definities die conflicteren tussen domeinoverzicht en BO-pagina.
- **Begrippentabel format** — domeinoverzichten moeten een begrippentabel hebben met kolommen: Begrip, Type, Omschrijving, BO?, Reden, Voorbeelden, GGM. Signaleer domeinpagina's die begrippen als bullet-lijst hebben i.p.v. tabel.
- **GGM-dekkingssecties verwijderd** — domeinoverzichten mogen geen `## GGM-entiteitendekking` of `## GGM-dekkingsanalyse` secties meer bevatten. GGM-dekking is verplaatst naar centrale pagina `[[Wiki/Analyses/ggm-dekking]]`.
- **Domein-afgetekend** — domeinoverzichten met `status: in-behandeling` zonder verantwoording, of `_count`-frontmatter die niet klopt met de inhoud.
- **Data-object kolom** — begrippentabellen zonder "Data-object" kolom; BO's met grondslag=ggm-entiteit maar Data-object=nee (inconsistent); Data-object=ja + GGM=nee zonder vermelding in openstaande acties.

### BO-frontmatter

- **Onvolledige frontmatter** — BO-pagina's zonder `grondslag`, of (bij grondslag=ggm-entiteit) zonder `ggm_entiteit` of `ggm_guid`. Let op: `ggm_entiteit` hoeft alleen gevuld bij grondslag `ggm-entiteit`; bij andere grondslagen is leeg correct.
- **Ontbrekende GGM-verrijkingsvelden** — BO-pagina's met grondslag `ggm-entiteit` die verrijkte velden missen (`ggm_guid`, `ggm_taakveld`, `ggm_diagram`, `ggm_gemma_naam`). Controleer tegen `ggm_parsed.json`: als het veld in de GGM-bron zelf leeg is, is leeg in de wiki correct (geen actie). Alleen vlaggen wanneer de bron data heeft die niet is overgenomen. Suggereer `python3 tools/enrich_bo_frontmatter.py` voor velden die wél beschikbaar zijn.
- **GGM-guid validatie** — als het geparsede XMI beschikbaar is, controleer of `ggm_guid` overeenkomt met een bestaande entiteit. Signaleer verwijderde of hernoemde entiteiten.
- **Frontmatter enum-validatie** — ongeldige waarden voor grondslag, archimate_type, ggm_uml_type. Geldige waarden (zie `templates/bedrijfsobject.md`): grondslag ∈ {ggm-entiteit, ggm-afgeleid, procesobject, governance-object}; archimate_type ∈ {business-object, contract, product}; ggm_uml_type ∈ {Class, Enumeration}.
- **`relaties`-structuur** — BO-pagina's met `relaties`-items die `type`, `richting` of `kardinaliteit` missen, of waarvan `bedrijfsobject:` geen wiki-link bevat.
- **`gemma_definitie` geldig** — BO-pagina's zonder `gemma_definitie`, met lege waarde, of met de placeholder `"gelijk aan GGM"`. Dit veld moet altijd een zelfstandige definitie op bedrijfsniveau bevatten (één zin). "Gelijk aan GGM" is geen definitie — herformuleer vanuit gemeentelijk perspectief.

### Subtypes

- **Begrippentabel → BO** — begrippen met BO?=❌ waarvan de reden een subtype-patroon bevat (match op: "subtype van", "type van", "onderdeel van", "onderdeel/type van", "specialisatie van", "valt onder", "categorie van", "variant van") die niet voorkomen als `gemma_subtypes` in de frontmatter van het genoemde parent-BO, en ook niet in een Specialisaties-tabel in de body. Alleen signaleren wanneer het parent-BO in de wiki bestaat — verwijzingen naar externe concepten overslaan. Let op: "onderdeel van" vangt ook composities (component/fase), niet alleen subtypes; beoordeel handmatig of het daadwerkelijk een subtype betreft.
- **Frontmatter ↔ body** — BO's met `gemma_subtypes` in frontmatter maar zonder `## Specialisaties`-sectie in de body, of subtypes die in frontmatter staan maar niet in de body-tabel voorkomen, of subtypes die in de body-tabel staan maar niet in `gemma_subtypes` in frontmatter.
- **GGM-link compleetheid subtypes** — subtypes in `gemma_subtypes` die een `ggm_entiteit` hebben maar geen `ggm_guid` of `ggm_attribuut` missen (verplicht per CLAUDE.md-regel "GGM-link verplicht").

### Analysepagina's

- **GGM-dekking tabel** — `Wiki/Analyses/ggm-dekking.md` moet een volledige tabel hebben met alle 48+ beleidsdomeinen uit `ggm_parsed.json`. Controleer of de BO-counts kloppen met ingetelde BO's in `Wiki/Bedrijfsobjecten/`. Signaleer ontbrekende rijen of tellingen die niet meer kloppen na recente ingests.
- **Analyse-links geldig** — links in analyses naar domeinen en BO's moeten naar bestaande pagina's verwijzen.

### Wiki-structuur & links

- **Wees-BO's** — BO-pagina's die door geen enkel domeinoverzicht worden gelinkt.
- **Geen losse begrippenpagina's** — controleer of `Wiki/Begrippen/` directory niet bestaat. Begrippen horen in de begrippentabel op de domeinpagina, niet als aparte pagina's.
- **Geen Wiki/Begrippen/ links** — zoek naar `[[Wiki/Begrippen/` in alle wiki-bestanden. Deze links zijn verouderd; begrippen staan op domeinpagina's.
- **Wiki-link alias verplicht** — alle `[[Wiki/...]]` links (met pad ≥2 segmenten) moeten een alias hebben. In tabellen: `[[pad\|alias]]` (escaped pipe, anders breekt de tabel). Buiten tabellen: `[[pad|alias]]` (gewone pipe). Signaleer: (a) bare `[[Wiki/lang/pad]]` zonder alias, (b) onescaped `|` in `[[...|...]]` binnen tabelrijen, (c) kapotte syntax zoals `[[pad]\|alias]]`. **Uitzondering:** links in `## Bronnen`-secties hebben bewust geen alias.

### Inhoudelijke consistentie

- **Terugmeldingen-consistentie** — BO's met "⚠️ ter discussie" of afwijking in body die niet in `Wiki/Analyses/ggm-terugmeldingen.md` staan, en omgekeerd (terugmeldingen die naar niet-bestaande BO verwijzen).
- **Anti-patroon registr\*** — begrippentabel "Reden" of BO-body die "registreerbaar"/"registratieobject" als afwijsgrond of motivatie gebruikt. De 6 BO-criteria zijn de enige toets.

Rapporteer per check: aantal bevindingen + lijst. Sorteer op ernst (herleidbaarheid > ontbrekende data > inconsistenties > suggesties).
