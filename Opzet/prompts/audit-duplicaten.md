# audit-duplicaten

**Doel:** alle BO's systematisch scannen op nog niet gedocumenteerde naamconflicten (duplicaten en homoniemen); resultaat is een lijst voorgestelde correcties die per geval worden beoordeeld.
**Aanbevolen model:** licht (read-only analyse, geen redeneerwerk)
**Parameters:** {{scope}} — optioneel: onderwerp of taakveld; leeg = alle BO's.
**Benodigde context:** `Wiki/Bedrijfsobjecten/` (frontmatter), `Sources/GGM-repository/ggm_parsed.json`, [../templates/element.md](../templates/element.md).
**Verwachte uitvoer:** rapportage in drie categorieën (A: ongedocumenteerde conflicten, B: ontbrekende symmetrie, C: synoniemsuggesties); correcties pas na beoordeling door de gebruiker.

## Prompt

Controleer alle bestaande BO's op naamconflicten (duplicaten en homoniemen). Scope: {{scope}}

1. **Inventarisatie.** Lijst alle BO-bestanden met `naam`, `ggm_entiteit`, `ggm_guid`, `ggm_beleidsdomein`, `bo_synoniemen`, `bo_homoniemen` en `ggm_duplicaat_entiteiten` uit de frontmatter. Laad de GGM-data uit `ggm_parsed.json`.
2. **Duplicaat-bestandsnamen.** Zoek gelijknamige BO-bestanden in verschillende domeinmappen — potentiële homoniemen. Signaleer waar `bo_homoniemen` nog leeg is.
3. **GGM-naamconflicten.** Voor elke BO met grondslag ggm-entiteit: zoek alle GGM-entiteiten met dezelfde naam. Bij meerdere voorkomens: duplicaat-check (zelfde concept, ander beleidsdomein — staat het in `ggm_duplicaat_entiteiten`?) en homoniem-check (ander concept — staat het in `bo_homoniemen`?). Signaleer ontbrekende documentatie.
4. **Cross-referentie.** Voor elke BO met gevulde `bo_homoniemen`: heeft het gerefereerde BO een symmetrische verwijzing terug, en vermeldt de `## GGM-duplicaten`-sectie het homoniem?
5. **Synoniemsuggesties.** Voor elke BO waarvan `naam` ≠ `ggm_entiteit` (en `ggm_entiteit` gevuld): staat de GGM-naam in `bo_synoniemen`? Staat een afwijkende `ggm_gemma_alternate_name` erin?
6. **Rapportage** in drie categorieën, gesorteerd A → B → C:
   - **A. Ongedocumenteerde naamconflicten (actie vereist)** — per conflict: BO-naam en pad, GGM-entiteitnaam, conflicterende entiteit (naam, GUID, beleidsdomein), type (duplicaat/homoniem), voorstel (frontmatter vullen / hernoemen / samenvoegen).
   - **B. Ontbrekende symmetrie (correctie vereist)** — eenzijdige homoniemverwijzingen.
   - **C. Ontbrekende synoniemen (suggestie).**

Vraag per bevinding om beoordeling voordat je correcties doorvoert.

## Voorbeeld

> Controleer alle bestaande BO's op naamconflicten (duplicaten en homoniemen). Scope: (leeg — hele wiki)
