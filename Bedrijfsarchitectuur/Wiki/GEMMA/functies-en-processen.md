---
type: analyse
titel: "Bedrijfsfuncties en bedrijfsprocessen: definities en criteria"
domein: []
datum: 2026-09-23
---

# Bedrijfsfuncties en bedrijfsprocessen: definities en criteria

Deze pagina is de naslagbron voor het onderscheid tussen Business Function en Business Process (ArchiMate) en de criteria waarmee begrippen uit bronnen als bedrijfsfunctie of bedrijfsproces worden geclassificeerd. De skills [[assess-element]] en [[write-element]] verwijzen hiernaar.

## Plaats in de wiki

Bedrijfsfuncties en bedrijfsprocessen zijn volwaardige elementen naast bedrijfsobjecten, actoren en rollen:

- Bedrijfsfunctie-pagina's staan in `Wiki/Bedrijfsfuncties/{taakveld}/{beleidsdomein}/{naam}.md`
- Bedrijfsproces-pagina's staan in `Wiki/Bedrijfsprocessen/{taakveld}/{beleidsdomein}/{naam}.md`
- Beide volgen, anders dan Actoren/Rollen, dezelfde taakveld/beleidsdomein-substructuur als `Wiki/Bedrijfsobjecten/` (besluit 2026-09-23) — functies en processen zijn net als BO's onderwerp-/domeingebonden.

Andere BO-pagina's verwijzen naar deze pagina's via de bestaande frontmatter-velden `bedrijfsprocessen`/`bedrijfsfuncties` (zie `templates/element.md`), voortaan als wiki-link in plaats van vrije tekst.

## Business Function

**Definitie (ArchiMate):** *A collection of business behavior based on a chosen set of criteria (typically required business resources and/or competences), closely aligned to an organization, but not necessarily explicitly governed by the organization.*

Een gebundeld vermogen van de gemeente om een bepaald soort gedrag te leveren, ingedeeld op vereiste kennis/resources (bv. "vergunningverlening", "belastingheffing", "handhaving") — organisatorisch stabiel, ongeacht wie het uitvoert of in welke volgorde.

Diagnostische vragen:

1. Beschrijft het begrip een vermogen/capaciteit van de gemeente, geen concrete stappen?
2. Blijft het begrip herkenbaar ongeacht de volgorde waarin werk wordt uitgevoerd?
3. Is het begrip organisatorisch stabiel (verandert zelden, ook als processen erbinnen wijzigen)?
4. Bundelt het begrip meerdere processen die hetzelfde soort resources/kennis vereisen?
5. Heeft het begrip geen eigen begin/einde of doorlooptijd?
6. Zou een domeinexpert dit noemen als antwoord op "wat kan de gemeente op dit vlak"?

## Business Process

**Definitie (ArchiMate):** *A sequence of business behaviors that achieves a specific outcome such as a defined set of products or business services.*

Een reeks van activiteiten die een specifiek resultaat oplevert (bv. "vergunningaanvraag behandelen", "aanslag opleggen") — heeft een begin, een einde en een concrete uitkomst.

Diagnostische vragen:

1. Beschrijft het begrip een reeks activiteiten met een begin en een einde?
2. Levert het begrip een specifiek, benoembaar resultaat op (product, besluit, dienst)?
3. Is er een volgorde of afhankelijkheid tussen de stappen?
4. Wordt het begrip in de praktijk "doorlopen" of "afgehandeld" (i.p.v. "uitgevoerd als vermogen")?
5. Kan het begrip meerdere keren instantiëren (elke aanvraag is een nieuwe procesinstantie)?
6. Valt het begrip onder een bredere bedrijfsfunctie die het vermogen ervoor levert?

## Beslisvraag

Gaat het begrip over **wat de gemeente kan** (Function) of **hoe een specifiek resultaat tot stand komt** (Process)?

## Verhouding tot bedrijfsobjecten

Een bedrijfsfunctie of -proces is zelf normaal gesproken géén bedrijfsobject: er wordt niet typisch "data over vastgelegd" op dezelfde manier als bij een BO. Het twee-pagina-patroon van actoren/rollen (zie [[Wiki/GEMMA/actoren-en-rollen|Actoren en rollen]]) is hier daarom uitzondering, geen regel: alleen toepassen als de 6 BO-criteria zelfstandig slagen (bijv. een geregistreerde "procesinstantie" met eigen levenscyclus en attributen).

## GGM-verwachting

Het GGM modelleert vrijwel uitsluitend data-objecten; bedrijfsfuncties en -processen zijn doorgaans niet (compleet) gedekt — zelfde voorbehoud als bij `grondslag: procesobject`/`governance-object` (CLAUDE.md, `templates/element.md` §Grondslag). Een GGM-match bij een functie/proces is dus de uitzondering, geen verwachting; het ontbreken ervan is geen hiaat om te melden (analoog aan `/assess-element` Stap 10).

## Scope

Het [[gemeentelijk perspectief]] blijft leidend: alleen functies/processen die de gemeente zelf uitvoert of aanstuurt krijgen een pagina. Functies/processen van ketenpartners blijven context ([WC5]).
