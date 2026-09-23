---
model: haiku
---

Voer een consistentiecheck uit op de wiki. Scope: $ARGUMENTS (leeg = hele wiki, anders = opgegeven onderwerp).

Twee stappen: eerst een script voor alles wat objectief telbaar is, dan een modelbeoordeling voor wat context vereist. Output: één chat-rapportage.

## Stap 1: Script

```
python3 tools/lint_checks.py $ARGUMENTS
```

Zonder argument = hele wiki; met een onderwerp-substring worden BO/Actor/Rol-pagina's op `onderwerp:`/pad gefilterd (cross-cutting checks als wees-BO's, dubbele bestandsnamen en de `Begrippen/`-directory blijven altijd wiki-breed).

Dekt: Bronnen-secties (aanwezigheid, format, dode Sources-links, platte-tekst Sources-referenties i.p.v. wiki-link), map-naam-consistentie Sources/Onderwerpen ↔ Wiki/Bronsamenvattingen (hoofdletter-only mismatch), frontmatter-compleetheid en enum-validatie, `ggm_guid`-validatie tegen `ggm_parsed.json`, `bo_definitie`-geldigheid (leeg veld, placeholder "gelijk aan GGM"), `bo_relaties`-structuur, subtypes frontmatter↔body-consistentie, `ggm_duplicaat_entiteiten`-schema en -sectieconsistentie, homoniemen/synoniemen-compleetheid en -symmetrie (incl. `bo_homoniemen`-eenzijdigheid), wees-BO's, wees-bedrijfsfuncties/-processen (`Wiki/Bedrijfsfuncties/`/`Wiki/Bedrijfsprocessen/`-pagina's die door geen element worden genoemd), `bedrijfsprocessen`/`bedrijfsfuncties`-velden die nog vrije tekst zijn i.p.v. wiki-link of die dood wiki-linken, bronsamenvattingen die niet in een onderwerpoverzicht zijn verwerkt, een samengestelde end-to-end traceability-check per BO (onderwerpoverzicht → Bronnen-sectie → geldige Sources-link), `Wiki/Begrippen/`-verbod, verplichte wiki-link-aliassen, dubbele bestandsnamen, verboden GGM-dekkingssecties, begrippentabel-format, regelverwijzingen (`[ID]` in skills/templates/rules bestaan, IDs uniek, geen verboden zinnen; zie `FORBIDDEN_PHRASES` in het script). Zie de docstring in het script voor de precieze lijst.

**`bedrijfsprocessen`/`bedrijfsfuncties`-migratie:** deze velden hoorden vóór 2026-09-23 vrije tekst te zijn; sinds dat besluit horen ze wiki-links te zijn naar `Wiki/Bedrijfsfuncties/`/`Wiki/Bedrijfsprocessen/`-pagina's (zie CLAUDE.md BO12, `templates/element.md`). De grote hoeveelheid "vrije tekst"-bevindingen die dit oplevert is bestaande achterstand, geen regressie — NIET in bulk vervangen door lege of geraden wiki-links. Nieuwe functies/processen ontstaan via `/assess-element` + `/write-element` (zelfde flow als een BO); bestaande vrije-tekstvermeldingen migreren pas zodra de onderliggende functie/proces inhoudelijk is beoordeeld.

Neem de output 1-op-1 over — niet hertellen of herformuleren.

**Fixes:**
- Mechanisch veilig (elk verifieert zijn eigen schrijfactie voor commit) → `python3 tools/lint_checks.py --fix $ARGUMENTS`: strip aliassen uit `## Bronnen`-links, lost dode `[[Sources/...]]`-links op (alleen bij een eenduidige kandidaat), werkt `ggm_duplicaat_entiteiten` bij van platte GUID-lijst naar het dict-schema (via `ggm_parsed.json`), en vult een ontbrekende `ggm_entiteit`/`ggm_guid` in een `bo_homoniemen`-item aan vanuit de eigen frontmatter van het genoemde `bedrijfsobject`-target (alleen als die pagina bestaat en die data zelf heeft).
- **Niet mechanisch, ondanks dat het op "data-omissie" lijkt:** `bo_relaties` zonder kardinaliteit (geen bron om uit te lenen — vereist een keuze), `bo_homoniemen` zonder `bedrijfsobject` (meestal bestaat de doelpagina nog niet), `bo_homoniemen`-eenzijdigheid (het bronbestand heeft zelf vaak geen eigen GGM-identiteit om terug te spiegelen), `## GGM-duplicaten`-sectie genereren (alle 14 bestaande secties bevatten een "primair vs. duplicaat"-redenering en een terugmelding-verwijzing — een kale sectie zonder die twee zou de conventie doorbreken). Deze categorieën aan de gebruiker voorleggen, niet scripten.
- Frontmatter-stijl (quotes, lege waarden) → `python3 tools/migrate_frontmatter_style.py --dry-run`, dan zonder flag.
- Overige bevindingen (grondslag/ggm_guid, bo_definitie-inhoud, bo_relaties-velden, subtypes-mismatch, homoniemen) vereisen inhoudelijke kennis — voorleggen aan de gebruiker of via `/write-element`/`/audit-element`, niet blind fixen.

