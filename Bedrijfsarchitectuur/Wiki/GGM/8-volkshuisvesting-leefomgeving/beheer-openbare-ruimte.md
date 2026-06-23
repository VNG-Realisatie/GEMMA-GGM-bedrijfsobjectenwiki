---
type: ggm-beleidsdomein
naam: Beheer Openbare Ruimte
definitie: ""Het informatiedomein dat gegevens omvat over: 1. De fysieke objecten in de publieke buitenruimte, inclusief hun kenmerken, locatie en conditie. 2. De processen en activiteiten gericht op het onderhouden, inrichten en beheren van deze objecten.""
taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
aantal_entiteiten: 82
---

# GGM Beleidsdomein: Beheer Openbare Ruimte

### Diagram IMBOR vs IMGeo

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Boom** | Een houtachtig gewas (loofboom of conifeer) met een wortelgestel en een enkele, stevige, houtige stam, die zich boven de grond vertakt. Toelichting: Een houtachtig gewas (loofboom of conifeer) met een wortelgestel en een enkele, stevige, houtige stam, die zich boven de grond vertakt. | beleidsstatus, beoogdeOmlooptijd, boombeeld, boombeschermer, boomgroep, boomhoogteActueel, boomhoogteklasseActueel, boomhoogteklasseEindebeeld, boomspiegel, boomTypeBeschermingsstatusPlus, boomvoorziening, controlefrequentie, feestverlichting, groeifase, groeiplaatsinrichting, herplantplicht, kiemjaar, kroondiameterklasseActueel, kroondiameterklasseEindebeeld, kroonvolume, leeftijd, meerstammig, monetaireBoomwaarde, snoeifase, stamdiameter, stamdiameterklasse, takvrijeRuimteTotGebouw, takvrijeStam, takvrijeZonePrimair, takvrijeZoneSecundair, transponder, type, typeBeschermingsstatus, typeOmgevingsrisicoklasse, typePlus, typeVermeerderingsvorm, veiligheidsklasseBoom, verplant, verplantbaar, vrijeDoorrijhoogte, vrijeDoorrijhoogtePrimair, vrijeDoorrijhoogteSecundair, vrijeTakval | Nee | GGM |

### Diagram Verkeer en Vervoer

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Kast** | Object met een permanent karakter dat dient om iets in te bergen en te beschermen. | aantalDeuren, adresTelecom, BAGCode, breedte, EANCode, fabrikant, hoogte, inbelgegevens, installateur, jaarOnderhoudUitgevoerd, kleur, lengte, leverancier, typeCommunicatie, typeFundering, typeSlot, vermogen | Nee | GGM |
| **Paal** | Langwerpig stuk hout, ijzer, steen enz., dat in de grond staat. | breedte, diameter, hoogte, jaarOnderhoudUitgevoerd, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, leverancier, materiaal, vorm | Nee | GGM |
| **Sensor** | Apparaat voor de meting van een fysieke grootheid (bijv. temperatuur, licht, druk, elektriciteit). | aanleghoogte, elektrakast, frequentieOmvormer, hoogte, jaarOnderhoudUitgevoerd, leverancier, meetpunt, PLC | Nee | GGM |

