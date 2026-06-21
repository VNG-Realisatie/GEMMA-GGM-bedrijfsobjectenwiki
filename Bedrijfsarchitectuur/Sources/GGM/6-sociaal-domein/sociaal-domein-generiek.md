---
type: ggm-beleidsdomein
naam: Sociaal Domein Generiek
definitie: "Het domein met de generieke objecttypen die door de deeldomeinen van het sociaal domein gebruikt worden."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 56
---

# GGM Beleidsdomein: Sociaal Domein Generiek

Beleidsdomein binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

### Sociaal Domein Domain

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Client** | Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente. | code, gezagsdragerGekend, juridischeStatus, wettelijkeVertegenwoordiging | Nee | GGM |
| **Huishouden** | Persoon of groep personen die een huishouden voert waarbij sprake is van een onderlinge verbondenheid en continu&#239;teit in de samenstelling ervan, die binnen een woning duurzaam gebruik maakt van dezelfde voorzieningen. | soort | Nee | GGM |
| **Relatie** | Betrekking waarin personen, zaken, begrippen of grootheden van nature tot elkaar staan. | relatiesoort | Nee | GGM |
| **Relatiesoort** | De typering van het structurele verband tussen een object van een objecttype en een (ander) object van een ander (of hetzelfde) objecttype. | Omschrijving | Nee | GGM |

### Relaties Sociaal Domein tot Kern

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Clientbegeleider** | De persoon die verantwoordelijk is voor het opstellen en uitvoeren van het ondersteuningsplan in samenwering met de client en personen uit zijn/haar omgeving . | begeleiderscode | Nee | GGM |
| **Leverancier** | Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie | AGBCode, soortLeverancierCode, soortLeverancier, leverancierscode, naam | Nee | GGM |

### Gezag

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Gerechtelijke uitspraak** | Een gerechtelijke uitspraak is een formele beslissing van een rechter of gerechtshof in een juridische procedure. Deze uitspraak bevat de beoordeling van de feiten, de toepassing van het recht en de uiteindelijke beslissing over het geschil dat aan de rechter is voorgelegd. Een gerechtelijke uitspraak kan verschillende vormen aannemen, zoals een vonnis, arrest, beschikking of een kortgedingbeslissing, afhankelijk van de aard van de procedure. Het doel van een gerechtelijke uitspraak is om een bindende oplossing te bieden voor het conflict tussen partijen, en het kan zowel betrekking hebben op civiele, strafrechtelijke, bestuursrechtelijke als andere juridische kwesties. | *(geen attributen)* | Nee | GGM |
| **Gezagsverhouding** | Een gezagsverhouding is een juridische of feitelijke relatie tussen twee partijen, waarbij de ene partij (de gezagsdrager) bevoegd is om instructies of richtlijnen te geven, en de andere partij (de ondergeschikte) verplicht is deze op te volgen. Deze verhouding speelt een belangrijke rol in verschillende contexten, zoals arbeidsrelaties, waarbij een werkgever zeggenschap heeft over een werknemer, of familierecht, waar ouders gezag uitoefenen over hun minderjarige kinderen. Een gezagsverhouding impliceert doorgaans een zekere mate van hiërarchie en verantwoordelijkheid, waarbij de gezagsdrager verplicht is om zijn bevoegdheden zorgvuldig en in het belang van de ondergeschikte uit te oefenen. | indicatie curateleregister, indicatie gezag minderjarige, ingangsdatum, einddatum | Nee | GGM |

