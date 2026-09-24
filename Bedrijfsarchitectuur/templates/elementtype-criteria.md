# Elementtype-criteria

Referentiemateriaal bij `.claude/commands/assess-element.md` en `.claude/commands/write-element.md`: hoe een begrip wordt geclassificeerd als bedrijfsobject, actor, rol, bedrijfsfunctie of bedrijfsproces — of als geen van deze. Dit zijn regels die een skill uitvoert, geen wiki-inhoud; wiki-pagina's verwijzen er daarom niet naar (zie `CLAUDE.md` [WC7]).

## Generiek — classificatie (alle typen)

Eerste stap voor elk begrip: bepaal het begripstype.

| Begripstype | Omschrijving | ArchiMate-elementtype | Element-kandidaat? | GGM-match verwacht? |
|---|---|---|---|---|
| **object** | Concreet ding dat in processen wordt gebruikt/geproduceerd | Business Object | Ja (BO) | Ja |
| **governance-instrument** | Regeling, programma, wet, maatregel, verordening | Contract / Product | Ja (BO) | Doorgaans niet (GGM dekt governance niet compleet) |
| **actor** | Persoon, organisatie of organisatorische eenheid die kan handelen | Business Actor | Ja (actor-pagina) | Deels (RSGB) |
| **rol** | Verantwoordelijkheid voor specifiek gedrag, door een actor vervulbaar | Business Role | Ja (rol-pagina) | Deels (RSGB) |
| **doelgroep** | Groep waarop beleid of uitvoering gericht is | Business Object (classificatie) | Ja (BO) | Deels (RSGB) |
| **bedrijfsfunctie** | Gebundeld vermogen van de gemeente, organisatorisch stabiel | Business Function | Ja (functie-pagina) | Doorgaans niet (GGM dekt functies niet compleet) |
| **bedrijfsproces** | Reeks activiteiten met begin, einde en specifiek resultaat | Business Process | Ja (proces-pagina) | Doorgaans niet (GGM dekt processen niet compleet) |
| **thema** | Werkgebied dat doelen, actoren en instrumenten bundelt | Grouping | Nee | Nee |
| **doel** | Nagestreefde situatie of uitkomst | Goal / Outcome | Nee | Nee |
| **waarde** | Maatschappelijk ideaal, richtinggevend principe | Driver / Principle | Nee | Nee |

**Begripstype vs. entiteitstype:** dit zijn begripstypen — ze classificeren begrippen uit bronnen (*wat is het?*). De `/entiteitendekking` skill gebruikt een apart classificatiesysteem, entiteitstypen, dat GGM-entiteiten classificeert (*waarom is het wel/geen BO?*). Zie die skill voor de entiteitstype-classificatie.

**Stop-regel:** thema / doel / waarde = geen element-kandidaat → vastleggen in begrippentabel met BO?=❌, geen verdere beoordeling.

**Routering naar type-specifieke criteria:**
- object, governance-instrument, doelgroep → §Bedrijfsobject
- actor, rol → §Actor en rol
- bedrijfsfunctie, bedrijfsproces → §Bedrijfsfunctie en bedrijfsproces

Een doelgroep is géén actor of rol maar een classificatie waarmee actoren worden ingedeeld — behandel als gewoon bedrijfsobject (§Bedrijfsobject), niet via §Actor en rol.

## Bedrijfsobject

### De 6 BO-criteria

Scoor elk criterium met ja/nee:

1. **Heeft betekenis binnen het onderwerp** — is dit een herkenbaar concept in het vakgebied?
2. **Is herkenbaar voor domeinexperts** — weten beleidsmedewerkers/uitvoerders wat dit is?
3. **Heeft een eigen bestaan binnen het onderwerp** — bestaat het onafhankelijk van andere objecten?
4. **Kan in meervoud bestaan** — zijn er meerdere exemplaren van?
5. **Heeft een eigen levenscyclus** — wordt het aangemaakt, gewijzigd, beëindigd?
6. **Heeft relaties met andere concepten** — relateert het aan andere BO's of concepten?

**Drempel:** 5 of meer van de 6 = BO.

**Beslisvraag:** herkent de gemeente dit als een zelfstandig ding waar beleid op gemaakt wordt?

