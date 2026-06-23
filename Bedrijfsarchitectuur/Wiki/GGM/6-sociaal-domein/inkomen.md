---
type: ggm-beleidsdomein
naam: Inkomen
definitie: "Het informatiedomein dat gegevens omvat over inkomensvoorzieningen, -regelingen en financiële ondersteuning voor inwoners, gericht op het waarborgen van bestaanszekerheid en participatie in de samenleving."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 89
---

# GGM Beleidsdomein: Inkomen

Beleidsdomein binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

### Diagram Diensten

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

### Diagram GGM en Inkomen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Debiteur** | Binnen het domein van terug- en invorderen is een debiteur een persoon waarop de gemeente een of meerdere vorderingen heeft. | Eigen kenmerk, Opvoerdatum, Soort debiteur | Nee | GGM |
| **Normafwijking** | Een *normafwijking* (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde **afwijkt van de normatieve verplichtingen** die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering. | Datum vaststelling normafwijking, Datum vaststelling verwijtbaarheid, identificatie, Motivatie verwijtbaarheid, Recidive, Type normafwijking, Verwijtbaarheid | Nee | GGM |
| **Reden aanvraag** | Reden waarom dienst wordt aanvraagd bij gemeente. | Diensttype, Gewenste ingangsdatum | Nee | GGM |
| **Terugvorderingsverzoek** | Het vorderingsverzoek is de handshake tussen een voorliggend proces en de bedrijfsfunctie Terug- en Invorderen. In het kader van een bepaalde regeling is geconstateerd dat een zeker bedrag terug moet worden gevorderd. Dit wordt her gemakshalve het voorliggende proces genoemd. Het voorliggende proces moet de juiste, noodzakelijke en voldoende gegevens toeleveren aan Terug- en invorderen opdat het verzoek tot terugvorderen in behandeling kan worden genomen.Het vorderingsverzoek start een terugvorderingszaak. Op basis van de voortgang van die zaak kan het verzoekende voorliggende proces op de hoogte worden gehouden van de voortgang via zaakstatusinformatie. | Aanmaakdatum, Behandelstatus verzoek, Categorie, Fiscaal, Periode einddatum, Periode startdatum, Priotype, Regeling, Subcategorie | Nee | GGM |

### Diagram Basismodel Inkomen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Component** | Een *inkomenscomponent* is een afzonderlijk onderdeel of bron van inkomen, zoals loon, winst uit onderneming, uitkeringen of andere inkomensbronnen, die samen het totale inkomen van een persoon of huishouden vormen. | bedrag, begindatumBetrekkingop, eindatumBetrekkingop, debetCredit, rekeningNummer, grootboekcode, grootboekomschrijving, kostenplaats, groep, omschrijving, toelichting, groepcode | Nee | GGM |
| **ComponentSoort** | *ComponentSoort* is de classificatie of het type van een inkomenscomponent binnen een inkomen- of financiële administratie, waarmee wordt bepaald welke categorie of soort een specifieke component behoort. | regelingcode, regeling, kolom, kolomcode, componentcode, omschrijving | Nee | GGM |
| **Inkomensvoorziening** | Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving | ingangsdatum, einddatum, toekenningsdatum, bedrag, eenmalig, groep, administratieveEinddatum, administratieveStartdatum, betalingsmomentcode, code, datumToekenning, indicatieBlokkering, indicatieStudietoeslag, indicatieUitkeringSplitsen, indicatieUitkeringsspecificatie, versterkkingsvorm, verwerktTotEnMetDatum | Nee | GGM |
| **Inkomensvoorzieningsoort** | Typering van een inkomensvoorziening | naam, omschrijving, wet, vergoeding, vergoedingscode, regeling, regelingscode, code | Nee | GGM |
| **Regeling** | Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert. | startdatum, einddatum, toekenningsdatum, omschrijving | Nee | GGM |
| **Regelingsoort** | Typologie van een regeling | naam, omschrijving | Nee | GGM |
| **UitkeringsRun** | Een *UitkeringsRun* is een geautomatiseerde verwerking in een financieel of administratief systeem waarbij **een groep uitkeringen of betalingen tegelijk wordt berekend en uitgevoerd** als onderdeel van een periodieke batch-verwerking. | datumRun, periodeRun, soortRun, frequentie | Nee | GGM |

### In- en uitstroom inkomensvoorziening

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Huisvestingsoort** | Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, soorthuisvestingCode | Nee | GGM |
| **RedenBlokkering** | Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenBlokkeringCode | Nee | GGM |
| **RedenInstroom** | De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenInstroomCode, CBS-code, CBS-omschrijving | Nee | GGM |
| **RedenUitstroom** | De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering be&#235;indigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenUitstroomCode, CBS-code, CBS-omschrijving | Nee | GGM |

### Normafwijking

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Afwijkende maatregel** | Een *afwijkende maatregel* is een maatregel die afwijkt van de standaardregel of wettelijke norm en die op basis van een wettelijke grondslag, beleidsregel of gemotiveerde beslissing in een concreet geval wordt toegepast. | Bedrag, Code reden afwijking maatregel, Motivatie afwijking maatregel, Percentage | Nee | GGM |
| **Boete** | Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering. Als de vordering niet (meer) bestaat, zou dit gegeven daarmee niet beschikbaar zijn.Daarnaast kan dit ook helpen bij het vastleggen van een boete van een poging tot fraude (zonder financiele consequenties, waardoor geen vordering is ontstaan. (tijdig ondekte valsheid in geschifte e.d.).Bij bedragen hoger dan 50.000 euro, wordt aangifte van fraude gedaan en volgt strafrechtelijk onderzoek.Feitelijk is het uitgangspunt bij het opleggen van een boete dat er altijd sprake is van opzet. Daarom is een apart gegeven Fraude niet opgenomen. | Bedrag boete, Boetevorm, Reden boete, Voorwaarde boete | Nee | GGM |
| **Maatregel** | Een *maatregel* is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven. | Datum aanvang maatregel, Datum einde maatregel, Datum vaststelling maatregel, identificatie, Type maatregel | Nee | GGM |
| **Maatregel op uitkering** | Een *maatregel op uitkering* is een sanctie van een uitvoerend orgaan (zoals een gemeente) waarbij de hoogte van een uitkering tijdelijk wordt verlaagd of aangepast omdat de uitkeringsgerechtigde niet heeft voldaan aan de aan de uitkering verbonden verplichtingen. | Code reden maatregel, Motivatie vermindering maatregel, Percentage maatregel | Nee | GGM |

### Reden aanvraag- overzicht

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Andere reden afwijkende startdatum** | *Andere reden afwijkende startdatum* is een omschrijving van een **reden waarom de startdatum van een dienst of uitkering afwijkt van de standaard startdatum**, voor zover deze reden niet onder de standaardcategorieën valt. | omschrijvingBijzondereReden | Nee | GGM |
| **Andere reden verzoek** | *Andere reden verzoek* is een categorie voor een **overige reden** waarom een aanvraag wordt gedaan die niet onder de standaard-redencategorieën valt binnen het *Reden aanvraag*-model. | Opgave financiële ondersteuning, Specificatie geldtekort | Nee | GGM |
| **Diensten::Aanvraag** | Een aanvraag is een verzoek van een burger, bedrijf of organisatie aan een overheid om een specifieke dienst te verkrijgen of een besluit te ontvangen (bijv. vergunning, subsidie, paspoort of beschikkingsbesluit). | *(geen attributen)* | Nee | GGM |
| **Diensten::Aanvraag levensonderhoud** | Een aanvraag levensonderhoud is het formele verzoek van een persoon aan een gemeentelijke of overheidsinstantie om een uitkering of financiële ondersteuning te verkrijgen die het inkomen aanvult zodat in het basislevensonderhoud kan worden voorzien. | *(geen attributen)* | Nee | GGM |
| **Gestopt betaald werk** | *Gestopt betaald werk* is de situatie waarin iemand **zijn of haar betaalde arbeidsrelatie heeft beëindigd**, waardoor het reguliere inkomen uit werk is komen te vervallen en dit relevant is voor de beoordeling van een uitkeringsaanvraag of inkomenssituatie. | Afwijsreden WW-aanvraag, Bedrijfsadres, Bedrijfstelefoonnummer, Contractperiode, Laatste salarisdatum, Minimaal 26 weken van 36 gewerkt, Naam bedrijf, Ontslagbrief ontvangen, Ontslagvergoeding ontvangen, Reden einde werk, Specificatie reden einde werk, Wettelijke stappen gezet, WW-uitkering aangevraagd, Ziektewet-uitkering aangevraagd | Nee | GGM |
| **Gestopt of verkocht eigen bedrijf** | *Gestopt of verkocht eigen bedrijf* is de situatie waarin een persoon zijn of haar **bedrijf volledig beëindigt of overdraagt/verkoopt**, waardoor de zelfstandige activiteit ophoudt en de reguliere inkomsten uit de onderneming verdwijnen. | Datum gestopt met eigen bedrijf, KvK-inschrijfnummer, Reden eigen bedrijfs gestopt, Uitgeschreven bij Kamer van Koophandel, Verkoopbedrag | Nee | GGM |
| **Gestopte bijstanduitkering** | *Gestopte bijstandsuitkering* is een reden van aanvraag binnen de GBI-Ontologie die aanduidt dat een cliënt een inkomensdienst aanvraagt omdat **een eerder ontvangen bijstandsuitkering is beëindigd**. | Reden einde bijstandsuitkering, Situatie gewijzigd, Specificatie reden einde bijstand, Specificatie wijziging situatie | Nee | GGM |
| **Gestopte detentie** | *Gestopte detentie* is een reden van aanvraag binnen het GBI-model die aangeeft dat een persoon **vrij is gekomen uit detentie**, waardoor de detentie-periode is beëindigd en dit relevant is voor de beoordeling van een nieuwe aanvraag of wijziging in de ondersteuningsbehoefte. | Duur detentie, Einddatum detentie, Soort uitkering voor detentie, Specificatie uitkering voor detentie, Uitkering voor detentie | Nee | GGM |
| **Gestopte of verlaagde alimentatie** | *Gestopte of verlaagde alimentatie* is een reden van aanvraag binnen het GBI-Ontologiemodel die aangeeft dat een persoon een inkomensdienst aanvraagt omdat **alimentatiebetalingen zijn gestopt of verlaagd**, waardoor het reguliere ondersteuningsinkomen is verminderd. | Einddatum alimentatie, LBIO ingeschakeld, Nabestaandeuitkering aangevraagd, Opgave financiële ondersteuning, Reden einde of verlaagde alimentatie | Nee | GGM |
| **Gestopte studiefinanciering** | *Gestopte studiefinanciering* is een reden van aanvraag binnen de GBI-Ontologie die aangeeft dat een persoon een inkomensdienst aanvraagt omdat **de studiefinanciering is beëindigd of gestopt**, waardoor het (studie)inkomen wegvalt en inkomensondersteuning nodig kan zijn. | Einddatum studiefinanciering, Specificatie studiefinanciering | Nee | GGM |
| **Gestopte uitkering** | *Gestopte uitkering* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een cliënt een inkomensdienst aanvraagt omdat **een eerdere uitkering is beëindigd**, waardoor opnieuw inkomensondersteuning nodig is. | Einddatum uitkering, Einde uitkering in bezwaar, Gedeeltelijk arbeidsongeschikt na 50e, Ingangsdatum WGA binnen periode, IOAW-uitkering ontvangen, minderDan35%AO, Reden einde uitkering, Specificatie andere uitkering, Specificatie reden einde uitkering, Startdatum WW- of WGA-uitkering, Uitkering, Werkloosperiode | Nee | GGM |
| **Ingang bijstandsuitkering** | In de meeste gevallen is de startdatum van een dienst gelijk aan de datum eerste melding (melddatum). Echter, er zijn redenen om hiervan af te wijken. In dat geval wijkt de startdatum af van de melddatum. Ingangsdatum uitkering bevat een Reden afwijkende startdatum om op te nemen met welke reden een afwijkende ingangsdatum gehanteerd wordt. Ingang bijstandsuitkering kan, zoals de naam al doet vermoeden, alleen van toepassing zijn indien het een aanvraag betreft van het diensttype 'Aanvulling levensonderhoud' (ALO)'. | Afwijkende ingangsdatum, Datum melding bij gemeente, Gewenste startdatum uitkering, Na melding gemeente digitaal verwezen | Nee | GGM |
| **Levenssituatie::Levenssituatie** | De levenssituatie is de kwaliteit van de omgeving en omstandigheden waarin een persoon leeft en functioneert op een bepaald moment. | *(geen attributen)* | Nee | GGM |
| **Opname instelling** | *Opname instelling* is een reden van aanvraag binnen de GBI-Ontologie die aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **(net) is opgenomen in of vrijgekomen uit een instelling**, wat financiële gevolgen heeft voor de inkomenssituatie. | Einddatum opname, Startdatum opname | Nee | GGM |
| **Overleden partner** | *Overleden partner* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat **de partner is overleden**, met als gevolg dat het huishoudinkomen is verminderd. | Meer dan 45% arbeidsongeschikt, Nabestaandeuitkering aangevraagd, Reden ANW afgewezen | Nee | GGM |
| **Reden aanvraag Levensonderhoud** | *Reden aanvraag Levensonderhoud* is een categorie binnen het GBI-Ontologiemodel die aangeeft dat een cliënt een inkomensdienst aanvraagt vanwege een situatie waarin **middelen voor levensonderhoud ontbreken of zijn weggevallen**, en deze aanleiding geeft voor ondersteuning. | Onvoldoende inkomen, Reden, Verblijfstatus, Wijziging gezin, Zelfstandige | Nee | GGM |
| **Reden afwijkende startdatum** | *Reden afwijkende startdatum* is een categorie binnen het GBI-Ontologiemodel die aangeeft **waarom de ingangsdatum van een dienst of uitkering afwijkt van de standaard startdatum** (bijv. de datum van eerste melding). | Reden afwijking aanwezig, Reden Niet Eerder Aanvragen, RedenAfwijkendeStartdatumType | Nee | GGM |
| **Verbroken relatie** | *Verbroken relatie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt doordat **de (huwelijkse/samenlevings)relatie is beëindigd**, met financiële gevolgen voor het levensonderhoud. | Afspraak onderhoudsbijdrage gemaakt, Datum relatie verbroken, Geregistreerde partner, Opgave financiële ondersteuning | Nee | GGM |
| **Vertrek uit asielzoekerscentrum** | *Vertrek uit asielzoekerscentrum* is een subtype van **Reden aanvraag** in het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **recentelijk een asielzoekerscentrum heeft verlaten**, waardoor de financiële situatie is veranderd. | Bedrag weekgeld COA, Einddatum weekgeld COA, Ingangsdatum huurcontract, Weekgeld COA, Weekgeld COA stopt | Nee | GGM |
| **Wachten DigiD** | *Wachten DigiD* is een subtype van **Reden afwijkende startdatum** binnen het GBI-Ontologiemodel dat aangeeft dat de ingangsdatum van een inkomensdienst **vertraging oploopt doordat een DigiD nog niet is aangevraagd, geactiveerd of bruikbaar is**. | Aanvraagdatum DigiD | Nee | GGM |
| **Wachten beslissing instantie** | *Wachten beslissing instantie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **moet wachten op een besluit van een externe instantie**, waardoor de startdatum van de dienst afwijkt van de standaardprocedure. | Ontvangstdatum beslissing instantie | Nee | GGM |

### Diagram Terug- en invordering

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aflossing** | Een aflossing is de betaling van een afgesproken of opgelegd bedrag op een vordering. Een aflos-sing gebeurt in het kader van een aflossingsafspraak gemaakt bij een vordering of wordt eenzijdig opgelegd. De aflossing wordt geadministreerd als een vorderingscomponent onder die vordering. Afgesproken is minnelijk maar kan ook opgelegd worden, bijv 5% verrekening of beslag op loon. | Aflossingskenmerk, Bedrag, Boekingsdatum, Ontvangstdatum | Nee | GGM |
| **Aflossingsafspraak** | Een aflossingsafspraak is een onderdeel van het aflossingsplan. Het is een afspraak over hoe en wanneer het opgelegde bedrag wordt afgelost. Het opgelegde bedrag is het bedrag is de hele vordering of het bdrag na verrekening of beslag.Elke afspraak in het aflossingsplan bepaalt welk bedrag afgelost wordt op welke vordering vanaf een zekere startdatum per tijdseenheid (doorgaans een maand). | Bedrag, Einddatum, Indicatie inclusief vakantiegeld, Periodiek, Startdatum | Nee | GGM |
| **Aflossingsplan** | Een aflossingsplan bevat alle afspraken tussen de gemeente en de debiteur over op welke vordering hij/zij per wanneer welk bedrag aflost.Verder geldt dat er bijzondere afspraken kunnen worden vastgelegd, bijvoorbeeld Dwangbevel. In zulke gevallen wordt de gehele schuld in één keer weer opeisbaar gesteld. | Aflossingskenmerk, Einddatum, Startdatum | Nee | GGM |
| **Afschrijving** | De vordering blijkt oninbaar. Er is (nog) geen aflossingsmogelijkheid. Er wordt ook niet geacht dat er perspectief is tot invordering. Er wordt afscheid genomen van de vordering.Afscheid nemen van de vordering gebeurt via het afschrijven van de vordering. De reden daarvan wordt opgegeven. | Aanmaakdatum, Reden afschrijving | Nee | GGM |
| **Betaalcomponent** | Een rechtmaand kan door de tijd heen door correcties meerdere betaalcomponenten krijgen. Met de betaalcomponent leg je vast welk bedrag op welke boekingsdatum is betaald in het kader van de rechtmaand.Deze administratie is noodzakelijk omdat moet kunnen worden bepaald welk deel in de terugvordering bruto en welke netto moet worden teruggevorderd. | Bedrag, Boekingsdatum | Nee | GGM |
| **Boetevordering** | Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente. Vorderingen die zijn ingesteld omdat er een boete vanwege een overtreding van de inlichtingenplicht is opgelegd. De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden gelegd. | *(geen attributen)* | Nee | GGM |
| **Conservatoir beslag** | In het Nederlands recht is een conservatoir beslag een beslaglegging op (een deel van) het vermogen van een schuldenaar ter verzekering van de betaling van een onbetaald gebleven vordering nog voordat de rechter uitspraak heeft gedaan over de juistheid van die vordering. De toestemming tot het leggen van dit beslag moet door een advocaat namens de schuldeiser aan de beslagrechter, ook wel "voorzieningenrechter", worden gevraagd. Door het leggen van het beslag ontstaat meer zekerheid dat het beslagen vermogen ter beschikking staat. De voorzieningenrechter is in Nederland over het algemeen snel geneigd toestemming voor het beslag te verlenen en dat zelfs zonder dat de schuldenaar van het verzoek op de hoogte is of daarover wordt gehoord. | Aanvraagdatum, Toestemmingsdatum | Nee | GGM |
| **Correctie** | Na nader inzicht corrigeren van het te vorderen bedrag met een zeker bedrag. Correcties worden geadministreerd onder de vordering. | Bedrag, Boekingsdatum, Reden | Nee | GGM |
| **Incassokostenvordering** | AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.IncassokostenvorderingBij het invorderproces kunnen incassokosten ontstaan bij een bepaalde vordering. Bij incassokosten boven een drempel (instelbare referentiewaarde) kan een incassokostenvordering worden opgevoerd. De incassokostenvordering wordt gerelateerd aan de hoofdvordering. De incassokostenvordering is een zogenaamde accessoire vordering, die zijn titel ontleend aan de hoofdvordering.Dit type vordering is als verbijzondering opgenomen, opdat deze relatie expliciet kan worden gelegd. | *(geen attributen)* | Nee | GGM |
| **Interventie** | De daadwerkelijke interventie, die wordt ondernomen naar aanleiding van een interventieverzoek. | Beslisdatum, Ingangsdatum, Interventietype | Nee | GGM |
| **Interventieverzoek** | In het geval van monitoring op aflossingsafspraken bij een vordering kan bij ongeregeldheden, zoals het achterwege blijven van aflossingen, een signaal worden gegeven om te interveneren. Dit gebeurt door een interventieverzoek. Interventies geschieden volgens een interventieladder. Altijd kan een medewerker daar gemotiveerd van afwijken, bijvoorbeeld na klantcontact. Dit betekent niet dat het interventieverzoek niet minder dwingend is. | Verzoekdatum | Nee | GGM |
| **Invorderingsbasis** | Een invordering is het innen van een schuld of een te veel uitbetaalde uitkeringssom, soms als gevolg van uitkeringsfraude. In de terugvorderingszaak wordt de vordering vastgesteld en beslist. In de invorderingszaak wordt die schuld vervolgens van de debiteur geïnd. Na betaling vervalt de vordering. Bij niet-betaling kan de vordering ook tenietgaan in de volgende situaties:bij verjaring (de verjaringstermijn werd niet op tijd gestuit)bij kwijtscheldingbij verrekeningbij overlijdenIndien geen verhaalsmogelijkheden aanwezig zijn en binnen afzienbare tijd niet te verwachten zijn, wordt de vordering oninbaar geleden. Dit betekent echter niet dat de vordering teniet gaat. Als nadat de vordering oninbaar is geleden verhaalsmogelijkheden bekend worden, kan daarop gewoon verhaal worden gehaald.Indien geen verhaalsmogelijkheden aanwezig en binnen afzienbare tijd niet te verwachten zijn, wordt de vordering oninbaar geleden. Dit betekent echter niet dat de vordering teniet gaat. Als nadat de vordering oninbaar is geleden verhaalsmogelijkheden bekend worden, kan daarop gewoon verhaal worden gehaald.Teruggaven blijven verrekend worden met oninbaar geleden vorderingen, zolang deze nog niet verjaard zijn.Basis voor het invorderen vormen drie grootheden:de invorderingsmogelijkheidde beslagvrije voetde aflossingscapacteit.In de tijd kunnen deze basisvariabelen wijzigen. Per wijziging worden deze basisvariabelen geadministreerd.De invorderingsbasis vormt dus de basis voor invorderen en derhalve voor het maken van de aflossingsafspraken in het aflossingsplan.Omdat de drie hiervoor genoemde grootheden debiteurafhankelijk zijn, is de invorderingsbasis direct gekoppeld aan de debiteur.Let op!Van de invorderingsbasis wordt alleen de actuele situatie geadministreerd. Historie kan worden vastgehouden in de zaak. | Aflossingscapaciteit, Beslagvrije voet, Invorderingsmogelijkheid, Type invorderingsmogelijkheid, Vaststeldatum aflossingscapaciteit, Vaststeldatum beslagvrije voet, Vaststeldatum invorderingsmogelijkheid | Nee | GGM |
| **Krediethypotheek** | AlgemeenAls de bijstandsuitkering aan u geleend wordt, kan de gemeente u verplichten een hypotheek op de woning te vestigen. Dit wordt een krediethypotheek genoemd. Gemeenten doen dit om zekerheid te hebben dat de lening in de toekomst wordt afgelost. Bent u eigenaar van een woonwagen of een niet-geregistreerd woonschip? Dan kan de gemeente u verplichten een pandrecht te vestigen. Als de hypotheek of het pandrecht is gevestigd, kunt u gewoon in uw woning blijven wonen.De gemeente kan zelf bepalen of en wanneer zij overgaat tot het vestigen van pandrecht of hypotheek op uw huis, woonschip of woonwagen.Gevolgen krediethypotheekDoor het vestigen van een krediethypotheek gebruikt u de overwaarde van uw woning als onderpand voor uw leenbijstand. Onderpand wil zeggen dat de gemeente uw woning mag verkopen als u uw betalingsverplichtingen niet nakomt. Als u uw rente- en aflossingsverplichtingen niet nakomt, dan kan de gemeente uw woning verkopen en van de opbrengst uw rente– en aflossingsverplichtingen betalen. Als u zelf besluit om uw woning te verkopen, dan moet u (een deel van) de opbrengst gebruiken om uw leenbijstand af te lossen.Kosten krediethypotheekVoor de kosten die u eventueel maakt in verband met de taxatie van de woning en het vestigen van een krediethypotheek kunt u bijzondere bijstand ontvangen. U moet dan wel aan de voorwaarden voor het recht op bijzondere bijstand voldoen.Aflossing leningHieronder worden de situaties beschreven wanneer de lening moet worden afgelost.U stroomt uit de bijstand omdat u werk heeft gevonden. Als u uit de bijstand stroomt omdat u werk heeft gevonden moet u in principe de lening gaan aflossen. Wanneer dat het geval is, is afhankelijk van het gemeentelijke beleid.U moet opnieuw bijstand aanvragen. Is uw bijstand in de vorm van een geldlening geëindigd, maar doet u binnen een bepaalde periode opnieuw een beroep op bijstand? Dan kunt u mogelijk opnieuw bijstand in de vorm van een geldlening ontvangen. Informeer bij de gemeente.U verkoopt de woning. Verkoopt u de woning? Dan moet de lening meestal worden terugbetaald, mits de verkoop voldoende heeft opgebracht.U overlijdt. Als u overlijdt valt de woning in uw nalatenschap. Uw erfgenamen zullen de geldlening dan moeten terugbetalen uit de nalatenschap. De gemeente zal hierover met de erven corresponderen.OverzichtKrediethypotheek leidt dus niet meteen tot een vordering. Toch wordt een krediethypotheek gemeld aan Terug- en Invorderen. Met deze informatie kan beter maatwerk worden geleverd bij het bepalen van de aflossingsafspraken. Hetzelfde geldt voor de leenbijstand. | Bedrag, Vestigingsdatum | Nee | GGM |
| **Krediethypotheekvordering** | AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Relaties tussen vorderingenVorderingen kunnen ook onderling in relatie staan, bijvoorbeeld:Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vorderingIncassokostenvordering voor als er in het kader van een vordering incassokosten zijn gemaakt, die verhaald worden.Rentevordering als bij leningen of kredieten rente in rekening wordt gebracht.Al deze vorderingen zijn zelfstandige vorderingen gerelateerd aan de originele vordering. Zij verkrijgen automatisch dezelfde titel als de originele vordering.InterventieladderBij een terugvordering vanwege het aflossen op een krediethypotheek moet in de interventieladder na een aanmaning een grosse gehaald worden bij de rechter. Vervolgens kan pas doorgeescaleerd worden naar dwangbevel. | *(geen attributen)* | Nee | GGM |
| **Kwijtschelding** | Het kwijtschelden van het restant van de vordering.RedenenDit kan om diverse redenen gebeuren, waaronder redenen uit het beleid.Als een debiteur zijn 36 maanden lang houdt aan de betaalafspraken, dan komt de debiteur in aanmerking voor kwijtschelding. Enkele noties hierbij:Het gaat hier om het houden van de afspraken.Hieronder vallen ook afspraken om tijdelijk niet af te lossen.In principe zal een enkele maand opschorten vanwege een maand niet betalen niet de betaaldiscipline verbreken, omdat de gemeente niet heeft ingegrepen via een interventie.Als de debiteur ineens de helft of meer aflost op de vordering.BedragHet bedrag in de kwijtschelding heeft die hoogte dat de totale restant van de vordering op nul komt. | Bedrag, Boekingsdatum, Reden | Nee | GGM |
| **Leenbijstand** | AlgemeenLeenbijstand is een lening aan de burger, die in termijnen moet worden terugbetaald.TerugbetalingAflossingen op leningen bedragen standaard 5% van de toepasselijke maandnorm inclusief vakantietoeslag (VT);De lening wordt in maximaal 36 termijnen terugbetaald. Het restant wordt afgeschreven. De gemeente vordert terug als iemand zich niet aan de verplichtingen van de leenovereenkomst houdt.Leenbijstand worden gemeld aan Terug- en Invorderen voor een 360-graden view op de debiteur. Dan kan hiermee rekening worden gehouden bij het maken van aflossingsafspraken.Leenbijstand wordt verrekend met de uitkering en zal in dergelijke gevallen niet leiden tot terugvorderenPas als de persoon uit de bijstand gaat, zal het voorliggende proces een terugvorderingsverzoek doen bij Terug- en Invorderen.De totaal gegeven leenbijstand wordt teruggevorderd. Hier is een CBS-categorie voor.Mogelijke gevallen (illustratief)Leenbijstand (in de vorm van Bijzondere Bijstand) is onder andere mogelijk in de volgende situaties:U moet een waarborgsom betalen bij het huren van een huis;U wacht op geld waarvan u kunt leven. Het is bijvoorbeeld mogelijk dat u lange tijd moet wachten op de uitbetaling van een erfenis;U moet door eigen toedoen bijstand aanvragen of eerder aanvragen dan nodig was;U hebt een koophuis, u hebt (redelijk) veel eigen vermogen in het huis zitten en geen of weinig inkomsten;U bent zelfstandige of u bent net gestart met uw eigen bedrijf of beroep.NB: U moet een lening altijd weer terugbetalen. | Aflossingskenmerk, Bedrag, Boekingsdatum, Ontvangstdatum | Nee | GGM |
| **Leenbijstandvordering** | AlgemeenLeenbijstand is een lening aan de burger, die in termijnen moet worden terugbetaald. Zie: Leenbijstand.TerugbetalingAflossingen op leningen bedragen standaard 5% van de toepasselijke maandnorm inclusief vakantietoeslag (VT);De lening wordt in maximaal 36 termijnen terugbetaald. Het restant wordt afgeschreven. De gemeente vordert terug als iemand zich niet aan de verplichtingen van de leenovereenkomst houdt.Leenbijstand wordt verrekend met de uitkering en zal in dergelijke gevallen niet leiden tot terugvorderenPas als de persoon uit de bijstand gaat, zal het voorliggende proces een terugvorderingsverzoek doen bij Terug- en Invorderen.De totaal gegeven leenbijstand wordt teruggevorderd. Hier is een CBS-categorie voor. | *(geen attributen)* | Nee | GGM |
| **Loonbeslagafspraak** | Een loonbeslagafspraak is een aflossingsafspraak.Tevens is het een afspraak tussen twee partijen (organisaties) om voor het aflossen van vorderingen. Hierbij zal de ene partij - de werkgever van de debiteur - een afgesproken bedrag in houden op het loon van de debiteur en het ingehouden bedrag overmaken naar crediteur.Aangezien Loonbeslag een Inkomstencomponent is (zie het inkomstenmodel) ligt er een impliciete relatie tussen de Loonbeslagafspraak en het Loonbeslag. | *(geen attributen)* | Nee | GGM |
| **Rechtmaand** | Een vordering in het kader van de bijvoorbeeld de bijstand kan over meerdere kalendermaanden betreffen. In die maanden had de debiteur recht op die bijstand. Zo'n maand onder die vordering noemt men een rechtmaand.Rechtmaanden worden geadministreerd onder een vorderingscomponent bij de vordering. Als de vordering meerdere rechtmaanden bevat die of niet opvolgend zijn of een jaargrens passeren, dan worden die rechtmaanden opgesplitst in reeksen van opvolgende rechtmaanden binnen een jaar. Elke opsplitsing vormt dan een vorderingscomponent. | Boekjaar, Jaar, Maand | Nee | GGM |
| **Rentevordering** | AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.RentevorderingBepaalde vorderingen zijn rentedragend. De rente wordt niet als aparte component opgevoerd bij de hoofdvordering, maar als een aparte vordering. De rentevordering wordt gerelateerd aan de hoofdvordering. De rentevordering is een zogenaamde accessoire vordering, die zijn titel ontleend aan de hoofdvordering.Dit type vordering is als verbijzondering opgenomen, opdat deze relatie expliciet kan worden gelegd. | *(geen attributen)* | Nee | GGM |
| **Restitutie** | Restitutie is terugbetaling van te veel ontvangen aflossing. Restituties worden geadministreerd onder de vordering. | Bedrag, Betaaldatum, Boekingsdatum | Nee | GGM |
| **Uitstel aflossing** | Er kunnen redenen zijn om het aflossingsplan te pauseren. Zie de opties bij het attribuut Reden uitstel.Het volgende geldt:Uitstel van aflossing grijpt aan op alle afspraken in het aflossingsplan.Uitstel leidt tot termijnbewaking om de medewerker er op te attenderen of het uitstel nog aan de orde zou moeten zijn.De termijn in de termijnbewaking kan verschillen per reden van uitstel. | Aanmaakdatum, Periode einddatum, Periode startdatum, Reden uitstel | Nee | GGM |
| **Vermindering terugvordering** | Vermindering terugvordering is het resultaat van een beslissing de terugvordering te verminderen met een zeker bedrag met zekere motivatie. De vermindering terugvordering wordt geadministreerd onder de vordering. | Bedrag, Boekingsdatum, Motivatie vermindering, Vaststeldatum, Verminderingtype | Nee | GGM |
| **Verrekening** | Bij het vaststellen van de vordering wordt gekeken of de debiteur een uitkering geniet. Er zijn twee soorten situaties van verrekening. inkomstenverrekening waar de inkomsten 6 maanden wordt verrekend met de bijstandsuitkeringverrekening alias inhouding op een uitkering (een soort van loonbeslag) / verrekening in de zin van art. 60 lid 3 en 4 PW.Hier wordt de laatste bedoeld.Verrekening op grond van artikel 60 lid 3 en 4 Participatiewet door de gemeente gaat vóór beslag door een derde (artikel 60 lid 7 Participatiewet). Voor de praktijk betekent dit dat:Een lopend beslag wordt opgeschort zodra de gemeente (op grond van hun invorderingsbevoegdheid) een bedrag gaat verrekenen met de bijstandsuitkering. De beslaglegger wordt van de opschorting op de hoogte gesteld.De verrekening ongewijzigd wordt voortgezet indien nadien beslag door een derde wordt gelegd. De beslaglegger wordt medegedeeld dat het beslag niet uitvoerbaar is in verband met verrekening.Voorwaarde voor verrekening op grond van artikel 60 lid 3 en 4 Participatiewet is dat er een terugvorderingsbesluit of boetebesluit is genomen. Bij verstrekking van bijstand in de vorm van een geldlening kunnen echter de vastgestelde aflossingsbedragen direct worden verrekend op grond van artikel 48 lid 4 Participatiewet. Een terugvorderingsbesluit ingevolge artikel 58 lid 2 onderdeel b Participatiewet is dan dus niet noodzakelijk.Pseudo-verrekening gaat niet voor beslag.Pseudo-verrekening zoals bedoeld in artikel 60a Participatiewet gaat niet voor beslag door een derde onder een andere gemeente (of onder het Uitvoeringsinstituut werknemersverzekeringen of de Sociale verzekeringsbank).Een verrekening is verder te behandelen als een vordering, maar juridisch een ander ding. | *(geen attributen)* | Nee | GGM |
| **Verwijtbare vordering** | Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente. Het zijn vorderingen die zijn ingesteld vanwege het niet nakomen van de inlichtingen-plicht waardoor de uitkerende instantie ten onrechte heeft uitbetaald . De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden gelegd. | *(geen attributen)* | Nee | GGM |
| **Vordering** | Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag (terug) moet betalen aan de gemeente in het kader van de bijstand of een bijstandsgerelateerde uitkering.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden vastgelegd. | Categorie, Fiscaal, Periode einddatum, Periode startdatum, Priotype, Regeling, Stuitingsvoortgangsindicator, Subcategorie, Titel, Vaststeldatum terugvordering, Verjaringsdatum, Verwerkingsstatus | Nee | GGM |
| **Vorderingscomponent** | Vorderingen, die bestaan uit verschillende rechtmaanden, worden gesplitst in vorderingscomponenten alsde rechtmaanden niet aansluitend zijn ofals er tussen opvolgende rechtmaanden een jaarovergang zit.De een opeenvolgende reeks van rechtmaanden binnen een jaar wordt gekoppeld aan de vorderingscomponent. Dit gebeurt tijdens het vaststellen van de terugvordering. | Periode einddatum, Periode startdatum, Priotype | Nee | GGM |

## Overervingshiërarchie

```
Aflossingsafspraak (abstract)
    └── Loonbeslagafspraak
```

```
Diensten::Aanvraag (abstract)
    └── Diensten::Aanvraag levensonderhoud
```

```
Hypotheek (abstract)
    └── Krediethypotheek
```

```
Maatregel (abstract)
    └── Afwijkende maatregel
    └── Boete
    └── Maatregel op uitkering
```

```
Reden aanvraag (abstract)
    └── Reden aanvraag Levensonderhoud
```

```
Reden aanvraag Levensonderhoud (abstract)
    └── Andere reden verzoek
    └── Gestopt betaald werk
    └── Gestopt of verkocht eigen bedrijf
    └── Gestopte bijstanduitkering
    └── Gestopte detentie
    └── Gestopte of verlaagde alimentatie
    └── Gestopte studiefinanciering
    └── Gestopte uitkering
    └── Overleden partner
    └── Verbroken relatie
    └── Vertrek uit asielzoekerscentrum
```

```
Reden afwijkende startdatum (abstract)
    └── Andere reden afwijkende startdatum
    └── Opname instelling
    └── Wachten DigiD
    └── Wachten beslissing instantie
```

```
Voorwaarde (abstract)
    └── Uitsluitingsgrond
    └── Voorliggende voorziening
```

```
Vordering (abstract)
    └── Boetevordering
    └── Incassokostenvordering
    └── Krediethypotheekvordering
    └── Leenbijstandvordering
    └── Rentevordering
    └── Verrekening
    └── Verwijtbare vordering
```

## Relatiediagrammen

### Diagram Diensten

```
Client [1] ──── Aanvraag [0..*] (doet aanvraag)
Client [1..2] ──── Dienst [0..*] (neemt dienst af)
Leveringscomponent [0..*] ──── Kostenplaats [0..1] (heeft)
```

### Diagram GGM en Inkomen

```
Client [1] ──── Normafwijking [0..*] (veroorzaakt)
Debiteur [0..1] ──── Client [1] (verwijst)
Levenssituatie::Levenssituatie [0..1] ──── Reden aanvraag [0..*] (Is reden tot)
Profiel [1] ──── Reden aanvraag [0..1] (bevat)
Terugvorderingsverzoek [0..*] ──── Client [1..2] (betreft)
```

### Diagram Basismodel Inkomen

```
Client [0] ──── Inkomensvoorziening [1] (is partner van)
Client [1..*] ──── Inkomensvoorziening [0..*] (Voorziening Bijstandspartij)
Client [1] ──── Inkomensvoorziening [1] (heeft voorziening)
Client [1] ──── Regeling [0..*] (heeft regeling)
Clientbegeleider [1] ──── Inkomensvoorziening [0..*]
Component [1..*] ──── ComponentSoort [1] (is van soort)
Component [1..*] ──── UitkeringsRun [1] (heeft)
IngeschrevenPersoon [1] ──── Inkomensvoorziening [0..*] (heeft uitkering)
IngeschrevenPersoon  ──── Regeling 
Inkomensvoorziening [1] ──── Component [1..*] (is opgebouwd uit)
Inkomensvoorziening [1] ──── Huisvestingsoort [0..*] (soortHuisvesting)
Inkomensvoorziening [1] ──── RedenBlokkering [0..*] (redenBlokkering)
Inkomensvoorziening [1] ──── RedenInstroom [1..*] (redenInstroom)
Inkomensvoorziening [1] ──── RedenUitstroom [0..*] (redenUitstroom)
Inkomensvoorzieningsoort [1] ──── Inkomensvoorziening [0..*] (is soort voorziening)
Regeling [0..*] ──── Regelingsoort [1] (is regelingsoort)
```

### In- en uitstroom inkomensvoorziening

```
Inkomensvoorziening [1] ──── Huisvestingsoort [0..*] (soortHuisvesting)
Inkomensvoorziening [1] ──── RedenBlokkering [0..*] (redenBlokkering)
Inkomensvoorziening [1] ──── RedenInstroom [1..*] (redenInstroom)
Inkomensvoorziening [1] ──── RedenUitstroom [0..*] (redenUitstroom)
```

### Reden aanvraag- overzicht

```
Levenssituatie::Levenssituatie [0..1] ──── Reden aanvraag [0..*] (Is reden tot)
```

## Observaties

- Dit beleidsdomein bevat 89 entiteiten.
- Entiteiten zijn gegroepeerd in 7 diagramgroepen: Diagram Diensten (22), Diagram GGM en Inkomen (4), Diagram Basismodel Inkomen (7), In- en uitstroom inkomensvoorziening (4), Normafwijking (4), Reden aanvraag- overzicht (21), Diagram Terug- en invordering (27).
- Er zijn 31 generalisatierelaties aanwezig.
