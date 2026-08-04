# Template: element-candidate-pagina

Locatie: `{wiki-root}/kandidaten/{slug}.md` — slug = begripsnaam, lowercase-kebab-case. **Eén pagina per begrip**, ook wanneer meerdere ArchiMate-typen in beeld zijn.

De centrale analysepagina: bronanalyse, typeanalyse, modelleerbesluit en voorgesteld element op één plek. Na goedkeuring wordt de machine-leesbare kern (frontmatter) geëxporteerd naar GEMMA; analyse en motivatie blijven hier. Statuscyclus en overgangsregels: [../ontwerp/paginamodel.md](../ontwerp/paginamodel.md).

## Frontmatter

```yaml
---
type: element-candidate
naam: 
status: kandidaat           # kandidaat | review | goedgekeurd | afgewezen
onderwerpen: []             # topic-slugs waar dit begrip uit voortkomt
typen:                      # elk gevonden of overwogen ArchiMate-type
  - type:                   # type-slug uit typen/, bijv. business-object
    besluit:                # leeg = nog niet beoordeeld | voorgesteld | afgevallen | gekozen
synoniemen: []
definitie:                  # voorgestelde definitie, tussen dubbele quotes; leeg tot stap 5
toelichting:                # aanvulling op de definitie; leeg als de definitie volstaat
relaties: []
#  - type:                  # associatie | compositie | aggregatie | generalisatie | toewijzing | realisatie | ...
#    element:               # slug van andere kandidaat of naam van bestaand GEMMA-element
#    element_in: kandidaten # kandidaten | gemma
#    beschrijving: ""
export:                     # leeg tot export; daarna datum + bestand
#  datum: 
#  bestand: 
---
```

## Body-secties

- **Context** — het begrip in gewone taal: wat is het, in welke situaties komt het voor.
- **Bronanalyse** — per bron: link naar de source-pagina, de relevante passages (verwijzing of kort citaat met plaatsaanduiding), gevonden termen en synoniemen. Open vragen die de bronnen niet beantwoorden expliciet markeren.
- **Typeanalyse** — per type uit `typen:` een subsectie met de criteriatabel uit het typekader ([../typen/](../typen/)): criterium | oordeel | onderbouwing met bronverwijzing.
- **Alternatieve typen** — overwogen maar niet gekozen typen, elk met de reden.
- **Modelleerbesluit** — welk(e) type(n) voorgesteld/gekozen en waarom; bij afwijzing: waarom dit begrip geen element wordt. Dit is de kern van de pagina.
- **Voorgestelde definitie** — de definitie met herkomst: letterlijke bronformulering (met verwijzing) of eigen synthese (dan gemarkeerd als zodanig).
- **Voorgestelde relaties** — tabel: relatietype | element | beschrijving | bron.

## Vuistregels

- Stub na extractie (stap 3): frontmatter + Context + eerste vindplaatsen volstaan; de overige secties volgen in stap 4–5.
- Elk criteriumoordeel en elke relatie draagt een bronverwijzing — geen onderbouwing zonder bron.
- Onzekerheid markeren (bijv. *ter discussie:* …), niet gokken.

Ingevulde voorbeelden in drie stadia: [../voorbeelden/kandidaten/](../voorbeelden/kandidaten/) — goedgekeurd ([omgevingsvergunning](../voorbeelden/kandidaten/omgevingsvergunning.md)), review ([omgevingsdienst](../voorbeelden/kandidaten/omgevingsdienst.md)), kandidaat ([toezichthouder](../voorbeelden/kandidaten/toezichthouder.md)).