**Negatieve toets:** geen BO als het slechts een eigenschap, status, activiteit, regel of classificatie van iets anders is.

### Anti-patronen

De 6 criteria zijn de enige toets. Zie `CLAUDE.md` [BO1]–[BO3]: NOOIT registr* (registreerbaar, registreren, registratieobject), eigendom, systeembeheer, regie of extern systeem als criterium of motivatie bij BO-beoordeling.

## Actor en rol

Onderscheid tussen Business Actor en Business Role (ArchiMate) en de criteria waarmee begrippen uit bronnen als actor of rol worden geclassificeerd.

### Plaats in de wiki

Actoren en rollen zijn volwaardige elementen naast bedrijfsobjecten:

- Actor-pagina's staan in `Wiki/Actoren/{naam}.md`
- Rol-pagina's staan in `Wiki/Rollen/{naam}.md`
- Beide mappen zijn plat (geen taakveld-substructuur); het taakveld staat in de frontmatter.

Een begrip kan zowel actor/rol als bedrijfsobject zijn: het is een actor of rol op grond van de criteria hieronder, en **daarnaast ook** een bedrijfsobject zodra er gegevens over worden vastgelegd (de 6 BO-criteria worden gehaald). In dat geval komen er **twee aparte pagina's** — één in `Wiki/Actoren/` of `Wiki/Rollen/` en één in `Wiki/Bedrijfsobjecten/` — met cross-links in frontmatter en tekst, elk met een eigen definitie vanuit het eigen perspectief (wie handelt vs. welke gegevens worden vastgelegd).

### Business Actor

**Definitie (ArchiMate):** *A business entity that is capable of performing behavior.*

Een concrete organisatorische entiteit die kan handelen: een persoon, organisatie of organisatorische eenheid (bv. de gemeenteraad, het college van B&W, een raadslid, een uitvoeringsorganisatie).

Diagnostische vragen:

1. Heeft het begrip een eigen identiteit?
2. Kan het begrip zelfstandig gedrag uitvoeren?
3. Kan het begrip meerdere rollen vervullen?
4. Blijft het begrip bestaan als verantwoordelijkheden veranderen?
5. Kan het begrip worden toegewezen aan processen, functies of services?
6. Is het begrip een persoon, organisatie of organisatorische eenheid?

### Business Role

**Definitie (ArchiMate):** *The responsibility for performing specific behavior, to which an actor can be assigned.*

Een verantwoordelijkheid voor specifiek gedrag, waaraan een actor kan worden toegewezen (bv. heffingsambtenaar, indiener, vergunningverlener). De rol bestaat onafhankelijk van wie hem vervult.

Diagnostische vragen:

1. Beschrijft het begrip een verantwoordelijkheid in plaats van een entiteit?
2. Kan deze verantwoordelijkheid door meerdere actoren worden vervuld?
3. Kan één actor meerdere van deze rollen tegelijk vervullen?
4. Is het begrip gekoppeld aan specifieke taken, bevoegdheden of verantwoordelijkheden?
5. Heeft het begrip geen eigen identiteit, maar wordt het door een actor vervuld?
6. Kan een actor expliciet aan dit begrip worden toegewezen?

**Toetsdrempel:** meeste vragen (4+) met ja beantwoord = het begrip kwalificeert als actor resp. rol.

### Beslisvraag

Gaat het begrip over **wie** iets doet (Actor) of **in welke verantwoordelijkheid** iets wordt gedaan (Role)?

### Scope

Het gemeentelijk perspectief blijft leidend: alleen actoren en rollen die de gemeente zelf ziet, inzet of waarmee zij direct handelt krijgen een pagina. Externe partijen die louter context zijn, blijven context.

## Bedrijfsfunctie en bedrijfsproces

Onderscheid tussen Business Function en Business Process (ArchiMate) en de criteria waarmee begrippen uit bronnen als bedrijfsfunctie of bedrijfsproces worden geclassificeerd.

### Plaats in de wiki

Bedrijfsfuncties en bedrijfsprocessen zijn volwaardige elementen naast bedrijfsobjecten, actoren en rollen:

