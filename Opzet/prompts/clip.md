# clip

**Doel:** een webclip uit de landingszone `Clippings/` verwerken tot een bronbestand in `Sources/`.
**Aanbevolen model:** standaard
**Parameters:** {{bestand}} — bestandsnaam in `Clippings/`; optioneel (leeg = toon de aanwezige bestanden en vraag welke).
**Benodigde context:** [../context/bronnen.md](../context/bronnen.md), `Clippings/`, `Sources/Onderwerpen/` (bestaande onderwerpmappen).
**Verwachte uitvoer:** het bestand staat als bron in `Sources/Onderwerpen/{onderwerp}/` met complete frontmatter; voorstel om een ingest te starten.

## Prompt

Verwerk de clipping: {{bestand}}

1. Lees het bestand in `Clippings/`. Is er geen bestand opgegeven, toon dan de aanwezige bestanden en vraag welke.
2. Is het een PDF, converteer die dan eerst via de prompt `convert-pdf`.
3. Bepaal het onderwerp volgens de indelingsregels in [../context/bronnen.md](../context/bronnen.md).
4. Verplaats naar `Sources/Onderwerpen/{onderwerp}/{beschrijvende-slug}.md` (lowercase, kebab-case, max 60 tekens).
5. Vul ontbrekende frontmatter aan (description, tags).
6. Meld welk bestand is aangemaakt en stel voor een ingest te starten (prompt `ingest`).

Let op: bronbestanden worden nooit vertaald of herschreven — behoud de originele tekst.

## Voorbeeld

> Verwerk de clipping: `Clippings/Nota Dierenwelzijn Utrecht.md`
