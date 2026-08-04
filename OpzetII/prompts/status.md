# status

**Doel:** het statusoverzicht `voortgang.md` genereren uit de frontmatter van de wiki-pagina's.
**Aanbevolen model:** licht
**Parameters:** geen.
**Benodigde context:** `{wiki-root}/kandidaten/`, `{wiki-root}/onderwerpen/`, `{wiki-root}/bronnen/` (alleen frontmatter en extractietabellen).
**Verwachte uitvoer:** overschreven `{wiki-root}/voortgang.md`. Geen logregel — afgeleide bestanden worden niet gelogd.

## Prompt

Genereer het voortgangsoverzicht.

1. **Lees** de frontmatter van alle kandidaatpagina's en de extractietabellen van alle topic-pagina's.
2. **Schrijf `{wiki-root}/voortgang.md`** (volledig overschrijven) met:
   - generatiestempel en de melding dat dit bestand gegenereerd is — niet handmatig bewerken;
   - telling per status en per elementtype;
   - per status een tabel: kandidaat (link) | typen (met besluit) | onderwerpen;
   - per onderwerp: welke `relevante_typen` nog geen extractie hebben gehad (openstaand werk);
   - goedgekeurde kandidaten zonder `export:` (klaar voor export).
3. **Wijzig niets anders** — deze taak is verder read-only.

## Voorbeeld

> Genereer het voortgangsoverzicht.
