Controleer bestaande elementen inhoudelijk of spoor ontbrekende elementen op: $ARGUMENTS

Input: modus (`definities` | `duplicaten` | `werkvoorraad`) + optioneel scope (onderwerp, beleidsdomein of elementtype BO/actor/rol); leeg = alle drie modi, hele wiki.
Output: chat-rapportage; modus `definities` kan na akkoord direct `bo_definitie`/`bo_toelichting` herschrijven. Draait op `Wiki/Bedrijfsobjecten/` + `Wiki/Actoren/` + `Wiki/Rollen/` (zelfde frontmatter-schema, zie `write-element.md` Stap 11).

Drie inhoudelijke controle-modi — alles wat objectief telbaar/parseerbaar is zit in `/lint`, niet hier. Deze skill oordeelt; `/lint` telt.

## Modus: definities

Controleert `bo_definitie` en `bo_toelichting` inhoudelijk. Vormfouten (leeg veld, placeholder "gelijk aan GGM", lengte/zinsaantal via [VR3]) worden al door `/lint` gemeld — deze modus behandelt de inhoud.

### Stap 1: Elementen verzamelen

Verzamel alle BO-/actor-/rolpagina's in scope. Lees per element het frontmatter.

### Stap 2: Per element controleren

#### 2a. GGM-vergelijking (bij grondslag `ggm-entiteit` of `ggm-afgeleid`)

Vergelijk `bo_definitie` met `ggm_definitie` en de bronnen in `Wiki/Bronsamenvattingen/` (via de `## Bronnen`-sectie van het element).

Classificeer het scenario:

| Scenario | Herkenning | Verwacht resultaat |
|---|---|---|
| **GGM overgenomen** | `bo_definitie` is (nagenoeg) gelijk aan `ggm_definitie` | OK als GGM qua strekking klopt met bronnen |
| **GGM aangepast zonder reden** | `bo_definitie` wijkt af van `ggm_definitie`, maar GGM klopt wél met bronnen | Fout: GGM-definitie had overgenomen moeten worden |
| **GGM terecht afgeweken** | `bo_definitie` wijkt af, GGM klopt niet met bronnen, body bevat **BO-definitie** sectie | OK |
| **GGM afgeweken zonder documentatie** | `bo_definitie` wijkt af, maar geen **BO-definitie** body-sectie | Fout: afwijking niet gedocumenteerd |
| **GGM onvolledig** | `bo_definitie` = GGM, maar aanvulling ontbreekt in `bo_toelichting` terwijl bronnen meer info bevatten | Waarschuwing: overweeg `bo_toelichting` |

#### 2b. Broncontrole (bij grondslag `procesobject`/`governance-object`, of zonder GGM-match)

Controleer of `bo_definitie` herleidbaar is naar de gelinkte bronsamenvattingen. Als een bron een letterlijke definitie bevat, had die overgenomen moeten worden.

#### 2c. bo_toelichting

| Check | Criterium |
|---|---|
| Veld bestaat | `bo_toelichting` in frontmatter (mag leeg zijn) |
| Inhoud gebaseerd op bronnen | Geen vrij verzonnen uitleg of voorbeelden |

### Stap 3: Rapportage

Per element: naam (wiki-link), elementtype (BO/actor/rol), scenario, status (OK/Fout/Waarschuwing), bevinding (kort). Groepeer op status: eerst fouten, dan waarschuwingen, dan OK. Toon samenvattende tellingen: totaal gecontroleerd, fouten, waarschuwingen, OK.

### Stap 4: Herstel

Na rapportage: bied aan om de fouten te herstellen. Pas per element `bo_definitie`/`bo_toelichting` opnieuw af volgens [VR3] en de regels in `/write-element` Stap 5. Lees de bronsamenvattingen en GGM-definitie, doorloop de scenario's, en schrijf het resultaat terug. Voer herstel per element uit en toon wat is gewijzigd.

## Modus: duplicaten

Retroactieve correctie van naamconflicten loopt altijd via deze modus, nooit via een eenmalige bulk-actie. Regels voor duplicaten en homoniemen: `/write-element` Stap 0 en 4b. Symmetrie van `bo_homoniemen` en veldcompleetheid van `bo_synoniemen` worden al door `/lint` gemeld — deze modus doet de semantische classificatie (is dit hetzelfde concept of niet) die geen script kan doen.

