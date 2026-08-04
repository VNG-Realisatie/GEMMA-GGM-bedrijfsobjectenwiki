# Business Object
**ArchiMate-type:** Business Object
**Exportcode:** BusinessObject

Een passief element: iets waarover de organisatie informatie vastlegt en dat in bedrijfsprocessen wordt gebruikt of geproduceerd.

## Herkenning

Zoek in bronnen naar:

- zelfstandige naamwoorden waarover wordt **geregistreerd, vastgelegd, bijgehouden, aangevraagd, verleend, beheerd of besloten**;
- zaken met een **nummer, kenmerk, dossier of register** (aanvraagnummer, vergunningkenmerk);
- het onderwerp van formulieren, besluiten, meldingen, aanslagen, plannen en overeenkomsten.

## Criteria

| # | Criterium | Toetsvraag |
|---|---|---|
| 1 | Informatie | Wordt er informatie over vastgelegd? |
| 2 | Identiteit | Is een exemplaar aanwijsbaar en van andere exemplaren te onderscheiden? |
| 3 | Levenscyclus | Ontstaat het, verandert het en eindigt het? |
| 4 | Eigenschappen | Heeft het eigen kenmerken/attributen? |

Alle vier de criteria moeten aantoonbaar zijn, elk onderbouwd met een bronpassage.

## Afbakening

- **[Business Actor](business-actor.md) / [Business Role](business-role.md)** — een partij waarover óók informatie wordt bijgehouden kan beide zijn (multi-type kandidaat, bijvoorbeeld een inwoner): actor/rol voor het handelen, business object voor de vastgelegde informatie.
- **Product** — een samenhangend aanbod van diensten aan afnemers; een vergunning of subsidie kan als aanbod product zijn én als registratie business object. Kies business object wanneer de informatieregistratie centraal staat.
- **Representation / Data Object** — een formulier, brief of bestand is een weergave of technische vorm van het object, niet het bedrijfsobject zelf. Modelleer het onderliggende begrip.
