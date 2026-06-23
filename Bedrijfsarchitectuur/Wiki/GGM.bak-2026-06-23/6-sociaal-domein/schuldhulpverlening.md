---
type: ggm-beleidsdomein
naam: Schuldhulpverlening
definitie: "Alle objecten die in het kader van schuldhulpverlening worden toegepast. Dit model is opgesteld in het kader van het programma DDAS (Data Delen Armoede en Schulden)"
taakveld: "Schulden"
aantal_entiteiten: 27
---

# GGM Beleidsdomein: Schuldhulpverlening

### Schuldhulp Client

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Inkomen** | Inkomen dat door een persoon wordt verworven uit verschillende mogelijke inkomstenbronnen: inkomen uit arbeid, inkomen uit eigen onderneming, uitkering inkomensverzekeringen en uitkering sociale voorzieningen (m.u.v. kinderbijslag en kindgebonden budget). Premies inkomensverzekeringen (m.u.v. premies voor volksverzekeringen) zijn hierop in mindering gebracht. | startdatum, inkomstenbron, inkomenscategorie, brutoBedrag, einddatum, nettoBedrag | Nee | GGM |
| **Leefsituatie** | Leefsituatie is de combinatie van factoren zoals schulden, ondernemerschap, aanwezigheid van een partner, en inkomen, die samen de sociale en economische omstandigheden van een individu bepalen. Deze wordt in het kader van schuldhulpverlening gebruikt om alle relevante zaken van clienten aan te koppelen. | datumGeldigVanaf, datumGeldigTot | Nee | GGM |
| **Ondernemer** | Een ondernemer is een individu die die goederen of diensten levert aan anderen om winst te maken. | startdatum, einddatum | Nee | GGM |
| **Partner** | Een partner is een persoon met wie iemand een romantische en vaak langdurige relatie heeft, gebaseerd op wederzijdse liefde, steun en commitment. | samenwonend, datumVanaf, datumTot, getrouwdOfGeregistreerdPartner | Nee | GGM |
| **Schuld** | Een schuld is een financiële verplichting waarbij een persoon nu of in de toekomst een bedrag moet betalen aan een derde. In het kader van schuldhulpverlening wordt over een schuld gesproken als de persoon niet aan deze verplichting kan voldoen. . | bedrag, peildatum, zakelijkeSchuld, schuldsoort | Nee | GGM |
| **Schuldeiser** | Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar. In de meeste gevallen is de prestatie het betalen van geld. Dit geldbedrag is dan de schuld die de schuldenaar aan de schuldeiser moet betalen. De schuld is meestal het gevolg van het niet nakomen van een verplichting uit een overeenkomst tussen de partijen. De schuldeiser kan de schuldenaar dwingen om de schuld te voldoen. | peildatum, naam | Nee | GGM |
| **Schuldhulptraject** | Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert. | omschrijving, startdatum, einddatum, toekenningsdatum, totaalSchuldbedragBijAanvangSchuld | Nee | GGM |
| **Woningbezit** | Een koopwoning is een woning die eigendom is van een individu of een entiteit, die het heeft gekocht en waarvoor meestal een hypotheek is afgesloten. | startdatum, einddatum, soort | Nee | GGM |

### Schuldhulp Hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Schuldhulporganisatie** | Een schuldhulporganisatie is een instantie die individuen en gezinnen helpt met het beheren, verminderen en oplossen van hun schulden door middel van advies, begeleiding en bemiddeling. Het betreft een gemeenten of een SHV-organisatie die de gemeentelijke schuldhulpverleningstaak vanuit een gemeente gemandateerd of gedelegeerd heeft. | naam | Nee | GGM |

### Schuldhulp Schuldhulporganisatie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Begeleiding** | Begeleiding voor clienten in het kader van schuldhulpdienstverlening. | startdatum, einddatum, soort | Nee | GGM |
| **Begeleidingssoort** | Soort begeleiding in het kader van schuldhulpverlening | soort | Nee | GGM |
| **Contactpersoon** | Contactpersoon van een organisatie | naam, telefoonnummer, email, functietitel | Nee | GGM |
| **Oplossing** | In de schuldhulpverlening verwijst een “oplossing” naar een regeling waarbij schulden op een beheersbare manier worden afgelost of kwijtgescholden, met als doel de financiële situatie van de schuldenaar te stabiliseren. Er worden verschillende oplossingsvormen onderscheiden, waaronder saneringskrediet, schuldbemiddeling, herfinanciering, betalingsregelingen en schuldregelingen zonder afloscapaciteit. Bij een saneringskrediet ontvangt de schuldenaar een lening om alle schuldeisers in één keer af te betalen, waarna hij deze lening aflost aan de kredietverstrekker. Schuldbemiddeling houdt in dat de schuldenaar gedurende een afgesproken periode periodiek bedragen aflost aan de schuldeisers. Herfinanciering betreft het vervangen van bestaande schulden door een nieuwe lening met gunstigere voorwaarden. Een betalingsregeling is een afspraak tussen schuldenaar en schuldeiser om de schuld in termijnen af te lossen. Bij een schuldregeling zonder afloscapaciteit wordt vastgesteld dat de schuldenaar geen financiële ruimte heeft om af te lossen, wat kan leiden tot kwijtschelding van de schuld. Deze oplossingsvormen worden ingezet afhankelijk van de specifieke situatie van de schuldenaar en zijn gericht op een duurzame oplossing van de schuldenproblematiek. | startdatum, einddatum, soort, vtlb | Nee | GGM |
| **Oplossingssoort** | De soort oplossing in het kader van Schuldhulpverlening | soort | Nee | GGM |

