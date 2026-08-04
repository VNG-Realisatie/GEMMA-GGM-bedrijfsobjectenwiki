# Promptbibliotheek

Zeven uitvoerbare taakprompts, bruikbaar met elke LLM-tool: één per processtap uit [../ontwerp/procesmodel.md](../ontwerp/procesmodel.md), plus een rapportageprompt.

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

1. Open het promptbestand van de taak en vervang de `{{parameter}}`-placeholders door concrete waarden (of geef ze mee zoals je tool dat ondersteunt).
2. Zorg dat de LLM de bestanden onder **Benodigde context** kan lezen: in een agent-tool volstaat de verwijzing, in een chat-tool upload of plak je ze.
3. **Aanbevolen model** `licht` = read-only analyse zonder redeneerwerk, een klein/goedkoop model volstaat; `standaard` = het reguliere projectmodel.

## Overzicht

| Prompt | Processtap | Doel | Model |
|---|---|---|---|
| [bron-intake.md](bron-intake.md) | 1 Bronnen | bron veiligstellen + source-pagina | standaard |
| [onderwerp.md](onderwerp.md) | 2 Onderwerpen | topic-pagina aanmaken/bijwerken | standaard |
| [type-extractie.md](type-extractie.md) | 3 Type-extractie | kandidaten identificeren per onderwerp × type | standaard |
| [kandidaat.md](kandidaat.md) | 4 Kandidaat-elementen | bronanalyse van een kandidaat uitwerken | standaard |
| [beoordeling.md](beoordeling.md) | 5 Beoordeling en modellering | typetoetsing, modelleerbesluit, voorstel | standaard |
| [export.md](export.md) | 6 Export | goedgekeurde kandidaten exporteren | standaard |
| [status.md](status.md) | — | voortgang.md genereren | licht |

## Vaste afspraken voor alle prompts

- Prompts die pagina's wijzigen voegen per mutatie één regel toe aan `{wiki-root}/log.md`.
- Getrapte autonomie: eenduidige gevallen zelfstandig, twijfelgevallen per stuk voorleggen; de statussen `goedgekeurd`/`afgewezen` alleen als verwerking van een teambesluit.
- Raakt een taak een open punt ([../ontwerp/open-punten.md](../ontwerp/open-punten.md)): benoemen, niet oplossen.