### Sociale Relaties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Sociale Groep** | Een sociale groep is een verzameling van twee of meer individuen die met elkaar interacteren, gemeenschappelijke waarden, normen of doelen delen, en een gevoel van saamhorigheid of identiteit hebben. Sociale groepen kunnen variëren in omvang en structuur, van kleine, informele groepen zoals een gezin of vriendengroep tot grote, formele organisaties zoals verenigingen of professionele netwerken. Het lidmaatschap van een sociale groep beïnvloedt vaak het gedrag en de sociale interacties van de leden en speelt een belangrijke rol in de vorming van persoonlijke en sociale identiteiten. | naam, omschrijving, startdatum, einddatum, typering | Nee | GGM |
| **Sociale Relatie** | Een sociale relatie is een duurzame en wederzijdse verbinding tussen twee of meer individuen, gebaseerd op interactie, communicatie en sociale normen. Sociale relaties kunnen verschillende vormen aannemen, zoals persoonlijke (bijvoorbeeld vriendschappen of familiebanden), professionele (zoals collega’s of werkgever-werknemer) of maatschappelijke relaties (bijvoorbeeld tussen buren of leden van een gemeenschap). Ze worden gekenmerkt door wederzijdse verwachtingen en beïnvloeden vaak het gedrag, de gevoelens en de sociale positie van de betrokken personen. Sociale relaties spelen een cruciale rol in het opbouwen van sociale netwerken en het functioneren van samenlevingen. | typering, startdatum, einddatum | Nee | GGM |

### Diagram Profiel

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bankrekening** | De gegevens die betrekking hebben op een bankrekening van een PERSOON of een RECHTSPERSOON.Bron: SGR 16.0We kiezen er voor om bankrekening als zelfstandig concept op te nemen, omdat het mogelijk is dat eenzelfde bankrekening gekoppeld kan zijn aan meerdere personen. Voor rechtspersonen geldt dat een bankrekening maar aan ten hoogste 1 ORGANISATORISCHE EENHEID gekoppeld kan zijn. | Bankrekeningnummer, Brontype, Datum aanvang bankrekening, Datum einde bankrekening, IBAN, Rekeningtype, Tenaamstelling, Voorkeur bankrekening | Nee | GGM |
| **Inkomstenverhouding** | Een persoon kan vanuit diverse bronnen inkomsten krijgen. Denk bijvoorbeeld aan alimentatie, loon, uitkering of zelfs vergoedingen voor maaltijden, onkosten, vervoer e.d. Er zijn nu twee gegevensbehoeften:Enerzijds het kunnen vastleggen van de inkomstencomponenten (zie daarvoor het gelijknamige concept)Anderzijds het vastleggen van de inkomstenverhouding.Een voorbeeld van zo'n inkomstenverhouding is een arbeidsverhouding.De inkomstenverhouding geeft per inkomstensoort aan:de partij die de inkomsten verstrekt, hetgeen een organisatie of een persoon kan zijn ende partij die de inkomsten ontvangtVerder zijn we geïnteresseerd in de periode waarin deze inkomstenverhouding bestond en de periodiciteit van de uitbetalingen.Inkomstenverhoudingen worden geadministreerd in het profiel van de klant. De klant is de ontvanger van de inkomsten. Vandaar dat in de inkomstenverhouding zelf geen expliciete verwijzing is opgenomen naar de ontvanger.Ten aanzien van de bekostiger van de inkomsten geldt, dat dit niet voor elke inkomstenverhouding relevant is. Bij uitkeringen, arbeid, studiefinanciering, stage en pensioen bijvoorbeeld wel, maar bij hobbies niet. | Categorie Inkomsten, Periode einddatum, Periode startdatum | Nee | GGM |
| **Primair inkomstencomponent** | Een persoon kan vanuit diverse bronnen inkomsten krijgen. Denk bijvoorbeeld aan alimentatie, loon, uitkering of zelfs vergoedingen voor maaltijden, onkosten, vervoer e.d. De inkomstencomponent vormt een deel van de totale inkomsten van een persoon. Hiermee leggen we vast het type inkomste, het bedrag en de periode waarover dat bedrag is ontvangen en de boekingsdatum waarop het bedrag is ontvangen.Dat laatste is belangrijk voor de verschillende perspectieven op inkomsten te onderscheiden naar loon-in en loon-over.Achtergrond hierbij zijn twee regelingenLoon wordt als regel toegerekend aan het tijdvak waarin het aan de werknemer is betaald (loon-in). Onder bepaalde voorwaarden mogen werkgevers het uitbetaalde loon toerekenen aan een verstreken loontijdvak. Dit wordt de 'loon-over-regeling' genoemd. Waarom populair: voor een werknemer kan het verstrekken van een uitkering e.d. niet in het kalenderjaar maar bijvoorbeeld in het jaar daarop, hem fiscaal gezien voordelen geven.Bij loon-over gaat het om twee regelingen:De eerste regeling houdt in dat een werkgever een in de maand januari van het nieuwe jaar gedane inhouding op loon dat de werknemer voor het voorgaande jaar nog toekomt, mag opnemen in de laatste aangifte over het oude jaar. Daarbij wordt de inhouding volgens de tarieven van het voorgaande jaar berekend. Deze regeling is structureel in de wet opgenomen.De tweede regeling houdt in dat de werkgever binnen het kalenderjaar loonbetalingen mag toerekenen aan de verstreken loontijdvakken waarop zij betrekking hebben, zo nodig door het indienen van correctieberichten. | *(geen attributen)* | Nee | GGM |
| **Profiel** | *(geen definitie in GGM)* | profielID, profieltype, datumAanvangProfiel, datumEindeProfiel | Nee | GGM |
| **Vermogenscomponent** | Een *vermogenscomponent* is een **onderdeel van het totale vermogen** van een persoon of huishouden, dat afzonderlijk wordt weergegeven (zoals spaargeld, beleggingen, eigen woning netto of pensioenvermogen). | Code soort vermogenscomponent, Datum vaststelling vermogencomponent, identificatie, Nog aan te spreken vermogen, Vrij te laten vermogen | Nee | GGM |

