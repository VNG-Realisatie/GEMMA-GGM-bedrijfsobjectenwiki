# Werkwijze (generiek)

## niet-herschrijven

Bij verplaatsen of herstructureren van tekst: alleen knippen en plakken, niet herschrijven.

**Why:** Gebruiker vroeg om het tweede deel van een definitie te verplaatsen naar een toelichtingsveld. In plaats van de bestaande tekst te splitsen, werd de definitie herschreven en ingekort. Dat kostte drie correctierondes.

**How to apply:** Als de instructie is "verplaats X naar Y" of "splits dit op": gebruik de exacte bestaande tekst. Herformuleer niet, kort niet in, "verbeter" niet. Alleen knippen en plakken. Herschrijven mag alleen als dat expliciet gevraagd wordt.

## cross-cutting-verificatie

Na afloop van subagent-werk altijd een checklist aflopen van cross-cutting updates. Agents schrijven per-bestand correct maar updaten geen gedeelde bestanden.

**Why:** Subagents maken BO-pagina's met forward references (`Zie [[ggm-terugmeldingen]]`) maar updaten dat bestand niet. Controle op "bestanden bestaan + juist format" mist doorwerkingen naar centrale bestanden.

**How to apply:** Na elke agent-run deze checklist doorlopen:
1. `Wiki/Analyses/ggm-terugmeldingen.md` — nieuwe hiaten/correcties uit de BO-pagina's toegevoegd?
2. `Wiki/index.md` — alle nieuwe BO's en bronsamenvattingen opgenomen?
3. `Wiki/log.md` — entry kloppend met werkelijke aantallen?
4. `Wiki/Domeinen/{domein}.md` — bo_count en begrippen_count actueel?
5. Forward references in BO-pagina's — verwijzen ze naar bestaande bestanden?

Niet aannemen dat agents cross-cutting updates afhandelen. Zie ook ggm-dekking-verificatie.

## wetten-curl

Wetteksten van wetten.overheid.nl moeten via `curl` + Python HTML-extractie worden opgehaald, niet via WebFetch. WebFetch stuurt de pagina door een samenvattend model dat de wettekst parafraseert of inkort — bronbestanden moeten originele tekst bevatten.

**Why:** 6 van 9 wetten.overheid.nl-bronnen bleken samengevat in plaats van origineel. WebFetch's interne model heeft een outputlimiet en eigen quoteerbeperkingen waardoor het wettekst herformuleert.

**How to apply:** Bij elke URL van wetten.overheid.nl: (1) `curl -sL` → HTML downloaden, (2) Python HTMLParser om navigatie/footer/LiDO-links te strippen, (3) wettekst begint bij eerste "Hoofdstuk" heading. Extractiescript: zie pdf-conversie voor vergelijkbaar patroon. Het `extract_wetten.py` script in scratchpad is herbruikbaar.

## feedback-geen-technische-verwijzingen-wiki

Bij het Bedrijfsarchitectuur GEMMA-wiki-project (VNG): twee gekoppelde regels, nu ook vastgelegd in CLAUDE.md §7 punt 4 en `templates/element.md`.

**Regel 1 — geen verwijzingen naar technische/proces-bestanden vanuit wiki-content.** BO-pagina's, begrippen, analyses en bronsamenvattingen mogen niet citeren naar `CLAUDE.md`, `templates/`, `tools/` of skills (`.claude/commands/`). Die bestanden beschrijven hóe de wiki gebouwd wordt, niet wát erin staat, en zijn geen stabiel citaat-anker (sectienummers verschuiven, bestanden worden hernoemd/verwijderd).

**Regel 2 — generieke absolute taal is een geurmarkering voor een te zwakke bewering.** Formuleringen als "structureel buiten scope", "per definitie", "GGM modelleert nooit X" zonder domeinspecifieke onderbouwing zijn fout gebleken: het GGM-beleidsdomein Normafwijking (ontdekt tijdens de Participatiewet-ingest, 2026-09-18) modelleert wél een deel van het handhavingsproces (Maatregel, Boete), wat de eerdere absolute claim "GGM modelleert nooit processen/governance" weerlegt. De juiste, zwakkere en correcte formulering is: procesobjecten/governance-objecten zijn in het GGM *niet compleet gedekt* — een waargenomen gat, geen categorische/definitionele uitsluiting.

**Cruciale nuance (expliciet door de gebruiker bevestigd):** dit geldt alleen voor het generieke patroon zonder eigen redenering. Een inhoudelijk onderbouwde constatering met een concrete, specifieke reden (bijv. "dit beleidsdomein begint pas bij X, de fase daarvoor valt erbuiten" of "GGM heeft wel BAG-locaties maar niet dit type locatie") is prima en moet **niet** aangepast worden, ook al bevat de zin het woord "structureel". Bij een lint-achtige opschoning van deze framing: eerst per geval beoordelen of er een specifieke reden gegeven wordt, niet blind alle voorkomens van "structureel"/"buiten scope" vervangen.

**Why:** de gebruiker corrigeerde dit toen ik (bij het oplossen van dode links naar een verwijderde analysepagina) zelf per ongeluk beide fouten maakte: ik voegde CLAUDE.md-citaten toe aan BO-pagina's, én ik kopieerde de te-absolute "buiten scope per definitie"-formulering zonder de Normafwijking-tegenvoorbeeld-nuance.

**How to apply:** bij het schrijven of redigeren van BO-pagina's (via `/write-element` of losse edits): nooit een technisch bestand citeren als onderbouwing; laat de inhoudelijke bewering op eigen kracht staan met een concrete, domeinspecifieke reden. Bij een generieke "GGM doet dit niet"-bewering: herformuleer naar "in het GGM niet compleet gedekt" tenzij er een specifieke, aanwijsbare reden is (ontbrekend beleidsdomein, specifieke wetsverwijzing, attribuutvergelijking).