### Schuldhulpproces

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanmelding** | Moment dat een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn. | startdatum, einddatum, crisisinterventie | Nee | GGM |
| **Crisisinterventie** | Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te creëren om de klant te helpen via de reguliere schuldhulpverlening. Volgens de Wgs gaat het in elk geval om de volgende situaties: ■ gedwongen woningontruiming; ■ beëindiging van de levering van gas, water, elektriciteit of stadsverwarming; ■ opzegging of ontbinding van de zorgverzekering. Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals: ■ aangekondigde boedelverkoop of verkoop van de eigen woning; ■ loon- of bankbeslag; ■ een faillissementsaanvraag. En voor ondernemers: ■ beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt; ■ opzegging van het bankkrediet. | startdatum, einddatum | Nee | GGM |
| **InformatieEnAdvies** | Het betreft hier de activiteiten die in het kader van Informatie en advies worden uitgevoerd. Het doel van Informatie en Advies is inwoners zelf in staat te stellen een duurzaam financieel evenwicht te bereiken. Het kan een beroep op uitgebreidere vormen van dienstverlening overbodig maken. | startdatum, einddatum | Nee | https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Informatie--Advies?originNode=1401 |
| **Intake** | Dit is de fase tussen het eerste gesprek en het Plan van Aanpak. Tijdens de intakefase wordt geinventariseerd welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een duurzaam financieel evenwicht te bereiken. | startdatum, einddatum, beschikkingsdatum, beschikkingssoort | Nee | GGM |
| **Moratorium** | Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter. Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is. Het moratorium is bedoeld om het minnelijke traject te kunnen voortzetten. Het moratorium kan in de volgende situaties worden ingezet: - gedwongen woningontruiming; - beëindiging van de levering van gas, water elektriciteit of stadsverwarming; - opzegging dan wel ontbinding van de zorgverzekering. Het moratorium duurt maximaal zes maanden. | datumAanvraag, datumGoedkeuring, startdatum, einddatum | Nee | GGM |
| **Nazorg** | Ondersteuning die een persoon ontvangt ná een schuldhulptraject, om zo bij de start van een schuldenvrij leven zelfredzaamheid verder te bevorderen én recidive (terugval) te voorkomen. | startdatum, einddatum | Nee | GGM |
| **PlanVanAanpak** | Een document waarin in elk geval het volgende staat: ■ de hulpvraag van de persoon; ■ de voorgestelde ondersteuning; ■ eventueel de organisatie(s) waarnaar je hebt doorverwezen; ■ de voorwaarden voor schuldhulpverlening (bijvoorbeeld dat de persoon geen nieuwe schulden mag maken). De hoogte van beslagvrije voet voor de persoon (zie artikel 4a:5 van de Wgs) moet in acht worden genomen. | datumAfronding | Nee | GGM |
| **Schuldregeling** | De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit (of op andere wijze vastgestelde minimale afdracht) lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt. Voordat de schuldregeling start, sluit je een schuldregelingsovereenkomst met de schuldenaar. Daarin staan de rechten en plichten van beide partijen. Een schuldregeling kan met een saneringskrediet of een schuldbemiddeling gerealiseerd worden. Als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregeling, informeer je de schuldenaar over mogelijke vervolgstappen, zoals het aanvragen van een dwangakkoord (artikel 287a Fw) of toelating tot de Wsnp. | datum, toegekend, afgewezen, ingetrokken, dwangakkoord, datumVerzoekDwangakkoord | Nee | GGM |
| **Stabilisatie** | Fase van het schuldhulpverleningstraject met als doel de inkomsten en uitgaven van een persoon in evenwicht te brengen. De stabilisatie van inkomen en uitgaven is een resultaat van werkzaamheden uit het plan van aanpak. Als stabilisatie bereikt is kan een betalingsregeling, herfinanciering of schuldregeling worden opgezet. Een belangrijk tweede doel is om de hulpvrager hierbij schuldenrust te bieden: stress wegnemen en tijd maken voor oplossingen naar een schuldenzorgvrije toekomst. In de stabilisatiefase kan een schuldhulpverlener andere instrumenten, activiteiten of ondersteuning inzetten, die bijdragen aan de duurzame oplossing van het financiële probleem, zoals budgetcoaching, budgetbeheer, beschermingsbewind of flankerende hulp. | startdatum, einddatum | Nee | GGM |
| **Uitstroom** | Het betreft hier de gegevens die worden vastgelegd bij uitstroom en dus beëindiging van een schuldhulptraject. | omschrijving, datum, reden, datumBeeindigingsbeschikking | Nee | GGM |
| **VoorlopigeVoorziening** | Een voorlopige voorziening is een tijdelijke regeling die de hulpvrager beschermt tegen verslechtering van zijn financiële situatie of het verlies van essentiële voorzieningen (zoals energie, woning, zorg), totdat een schuldregelingstraject is gestart of er meer duidelijkheid is over de vervolgstappen. Voorbeelden van voorlopige voorzieningen: • Tijdelijke betalingsregelingen met schuldeisers • Een moratorium (tijdelijke opschorting van afbetalingen) • Het aanvragen van uitstel van betaling bij woningcorporaties of energiebedrijven • Hulp bij het voorkomen van afsluiting van gas, water, licht of ontruiming • Budgetbeheer of beschermingsbewind als tijdelijke maatregel | startdatum, einddatum | Nee | GGM |
| **WSNP-traject** | Een WSNP-traject (Wet schuldsanering natuurlijke personen) is een wettelijk regeling in Nederland waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen. | datumVerzoek, datumGoedkeuring, startdatum, einddatum | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **WSNP-verklaring** | Een WSNP-verklaring is een officieel document dat bevestigt dat een persoon toegelaten is tot de Wet Schuldsanering Natuurlijke Personen (WSNP) om hun schulden onder toezicht van een bewindvoerder af te lossen. | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
NatuurlijkPersoon (abstract)
    └── Partner
