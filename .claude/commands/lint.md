Voer een consistentiecheck uit op de wiki. Scope: $ARGUMENTS (leeg = hele wiki, anders = opgegeven onderwerp).

**Voer uit op model: Haiku** (deze skill is read-only analyse, geen reasoning nodig).

### Bronnen & herleidbaarheid

- **BO zonder bronnen** — BO-pagina's zonder `## Bronnen`-sectie in de body. Elke BO moet traceerbaar zijn naar ten minste één bronsamenvatting.
- **Bronnen-sectie format** — elke bullet in `## Bronnen` moet een wiki-link zijn naar een bestaand bronsamenvatting- of source-bestand (bijv. `[[Wiki/Bronsamenvattingen/Economie/slug]]`). Geen alias — het pad maakt expliciet wat voor soort bestand het is.
- **Source zonder bronsamenvatting** — bronbestanden in `Sources/` zonder bronsamenvatting in `Wiki/Bronsamenvattingen/`.
- **Bronsamenvatting zonder bronnen** — bronsamenvattingen zonder `## Bronnen`-sectie met wiki-link naar het source-bestand.

### Domeinoverzichten & begrippentabel

- **Domeinoverzicht compleetheid** — begrippen in de tabel zonder BO-beoordeling (BO? kolom leeg). BO's in `Wiki/Bedrijfsobjecten/` die niet in een onderwerpoverzicht staan.
- **Tegenstrijdige definities** — definities die conflicteren tussen onderwerpoverzicht en BO-pagina.
- **Begrippentabel format** — onderwerpoverzichten moeten een begrippentabel hebben met kolommen: Begrip, Type, Omschrijving, BO?, Reden, Voorbeelden, GGM. Signaleer domeinpagina's die begrippen als bullet-lijst hebben i.p.v. tabel.
- **GGM-dekkingssecties verwijderd** — onderwerpoverzichten mogen geen `## GGM-entiteitendekking` of `## GGM-dekkingsanalyse` secties meer bevatten. GGM-dekking is verplaatst naar centrale pagina `[[Wiki/Analyses/ggm-dekking]]`.
- **Domein-afgetekend** — onderwerpoverzichten met `status: in-behandeling` zonder verantwoording, of `_count`-frontmatter die niet klopt met de inhoud.
- **Data-object kolom** — begrippentabellen zonder "Data-object" kolom; BO's met grondslag=ggm-entiteit maar Data-object=nee (inconsistent); Data-object=ja + GGM=nee zonder vermelding in openstaande acties.

### BO-frontmatter

- **Onvolledige frontmatter** — BO-pagina's zonder `grondslag`, of (bij grondslag=ggm-entiteit) zonder `ggm_entiteit` of `ggm_guid`. Let op: `ggm_entiteit` hoeft alleen gevuld bij grondslag `ggm-entiteit`; bij andere grondslagen is leeg correct.
- **Ontbrekende GGM-verrijkingsvelden** — BO-pagina's met grondslag `ggm-entiteit` die verrijkte velden missen (`ggm_guid`, `ggm_taakveld`, `ggm_diagram`, `ggm_gemma_naam`). Controleer tegen `ggm_parsed.json`: als het veld in de GGM-bron zelf leeg is, is leeg in de wiki correct (geen actie). Alleen vlaggen wanneer de bron data heeft die niet is overgenomen. Suggereer `python3 tools/enrich_bo_frontmatter.py` voor velden die wél beschikbaar zijn.
- **GGM-guid validatie** — als het geparsede XMI beschikbaar is, controleer of `ggm_guid` overeenkomt met een bestaande entiteit. Signaleer verwijderde of hernoemde entiteiten.
- **Frontmatter enum-validatie** — ongeldige waarden voor grondslag, archimate_type, ggm_uml_type. Geldige waarden (zie `templates/element.md`): grondslag ∈ {ggm-entiteit, ggm-afgeleid, procesobject, governance-object}; archimate_type ∈ {business-object, contract, product, business-actor, business-role}; ggm_uml_type ∈ {Class, Enumeration}. Element-pagina's hebben `type: element`; business-actor hoort in `Wiki/Actoren/`, business-role in `Wiki/Rollen/`, de overige in `Wiki/Bedrijfsobjecten/`.
- **`bo_relaties`-structuur** — BO-pagina's met `bo_relaties`-items die `type`, `richting` of `kardinaliteit` missen, of waarvan `bedrijfsobject:` geen wiki-link bevat.
- **`bo_definitie` geldig** — BO-pagina's zonder `bo_definitie`, met lege waarde, of met de placeholder `"gelijk aan GGM"`. Dit veld moet altijd een zelfstandige definitie op bedrijfsniveau bevatten (één zin). "Gelijk aan GGM" is geen definitie — herformuleer vanuit gemeentelijk perspectief.

