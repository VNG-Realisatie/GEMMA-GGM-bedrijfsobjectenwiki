# AGENTS.md — GEMMA ArchiMate-elementafleiding (OpzetII)

Instructies voor elke AI-assistent die onder de OpzetII-werkwijze werkt.

## Wat dit is

Analyse- en curatieomgeving van het GEMMA-team (VNG): uit beleidsbronnen worden kandidaten voor GEMMA ArchiMate-elementen afgeleid, per elementtype getoetst, ter beoordeling voorgelegd en na goedkeuring geëxporteerd naar het GEMMA ArchiMate-model. **Het GEMMA ArchiMate-model is de formele bron van waarheid** — de wiki bevat analyse, onderbouwing en voorstellen, nooit de definitieve registratie.

De wiki-mappen (`{wiki-root}/…`) staan beschreven in [ontwerp/mappenstructuur.md](ontwerp/mappenstructuur.md); de locatie van de wiki-root is nog een te nemen besluit.

## Kernregels (altijd van toepassing)

1. **Bronnen zijn immutabel** — de inhoud van bestanden in `Sources/` wijzig je nooit; verplaatsen en frontmatter-intake mogen wel.
2. **Herleidbaarheid** — elke claim en elk voorgesteld element is traceerbaar: kandidaatpagina → source-pagina → bronbestand. Onzeker? Markeren, niet gokken.
3. **Getrapte autonomie** — bespreek een bron op hoofdlijnen vóór je schrijft; eenduidige gevallen handel je zelfstandig af, twijfelgevallen leg je per stuk voor. De statusovergangen naar `goedgekeurd` en `afgewezen` zijn altijd een teambesluit — die zet je nooit zelfstandig.
4. **Geen dubbele vastlegging** — elk gegeven heeft één vindplaats; volg [ontwerp/dubbeling.md](ontwerp/dubbeling.md).
5. **Logboek** — elke inhoudelijke paginamutatie krijgt één regel in `{wiki-root}/log.md`; overzichten worden gegenereerd (`voortgang.md`), nooit met de hand bijgehouden.
6. **Typegericht werken** — kandidaten ontstaan uit type-extractie met de kaders in [typen/](typen/), niet uit een generieke begrippenlijst.

## Waar staat wat

- Procesmodel (6 stappen): [ontwerp/procesmodel.md](ontwerp/procesmodel.md)
- Paginatypen en statuscyclus: [ontwerp/paginamodel.md](ontwerp/paginamodel.md)
- Mappenstructuur en logboek: [ontwerp/mappenstructuur.md](ontwerp/mappenstructuur.md)
- Toetsingskaders per elementtype: [typen/](typen/)
- Paginatemplates: [templates/](templates/)
- Export naar GEMMA: [ontwerp/exportmodel.md](ontwerp/exportmodel.md)
- Open punten (benoemen, niet zelf oplossen): [ontwerp/open-punten.md](ontwerp/open-punten.md)

## Werken

- **Een taak uitvoeren:** gebruik de prompt uit [prompts/](prompts/) die bij de processtap hoort; elke prompt vermeldt doel, parameters en benodigde context.
- **Pagina's aanmaken:** volg de templates in [templates/](templates/). Linkconventie: relatieve markdown-links, geen `[[wiki-links]]`.
- **Twijfel over een elementtype:** raadpleeg het typebestand in [typen/](typen/); ontbreekt het type, voeg dan eerst het kader toe volgens [typen/README.md](typen/README.md).
- **Een open punt geraakt** (GGM-rol, migratie, CSV-pijplijn, levenscyclus na export): benoemen en voorleggen, niet zelf oplossen.