### Diagram Inkomsten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Alimentatie** | Een persoon kan inkomsten hebben uit alimentatie. | Bedrag aan andere rekeningen, Bedrag in convenant, BijdrageExPartnerAndereRekeningen, Inkomstensoort alimentatie, Juiste bedrag betaald door ex partner, LBIO ingeschakeld | Nee | GGM |
| **Ander inkomen** | Een persoon kan inkomsten hebben uit ander inkomen. | Beschrijving ander inkomen, Categorie | Nee | GGM |
| **Beslag op inkomen** | Beslag op inkomen | Soort | Nee | GGM |
| **Betaald werk** | Een persoon kan inkomsten hebben uit betaald werk. | Arbeidscontract, Begindatum contract, Einddatum contract, Inkomsten uit IKB-regeling, Inkomstensoort betaald werk, Loondienst, Loonheffingsnummer, Periodiciteit uitbetaling loon, Soort contract, Urenvermindering | Nee | GGM |
| **Dertiende maand - eindejaarsuitkering** | Een persoon kan inkomsten hebben uit dertiende maand/eindejaarsuitkering. | *(geen attributen)* | Nee | GGM |
| **Draagkracht** | Het gedeelte uit je inkomen of vermogen dat je zelf zou kunnen bijdragen in de kosten (?) voor de bijzondere bijstand(?).De draagkracht is de uitkomst van een ingewikkelde berekening maar wordt voor een jaar vastgesteld en gebruikt.Let wel: niet alle gegevens, die nodig zijn om de draagkracht te berekenen, zijn opgenomen in de ontologie inkomen, omdat bepaalde gegevens van buiten het inkomensdomein komen. | Einddatum, Startdatum | Nee | GGM |
| **Draagkrachtregime** | Het regime wat van toepassing is op de draagkracht. | Initiele draagkracht, Naam, Peildatum, Resterende draagkracht | Nee | GGM |
| **Eigen bedrijf** | Een persoon kan inkomsten hebben uit eigen bedrijf. | Aantal uren per week besteed aan werk, Ingeschreven bij KvK, Recht op zelfstandigenaftrek, Soort bedrijf, Toestemming gemeente parttime ondernemen | Nee | GGM |
| **Eigen bijdrage** | Eigen bijdrage bijvoorbeeld voor CAK of kinderopvang | Soort | Nee | GGM |
| **Heffingskorting** | Een persoon kan inkomsten hebben uit heffingskorting. | Algemene heffingskorting, Inkomensafhankelijke combinatiekorting | Nee | GGM |
| **Hobby** | Een persoon kan inkomsten hebben uit hobbies. | Aantal uren per week besteed aan hobby, Beschrijving hobby | Nee | GGM |
| **Inkomstencomponent** | Een persoon kan vanuit diverse bronnen inkomsten krijgen. Denk bijvoorbeeld aan alimentatie, loon, uitkering of zelfs vergoedingen voor maaltijden, onkosten, vervoer e.d. De inkomstencomponent vormt een deel van de totale inkomsten van een persoon. Hiermee leggen we vast het type inkomste, het bedrag en de periode waarover dat bedrag is ontvangen en de boekingsdatum waarop het bedrag is ontvangen.Dat laatste is belangrijk voor de verschillende perspectieven op inkomsten te onderscheiden naar loon-in en loon-over.Achtergrond hierbij zijn twee regelingenLoon wordt als regel toegerekend aan het tijdvak waarin het aan de werknemer is betaald (loon-in). Onder bepaalde voorwaarden mogen werkgevers het uitbetaalde loon toerekenen aan een verstreken loontijdvak. Dit wordt de 'loon-over-regeling' genoemd. Waarom populair: voor een werknemer kan het verstrekken van een uitkering e.d. niet in het kalenderjaar maar bijvoorbeeld in het jaar daarop, hem fiscaal gezien voordelen geven.Bij loon-over gaat het om twee regelingen:De eerste regeling houdt in dat een werkgever een in de maand januari van het nieuwe jaar gedane inhouding op loon dat de werknemer voor het voorgaande jaar nog toekomt, mag opnemen in de laatste aangifte over het oude jaar. Daarbij wordt de inhouding volgens de tarieven van het voorgaande jaar berekend. Deze regeling is structureel in de wet opgenomen.De tweede regeling houdt in dat de werkgever binnen het kalenderjaar loonbetalingen mag toerekenen aan de verstreken loontijdvakken waarop zij betrekking hebben, zo nodig door het indienen van correctieberichten. | Bijgevoegd bewijs, Boekingsdatum, Bruto-Netto, Inkomsten, Inkomstencomponenttype, Link naar bewijs, Peilmoment, Periode einddatum, Periode startdatum | Nee | GGM |
| **Inkomstenvermindering** | Een persoon kan vermindering van inkomsten hebben. | *(geen attributen)* | Nee | GGM |
| **Kostencomponent** | Noodzakelijke kosten voor het bestaan welke leiden tot een lager (berekend) inkomen. | Bedrag | Nee | GGM |
| **Loonbeslag** | Een persoon kan vermindering van inkomsten hebben door loonbeslag. | *(geen attributen)* | Nee | GGM |
| **Maaltijdvergoeding** | Een persoon kan inkomsten hebben uit maaltijdvergoeding. | *(geen attributen)* | Nee | GGM |
| **Onderhoudsplicht** | Onderhoudsplicht is een wettelijke verplichting van iemand om een ander te onderhouden.Echtgenoten en geregistreerde partners hebben een onderhoudsplicht ten opzichte van elkaar. Ouders hebben een onderhoudsplicht voor hun kinderen tot ze 21 jaar zijn (ook al is het met 18 jaar al meerderjarig). Ex-partners hebben een onderhoudsplicht als een van de partners te weinig inkomen heeft om van te leven. Het in sommige gevallen moeten betalen van alimentatie is ook op de onderhoudsplicht gebaseerd. De inkomsten uit alimentatie zijn in het model zelf een inkomstencomponent.De onderhoudsplicht van ouders om hun kind te onderhouden staat geschreven als artikel: 395a van Boek 1 van het Nederlandse Burgerlijk Wetboek.Dit houdt in ieder geval in dat ouders ervoor moeten zorgen dat het kind de meest basale dingen krijgt, zoals onderdak, kleding, voeding, scholing en medische hulp.Het niet nakomen van de onderhoudsplicht, hetzij wel of niet bij vonnis gesteld, kan strafrechtelijke gevolgen hebben. Dit is strafbaar gesteld in artikel 255 van het Wetboek van Strafrecht.Het betreft hier een verhouding tussen een partij, zijnde een persoon of een organisatie, en de burger, waarbij de onderhoudsplichtige partij de betreffende burger onderhoudt in zijn bestaan.NB: Onderhoudsplicht en onderhoudsplichtverhouding leggen we vast als de onderhoudsplichtige (na verhaal) de onderhoudsplicht voldoet aan de gemeente. In alle gevallen dat een onderhoudsplichtige een onderhoudsbijdrage betaalt aan de onderhoudsgerechtigde spreken we van alimentatie. Dit is opgenomen als inkomstencomponent onder een inkomstenverhouding. | Bijdrage, Boekingsdatum, Onderhoudsplichttype, Peilmoment, Periode einddatum, Periode startdatum | Nee | GGM |
| **Onderhoudsverhouding** | Onderhoudsplicht is een wettelijke verplichting van iemand om een ander te onderhouden. In de onderhoudsplichtverhouding wordt vastgelegd wie de onderhoudsplicht heeft. Omdat de onderhoudsplichtverhouding in het profiel van de klant is opgenomen, wordt de onderhoudsgerechtigde in deze verhouding niet opgenomen. De klant is de onderhoudsgerechtigde.NB:Onderhoudsplicht en onderhoudsplichtverhouding leggen we vast als de onderhoudsplichtige (na verhaal) de onderhoudsplicht voldoet aan de gemeente. In alle gevallen dat een onderhoudsplichtige een onderhoudsbijdrage betaalt aan de onderhoudsgerechtigde spreken we van alimentatie. Alimentatie is opgenomen als inkomstencomponent onder een inkomstenverhouding.Onderhoudsplicht kan gelden voor de ex-partner en/of voor kinderen. | Onderhoudsverhoudingtype, Periode einddatum, Periode startdatum | Nee | GGM |
| **Onkostenvergoeding** | Een persoon kan inkomsten hebben uit onkostenvergoeding. | *(geen attributen)* | Nee | GGM |
| **Pensioen** | Een persoon kan inkomsten hebben uit pensioen. | Beslag op pensioen, Inkomstensoort pensioen, Loonheffingskorting, Periodiciteit uitbetaling pensioen, Uitbetaling vakantiegeld pensioen | Nee | GGM |
| **Reiskosten naar het werk ** | Reiskosten naar het werk | Soort | Nee | GGM |
| **Reiskostenvergoeding** | Een persoon kan inkomsten hebben uit reisvergoeding. | *(geen attributen)* | Nee | GGM |
| **Secundair inkomstencomponent** | Een persoon kan vanuit diverse bronnen inkomsten krijgen. Denk bijvoorbeeld aan alimentatie, loon, uitkering of zelfs vergoedingen voor maaltijden, onkosten, vervoer e.d. De inkomstencomponent vormt een deel van de totale inkomsten van een persoon. Hiermee leggen we vast het type inkomste, het bedrag en de periode waarover dat bedrag is ontvangen en de boekingsdatum waarop het bedrag is ontvangen.Dat laatste is belangrijk voor de verschillende perspectieven op inkomsten te onderscheiden naar loon-in en loon-over.Achtergrond hierbij zijn twee regelingenLoon wordt als regel toegerekend aan het tijdvak waarin het aan de werknemer is betaald (loon-in). Onder bepaalde voorwaarden mogen werkgevers het uitbetaalde loon toerekenen aan een verstreken loontijdvak. Dit wordt de 'loon-over-regeling' genoemd. Waarom populair: voor een werknemer kan het verstrekken van een uitkering e.d. niet in het kalenderjaar maar bijvoorbeeld in het jaar daarop, hem fiscaal gezien voordelen geven.Bij loon-over gaat het om twee regelingen:De eerste regeling houdt in dat een werkgever een in de maand januari van het nieuwe jaar gedane inhouding op loon dat de werknemer voor het voorgaande jaar nog toekomt, mag opnemen in de laatste aangifte over het oude jaar. Daarbij wordt de inhouding volgens de tarieven van het voorgaande jaar berekend. Deze regeling is structureel in de wet opgenomen.De tweede regeling houdt in dat de werkgever binnen het kalenderjaar loonbetalingen mag toerekenen aan de verstreken loontijdvakken waarop zij betrekking hebben, zo nodig door het indienen van correctieberichten. | *(geen attributen)* | Nee | GGM |
| **Stage** | Een persoon kan inkomsten hebben uit stage. | Maaltijdvergoeding, Onkostenvergoeding, Periodiciteit uitbetaling loon, Reiskostenvergoeding, Vergoeding in natura | Nee | GGM |
| **Studiefinanciering** | Een persoon kan inkomsten hebben uit studiefinanciering. | Daadwerkelijk Genoten, Inkomstensoort studiefinanciering | Nee | GGM |
| **Te betalen alimentatie** | Te betalen alimentatie | Soort | Nee | GGM |
| **Uitkering** | Een persoon kan inkomsten hebben uit uitkering. | Beslag op uitkering, Inkomstensoort uitkering, Loonheffingskorting, Periodiciteit uitbetaling uitkering, Toeslag op uitkering, Uitkering verlaagd door boete, Uitkering verlaagd door maatregel, Vakantiegeld jaarlijks ontvangen | Nee | GGM |
| **Vakantiegeld** | Een persoon kan inkomsten hebben uit vakantiegeld. | *(geen attributen)* | Nee | GGM |
| **Vergoeding** | Een persoon kan inkomsten hebben uit vergoedingen als voor maaltijden, onkosten of reizen | *(geen attributen)* | Nee | GGM |
| **Vergoeding in natura** | Een persoon kan inkomsten hebben uit vergoeding in natura. | *(geen attributen)* | Nee | GGM |
| **Verlaging door boete** | Een persoon kan vermindering van inkomsten hebben door boete. | *(geen attributen)* | Nee | GGM |
| **Verlaging door maatregel** | Een persoon kan vermindering van inkomsten hebben door maatregel. | *(geen attributen)* | Nee | GGM |
| **Vrijlating inkomsten** | Wanneer u aan het werk gaat dan mag u van het loon dat u krijgt 25 procent houden, met een maximum van € 224,-.(bedrag per 1 januari 2022). Dit noemen wij vrijlating. Dus: als u in een maand netto € 500,- verdient met werken, mag u € 125,- houden. Deze 500 euro zou in het geheel in mindering gebracht worden op de uitkering. 25% wordt vrijgelaten. Dus in plaats van 500 wordt er (500 – 125) = 375 gekort. De 125 wordt dan vrijgelaten en niet verrekend met de uitkering. U geeft altijd uw hele loon op. De gemeente berekent de vrijlating.Is uw inkomen hoger dan uw bijstandsnorm maar na aftrek van deze inkomstenvrijlating lager? Dan kunt u ervoor kiezen om nog een aanvullende bijstandsuitkering te blijven ontvangen. De verplichtingen blijven voor u gelden. Wijzigingen in uw woon- en leefsituatie, vermogen en inkomsten moet u blijven doorgeven. U behoudt ook de arbeidsverplichtingen. Dat houdt in dat u uw best moet doen het werk en het aantal uren dat u werkt te behouden. | Doelgroep, Medisch, Periode einddatum, Periode startdatum, Soort vrijlating, Vrijgelaten bedrag | Nee | GGM |

