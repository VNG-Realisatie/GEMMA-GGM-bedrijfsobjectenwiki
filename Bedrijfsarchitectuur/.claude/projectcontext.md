# Projectcontext

## Doel en gebruiker
- [P1] Gebruiker is het GEMMA-team bij VNG. De wiki is een professioneel werkinstrument voor standaardontwikkeling (fundament voor onderhoud en doorontwikkeling van de GEMMA bedrijfsobjecten), geen persoonlijk naslagwerk.
- [P2] Kwaliteit en onderbouwing zijn cruciaal: de wiki voedt een landelijke standaard.
- [P3] GGM is de primaire bron maar kan fouten bevatten; correcties worden teruggekoppeld aan het GGM.
- [P4] GGM-entiteiten ≠ BO's; de wiki onderbouwt de vertaalslag.
- [P5] Hiaten (BO's zonder GGM-grondslag) worden opgevuld en eventueel teruggekoppeld.

## Element-schema (besluit 2026-07-08)
- [P6] Overkoepelende term is **element**. Skills: `/assess-element`, `/write-element` (voorheen `/assess-bo`, `/write-bo`). Template: `templates/element.md`. Frontmatter `type: element` (voorheen `type: bedrijfsobject`) voor alle pagina's in `Wiki/Bedrijfsobjecten/`, `Wiki/Actoren/` en `Wiki/Rollen/`.
- [P7] `archimate_type` is de enige plek voor het specifieke elementtype: `business-object | contract | product | business-actor | business-role`.
- [P8] Actoren en rollen krijgen eigen pagina's in platte mappen: `Wiki/Actoren/{naam}.md`, `Wiki/Rollen/{naam}.md`.
- [P9] ALS een begrip zowel actor/rol als BO is (6 BO-criteria gehaald) → TWEE aparte pagina's met cross-links (patroon: [BO22]). NOOIT dubbele tags op één pagina.
- [P10] `ggm_guid` mag op meerdere pagina's staan (BO en actor delen dezelfde GGM-entiteit). Scripts gebruiken multi-map indexen; NOOIT last-write-wins.
- [P11] Doelgroep is GEEN actor of rol, maar een BO-classificatie waarmee Business Actors worden ingedeeld.
- [P12] Beslisvraag actor vs. rol: gaat het over *wie* iets doet (Actor) of *in welke verantwoordelijkheid* (Role)? Criteria: 6 diagnostische vragen per type in `Wiki/GEMMA/actoren-en-rollen.md`.
- [P13] ALTIJD element-terminologie en het twee-pagina-patroon gebruiken bij ingest, assess en write.
- [P14] Bij entiteitendekking: actoren/rollen matchen. NIET automatisch n.v.t.
- [P15] `/audit-actoren` track 2 (sweep over bronsamenvattingen): max 3–4 subagents tegelijk (quota); volledige instructies staan in de skill.

## ArchiMedes-sjablonen (read-only)
- [P16] `Categorie:SmartConnectArchiMate™` (30 pagina's) op redactie.gemmaonline.nl bevat de kernsjablonen van de extensie SmartConnectArchiMate™ (ArchiMedes), beheerd door leverancier ArchiXL. Lokaal gespiegeld in `GEMMA online/SmartConnectArchiMate™/` (2026-08-07). READ-ONLY.
- [P17] NOOIT voorstellen deze pagina's te bewerken of naar de wiki te publiceren; wijzigingen lopen via ArchiXL.
- [P18] Bij vragen over de werking van ArchiMedes (bv. `#displayArchiMateDiagram`, `{{#element:...}}`, `DisplayArchiMateElement`): ALTIJD eerst die map raadplegen. NOOIT aannames doen.
- [P19] De GEMMA-eigen `...Custom`-varianten (`GEMMA sjablonen/GEMMA ArchiMedesTemplates/`) worden WEL door dit project beheerd. Ze overschrijven de standaardsjablonen via de naamconventie van ArchiMedes (zie `Sjabloon:DisplayArchiMateCustom/_index`).

## Toegang redactie.gemmaonline.nl
- [P20] `redactie.gemmaonline.nl` is de MediaWiki-redactieomgeving waarin het GEMMA-team schrijft vóór publicatie naar de publieke `gemmaonline.nl`. Lezen vereist authenticatie (anonieme API-calls geven `readapidenied`). Werkregels voor de lokale content: `GEMMA online/CLAUDE.md`.
- [P21] Toegang via de MCP-server `@professional-wiki/mediawiki-mcp-server` (npm); geen custom script. Wiki-config: `scriptpath: ""`, `articlepath: "/wiki"`.
- [P22] Authenticatie ALTIJD via MediaWiki Bot Password (NIET het hoofdaccount-wachtwoord). Config `~/.config/mediawiki-mcp/config.json` staat buiten de repo; wachtwoord via `${VAR}`-substitutie; NOOIT in de repo.
- [P23] Controleer vóór gebruik van de MCP-tools met `claude mcp list` of de server verbonden is.
- [P24] Schrijven naar redactie ALLEEN met bevestiging per pagina. NOOIT batch.
- [P25] Het Bot Password draait onder account `MarkBacker` (groepen `sysop`/`bureaucrat`/`interface-admin`) en is NIET read-only. De enige beveiliging is client-side `readOnly: true` in de config. De gebruiker heeft dit risico op 2026-08-04 bewust geaccepteerd; NIET opnieuw als open stap opvoeren.

## Notes
- Status element-schema 2026-07-09: fase 1–4 uitgevoerd (schema-migratie, 22 actor/rol-pagina's + 6 BO-tegenhangers, scripts multi-map, rapporten geregenereerd: gedekt 694→709). Open: track 2 van `/audit-actoren` (218 bronsamenvattingen, 34 onderwerpmappen) en 4 "ter discussie"-ambiguïteiten (Raadscommissie, Pachter e.a.) via `bo_via_kandidaten` cureren.
- Status toegang 2026-08-04: MCP-server geïnstalleerd en geverifieerd (`get-page` op "Toelichting data bij de bron" gaf correcte wikitext).
