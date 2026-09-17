Controleer alle bestaande BO's op naamconflicten (duplicaten en homoniemen): $ARGUMENTS

Input: `Wiki/Bedrijfsobjecten/`.
Output: chat-rapportage met voorstellen (geen automatische fix).

**Voer uit op model: Haiku** (deze skill is read-only analyse, geen reasoning nodig).

## Doel

Systematische scan van alle BO-pagina's om naamconflicten op te sporen die nog niet gedocumenteerd zijn in de `bo_synoniemen`, `bo_homoniemen` of `ggm_duplicaat_entiteiten` frontmatter. Resultaat: een lijst van voorgestelde correcties die per geval beoordeeld worden.

## Stap 1: Inventarisatie

1. **Lijst alle BO-bestanden** in `Wiki/Bedrijfsobjecten/` met hun `naam`, `ggm_entiteit`, `ggm_guid`, `ggm_beleidsdomein`, `bo_synoniemen`, `bo_homoniemen` en `ggm_duplicaat_entiteiten` uit frontmatter.
2. **Laad GGM-data** uit `Sources/GGM-repository/ggm_parsed.json`.

## Stap 2: Duplicaat-bestandsnamen detecteren

Zoek BO-bestanden met dezelfde bestandsnaam in verschillende domeinfolders. Dit zijn potentiële homoniemen.

Per match: controleer of de frontmatter `bo_homoniemen` al gevuld is. Zo niet → signaleer.

## Stap 3: GGM-naamconflicten detecteren

Voor elke BO met grondslag `ggm-entiteit`:

1. Zoek in `ggm_parsed.json` naar alle entiteiten met dezelfde naam als `ggm_entiteit`.
2. Als er meerdere voorkomens zijn:
   - **Duplicaat-check:** is het hetzelfde concept in een ander beleidsdomein? Check of `ggm_duplicaat_entiteiten` al gevuld is.
   - **Homoniem-check:** is het een ander concept? Check of `bo_homoniemen` al gevuld is.
3. Signaleer ontbrekende documentatie.

## Stap 4: Cross-referentie-check

Voor elke BO met **gevulde** `bo_homoniemen`:
- Controleer of het gerefereerde BO ook een `bo_homoniemen`-verwijzing terug heeft (symmetrie).
- Controleer of de `## GGM-duplicaten` body-sectie het homoniem vermeldt.

## Stap 5: Synoniemen-suggesties

Voor elke BO waarvan `naam` ≠ `ggm_entiteit` (en `ggm_entiteit` niet leeg):
- Controleer of de GGM-entiteitnaam in `bo_synoniemen` staat. Zo niet → suggereer toevoeging.
- Controleer of `ggm_gemma_alternate_name` in `bo_synoniemen` staat (als die gevuld is en afwijkt). Zo niet → suggereer toevoeging.

## Stap 6: Rapportage

Presenteer de bevindingen in drie categorieën:

### A. Ongedocumenteerde naamconflicten (actie vereist)
Naamconflicten die nog niet in frontmatter staan. Per conflict:
- BO-naam en pad
- GGM-entiteitnaam
- Conflicterende entiteit (naam, GUID, beleidsdomein)
- Type: duplicaat of homoniem
- **Voorstel:** wat moet er gebeuren (frontmatter vullen, hernoemen, samenvoegen)

### B. Ontbrekende symmetrie (correctie vereist)
Eenzijdige homoniemen-verwijzingen.

### C. Ontbrekende bo_synoniemen (suggestie)
GGM-namen of alternate names die als synoniem toegevoegd kunnen worden.

Sorteer op categorie A → B → C. Per bevinding: vraag de gebruiker om beoordeling voordat correcties worden doorgevoerd.
