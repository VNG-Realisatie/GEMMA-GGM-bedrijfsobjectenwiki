Spoor ontbrekende actor- en rol-pagina's op in bestaande content: $ARGUMENTS

Input: `Wiki/Bedrijfsobjecten/` + `Wiki/Bronsamenvattingen/`.
Output: werkvoorraadlijst (chat) — vervolg via `/assess-element` en `/write-element`.

Retrofit-sweep, analoog aan `/audit-definities` en `/audit-duplicaten`: eenmalig (herhaalbaar), los van de doorlopende `/ingest`-flow. Deze skill **vindt alleen de werkvoorraad** — de beoordeling gebeurt via `/assess-element` (Stap 2b, actor/rol-toets) en het schrijven via `/write-element` (Stap 11). Definities en criteria: [[Wiki/GEMMA/actoren-en-rollen|Actoren en rollen]].

Scope-argument (optioneel): een onderwerp of taakveld om de sweep te beperken; leeg = alles.

## Track 1: GGM-geankerde kandidaten (goedkoop, geen bronnen nodig)

1. Doorzoek de gegenereerde rapporten in `Wiki/Analyses/entiteitendekking/` op tabelrijen met Entiteitstype `actor` of `rol` en BO/Dekking `⚠️ geen actor-pagina` of `⚠️ geen rol-pagina` — dit kan met grep/script, zonder LLM.
2. Dedupliceer op GGM-entiteitnaam en sla kandidaten over die al een pagina in `Wiki/Actoren/` of `Wiki/Rollen/` hebben (check op `ggm_entiteit`/`ggm_guid` in frontmatter).
3. Resultaat: een kandidatenlijst met per kandidaat GGM-entiteit, GUID, taakveld/beleidsdomein en de rapportregel als context.

## Track 2: Niet-GGM kandidaten uit bronsamenvattingen (zwaarder, gebatcht)

1. Scan de bronsamenvattingen in `Wiki/Bronsamenvattingen/` per onderwerp-map op genoemde actoren en rollen die géén GGM-entiteit zijn (governance-hiaten, bv. heffingsambtenaar/invorderingsambtenaar).
2. **Batch per onderwerp-map, niet per bestand.** Bij delegatie aan subagents: golven van maximaal 3-4 agents tegelijk, elk een cluster van 5-8 onderwerpen — geen agent per onderwerp. Na elke golf een tussenstand aan de gebruiker melden.
3. Per gevonden kandidaat noteren: naam, type-vermoeden (actor/rol), bronsamenvatting(en) waarin genoemd, en of het gemeentelijk perspectief van toepassing is (externe context uitsluiten).
4. Sla kandidaten over die al een pagina hebben (naam-check in `Wiki/Actoren/`, `Wiki/Rollen/` én `bo_synoniemen`).

## Beoordeling en vastlegging

Per kandidaat uit beide tracks:

1. `/assess-element {kandidaat}` — begripstype + actor/rol-toets (Stap 2b) + onafhankelijk de 6 BO-criteria. De autonomieregels van assess-element Stap 11 bepalen wat zelfstandig afgehandeld mag worden en wat aan de gebruiker wordt voorgelegd.
2. Bij bevestiging: `/write-element {kandidaat}` — actor/rol-pagina (Stap 11), en bij het twee-pagina-patroon ook de BO-pagina met `element_tegenhangers` beide kanten op.
3. Kandidaten die het gemeentelijk perspectief niet halen (louter externe context): niet vastleggen, wel in de sweeprapportage vermelden met reden.

## Nazorg

Zoals bij alle audits:
- Onderwerpoverzichten bijwerken (begrippentabel: begripstype actor/rol invullen waar de sweep dat heeft vastgesteld)
- `Wiki/index.md` — secties Actoren en Rollen aanvullen
- `Wiki/log.md` — één samenvattende entry voor de sweep met aantallen (kandidaten gevonden / pagina's aangemaakt / afgewezen met reden)

## Rapportage

Sluit af met een tabel: kandidaat | track | actor/rol | pagina aangemaakt? | ook BO? | opmerking.