### Hoofdobjecten IMBOR en Geo-object

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bak** | Object met een permanent karakter dat dient om iets in te bergen of te verzamelen. (bron: definities.geostandaarden.nl) Synoniemen: Bak | breedte, diameter, gewichtLeeg, gewichtVol, hoogte, inhoud, jaarOnderhoudUitgevoerd, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, materiaal, verplaatsbaar, vorm | Nee | GGM |
| **Beheerobject** | Verzamelobject - niveau 1 | aangemaaktDoor, beginGarantieperiode, beheergebied, beheerobjectBeheervak, beheerobjectGebruiksfunctie, beheerobjectMemo, beschermdeFloraEnFauna, buurt, conversieID, datumMutatie, datumOplevering, datumPublicatieLV, datumVerwijdering, eindeGarantieperiode, gebiedstype, gemeente, geometrie, gewijzigdDoor, grondsoort, grondsoortPlus, identificatieIMBOR, identificatieIMGeo, jaarVanAanleg, objectBeginTijd, objectEindtijd, onderhoudsplichtige, openbareRuimte, postcode, relatieveHoogteligging, stadsdeel, status, theoretischEindejaar, tijdstipRegistratie, typeBeheerder, typeBeheerderPlus, typeEigenaar, typeEigenaarPlus, typeLigging, waterschap, wijk, woonplaats, zettingsgevoeligheid, zettingsgevoeligheidPlus | Nee | GGM |
| **Bord** | Paneel waarop (statische) informatie wordt afgebeeld, verwoord in tekst, pictogram of code. | breedte, diameter, drager, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, materiaal, vorm | Nee | GGM |
| **Bouwwerk** | Met de aarde verbonden duurzaam bouwwerk, dat niet valt onder de definities van een pand of kunstwerk (bron: definities.geostandaarden.nl) | aanleghoogte, bouwwerkMateriaal, breedte, fabrikant, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, oppervlakte, typeFundering | Nee | GGM |
| **FunctioneelGebied** | Begrensd en benoemd gebied dat door een functionele eenheid beschreven wordt. (bron: definities.geostandaarden.nl) | functioneelGebiedCode, functioneelGebiedNaam, omtrek, oppervlakte | Nee | GGM |
| **Geo-Object** | Abstractie van een fenomeen in de werkelijkheid, dat direct of indirect is geassocieerd met een locatie relatief ten opzichte van de aarde. [NEN 3610:2011] | datumBeginGeldigheid, datumEindeGeldigheid, identificatie, geometrieSoort | Nee | GGM |
| **Groenobject** | Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten vegetatie. | aantalObstakels, aantalZijden, afvoeren, bereikbaarheid, bergendVermogen, bewerkingspercentage, BGTFysiekVoorkomen, bollen, breedte, breedteklasseHaag, BVC, cultuurhistorischWaardevol, draagkrachtig, ecologischBeheer, fysiekVoorkomenIMGeo, gewenstSluitingspercentage, groenobjectBereikbaarheidPlus, groenobjectConstructielaag, groenobjectRand, groenobjectSoortnaam, haagvoetLengte, haagvoetOppervlakte, herplantplicht, hoogte, hoogteklasseHaag, knipfrequentie, knipoppervlakte, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, leverancier, maaifrequentie, maximaleValhoogte, objectnummer, obstakels, omtrek, ondergroei, oppervlakte, opTalud, taludsteilte, type, typeBewerking, typeOmgevingsrisicoklasse, typePlus, typePlus2, veiligheidsklasseBoom | Nee | GGM |
| **Installatie** | Samenhangend systeem dat een bepaald doel dient. | breedte, EANCode, fabrikant, hoogte, inbelgegevens, installateur, jaarOnderhoudUitgevoerd, lengte, leverancier, typeCommunicatie | Nee | GGM |
| **Kunstwerk** | Civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen en niet bedoeld voor permanent menselijk verblijf. http://definities.geostandaarden.nl | aanleghoogte, antiGraffitiVoorziening, bereikbaarheid, breedte, constructietype, gewicht, hoogte, installateur, jaarConserveren, jaarOnderhoudUitgevoerd, jaarRenovatie, jaarVervanging, kilometreringBegin, kilometreringEinde, kleur, kunstwerkBereikbaarheidPlus, kunstwerkMateriaal, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, leverancier, looprichel, minimumConditiescore, monument, monumentnummer, objectnaam, objectnummer, onderhoudsregime, oppervlakte, orientatie, technischeLevensduur, typeFundering, typeMonument, vervangingswaarde, wegnummer | Nee | GGM |
| **Leiding** | Een geheel van geleiders welke voorzien zijn van één ommanteling en bestemd is voor transport van materie | afwijkendeDieptelegging, breedte, diameter, diepte, eisVoorzorgsmaatregel, geoNauwkeurigheidXY, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, materiaal, themaIMKL, verhoogdRisico | Nee | GGM |
| **Leidingelement** | Een object dat bij een leiding behoort. | afwijkendeDieptelegging, diepte, geoNauwkeurigheidXY, jaarOnderhoudUitgevoerd, leverancier, themaIMKL | Nee | GGM |
| **Mast** | Draagconstructie, bestaande uit een verticale buispaal, die wordt gebruikt om iets op hoogte te brengen. | *(geen attributen)* | Nee | GGM |
| **Meubilair** | De verzameling van ruimtelijke objecten ter inrichting van de openbare ruimte of terreinen. Een ruimtelijk object ter inrichting van de openbare ruimte. | aanleghoogte, bouwjaar, breedte, datumAanschaf, diameter, fabrikant, gewicht, hoogte, installateur, jaarOnderhoudUitgevoerd, jaarPraktischEinde, kleur, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, leverancier, meubilairMateriaal, model, ondergrond, oppervlakte, prijsAanschaf, serienummer, transponder, transponderlocatie, typeFundering, typePlaat | Nee | GGM |
| **Overbruggingsobject** | Onderdeel van een beweegbare of vaste verbinding tussen twee punten, die door water, een weg of anderszins gescheiden zijn, dat essentieel is voor de constructie . | aanleghoogte, antiGraffitiVoorziening, bereikbaarheid, breedte, hoogte, installateur, jaarConserveren, jaarOnderhoudUitgevoerd, jaarRenovatie, jaarVervanging, kleur, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, looprichel, minimumConditiescore, onderhoudsregime, oppervlakte, overbruggingsobjectMateriaal, overbruggingsobjectModaliteit, technischeLevensduur, typeFundering, vervangingswaarde | Nee | GGM |
| **Put** | Verticale waterdichte constructie, toegepast om leidingen aan te sluiten, van richting of niveau te veranderen, om toegang te verschaffen aan personeel en/of apparatuur voor inspectie en onderhoud, en om beluchting en ventilatie mogelijk te maken | bovengrondsZichtbaar, breedte, diameter, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, maaiveldhoogte, materiaal, toegankelijk, typeAfdekking, vorm, wanddikte | Nee | GGM |
| **Scheiding** | Kunstmatig, meestal lineair obstakel met een werende functie. | aanleghoogte, breedte, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, objectnaam, objectnummer, oppervlakte, scheidingMateriaal, verplaatsbaar | Nee | GGM |
| **Terreindeel** | Kleinste functioneel onafhankelijk stukje van een terrein, dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met of zonder aaneengesloten vegetatie. | breedte, cultuurhistorischWaardevol, herplantplicht, oppervlakte, opTalud, percentageLoofbos, terreindeelSoortnaam, type, typeBewerking, typePlus, typePlus2 | Nee | GGM |
| **Tunnelobject** | Onderdeel van een kunstmatig aangelegde, kokervormige onderdoorgang dat essentieel is voor de constructie. | aanleghoogte, aantalTunnelbuizen, breedte, doorrijbreedte, doorrijhoogte, hoogte, jaarConserveren, jaarOnderhoudUitgevoerd, lengte, leverancier, objectnaam, objectnummer, oppervlakte, tunnelobjectMateriaal | Nee | GGM |
| **Vegetatieobject** | Verzamelobject van alle vegetatieobjecten - niveau 2 | afvoeren, bereikbaarheid, ecologischBeheer, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, kweker, leverancier, objectnummer, soortnaam, typeStandplaats, typeStandplaatsPlus, vegetatieobjectBereikbaarheidPlus | Nee | GGM |
| **Verhardingsobject** | Verharde lagen van een weglichaam, speel- en sportondergronden en onbegroeid terreindelen inclusief de fundering. | aanleghoogte, aanOfVrijliggend, aantalDeklagen, aantalOnderlagen, aantalTussenlagen, afmeting, belasting, bergendVermogen, BGTFysiekVoorkomen, breedte, dikteConstructie, draagkrachtig, formaat, fysiekVoorkomenIMGeo, geluidsreducerend, jaarConserveren, jaarOnderhoudUitgevoerd, jaarPraktischEinde, kleur, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, lengteKunstgras, lengteVoegen, levensduur, materiaal, maximaleValhoogte, omtrek, ondergrondcode, oppervlakte, opTalud, plaatsorientatie, prijsAanschaf, rijstrook, soortVoeg, toelichtingGemengdeBestrating, type, typeConstructie, typeFundering, typePlus, typePlus2, typeRijstrook, typeVoeg, typeVoegvulling, vegen, verhardingsobjectConstructielaag, verhardingsobjectModaliteit, verhardingsobjectRand, verhardingsobjectWegfunctie, verhoogdeLigging, vulmateriaalKunstgras, waterdoorlatendheid, wegas, wegcategorieDV, wegcategorieDVPlus, wegnummer, wegtypeBestaand, wegvak, wegvaknummer | Nee | GGM |
| **Verlichtingsobject** | Paal of mast waaraan openbare verlichting is bevestigd. | *(geen attributen)* | Nee | GGM |
| **Waterinrichtingsobject** | Een ruimtelijk object ter inrichting van het water. | aanleghoogte, breedte, jaarConserveren, jaarOnderhoudUitgevoerd, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, leverancier, materiaal, oppervlakte | Nee | GGM |
| **Waterobject** | Kleinste functioneel onafhankelijk stukje water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen het objecttype Water van NEN 3610 wordt onderscheiden en dat permanent met water bedekt is. (imgeo.geostandaarden.nl) | breedte, folie, hoogte, infiltrerendOppervlak, infiltrerendVermogen, lengte, lozingspunt, oppervlakte, porositeit, streefdiepte, type, typePlus, typePlus2, typeVaarwater, typeWaterplant, uitstroomniveau, vaarwegtraject, vorm, waternaam, waterpeil, waterpeilWinter, waterpeilZomer, waterplanten | Nee | GGM |
| **Weginrichtingsobject** | Een ruimtelijk object dat dient voor de inrichting van de openbare weg. | aanleghoogte, breedte, hoogte, jaarConserveren, jaarOnderhoudUitgevoerd, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, leverancier, materiaal, oppervlakte, weginrichtingsobjectWegfunctie | Nee | GGM |

