---
type: ggm-beleidsdomein
naam: Inburgering
definitie: "Het informatiedomein dat gegevens omvat over de uitvoering van de Wet inburgering, gericht op het ondersteunen van inburgeraars bij hun integratie en participatie in de Nederlandse samenleving."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 35
---

# GGM Beleidsdomein: Inburgering

Beleidsdomein binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

### Inburgering

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aandachtspunt ** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Aandachtspunt</b></font><font color="#0e0e0e"> is een bijzonder aspect of omstandigheid in de persoonlijke situatie van de inburgeraar, dat extra aandacht vereist bij de begeleiding of dienstverlening in het kader van inburgering.</font> | aandachtspuntOmschrijving, StartDatum, EindDatum | Nee | GGM |
| **Aanvraag verlenging Inburgeringstermijn** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Aanvraag verlenging inburgeringstermijn</b></font><font color="#0e0e0e"> is een verzoek van een inburgeringsplichtige aan het college van burgemeester en wethouders tot verlenging van de inburgeringstermijn op grond van persoonlijke omstandigheden als bedoeld in artikel 7.3, tweede lid, van de Wet inburgering 2021.</font> | BeoordelingAanvraagVerlenging, VerlengingsGrond | Nee | GGM |
| **Asielstatushouder** | De Inburgeringsplichtige die rechtmatig verblijf heeft | Telefoonnummer verblijf AZC, Emailadres verblijf AZC, DigiD aangevraagd, Rijbewijs, Land Rijbewijs, Is gekoppeld aan | Nee | GGM |
| **B1-route** | <font color="#0e0e0e">De </font><font color="#0e0e0e"><b>B1-route</b></font><font color="#0e0e0e"> is &#233;&#233;n van de drie leerroutes in het inburgeringsstelsel, waarbij de inburgeringsplichtige zich voorbereidt op het afleggen van het inburgeringsexamen op taalniveau B1, gericht op brede participatie in de Nederlandse samenleving en toeleiding naar arbeid.</font> | ExamenDatum, Resultaat, RedenGeenResultaat, AantalGratisExamenpogingenTegoed, GevolgdeUrenParticipatieTaalles | Nee | GGM |
| **Brede Intake** | De Brede Intake in het sociaal domein is een gestructureerd proces waarbij een hulpverlener samen met een inwoner diens situatie, behoeften, en problemen in kaart brengt om tot een integraal beeld te komen van wat nodig is om passende ondersteuning te bieden. Hierbij wordt niet alleen gekeken naar specifieke hulpvragen, zoals schulden of werkloosheid, maar ook naar onderliggende factoren, zoals gezondheidsproblemen, woonsituatie, en sociaal netwerk. Het doel is om vanuit een holistisch perspectief samenhangende oplossingen te vinden en de inwoner te ondersteunen bij het versterken van zelfredzaamheid en participatie. | GevolgdeUrenKNMenTaalles, UrenGeoorloofdVerzuim, UrenOngeoorloofdVerzuim, DatumTot(Peildatum), AantalUrenAlfabetiseringsOnderwijs, startdatum, einddatum | Nee | GGM |
| **Diplomawaardering** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Diplomawaardering</b></font><font color="#0e0e0e"> is de beoordeling van een buitenlands diploma, certificaat of graad door het Informatiecentrum Diplomawaardering (IDW), met als doel het vaststellen van het Nederlandse opleidingsniveau waarmee dit diploma vergelijkbaar is.</font> | NiveauCompetentie, WaarderingAangevraagd, DiplomaWaarderingVoor, DiplomaWaarderingNederlandsNiveau, DiplomaWaarderingRichting | Nee | GGM |
| **Educatie** | <font color="#0e0e0e"><b>Educatie</b></font><font color="#0e0e0e"> betreft het formele en non-formele onderwijsaanbod dat gericht is op het vergroten van basisvaardigheden, zoals taalvaardigheid, rekenen en digitale vaardigheden, ter ondersteuning van participatie en zelfredzaamheid van (laagopgeleide) volwassenen, waaronder inburgeringsplichtigen.</font> | Opleiding, EducatieVan, EducatieTot, EducatieLand, EducatieDiploma, EducatieInBezit | Nee | GGM |
| **Examen** | Een Examen in de context van onderwijs is een formele toetsingsactiviteit waarmee de kennis, vaardigheden en competenties van een leerling of student worden beoordeeld ten opzichte van vooraf vastgestelde leerdoelen of eindtermen. Het examen kan schriftelijk, mondeling, digitaal of praktijkgericht zijn en vormt doorgaans een afsluiting van een cursus, module of opleiding. Het behalen van een examen kan leiden tot het verkrijgen van een diploma, certificaat of overgangsbewijs en is bedoeld om de voortgang en geschiktheid voor verdere studie of beroep te waarborgen. | ExamenResultaat | Nee | GGM |
| **Examenonderdeel** | Een Examenonderdeel in de context van onderwijs is een specifieke, afgebakende component van een examen waarin een deelaspect van de leerdoelen of eindtermen wordt getoetst. Het kan betrekking hebben op een specifiek vak, thema of vaardigheid en kan bestaan uit verschillende toetsvormen, zoals meerkeuzevragen, essays, praktijkopdrachten of mondelinge presentaties. Het examenonderdeel draagt bij aan de totaalscore of het eindresultaat van het examen en kan afzonderlijk beoordeeld en gewaardeerd worden. | ExamenOnderdeelSpecificatie, Resultaat, Ontheffing, RedenVrijstelling, DatumRegistratieUitslag, BehaaldeScore | Nee | GGM |
| **Gezinsmigrant en Overige migrant
** | Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant. Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en Overige Migrant zoals bijvoorbeeld: object Aanvraag Sociale Lening. Hetzelfde geldt ook voor object Asielstatushouder, deze heeft overigens wel kenmerken. | *(geen attributen)* | Nee | GGM |
| **Hoofddoel** | <font color="#0e0e0e">Het </font><font color="#0e0e0e"><b>Hoofddoel</b></font><font color="#0e0e0e"> is de door de gemeente vastgestelde eindbestemming van het inburgeringstraject, waarin wordt vastgelegd of de inburgeringsplichtige wordt begeleid richting werk, onderwijs of (maatschappelijke) participatie, op basis van de brede intake en het leerrouteadvies.</font> | Doel, StartDatum, EindDatum | Nee | GGM |
| **ICT-Vaardigheid** | <font color="#0e0e0e"><b>ICT-vaardigheid</b></font><font color="#0e0e0e"> betreft het vermogen van de inburgeringsplichtige om digitale middelen en toepassingen zelfstandig en doelgericht te gebruiken voor communicatie, informatieverwerking en deelname aan de samenleving.</font> | ICTVaardigheid, NiveauICTVaardigheid | Nee | GGM |
| **Inburgeraar** | De gemeente gaat inburgeringsplichtige nieuwkomers begeleiden bij hun inburgering. Voor asielstatushouders doen zij dit vanaf het moment van koppeling aan een gemeente | Gedetailleerde Doelgroep, Doelgroep | Nee | GGM |
| **InburgeringsAanbod** | <font color="#0e0e0e">Het </font><font color="#0e0e0e"><b>Inburgeringsaanbod</b></font><font color="#0e0e0e"> is het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen, zoals vastgelegd in het persoonlijk plan inburgering en participatie (PIP).</font> | DatumInburgeringsAanbod, DatumAanvangTaalschakelTraject, DatumEindeCursus, CursusInstelling, IndicatorAlfabetisering, TaalschakelTraject, DatumTaalschakelDiploma, ParticipatieDeelname, ContractId | Nee | GGM |
| **Inburgeringsplicht** | Bevat de uitkomst Leerbaarheidstoets dat een groot deel van de leerroutes bepaalt. Bevat mogelijk ook de Examenresultaten (nog toe te voegen als Ja). Dit zijn DUO berichten (Opvragen en per API beschikbaar stellen aan deze Entiteit/Attributen. | IndicatorInburgeringsplicht, UitkomstLeerbaarheidstoets, BeschikkingVoldaanInburgeringsplicht, V-nummer, InburgeraarSpecialisatie, DatumStart, DatumEind, RedenGeenInburgeringsplicht, DatumGewijzigdInburgeringsplicht, WordtBehandelsAls, DatumGewijzigdWordtBehandeldAls | Nee | GGM |
| **Inburgeringstermijn** | <font color="#0e0e0e">De </font><font color="#0e0e0e"><b>Inburgeringstermijn</b></font><font color="#0e0e0e"> is de wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, gerekend vanaf de startdatum van de verplichting zoals vastgesteld door DUO of de gemeente.</font> | DatumAanvangInburgeringstermijn, DatumEindeInburgeringstermijn, VooraankondigingBoete, BoeteBedrag, DatumBoete | Nee | GGM |
| **Inburgeringstraject** | Een Inburgeringstraject in de context van inburgering bij gemeenten is een persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving, en het ontwikkelen van vaardigheden om zelfstandig te participeren in de Nederlandse maatschappij. Het traject omvat doorgaans onderdelen zoals taallessen (NT2), kennis van de Nederlandse maatschappij (KNM), en participatieactiviteiten, zoals vrijwilligerswerk of een werkstage. Het inburgeringstraject wordt afgestemd op de behoeften, achtergrond en mogelijkheden van de nieuwkomer en heeft als doel hen te begeleiden naar maatschappelijke zelfredzaamheid en een actieve rol in de samenleving. | UItkomstLeerbaarheidstoets | Nee | GGM |
| **Introductiemodule** | <font color="#0e0e0e">De </font><font color="#0e0e0e"><b>Introductiemodule</b></font><font color="#0e0e0e"> is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige basisinformatie ontvangt over de Nederlandse samenleving, de inburgeringsplicht en het lokale voorzieningenaanbod, direct na de brede intake.</font> | ModuleNaam, DeelnameIntroductieModule | Nee | GGM |
| **Leerroute** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Leerroute</b></font><font color="#0e0e0e"> is het door de gemeente vastgestelde traject dat een inburgeringsplichtige volgt om te voldoen aan de inburgeringsplicht, bestaande uit taallessen, participatieactiviteiten en aanvullende modules, afgestemd op het leervermogen en het hoofddoel van de inburgeraar.</font> | LeerrouteType, Niveau, GeschatteIntensiteitB1Route, IndicatorAlfabetisering, IndicatorToestemmingExamenA2, IndicatorMagOpleidingAfmaken, geenLeerbaarheidstoetsZB, ExamenA2 | Nee | GGM |
| **MAP** | <font color="#0e0e0e">De </font><font color="#0e0e0e"><b>Module Arbeidsmarkt en Participatie (MAP)</b></font><font color="#0e0e0e"> is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige wordt voorbereid op deelname aan de Nederlandse arbeidsmarkt, door middel van voorlichting, ori&#235;ntatie en arbeidsmarktgerichte activiteiten.</font> | Resultaat, DatumEindgesprekMAP, RedenNietSuccesvolVoltooid, IndicatorVerwijtbaar | Nee | GGM |
| **Ontheffing** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Ontheffing</b></font><font color="#0e0e0e"> is een formeel besluit van de gemeente of van DUO waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt vrijgesteld van onderdelen van de inburgeringsplicht, op grond van persoonlijke omstandigheden zoals medische beperkingen, psychische problematiek of aantoonbare inspanning.</font> | BeslissingOntheffing, DatumOntheffing | Nee | GGM |
| **Ontwikkelwens ** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Ontwikkelwens</b></font><font color="#0e0e0e"> is een door de inburgeringsplichtige geuite persoonlijke ambitie of leerdoel die richting kan geven aan het inburgeringstraject, en wordt meegenomen bij het opstellen van het Persoonlijk Plan Inburgering en Participatie (PIP).</font> | ontwikkelwensOmschrijving, StartDatum, EindDatum | Nee | GGM |
| **PIP** | <font color="#0e0e0e">Het </font><font color="#0e0e0e"><b>Persoonlijk Plan Inburgering en Participatie (PIP)</b></font><font color="#0e0e0e"> is een individueel plan dat door de gemeente wordt vastgesteld in overleg met de inburgeringsplichtige, waarin het leerrouteadvies, het inburgeringsaanbod, het hoofddoel en de begeleidingsafspraken zijn vastgelegd, met als doel het succesvol afronden van de inburgering binnen de gestelde termijn.</font> | DagtekeningInitielePIP, DagtekeningPIP, NaamContactPersoon, EmailContactPersoon, IndicatorMagOpleidingAfmaken | Nee | GGM |
| **PVT** | <font color="#0e0e0e">Het </font><font color="#0e0e0e"><b>Participatieverklaringstraject (PVT)</b></font><font color="#0e0e0e"> is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige kennismaakt met de basiswaarden van de Nederlandse samenleving, en deze onderschrijft door het ondertekenen van de participatieverklaring.</font> | Resultaat, DatumOndertekening PVT, RedenNietVoldaan, VerwijtbaarNietVoldaan | Nee | GGM |
| **Subdoel Aandachtspunt** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Subdoel aandachtspunt</b></font><font color="#0e0e0e"> is een concreet, afgebakend leer- of begeleidingsdoel dat voortvloeit uit een gesignaleerd aandachtspunt in de persoonlijke situatie van de inburgeringsplichtige, en dat bijdraagt aan het wegnemen van belemmeringen voor het volgen van de leerroute of het behalen van het PIP-doel.</font> | Subdoel, Startdatum, Einddatum | Nee | GGM |
| **Subdoel Ontwikkelwens** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Subdoel ontwikkelwens</b></font><font color="#0e0e0e"> is een concreet, haalbaar leer- of ontwikkeldoel dat is afgeleid van een door de inburgeringsplichtige geuite ontwikkelwens, en dat richting geeft aan de invulling van het inburgeringstraject binnen het PIP.</font> | Subdoel, StartDatum, EindDatum | Nee | GGM |
| **Taalvaardigheid** | <font color="#0e0e0e"><b>Taalvaardigheid</b></font><font color="#0e0e0e"> is het niveau van beheersing van de Nederlandse taal door de inburgeringsplichtige, gemeten op onderdelen zoals luisteren, spreken, lezen en schrijven, overeenkomstig het Europees Referentiekader voor Talen (ERK).</font> | ToetsTaalleerbaarheid, Score, ResultaatToetsTaalleerbaarheid, ToetsSpreekvaardigheid, ResultaatToetsSpreekvaardigheid, OpleidingsniveauGeschat, TaallesActiviteit, StartVanTaallesActviteit, EindeVanTaallesActviteit, ResultaatTaalles, PresentieTaalles, TaalvaardigheidOverall, TaalvaardigheidMondeling, TaalvaardigheidSchriftelijk | Nee | GGM |
| **Training** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Training</b></font><font color="#0e0e0e"> is een gestructureerde leeractiviteit binnen het inburgeringstraject, gericht op het aanleren of versterken van specifieke vaardigheden of kennis ter ondersteuning van taalverwerving, participatie of persoonlijke ontwikkeling.</font> | TrainingGevolgd, PeriodeTraining, ResultaatTraining | Nee | GGM |
| **Verblijfplaats AZC** | <font color="#0e0e0e"><b>Verblijfplaats AZC</b></font><font color="#0e0e0e"> is de formele verblijfslocatie van een asielgerechtigde of inburgeringsplichtige binnen een Asielzoekerscentrum (AZC), beheerd door het Centraal Orgaan opvang Asielzoekers (COA), voorafgaand aan of tijdens het inburgeringstraject.</font> | Plaats, Straatnummer, Huisnummer | Nee | GGM |
| **Verlengingsgrond** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Verlengingsgrond</b></font><font color="#0e0e0e"> is een wettelijk erkende reden op basis waarvan de gemeente de inburgeringstermijn van een inburgeringsplichtige kan verlengen, zoals vastgelegd in artikel 7.3, tweede lid, van de Wet inburgering 2021.</font> | AanwezigheidAanvraagVerlening, VerlengingInWeken, Verlengingsgrondslag, DatumAanvangVerlengingsgrond, DatumEindeVerlengingsgrond, DatumBeoordelingVerlengingsgrond | Nee | GGM |
| **Voorbereiding op Inburgering** | <font color="#0e0e0e"><b>Voorbereiding op inburgering</b></font><font color="#0e0e0e"> omvat de activiteiten die worden aangeboden aan asielstatushouders v&#243;&#243;r de start van de formele inburgeringsplicht, gericht op ori&#235;ntatie op de Nederlandse samenleving, taal en het inburgeringsstelsel.</font> | InstemmingDeelnameVoorinburgering, DatumInstemming, Reden | Nee | GGM |
| **Vreemdeling** | Een Vreemdeling is een Natuurlijk Persoon die de Nederlandse Nationaliteit niet bezit en niet op grond van een wettelijke bepaling als Nederlander wordt behandeld. | v-nummer, Sociaal Referent | Nee | GGM |
| **Vrijstelling** | <font color="#0e0e0e">Een </font><font color="#0e0e0e"><b>Vrijstelling</b></font><font color="#0e0e0e"> is een formeel besluit waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt ontheven van specifieke onderdelen van de inburgeringsplicht, omdat deze reeds op andere wijze zijn behaald of niet van toepassing zijn, zoals bedoeld in artikel 7.2 van de Wet inburgering 2021.</font> | EindoordeelVrijstelling, DatumVrijstelling | Nee | GGM |
| **Werk** | <font color="#0e0e0e"><b>Werk</b></font><font color="#0e0e0e"> betreft het verrichten van betaalde arbeid door een inburgeringsplichtige, als onderdeel van of resultaat uit het inburgeringstraject, en wordt meegenomen in de beoordeling van participatie, uitstroom en leerroutegeschiktheid.</font> | CVGemaakt, VrijeTekstBesteding, Ambitie, ContactUAF, Beroep, BeroepVan, BeroepTot, SoortAanstelling, Taak, TaakVan, TaakTot | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Z-route** | De *Z-route* (Zelfredzaamheidsroute) is een van de drie leerroutes onder de Nederlandse Wet inburgering 2021 en is bedoeld voor inburgeringsplichtigen met een lage leerbaarheid die moeite hebben met het leren van de Nederlandse taal, gericht op zelfredzaamheid, participatie en taalontwikkeling zonder centrale examenvereisten. | Resultaat, ExamenDatum, Onderdeel, Niveau, RedenGeenResultaat, AantalGratisExamenpogingenTegoed, GevolgdeUrenParticipatieActiviteiten | Nee | GGM |

## Overervingshiërarchie

```
Inburgeraar (abstract)
    └── Asielstatushouder
    └── Gezinsmigrant en Overige migrant

```

```
NatuurlijkPersoon (abstract)
    └── Vreemdeling
```

```
Vreemdeling (abstract)
    └── Inburgeraar
```

## Relatiediagrammen

### Inburgering

```
Aandachtspunt  [0] ──── Subdoel Aandachtspunt [0..*]
Aanvraag verlenging Inburgeringstermijn [1] ──── Inburgeringstermijn [1..*] (beoordeling Aanvraag)
Aanvraag verlenging Inburgeringstermijn [1] ──── Verlengingsgrond [1..*]
Asielstatushouder [1] ──── Diplomawaardering [0..*] (heeft aangevraagd)
Asielstatushouder [1] ──── Educatie [0..*] (heeft gevolgd)
Asielstatushouder [0..*] ──── Gemeente [0..1] (is gekoppeld aan )
Asielstatushouder [0..*] ──── Gemeente [0..1] (is gekoppeld aan)
Asielstatushouder [1] ──── ICT-Vaardigheid [0..*] (bezit)
Asielstatushouder [1] ──── Taalvaardigheid [1] (heeft)
Asielstatushouder [1] ──── Training [0..*] (heeft gevolgd)
Asielstatushouder [0..*] ──── Verblijfplaats AZC [0..1] (verblijft)
Asielstatushouder [1] ──── Voorbereiding op Inburgering [1] (neemt deel)
Asielstatushouder [1] ──── Werk [0..*]
B1-route [0..1] ──── Leerroute [1] (onderdeel van )
Brede Intake [1] ──── Inburgeringstraject [1] (onderdeel van)
Brede Intake [0..1] ──── Leerroute [1] (heeft)
Examen [0..1] ──── Inburgeringstraject [1] (Afgerond met)
Examenonderdeel [0..*] ──── Examen [1]
Inburgeraar [1] ──── Aandachtspunt  [0..*] (heeft)
Inburgeraar [1] ──── Aanvraag verlenging Inburgeringstermijn [0..1] (heeft)
Inburgeraar [1] ──── Hoofddoel [0..*] (heeft)
Inburgeraar [1] ──── Inburgeringsplicht [1] (heeft een)
Inburgeraar [1] ──── Ontwikkelwens  [0..*] (heeft)
InburgeringsAanbod [1] ──── Inburgeraar [1..*] (voor)
Inburgeringsplicht [1] ──── Inburgeringstermijn [1..*] (heeft)
Inburgeringsplicht [1] ──── Ontheffing [0..*] (Ontheffing)
Inburgeringsplicht [1] ──── Vrijstelling [0..*] (Vrijstelling)
Inburgeringstraject [1] ──── Inburgeringsplicht [1] (Heeft)
Leerroute [0..1] ──── PIP [1] (afgesproken in)
MAP [0..1] ──── Leerroute [1] (Onderdeel van)
Ontheffing [1] ──── Examenonderdeel [0..*] (ontheffing voor)
Ontwikkelwens  [0] ──── Subdoel Ontwikkelwens [0..*]
PIP [1] ──── InburgeringsAanbod [1] (bevat)
PVT [0..1] ──── Leerroute [1] (Onderdeel van)
Voorbereiding op Inburgering [1] ──── Introductiemodule [1..*] (bestaat uit)
Vrijstelling [1] ──── Examenonderdeel [1] (vrijstelling voor)
Z-route [0..1] ──── Leerroute [1] (heeft (onderdeel van))
```

### Overig

```
Z-route [0..1] ──── Leerroute [1] (heeft (onderdeel van))
```

## Observaties

- Dit beleidsdomein bevat 35 entiteiten.
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Inburgering (34), Overig (1).
- Er zijn 4 generalisatierelaties aanwezig.
