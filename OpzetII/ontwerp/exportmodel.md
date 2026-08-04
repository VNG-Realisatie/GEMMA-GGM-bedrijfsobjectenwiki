# Exportmodel naar het GEMMA ArchiMate-model

## Principe

De wiki exporteert **voorstellen**; het GEMMA ArchiMate-model registreert. Wat wordt geëxporteerd is precies de machine-leesbare kern uit de frontmatter van goedgekeurde kandidaatpagina's — de analyse en motivatie blijven in de wiki en gaan níet mee. Zo ontstaat geen dubbele vastlegging: definitie en relaties krijgen hun definitieve, beheerde vorm in GEMMA; de wiki bewaart waaróm ze zo luiden.

## Wat wordt geëxporteerd

- Alle kandidaatpagina's met status `goedgekeurd` en een leeg `export:`-veld (of een expliciete selectie).
- Per **gekozen** type in de `typen:`-lijst één ArchiMate-element; afgevallen typen exporteren niet.
- De voorgestelde relaties van die pagina's, voor zover beide uiteinden exporteerbaar zijn (zie onder).

## Veldmapping

| Frontmatter kandidaatpagina | ArchiMate | Toelichting |
|---|---|---|
| `naam` | name | |
| `typen[].type` (besluit `gekozen`) | elementtype | typecode uit het typekader, bijv. `BusinessObject` |
| `definitie` | documentation | de voorgestelde definitie |
| `toelichting` | documentation (vervolg) | alleen indien gevuld |
| `synoniemen` | property `Synoniemen` | kommagescheiden |
| bronverwijzingen (uit de bronanalyse) | property `Bron` | paden/URL's van de brondocumenten |
| pad van de kandidaatpagina | property `Onderbouwing` | verwijzing terug naar de wiki-analyse |
| `relaties[]` | ArchiMate-relaties | zie onder |

Niet geëxporteerd: status, motivatie, typeanalyse, alternatieve typen — dat is wiki-inhoud.

## Relaties

Elke relatie in `relaties:` heeft een relatietype (associatie, compositie, aggregatie, generalisatie, toewijzing, realisatie, …), een doel-element en een beschrijving:

- doel is een **andere kandidaat** (`element_in: kandidaten`): de relatie exporteert alleen als dat doel zelf `goedgekeurd`/geëxporteerd is; anders komt hij op de wachtlijst in het exportrapport en gaat hij mee met een latere run;
- doel is een **bestaand GEMMA-element** (`element_in: gemma`): de relatie exporteert direct, met het element bij naam.

## Vorm van een exportrun

Eén run schrijft een datummap `{wiki-root}/export/{jjjj-mm-dd}/` met:

- **`elementen.csv`** — kolommen: `naam; elementtype; definitie; toelichting; synoniemen; bron; onderbouwing`
- **`relaties.csv`** — kolommen: `van; relatietype; naar; naar_in; beschrijving`
- **`rapport.md`** — wat er in deze run is geëxporteerd, welke relaties op de wachtlijst staan en waarom, en welke goedgekeurde kandidaten zijn overgeslagen (bijv. onvolledige frontmatter).

Exportbestanden zijn afgeleide bestanden: nooit handmatig bewerken; een run is altijd reproduceerbaar uit de kandidaatpagina's.

## Na de export

- De pagina krijgt in `export:` de datum en het exportbestand; het logboek krijgt één regel voor de run.
- De verwerking van de CSV's in het GEMMA ArchiMate-model (aanmaken/wijzigen van elementen) gebeurt buiten de wiki, door de modelbeheerder.
- **Open punten** (zie [open-punten.md](open-punten.md)): of dit exportpad aansluit op de bestaande CSV-pijplijn `Bedrijfsarchitectuur/tools/export_ggm_csv.py` of die vervangt, en wat er met de kandidaatpagina gebeurt ná export (bevriezen, archiveren, reduceren tot verwijzing).