### Meldingen Graafwerkzaamheden

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Grondbeheerder** | Beheerder van grondgrondbeheer., oplossing voor duurzaam landbeheer en voedselproductie | *(geen attributen)* | Nee | GGM |
| **MOOR-melding** | Meldingsproces rondom werkzaamheden aan kabels en leidingen. | datumAanmelding, wegbeheerder, adresaanduiding, starttijd, eindtijd, datumGoedkeuring, publiceren, goedgekeurd, herstelwerkzaamhedenVereist, omschrijvingHerstelwerkzaamheden | Nee | GGM |
| **Omgevingsvergunning** | Vergunning als bedoeld in afdeling 5.1 van de Omgevingswet | *(geen attributen)* | Nee | GGM |
| **Opbreking** | Vorm van wegwerkzaamheid | *(geen attributen)* | Nee | GGM |
| **Proces-verbaal-MOOR-melding** | Officieel op papier gesteld verslag met betrekking tot heen MOOR-melding | datum, goedkeuring, opmerkingen | Nee | GGM |
| **Uitvoerder Graafwerkzaamheden** | Degene die op de bouwlocatie van een project de leiding heeft met betrekking tot de graafwerkzaamheden | *(geen attributen)* | Nee | GGM |

### Ruimte WOZ en Benoemd Object

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **KadastraleMutatie** | Wijziging in de kadatrale registratie | *(geen attributen)* | Nee | GGM |

