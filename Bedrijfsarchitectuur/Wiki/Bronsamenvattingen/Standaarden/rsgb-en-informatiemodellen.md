---
type: bronsamenvatting
bron: "[RSG_Basisgegevens_2.02_deel_I_(in_gebruik)](../../Sources/Standaarden/RSG_Basisgegevens_2.02_deel_I_(in_gebruik).md)"
titel: "RSGB 2.02 Deel I en VNG Informatiemodellen"
domein: []
datum_ingest: 2026-06-18
begrippen_geextraheerd: []
---

# Bronsamenvatting: RSGB en VNG Informatiemodellen

**Bronnen:**
- RSG Basisgegevens 2.02 Deel I (KING, april 2018)
- Wat is een Informatiemodel? (standaarden.vng.nl/Informatiemodellen)

## RSGB: Referentiemodel Stelsel van Gemeentelijke Basisgegevens

### Doel en positionering

Het RSGB is een objecten- of gegevensmodel dat gemeenten ondersteunt bij het stroomlijnen van hun gegevenshuishouding. Het is onderdeel van de GEMMA en in lijn met de NORA.

**Drie doelen:**
1. Eenduidig onderhouden van basisgegevens door gemeenten
2. Uitwisseling van basisgegevens mogelijk maken (via StUF-BG)
3. Uitwisselen met en benutten van het landelijk stelsel van basisregistraties

### Bronnen van het RSGB

Het RSGB is gebaseerd op de catalogi van zes basisregistraties en één aanvullend model:

| Basisregistratie | Catalogus/Model |
|---|---|
| BRP (voorheen GBA) | Logisch Ontwerp GBA v3.6/3.7 |
| BAG (BRA + BGR) | Catalogus BRA v4.0 + Catalogus BGR v4.0 |
| BRK (Kadaster) | Catalogus BRK v1.0.4 |
| BRWOZ | Catalogus Basisregistratie WOZ v1.3 |
| NHR (Handelsregister) | Gegevenscatalogus NHR + PvE HR v1.6 |
| BGT/IMGeo | Informatiemodel Geografie v2.0 |
| *(aanvulling)* | GFO Basisgegevens (VNG, 1998) |

### Méér dan de basisregistraties

> "Het binnengemeentelijk stelsel is dan ook 'rijker' dan het landelijke stelsel."

> "De basisgegevens vormen nog maar het topje van de ijsberg van wat gemeenten aan gegevens nodig hebben om hun processen uit te voeren."

Het RSGB neemt de basisregistraties bijna volledig over, maar voegt toe:
- **Generalisaties**: GEBOUWD OBJECT (verblijfsobject + overig), BENOEMD OBJECT, RECHTSPERSOON, SUBJECT
- **Gemeentelijke objecten**: OVERIG GEBOUWD OBJECT, OVERIG TERREIN, GEMEENTE, WIJK, BUURT
- **Aanvullende relaties**: correspondentieadressen, nevenlocaties vestigingen, ruimtelijke relaties
- **Aanvullende gegevens**: gegevens die "voor de gemeentelijke processen cruciaal zijn, maar niet in het landelijk stelsel worden geregistreerd"

### Géén databaseontwerp

> "Dit gegevensmodel vormt geen grondslag voor een (relationele) database. Het staat partijen vrij om een eigen technische realisatievorm te kiezen."

Het RSGB is een referentiemodel: het geeft aan welke informatievragen gesteld en beantwoord kunnen worden, niet hoe de data fysiek wordt opgeslagen.

### Relatie met taakspecifieke modellen

Naast het RSGB bestaan taakspecifieke informatiemodellen die zijn gerelateerd aan het stelsel doordat zij een deel van de basisgegevens bevatten. Het RSGB vormt de horizontale laag; taakspecifieke modellen de verticale laag.

## VNG Informatiemodellen

De VNG onderscheidt drie categorieën informatiemodellen:

1. **RSGB**: basis- en kerngegevens (horizontaal)
2. **Zaakgericht werken**: RGBZ (informatiemodel Zaken) en ImZTC (informatiemodel Zaaktypen)
3. **Koppelvlakbeschrijvingen**: domeinspecifieke modellen als onderdeel van StUF-standaarden

Alle modellen voldoen bij voorkeur aan het **Metamodel voor Informatiemodellen (MIM)**.

## Relevantie voor de wiki

Deze bronnen nuanceren het beeld van het GGM als "bottom-up inventarisatie van bestaande databases." Het GGM is gebouwd op drie lagen bronnen:

1. **Informatiemodellen van basisregistraties** — formele catalogi, niet ruwe data
2. **RSGB** — integratiemodel dat de basisregistraties verbindt en aanvult met gemeentelijke behoeften
3. **Domeinmodellen** — taakspecifieke uitwerkingen per beleidsdomein

Het RSGB beschrijft wat de gemeente met basisregistraties uitwisselt. Intern registreert de gemeente meer — de domeinmodellen in het GGM dekken dit bredere veld. Het verschil tussen RSGB (uitwisseling) en interne registratie (domeinmodellen) is relevant voor het begrip van de GGM-scope.

## Citaten

> "Het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) biedt gemeenten en hun leveranciers houvast bij het invoeren en het gebruiken van deze gegevens."

> "KING raadt gemeenten dringend aan om bij de ontwikkeling van hun informatievoorziening uit te gaan van het referentiemodel en niet alleen van één, of meer, catalogi van landelijke basisregistraties."

> "Het kan voorkomen dat taakspecifieke modellen ook zijn gebaseerd op gegevensuitwisseling met niet-gemeentelijke ketenpartners, die op hun beurt weer andere sectormodellen toepassen."
