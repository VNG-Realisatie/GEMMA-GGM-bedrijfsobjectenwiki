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
- [P9] ALS een begrip zowel actor/rol als BO is (6 BO-criteria gehaald) → TWEE aparte pagina's, gekoppeld via `element_tegenhangers` (frontmatter) en een cross-link in de tekst. NOOIT dubbele tags op één pagina.
- [P10] `ggm_guid` mag op meerdere pagina's staan (BO en actor delen dezelfde GGM-entiteit). Scripts gebruiken multi-map indexen; NOOIT last-write-wins.
- [P11] Doelgroep is GEEN actor of rol, maar een BO-classificatie waarmee Business Actors worden ingedeeld.
- [P12] Beslisvraag actor vs. rol: gaat het over *wie* iets doet (Actor) of *in welke verantwoordelijkheid* (Role)? Criteria: 6 diagnostische vragen per type in `Wiki/GEMMA/actoren-en-rollen.md`; 4 of meer ja = kwalificeert als actor resp. rol, ongeacht of er gegevens over worden vastgelegd.
- [P13] ALTIJD element-terminologie en het twee-pagina-patroon gebruiken bij ingest, assess en write.
- [P14] Bij entiteitendekking: actoren/rollen matchen. NIET automatisch n.v.t.
- [P15] `/audit-actoren` track 2 (sweep over bronsamenvattingen): max 3–4 subagents tegelijk (quota); volledige instructies staan in de skill.

## Notes
- Status element-schema 2026-07-09: fase 1–4 uitgevoerd (schema-migratie, 22 actor/rol-pagina's + 6 BO-tegenhangers, scripts multi-map, rapporten geregenereerd: gedekt 694→709). Open: track 2 van `/audit-actoren` (218 bronsamenvattingen, 34 onderwerpmappen) en 4 "ter discussie"-ambiguïteiten (Raadscommissie, Pachter e.a.) via `bo_via_kandidaten` cureren.