### Schouwrondes Beheersobjecten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Actie** | Kleinst mogelijke eenheid van werk die zinvol onderscheiden kan worden, uitgevoerd door een persoon of machine op 1 plek op 1 moment. | *(geen attributen)* | Nee | GGM |
| **CROW-Melding** | BOR-MELD is een CROW-standaard voor het vastleggen van meldingen. | kwaliteitsniveau | Nee | GGM |
| **Inspectie** | het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen. | *(geen attributen)* | Nee | GGM |
| **Kwaliteitscatalogus Openbare Ruimte** | zie https://www.crow.nl/publicaties/kwaliteitscatalogus-openbare-ruimte-2018 | *(geen attributen)* | Nee | GGM |
| **Logboek** | Registratie waarin gebeurtenissen worden bijgehouden. | *(geen attributen)* | Nee | GGM |
| **Melding** | De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend | datumMelding, status, categorie, constatering, opmerkingen, advies, datumAdvies, uitgevoerd, datumUitvoering, foto, locatie | Nee | GGM |
| **MeldingOngeval** | Aangifte vna een ongeval | *(geen attributen)* | Nee | GGM |
| **Schouwronde** | Activiteit om te controleren of de opdrachtnemer aan de afspraken voldoet. | *(geen attributen)* | Nee | GGM |
| **Storing** | Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren. | *(geen attributen)* | Nee | GGM |

