Maak een GGM-dekkingsanalyse (centrale pagina): $ARGUMENTS

**Voer uit op model: Haiku** (deze skill is read-only analyse, geen reasoning nodig).

Doel: inventariseer voor alle GGM-beleidsdomeinen welke entiteiten wél/niet een BO hebben, en waar bronnen beschikbaar zijn. 

**Waarom centraal, niet per domein:** GGM-beleidsdomeinen en wiki-domeinen lopen niet 1-op-1. Een wiki-domein kan meerdere beleidsdomeinen raken; een beleidsdomein kan relevant zijn voor meerdere wiki-domeinen. Dit overzicht werkt vanuit de GGM-structuur (taakveld → beleidsdomein) en maakt per beleidsdomein zichtbaar:
- Zijn er bronnen beschikbaar om entiteiten te beoordelen?
- Hoeveel entiteiten zijn al beoordeeld (BO of niet-BO)?
- Welke beleidsdomeinen hebben nog geen bronnen (= waar moeten documenten gezocht worden)?

Input: "dekking" (volledige analyse van alle beleidsdomeinen) of "{domein-naam}" (analyse voor domeinen die dit raken).

Stappen:
1. Lees het geparsede GGM uit `Sources/GGM-repository/ggm_parsed.json`.
2. Lees alle BO-pagina's uit `Wiki/Bedrijfsobjecten/` en extract `ggm_guid`, `ggm_entiteit`, `beleidsdomein`, `grondslag` uit frontmatter.
3. Lees alle bronsamenvattingen uit `Wiki/Bronsamenvattingen/` en bepaal per wiki-domein welke beleidsdomeinen geraakt zijn.
4. Bouw per GGM-beleidsdomein:
   - Totaal entiteiten (uit JSON)
   - BO-count (BO-pagina's met `ggm_guid`-match)
   - Niet-BO-count (GGM-entiteiten zonder BO-match, beoordeeld o.b.v. bronsamenvatting)
   - Niet-beoordeeld-count (GGM-entiteiten zonder bron)
   - Wiki-domein(en) die dit beleidsdomein raken (met links)
   - Bronnenaantal (verwerkte bronsamenvattingen die dit domein raken)
5. Update `Wiki/Analyses/ggm-dekking.md` met de tabel.
6. Voeg GGM-hiaten toe aan `Wiki/Analyses/ggm-terugmeldingen.md` (data-objecten zonder GGM-match).
7. Onder de tabel: samenvattende statistieken en sectie "Beleidsdomeinen zonder bronnen".
8. Voeg entry toe aan `Wiki/log.md`.

Coverage telt en signaleert; het beoordeelt niet zelf of een entiteit een BO moet worden. Voor beoordeling: verwijs door naar `/assess-bo`.