### Diagram Vermogen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Hypotheek** | Een hypotheek is een lening waarbij een onroerend goed, zoals een woning, dient als onderpand voor de schuld. Het wordt doorgaans verstrekt door een financiële instelling, zoals een bank, en stelt de lener in staat om een woning te kopen of te bouwen. De lening wordt over een afgesproken periode terugbetaald, inclusief rente. Als de lener niet aan de betalingsverplichtingen voldoet, heeft de kredietverstrekker het recht om het onderpand te verkopen om de openstaande schuld te vereffenen. Een hypotheek is daarmee zowel een financieringsvorm als een juridische zekerheid voor de kredietverstrekker. | Overwaarde | Nee | GGM |
| **Motorvoertuig** | Een motorvoertuig is een voertuig dat is uitgerust met een motor als krachtbron en bedoeld is voor het vervoer van personen, goederen of het uitvoeren van specifieke taken. Het kan zich zelfstandig voortbewegen zonder de directe fysieke inspanning van een bestuurder of passagier. Voorbeelden van motorvoertuigen zijn auto’s, vrachtwagens, motorfietsen en bussen. Motorvoertuigen zijn doorgaans voorzien van wielen en rijden op de weg, en het gebruik ervan is vaak gebonden aan wettelijke regels, zoals registratie, verzekering en rijbewijsvereisten. | Kenteken, Soort motorvoertuig | Nee | GGM |
| **Onroerend goed** | Onroerend goed is een juridische term die verwijst naar fysieke objecten die duurzaam met de grond zijn verbonden en niet zonder schade kunnen worden verplaatst. Dit omvat gronden, gebouwen, woningen en andere constructies die vast met de grond zijn verbonden, zoals bruggen of schuren. Onroerend goed wordt vaak onderscheiden van roerende zaken, die wel verplaatsbaar zijn. Het eigendom en de overdracht van onroerend goed zijn gebonden aan specifieke wettelijke regels, zoals registratie in openbare registers en het opstellen van notariële akten. | Overwaarde | Nee | GGM |
| **Waardepeiling** | *Waardepeiling* is een **bepaling of schatting van de waarde van een object, goed of situatie**, verkregen door middel van peiling of inschatting van wat het waard zou zijn. | Bijgevoegd bewijs, Brontype, Datum aanspraak vermogenscomponent, Link naar bewijs, Peilmoment, Waarde vermogenscomponent, WaardepeilingId, WaardeSoort vermogenscomponent | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AanvraagStadspas** | Te specifiek. AanvraagGemeentepas | *(geen attributen)* | Nee | GGM |
| **Incident** | Een *incident* is een afzonderlijke gebeurtenis of voorval dat plaatsvindt en kan afwijken van de normale gang van zaken, vaak onverwacht of onvoorzien. | datumtijdVanaf, datumTijdTot, omschrijving, toelichting, soort, locatie | Nee | GGM |
| **Stadspas** | Te specifiek, voorstel gemeentepas? | ingangsdatum, einddatum | Nee | GGM |
| **Uitbreiding Zorgmelding** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
Client (abstract)
    └── Werkzoekende