### Schouwrondes en Arealen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Areaal** | Het verspreidingsgebied van een een soort, een levensgemeenschap of een biotooptype. | geometrie | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aansluitput** | Type put met de functie aansluitleidingen aansluiten | aansluitpunt, risicogebied, type | Nee | GGM |
| **Afvalbak** | Inzamelobject voor afval in de openbare ruimte dat handmatig kan worden leeggemaakt. Toelichting: Inzamelobject voor afval in de openbare ruimte dat handmatig kan worden leeggemaakt. | type, typePlus | Nee | GGM |
| **Bank** | Aaneengesloten zitplaats voor verscheidene personen, bedoeld voor openbaar gebruik en geplaatst in de openbare ruimte (vnl. in parken, plantsoenen, bossen en langs wegen). | type, typePlus | Nee | GGM |
| **Bemalingsgebied** | Een rioleringsgebied waaruit het afvalwater door een gemaal wordt verwijderd. Toelichting: Een rioleringsgebied waaruit het afvalwater door een gemaal wordt verwijderd | rioleringsgebied | Nee | GGM |
| **Bergingsbassin** | Een gesloten reservoir waarin het afvalwater tijdelijk wordt opgevangen Synoniemen: Retentiebassin, bufferbassin | bergendVermogen, pompLedigingsVoorziening, pompSpoelVoorziening, spoelleiding, vorm | Nee | GGM |
| **Brug** | Kunstwerk over een waterweg, watergang of waterloop, bestaande uit een brugdek gesteund door pijlers en/of landhoofden. | aantalOverspanningen, bedienaar, bedieningstijden, belastingklasseNieuw, belastingklasseOud, beweegbaar, doorrijbreedte, draagvermogen, hoofdroute, hoofdvaarroute, maximaalToelaatbaarVoertuiggewicht, maximaleAsbelasting, maximaleOverspanning, statischMoment, type, typePlus, zwaarsteVoertuig | Nee | GGM |
| **Deelplan/Veld** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Drainageput** | Put welke toegang geeft naar een poreuze of geperforeerde buisleiding, aangebracht onder de grond om de afwatering van de grond te verbeteren. | risicogebied, type | Nee | GGM |
| **Ecoduct** | Wildwissel in de vorm van een viaduct voor passages van dieren over een weg of spoorweg. IMGeo Synoniemen: Natuurbrug, Faunabrug, Ecobrug, Ecopassage, Natuurpassage Toelichting: Opheffen van barriÃ¨res en de migratie van fauna mogelijk maken tussen of binnen leefgebieden en populaties. | aantalOverspanningen, draagvermogen, maximaalToelaatbaarVoertuiggewicht, maximaleAsbelasting, maximaleOverspanning, overbruggingsobjectDoorrijopening, type, zwaarsteVoertuig | Nee | GGM |
| **Fase/Oplevering** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Fietsparkeervoorziening** | Een duurzaam verankerd rek in de openbare ruimte voor het stallen van fietsen | aantalParkeerplaatsen, type, typePlus | Nee | GGM |
| **Filterput** | Put met een filterconstructie voor het onttrekken van grondwater. Kan ook beschouwd worden als een soort drainagevoorziening. | drain, risicogebied | Nee | GGM |
| **Flyover** | Kunstwerk in de vorm van een viaduct dat deel uitmaakt van een verkeersbaan en waarmee een verkeersstroom over twee of meer ongelijkvloerse verkeersstromen wordt geleid. | aantalOverspanningen, belastingklasseNieuw, belastingklasseOud, draagvermogen, maximaalToelaatbaarVoertuiggewicht, maximaleAsbelasting, maximaleOverspanning, overbruggingsobjectDoorrijopening, type, zwaarsteVoertuig | Nee | GGM |
| **Geluidsscherm** | Een scheiding bedoeld om geluidshinder in de buitenlucht te verminderen. (IMGeo) | aantalDeuren, aantalPanelen, type | Nee | GGM |
| **Gemaal** | Een constructie ten behoeve van het verplaatsen van water | aantalBedrijfsaansluitingen, aantalHuisaansluitingen, aantalPompen, bedienaar, effectieveGemaalcapaciteit, hijsinrichting, lanceerinrichting, pompenInSamenloop, type, veiligheidsrooster | Nee | GGM |
| **Infiltratieput** | Een put met waterdoorlatende wanden bestemd voor de inzameling van hemelwater, waarbij het hemelwater door middel van infiltratie door de wanden kan worden afgevoerd | porositeit, risicogebied | Nee | GGM |
| **Kademuur** | Verticale wand ter scheiding van land en water, opgebouwd uit een muur van gemetselde stenen of gestort beton. (bron: definities.geostandaarden.nl) | belastingklasseNieuw, belastingklasseOud, grijpstenen, hoogteBovenkantKademuur, materiaalBovenkantKademuur, oppervlakteBovenkantKademuur, reddingslijn, type, typeBovenkantKademuur, typeFundering, typeVerankering | Nee | GGM |
| **Keermuur** | Muur die door vorm, gewicht en fundering zonder verankering de grond keert, vaak van beton met L-vormige doorsnede. Een keermuur of keerwand is een stijf, grond- of waterkerend kunstwerk dat door een groot gewicht en een brede voet een grote standzekerheid kan bereiken. Een keermuur is meestal van gewapend beton, maar er kan ook ander materiaal gebruikt worden. (IMGeo) Synoniemen: Keerwand, klip | belastingklasseNieuw, belastingklasseOud, type | Nee | GGM |
| **Klimplant** | Plant met buigzame stengels die zich op diverse manieren aan muren, bomen of constructies hecht en zodoende omhoog klimt. Toelichting: Plant met buigzame stengels die zich op diverse manieren aan muren, bomen of constructies hecht en zodoende omhoog klimt. | hoogte, knipfrequentie, knipoppervlakte, ondersteuningsvorm, type | Nee | GGM |
| **Kolk** | Een reservoir bestemd voor de opvang van hemelwater afkomstig van erop aangesloten oppervlakken, het laten bezinken van in dit water meegevoerde bezinkbare stoffen en de afvoer van dit water naar een rioolstelsel of naar de ondergrond. Synoniemen: Afvoerput | bereikbaarheidKolk, risicogebied, type | Nee | GGM |
| **Kwaliteitskenmerken** | Aanduiding van de hoedanigheid van uitvoering, bewerking en representativiteit van een meting, volgens een overeengekomen waarderingsschaal. | *(geen attributen)* | Nee | GGM |
| **Onderhoud** | Maatregelen om de functionele kwaliteit in stand te houden of te herstellen en dus de levensduur van een (object)onderdeel te realiseren c.q. te verlengen. | *(geen attributen)* | Nee | GGM |
| **Overstortconstructie** | Een constructie voorzien van een overstortdrempel met een ontworpen drempelbreedte en -hoogte. | bassin, drempelbreedte, drempelniveau, klep, type, vormDrempel, waking | Nee | GGM |
| **Pomp** | Een technische installatie die het (afval) water onder druk transporteert. | aanslagniveau, beginstandDraaiurenteller, besturingskast, laatsteStandDraaiurenteller, laatsteStandkWhTeller, levensduur, model, motorvermogen, onderdeelMetPomp, ontwerpcapaciteit, pompcapaciteit, serienummer, type, typeOnderdeelMetPomp, typePlus, typeWaaier, uitslagpeil | Nee | GGM |
| **Putdeksel** | Deksel met als functie het afdekken van een put (GWSW). Dekt meestal de opening van een rioolput af, is meestal rond, van zwaar metaal, soms van kunststof. | diameter, put, type, vorm | Nee | GGM |
| **Rioleringsgebied** | Het gebied waarbinnen één of meerdere inliggende rioolstelsel(s) het afvalwater naar één gemaal of overnamepunt transporteert/teren. Een rioleringsgebied kan een enkelvoudig gebied zijn, maar kan ook meerdere rioleringsgebieden omvatten. Een gebied is zodanig gekozen dat het voldoende inzicht geeft in de belasting van oppervlaktewater en overnamepunt. Toelichting: Het gebied waarbinnen één of meerdere inliggende rioolstelsel(s) het afvalwater naar één gemaal of overnamepunt transporteert/teren. Een rioleringsgebied kan een enkelvoudig gebied zijn, maar kan ook meerdere rioleringsgebieden omvatten. Een gebied is zodanig gekozen dat het voldoende inzicht geeft in de belasting van oppervlaktewater en overnamepunt. | rioleringsgebied, zuiveringsgebied | Nee | GGM |
| **Rioolput** | Constructie toegang gevend tot het rioolstelsel | aantalBedrijven, aantalRecreatie, aantalWoningen, afvoerendOppervlak, bergendOppervlak, rioolputConstructieonderdeel, rioolputRioolleiding, risicogebied, toegangBreedte, toegangLengte, type, typePlus | Nee | GGM |
| **SolitairePlant** | Plant, heester of siergras, te beheren als solitair beplantingselement. | hoogte, type | Nee | GGM |
| **Speelterrein** | Geheel van begroeiing verharding opstallen en speelwerktuigen bedoeld als speelplaats voor kinderen. Synoniemen: Speelplek, Speelgelegenheid | jaarHerinrichting, speelterreinLeeftijdDoelgroep, type, typePlus | Nee | GGM |
| **Speeltoestel** | Toestel en structuren, met inbegrip van componenten en constructieve onderdelen, waarmee of waarop kinderen binnen of buiten kunnen spelen, individueel of gezamenlijk, volgens hun eigen spelregels of beweegredenen, die te allen tijde kunnen worden gewijzi Synoniemen: Speelvoorziening | catalogusprijs, certificaat, certificaatnummer, certificeringsinstantie, controlefrequentie, datumCertificaat, gemakkelijkToegankelijk, inspectievolgorde, installatiekosten, speelterrein, speeltoestelToestelonderdeel, technischeLevensduur, toestelcode, toestelgroep, toestelnaam, type, typenummer, typePlus, typePlus2, valruimteHoogte, valruimteOmvang, vrijeValhoogte | Nee | GGM |
| **Sportterrein** | Terrein mogelijk met groenvoorziening, verharding en bebouwing bestemd voor sportbeoefening. Synoniemen: Sportveld | drainage, gebruiksvorm, sportcomplex, sportterreinTypeSport, type, typePlus, veldnummer, verlicht | Nee | GGM |
| **Stuwgebied** | Een deelgebied van een bemalingsgebied waarvan de afvoer via een stuwput of stuwriool wordt beperkt. | bemalingsgebied | Nee | GGM |
| **Taak** | Een samenhangende set activiteiten. | *(geen attributen)* | Nee | GGM |
| **Uitlaatconstructie** | Het eindpunt van een rioolleiding waar uitstroming van afvalwater uit het rioolstelsel naar het oppervlaktewater mogelijk is. | type, waterobject | Nee | GGM |
| **Verkeersdrempel** | Verhoging in de rijbaan, bedoeld om het gemotoriseerde verkeer met een lage(re) snelheid te laten rijden. Toelichting: Sinds ongeveer 2000 beschikt de Nederlandse wegenbouw over technische mogelijkheden om drempels uit te voeren in een doorlopende asfaltverharding en dan zodanig dat deze een specifieke snelheid uitlokken bij circa 80 procent van het gemotoriseerde verkeer. | ontwerpsnelheid, type, typePlus | Nee | GGM |
| **Verkeerslicht** | Lichten die aangeven dat je moet stoppen, dat je mag doorrijden, of die je waarschuwen voor gevaar. | *(geen attributen)* | Nee | GGM |
| **Viaduct** | Kunstwerk over een weg, spoorweg of terreinverdieping, bestaande uit een dek gesteund door pijlers en/of landhoofden. | aantalOverspanningen, belastingklasseNieuw, belastingklasseOud, draagvermogen, maximaalToelaatbaarVoertuiggewicht, maximaleAsbelasting, maximaleOverspanning, overbruggingsobjectDoorrijopening, type, waterobject, zwaarsteVoertuig | Nee | GGM |

