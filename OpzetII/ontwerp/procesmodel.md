# Procesmodel

Zes stappen van bron tot GEMMA-element. Elke stap heeft een eigen prompt in [../prompts/](../prompts/). Per stap staat benoemd wat **permanent** wordt vastgelegd; alles daarbuiten is werkgeheugen en wordt niet bewaard.

```
Bronnen ──▶ Onderwerpen ──▶ Type-extractie ──▶ Kandidaat-elementen ──▶ Beoordeling en modellering ──▶ Export naar GEMMA
```

| # | Stap | Prompt | Permanente neerslag |
|---|---|---|---|
| 1 | Bronnen | [bron-intake.md](../prompts/bron-intake.md) | bronbestand in `Sources/` + source-pagina |
| 2 | Onderwerpen | [onderwerp.md](../prompts/onderwerp.md) | topic-pagina |
| 3 | Type-extractie | [type-extractie.md](../prompts/type-extractie.md) | kandidaatpagina's (status `kandidaat`) + extractietabel op de topic-pagina |
| 4 | Kandidaat-elementen | [kandidaat.md](../prompts/kandidaat.md) | uitgewerkte bronanalyse op de kandidaatpagina |
| 5 | Beoordeling en modellering | [beoordeling.md](../prompts/beoordeling.md) | typeanalyse, modelleerbesluit en voorstel; status `review`, na teambesluit `goedgekeurd`/`afgewezen` |
| 6 | Export naar GEMMA | [export.md](../prompts/export.md) | exportbestanden + exportmarkering op de pagina; het element zelf in GEMMA |

Elke stap die pagina's wijzigt voegt een regel toe aan `{wiki-root}/log.md` (zie [mappenstructuur.md](mappenstructuur.md)).

## Stap 1 — Bronnen

- **Doel:** een bron veiligstellen en ontsluiten: exacte, immutabele kopie in `Sources/`, plus een source-pagina met metadata, samenvatting, relevante passages en onderwerpkoppeling. Geen ArchiMate-analyse — die volgt pas in stap 3–5.
- **LLM-skill:** [bron-intake.md](../prompts/bron-intake.md).
- **Input:** een bronbestand, URL of PDF.
- **Output:** bronbestand in `Sources/` + source-pagina in `{wiki-root}/bronnen/`.
- **Permanent:** beide. De source-pagina is het herleidbaarheidsanker voor alle latere analyse.
- **Autonomie:** kernpunten van de bron worden op bronniveau besproken vóór er geschreven wordt (getrapte autonomie).

## Stap 2 — Onderwerpen

- **Doel:** bronnen groeperen rond een domein of onderwerp en zo de werkeenheid voor extractie afbakenen; per onderwerp inschatten welke ArchiMate-elementtypen er te verwachten zijn.
- **LLM-skill:** [onderwerp.md](../prompts/onderwerp.md).
- **Input:** één of meer source-pagina's.
- **Output:** een nieuwe of bijgewerkte topic-pagina (omschrijving, gekoppelde bronnen, relevante termen, relevante elementtypen).
- **Permanent:** de topic-pagina. Geen elementdefinities — een topic groepeert alleen.

## Stap 3 — Type-extractie

- **Doel:** per elementtype kandidaten identificeren binnen een onderwerp. Typegericht: de herkenningsvragen uit het typekader worden op de bronnen toegepast — er wordt niet eerst een generieke begrippenlijst gemaakt.
- **LLM-skill:** [type-extractie.md](../prompts/type-extractie.md), met parameters onderwerp en (optioneel) elementtype.
- **Input:** topic-pagina + gekoppelde source-pagina's (zo nodig de bronbestanden zelf) + het typekader uit [../typen/](../typen/) + de bestaande kandidatenmap (dedupe).
- **Output:** per nieuwe kandidaat een stub-kandidaatpagina met status `kandidaat` en de vindplaatsen; bij bestaande kandidaten een aangevulde `typen:`-lijst of synoniemenlijst. De extractietabel op de topic-pagina registreert dat dit type voor dit onderwerp is gedaan.
- **Permanent:** de kandidaatpagina's en de extractietabel.

## Stap 4 — Kandidaat-elementen

- **Doel:** van stub naar volwaardige kandidaat: de bronanalyse uitwerken over álle gekoppelde onderwerpen en bronnen heen — passages, termen en synoniemen, context. Duplicaten en synoniemen worden hier definitief samengevoegd: één pagina per begrip, ook bij meerdere typen.
- **LLM-skill:** [kandidaat.md](../prompts/kandidaat.md).
- **Input:** de kandidaatpagina + alle source-pagina's van de gekoppelde onderwerpen.
- **Output:** kandidaatpagina met gevulde secties Context en Bronanalyse; open vragen (wat de bronnen níet beantwoorden) gemarkeerd.
- **Permanent:** de uitgewerkte kandidaatpagina.

## Stap 5 — Beoordeling en modellering

- **Doel:** per overwogen type de criteria uit het typekader toetsen (elk criterium onderbouwd met een bronverwijzing), alternatieve typen expliciet wegen, een modelleerbesluit formuleren en het element voorstellen: definitie en relaties.
- **LLM-skill:** [beoordeling.md](../prompts/beoordeling.md).
- **Input:** de kandidaatpagina + de typekaders + de source-pagina's.
- **Output:** volledige kandidaatpagina (typeanalyse, alternatieve typen, modelleerbesluit, voorgestelde definitie, voorgestelde relaties); status naar `review`; een samenvatting ter bespreking.
- **Permanent:** het besluit mét motivatie op de pagina — ook bij afwijzing: een afgewezen kandidaat blijft bestaan, zodat dezelfde analyse niet opnieuw wordt gedaan.
- **Autonomie:** de LLM zet status `review` en legt voor; `goedgekeurd` en `afgewezen` zijn uitsluitend de verwerking van een expliciet teambesluit.

## Stap 6 — Export naar GEMMA

- **Doel:** goedgekeurde voorstellen overdragen aan het GEMMA ArchiMate-model, zonder dubbele vastlegging: het element wordt dáár geregistreerd, de wiki houdt de onderbouwing.
- **LLM-skill:** [export.md](../prompts/export.md).
- **Input:** alle kandidaatpagina's met status `goedgekeurd` en een leeg `export:`-veld (of een expliciete selectie).
- **Output:** exportbestanden in `{wiki-root}/export/{datum}/` volgens [exportmodel.md](exportmodel.md) + gevuld `export:`-veld op de pagina's + exportrapport.
- **Permanent:** in GEMMA het element; in de wiki de onderbouwing en de exportmarkering. Wat er daarna met de kandidaatpagina gebeurt (bevriezen, archiveren, reduceren) is een open punt — zie [open-punten.md](open-punten.md).