### Subtypes en Specialisaties

- **Begrippentabel → BO** — begrippen met BO?=❌ waarvan de reden een subtype-patroon bevat (match op: "subtype van", "type van", "onderdeel van", "onderdeel/type van", "specialisatie van", "valt onder", "categorie van", "variant van") die niet voorkomen als `bo_subtypes` in de frontmatter van het genoemde parent-BO, en ook niet in een Subtypes- of Specialisaties-tabel in de body. Alleen signaleren wanneer het parent-BO in de wiki bestaat — verwijzingen naar externe concepten overslaan. Let op: "onderdeel van" vangt ook composities (component/fase), niet alleen subtypes; beoordeel handmatig of het daadwerkelijk een subtype betreft.
- **Frontmatter ↔ body subtypes** — BO's met **gevulde** `bo_subtypes` in frontmatter (niet `[]`) maar zonder `## Subtypes`-sectie in de body, of subtypes die in frontmatter staan maar niet in de body-lijst voorkomen, of subtypes die in de body-lijst staan maar niet in `bo_subtypes` in frontmatter. Lege placeholders (`gemma_subtypes: []`) overslaan — die vereisen geen body-sectie.
- **GGM-link compleetheid subtypes** — subtypes in `bo_subtypes` die een `ggm_entiteit` hebben maar geen `ggm_guid` of `ggm_attribuut` missen (verplicht per CLAUDE.md-regel "GGM-link verplicht").

### Generalisatie en Specialisaties (BO-hiërarchie)

- **Specialisaties ↔ generalisatie symmetrie** — BO's met `## Specialisaties`-sectie die children noemen: elk child-BO moet een `generalisatie`-relatie in frontmatter hebben die terugwijst naar het parent-BO (met `richting: naar-dit-BO`). Omgekeerd: BO's met `generalisatie`-relatie in frontmatter (`richting: naar-dit-BO`) moeten voorkomen in de `## Specialisaties`-tabel van het genoemde parent-BO.
- **Generalisatie-sectie consistentie** — BO's met `## Generalisatie`-sectie in de body: de hiërarchie moet wiki-links bevatten naar andere BO's die in de wiki bestaan. Signaleer dode links naar niet-bestaande BO's.
- **Verwarring Subtypes vs Specialisaties** — `## Specialisaties` is voor children die wél aparte BO's zijn (tabel met wiki-links). `## Subtypes` is voor children die géén apart BO zijn (lijst met vetgedrukte namen). Signaleer Specialisaties-secties die naar niet-bestaande BO's linken, of Subtypes-secties die naar bestaande BO's linken (die horen dan in Specialisaties).

### Analysepagina's

- **GGM-dekking tabel** — `Wiki/Analyses/ggm-dekking.md` moet een volledige tabel hebben met alle 48+ beleidsdomeinen uit `ggm_parsed.json`. Controleer of de BO-counts kloppen met ingetelde BO's in `Wiki/Bedrijfsobjecten/`. Signaleer ontbrekende rijen of tellingen die niet meer kloppen na recente ingests.
- **Analyse-links geldig** — links in analyses naar domeinen en BO's moeten naar bestaande pagina's verwijzen.

### Wiki-structuur & links

