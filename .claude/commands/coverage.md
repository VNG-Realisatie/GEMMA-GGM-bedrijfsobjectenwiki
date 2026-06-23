Maak een GGM-dekkingsanalyse (centrale pagina): $ARGUMENTS

**Voer uit op model: Haiku** (deze skill is read-only analyse, geen reasoning nodig).

Doel: inventariseer voor alle GGM-beleidsdomeinen welke entiteiten wél/niet een BO hebben, en waar bronnen beschikbaar zijn. 

**Waarom centraal, niet per onderwerp:** GGM-beleidsdomeinen en wiki-domeinen lopen niet 1-op-1. Een wiki-onderwerp kan meerdere beleidsdomeinen raken; een beleidsdomein kan relevant zijn voor meerdere wiki-domeinen. Dit overzicht werkt vanuit de GGM-structuur (taakveld → beleidsdomein) en maakt per beleidsdomein zichtbaar:
- Zijn er bronnen beschikbaar om entiteiten te beoordelen?
- Hoeveel entiteiten zijn al beoordeeld (BO of niet-BO)?
- Welke beleidsdomeinen hebben nog geen bronnen (= waar moeten documenten gezocht worden)?

Input: "dekking" (volledige analyse van alle beleidsdomeinen) of "{onderwerp-naam}" (analyse voor domeinen die dit raken).

**Uitvoering:** draai `python3 tools/coverage_analysis.py`. Het script leest GGM, BO-pagina's, bronsamenvattingen en GGM/onderwerpoverzicht-pagina's, en genereert `Wiki/Analyses/ggm-dekking.md`.

Na het draaien van het script:
1. Voeg entry toe aan `Wiki/log.md`.
2. Verifieer output in `Wiki/Analyses/ggm-dekking.md`.

Coverage telt en signaleert; het beoordeelt niet zelf of een entiteit een BO moet worden. Voor beoordeling: verwijs door naar `/assess-bo`.
