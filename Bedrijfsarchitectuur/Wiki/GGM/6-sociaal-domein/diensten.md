---
type: ggm-beleidsdomein
naam: Diensten
definitie: "Het Dienstenmodel biedt een gestructureerde weergave van de processen en objecttypen die betrokken zijn bij het leveren van diensten binnen het sociaal domein. Het model richt zich op de relaties tussen aanvragen, besluiten, rechten en voorwaarden die de basis vormen voor het verstrekken van voorzieningen."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 22
---

# GGM Beleidsdomein: Diensten

Onderdeel van beleidsdomein **Inkomen** binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanvraag** | Het officiële verzoek met het oogmerk om te komen tot toelating tot de dienstverlening zoals beschreven in de Participatiewet, schriftelijk ingediend bij het bestuursorgaan dat bevoegd is op het verzoek te beslissen. Het verzoek moet voldoen aan de wettelijke vereisten zoals bepaald in artikel 4.2 van de Algemene Bestuurswet. | Aanvraagdatum, AanvraagId, Code ontvangende gemeente | Nee | GGM |
| **Aanvraagtype** | Een door de gemeente vastgestelde set van diensttypen die met één aanvraag kan worden aangevraagd. | AanvraagtypeId, Einddatum, Naam, Soort Aanvraag, Startdatum | Nee | GGM |
| **Beschikking** | Een voor beroep vatbaar overheidsbesluit. Veelal de op schrift gestelde juridische motivering van de beslissing, met vermelding van de bezwaar en beroepsmogelijkheden. | Datum beschikking | Nee | GGM |
| **Besluit** | Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval. | Datum beslissing | Nee | GGM |
| **Betalingsblokkade** | Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De belatingsblokkade wordt opgenomen bij de dienst, die wordt genten door de persoon. | Aanduiding, Direct blokkeren, Initiële aanmaakdatum, Reden | Nee | GGM |
| **Dienst** | Een door de burger of bedrijf afgenomen dienst als een uit het aanbod van een overheidsorgaan in het kader van de Participatiewet.Let wel! Het gaat hier om dienst als de uiteindelijke levering van een diensttype op een aanvraag. | Aantal kostendelers, Begindatum, DienstId, Einddatum, Periodiciteit statusformulier, Startdatum statusformulier | Nee | GGM |
| **Diensttype** | Het resultaat of effect van een afgeronde inspanning die een overheidsorgaan op basis van wettelijke taken levert en waarmee in een behoefte van een burger (of bedrijf) wordt voorzien. De daadwerkelijke levering van een dienst, meestal in de vorm van een financiële betaling. | Duur referteperiode, Einddatum, minBetrouwbaarheidsniveau, Naam, Periodiciteit, Periodiciteit inkomstenformulier, Startdatum, Type referteperiodebepaling | Nee | GGM |
| **Individuele plicht** | De individueel bepaalde vooraf gestelde eisen, los van de bij wet genoemde geldende toelatingseisen tot de dienstverlening, die gesteld worden om de dienst te kunnen (blijven) afnemen. | *(geen attributen)* | Nee | GGM |
| **Leveringscomponent** | Een samenstellend deel van een Dienst. Bijvoorbeeld een gezinsnorm, een maatregel op de uitkering of bij een fysiek product: een koelkast.Nadat het recht is bepaald, wordt de levering gespecificeerd. Bij een financieel product is dat de hoogte van het bedrag. De hoogte van het bedrag is opgebouwd uit componenten waarvan de relevantie weer wordt bepaald door het recht en de situatie. Hoe het ook zij, de specificatie van de levering wordt in haar componenten vastgelegd als Leveringscomponent. | Bedrag, Einddatum, Gevalsrubriek, Omschrijving afwijking, Percentage, Periode startdatum, Soort | Nee | GGM |
| **Leveringscomponenttype** | Een samenstellend deel van het product dat word geleverd, bijvoorbeeld in het geval van een fysieke product:Product = huisraadDeelproduct 1= bankstel,Deelproduct 2 = eettafel, etc.Of in het geval van een financieel product Product = IITIIT-norm alleenstaande | Afwijkende norm, Einddatum, Fiscaal, Kostensoort, Normbedrag, Normpercentage, Rubriek, Soort wettelijke norm, Startdatum | Nee | GGM |
| **Leveringsopdracht** | Een informatieobject dat wordt uitgewisseld tussen twee bedrijfsfuncties, waarvan de één de inhoudelijke afhandeling heeft gedaan en de ander de uitvoering moet verrichten. De leveringsopdracht bevat de nodige gegevens om de levering te kunnen uitvoeren.De daadwerkelijke levering van de dienst, hetzij in natura, hetzij in uitkering, wordt door een andere bedrijfsfunctie uitgevoerd. Hiertoe moet een leveringsopdracht worden opgesteld. Dit bedrijfsobject is meer een koppelvlakbeschrijving over gegevens uit het behandelproces, dan een uit te werken concept in de ontologie. | Leveringskanaal | Nee | GGM |
| **Leveringsspecificatie** | De specificatie van de te leveren dienst.Nadat het recht is bepaald, wordt de levering gespecificeerd. Bij een financieel product is dat de hoogte van het bedrag. De hoogte van het bedrag is opgebouwd uit componenten waarvan de relevantie weer wordt bepaald door het recht en de situatie. Hoe het ook zij, de Leveringsspecificatie wordt in haar Leveringscomponenten vastgelegd. | Periode einddatum, Periode startdatum, Periodiciteit | Nee | GGM |
| **Onderdeel beschikking** | Een beschikking is een voor beroep vatbaar overheidsbesluit. Veelal de op schrift gestelde juridische motivering van de beslissing, met vermelding van de bezwaar en beroepsmogelijkheden. Omdat de aangevraagde dienst uit meerdere onderdelen bestaat en op elk onderdeel wordt beslist, zijn deze beslissingen en hun juridische motivering opgenomen als onderdelen in de beschikking. | Datum beschikking diensttype, Reden beschikking diensttype | Nee | GGM |
| **Periodiek dienst Bijz. bijstand** | Dit concept is redundant met leveringscomponenten in een leveringsspecificatie.De bijzondere bijstand hier bedoeld moet worden opgevoerd als een apart diensttypeDe kostensoort moet worden opgevoerd als een leveringscomponenttype bij het diensttype Bijzondere bijstandBij recht op de dienst bevat de leveringsspecificatie de relevante kostensoorten als leveringscomponenten met het vastgestelde bedrag. | Bedrag, Einddatum, Fiscaal, Kostensoort, Periodiciteit, Startdatum | Nee | GGM |
| **Recht** | Het bepaalde recht op het verkrijgen van een dienst. Het recht is opgebouwd uit conclusies op relevante voorwaarden voor het verkrijgen van een dienst. | Begindatum van het recht, Beschrijving, Einddatum van het recht, RechtId, Vaststeldatum van het recht | Nee | GGM |
| **Referteperiode** | De referteperiode bij een dienst is die periode waarover gegevens bij de aanvraag worden verzameld om op basis daarvan tot een beslissing te komen. | Einddatum, Startdatum | Nee | GGM |
| **Regeling** | Bijvoorbeeld Participatiewet, IOAW/IOAZ e.d. | Beschrijving, Einddatum, Naam, Startdatum | Nee | GGM |
| **Uitsluitingsgrond** | Gronden waarop de klant in een situatie verkeert die maakt dat er per definitie geen recht op een dienst c.q. uitkering bestaat. Dit maakt een uitsluitingsgrond een verbijzondering van een voorwaarde. | Type, Uitsluitingsgrond Id | Nee | GGM |
| **Verstrekkingsvorm** | De aard van afgifte van het product aan de burger (of bedrijf). Dit kan bijvoorbeeld zijn als gift, als lening, onder verband van hypotheek, … | Naam, Type | Nee | GGM |
| **Voorliggende voorziening** | Voorzieningen die de klant heeft, of waar hij voor in aanmerking komt, die de klant in een situatie doen verkeren die maakt dat er geen dienst c.q. uitkering toegekend wordt. Dit maakt dat de controle op een voorliggende voorziening een verbijzondering is van een voorwaarde. | Type, Voorliggende voorziening Id | Nee | GGM |
| **Voorwaarde** | De voorwaarde is de instantie van een **relevant** voorwaardetype bij een dienst, waarvan de conclusie wordt vastgelegd en daarmee een onderdeel vormt van het recht op het verkrijgen van een dienst. | Brontype, Conclusie, Vastleggingsdatum, Verantwoording vaststelling | Nee | GGM |
| **Voorwaardetype** | Een by design ontworpen voorwaarde waarop de aanvraag voor een diensttype kan worden beoordeeld.Het betreft hier alle mogelijke voorwaarden voor elke situatie. Welke voorwaardetypen relevant zijn voor een situatie wordt bepaald uit het profiel van de aanvrager(s).De voorwaardetypen worden ontwikkeld en in compliance gehouden met geldende gezagsdragende documenten als wet-en regelgeving, circulaires en beleid. | Beschrijving, VoorwaardetypeId | Nee | GGM |

## Overervingshiërarchie

```
Voorwaarde (abstract)
    └── Uitsluitingsgrond
    └── Voorliggende voorziening
```

## Relatiediagrammen

```
Client [1] ──── Aanvraag [0..*] (doet aanvraag)
Client [1..2] ──── Dienst [0..*] (neemt dienst af)
Leveringscomponent [0..*] ──── Kostenplaats [0..1] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 22 entiteiten.
- Er zijn 2 generalisatierelaties aanwezig.
