# lint

**Doel:** consistentiecheck van de wiki tegen templates en werkafspraken; rapporteert bevindingen met voorgestelde fixes.
**Aanbevolen model:** licht (read-only analyse, geen redeneerwerk)
**Parameters:** {{scope}} — onderwerp; optioneel (leeg = hele wiki).
**Benodigde context:** [../templates/](../templates/), [../context/conventies.md](../context/conventies.md), de wiki-pagina's in scope, `Sources/GGM-repository/ggm_parsed.json`.
**Verwachte uitvoer:** per check het aantal bevindingen plus een genummerde lijst met voorgestelde fixes, gesorteerd op ernst (herleidbaarheid > ontbrekende data > inconsistenties > suggesties).

## Prompt

Voer een consistentiecheck uit op de wiki. Scope: {{scope}} (leeg = hele wiki).

### Bronnen & herleidbaarheid

- **BO zonder bronnen** — elementpagina's zonder `## Bronnen`-sectie in de body.
- **Bronnen-sectieformat** — elke bullet in `## Bronnen` is een link (zonder alias) naar een bestaand bronsamenvattings- of bronbestand.
- **Bron zonder bronsamenvatting** — bronbestanden in `Sources/` zonder samenvatting in `Wiki/Bronsamenvattingen/`.
- **Bronsamenvatting zonder bronverwijzing** — samenvattingen zonder `## Bronnen`-sectie naar het bronbestand.

### Onderwerpoverzichten & begrippentabel

- **Compleetheid** — begrippen zonder BO-beoordeling; BO's die in geen enkel onderwerpoverzicht staan.
- **Tegenstrijdige definities** — conflicten tussen onderwerpoverzicht en elementpagina.
- **Tabelformat** — begrippentabel met de kolommen Begrip, Begripstype, Omschrijving, BO?, Data-object, Reden, Voorbeelden, GGM (geen bullet-lijsten).
- **Geen dekkingssecties** — onderwerpoverzichten bevatten geen GGM-dekkingssecties meer; dekking staat centraal in `Wiki/Analyses/`.
- **Aftekening** — `status: in-behandeling` zonder verantwoording; `_count`-frontmatter die niet klopt met de inhoud.
- **Data-objectkolom** — ontbrekende kolom; grondslag ggm-entiteit met Data-object=nee (inconsistent); Data-object=ja + GGM=nee zonder vermelding bij openstaande acties.

### Element-frontmatter

- **Onvolledig** — geen `grondslag`, of (bij grondslag ggm-entiteit) geen `ggm_entiteit`/`ggm_guid`. Bij andere grondslagen is leeg correct.
- **Ontbrekende GGM-verrijking** — velden (`ggm_guid`, `ggm_taakveld`, `ggm_diagram`, `ggm_gemma_naam`) leeg terwijl `ggm_parsed.json` wél data heeft; is de bron zelf leeg, dan is leeg correct.
- **GUID-validatie** — `ggm_guid` moet bestaan in het geparsede XMI; signaleer verwijderde of hernoemde entiteiten.
- **Enum-validatie** — grondslag ∈ {ggm-entiteit, ggm-afgeleid, procesobject, governance-object}; archimate_type ∈ {business-object, contract, product, business-actor, business-role}; ggm_uml_type ∈ {Class, Enumeration}; `type: element`. business-actor hoort in `Wiki/Actoren/`, business-role in `Wiki/Rollen/`, de rest in `Wiki/Bedrijfsobjecten/`.
- **`bo_relaties`-structuur** — items zonder `type`, `richting` of `kardinaliteit`, of met een ongequote `bedrijfsobject:`-wiki-link (parseert als geneste lijst — altijd fixen, dit is een correctheidsbug).
- **`bo_definitie` geldig** — niet leeg, geen placeholder als "gelijk aan GGM"; altijd een zelfstandige definitie op bedrijfsniveau.
- **Frontmatter-stijl** — lege waarden blanco (niet `""`/`''`/`~`); dubbele quotes waar voorgeschreven; veldnaam `onderwerp:` (niet `domein:`). Fix wiki-breed met `python3 tools/migrate_frontmatter_style.py`.