```

```
NietNatuurlijkPersoon (abstract)
    └── Schuldhulporganisatie
```

```
Rechtspersoon (abstract)
    └── Schuldeiser
```

## Relatiediagrammen

```
Aanmelding ──── Intake
Begeleiding ──── Begeleidingssoort
Begeleiding ──── Nazorg
Intake ──── Begeleiding
Intake ──── InformatieEnAdvies
Intake ──── Stabilisatie
Leefsituatie ──── Inkomen
Leefsituatie ──── Ondernemer
Leefsituatie ──── Partner
Leefsituatie ──── Woningbezit
Oplossing ──── Nazorg
Oplossing ──── Oplossingssoort
Schuld ──── Schuldeiser
Schuldhulporganisatie ──── Begeleidingssoort
Schuldhulporganisatie [1..*] ──── Contactpersoon [0..*]
Schuldhulporganisatie ──── Oplossingssoort
Schuldhulporganisatie ──── Schuldhulptraject
Schuldhulptraject ──── Aanmelding
Schuldhulptraject ──── Begeleiding
Schuldhulptraject ──── Crisisinterventie
Schuldhulptraject ──── InformatieEnAdvies
Schuldhulptraject ──── Intake
Schuldhulptraject ──── Moratorium
Schuldhulptraject ──── Nazorg
Schuldhulptraject ──── Oplossing
Schuldhulptraject ──── PlanVanAanpak
Schuldhulptraject ──── Schuld
Schuldhulptraject ──── Schuldregeling
Schuldhulptraject ──── Stabilisatie
Schuldhulptraject ──── Uitstroom
Schuldhulptraject ──── VoorlopigeVoorziening 
Schuldregeling ──── Begeleiding
Schuldregeling ──── Oplossing
Stabilisatie ──── Begeleiding
Stabilisatie ──── Schuldregeling
WSNP-traject ──── Leefsituatie
```

## Observaties

- Dit beleidsdomein bevat 27 Objecttype-entiteiten (+ 7 Enumeraties, 2 diagramhulpobjecten zonder stereotype).
- Entiteiten zijn gegroepeerd in 4 diagramgroepen: Schuldhulp Client (8), Schuldhulp Hoofdlijnen (2), Schuldhulp Schuldhulporganisatie (7), Schuldhulpproces (17).
- Er zijn 3 generalisatierelaties aanwezig.
