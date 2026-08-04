# Template: Onderwerpoverzicht

Locatie: `Wiki/Onderwerpoverzichten/{onderwerpnaam}.md`

Het onderwerpoverzicht is de **centrale werkpagina** per onderwerp: alle begrippen in één tabel, geen aparte begrippenpagina's. Een onderwerp wordt altijd afgetekend na verwerking — ook bij 0 BO's.

## Frontmatter

```yaml
---
type: onderwerp
naam: {onderwerpnaam}
status: {afgerond | in-behandeling | niet-gestart}
verwerkingsdatum: {datum laatste verwerking}
bronnen_count: {aantal verwerkte bronnen}
begrippen_count: {aantal geïdentificeerde begrippen}
bo_count: {aantal bedrijfsobjecten}
---
```

## Body

- **Korte beschrijving** van het gemeentelijk onderwerp
- **Begrippentabel** — het hart van de pagina:

```markdown
| Begrip | Begripstype | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | object | Onroerende zaak voor WOZ-waardering | ✅ | ja | 6/6 criteria, exact match | Woning, kantoor | ja |
| belastingaanslag | object | Individuele vaststelling belastingbedrag | ✅ | ja | 6/6 criteria, GGM-hiaat | OZB-aanslag 2025 | nee |
| heffingsmaatstaf | object | Maatstaf voor belastingschuld | ❌ | ja | Eigenschap van verordening | WOZ-waarde | nee |
| belastingmix | thema | Gekozen combinatie belastingen | ❌ | nee | Beleidsmatig, geen object | — | nee |
```

  - **Begrip** — wiki-link naar de elementpagina als het een element is (in de tabel met escaped pipe), anders platte tekst
  - **Begripstype** — een van de acht typen uit de beoordeling: object, governance-instrument, actor, rol, doelgroep, thema, doel, waarde (zie de prompt assess-element voor de definities)
  - **Omschrijving** — identiek aan de definitie als het een element is
  - **BO?** — ✅ of ❌
  - **Data-object** — ja/nee: wordt dit begrip als zelfstandige entiteit met eigen attributen vastgelegd in een informatiesysteem? Onafhankelijk van de BO-kolom; data-objecten met GGM=nee zijn de sterkste hiaatkandidaten
  - **Reden** — korte samenvatting van het oordeel (de volledige onderbouwing staat op de elementpagina)
  - **Voorbeelden** — concrete instanties
  - **GGM** — ja/nee: heeft dit begrip een GGM-entiteit

- **Verwerkte bronnen** — wiki-links naar de bronsamenvattingen: `[[Wiki/Bronsamenvattingen/{onderwerp}/{slug}|display-tekst]]`
- **Nog te verwerken bronnen** — markdown-links naar `Sources/`-bestanden (geen wiki-pagina's)
- **Openstaande vragen of hiaten**
- **Terugmeldingen richting GGM** — link naar `[[Wiki/Analyses/ggm-terugmeldingen|ggm-terugmeldingen]]`
