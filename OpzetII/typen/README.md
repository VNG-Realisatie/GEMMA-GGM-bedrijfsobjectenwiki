# Typekaders

Eén bestand per ArchiMate-elementtype: het toetsingskader. Twee processtappen gebruiken deze bestanden:

- **Type-extractie** (stap 3) gebruikt de sectie *Herkenning* om kandidaten in bronnen te vinden;
- **Beoordeling** (stap 5) gebruikt de sectie *Criteria* om een kandidaat per type te toetsen en *Afbakening* om alternatieve typen te wegen.

## Huidige typen

| Bestand | ArchiMate-type | Kern |
|---|---|---|
| [business-object.md](business-object.md) | Business Object | waarover informatie wordt vastgelegd |
| [business-actor.md](business-actor.md) | Business Actor | zelfstandige partij die gedrag uitvoert |
| [business-role.md](business-role.md) | Business Role | verantwoordelijkheid of positie, vervulbaar door meerdere actoren |
| [business-process.md](business-process.md) | Business Process | geordende activiteiten met trigger en resultaat |
| [business-function.md](business-function.md) | Business Function | stabiele capaciteit, organisatie-onafhankelijk |

## Bestandsformat

```markdown
# {Typenaam}
**ArchiMate-type:** {officiële naam}
**Exportcode:** {typecode voor elementen.csv, bijv. BusinessObject}

{één zin: wat dit type is}

## Herkenning
{signaalvragen en -woorden waarmee extractie kandidaten in bronnen vindt}

## Criteria
{genummerde tabel met toetsvragen; vermeld welke criteria verplicht zijn}

## Afbakening
{verwante typen en hoe je kiest, met links naar hun kaders}
```

## Een type toevoegen

1. Maak `typen/{type-slug}.md` volgens het format hierboven (slug lowercase-kebab-case, gelijk aan de `typen[].type`-waarde in kandidaat-frontmatter).
2. Voeg het type toe aan de tabel hierboven.
3. Vul waar relevant `relevante_typen:` aan op bestaande topic-pagina's, zodat de extractie het meeneemt.

Meer is niet nodig: de prompts itereren over de bestanden in deze map en zijn niet aan specifieke typen gebonden. Zo is uitbreiding naar andere ArchiMate-typen (Business Service, Product, Contract, Application Component, …) een kwestie van één bestand.
