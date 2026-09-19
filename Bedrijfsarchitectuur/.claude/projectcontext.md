# Projectcontext

## gemma-team-wiki

Het team dat deze wiki gebruikt IS het GEMMA-team bij VNG. De wiki dient als fundament voor het onderhouden en doorontwikkelen van de GEMMA bedrijfsobjecten.

**Why:** Er ontbreekt een onderbouwd besliskader voor welke GGM-entiteiten bedrijfsobjecten worden, wat ontbreekt, en wat gecorrigeerd moet worden. De wiki bouwt dat fundament op vanuit bronnen.

**How to apply:**
- De wiki is geen persoonlijk naslagwerk maar een professioneel werkinstrument voor standaardontwikkeling
- GGM is de primaire bron maar kan fouten bevatten — correcties worden teruggekoppeld naar het GGM
- GGM-entiteiten ≠ bedrijfsobjecten; de wiki onderbouwt de vertaalslag
- Hiaten (BO's zonder GGM-grondslag) worden opgevuld en eventueel teruggekoppeld
- Kwaliteit en onderbouwing zijn cruciaal — dit voedt een landelijke standaard

## project-element-schema

Besloten op 8 juli 2026 (goedgekeurd plan, zie `.claude/plans/er-wordt-nu-niet-federated-curry.md`):

- Overkoepelende term is **element**: skills heten `/assess-element` en `/write-element` (voorheen `/assess-bo`/`/write-bo`), template `templates/element.md`, frontmatter `type: element` (voorheen `type: bedrijfsobject`) voor alle pagina's in `Wiki/Bedrijfsobjecten/`, `Wiki/Actoren/` en `Wiki/Rollen/`.
- `archimate_type` is de enige plek voor het specifieke elementtype: `business-object | contract | product | business-actor | business-role`.
- **Actoren en rollen krijgen eigen pagina's** in platte mappen `Wiki/Actoren/{naam}.md` en `Wiki/Rollen/{naam}.md`. Een begrip dat zowel actor/rol als bedrijfsobject is (6 BO-criteria gehaald = er worden gegevens over vastgelegd) krijgt **twee aparte pagina's** met cross-links — geen dubbele tags op één pagina.
- `ggm_guid` mag op meerdere pagina's staan (BO + actor delen dezelfde GGM-entiteit); scripts gebruiken multi-map indexen, geen last-write-wins.
- **Doelgroep is geen actor of rol** maar een BO-classificatie waarmee Business Actors worden ingedeeld.
- Actor/rol-criteria: ArchiMate-definities met elk 6 diagnostische vragen, gedocumenteerd in `Wiki/GEMMA/actoren-en-rollen.md`. Beslisvraag: gaat het over *wie* iets doet (Actor) of *in welke verantwoordelijkheid* (Role)?

**Why:** actoren/rollen werden inconsistent behandeld (soms BO, bij entiteitendekking altijd n.v.t.) terwijl ze wel relevant zijn voor GEMMA (Business Actor/Role-elementen).

**How to apply:** bij ingest/assess/write altijd de element-terminologie en het twee-pagina-patroon gebruiken; bij entiteitendekking actoren/rollen matchen i.p.v. automatisch n.v.t. Zie [[feedback-dubbele-namen]] voor het cross-linkpatroon.

**Status 9 juli 2026:** Fase 1-4 uitgevoerd (schema-migratie, 22 actor/rol-pagina's + 6 BO-tegenhangers, scripts multi-map + nieuwe mappen, rapporten geregenereerd: gedekt 694→709). **Nog open:** track 2 van `/audit-actoren` — sweep over de 218 bronsamenvattingen (34 onderwerpmappen) op niet-GGM actoren/rollen, in golven van max 3-4 subagents (quota); de skill bevat de volledige instructies. Ook open: 4 nieuwe "ter discussie"-ambiguïteiten (Raadscommissie, Pachter e.a.) via bo_via_kandidaten cureren. Wijzigingen stonden toen nog niet gecommit.

## project-archimedes-readonly-templates

De wiki-categorie `Categorie:SmartConnectArchiMate™` (30 pagina's, deels `Sjabloon:`-namespace, deels
mainspace zoals help-/glossarypagina's) bevat de kernsjablonen van de SmartConnectArchiMate™-extensie
(ArchiMedes), die door leverancier ArchiXL wordt beheerd en uitgerold — niet door het GEMMA-team.

**Why:** Deze pagina's zijn lokaal gespiegeld in `GEMMA online/SmartConnectArchiMate™/` (2026-08-07) als
referentiemateriaal, maar zijn read-only: wijzigingen moeten via ArchiXL, niet via directe wiki-edits
vanuit dit project.

**How to apply:** Bij vragen over hoe ArchiMedes zelf werkt (bv. `#displayArchiMateDiagram`,
`{{#element:...}}`, `DisplayArchiMateElement` als standaardsjabloon) eerst deze map raadplegen in plaats
van aannames te doen. Niet voorstellen om deze pagina's te bewerken of naar de wiki te publiceren; de
GEMMA-eigen `...Custom`-varianten (in `GEMMA sjablonen/GEMMA ArchiMedesTemplates/`) zijn wél door dit
project beheerd en overschrijven de standaardsjablonen via ArchiMedes' eigen naamconventie (zie
[[project_element-schema]] en de uitleg in `Sjabloon:DisplayArchiMateCustom/_index`).

## redactie-gemmaonline-toegang

`redactie.gemmaonline.nl` is de MediaWiki-redactieomgeving waarin het GEMMA-team daadwerkelijk schrijft, vóór publicatie naar de publieke `gemmaonline.nl`. Deze omgeving is netwerktechnisch rechtstreeks bereikbaar vanuit deze Claude Code-sessie (curl → HTTP 200), maar vereist authenticatie voor lezen (`readapidenied` op anonieme API-calls) — in tegenstelling tot de publieke site.

Gekozen aanpak (plan opgesteld 2026-08-04, bestand: `~/.claude/plans/is-het-mogelijk-om-soft-llama.md`, nog niet uitgevoerd):
- Gebruik de bestaande, officieel onderhouden **`@professional-wiki/mediawiki-mcp-server`** (npm) als MCP-server in Claude Code — geen custom script. Ondersteunt lezen én schrijven, met een `readOnly`-vlag per wiki.
- Authenticatie via **MediaWiki Bot Password** (self-service via `Special:BotPasswords`, niet het hoofdaccount-wachtwoord — dat ondersteunt deze adapter niet). Voor fase 1 alleen leesrechten toekennen.
- Config (`~/.config/mediawiki-mcp/config.json`) leeft buiten de git-repo; wachtwoord via `${VAR}`-substitutie, nooit in de repo.
- Schrijven naar redactie is expliciet uitgesteld tot een latere, aparte stap — altijd met bevestiging per pagina, nooit batch.

**Why:** de gebruiker wil redactie.gemmaonline.nl als actuele/autoritatieve bron gebruiken om de lokale `GEMMA online/`-content (werkregels: zie `GEMMA online/CLAUDE.md`) te verifiëren en verbeteren, en op termijn rechtstreeks pagina's daar te wijzigen.

**How to apply:** voordat er daadwerkelijk MCP-tools voor deze wiki gebruikt worden, controleren of de MCP-server al geïnstalleerd is (`claude mcp list`) — dit was op 2026-08-04 nog niet het geval. Zie het plan-bestand voor de volledige installatiestappen.

**Status (2026-08-04): geïnstalleerd en geverifieerd, met een geaccepteerd risico.**
- MCP-server draait (`claude mcp list` → Connected), `get-page` op "Toelichting data bij de bron" gaf de correcte, actuele wikitext terug — config (`scriptpath: ""`, `articlepath: "/wiki"`) klopt.
- **Afwijking van het plan:** `whoami` toont dat het gebruikte Bot Password niet beperkt is tot leesrechten — het draait onder account `MarkBacker` met groepen `sysop`/`bureaucrat`/`interface-admin` en volle edit/create/move/upload-rechten, niet de bedoelde read-only grants. De bescherming zit dus alleen client-side via `readOnly: true` in `~/.config/mediawiki-mcp/config.json` (verbergt de schrijf-tools voor de MCP-client), niet server-side op het Bot Password zelf.
- Gebruiker is hierop gewezen en heeft **expliciet gekozen door te gaan met dit account**, voorlopig vertrouwend op de client-side `readOnly`-beperking in plaats van de grants op `Special:BotPasswords` alsnog te beperken. Bij het bouwen van de schrijf-fase (stap 5 uit het plan) is dit dus geen extra stap die nog gezet moet worden — het risico is bewust geaccepteerd, niet opgelost.
