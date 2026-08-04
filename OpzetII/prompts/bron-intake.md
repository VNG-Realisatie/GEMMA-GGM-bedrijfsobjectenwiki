# bron-intake

**Doel:** een bron veiligstellen als immutabele kopie in `Sources/` en ontsluiten met een source-pagina.
**Aanbevolen model:** standaard
**Parameters:** {{bron}} — pad, URL of PDF van de bron. Verplicht.
**Benodigde context:** [../templates/source.md](../templates/source.md), [../ontwerp/mappenstructuur.md](../ontwerp/mappenstructuur.md), `{wiki-root}/onderwerpen/` (bestaande topics).
**Verwachte uitvoer:** bronbestand in `Sources/`, source-pagina in `{wiki-root}/bronnen/`, logregel, voorstel voor vervolg.

## Prompt

Verwerk de bron: {{bron}}

1. **Stel de kopie veilig.** Een URL haal je op als exacte kopie (bijv. met `curl` + eenvoudige HTML-naar-markdown-conversie) — gebruik geen fetch-functie die samenvat of parafraseert. Een PDF converteer je naar markdown. Plaats het resultaat in `Sources/` (verplaatsen, niet herschrijven). De inhoud van bronbestanden is immutabel: nooit herschrijven of vertalen.
2. **Bespreek op bronniveau.** Vat de kernpunten van de bron samen en leg die voor vóór je pagina's schrijft.
3. **Maak de source-pagina** volgens [../templates/source.md](../templates/source.md): metadata in de frontmatter, samenvatting, selectief letterlijke passages met plaatsaanduiding. Geen ArchiMate-analyse.
4. **Koppel onderwerpen.** Past de bron bij bestaande topic-pagina's, vul dan `onderwerpen:` en de brontabel van die topics aan; ontbreekt een passend onderwerp, stel er dan een voor en maak het aan via de prompt [onderwerp.md](onderwerp.md).
5. **Log** één regel per aangemaakte/gewijzigde pagina in `{wiki-root}/log.md`.
6. **Meld** wat is aangemaakt en stel voor welke type-extracties (onderwerp × type) nu zinvol zijn.

## Voorbeeld

> Verwerk de bron: https://www.voorbeeldstad.nl/beleid/vth-beleidsplan-2025-2028.pdf
