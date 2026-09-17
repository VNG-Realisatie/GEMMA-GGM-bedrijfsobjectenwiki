Voer een consistentiecheck uit op de wiki. Scope: $ARGUMENTS (leeg = hele wiki, anders = opgegeven onderwerp).

Input: hele wiki of opgegeven onderwerp.
Output: chat-rapportage; fixes op aanwijzing (zie tools hieronder per categorie).

## Waarom dit commando in twee stappen werkt

Een `/lint`-run op Haiku (2026-09-17) hallucineerde op precies de telbare/structurele checks: "344 bestanden met veld `domein:`" bleek 0, "381 wees-BO's" bleek 6, "1.123 wiki-links zonder alias" bleek 46 (zie `Wiki/log.md`, entry 2026-09-17). Alles wat objectief telbaar of greppbaar is, hoort daarom bij een **script**, niet bij een LLM-narratief. Wat overblijft — context beoordelen, "is dit terecht", contradicties, verouderde claims — hoort wél bij het model.

## Stap 1 — Deterministische checks (altijd eerst, geen model nodig)

```
python3 tools/lint_checks.py $ARGUMENTS
```

(zonder argument = hele wiki; met een onderwerp-substring worden alleen BO/Actor/Rol-pagina's met dat `onderwerp:` of pad gefilterd — cross-cutting checks zoals wees-BO's, dubbele bestandsnamen en Begrippen/-directory blijven wiki-breed, dat is inherent).

Het script dekt: BO/bronsamenvatting-Bronnen-secties (aanwezigheid, format, dode Sources-links), frontmatter-compleetheid (grondslag, ggm_entiteit/ggm_guid, enum-validatie tegen `templates/element.md`, verkeerde map voor actor/rol), ggm_guid-validatie tegen `ggm_parsed.json`, `bo_definitie`-geldigheid, `bo_relaties`-structuur, subtypes frontmatter↔body-consistentie, `ggm_duplicaat_entiteiten`-schema en sectie-consistentie, homoniemen/synoniemen-compleetheid en -symmetrie, wees-BO's, `Wiki/Begrippen/`-verbod, verplichte wiki-link-aliassen, dubbele bestandsnamen, verboden GGM-dekkingssecties in onderwerpoverzichten, begrippentabel-format (Data-object-kolom, lege BO?-kolom). Zie de docstring in het script zelf voor de precieze lijst — die twee documenten (script + dit bestand) moeten in sync blijven; als je hier een check aanpast, pas het script aan en andersom.

Neem de output 1-op-1 over in de rapportage — niet hertellen, niet herformuleren. Het script is getest tegen de wiki en de tellingen zijn exact.

**Fixes voor stap-1-bevindingen:**
- Frontmatter-stijl (lege waarden, quote-stijl, `bedrijfsobject: [[...]]` zonder quotes) → `python3 tools/migrate_frontmatter_style.py --dry-run` ter preview, dan zonder flag.
- Aliassen in `## Bronnen`-secties → geen bestaand script; schrijf een gericht eenmalig script zoals op 2026-09-17 (zie log), of vraag het opnieuw.
- `ggm_duplicaat_entiteiten` oud schema (platte GUID-string i.p.v. dict) → GUID opzoeken in `ggm_parsed.json` (`entities[guid]['name'/'beleidsdomein'/'taakveld']`) en omzetten naar het dict-schema; `afwijkende_attributen` blanco laten. Verifieer na afloop dat de GUID's voor en na identiek zijn (voorkomt dataverlies).
- Overige bevindingen (missing grondslag/ggm_guid, bo_definitie, bo_relaties-velden, subtypes-mismatch, homoniemen) vereisen inhoudelijke kennis — niet blind fixen, aan de gebruiker voorleggen of `/write-element`/`/assess-element` gebruiken.

## Stap 2 — Modelbeoordeling (na het script, alleen wat overblijft)

Dit mag op **Haiku**, zoals voorheen — het risico zat in tellen over de hele wiki, niet in het beoordelen van een kleine, al voorgeselecteerde kandidatenlijst of het lezen van een paar pagina's.

- **Anti-patroon registr\*** — het script levert kandidaatregels (elke regel met "registreerbaar"/"registratieobject"). Lees per kandidaat de context: wordt de term gebruikt als *afwijsgrond* tegen de 6 BO-criteria (overtreding) of ter ondersteuning/beschrijving (geen overtreding)? Rapporteer alleen de echte overtredingen — bij de vorige lint-run bleek de naïeve grep-aanpak zelf al 40+ kandidaten op te leveren waarvan de meeste legitiem taalgebruik waren.
- **`bo_relaties`-incompleetheid** — het script noemt ontbrekende kardinaliteit (bij niet-generalisatie relaties) of een `bedrijfsobject`-waarde die geen wiki-link is. Beoordeel per geval: omissie (fix) of bewust (relatie naar een concept zonder eigen BO-pagina, dan is platte tekst correct).
- **Wees-BO's** — beoordeel per genoemde BO of dat terecht is (nog niet verwerkt, nieuw) of een omissie in een onderwerpoverzicht.
- **Subtypes-mismatch / `## Subtypes` zonder frontmatter** — beoordeel of het genoemde begrip een eigen BO-pagina zou moeten zijn i.p.v. subtype.
- **Begrippentabel → BO (subtype-patroon)** — begrippen met BO?=❌ waarvan de Reden een subtype-patroon bevat ("subtype van", "onderdeel van", "specialisatie van", "valt onder", "categorie van", "variant van") die niet als `bo_subtypes` of in een Subtypes/Specialisaties-tabel bij het genoemde parent-BO staan. Alleen signaleren als het parent-BO bestaat. Let op: "onderdeel van" vangt ook composities — handmatig beoordelen.
- **Specialisaties ↔ generalisatie symmetrie, dode links in `## Generalisatie`** — nog niet gescript; lees de betrokken BO-paren en controleer de wederkerigheid handmatig.
- **`Wiki/Analyses/ggm-dekking.md` volledigheid en Analyse-links** — nog niet gescript; steekproefsgewijs controleren.
- **Terugmeldingen-consistentie** (`⚠️ ter discussie` in body ↔ vermelding in `Wiki/Analyses/ggm-terugmeldingen.md`), **Duplicaat-/homoniem-terugmelding**, **Naamkeuze-consistentie** — nog niet gescript; cross-referentie vereist tekstuele matching die (nog) niet betrouwbaar te automatiseren was in de eerste scriptversie.
- **Tegenstrijdige definities** tussen onderwerpoverzicht en BO-pagina, **contradicties** tussen willekeurige pagina's, **verouderde claims** — inherent semantisch, blijft bij het model.

## Rapportage

Eén gecombineerd rapport, gesorteerd op ernst (herleidbaarheid > ontbrekende data > inconsistenties > suggesties). Markeer bij elke regel de bron: **[script]** (exacte telling) of **[model]** (beoordeeld, aantal kan door interpretatie afwijken). Sluit af met een totaaltelling per bron.
