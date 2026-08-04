# Promptbibliotheek

Vijftien uitvoerbare taakprompts, bruikbaar met elke LLM-tool. Elke prompt is een zelfstandig markdown-bestand met een vaste kop en daaronder de prompttekst.

## Formaat

```markdown
# naam
**Doel:** wat de taak oplevert
**Aanbevolen model:** standaard | licht
**Parameters:** {{naam}} — betekenis, verplicht/optioneel
**Benodigde context:** welke bestanden de LLM moet kunnen lezen
**Verwachte uitvoer:** wat er aan het eind bestaat of gerapporteerd is

## Prompt
(de prompttekst)

## Voorbeeld
(één concrete aanroep)
```

## Gebruik

1. Open het promptbestand van de taak.
2. Vervang de `{{parameter}}`-placeholders door concrete waarden (of geef ze mee zoals je tool dat ondersteunt — sommige tools substitueren parameters automatisch, in een chat-tool plak je de ingevulde prompt).
3. Zorg dat de LLM de bestanden onder **Benodigde context** kan lezen: in een agent-tool met bestandtoegang volstaat de verwijzing; in een chat-tool upload of plak je ze.
4. **Aanbevolen model** `licht` betekent: read-only analyse zonder redeneerwerk — een klein/goedkoop model volstaat. `standaard` betekent: het reguliere projectmodel.

Prompts die naar elkaar verwijzen (bijv. ingest → assess-element → write-element) voer je uit door de genoemde prompt als volgende taak te starten, met dezelfde regels.

## Overzicht

| Prompt | Doel | Model |
|---|---|---|
| [ingest.md](ingest.md) | Bron(nen) verwerken tot wiki-pagina's (orchestrator) | standaard |
| [assess-element.md](assess-element.md) | Begrip volledig beoordelen (classificatie, criteria, hiaat) | standaard |
| [write-element.md](write-element.md) | Beoordeeld element vastleggen als pagina | standaard |
| [entiteitendekking.md](entiteitendekking.md) | GGM-dekkingsrapportage genereren/verversen | standaard |
| [domain-status.md](domain-status.md) | Voortgangsrapport per onderwerp (read-only) | licht |
| [lint.md](lint.md) | Consistentiecheck op de wiki | licht |
| [fetch.md](fetch.md) | URL ophalen als bronbestand | licht |
| [clip.md](clip.md) | Webclip verplaatsen naar Sources | standaard |
| [convert-pdf.md](convert-pdf.md) | PDF converteren naar markdown-bron | standaard |
| [crawl.md](crawl.md) | Webpagina('s) crawlen naar markdown | standaard |
| [generate-ggm.md](generate-ggm.md) | GGM-pipeline: XMI → JSON → Wiki/GGM | standaard |
| [export-ggm.md](export-ggm.md) | GGM-GEMMA CSV's genereren | standaard |
| [audit-duplicaten.md](audit-duplicaten.md) | Scan op naamconflicten in alle BO's | licht |
| [audit-definities.md](audit-definities.md) | Definities controleren en herstellen | standaard |
| [audit-actoren.md](audit-actoren.md) | Ontbrekende actor-/rolpagina's opsporen | standaard |

Prompts die pagina's wijzigen werken altijd `Wiki/index.md` bij en voegen een entry toe aan `Wiki/log.md`.