## Overervingshiërarchie

```
Bak (abstract)
    └── Afvalbak
```

```
Beheerobject (abstract)
    └── Bak
    └── Bord
    └── Bouwwerk
    └── FunctioneelGebied
    └── Groenobject
    └── Installatie
    └── Kast
    └── Kunstwerk
    └── Leiding
    └── Leidingelement
    └── Mast
    └── Meubilair
    └── Overbruggingsobject
    └── Paal
    └── Put
    └── Scheiding
    └── Sensor
    └── Terreindeel
    └── Tunnelobject
    └── Vegetatieobject
    └── Verhardingsobject
    └── Verlichtingsobject
    └── Waterinrichtingsobject
    └── Waterobject
    └── Weginrichtingsobject
```

```
Bouwwerk (abstract)
    └── Bergingsbassin
```

```
FunctioneelGebied (abstract)
    └── Bemalingsgebied
    └── Rioleringsgebied
    └── Speelterrein
    └── Sportterrein
    └── Stuwgebied
```

```
Grondbeheerder (abstract)
    └── Uitvoerder Graafwerkzaamheden
```

```
Installatie (abstract)
    └── Pomp
```

```
Kunstwerk (abstract)
    └── Gemaal
    └── Overstortconstructie
    └── Uitlaatconstructie
```

