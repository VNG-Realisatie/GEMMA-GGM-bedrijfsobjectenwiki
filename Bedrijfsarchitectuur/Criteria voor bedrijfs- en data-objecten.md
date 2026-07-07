# vertalen begrippen naar bedrijfsobjecten

verwarrend is dat de inwoner zowel actief als passief kan worden gezien. als actor en als bedrijfsobject. hoe vang je dit in definities en criteria

Dit is inderdaad één van de lastigste aspecten van ArchiMate. De verwarring ontstaat doordat hetzelfde begrip uit de werkelijkheid vanuit twee verschillende perspectieven wordt gemodelleerd.

De oplossing is om **niet het ding zelf te classificeren**, maar **de rol die het in het model vervult**.

| Vraag                      | Antwoord        | ArchiMate       |
| -------------------------- | --------------- | --------------- |
| Wie voert handelingen uit? | Actief element  | Business Actor  |
| Waarover gaat informatie?  | Passief element | Business Object |

De **inwoner** kan dus beide zijn, maar nooit tegelijkertijd in dezelfde betekenis.

## Actor

Definitie:

> Een actor is een entiteit die gedrag uitvoert of verantwoordelijk is voor gedrag.

Criteria:

* voert activiteiten uit;
* neemt besluiten;
* initieert processen;
* heeft verantwoordelijkheden.

Voorbeeld:

```
Inwoner
    │
vraagt aan
    ▼
Paspoort aanvragen
```

Hier is de inwoner actor.

---

## Bedrijfsobject

Definitie:

> Een bedrijfsobject is een informatie-object waarover de organisatie informatie beheert of gebruikt.

Criteria:

* wordt gelezen;
* wordt gewijzigd;
* wordt geregistreerd;
* wordt uitgewisseld;
* wordt opgeslagen;
* wordt geclassificeerd.

Voorbeeld:

```
Registreren persoonsgegevens
          │
      wijzigt
          ▼
Inwoner
```

Hier betekent "Inwoner" de informatie over de inwoner.

---

## Eigenlijk zijn dit twee verschillende dingen

Dat ze dezelfde naam hebben, maakt het verwarrend.

| Werkelijkheid           | ArchiMate       |
| ----------------------- | --------------- |
| fysieke persoon         | Business Actor  |
| informatie over persoon | Business Object |

Veel organisaties noemen beide simpelweg "Inwoner".

Semantisch zijn het echter:

```
Persoon
├── handelende persoon
└── informatie over persoon
```

---

## Mogelijke naamgevingsconventies

Om verwarring te voorkomen gebruiken sommige architecturen:

| Actor       | Bedrijfsobject      |
| ----------- | ------------------- |
| Inwoner     | Inwonergegevens     |
| Burger      | Persoonsgegevens    |
| Leverancier | Leveranciersdossier |
| Medewerker  | Medewerkergegevens  |

Voordeel:

* geen dubbele betekenis.

Nadeel:

* minder natuurlijk taalgebruik.

---

## Of juist dezelfde naam

Veel modellen (ook UML-domeinmodellen) houden gewoon:

```
Actor:
Inwoner

Business Object:
Inwoner
```

Context bepaalt betekenis.

Dat is hoe ArchiMate meestal wordt toegepast.

---

## Voor een semantisch bedrijfsobjectenmodel

Voor GEMMA zou ik het onderscheid explicieter maken dan ArchiMate doet.

**Begrip**

> Inwoner: natuurlijke persoon die ingezetene is van een gemeente.

Vanuit dat begrip kun je twee modelleerrollen afleiden:

| Rol                                 | ArchiMate       |
| ----------------------------------- | --------------- |
| Inwoner als deelnemer aan processen | Business Actor  |
| Informatie over inwoner             | Business Object |

Zo voorkom je dat definities afhankelijk worden van het modelleernotatie.

## Algemene criteria

Je kunt een eenvoudig beslisschema hanteren:

```
Is het iets dat handelt?
        │
      ja ─────────► Actor

      nee
        │
Is het informatie waar processen mee werken?
        │
      ja ─────────► Business Object
```

[Inferred] Voor een bedrijfsobjectenmodel is het zelfs beter om **"Inwoner" slechts één keer als bedrijfsbegrip** te definiëren. Vervolgens kan datzelfde begrip in verschillende modellen verschillende rollen aannemen: als **Business Actor** in een procesmodel, als **Business Object** in een informatiemodel en als **klasse** in een UML-domeinmodel. Daarmee voorkom je dat elk model een eigen definitie van "Inwoner" introduceert; alleen de **functie van het begrip in het model** verandert.

---
Het is zelfs een algemeen patroon in ArchiMate: **één begrip uit de werkelijkheid kan in verschillende ArchiMate-elementtypen worden gemodelleerd, afhankelijk van het perspectief**.

Dat is een gevolg van ArchiMate's scheiding tussen **actief gedrag**, **passieve informatie**, **gedrag** en **structuur**.

