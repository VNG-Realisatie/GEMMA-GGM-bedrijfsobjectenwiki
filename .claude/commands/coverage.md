Maak een GGM-dekkingsanalyse (centrale pagina): $ARGUMENTS

**Voer uit op model: Haiku** (deze skill is read-only analyse, geen reasoning nodig).

Doel: inventariseer voor alle GGM-beleidsdomeinen welke entiteiten wél/niet een BO hebben, en waar bronnen beschikbaar zijn. 

**Waarom centraal, niet per onderwerp:** GGM-beleidsdomeinen en wiki-domeinen lopen niet 1-op-1. Een wiki-onderwerp kan meerdere beleidsdomeinen raken; een beleidsdomein kan relevant zijn voor meerdere wiki-domeinen. Dit overzicht werkt vanuit de GGM-structuur (taakveld → beleidsdomein) en maakt per beleidsdomein zichtbaar:
- Zijn er bronnen beschikbaar om entiteiten te beoordelen?
- Hoeveel entiteiten zijn al beoordeeld (BO of niet-BO)?
- Welke beleidsdomeinen hebben nog geen bronnen (= waar moeten documenten gezocht worden)?

Input: "dekking" (volledige analyse van alle beleidsdomeinen) of "{onderwerp-naam}" (analyse voor domeinen die dit raken).

Stappen:
1. Lees het geparsede GGM uit `Sources/GGM-repository/ggm_parsed.json`.
2. Lees alle BO-pagina's uit `Wiki/Bedrijfsobjecten/` en extract `ggm_guid`, `ggm_entiteit`, `beleidsdomein`, `grondslag` uit frontmatter.
3. Lees alle bronsamenvattingen uit `Wiki/Bronsamenvattingen/` en bepaal per wiki-onderwerp welke beleidsdomeinen geraakt zijn.
4. Genereer samenvattende statistieken: totaal entiteiten, BO-count, niet-BO-count, niet-beoordeeld-count.
5. Sectie "Beleidsdomeinen zonder bronnen": lijst van beleidsdomeinen die nog geen bronnen hebben.
6. **Onderste sectie (als laatste):** Tabel "GGM-entiteitendekking per beleidsdomein", opgesplitst per taakveld met headers:

   **Per taakveld-header:**
   | beleidsdomein | onderwerp (aantal bronnen) | aantal entiteiten | Bedrijfsobject | Geen bedrijfsobject | Niet beoordeeld |
   |---|---|---|---|---|---|
   
   Kolom-richtlijnen:
   - **beleidsdomein**: naam van het GGM-beleidsdomein
   - **onderwerp (aantal bronnen)**: wiki-onderwerp(en) die dit raken, met link [[Wiki/...]], in haakjes: aantal bronsamenvattingen
   - **aantal entiteiten**: totaal GGM-entiteiten in dit beleidsdomein
   - **Bedrijfsobject**: GGM-entiteitnamen (komma-gescheiden) die als BO zijn vastgelegd
   - **Geen bedrijfsobject**: GGM-entiteitnamen (komma-gescheiden) die zijn beoordeeld maar geen BO werden
   - **Niet beoordeeld**: GGM-entiteitnamen (komma-gescheiden), elk gevolgd door reden in haakjes, bijv. "Stoornis (geen bron)" of "Woning (buiten scope)"

7. Update `Wiki/Analyses/ggm-dekking.md` met statistieken, hiaten-sectie, en onderste dekkingstabel.
8. Voeg GGM-hiaten toe aan `Wiki/Analyses/ggm-terugmeldingen.md` (data-objecten zonder GGM-match).
9. Voeg entry toe aan `Wiki/log.md`.

Coverage telt en signaleert; het beoordeelt niet zelf of een entiteit een BO moet worden. Voor beoordeling: verwijs door naar `/assess-bo`.
