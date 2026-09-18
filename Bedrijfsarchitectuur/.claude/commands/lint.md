Voer een consistentiecheck uit op de wiki. Scope: $ARGUMENTS (leeg = hele wiki, anders = opgegeven onderwerp).

Twee stappen: eerst een script voor alles wat objectief telbaar is, dan een modelbeoordeling voor wat context vereist. Output: één chat-rapportage.

## Stap 1 — Script

```
python3 tools/lint_checks.py $ARGUMENTS
```

Zonder argument = hele wiki; met een onderwerp-substring worden BO/Actor/Rol-pagina's op `onderwerp:`/pad gefilterd (cross-cutting checks als wees-BO's, dubbele bestandsnamen en de `Begrippen/`-directory blijven altijd wiki-breed).

Dekt: Bronnen-secties (aanwezigheid, format, dode Sources-links), frontmatter-compleetheid en enum-validatie, `ggm_guid`-validatie tegen `ggm_parsed.json`, `bo_definitie`-geldigheid, `bo_relaties`-structuur, subtypes frontmatter↔body-consistentie, `ggm_duplicaat_entiteiten`-schema en -sectieconsistentie, homoniemen/synoniemen-compleetheid en -symmetrie, wees-BO's, `Wiki/Begrippen/`-verbod, verplichte wiki-link-aliassen, dubbele bestandsnamen, verboden GGM-dekkingssecties, begrippentabel-format. Zie de docstring in het script voor de precieze lijst.

Neem de output 1-op-1 over — niet hertellen of herformuleren.

**Fixes:**
- Mechanisch veilig (elk verifieert zijn eigen schrijfactie voor commit) → `python3 tools/lint_checks.py --fix $ARGUMENTS`: strip aliassen uit `## Bronnen`-links, lost dode `[[Sources/...]]`-links op (alleen bij een eenduidige kandidaat), werkt `ggm_duplicaat_entiteiten` bij van platte GUID-lijst naar het dict-schema (via `ggm_parsed.json`), en vult een ontbrekende `ggm_entiteit`/`ggm_guid` in een `bo_homoniemen`-item aan vanuit de eigen frontmatter van het genoemde `bedrijfsobject`-target (alleen als die pagina bestaat en die data zelf heeft).
- **Niet mechanisch, ondanks dat het op "data-omissie" lijkt:** `bo_relaties` zonder kardinaliteit (geen bron om uit te lenen — vereist een keuze), `bo_homoniemen` zonder `bedrijfsobject` (meestal bestaat de doelpagina nog niet), `bo_homoniemen`-eenzijdigheid (het bronbestand heeft zelf vaak geen eigen GGM-identiteit om terug te spiegelen), `## GGM-duplicaten`-sectie genereren (alle 14 bestaande secties bevatten een "primair vs. duplicaat"-redenering en een terugmelding-verwijzing — een kale sectie zonder die twee zou de conventie doorbreken). Deze categorieën aan de gebruiker voorleggen, niet scripten.
- Frontmatter-stijl (quotes, lege waarden) → `python3 tools/migrate_frontmatter_style.py --dry-run`, dan zonder flag.
- Overige bevindingen (grondslag/ggm_guid, bo_definitie, bo_relaties-velden, subtypes-mismatch, homoniemen) vereisen inhoudelijke kennis — voorleggen aan de gebruiker of via `/write-element`/`/assess-element`, niet blind fixen.

## Stap 2 — Modelbeoordeling (op Haiku)

Alleen wat het script signaleert maar niet kan duiden, plus wat inherent semantisch is:

- **Anti-patroon registr\*** — script levert kandidaatregels ("registreerbaar"/"registratieobject"); beoordeel per regel of het als afwijsgrond tegen de 6 BO-criteria wordt gebruikt (overtreding) of legitiem taalgebruik is.
- **`bo_relaties`-incompleetheid** — ontbrekende kardinaliteit of `bedrijfsobject` zonder wiki-link: omissie (fix) of bewust (relatie naar concept zonder eigen BO-pagina)?
- **Wees-BO's** — terecht (nog niet verwerkt) of omissie in een onderwerpoverzicht?
- **Subtypes-mismatch** — moet het begrip een eigen BO-pagina zijn i.p.v. subtype?
- **Begrippentabel → BO** — begrippen met BO?=❌ waarvan de Reden een subtype-patroon bevat ("subtype van", "onderdeel van", "specialisatie van", "valt onder", "categorie van", "variant van") die niet als `bo_subtypes` of in een Subtypes/Specialisaties-tabel bij het genoemde parent-BO staan. Alleen bij bestaand parent-BO; "onderdeel van" vangt ook composities — handmatig beoordelen.
- **Generalisatie/Specialisaties-symmetrie**, dode links in `## Generalisatie`, volledigheid van `Wiki/Analyses/ggm-dekking.md`, analyse-links, terugmeldingen-consistentie (`⚠️ ter discussie` ↔ `Wiki/Analyses/ggm-terugmeldingen.md`), duplicaat-/homoniem-terugmelding, naamkeuze-consistentie — nog niet gescript, handmatig/steekproefsgewijs controleren.
- **Tegenstrijdige definities**, contradicties tussen pagina's, verouderde claims — semantisch, altijd modelwerk.

## Rapportage

Eén rapport, gesorteerd op ernst (herleidbaarheid > ontbrekende data > inconsistenties > suggesties). Markeer elke regel met **[script]** of **[model]**, met totaaltelling per bron.