|Begrip|Mogelijke ArchiMate-elementen|Afhankelijk van perspectief|
|---|---|---|
|Inwoner|Business Actor, Business Object|Persoon of informatie over persoon|
|Medewerker|Business Actor, Business Object|Werknemer of personeelsgegevens|
|Leverancier|Business Actor, Business Object|Organisatie of leveranciersgegevens|
|Organisatie|Business Actor, Business Collaboration, Business Object|Organisatie, samenwerking of organisatiegegevens|
|Gemeente|Business Actor, Business Object|Organisatie of gegevens over gemeente|
|Vergunning|Business Object, Business Service, Business Event|Informatieobject, verleende dienst of gebeurtenis|
|Melding|Business Event, Business Object|Gebeurtenis of registratie|
|Aanvraag|Business Process, Business Object, Business Event|Proces, dossier of indienmoment|
|Besluit|Business Event, Business Object|Besluitmoment of besluitdocument|
|Betaling|Business Process, Business Event, Business Object|Proces, transactie of betalingsgegevens|
### Event ↔ Business Object

Bijvoorbeeld "Melding".

Als gebeurtenis:

> melding wordt gedaan

→ Business Event

Als registratie:

> melding bevat omschrijving en status

→ Business Object
## Voor semantische modellen

[Inferred] Dit pleit ervoor om **begrippen los te koppelen van ArchiMate-elementtypen**.

Bijvoorbeeld:

```
Begrip
-------
Aanvraag
```

Van daaruit kunnen verschillende modelprojecties ontstaan:

```
                Aanvraag
                    │
      ┌─────────────┼──────────────┐
      ▼             ▼              ▼
Business Object  Business Process  Business Event
```

Niet elk begrip heeft alle projecties.

## Richtlijn

Je kunt onderscheid maken tussen drie niveaus:

|Niveau|Vraag|
|---|---|
|Begrip|Wat betekent dit?|
|Bedrijfsobject|Welke informatie bestaat hierover?|
|ArchiMate|Welke rol speelt dit in deze architectuur?|

Daarmee wordt ArchiMate een **weergave van een semantisch model**, niet de bron van de betekenis.

[Inferred] Voor GEMMA is dat waarschijnlijk de meest consistente aanpak. Definieer elk begrip één keer in het begrippenmodel. Pas daarna bepaal je per architectuurview of dat begrip wordt gemodelleerd als een **Business Actor**, **Business Object**, **Business Process**, **Business Event** of een ander ArchiMate-element. Zo voorkom je dubbele definities en blijft de semantiek onafhankelijk van de gekozen modelleertaal.
# Onderscheid bedrijfsobject en data-object
### Bedrijfsobject

| GEMMA begrip  | definitie   |
|---|---|
|[Bedrijfsobject](https://redactie.gemmaonline.nl/wiki/Id-2a98a3f2-546c-40a3-824f-ecb96b3bbdbb "Id-2a98a3f2-546c-40a3-824f-ecb96b3bbdbb")|Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft.|
- Concept uit de werkelijkheid.
- Heeft betekenis voor de organisatie.
- Voorbeeld: Aanvraag, Vergunning, Medewerker.

### Data-object

- Gegevensrepresentatie van een bedrijfsobject.
- Beschrijft welke informatie wordt vastgelegd.
- Nog onafhankelijk van een specifiek datamodel.


# Criteria voor een bedrijfsobject

- Heeft betekenis binnen het domein.
- Is herkenbaar voor domeinexperts.
- Heeft een eigen bestaan binnen het domein.
- Heeft relaties met andere concepten.
- Is geen attribuut, status of processtap.

## Vragen die wijzen op een bedrijfsobject

- Heeft het begrip een duidelijke betekenis binnen het domein?
- Praten medewerkers en experts over dit begrip als een zelfstandig "ding"?
- Kunnen er meerdere exemplaren van bestaan?
- Heeft het begrip een eigen levenscyclus?
- Heeft het relaties met andere begrippen?

## Vuistregel

Een begrip is meestal een **bedrijfsobject** als je er natuurlijk over kunt spreken als:

- "Deze ..."
- "Die ..."
- "Een nieuwe ..."
- "Deze heeft kenmerken en relaties"

Een begrip is meestal **geen bedrijfsobject** als het slechts een:

- eigenschap,
- status,
- activiteit,
- regel,
- of classificatie

van iets anders is.
# Data-object

Een data-object ontstaat wanneer een bedrijfsobject wordt vastgelegd in gegevens:
- Het bedrijfsobject wordt geregistreerd.
- Attributen worden vastgelegd.
- Het object wordt opgeslagen, uitgewisseld of verwerkt.

## Mogelijke relatie

- Elk data-object representeert een bedrijfsobject.
- Niet elk bedrijfsobject hoeft als data-object te worden vastgelegd.