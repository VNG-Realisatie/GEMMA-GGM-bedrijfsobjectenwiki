---
type: analyse
titel: "Actoren en rollen: definities en criteria"
domein: []
datum: 2026-07-08
---

# Actoren en rollen: definities en criteria

Deze pagina is de naslagbron voor het onderscheid tussen Business Actor en Business Role (ArchiMate) en de criteria waarmee begrippen uit bronnen als actor of rol worden geclassificeerd. De skills [[assess-element]] en [[write-element]] verwijzen hiernaar.

## Plaats in de wiki

Actoren en rollen zijn volwaardige elementen naast bedrijfsobjecten:

- Actor-pagina's staan in `Wiki/Actoren/{naam}.md`
- Rol-pagina's staan in `Wiki/Rollen/{naam}.md`
- Beide mappen zijn plat (geen taakveld-substructuur); het taakveld staat in de frontmatter.

Een begrip kan zowel actor/rol als bedrijfsobject zijn: het is een actor of rol op grond van de criteria hieronder, en **daarnaast ook** een bedrijfsobject zodra er gegevens over worden vastgelegd (de 6 BO-criteria worden gehaald). In dat geval komen er **twee aparte pagina's** — één in `Wiki/Actoren/` of `Wiki/Rollen/` en één in `Wiki/Bedrijfsobjecten/` — met cross-links in frontmatter en tekst, elk met een eigen definitie vanuit het eigen perspectief (wie handelt vs. welke gegevens worden vastgelegd).

## Business Actor

**Definitie (ArchiMate):** *A business entity that is capable of performing behavior.*

Een concrete organisatorische entiteit die kan handelen: een persoon, organisatie of organisatorische eenheid (bv. de gemeenteraad, het college van B&W, een raadslid, een uitvoeringsorganisatie).

Diagnostische vragen:

1. Heeft het begrip een eigen identiteit?
2. Kan het begrip zelfstandig gedrag uitvoeren?
3. Kan het begrip meerdere rollen vervullen?
4. Blijft het begrip bestaan als verantwoordelijkheden veranderen?
5. Kan het begrip worden toegewezen aan processen, functies of services?
6. Is het begrip een persoon, organisatie of organisatorische eenheid?

## Business Role

**Definitie (ArchiMate):** *The responsibility for performing specific behavior, to which an actor can be assigned.*

Een verantwoordelijkheid voor specifiek gedrag, waaraan een actor kan worden toegewezen (bv. heffingsambtenaar, indiener, vergunningverlener). De rol bestaat onafhankelijk van wie hem vervult.

Diagnostische vragen:

1. Beschrijft het begrip een verantwoordelijkheid in plaats van een entiteit?
2. Kan deze verantwoordelijkheid door meerdere actoren worden vervuld?
3. Kan één actor meerdere van deze rollen tegelijk vervullen?
4. Is het begrip gekoppeld aan specifieke taken, bevoegdheden of verantwoordelijkheden?
5. Heeft het begrip geen eigen identiteit, maar wordt het door een actor vervuld?
6. Kan een actor expliciet aan dit begrip worden toegewezen?

## Beslisvraag

Gaat het begrip over **wie** iets doet (Actor) of **in welke verantwoordelijkheid** iets wordt gedaan (Role)?

## Doelgroep is geen actor of rol

Een doelgroep (bv. jongeren, ondernemers, minima) is geen entiteit met eigen identiteit (geen actor) en geen verantwoordelijkheid (geen rol). Het is een **bedrijfsobject/classificatie waarmee Business Actors worden ingedeeld** — bv. de actor Inwoner of Ondernemer, met de doelgroep als classificatie daarop. Doelgroepen worden dus beoordeeld en vastgelegd als gewoon bedrijfsobject in `Wiki/Bedrijfsobjecten/`, via de 6 BO-criteria.

## Scope

Het [[gemeentelijk perspectief]] blijft leidend: alleen actoren en rollen die de gemeente zelf ziet, inzet of waarmee zij direct handelt krijgen een pagina. Externe partijen die louter context zijn, blijven context.
