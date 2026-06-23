---
type: ggm-beleidsdomein
naam: Normafwijking
definitie: "Het onderdeel Normafwijking bricht zich op de registratie en afhandeling van situaties waarin een afwijking van de gestelde normen wordt geconstateerd bij inkomensvoorzieningen."
taakveld: "Inkomen"
aantal_entiteiten: 5
---

# GGM Beleidsdomein: Normafwijking

### Diagram GGM en Inkomen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Normafwijking** | Een *normafwijking* (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde **afwijkt van de normatieve verplichtingen** die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering. | Datum vaststelling normafwijking, Datum vaststelling verwijtbaarheid, identificatie, Motivatie verwijtbaarheid, Recidive, Type normafwijking, Verwijtbaarheid | Nee | GGM |

### Normafwijking

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Afwijkende maatregel** | Een *afwijkende maatregel* is een maatregel die afwijkt van de standaardregel of wettelijke norm en die op basis van een wettelijke grondslag, beleidsregel of gemotiveerde beslissing in een concreet geval wordt toegepast. | Bedrag, Code reden afwijking maatregel, Motivatie afwijking maatregel, Percentage | Nee | GGM |
| **Boete** | Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering. Als de vordering niet (meer) bestaat, zou dit gegeven daarmee niet beschikbaar zijn.Daarnaast kan dit ook helpen bij het vastleggen van een boete van een poging tot fraude (zonder financiele consequenties, waardoor geen vordering is ontstaan. (tijdig ondekte valsheid in geschifte e.d.).Bij bedragen hoger dan 50.000 euro, wordt aangifte van fraude gedaan en volgt strafrechtelijk onderzoek.Feitelijk is het uitgangspunt bij het opleggen van een boete dat er altijd sprake is van opzet. Daarom is een apart gegeven Fraude niet opgenomen. | Bedrag boete, Boetevorm, Reden boete, Voorwaarde boete | Nee | GGM |
| **Maatregel** | Een *maatregel* is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven. | Datum aanvang maatregel, Datum einde maatregel, Datum vaststelling maatregel, identificatie, Type maatregel | Nee | GGM |
| **Maatregel op uitkering** | Een *maatregel op uitkering* is een sanctie van een uitvoerend orgaan (zoals een gemeente) waarbij de hoogte van een uitkering tijdelijk wordt verlaagd of aangepast omdat de uitkeringsgerechtigde niet heeft voldaan aan de aan de uitkering verbonden verplichtingen. | Code reden maatregel, Motivatie vermindering maatregel, Percentage maatregel | Nee | GGM |

## Overervingshiërarchie

```
Maatregel (abstract)
    └── Afwijkende maatregel
    └── Boete
    └── Maatregel op uitkering
```

## Relatiediagrammen

```
Afwijkende maatregel [1..1] ──── Maatregel op uitkering [1..1] (refereert)
Normafwijking [0..1] ──── Maatregel [1..1] (Normafwijking leidt tot Maatregel)
```

## Observaties

- Dit beleidsdomein bevat 5 Objecttype-entiteiten (+ 5 Enumeraties).
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Diagram GGM en Inkomen (1), Normafwijking (5).
- Er zijn 3 generalisatierelaties aanwezig.
