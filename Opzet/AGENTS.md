# AGENTS.md — GEMMA Bedrijfsobjecten Wiki

Instructies voor elke AI-assistent die in dit project werkt.

## Wat dit project is

Werkinstrument van het GEMMA-team (VNG) voor het onderbouwd opbouwen van het GEMMA-bedrijfsobjectenmodel. Vanuit gemeentelijke beleidsbronnen en het GGM (Gemeentelijk Gegevensmodel) worden begrippen beoordeeld aan vaste criteria en vastgelegd als bedrijfsobjecten (BO's), actoren en rollen — elk met volledige onderbouwing. Details: [context/project.md](context/project.md).

## Kernregels (altijd van toepassing)

1. **Bronnen zijn immutabel** — de inhoud van bestanden in `Sources/` wijzig je nooit; verplaatsen en frontmatter aanvullen bij intake mag wel.
2. **Alle afgeleide kennis gaat naar `Wiki/`** — strikte scheiding tussen bron en wiki.
3. **Herleidbaarheid** — elk BO traceerbaar naar bronsamenvattingen; elke feitelijke claim naar een bron. Onzeker? Markeer `ter discussie`, gok niet.
4. **Bespreek eerst op bronniveau** — kernpunten van een bron bespreken vóór je schrijft; begrippen die aan de autonomievoorwaarden voldoen handel je daarna zelfstandig af, twijfelgevallen leg je per stuk voor.
5. **Incrementeel** — bestaande pagina's bijwerken, geen duplicaten; na elke wijziging `Wiki/index.md` en `Wiki/log.md` actueel houden.
6. **Gemeentelijk perspectief** — BO's beschrijven wat de gemeente ziet, doet en registreert; externe actoren kunnen wél een actor-/rolpagina krijgen, maar geen BO.

Volledige regels: [context/regels.md](context/regels.md). Werkinstructies voor de LLM: [context/ai-richtlijnen.md](context/ai-richtlijnen.md).

## Waar staat wat

- Projectdoel en werkwijze: [context/project.md](context/project.md)
- Mappenstructuur van het project: [context/architectuur.md](context/architectuur.md)
- Regels voor bronnen: [context/bronnen.md](context/bronnen.md)
- Paginatypes en hun templates: [context/paginatypes.md](context/paginatypes.md)
- Naamgeving, taal en links: [context/conventies.md](context/conventies.md)
- Definitie- en citatieregels: [context/schrijfregels.md](context/schrijfregels.md)

## Werken

- Een taak uitvoeren: gebruik de bijbehorende prompt uit [prompts/](prompts/) (elke prompt vermeldt doel, parameters en benodigde context).
- Een proces begrijpen: [workflows/](workflows/) — ingest, vragen beantwoorden, lint, onderhoud.
- Een vraag beantwoorden: lees eerst `Wiki/index.md`, synthetiseer uit bestaande pagina's, citeer ze, en schrijf waardevolle antwoorden terug naar de wiki ([workflows/vragen-beantwoorden.md](workflows/vragen-beantwoorden.md)).
- Pagina's aanmaken: volg de templates in [templates/](templates/).
- Scripts draaien: zie [tools/README.md](tools/README.md).