## Stap 2: Modelbeoordeling

Alleen wat het script signaleert maar niet kan duiden, plus wat inherent semantisch is:

- **Anti-patroon registr\*** ([BO1]–[BO3]) — script levert kandidaatregels ("registreerbaar"/"registratieobject"); beoordeel per regel of het als afwijsgrond tegen de 6 BO-criteria wordt gebruikt (overtreding) of legitiem taalgebruik is.
- **`bo_relaties`-incompleetheid** — ontbrekende kardinaliteit of `bedrijfsobject` zonder wiki-link: omissie (fix) of bewust (relatie naar concept zonder eigen BO-pagina)?
- **Wees-BO's** — terecht (nog niet verwerkt) of omissie in een onderwerpoverzicht?
- **Subtypes-mismatch** — moet het begrip een eigen BO-pagina zijn i.p.v. subtype?
- **Begrippentabel → BO** — begrippen met BO?=❌ waarvan de Reden een subtype-patroon bevat ("subtype van", "onderdeel van", "specialisatie van", "valt onder", "categorie van", "variant van") die niet als `bo_subtypes` of in een Subtypes/Specialisaties-tabel bij het genoemde parent-BO staan. Alleen bij bestaand parent-BO; "onderdeel van" vangt ook composities — handmatig beoordelen.
- **Generalisatie/Specialisaties-symmetrie**, dode links in `## Generalisatie`, volledigheid van `Wiki/Analyses/ggm-dekking.md`, analyse-links, terugmeldingen-consistentie (`⚠️ ter discussie` ↔ `Wiki/Analyses/ggm-terugmeldingen.md`), duplicaat-/homoniem-terugmelding, naamkeuze-consistentie — nog niet gescript, handmatig/steekproefsgewijs controleren.
- **`bo_definitie`-vormcriteria** ([VR3]: lengte, zinsaantal) — nog niet gescript (het script checkt alleen leeg veld en de letterlijke placeholder "gelijk aan GGM").
- **`bo_synoniemen`-volledigheid** — staat `ggm_entiteit`/`ggm_gemma_alternate_name` in `bo_synoniemen` als die afwijkt van `naam`? Nog niet gescript (het script checkt alleen dat bestaande items een `naam`/`context` hebben, niet of een item ontbreekt).
- **Tegenstrijdige definities**, contradicties tussen pagina's, verouderde claims — semantisch, altijd modelwerk.

## Verificatie van bevindingen

- Verifieer gemelde bevindingen zelf (grep/Read/eigen script) vóór ze in het eindrapport komen, voor élke categorie, ook telbare/structurele claims.
- Vertrouw NOOIT een getal of "aanwezig/afwezig"-claim van het model zonder eigen deterministische verificatie (grep/Python-script over de volledige set). Een steekproef van 2–3 voorbeelden volstaat niet voor aggregaat-tellingen; voor semantische bevindingen volstaat een steekproef.
- Structureel/telbare checks (veldnaam-gebruik, sectie-aanwezigheid, link-tellingen, orphan-detectie) horen in `tools/lint_checks.py`, niet bij het model. Precedent 2026-09-17: het model meldde 344 (werkelijk 0), 381 (werkelijk 2) en 1.123 (werkelijk 46).

## Rapportage

Eén rapport, gesorteerd op ernst (herleidbaarheid > ontbrekende data > inconsistenties > suggesties). Markeer elke regel met **[script]** of **[model]**, met totaaltelling per bron.