- **Wees-BO's** — BO-pagina's die door geen enkel onderwerpoverzicht worden gelinkt.
- **Geen losse begrippenpagina's** — controleer of `Wiki/Begrippen/` directory niet bestaat. Begrippen horen in de begrippentabel op de domeinpagina, niet als aparte pagina's.
- **Geen Wiki/Begrippen/ links** — zoek naar `[[Wiki/Begrippen/` in alle wiki-bestanden. Deze links zijn verouderd; begrippen staan op domeinpagina's.
- **Wiki-link alias verplicht** — alle `[[Wiki/...]]` links (met pad ≥2 segmenten) moeten een alias hebben. In tabellen: `[[pad\|alias]]` (escaped pipe, anders breekt de tabel). Buiten tabellen: `[[pad|alias]]` (gewone pipe). Signaleer: (a) bare `[[Wiki/lang/pad]]` zonder alias, (b) onescaped `|` in `[[...|...]]` binnen tabelrijen, (c) kapotte syntax zoals `[[pad]\|alias]]`. **Uitzondering:** links in `## Bronnen`-secties hebben bewust geen alias.

### GGM-duplicaten

- **Duplicaat-frontmatter compleetheid** — BO's met **gevulde** `ggm_duplicaat_entiteiten` in frontmatter (niet `[]`): elk item moet `entiteit`, `guid`, `beleidsdomein` en `taakveld` bevatten. `afwijkende_attributen` mag leeg zijn. Lege placeholders (`ggm_duplicaat_entiteiten: []`) overslaan.
- **Duplicaat-body consistentie** — BO's met **gevulde** `ggm_duplicaat_entiteiten` (niet `[]`) moeten een `## GGM-duplicaten` sectie in de body hebben, en omgekeerd. Lege lijsten negeren.
- **Duplicaat-terugmelding** — BO's met **gevulde** `ggm_duplicaat_entiteiten` (niet `[]`) die niet in `Wiki/Analyses/ggm-terugmeldingen.md` staan als type `duplicaat`.
- **Homoniem-terugmelding** — `## GGM-duplicaten` secties die homoniemen vermelden: controleer of het homoniem in `Wiki/Analyses/ggm-terugmeldingen.md` staat als type `homoniem`.

### Synoniemen en homoniemen

- **Synoniemen-compleetheid** — BO's met **gevulde** `bo_synoniemen` in frontmatter (niet `[]`): elk item moet `naam` en `context` bevatten.
- **Homoniemen-compleetheid** — BO's met **gevulde** `bo_homoniemen` in frontmatter (niet `[]`): elk item moet `bedrijfsobject`, `ggm_entiteit`, `ggm_guid`, `ggm_beleidsdomein` en `toelichting` bevatten.
- **Homoniemen-symmetrie** — als BO-A in `bo_homoniemen` naar BO-B verwijst, moet BO-B ook in `bo_homoniemen` naar BO-A verwijzen. Signaleer eenzijdige verwijzingen.
- **Homoniemen ↔ GGM-duplicaten consistentie** — bo_homoniemen in frontmatter moeten ook in de `## GGM-duplicaten` body-sectie vermeld worden als homoniem-waarschuwing.
- **Naamkeuze-consistentie** — BO's waarvan `naam` ≠ `ggm_entiteit` door homoniem-disambiguatie (zie `templates/element.md`) missen een `## Naamkeuze`-sectie. Niet van toepassing bij generalisatie/specialisatie (matchsterkte `sterk`/`partieel`) — dat hoort bij `## GGM-bron`, niet bij Naamkeuze.
- **Duplicaat-bestandsnamen** — twee of meer BO-bestanden met dezelfde bestandsnaam in verschillende domeinfolders. Dit is een potentieel homoniem dat nog niet gedocumenteerd is.

### Inhoudelijke consistentie

- **Terugmeldingen-consistentie** — BO's met "⚠️ ter discussie" of afwijking in body die niet in `Wiki/Analyses/ggm-terugmeldingen.md` staan, en omgekeerd (terugmeldingen die naar niet-bestaande BO verwijzen).
- **Anti-patroon registr\*** — begrippentabel "Reden" of BO-body die "registreerbaar"/"registratieobject" als afwijsgrond of motivatie gebruikt. De 6 BO-criteria zijn de enige toets.

Rapporteer per check: aantal bevindingen + lijst. Sorteer op ernst (herleidbaarheid > ontbrekende data > inconsistenties > suggesties).