```
Leverancier (abstract)
    └── Uitvoerder Graafwerkzaamheden
```

```
Melding (abstract)
    └── Actie
    └── CROW-Melding
    └── Inspectie
    └── MeldingOngeval
    └── Storing
```

```
Meubilair (abstract)
    └── Bank
    └── Fietsparkeervoorziening
    └── Speeltoestel
```

```
Overbruggingsobject (abstract)
    └── Brug
    └── Ecoduct
    └── Flyover
    └── Viaduct
```

```
Put (abstract)
    └── Aansluitput
    └── Drainageput
    └── Filterput
    └── Infiltratieput
    └── Kolk
    └── Rioolput
```

```
Rechtspersoon (abstract)
    └── Grondbeheerder
```

```
Scheiding (abstract)
    └── Geluidsscherm
    └── Kademuur
    └── Keermuur
```

```
Vegetatieobject (abstract)
    └── Boom
    └── Klimplant
    └── SolitairePlant
```

```
Weginrichtingsobject (abstract)
    └── Putdeksel
    └── Verkeersdrempel
```

## Relatiediagrammen

```
Areaal [1..*] ──── Schouwronde [0..*]
Beheerobject [1..1] ──── Logboek [0..1]
CROW-Melding [0..*] ──── Kwaliteitscatalogus Openbare Ruimte [1..1]
Geo-Object [1..1] ──── Beheerobject [0..1]
Logboek [1..1] ──── Melding [0..*]
MOOR-melding ──── Omgevingsvergunning
MOOR-melding ──── Opbreking
MOOR-melding ──── Proces-verbaal-MOOR-melding
Melding [0..*] ──── Beheerobject [1..*]
Schouwronde [0..1] ──── Melding [0..*]
Uitvoerder Graafwerkzaamheden ──── MOOR-melding
Uitvoerder Graafwerkzaamheden ──── Opbreking
```

## Observaties

- Dit beleidsdomein bevat 82 Objecttype-entiteiten (+ 118 Enumeraties).
- Entiteiten zijn gegroepeerd in 10 diagramgroepen: Diagram IMBOR vs IMGeo (1), Diagram Verkeer en Vervoer (3), Hoofdobjecten IMBOR en Geo-object (26), Hoofdobjecten IMGeo en Beheerobjecten  (2), Kern:Overige geo objecten op hoofdlijnen (1), Meldingen Graafwerkzaamheden (6), Ruimte WOZ en Benoemd Object (1), Schouwrondes Beheersobjecten (10), Schouwrondes en Arealen (2), Woningbouwprojecten (1).
- Er zijn 65 generalisatierelaties aanwezig.