### Subtypes, specialisaties en generalisatie

- **Begrippentabel → BO** — begrippen met BO?=❌ en een subtype-achtige reden ("subtype van", "onderdeel van", "valt onder", …) die niet als subtype bij het genoemde parent-BO staan (frontmatter of body). Alleen signaleren als het parent-BO bestaat; "onderdeel van" kan ook een compositie zijn — handmatig beoordelen.
- **Frontmatter ↔ body** — gevulde `bo_subtypes` zonder `## Subtypes`-sectie of andersom; lijsten die niet overeenkomen. Lege lijsten (`[]`) overslaan.
- **GGM-link subtypes** — subtypes met `ggm_entiteit` maar zonder `ggm_guid`/`ggm_attribuut`.
- **Specialisaties ↔ generalisatie-symmetrie** — elk child in een `## Specialisaties`-tabel heeft een terugwijzende `generalisatie`-relatie (`richting: naar-dit-BO`), en andersom.
- **Subtypes vs. specialisaties** — Specialisaties-secties die naar niet-bestaande BO's linken; Subtypes-secties die naar bestaande BO's linken (horen dan in Specialisaties).
- **Generalisatie-secties** — dode links naar niet-bestaande BO's.

### Naamconflicten

- **Duplicaat-frontmatter** — gevulde `ggm_duplicaat_entiteiten`: elk item compleet (`entiteit`, `guid`, `beleidsdomein`, `taakveld`); bijbehorende `## GGM-duplicaten`-sectie aanwezig en andersom; terugmelding type `duplicaat` geregistreerd.
- **Synoniemen/homoniemen compleet** — gevulde `bo_synoniemen`-items hebben `naam` + `context`; gevulde `bo_homoniemen`-items hebben `bedrijfsobject`, `ggm_entiteit`, `ggm_guid`, `ggm_beleidsdomein`, `toelichting`.
- **Homoniem-symmetrie** — verwijst BO-A naar BO-B, dan ook andersom; homoniemen ook vermeld in de `## GGM-duplicaten`-sectie en teruggemeld als type `homoniem`.
- **Naamkeuze** — `naam` ≠ `ggm_entiteit` door disambiguatie zonder `## Naamkeuze`-sectie (niet van toepassing bij generalisatie/specialisatie-afwijkingen).
- **Duplicaat-bestandsnamen** — gelijknamige bestanden in verschillende domeinmappen: potentieel ongedocumenteerd homoniem.

### Structuur, links en inhoud

- **Wees-BO's** — elementpagina's die door geen enkel onderwerpoverzicht worden gelinkt.
- **Geen losse begrippenpagina's** — een `Wiki/Begrippen/`-map of links daarnaartoe zijn verouderd; begrippen staan in de begrippentabellen.
- **Linkconventie** — conform [../context/conventies.md](../context/conventies.md): padlinks met alias (in tabellen escaped pipe), kapotte linksyntax, uitzondering voor `## Bronnen`-secties.
- **Terugmeldingen-consistentie** — pagina's met `⚠️ ter discussie` of gedocumenteerde afwijking zonder terugmelding, en terugmeldingen die naar niet-bestaande pagina's verwijzen.
- **Anti-patroon registr\*** — "registreerbaar"/"registratieobject" als afwijsgrond of motivatie; de 6 BO-criteria zijn de enige toets.
- **Analyse-links** — links in analyses verwijzen naar bestaande pagina's; de centrale dekkingsrapportage dekt alle beleidsdomeinen en de tellingen kloppen.

## Voorbeeld

> Voer een consistentiecheck uit op de wiki. Scope: belastingen