- Bedrijfsfunctie-pagina's staan in `Wiki/Bedrijfsfuncties/{taakveld}/{beleidsdomein}/{naam}.md`
- Bedrijfsproces-pagina's staan in `Wiki/Bedrijfsprocessen/{taakveld}/{beleidsdomein}/{naam}.md`
- Beide volgen, anders dan Actoren/Rollen, dezelfde taakveld/beleidsdomein-substructuur als `Wiki/Bedrijfsobjecten/` (besluit 2026-09-23) — functies en processen zijn net als BO's onderwerp-/domeingebonden.

Andere BO-pagina's verwijzen naar deze pagina's via de bestaande frontmatter-velden `bedrijfsprocessen`/`bedrijfsfuncties` (zie `templates/element.md`), als wiki-link.

### Business Function

**Definitie (ArchiMate):** *A collection of business behavior based on a chosen set of criteria (typically required business resources and/or competences), closely aligned to an organization, but not necessarily explicitly governed by the organization.*

Een gebundeld vermogen van de gemeente om een bepaald soort gedrag te leveren, ingedeeld op vereiste kennis/resources (bv. "vergunningverlening", "belastingheffing", "handhaving") — organisatorisch stabiel, ongeacht wie het uitvoert of in welke volgorde.

Diagnostische vragen:

1. Beschrijft het begrip een vermogen/capaciteit van de gemeente, geen concrete stappen?
2. Blijft het begrip herkenbaar ongeacht de volgorde waarin werk wordt uitgevoerd?
3. Is het begrip organisatorisch stabiel (verandert zelden, ook als processen erbinnen wijzigen)?
4. Bundelt het begrip meerdere processen die hetzelfde soort resources/kennis vereisen?
5. Heeft het begrip geen eigen begin/einde of doorlooptijd?
6. Zou een domeinexpert dit noemen als antwoord op "wat kan de gemeente op dit vlak"?

### Business Process

**Definitie (ArchiMate):** *A sequence of business behaviors that achieves a specific outcome such as a defined set of products or business services.*

Een reeks van activiteiten die een specifiek resultaat oplevert (bv. "vergunningaanvraag behandelen", "aanslag opleggen") — heeft een begin, een einde en een concrete uitkomst.

Diagnostische vragen:

1. Beschrijft het begrip een reeks activiteiten met een begin en een einde?
2. Levert het begrip een specifiek, benoembaar resultaat op (product, besluit, dienst)?
3. Is er een volgorde of afhankelijkheid tussen de stappen?
4. Wordt het begrip in de praktijk "doorlopen" of "afgehandeld" (i.p.v. "uitgevoerd als vermogen")?
5. Kan het begrip meerdere keren instantiëren (elke aanvraag is een nieuwe procesinstantie)?
6. Valt het begrip onder een bredere bedrijfsfunctie die het vermogen ervoor levert?

**Toetsdrempel:** meeste vragen (4+) met ja beantwoord = het begrip kwalificeert als bedrijfsfunctie resp. bedrijfsproces.

### Beslisvraag

Gaat het begrip over **wat de gemeente kan** (Function) of **hoe een specifiek resultaat tot stand komt** (Process)?

### Verhouding tot bedrijfsobjecten

Een bedrijfsfunctie of -proces is zelf normaal gesproken géén bedrijfsobject: er wordt niet typisch "data over vastgelegd" op dezelfde manier als bij een BO. Het twee-pagina-patroon van actoren/rollen (zie §Actor en rol) is hier daarom uitzondering, geen regel: alleen toepassen als de 6 BO-criteria (§Bedrijfsobject) zelfstandig slagen (bijv. een geregistreerde "procesinstantie" met eigen levenscyclus en attributen).

### GGM-verwachting

Het GGM modelleert vrijwel uitsluitend data-objecten; bedrijfsfuncties en -processen zijn doorgaans niet (compleet) gedekt — zelfde voorbehoud als bij `grondslag: procesobject`/`governance-object` (`templates/element.md` §Grondslag). Een GGM-match bij een functie/proces is dus de uitzondering, geen verwachting; het ontbreken ervan is geen hiaat om te melden.

### Scope

Het gemeentelijk perspectief blijft leidend: alleen functies/processen die de gemeente zelf uitvoert of aanstuurt krijgen een pagina. Functies/processen van ketenpartners blijven context (`CLAUDE.md` [WC5]).
