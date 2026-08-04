# Business Role
**ArchiMate-type:** Business Role
**Exportcode:** BusinessRole

De verantwoordelijkheid voor specifiek gedrag, waaraan een actor kan worden toegewezen; een hoedanigheid, geen concrete partij.

## Herkenning

Zoek in bronnen naar:

- **functie- en hoedanigheidsbenamingen**, vaak op *-er/-aar*: aanvrager, toezichthouder, behandelaar, beheerder, vergunninghouder;
- **wettelijk gedefinieerde rollen**: bevoegd gezag, initiatiefnemer, belanghebbende;
- formuleringen als "in de rol van", "optredend als", "namens".

## Criteria

| # | Criterium | Toetsvraag |
|---|---|---|
| 1 | Verantwoordelijkheid | Beschrijft het een verantwoordelijkheid of positie (niet een concrete partij)? |
| 2 | Meerdere vervullers | Is de rol vervulbaar door meerdere actoren (nu of denkbaar)? |
| 3 | Gedrag | Is er gedrag aan de rol gekoppeld (wat dóet de rolvervuller)? |

Alle drie de criteria moeten aantoonbaar zijn, elk onderbouwd met een bronpassage.

## Afbakening

- **[Business Actor](business-actor.md)** — is er maar één concrete partij die dit ooit kan zijn, en heeft die een eigen naam en bestaan? Dan is het een actor. Twijfelregel: kun je vragen "wíe is vandaag de {benaming}?" met wisselend antwoord, dan is het een rol.
- **[Business Function](business-function.md)** — een rol is de *wie*-kant (verantwoordelijkheid, toewijsbaar), een functie de *wat*-kant (gebundelde capaciteit). "Toezichthouder" is een rol; "toezicht" is een functie.
- **[Business Object](business-object.md)** — wordt over de rolvervuller informatie vastgelegd (bijv. register van vergunninghouders), dan is het begrip mogelijk multi-type: rol én business object op dezelfde kandidaatpagina.
