# Workflow: lint

Periodieke consistentiecheck van de wiki tegen templates en werkafspraken. De uitvoerbare checklist staat in [../prompts/lint.md](../prompts/lint.md); dit bestand beschrijft de zes controlecategorieën.

1. **Contradicties** — pagina's die elkaar tegenspreken; beide markeren met `⚠️ Tegenspraak met {andere pagina}`.
2. **Wees-pagina's** — pagina's zonder inkomende links; controleren of ze echt wees zijn of gelinkt moeten worden.
3. **Concepten zonder pagina** — begrippen die meermaals genoemd worden maar geen eigen pagina of tabelrij hebben; toevoegen aan de openstaande taken.
4. **Verouderde claims** — beweringen die door nieuwere bronnen achterhaald kunnen zijn; markeren met `🔍 Verificatie nodig` en de nieuwere bron citeren.
5. **Template-naleving** — frontmatter, secties en formattering conform de [templates](../templates/).
6. **Herleidbaarheid** — elementpagina's hebben een `## Bronnen`-sectie; claims hebben citaten.

**Rapportage:** genummerde lijst met voorgestelde fixes per categorie, gesorteerd op ernst: herleidbaarheid > ontbrekende data > inconsistenties > suggesties.

Verwante audits (dieper op één aspect): [../prompts/audit-definities.md](../prompts/audit-definities.md), [../prompts/audit-duplicaten.md](../prompts/audit-duplicaten.md), [../prompts/audit-actoren.md](../prompts/audit-actoren.md).
