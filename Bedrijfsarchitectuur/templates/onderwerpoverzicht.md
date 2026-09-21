# Template: Onderwerpoverzicht

Locatie: `Wiki/Onderwerpoverzichten/{onderwerpnaam}.md`

## Frontmatter

```yaml
---
type: onderwerp
naam: {onderwerpnaam}
status: {afgerond | in-behandeling | niet-gestart}
verwerkingsdatum: {datum laatste verwerking}
bronnen_count: {aantal verwerkte bronnen}
begrippen_count: {aantal geidentificeerde begrippen}
bo_count: {aantal bedrijfsobjecten}
---
```

## Body

Het onderwerpoverzicht is de **centrale werkpagina** per onderwerp. Het bevat alle begrippen als tabel — geen aparte begrippenpagina's. Een onderwerp wordt altijd afgetekend na verwerking — ook als de uitkomst 0 BO's is.

### Linkconventie

- **Begrippentabel kolom "Begrip":** `[[Wiki/Bedrijfsobjecten/.../naam\|Leesbare naam]]` voor BO's (escaped pipe in tabellen), platte tekst voor niet-BO's
- **"Verwerkte bronnen":** `[[Wiki/Bronsamenvattingen/{onderwerp}/{slug}|display-tekst]]`
- **"Nog te verwerken bronnen":** gebruik markdown-links naar Sources/ (omdat dat geen wiki-pagina's zijn)
- **"Terugmeldingen":** `[[Wiki/Analyses/ggm-terugmeldingen|link naar terugmeldingen]]`

### Begripstypen

De kolom "Begripstype" in de begrippentabel heeft een van deze waarden:

| Begripstype | Omschrijving | ArchiMate-elementtype |
|---|---|---|
| **object** | Concreet ding dat in processen wordt gebruikt/geproduceerd | Business Object |
| **governance-instrument** | Regeling, programma, wet, maatregel, verordening | Contract / Product |
| **actor** | Persoon, organisatie of organisatorische eenheid die kan handelen | Business Actor |
| **rol** | Verantwoordelijkheid voor specifiek gedrag, door een actor vervulbaar | Business Role |
| **doelgroep** | Groep waarop beleid of uitvoering gericht is | Business Object (classificatie) |
| **thema** | Werkgebied dat doelen, actoren en instrumenten bundelt | Grouping |
| **doel** | Nagestreefde situatie of uitkomst | Goal / Outcome |
| **waarde** | Maatschappelijk ideaal, richtinggevend principe | Driver / Principle |

De BO-filterlogica (welke typen BO-kandidaat zijn) en beoordelingscriteria staan in `/assess-element`.

### Secties

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

  - **Begrip**: `[[BO-naam]]` naar BO-pagina als het een BO is, anders platte tekst
  - **Begripstype**: begripstype uit `/assess-element` (object, governance-instrument, actor, rol, doelgroep, thema, doel, waarde)
  - **Omschrijving**: identiek aan de BO-definitie als het een BO is
  - **BO?**: ✅ of ❌
  - **Data-object**: ja/nee — wordt dit begrip als zelfstandige entiteit vastgelegd in een informatiesysteem (eigen attributen)? Onafhankelijke classificatie naast BO?: een begrip kan BO=❌ maar Data-object=ja zijn (te granulair voor BO, wél geregistreerd), of BO=✅ maar Data-object=nee (governance-object). Data-objecten met GGM=nee zijn de sterkste kandidaten voor GGM-hiaten.
  - **Reden**: korte samenvatting waarom wel/niet (volledige onderbouwing staat in de BO-pagina)
  - **Voorbeelden**: concrete instanties
  - **GGM**: ja/nee — heeft dit begrip een GGM-entiteit

- **Verwerkte bronnen**: lijst met wiki-links naar [[Wiki/Bronsamenvattingen/{onderwerp}/{slug}|bronsamenvattingen]]
- **Nog te verwerken bronnen**: lijst naar Sources/-bestanden (markdown-links)
- **Openstaande vragen of hiaten**
- **Terugmeldingen richting GGM**: link naar [[Wiki/Analyses/ggm-terugmeldingen]]
