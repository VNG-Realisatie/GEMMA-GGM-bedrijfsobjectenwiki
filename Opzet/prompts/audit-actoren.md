# audit-actoren

**Doel:** ontbrekende actor- en rolpagina's opsporen in bestaande content (retrofit-sweep). Deze taak vindt alleen de werkvoorraad; beoordeling en vastlegging lopen via de prompts `assess-element` en `write-element`.
**Aanbevolen model:** standaard
**Parameters:** {{scope}} — onderwerp of taakveld; optioneel (leeg = alles).
**Benodigde context:** `Wiki/GEMMA/actoren-en-rollen.md` (definities en criteria), `Wiki/Analyses/entiteitendekking/`, `Wiki/Bronsamenvattingen/`, `Wiki/Actoren/`, `Wiki/Rollen/`.
**Verwachte uitvoer:** kandidatenlijst, beoordeelde en vastgelegde pagina's, bijgewerkte onderwerpoverzichten/index/log, en een afsluitende rapportagetabel.

## Prompt

Spoor ontbrekende actor- en rolpagina's op in bestaande content. Scope: {{scope}}

### Track 1: GGM-geankerde kandidaten (goedkoop, geen bronnen nodig)

1. Doorzoek de rapporten in `Wiki/Analyses/entiteitendekking/` op tabelrijen met entiteitstype `actor` of `rol` en dekking `n.v.t.` — dit kan met grep of een script, zonder LLM.
2. Dedupliceer op GGM-entiteitnaam; sla kandidaten over die al een pagina hebben (check `ggm_entiteit`/`ggm_guid` in de frontmatter van `Wiki/Actoren/` en `Wiki/Rollen/`).
3. Resultaat: kandidatenlijst met GGM-entiteit, GUID, taakveld/beleidsdomein en de rapportregel als context.

### Track 2: Niet-GGM-kandidaten uit bronsamenvattingen (zwaarder, gebatcht)

1. Scan de bronsamenvattingen per onderwerpmap op genoemde actoren en rollen zonder GGM-entiteit (governance-hiaten, bijv. heffingsambtenaar).
2. **Batch per onderwerpmap, niet per bestand.** Ondersteunt de tool subagents of parallelle sessies: werk in golven van maximaal 3-4 parallelle taken, elk met een cluster van 5-8 onderwerpen; anders sequentieel per cluster. Meld na elke golf een tussenstand.
3. Noteer per kandidaat: naam, type-vermoeden (actor/rol), bronsamenvatting(en), en of het begrip relevant is voor de gemeente (louter externe context zonder gemeentelijke relatie valt af).
4. Sla kandidaten over die al een pagina hebben (naam-check in `Wiki/Actoren/`, `Wiki/Rollen/` én `bo_synoniemen`).

### Beoordeling en vastlegging

Per kandidaat uit beide tracks:

1. Voer de prompt `assess-element` uit — begripstype, actor/rol-toets en onafhankelijk de 6 BO-criteria. De autonomieregels bepalen wat zelfstandig mag en wat wordt voorgelegd.
2. Bij bevestiging: voer de prompt `write-element` uit — actor-/rolpagina, en bij het twee-pagina-patroon ook de BO-pagina met `element_tegenhangers` in beide richtingen.
3. Afgewezen kandidaten: niet vastleggen, wél in de rapportage vermelden met reden.

### Nazorg

- Onderwerpoverzichten bijwerken (begripstype actor/rol invullen waar vastgesteld).
- `Wiki/index.md` — secties Actoren en Rollen aanvullen.
- `Wiki/log.md` — één samenvattende entry met aantallen (gevonden / aangemaakt / afgewezen met reden).

### Rapportage

Sluit af met een tabel: kandidaat | track | actor/rol | pagina aangemaakt? | ook BO? | opmerking.

## Voorbeeld

> Spoor ontbrekende actor- en rolpagina's op in bestaande content. Scope: taakveld 6 (Sociaal Domein)