### Stap 1: Inventarisatie

1. Lijst alle elementbestanden in scope met `naam`, `ggm_entiteit`, `ggm_guid`, `ggm_beleidsdomein`, `bo_synoniemen`, `bo_homoniemen` en `ggm_duplicaat_entiteiten` uit frontmatter.
2. Laad GGM-data uit `Sources/GGM-repository/ggm_parsed.json`.

### Stap 2: Duplicaat-bestandsnamen detecteren

Zoek bestanden met dezelfde bestandsnaam in verschillende domeinfolders. Dit zijn potentiële homoniemen. Per match: controleer of `bo_homoniemen` al gevuld is. Zo niet → signaleer.

### Stap 3: GGM-naamconflicten detecteren

Voor elk element met grondslag `ggm-entiteit`:
1. Zoek in `ggm_parsed.json` naar alle entiteiten met dezelfde naam als `ggm_entiteit`.
2. Bij meerdere voorkomens: **Duplicaat-check** (hetzelfde concept in een ander beleidsdomein? `ggm_duplicaat_entiteiten` al gevuld?) en **Homoniem-check** (ander concept? `bo_homoniemen` al gevuld?).
3. Signaleer ontbrekende documentatie.

### Stap 4: Rapportage

Per ongedocumenteerd naamconflict: elementnaam en pad, GGM-entiteitnaam, conflicterende entiteit (naam, GUID, beleidsdomein), type (duplicaat/homoniem), voorstel (frontmatter vullen, hernoemen, samenvoegen). Vraag de gebruiker om beoordeling per bevinding voordat correcties worden doorgevoerd.

## Modus: werkvoorraad

Spoort ontbrekende actor- en rolpagina's op — BO-hiaten dekt `/entiteitendekking` al. Vindt alleen de werkvoorraad; beoordeling en vastlegging gebeuren via `/element-pipeline`. Definities en criteria: [[Wiki/GEMMA/actoren-en-rollen|Actoren en rollen]].

### Track 1: GGM-geankerde kandidaten (goedkoop, geen bronnen nodig)

1. Doorzoek `Wiki/Analyses/entiteitendekking/` op tabelrijen met Entiteitstype `actor` of `rol` en BO/Dekking `⚠️ geen actor-pagina` of `⚠️ geen rol-pagina` — met grep/script, zonder LLM.
2. Dedupliceer op GGM-entiteitnaam; sla kandidaten over die al een pagina hebben (check `ggm_entiteit`/`ggm_guid` in frontmatter).
3. Resultaat: kandidatenlijst met GGM-entiteit, GUID, taakveld/beleidsdomein en de rapportregel als context.

### Track 2: Niet-GGM kandidaten uit bronsamenvattingen (zwaarder, gebatcht)

1. Scan `Wiki/Bronsamenvattingen/` per onderwerp-map op genoemde actoren/rollen zonder GGM-entiteit (governance-hiaten, bv. heffingsambtenaar/invorderingsambtenaar).
2. **Batch per onderwerp-map, niet per bestand.** Bij delegatie aan subagents: golven van max 3-4 agents tegelijk, elk een cluster van 5-8 onderwerpen. Na elke golf een tussenstand melden.
3. Per kandidaat: naam, type-vermoeden, bronsamenvatting(en), gemeentelijk perspectief (externe context uitsluiten).
4. Sla kandidaten over die al een pagina hebben (naam-check in `Wiki/Actoren/`, `Wiki/Rollen/` en `bo_synoniemen`).

### Beoordeling en vastlegging

1. `/element-pipeline {kandidaat}` — orchestreert beoordeling en vastlegging.
2. Kandidaten die het gemeentelijk perspectief niet halen: niet vastleggen, wel vermelden met reden.

### Nazorg

- Onderwerpoverzichten bijwerken (begrippentabel: begripstype actor/rol invullen waar de sweep dat heeft vastgesteld)
- `Wiki/index.md` — secties Actoren en Rollen aanvullen
- `Wiki/log.md` — één samenvattende entry met aantallen (kandidaten gevonden / pagina's aangemaakt / afgewezen met reden)

### Rapportage

Tabel: kandidaat | track | actor/rol | pagina aangemaakt? | ook BO? | opmerking.
