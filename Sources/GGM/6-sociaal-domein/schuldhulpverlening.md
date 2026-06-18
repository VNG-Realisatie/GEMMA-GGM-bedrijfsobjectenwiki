---
type: ggm-beleidsdomein
naam: Schuldhulpverlening
definitie: "Alle objecten die in het kader van schuldhulpverlening worden toegepast. Dit model is opgesteld in het kader van het programma DDAS (Data Delen Armoede en Schulden)"
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 29
---

# GGM Beleidsdomein: Schuldhulpverlening

Onderdeel van beleidsdomein **Schulden** binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanmelding** | Moment dat een persoon met een hulpvraag komt rondom (dreigende) schulden. Dit kan een persoonlijke, schriftelijke, digitale of telefonische vraag zijn. | startdatum, einddatum, crisisinterventie | Nee | GGM |
| **Begeleiding** | Begeleiding voor clienten in het kader van schuldhulpdienstverlening. | startdatum, einddatum, soort | Nee | GGM |
| **Begeleidingssoort** | Soort begeleiding in het kader van schuldhulpverlening | soort | Nee | GGM |
| **Contactpersoon** | Contactpersoon van een organisatie | naam, telefoonnummer, email, functietitel | Nee | GGM |
| **Crisisinterventie** | Het afwenden van een crisis- of dreigende situatie om zo de mogelijkheid te cre&#235;ren om de klant te helpen via de reguliere schuldhulpverlening. Volgens de Wgs gaat het in elk geval om de volgende situaties: ■ gedwongen woningontruiming; ■ be&#235;indiging van de levering van gas, water, elektriciteit of stadsverwarming; ■ opzegging of ontbinding van de zorgverzekering. Gemeenten kunnen extra situaties toevoegen aan hun crisisprotocol, zoals: ■ aangekondigde boedelverkoop of verkoop van de eigen woning; ■ loon- of bankbeslag; ■ een faillissementsaanvraag. En voor ondernemers: ■ beslag op (on)roerende zaken dat het voortbestaan van de onderneming bedreigt; ■ opzegging van het bankkrediet. | startdatum, einddatum | Nee | GGM |
| **InformatieEnAdvies** | <font color="#1e1d3a">Het betreft hier de activiteiten die in het kader van Informatie en advies worden uitgevoerd. Het doel van Informatie en Advies is inwoners zelf in staat te stellen een duurzaam financieel evenwicht te bereiken. Het kan een beroep op uitgebreidere vormen van dienstverlening overbodig maken.</font> | startdatum, einddatum | Nee | GGM |
| **Inkomen** | Inkomen dat door een persoon wordt verworven uit verschillende mogelijke inkomstenbronnen: inkomen uit arbeid, inkomen uit eigen onderneming, uitkering inkomensverzekeringen en uitkering sociale voorzieningen (m.u.v. kinderbijslag en kindgebonden budget). Premies inkomensverzekeringen (m.u.v. premies voor volksverzekeringen) zijn hierop in mindering gebracht. | startdatum, inkomstenbron, inkomenscategorie, brutoBedrag, einddatum, nettoBedrag | Nee | GGM |
| **Intake** | Dit is de fase tussen het eerste gesprek en het Plan van Aanpak. Tijdens de intakefase wordt geinventariseerd welke instrumenten, ondersteuning, activiteiten en gegevens nodig zijn om een duurzaam financieel evenwicht te bereiken. | startdatum, einddatum, beschikkingsdatum, beschikkingssoort | Nee | GGM |
| **Leefsituatie** | Leefsituatie is de combinatie van factoren zoals schulden, ondernemerschap, aanwezigheid van een partner, en inkomen, die samen de sociale en economische omstandigheden van een individu bepalen. Deze wordt in het kader van schuldhulpverlening gebruikt om alle relevante zaken van clienten aan te koppelen. | datumGeldigVanaf, datumGeldigTot | Nee | GGM |
| **Model Vroegsignalering** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Moratorium** | Het gaat hier om de datum waarop een verzoek tot een moratorium (ex art. 287 b Fw) is ingediend bij de rechter. Er kan een verzoek tot een moratorium bij de rechter worden gedaan om te voorkomen dat een schuldeiser zijn specifieke inningsmogelijkheden gebruikt, terwijl een aanvraag voor een minnelijke schuldregeling in behandeling is. Het moratorium is bedoeld om het minnelijke traject te kunnen voortzetten. Het moratorium kan in de volgende situaties worden ingezet: - gedwongen woningontruiming; - be&#235;indiging van de levering van gas, water elektriciteit of stadsverwarming; - opzegging dan wel ontbinding van de zorgverzekering. Het moratorium duurt maximaal zes maanden. | datumAanvraag, datumGoedkeuring, startdatum, einddatum | Nee | GGM |
| **Nazorg** | Ondersteuning die een persoon ontvangt n&#225; een schuldhulptraject, om zo bij de start van een schuldenvrij leven zelfredzaamheid verder te bevorderen &#233;n recidive (terugval) te voorkomen. | startdatum, einddatum | Nee | GGM |
| **Ondernemer** | Een ondernemer is een individu die die goederen of diensten levert aan anderen om winst te maken. | startdatum, einddatum | Nee | GGM |
| **Oplossing** | <font color="#0e0e0e">In de schuldhulpverlening verwijst een “oplossing” naar een regeling waarbij schulden op een beheersbare manier worden afgelost of kwijtgescholden, met als doel de financi&#235;le situatie van de schuldenaar te stabiliseren. Er worden verschillende oplossingsvormen onderscheiden, waaronder saneringskrediet, schuldbemiddeling, herfinanciering, betalingsregelingen en schuldregelingen zonder afloscapaciteit. Bij een saneringskrediet ontvangt de schuldenaar een lening om alle schuldeisers in &#233;&#233;n keer af te betalen, waarna hij deze lening aflost aan de kredietverstrekker. Schuldbemiddeling houdt in dat de schuldenaar gedurende een afgesproken periode periodiek bedragen aflost aan de schuldeisers. Herfinanciering betreft het vervangen van bestaande schulden door een nieuwe lening met gunstigere voorwaarden. Een betalingsregeling is een afspraak tussen schuldenaar en schuldeiser om de schuld in termijnen af te lossen. Bij een schuldregeling zonder afloscapaciteit wordt vastgesteld dat de schuldenaar geen financi&#235;le ruimte heeft om af te lossen, wat kan leiden tot kwijtschelding van de schuld. Deze oplossingsvormen worden ingezet afhankelijk van de specifieke situatie van de schuldenaar en zijn gericht op een duurzame oplossing van de schuldenproblematiek. </font> | startdatum, einddatum, soort, vtlb | Nee | GGM |
| **Oplossingssoort** | De soort oplossing in het kader van Schuldhulpverlening | soort | Nee | GGM |
| **Partner** | Een partner is een persoon met wie iemand een romantische en vaak langdurige relatie heeft, gebaseerd op wederzijdse liefde, steun en commitment. | samenwonend, datumVanaf, datumTot, getrouwdOfGeregistreerdPartner | Nee | GGM |
| **PlanVanAanpak** | Een document waarin in elk geval het volgende staat: ■ de hulpvraag van de persoon; ■ de voorgestelde ondersteuning; ■ eventueel de organisatie(s) waarnaar je hebt doorverwezen; ■ de voorwaarden voor schuldhulpverlening (bijvoorbeeld dat de persoon geen nieuwe schulden mag maken). De hoogte van beslagvrije voet voor de persoon (zie artikel 4a:5 van de Wgs) moet in acht worden genomen. | datumAfronding | Nee | GGM |
| **Schuld** | Een schuld is een financi&#235;le verplichting waarbij een persoon nu of in de toekomst een bedrag moet betalen aan een derde. In het kader van schuldhulpverlening wordt over een schuld gesproken als de persoon niet aan deze verplichting kan voldoen. . | bedrag, peildatum, zakelijkeSchuld, schuldsoort | Nee | GGM |
| **Schuldeiser** | Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar. In de meeste gevallen is de prestatie het betalen van geld. Dit geldbedrag is dan de schuld die de schuldenaar aan de schuldeiser moet betalen. De schuld is meestal het gevolg van het niet nakomen van een verplichting uit een overeenkomst tussen de partijen. De schuldeiser kan de schuldenaar dwingen om de schuld te voldoen. | peildatum, naam | Nee | GGM |
| **Schuldhulporganisatie** | Een schuldhulporganisatie is een instantie die individuen en gezinnen helpt met het beheren, verminderen en oplossen van hun schulden door middel van advies, begeleiding en bemiddeling. Het betreft een gemeenten of een SHV-organisatie die de gemeentelijke schuldhulpverleningstaak vanuit een gemeente gemandateerd of gedelegeerd heeft. | naam | Nee | GGM |
| **Schuldhulptraject** | Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert. | omschrijving, startdatum, einddatum, toekenningsdatum, totaalSchuldbedragBijAanvangSchuld | Nee | GGM |
| **Schuldregeling** | De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit (of op andere wijze vastgestelde minimale afdracht) lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt. Voordat de schuldregeling start, sluit je een schuldregelingsovereenkomst met de schuldenaar. Daarin staan de rechten en plichten van beide partijen. Een schuldregeling kan met een saneringskrediet of een schuldbemiddeling gerealiseerd worden. Als een of meer schuldeisers blijven weigeren in te stemmen met de minnelijke schuldregeling, informeer je de schuldenaar over mogelijke vervolgstappen, zoals het aanvragen van een dwangakkoord (artikel 287a Fw) of toelating tot de Wsnp. | datum, toegekend, afgewezen, ingetrokken, dwangakkoord, datumVerzoekDwangakkoord | Nee | GGM |
| **Stabilisatie** | Fase van het schuldhulpverleningstraject met als doel de inkomsten en uitgaven van een persoon in evenwicht te brengen. De stabilisatie van inkomen en uitgaven is een resultaat van werkzaamheden uit het plan van aanpak. Als stabilisatie bereikt is kan een betalingsregeling, herfinanciering of schuldregeling worden opgezet. Een belangrijk tweede doel is om de hulpvrager hierbij schuldenrust te bieden: stress wegnemen en tijd maken voor oplossingen naar een schuldenzorgvrije toekomst. In de stabilisatiefase kan een schuldhulpverlener andere instrumenten, activiteiten of ondersteuning inzetten, die bijdragen aan de duurzame oplossing van het financi&#235;le probleem, zoals budgetcoaching, budgetbeheer, beschermingsbewind of flankerende hulp. | startdatum, einddatum | Nee | GGM |
| **Uitstroom** | Het betreft hier de gegevens die worden vastgelegd bij uitstroom en dus be&#235;indiging van een schuldhulptraject. | omschrijving, datum, reden, datumBeeindigingsbeschikking | Nee | GGM |
| **VoorlopigeVoorziening ** | <font color="#0e0e0e">Een voorlopige voorziening is een tijdelijke regeling die de hulpvrager beschermt tegen verslechtering van zijn financi&#235;le situatie of het verlies van essenti&#235;le voorzieningen (zoals energie, woning, zorg), totdat een schuldregelingstraject is gestart of er meer duidelijkheid is over de vervolgstappen.</font> <font color="#0e0e0e"> </font><font color="#0e0e0e">Voorbeelden van voorlopige voorzieningen:</font> <font color="#0e0e0e"> • Tijdelijke betalingsregelingen met schuldeisers</font> <font color="#0e0e0e"> • Een moratorium (tijdelijke opschorting van afbetalingen)</font> <font color="#0e0e0e"> • Het aanvragen van uitstel van betaling bij woningcorporaties of energiebedrijven</font> <font color="#0e0e0e"> • Hulp bij het voorkomen van afsluiting van gas, water, licht of ontruiming</font> <font color="#0e0e0e"> • Budgetbeheer of beschermingsbewind als tijdelijke maatregel</font> | startdatum, einddatum | Nee | GGM |
| **Vroegsignalering** | *Vroegsignalering* is het proces waarbij gemeenten **vroegtijdig signalen van (potentiële) problemen bij inwoners in beeld brengen** om sneller passende hulp te kunnen bieden en escalatie van problemen te voorkomen. | *(geen attributen)* | Nee | GGM |
| **WSNP-traject** | Een WSNP-traject (Wet schuldsanering natuurlijke personen) is een wettelijk regeling in Nederland waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen. | datumVerzoek, datumGoedkeuring, startdatum, einddatum | Nee | GGM |
| **WSNP-verklaring** | Een WSNP-verklaring is een officieel document dat bevestigt dat een persoon toegelaten is tot de Wet Schuldsanering Natuurlijke Personen (WSNP) om hun schulden onder toezicht van een bewindvoerder af te lossen. | *(geen attributen)* | Nee | GGM |
| **Woningbezit** | Een koopwoning is een woning die eigendom is van een individu of een entiteit, die het heeft gekocht en waarvoor meestal een hypotheek is afgesloten. | startdatum, einddatum, soort | Nee | GGM |

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
Aanmelding [1] ──── Intake [0..1] (resulteert in)
Begeleiding [0..*] ──── Begeleidingssoort [1] (soort)
Begeleiding [0..1] ──── Nazorg [0..1] (resulteert in)
Client [1] ──── Leefsituatie [0..*] (heeft financiele situatie)
Intake [0..1] ──── Begeleiding [0..*] (resulteert in)
Intake [0..1] ──── InformatieEnAdvies [0..1] (resulteert in)
Intake [1] ──── Stabilisatie [0..1] (resulteert in )
Leefsituatie [1] ──── Inkomen [0..*] (heeft)
Leefsituatie [1] ──── Ondernemer [0..1] (is)
Leefsituatie [0..1] ──── Partner [0..*] (heeft)
Leefsituatie [0..*] ──── Woningbezit [0..*] (heeft)
Oplossing [0..1] ──── Nazorg [0..1] (resulteert in)
Oplossing [0..*] ──── Oplossingssoort [1] (soort)
Schuld [0..*] ──── Schuldeiser [1] (schuld bij)
Schuldhulporganisatie [0..*] ──── Begeleidingssoort [0..*] (dienstverlening)
Schuldhulporganisatie [1..*] ──── Contactpersoon [0..*] (heeft)
Schuldhulporganisatie [0..*] ──── Oplossingssoort [0..*] (dienstverlening)
Schuldhulporganisatie [1..*] ──── Schuldhulptraject [0..*] (voert traject uit)
Schuldhulptraject [1] ──── Aanmelding [0..1] (bevat)
Schuldhulptraject [1] ──── Begeleiding [0..*] (bevat)
Schuldhulptraject [0..*] ──── Client [1..2] (heeft traject)
Schuldhulptraject [1] ──── Crisisinterventie [0..*] (kan hebben)
Schuldhulptraject [0..*] ──── Gemeente [1] (onder verantwoordelijkheid van)
Schuldhulptraject [1] ──── InformatieEnAdvies [0..1] (bevat)
Schuldhulptraject [1] ──── Intake [0..1] (bevat)
Schuldhulptraject [1] ──── Moratorium [0..*] (kan hebben)
Schuldhulptraject [1] ──── Nazorg [0..1] (bevat)
Schuldhulptraject [1] ──── Oplossing [0..1] (bevat)
Schuldhulptraject [1] ──── PlanVanAanpak [0..1] (heeft)
Schuldhulptraject [1] ──── Schuld [0..*] (heeft)
Schuldhulptraject [1] ──── Schuldregeling [0..1] (bevat)
Schuldhulptraject [1] ──── Stabilisatie [0..1] (bevat)
Schuldhulptraject [1] ──── Uitstroom [0..1] (uitstroom)
Schuldhulptraject [1] ──── VoorlopigeVoorziening  [0..*] (heeft)
Schuldregeling [0..1] ──── Begeleiding [0..*] (resulteert in)
Schuldregeling [1] ──── Oplossing [0..1] (resulteert in)
Stabilisatie [0..1] ──── Begeleiding [0..*] (resulteert in)
Stabilisatie [1] ──── Schuldregeling [0..1] (resulteert in)
WSNP-traject [0..*] ──── Leefsituatie [1] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 29 entiteiten.
- Er zijn 3 generalisatierelaties aanwezig.