```

```
Hypotheek (abstract)
    └── Krediethypotheek
```

```
IngeschrevenPersoon (abstract)
    └── Client
```

```
Inkomstencomponent (abstract)
    └── Primair inkomstencomponent
    └── Secundair inkomstencomponent
```

```
Inkomstenvermindering (abstract)
    └── Loonbeslag
    └── Verlaging door boete
    └── Verlaging door maatregel
```

```
Kostencomponent (abstract)
    └── Beslag op inkomen
    └── Eigen bijdrage
    └── Reiskosten naar het werk 
    └── Te betalen alimentatie
```

```
Medewerker (abstract)
    └── Clientbegeleider
```

```
NatuurlijkPersoon (abstract)
    └── Relatie
```

```
Primair inkomstencomponent (abstract)
    └── Alimentatie
    └── Ander inkomen
    └── Betaald werk
    └── Eigen bedrijf
    └── Hobby
    └── Pensioen
    └── Stage
    └── Studiefinanciering
    └── Uitkering
```

```
Rechtspersoon (abstract)
    └── Leverancier
```

```
Secundair inkomstencomponent (abstract)
    └── Dertiende maand - eindejaarsuitkering
    └── Heffingskorting
    └── Inkomstenvermindering
    └── Vakantiegeld
    └── Vergoeding
