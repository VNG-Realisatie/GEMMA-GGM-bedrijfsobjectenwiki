Voer een consistentiecheck uit op de wiki. Scope: $ARGUMENTS (leeg = hele wiki, anders = opgegeven domein).

Checks:
1. **Herleidbaarheid** — BO-pagina's zonder `bronnen` in frontmatter. Elke BO moet traceerbaar zijn naar ten minste één bronsamenvatting.
2. **Onvolledige BO-frontmatter** — BO-pagina's zonder `grondslag`, of (bij grondslag=ggm-entiteit) zonder `ggm_entiteit` of `ggm_guid`. Let op: `ggm_entiteit` hoeft alleen gevuld bij grondslag `ggm-entiteit`; bij andere grondslagen is leeg correct.
3. **Ontbrekende GGM-velden** — BO-pagina's met grondslag `ggm-entiteit` die verrijkte velden missen (`ggm_guid`, `ggm_taakveld`, `ggm_diagram`, `ggm_gemma_naam`). Suggereer `python3 tools/enrich_bo_frontmatter.py`.
4. **GGM-guid validatie** — als het geparsede XMI beschikbaar is, controleer of `ggm_guid` overeenkomt met een bestaande entiteit. Signaleer verwijderde of hernoemde entiteiten.
5. **Domeinoverzicht compleetheid** — begrippen in de tabel zonder BO-beoordeling (BO? kolom leeg). BO's in `Wiki/Bedrijfsobjecten/` die niet in een domeinoverzicht staan.
6. **Bronsamenvattingen** — bronbestanden in `Sources/` zonder bronsamenvatting in `Wiki/Bronsamenvattingen/`.
7. **Wees-BO's** — BO-pagina's die door geen enkel domeinoverzicht worden gelinkt.
8. **Tegenstrijdigheden** — definities die conflicteren tussen domeinoverzicht en BO-pagina.
9. **Frontmatter enum-validatie** — ongeldige waarden voor grondslag, archimate_type, ggm_uml_type. Geldige waarden (zie `templates/bedrijfsobject.md`): grondslag ∈ {ggm-entiteit, ggm-afgeleid, procesobject, governance-object}; archimate_type ∈ {business-object, contract, product}; ggm_uml_type ∈ {Class, Enumeration}.
10. **Geen losse begrippenpagina's** — controleer of `Wiki/Begrippen/` directory niet bestaat. Begrippen horen in de begrippentabel op de domeinpagina, niet als aparte pagina's.
11. **Begrippentabel format** — domeinoverzichten moeten een begrippentabel hebben met kolommen: Begrip, Type, Omschrijving, BO?, Reden, Voorbeelden, GGM. Signaleer domeinpagina's die begrippen als bullet-lijst hebben i.p.v. tabel.
12. **Geen Wiki/Begrippen/ links** — zoek naar `[[Wiki/Begrippen/` in alle wiki-bestanden. Deze links zijn verouderd; begrippen staan op domeinpagina's.
13. **Ontbrekende subtypes** — drie deelchecks:
    - **13a. Begrippentabel → BO:** begrippen met BO?=❌ waarvan de reden een subtype-patroon bevat (match op: "subtype van", "type van", "onderdeel van", "onderdeel/type van", "specialisatie van", "valt onder", "categorie van", "variant van") die niet voorkomen als `gemma_subtypes` in de frontmatter van het genoemde parent-BO, en ook niet in een Specialisaties-tabel in de body. Signaleer apart als het parent-BO niet in de wiki bestaat.
    - **13b. Frontmatter ↔ body:** BO's met `gemma_subtypes` in frontmatter maar zonder `## Specialisaties`-sectie in de body, of subtypes die in frontmatter staan maar niet in de body-tabel voorkomen, of subtypes die in de body-tabel staan maar niet in `gemma_subtypes` in frontmatter.
    - **13c. GGM-link compleetheid:** subtypes in `gemma_subtypes` die een `ggm_entiteit` hebben maar geen `ggm_guid` of `ggm_attribuut` missen (verplicht per CLAUDE.md-regel "GGM-link verplicht").

14. **`bron:`-link in bronsamenvattingen** — bronsamenvattingen waarvan `bron:` een `[[wiki-link]]` is i.p.v. een markdown-link `[tekst](pad)`. Het `bron:` veld verwijst naar een source-bestand, geen wiki-pagina.
15. **Wiki-links naar Sources/** — `[[...]]` die naar een `Sources/`-pad wijst. Sources-verwijzingen gebruiken markdown-links, geen wiki-links.
16. **`relaties`-frontmatter structuur** — BO-pagina's met `relaties`-items die `type`, `richting` of `kardinaliteit` missen, of waarvan `bedrijfsobject:` geen wiki-link bevat.
17. **`gemma_definitie` geldig** — BO-pagina's zonder `gemma_definitie`, met lege waarde, of met de placeholder `"gelijk aan GGM"`. Dit veld moet altijd een zelfstandige definitie op bedrijfsniveau bevatten (één zin). "Gelijk aan GGM" is geen definitie — herformuleer vanuit gemeentelijk perspectief.
18. **Terugmeldingen-consistentie** — BO's met "⚠️ ter discussie" of afwijking in body die niet in `Wiki/Analyses/ggm-terugmeldingen.md` staan, en omgekeerd (terugmeldingen die naar niet-bestaande BO verwijzen).
19. **GGM-entiteitendekkingstabel** — domeinoverzichten zonder GGM-entiteitendekkingstabel, of waarvan de tellingen niet kloppen met de begrippentabel.
20. **Domein-afgetekend** — domeinoverzichten met `status: in-behandeling` zonder verantwoording, of `_count`-frontmatter die niet klopt met de inhoud.
21. **Wiki-link alias verplicht** — alle `[[Wiki/...]]` links (met pad ≥2 segmenten) moeten een alias hebben. In tabellen: `[[pad\|alias]]` (escaped pipe, anders breekt de tabel). Buiten tabellen: `[[pad|alias]]` (gewone pipe). Signaleer: (a) bare `[[Wiki/lang/pad]]` zonder alias, (b) onescaped `|` in `[[...|...]]` binnen tabelrijen, (c) kapotte syntax zoals `[[pad]\|alias]]`.
22. **Anti-patroon registr\*** — begrippentabel "Reden" of BO-body die "registreerbaar"/"registratieobject" als afwijsgrond of motivatie gebruikt. De 6 BO-criteria zijn de enige toets.
23. **Data-object kolom** — begrippentabellen zonder "Data-object" kolom; BO's met grondslag=ggm-entiteit maar Data-object=nee (inconsistent); Data-object=ja + GGM=nee zonder vermelding in openstaande acties.

Rapporteer per check: aantal bevindingen + lijst. Sorteer op ernst (herleidbaarheid > ontbrekende data > inconsistenties > suggesties).
