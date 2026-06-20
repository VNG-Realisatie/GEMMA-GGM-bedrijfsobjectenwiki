---
type: domein
naam: geluid
status: in-behandeling
verwerkingsdatum: 2026-06-20
bronnen_count: 2
begrippen_count: 9
bo_count: 5
---

## Beschrijving

Het domein geluid omvat het gemeentelijk beleid voor geluid en trillingen in de leefomgeving. De gemeente hanteert strengere normen dan landelijk vereist, beschermt stille gebieden, stelt eisen aan geluidluwe gevels bij nieuwbouw, en beheert geluidzones rond industrieterreinen. Het domein raakt aan verkeer, ruimtelijke ordening, milieu en volksgezondheid.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[Geluidbron]] | object | Bron die geluid veroorzaakt, ingedeeld naar bronsoort | ✅ | 6/6 criteria | Gemeentelijke weg, tramlijn, industrieterrein | nee |
| [[Geluidgevoelig gebouw]] | object | Gebouw waarvoor geluidnormen gelden | ✅ | 6/6 criteria | Woning, school, ziekenhuis | nee |
| [[Stil gebied]] | object | Rustig gebied dat de gemeente beschermt en uitbreidt | ✅ | 6/6 criteria | Park, hofje, groengebied | nee |
| [[Geluidzone]] | object | Zone rond industrieterrein met cumulatieve geluidnormen | ✅ | 6/6 criteria | Zone Lage Weide, zone Overvecht | nee |
| [[Geluidscherm]] | object | Fysieke afscherming om geluidhinder te verminderen | ✅ | 6/6 criteria, exact GGM-match | Scherm langs A2, scherm langs spoor | ja |
| geluidontheffing | instrument | Incidentele ontheffing van geluidnormen voor festiviteiten | ❌ | Subtype van Vergunning/Ontheffing | Ontheffing Koningsdag, sportclub | ja (Omgevingsvergunning) |
| geluidluwe gevel | eigenschap | Gevel die voor alle bronsoorten aan standaardwaarde voldoet | ❌ | Bouwkundige eis, eigenschap van gebouw | — | nee |
| geluidkartering | activiteit | Vijfjaarlijkse berekening geluidbelasting conform EU-richtlijn | ❌ | Periodieke activiteit, geen eigen bestaan | Kartering 2021, kartering 2026 | nee |
| actieplan geluid | instrument | Verplicht programma met maatregelen voor geluidknelpunten | ❌ | Governance-instrument | Actieplan 2024-2029 | nee |

## GGM-entiteitendekking

Het domein geluid valt niet samen met één GGM-beleidsdomein. Geluidsscherm zit in Beheer Openbare Ruimte (82 entiteiten), geluidnormen raken aan Omgevingswet (31 entiteiten). Alleen de direct geluid-gerelateerde entiteiten zijn beoordeeld.

| GGM-beleidsdomein | Relevante entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Beheer Openbare Ruimte | 82 (1 relevant: Geluidsscherm) | 1 | 0 | 81 | Overige entiteiten (wegen, groen, riolering) buiten scope geluidbeleid |
| Omgevingswet | 31 (deels relevant) | 0 | 0 | 31 | Brede domeinentiteiten; geluidnormen zijn geen apart BO |

### Dekkingsanalyse

Het GGM heeft geen dedicated beleidsdomein voor geluid. De enige directe match is **Geluidsscherm** (IMBOR). De begrippen Geluidbron, Geluidgevoelig gebouw, Stil gebied en Geluidzone zijn potentiële GGM-hiaten — het zijn herkenbare objecten in het geluidbeleid die de gemeente actief beheert, maar die niet als aparte entiteiten in het GGM voorkomen. Dit past bij het patroon dat het GGM fysieke objecten goed dekt (via IMBOR) maar beleidsmatige classificaties (welke gebouwen zijn geluidgevoelig, welke gebieden zijn stil) niet modelleert.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen|Beleidsnota Geluid en Trillingen (2024)]]
- [[Wiki/Bronsamenvattingen/geluid/actieplan-geluid-utrecht|Actieplan Geluid Utrecht 2018-2023]]

## Nog te verwerken bronnen

Geen bekende openstaande bronnen.

## Openstaande vragen

- Geluidontheffing: past als subtype bij een breder BO Vergunning/Ontheffing — dat BO bestaat nog niet in de wiki. Aanmaken bij verwerking van het domein vergunningen.
- Geluidbron, Geluidgevoelig gebouw, Stil gebied en Geluidzone: terugmelden als potentiële GGM-hiaten? Eerst beoordelen of dit dataobjecten zijn die gemeenten actief beheren, of beleidsmatige classificaties van bestaande objecten (weg, gebouw, terrein).