```

```
Vergoeding (abstract)
    └── Maaltijdvergoeding
    └── Onkostenvergoeding
    └── Reiskostenvergoeding
    └── Vergoeding in natura
```

```
Vermogenscomponent (abstract)
    └── Bankrekening
    └── Hypotheek
    └── Motorvoertuig
    └── Onroerend goed
```

## Relatiediagrammen

### Sociaal Domein Domain

```
AOMMeldingWmoJeugd [0..*] ──── Client [1] (heeft)
AOM_AanvraagWmoJeugd [0..*] ──── Client [1] (heeft)
Beschikking [0..*] ──── Client [1]
Client [1] ──── Aanvraag [0..*] (doet aanvraag)
Client [1..2] ──── Bankrekening [0..*] (bezit)
Client [1] ──── Dakloosheid [0..*] (heeft)
Client [1..2] ──── Dienst [0..*] (neemt dienst af)
Client [0..*] ──── Doelgroep [0..*] (valt binnen)
Client [0..*] ──── Huishouden [1] (maakt onderdeel uit van)
Client [0] ──── Inkomensvoorziening [1] (is partner van)
Client [1..*] ──── Inkomensvoorziening [0..*] (Voorziening Bijstandspartij)
Client [1] ──── Inkomensvoorziening [1] (heeft voorziening)
Client [1] ──── Leefsituatie [0..*] (heeft financiele situatie)
Client [1] ──── Normafwijking [0..*] (veroorzaakt)
Client [1] ──── Profiel [1..*] (heeft)
Client [1] ──── Regeling [0..*] (heeft regeling)
Client [0..*] ──── Relatie [0..*] (heeft relatie)
Client [1] ──── Score [0..*] (heeft)
Client [1] ──── SociaalTeamDossier [0..*] (heeft)
Clientbegeleider [0..*] ──── Client [0..*] (ondersteunt client)
Debiteur [0..1] ──── Client [1] (verwijst)
Declaratieregel [0..*] ──── Client [1] (betreft)
Huishouden [0..*] ──── Nummeraanduiding [1] (heeft als adres)
Levering [0..*] ──── Client [0..1] (prestatie voor)
NatuurlijkPersoon [1..*] ──── Huishouden [0..1] (maakt onderdeel uit van)
Relatie [0..*] ──── Huishouden [0..*] (maakt onderdeel van)
Relatie [0..*] ──── Relatiesoort [1] (is soort)
Schuldhulptraject [0..*] ──── Client [1..2] (heeft traject)
SociaalTeamDossier [0..*] ──── Relatie [0..*] (heeft betrokkenen)
Terugvorderingsverzoek [0..*] ──── Client [1..2] (betreft)
Verplichting Wmo Jeugd [1] ──── Client [0..1] (heeft)
Verzoek om Toewijzing [0..*] ──── Client [1] (betreft)
Vroegsignaal [0..*] ──── Client [1] (betreft)
```

### Relaties Sociaal Domein tot Kern

```
Clientbegeleider [1] ──── Beschikking [0..*] (geeft af)
Clientbegeleider [0..*] ──── Client [0..*] (ondersteunt client)
Clientbegeleider [1] ──── Inkomensvoorziening [0..*]
Clientbegeleider [1] ──── SociaalTeamDossier [0..*] (heeft)
Clientbegeleider [0..*] ──── Team [1] (maakt onderdeel uit van)
Declaratie [0..*] ──── Leverancier [1] (Ingediend door)
Leverancier [1] ──── Contract [0..*] (heeft)
Leverancier [1] ──── Levering [0..*] (leverde prestatie)
Tarief [0..*] ──── Leverancier [1] (heeft)
Toewijzing [0..*] ──── Leverancier [0..1] (levert voorziening)
Verplichting Wmo Jeugd [1] ──── Leverancier [0..1] (Verplichting aan)
Verzoek om Toewijzing [0..*] ──── Leverancier [1] (leverancier)
```

### Gezag

```
Gerechtelijke uitspraak [0..1] ──── Gezagsverhouding [0..*] (basis van)
Gezagsverhouding [0..2] ──── IngeschrevenPersoon [1] (betreft)
IngeschrevenPersoon [0..1] ──── Gezagsverhouding [0..*] (gezaghebbende)
NietNatuurlijkPersoon [0..1] ──── Gezagsverhouding [0..*] (gezaghebbende)
```

### Sociale Relaties

```
NatuurlijkPersoon [2..*] ──── Sociale Groep [0..*] (maakt deel uit van)
Sociale Relatie [0..*] ──── NatuurlijkPersoon [2..*] (heeft)
```

### Diagram Profiel

```
Client [1..2] ──── Bankrekening [0..*] (bezit)
Client [1] ──── Profiel [1..*] (heeft)
Profiel [1] ──── Inkomstenverhouding [0..*] (bevat)
Profiel [1] ──── Reden aanvraag [0..1] (bevat)
Profiel [1..2] ──── Vermogenscomponent [0..*] (bevat)
```

### Overig

```
Incident [1] ──── Informering [0..*] (informering)
Zorgelijke Situatie [1] ──── Incident [0..*] (berust op)
```

## Observaties

- Dit beleidsdomein bevat 56 entiteiten.
- Entiteiten zijn gegroepeerd in 8 diagramgroepen: Sociaal Domein Domain (4), Relaties Sociaal Domein tot Kern (2), Gezag (2), Sociale Relaties (2), Diagram Profiel (5), Diagram Inkomsten (33), Diagram Vermogen (4), Overig (4).
- Er zijn 37 generalisatierelaties aanwezig.
