# Architectuur: mappenstructuur

De projectinhoud staat in `Bedrijfsarchitectuur/`:

```
Bedrijfsarchitectuur/
├── Sources/                    # immutabele bronnen (inhoud nooit wijzigen)
│   ├── Onderwerpen/            # beleidsdocumenten per gemeentelijk onderwerp
│   │   └── {onderwerp}/
│   ├── GGM/                    # leesbare weergave van het GGM (gegenereerd uit XMI)
│   │   ├── structuur-ggm.md    # overzicht taakvelden en beleidsdomeinen
│   │   └── {taakveld}/         # per taakveld, bestanden per beleidsdomein
│   ├── GGM-repository/         # GGM-bronbestanden
│   │   ├── Gemeentelijk Gegevensmodel XMI2.1.xml   # de bron van waarheid
│   │   └── ggm_parsed.json     # geparsed XMI: GUIDs, GEMMA-tags, relaties
│   ├── GEMMA/                  # GEMMA-referentiemateriaal
│   ├── Standaarden/            # standaarden en specificaties
│   ├── informatiebeheer/       # vaste uitzondering (zie bronnen.md)
│   └── informatiesystemen/     # vaste uitzondering (zie bronnen.md)
├── Wiki/                       # afgeleide kennisbasis (door de LLM onderhouden)
│   ├── index.md                # inhoudelijk overzicht van alle pagina's
│   ├── log.md                  # chronologisch logboek van alle acties
│   ├── Onderwerpoverzichten/   # begrippentabellen per onderwerp
│   ├── Bedrijfsobjecten/       # BO-pagina's per {taakveld}/{beleidsdomein}/
│   ├── Actoren/                # actor-pagina's (platte map)
│   ├── Rollen/                 # rol-pagina's (platte map)
│   ├── Bronsamenvattingen/     # samenvattingen per bron, per {onderwerp}/
│   ├── GGM/                    # gegenereerde GGM-weergave (nooit handmatig bewerken)
│   ├── GEMMA/                  # GEMMA-referentiepagina's (o.a. actoren-en-rollen.md)
│   └── Analyses/               # dekkingsrapporten, terugmeldingen, syntheses
├── templates/                  # paginatemplates (zie paginatypes.md)
├── tools/                      # Python-scripts (zie ../tools/README.md)
├── exports/                    # gegenereerde GGM-GEMMA CSV's
├── ToDo/                       # backlogs (o.a. ingest-backlog.md)
└── Clippings/                  # landingszone webclipper — geen bron, wordt geleegd
```

## Vuistregels

- **Onderwerpen en taakvelden ontstaan bij het verwerken van bronnen** — ze worden niet vooraf aangemaakt. Controleer altijd bestaande submappen voordat je een nieuwe aanmaakt.
- **Sources = invoer, Wiki = uitvoer.** Alles wat de LLM schrijft gaat naar `Wiki/`; de herleidbaarheidsketen loopt van Sources via Bronsamenvattingen naar Bedrijfsobjecten (zie [project.md](project.md)).
- **`Wiki/GGM/` is gegenereerd** — regenereren via de GGM-pipeline ([../prompts/generate-ggm.md](../prompts/generate-ggm.md)), nooit handmatig bewerken.
- **`Wiki/Analyses/entiteitendekking/`** bevat de scriptgegenereerde dekkingsrapporten; alleen de beoordelingssecties zijn handwerk.
