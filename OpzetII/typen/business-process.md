# Business Process
**ArchiMate-type:** Business Process
**Exportcode:** BusinessProcess

Een geordende reeks activiteiten die, getriggerd door een gebeurtenis, een gedefinieerd resultaat oplevert.

## Herkenning

Zoek in bronnen naar:

- **procedurele beschrijvingen**: behandelen, afhandelen, beoordelen van een aanvraag; stappen, fasen, doorlooptijden, termijnen;
- woorden als **procedure, proces, werkwijze, aanpak**, of opsommingen van opeenvolgende handelingen;
- een herkenbare **aanleiding** ("na ontvangst van…", "op verzoek van…") en een herkenbaar **eindresultaat** (besluit, beschikking, oplevering).

## Criteria

| # | Criterium | Toetsvraag |
|---|---|---|
| 1 | Activiteiten | Bestaat het uit een geordende reeks activiteiten? |
| 2 | Trigger | Is er een aanwijsbare gebeurtenis die het start? |
| 3 | Resultaat | Levert het een gedefinieerd resultaat/product op? |
| 4 | Begin en einde | Heeft een doorloop een aanwijsbaar begin- en eindpunt? |

Alle vier de criteria moeten aantoonbaar zijn, elk onderbouwd met een bronpassage.

## Afbakening

- **[Business Function](business-function.md)** — een functie is stabiel en loopt altijd door (toezicht); een proces heeft per doorloop een begin en einde (een controle uitvoeren naar aanleiding van een melding). Twijfelregel: kun je één doorloop aanwijzen met een concreet resultaat, dan is het een proces.
- **Business Service** — de naar buiten geboden dienst is een service; de interne uitvoering ervan het proces.
- **[Business Object](business-object.md)** — het resultaat van een proces (besluit, beschikking) is vaak een business object; het proces zelf niet.
