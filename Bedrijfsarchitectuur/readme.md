# GEMMA Bedrijfsobjectenwiki

| Eigenaar | Ingevuld door |
|---------|----------------|
| Kennis Centrum Architectuur | Mark Backer |

Werkinstrument van het GEMMA-team voor het onderbouwd opbouwen en onderhouden van het GEMMA bedrijfsobjectenmodel. Het bestaande model is een gefilterde kopie van het GGM — deze wiki bouwt het opnieuw op met expliciete criteria en herleidbare onderbouwing vanuit beleidsbronnen.

## Werkwijze

De wiki wordt domein voor domein opgebouwd:

1. **Bronnen** — VNG-beleidsdocumenten worden opgehaald en opgeslagen in `Sources/`
2. **Begrippen** — uit bronnen worden begrippen geëxtraheerd en getypeerd (ArchiMate-mapping)
3. **BO-toetsing** — begrippen worden getoetst aan expliciete criteria (herkenbaarheid, eigen bestaan, levenscyclus, relaties)
4. **GGM-matching** — BO-kandidaten worden gematcht op GGM-entiteiten met beoordeling van matchsterkte
5. **Hiaten** — ontbrekende of afwijkende entiteiten worden gesignaleerd als terugmelding richting GGM

Het resultaat per domein: BO-beslisdocumenten met metadata die als properties naar het GEMMA ArchiMate-model gaan.

## Opzet

`Sources/` bevat immutabele bronnen (VNG-documenten, GGM-representatie). `Wiki/` bevat de afgeleide kennisbasis (begrippen, bedrijfsobjecten, bronsamenvattingen, analyses). `.claude/commands/` bevat 9 aanroepbare skills (`/ingest`, `/fetch`, `/lint`, `/coverage`, etc.). Schema en conventies staan in `CLAUDE.md`.

## Licentie

EUPL 1.2 (European Union Public Licence).
