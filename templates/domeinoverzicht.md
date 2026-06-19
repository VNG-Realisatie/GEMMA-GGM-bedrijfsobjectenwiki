# Template: Domeinoverzicht

Locatie: `Wiki/Domeinen/{domeinnaam}.md`

## Frontmatter

```yaml
---
type: domein
naam: {domeinnaam}
status: {afgerond | in-behandeling | niet-gestart}
verwerkingsdatum: {datum laatste verwerking}
bronnen_count: {aantal verwerkte bronnen}
begrippen_count: {aantal geidentificeerde begrippen}
bo_count: {aantal bedrijfsobjecten}
---
```

## Body

Het domeinoverzicht is de **centrale werkpagina** per domein. Het bevat alle begrippen als tabel — geen aparte begrippenpagina's. Een domein wordt altijd afgetekend na verwerking — ook als de uitkomst 0 BO's is.

### Linkconventie

- **Begrippentabel kolom "Begrip":** `[[bedrijfsobject-naam]]` voor BO's, platte tekst voor niet-BO's
- **"Verwerkte bronnen":** `[[Wiki/Bronsamenvattingen/{domein}/{slug}|display-tekst]]`
- **"Nog te verwerken bronnen":** gebruik markdown-links naar Sources/ (omdat dat geen wiki-pagina's zijn)
- **"Terugmeldingen":** `[[Wiki/Analyses/ggm-terugmeldingen|link naar terugmeldingen]]`

### Secties

- **Korte beschrijving** van het gemeentelijk domein
- **Begrippentabel** — het hart van de pagina:

```markdown
| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[woz-object]] | object | Onroerende zaak voor WOZ-waardering | ✅ | 6/6 criteria, exact match | Woning, kantoor | ja |
| belastingaanslag | object | Individuele vaststelling belastingbedrag | ✅ | 6/6 criteria, GGM-hiaat | OZB-aanslag 2025 | nee |
| heffingsmaatstaf | object | Maatstaf voor belastingschuld | ❌ | Eigenschap van verordening | WOZ-waarde | nee |
| belastingmix | thema | Gekozen combinatie belastingen | ❌ | Beleidsmatig, geen object | — | nee |
```

  - **Begrip**: `[[BO-naam]]` naar BO-pagina als het een BO is, anders platte tekst
  - **Type**: begripstype (object/instrument/actor/doelgroep/thema/doel/waarde)
  - **Omschrijving**: identiek aan de BO-definitie als het een BO is
  - **BO?**: ✅ of ❌
  - **Reden**: korte samenvatting waarom wel/niet (volledige onderbouwing staat in de BO-pagina)
  - **Voorbeelden**: concrete instanties
  - **GGM**: ja/nee — heeft dit begrip een GGM-entiteit

- **GGM-entiteitendekking** — overzichtstabel per GGM-beleidsdomein dat bij dit domein hoort:

```markdown
| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Monumenten | 6 | 1 | 5 | 0 | — |
| Archief | 8 | 1 | 4 | 3 | Geen beleidsbron over archieflogistiek |
| Archeologie | 17 | 0 | 0 | 17 | Geen beleidsbron; opgravingsdetails vermoedelijk te granulair |
```

  - **BO**: entiteit is als bedrijfsobject opgenomen
  - **Niet-BO**: entiteit is beoordeeld maar is geen BO (te granulair, classificatie, opslaglogistiek, etc.)
  - **Niet beoordeeld**: entiteit is niet beoordeeld omdat er geen beleidsbron voor is gevonden — dit zijn potentiële BO's die bij toekomstige bronnen alsnog beoordeeld moeten worden

  Deze tabel maakt zichtbaar waar de wiki **bewust onvolledig** is: veel GGM-entiteiten kunnen pas beoordeeld worden als er domeinspecifieke bronnen worden toegevoegd.

- **GGM-dekkingsanalyse**: proza-toelichting bij de tabel — welke patronen, welke subdomeinen zijn goed/slecht gedekt, structurele observaties
- **Verwerkte bronnen**: lijst met wiki-links naar [[Wiki/Bronsamenvattingen/{domein}/{slug}|bronsamenvattingen]]
- **Nog te verwerken bronnen**: lijst naar Sources/-bestanden (markdown-links)
- **Openstaande vragen of hiaten**
- **Terugmeldingen richting GGM**: link naar [[Wiki/Analyses/ggm-terugmeldingen]]
