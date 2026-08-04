# OpzetII — ontwerp: wiki voor GEMMA ArchiMate-elementafleiding

Nieuw, LLM-onafhankelijk wiki-ontwerp waarmee uit beleidsdocumenten en andere bronnen GEMMA ArchiMate-elementen worden afgeleid. Gebouwd juli 2026 volgens het ontwerpprompt [../Opzet/opzet prompt.md](../Opzet/opzet%20prompt.md); context en randvoorwaarden staan in [overdracht.md](overdracht.md).

## Kern van het ontwerp

- Het **GEMMA ArchiMate-model is de formele bron van waarheid** voor definitieve architectuurelementen; de wiki is een analyse- en curatieomgeving met onderbouwing, besluitvorming en voorstellen.
- **Typegerichte analyse**: per ArchiMate-elementtype wordt gezocht naar kandidaten — niet eerst alle begrippen verzamelen. Een begrip is alleen inputmateriaal; niet ieder begrip wordt een element.
- **Eén centrale kandidaatpagina** (element-candidate) per begrip: bronanalyse, typeanalyse, modelleerbesluit en voorgesteld element op één plek, met statuscyclus `kandidaat → review → goedgekeurd | afgewezen`.
- **Export zonder dubbele vastlegging**: goedgekeurde voorstellen gaan naar GEMMA; de wiki houdt de onderbouwing, nooit de definitieve registratie.

## Positie

| | |
|---|---|
| [../Opzet/](../Opzet/) | Documentatie van de huidige, werkende wiki-aanpak — blijft onaangeroerd; een keuze tussen beide werkwijzen valt later |
| Bestaande wiki (`Bedrijfsarchitectuur/Wiki/`) | Blijft onder de oude werkwijze; migratie is een apart, later besluit — zie [ontwerp/open-punten.md](ontwerp/open-punten.md) |
| GGM (Gemeentelijk Gegevensmodel) | Buiten scope van dit ontwerp — expliciet open punt, niet uitgewerkt |

## Structuur

| Map/bestand | Inhoud |
|---|---|
| [AGENTS.md](AGENTS.md) | Kerninstructies voor elke LLM — het startpunt van een werksessie |
| [ontwerp/](ontwerp/) | Het ontwerp: procesmodel, paginamodel, mappenstructuur, exportmodel, anti-dubbelingsrichtlijnen, open punten |
| [typen/](typen/) | Toetsingskaders per ArchiMate-elementtype (uitbreidbaar) |
| [templates/](templates/) | De 3 paginatemplates: source, topic, element-candidate |
| [prompts/](prompts/) | 7 uitvoerbare taakprompts — één per processtap plus rapportage |
| [voorbeelden/](voorbeelden/) | Doorgewerkt voorbeeld: bron → onderwerp → kandidaten (Business Object, Business Actor, Business Role) |
| [adapters.md](adapters.md) | Hoe je deze opzet in een specifieke LLM-tool laadt |
| [overdracht.md](overdracht.md) | De startnotitie waarmee dit ontwerp is gebouwd |

## Leesvolgorde

**Ontwerp beoordelen:** [ontwerp/procesmodel.md](ontwerp/procesmodel.md) → [ontwerp/paginamodel.md](ontwerp/paginamodel.md) → [voorbeelden/](voorbeelden/) → [ontwerp/open-punten.md](ontwerp/open-punten.md).

**LLM-sessie starten (toekomstig gebruik):** [AGENTS.md](AGENTS.md) laden; die verwijst naar de rest. Voor tools met beperkte context: minimaal AGENTS.md + de prompt van de taak + de context die de promptkop noemt.

## Hergebruikte vormconventies

Van de oude opzet zijn uitsluitend vendor-neutrale vormconventies overgenomen, geen inhoudelijk paginamodel of proces:

- **AGENTS.md als LLM-entrypoint** (open standaard) met dunne per-tool adapters;
- het **promptformat** (kop met Doel / Aanbevolen model / Parameters / Benodigde context / Verwachte uitvoer, daarna promptblok en voorbeeld);
- **relatieve markdown-links** — klikbaar in VS Code én Obsidian; geen `[[wiki-links]]`;
- **Nederlands**, bestandsnamen lowercase-kebab-case, kleine modulaire bestanden, documentatie en uitvoering gescheiden;
- **frontmatter-stijl**: lege waarde = blanco, dubbele quotes waar nodig, lege lijst = `[]`.
