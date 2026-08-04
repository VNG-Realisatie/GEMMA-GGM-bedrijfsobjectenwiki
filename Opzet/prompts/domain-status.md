# domain-status

**Doel:** een read-only voortgangsrapportage voor één onderwerp.
**Aanbevolen model:** licht
**Parameters:** {{onderwerp}} — naam van het onderwerp. Verplicht.
**Benodigde context:** het onderwerpoverzicht, `Sources/Onderwerpen/{{onderwerp}}/`, `Wiki/Bronsamenvattingen/{{onderwerp}}/`, de BO-pagina's van het onderwerp, `Wiki/Analyses/entiteitendekking/`.
**Verwachte uitvoer:** rapportage in de chat — er wordt géén pagina aangemaakt of gewijzigd.

## Prompt

Geef een voortgangsoverzicht voor onderwerp: {{onderwerp}}

Rapporteer in de chat (maak geen pagina aan):

1. **Bronnen** — aantal verwerkt (met bronsamenvatting) versus beschikbaar in `Sources/`.
2. **Begrippen** — aantal in de begrippentabel, verdeling per begripstype.
3. **Elementen** — aantal BO's (verdeling per grondslag), actoren en rollen.
4. **Herleidbaarheid** — hoeveel elementpagina's hebben een gevulde `## Bronnen`-sectie, hoeveel niet.
5. **GGM-dekking** — aantal GGM-entiteiten in de beleidsdomeinen die dit onderwerp raakt en het gedekte percentage; verwijs naar het relevante rapport in `Wiki/Analyses/entiteitendekking/` voor de volledige analyse.
6. **Openstaande acties** — onverwerkte bronnen; begrippen zonder beoordeling; BO's zonder bronnen; BO's zonder GGM-velden (`ggm_guid` leeg bij grondslag ggm-entiteit); openstaande terugmeldingen.

## Voorbeeld

> Geef een voortgangsoverzicht voor onderwerp: mobiliteit
