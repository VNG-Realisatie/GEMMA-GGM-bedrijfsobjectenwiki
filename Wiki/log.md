# Wiki Log

## [2026-06-19] reconsider | Bestuur — GGM-hiaten hergeclassificeerd
- Feedback: GGM-scope is dataobjecten (wat gemeenten registreren), niet processen (hoe werk verloopt)
- **Herclassificatie:**
  - **Verkiezing** en **Referendum**: Processen, niet dataobjecten → **geen terugmelding** naar GGM (structureel uit scope)
  - **Stembureau**: Registratieobject (fysieke locaties met capaciteit) → **wel terugmelding** (dataobject, pakt in GGM-scope)
  - **Gemeenschappelijke Regeling**: Juridische entiteit met registreerbare eigenschappen → **wel terugmelding** (dataobject, pakt in GGM-scope)
- BO-pagina's bijgewerkt met uitleg waarom sommige processen zijn (en dus niet in GGM-scope)
- [[Wiki/Analyses/ggm-terugmeldingen]] bijgewerkt: 4 items → 2 items (alleen Stembureau en GR als potentiële hiaten)

## [2026-06-19] ingest | Bestuur — 4 BO's aangemaakt
- Bronnen: 9 VNG-onderwerpenpagina's (rubriek + 8 onderwerpen)
- Directory: Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/
- 4 BO's aangemaakt — grondslag: procesobject/governance-object (geen GGM-grondslag)
  - **Verkiezing** (procesobject) — periodieke vervangingskeuze ambtsdragers; 6/6 criteria
  - **Referendum** (procesobject) — volksstemming; 6/6 criteria
  - **Stembureau** (procesobject, maar dataobject-karakter) — fysieke locatie stemming; 6/6 criteria
  - **Gemeenschappelijke Regeling** (governance-object, maar dataobject-karakter) — Wgr-samenwerkingsconstructie; 6/6 criteria
- 9 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Bestuur/
- Domeinoverzicht aangemaakt met status: afgerond (na herclassificatie)
- Index en log bijgewerkt

## [2026-06-19] lint & fixes | Wiki lint-issues opgelost
- **Wees-BO's:** domeinoverzicht Terug-en-invordering aangemaakt voor 7 BO's (aflossing, aflossingsplan, afschrijving, interventie, kwijtschelding, restitutie, vordering)
- **Herleidbaarheid:** MAP.md voorzien van bronnen-veld (Asiel en Integratie/vng-inburgering)
- **Enum-validatie:** bestuursovereenkomst.md archimate_type gecorrigeerd (contract → business-object)
- Index bijgewerkt met Terug-en-invordering domeinoverzicht

## [2026-06-19] bedrijfsobjecten | Asiel en Integratie — 15 BO's aangemaakt
- Directory: Wiki/Bedrijfsobjecten/Asiel-en-Integratie/
- 13 BO's met grondslag ggm-entiteit (GGM beleidsdomein Inburgering, taakveld 6): Asielstatushouder, Gezinsmigrant, Brede Intake, PIP, Inburgeringstraject, Leerroute, Inburgeringsplicht, Examen, Inburgeringsaanbod, Inburgeringstermijn, MAP, PVT, Voorbereiding op Inburgering
- 1 procesobject zonder GGM: Opvanglocatie (asielopvang structureel niet gemodelleerd in GGM)
- 1 governance-object zonder GGM: Bestuursovereenkomst (contract, overeenkomst gemeente-COA)
- Alle 13 GGM-matches: matchsterkte exact
- GGM-entiteiten geaggregeerd in BO's: B1-route en Z-route → classificatie van Leerroute; Examenonderdeel → detail van Examen; Ontheffing en Vrijstelling → status van Inburgeringsplicht; Aanvraag verlenging → processtap van Inburgeringstermijn
- Index bijgewerkt met sectie Asiel en Integratie

## [2026-06-19] ingest | Arbeidszaken — CvA-bronnen toegevoegd
- Bronnen: College voor Arbeidszaken.md, cva-beleidsplan_2023-2026.md (verplaatst uit opgeheven folder Bedrijfsvoering)
- 2 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Arbeidszaken/
- Conclusie ongewijzigd: 0 BO's, bronnen bevestigen governance/instrument-karakter domein
- Domeinoverzicht bijgewerkt: bronnen_count 9 → 11

## [2026-06-19] ingest | Arbeidszaken — domein afgerond (0 BO's)
- Bronnen: 9 VNG-onderwerpenpagina's (rubriek + 8 onderwerpen)
- Conclusie: geen BO's — domein betreft gemeente als werkgever, structureel buiten GGM-scope
- Alle bronnen zijn instrumenten (cao, gedragscode, rechtspositieregeling) en thema's (arbeidsmarktkrapte, integriteitsbeleid)
- Geen begrippenpagina's aangemaakt (geen BO-kandidaten)
- Domeinoverzicht aangemaakt met status: afgerond

## [2026-06-18] ingest | RGBZ 1.0 en ZTC2 v2.1 — domein Dienstverlening
- Bronnen: RGBZ 1.0 (KING, 2010), GEMMA ZTC2 Informatiemodel v2.1 (KING, 2014)
- Clippings verplaatst van Clippings/ naar Sources/Standaarden/
- Begrippen geëxtraheerd (5): zaakgericht werken (thema/operationeel), zaaktypecatalogus (object/operationeel), informatieobject (object/operationeel), zaakdossier (object/operationeel), resultaattype (object/operationeel)
- Pagina's aangemaakt: 5 begrippen, 2 bronsamenvattingen, 1 domeinoverzicht (Dienstverlening)
- Pagina's bijgewerkt: ggm-dekkingspatroon (Dienstverlening-sectie toegevoegd), gemma-bedrijfsobjecten-en-ggm (kruisverwijzingen)
- GGM-relatie: taakveld 10 Dienstverlening bestaat, nog geen GGM-bronbestand; taakveld 99 Kern/RGBZPlus dekt runtime (25 entiteiten) maar niet ZTC2-configuratielaag
- Structureel hiaat: CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE, ZAAKOBJECTTYPE ontbreken in GGM

## [2026-06-18] ingest | Introductie RGBZ (vng-realisatie.github.io)
- Bron: Introductie RGBZ (VNG Realisatie), verplaatst naar Sources/Standaarden/introductie-rgbz.md
- Samengevoegd met bestaande RGBZ-bronsamenvatting
- Meerwaarde: RGBZ 2.0 (concept, nooit vastgesteld) → ZGW API's (officieel); berichtenarchitectuur (StUF-ZKN, Zaak- en Documentservices, ZGW API's)
- Pagina's bijgewerkt: rgbz-informatiemodel (sectie Status en evolutie + Berichtenarchitectuur), zaakgericht-werken (berichtenstandaarden), dienstverlening (evolutie-sectie + openstaande vraag actualiteit RGBZPlus)

## [2026-06-18] ingest | 3 Raadgever-bronnen belastingendomein
- Bronnen: raadgever-gemeentelijke-belastingen, raadgever-kostenonderbouwing-lokale-heffingen, raadgever-woz
- Clippings verplaatst van Clippings/ naar Sources/Onderwerpen VNG/Belastingen/
- Raadgever Riool- en waterzorgheffing overgeslagen: duplicaat van bestaand bronbestand
- Begrippen geëxtraheerd (6): woz-waarde, woz-beschikking, onroerende-zaak, waarderingskamer, kruissubsidiering, kostenonderbouwing
- Bestaande begrippen bijgewerkt met nieuwe bronverwijzing: belastingmix, kostendekkend-tarief, kwijtschelding
- Pagina's aangemaakt: 6 begrippen, 3 bronsamenvattingen
- Pagina's bijgewerkt: domeinoverzicht belastingen, index

## [2026-06-18] ingest | 4 Raadgever-bronnen financiëndomein (NIEUW)
- Bronnen: raadgever-inkomstenbronnen-gemeenten, raadgever-gemeentebegroting-en-jaarrekening, raadgever-financiele-verordening, raadgever-financiele-conditie-gemeente
- Clippings verplaatst van Clippings/ naar Sources/Onderwerpen VNG/Financien/ (nieuwe map)
- Begrippen geëxtraheerd (10): gemeentefonds, algemene uitkering, specifieke uitkering, begrotingscyclus, budgetrecht, financiele verordening, kadernota, solvabiliteitsratio, netto schuldquote, onbenutte belastingcapaciteit
- Pagina's aangemaakt: 10 begrippen, 4 bronsamenvattingen, 1 domeinoverzicht (Financien)
- Koppeling met bestaande bedrijfsobjecten: Begroting, Taakveld, Doelstelling, Product, Kostenplaats, Activa
- Stub domeinoverzicht gemeentelijke-belasting.md verwijderd (duplicaat van belastingen.md)

## [2026-06-18] ingest | 1 Raadgever-bron bedrijfsvoering (NIEUW)
- Bron: raadgever-inkoop-en-aanbesteden
- Clipping verplaatst van Clippings/ naar Sources/Onderwerpen VNG/Bedrijfsvoering/ (nieuwe map)
- Begrippen geëxtraheerd (3): gemeentelijke inkoop, aanbesteding, mvoi
- Pagina's aangemaakt: 3 begrippen, 1 bronsamenvatting, 1 domeinoverzicht (Bedrijfsvoering)
- Koppeling met bestaande bedrijfsobjecten: Inkooporder, Factuur, Werkorder

## [2026-06-18] bronnen | RSGB en VNG Informatiemodellen
- Sources/Standaarden gelezen: RSGB 2.02 Deel I, Wat is een Informatiemodel
- Bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/Standaarden/rsgb-en-informatiemodellen.md
- Analyse ggm-oorsprong-en-meerwaarde.md gecorrigeerd: GGM niet alleen uit databases maar uit drie lagen bronnen (informatiemodellen basisregistraties, RSGB als integratiemodel, domeinmodellen uit bestaande systemen)
- RSGB beschrijft wat de gemeente met basisregistraties uitwisselt; gemeente registreert intern meer in de bronregistraties

## [2026-06-18] bronnen | GEMMA-referentiearchitectuur
- 8 pagina's geraadpleegd op gemmaonline.nl: Bedrijfsobjecten, GEMMA en het GGM, Procesarchitectuur kennismodel, Bedrijfsfuncties, Bedrijfsarchitectuur, Visie op zaakgericht werken, Procesarchitectuur relatie met zaakgericht werken, Samenhang PDC/UPL/ZTC/verwerkingsregister
- Geconsolideerd bronbestand aangemaakt: Sources/GEMMA/gemma-bedrijfsobjecten-en-ggm.md
- Bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/GEMMA/gemma-bedrijfsobjecten-en-ggm.md
- Kernbevindingen: (1) GEMMA leidt 507 bedrijfsobjecten af uit GGM-dataobjecten, (2) zaak is al een procesobject in GEMMA maar niet gegeneraliseerd naar het bedrijfsobjectenmodel, (3) GEMMA noemt zelf uitbreiding bedrijfsarchitectuur als verbetervoorstel
- Analyse ggm-oorsprong-en-meerwaarde.md uitgebreid met sectie over zaakgericht werken als bestaand verbindingsmechanisme
- Geen begrippen geëxtraheerd — deze bronnen zijn architectuurkader, geen beleidsdocumenten

## [2026-06-18] analyse | Van data-inventarisatie naar bedrijfsarchitectuur
- Nieuwe analyse: GGM-oorsprong (bottom-up MI), oprekking naar transactioneel, consequenties voor GEMMA
- GEMMA-bronnen geraadpleegd: Bedrijfsobjecten, Procesarchitectuur kennismodel, Bedrijfsfuncties, GEMMA en het GGM
- Kernbevinding: GEMMA leidt bedrijfsobjecten af uit GGM → bottom-up beperking werkt door in referentiearchitectuur
- GEMMA heeft 507 bedrijfsobjecten, alle GGM-afgeleid — procesobjecten en governance-objecten ontbreken structureel
- Meerwaarde: aanvulling met procesobjecten/governance-objecten maakt GEMMA-procesarchitectuur concreter en transactioneel toepasbaar
- Opbouwend geformuleerd: bevestigt waarde GGM, toont complementaire aanvulling

## [2026-06-18] conventie | Begripstype voorspelt GGM-match + BO-grondslag
- CLAUDE.md aangepast: begripstype is primaire voorspeller voor GGM-match, niet abstractieniveau
- Tabel toegevoegd: begripstype → verwachte GGM-match (object=vaak, instrument/actor/thema=zelden/nooit)
- Bedrijfsobject-frontmatter uitgebreid met `grondslag` veld: ggm-entiteit, ggm-afgeleid, procesobject, governance-object
- Afleidingsregels aangepast: eerst grondslag bepalen, dan pas afleiden
- Alle 19 bestaande BO's bijgewerkt met `grondslag: ggm-entiteit`
- Aanleiding: structureel patroon uit [[ggm-dekkingspatroon]] — GGM dekt data, niet processen/governance

## [2026-06-18] analyse | GGM-dekkingspatroon
- Nieuwe analyse: structureel patroon over vier domeinen (Belastingen, Financiën, Economie, Bedrijfsvoering)
- Kernbevinding: GGM dekt data-objecten (basisregistraties, boekhoudkundig) maar niet processen, governance of beleidsinstrumenten
- Grens loopt niet tussen abstractieniveaus maar tussen data (staat van systemen) en dynamiek (gedrag van de organisatie)
- Consequentie: bedrijfsarchitectuur moet procesmodellen, governance en actoren zelf opbouwen uit beleidsbronnen
- Verwachting: patroon zal zich herhalen bij nieuwe domeinen (Schuldhulpverlening, Cultuur, Dienstverlening)

## [2026-06-18] bedrijfsobjecten | WOZ-object en WOZ-waarde
- 2 bedrijfsobjecten aangemaakt in Wiki/Bedrijfsobjecten/Belastingen/
- WOZ-object: 1:1 match met GGM WOZ-object (RSGBPlus, taakveld 99 Kern)
- WOZ-waarde: 1:1 match met GGM WOZ-Waarde (RSGBPlus); omvat beschikkingsaspect (statusBeschikking)
- WOZ-beschikking niet als apart BO: in GGM attribuut van WOZ-Waarde, op bedrijfsniveau niet onderscheidbaar
- Begrippen woz-waarde en onroerende-zaak bijgewerkt met GGM-referenties

## [2026-06-18] analyse | GGM-hiaten uitgebreid met Financiën-domein
- Hiatenanalyse uitgebreid met 10 Financiën-begrippen zonder GGM-match
- Structureel patroon geïdentificeerd: GGM dekt objecten (boekhoudkundig, basisregistratie) maar niet processen (begrotingscyclus, heffingsproces) of governance (verordeningen, budgetrecht)
- Kengetallen (solvabiliteit, schuldquote, belastingcapaciteit) zijn afleidbaar uit bestaande GGM-objecten, niet als entiteiten nodig
- WOZ-bedrijfsobjecten bevestigen: basisregistratie-kant goed gedekt, heffingsketen ontbreekt

## [2026-06-18] batch-verwerking | 10 clippings (8 verwerkt, 2 overgeslagen)
- Verwerkt: 3 Belastingen, 4 Financiën, 1 Bedrijfsvoering
- Overgeslagen: Raadgever Riool- en waterzorgheffing (duplicaat), Over de adviescommissies en colleges (buiten gemeentelijk perspectief)
- Totaal aangemaakt: 19 begrippen, 8 bronsamenvattingen, 2 domeinoverzichten
- Twee nieuwe domeinen: Financiën, Bedrijfsvoering

## [2026-06-17] setup | GGM als bronmateriaal geladen
- Bron: Sources/Gemeentelijk Gegevensmodel XMI2.1.xml
- GGM-bronpagina's aangemaakt in Sources/GGM/: structuur-ggm, financien (24 entiteiten), terug-en-invordering (29), sport-cultuur-en-recreatie (83), schulden (33)
- Alle definities letterlijk uit het GGM v2.5.1 XMI-bestand, geen synthese
- GGM-pagina's zijn bronmateriaal (Sources), geen wiki-pagina's

## [2026-06-17] analyse | GGM-hiaten belastingendomein
- Overzicht aangemaakt van ontbrekende concepten in het GGM voor het belastingendomein
- 6 begrippen zonder GGM-entiteit, 6 kandidaat-entiteiten geïdentificeerd
- Structureel hiaat beschreven: heffingsproces valt tussen RSGB, Financien en Terug- en invordering
- Status: in opbouw, wordt aangevuld bij verwerking volgende bronnen

## [2026-06-17] ingest | Belastingtypen
- Bron: Sources/Onderwerpen VNG/Belastingen/Belastingtypen.md
- Begrippen geëxtraheerd: gemeentelijke belasting, algemene belasting, bestemmingsbelasting, retributie, leges, algemene middelen
- Pagina's aangemaakt: 6 begrippen, 1 bronsamenvatting, 1 domeinoverzicht
- Hiaat gesignaleerd: GGM kent geen belastingtypologie als entiteiten of enumeratie

## [2026-06-17] bedrijfsobjecten | eerste set uit GGM
- 17 bedrijfsobjecten aangemaakt, afgeleid van GGM-entiteiten
- Financien (10): Begroting, Taakveld, Doelstelling, Product, Kostenplaats, Factuur, Inkooporder, Debiteur, Activa, Werkorder
- Terug-en-invordering (7): Vordering, Aflossingsplan, Aflossing, Kwijtschelding, Afschrijving, Restitutie, Interventie
- Debiteur combineert twee GGM-definities (Financien + T&I) in één bedrijfsobject
- Kwijtschelding noteert contextverschil: GGM = sociaal domein, belastingdomein = Invorderingswet
- 36 GGM-entiteiten uitgesloten: te granulair (Begrotingregel, Vorderingscomponent, etc.), te technisch (Batch, Batchregel), of specialisaties (Boetevordering, Rentevordering, etc.)
- Format per bedrijfsobject: naam, definitie (= GGM, afwijkend indien nodig), beleidsdomein, bedrijfsprocessen, bedrijfsfuncties

## [2026-06-17] ingest | 7 bronnen belastingendomein
- Bronnen: Belastinggebied, Belastingpolitiek, Belastingverordening, Bevoegdhedenverdeling, Invordering en kwijtschelding, Kostendekkende tarieven, Wettelijke grenzen
- Begrippen geëxtraheerd: belastinggebied, belastingverordening, belastingplichtige, heffingsambtenaar, invorderingsambtenaar, belastingmix, belastingaanslag, heffingsmaatstaf, kostendekkend tarief, kwijtschelding, woonlasten
- Pagina's aangemaakt: 11 begrippen, 7 bronsamenvattingen
- Pagina's bijgewerkt: gemeentelijke-belasting, bestemmingsbelasting, retributie, domeinoverzicht belastingen
- GGM-hiatenanalyse uitgebreid: 17 begrippen zonder (volledige) GGM-entiteit, procesmodel gereconstrueerd, overlap met Terug-en-invordering geanalyseerd
- Enige GGM-match: kwijtschelding → GGM "Kwijtschelding" (Terug-en-invordering), maar in context sociaal domein

## [2026-06-17] analyse | VNG-rubrieken mapping op GGM
- Alle 26 VNG-rubrieken (vng.nl/rubrieken) opgehaald met beschrijvingen en onderwerpen
- Mapping aangemaakt naar GGM-taakvelden (0-10, 99) en beleidsdomeinen
- Dekking: 14 rubrieken goed gedekt, 7 deels gedekt, 4 met hiaat, 1 zonder dekking
- Belangrijkste hiaten: Belastingen, Energietransitie, Openbare gezondheid, Recht, Risicobeheer
- Europa en internationaal valt geheel buiten GGM-scope
- Observatie: sociaal domein het breedst vertegenwoordigd (5 rubrieken → 13 beleidsdomeinen); taakveld 7 het smalst (alleen Afval)

## [2026-06-17] setup | GGM taakveld 3 Economie als bronmateriaal
- GGM-bronpagina aangemaakt: Sources/GGM/economie.md
- 6 entiteiten zonder definities: Contact, Hotel, Hotelbezoek, Verkooppunt, Werkgelegenheid, Winkelvloeroppervlak
- Observatie: zeer smal model, gericht op hotel/retail-statistieken rond Vestiging (RSGB)
- Groot hiaat t.o.v. breedte taakveld-definitie ("economische ontwikkeling, bedrijvigheid en innovatie")

## [2026-06-17] conventie | Begripstypen en abstractieniveaus
- CLAUDE.md uitgebreid met twee nieuwe dimensies voor begrippen: begripstype en abstractieniveau
- Begripstypen: waarde, doel, thema, instrument, actor, doelgroep, object
- Abstractieniveaus: normatief, strategisch, tactisch, operationeel
- Aanleiding: VNG-beleidsdocumenten spreken fundamenteel andere taal dan GGM — onderscheid moet structureel zichtbaar zijn
- Frontmatter begrippenpagina's uitgebreid met velden begripstype en abstractieniveau

## [2026-06-17] ingest | Economie speerpunten VNG
- Bron: Sources/Onderwerpen VNG/Economie/Economie speerpunten VNG.md
- Begrippen geëxtraheerd (9): brede welvaart (waarde/normatief), vestigingsklimaat (doel/strategisch), ondernemersdienstverlening (thema/tactisch), regeldruk (thema/tactisch), economische ruimte (thema/tactisch), arbeidsmarkt (thema/strategisch), human capital (thema/strategisch), midden- en kleinbedrijf (doelgroep/tactisch), werklocatie (object/operationeel)
- Pagina's aangemaakt: 9 begrippen, 1 bronsamenvatting, 1 domeinoverzicht
- GGM-matching: 0 directe matches, 3 gedeeltelijke (Werkgelegenheid, Winkelvloeroppervlak, Vestiging RSGB)
- Groot hiaat: GGM taakveld 3 dekt slechts statistisch fragment van het beleidsveld

## [2026-06-17] revisie | GGM-hiaten belastingendomein
- Hiatenanalyse herzien met begripstype/abstractieniveau-indeling
- Begrippen gegroepeerd per niveau: 1 strategisch, 9 tactisch, 7 operationeel
- Kernpunt: operationeel hiaat (heffingsproces) is het eigenlijke probleem; dat strategische begrippen geen GGM-match hebben is logisch
- Kandidaat-entiteiten getypeerd naar begripstype (object, doelgroep, actor)
- Onderscheid aangebracht tussen GGM-kandidaten (operationeel) en architectuurkader (tactisch)

## [2026-06-17] ingest | Inburgering en Asielopvang — 2 bronnen
- Bronnen: Asielopvangwijzer (COA portaal), COA Dienstverleningsgids (januari 2026)
- Begrippen geëxtraheerd (11): asielopvang, opvanglocatie, spreidingswet, duurzame gemeentelijke opvang, bestuursovereenkomst, statushouder, alleenstaande minderjarige vreemdeling, inburgering, voorinburgering, meedoenbalie, kansrijke koppeling, inhuisregistratie
- Pagina's aangemaakt: 11 begrippen, 2 bronsamenvattingen, 1 domeinoverzicht
- Scope: gemeentelijk perspectief — wat de gemeente ziet en doet in de asielketen
- COA/IND/DT&V/AVIM benoemd als ketenpartners, niet als eigen begrip uitgewerkt
- GGM-referentie: beleidsdomein Inburgering (35 entiteiten, taakveld 6) beschikbaar maar nog niet gemapped
- GGM-hiaat: asielopvangfase is niet gemodelleerd in het GGM
- Handreiking effectrapportage bij nieuwe bedrijvigheid verplaatst van Sources/Inburgering naar Sources/Economie (betreft arbeidsmigranten, niet inburgering)
- Conventie toegevoegd aan CLAUDE.md: gemeentelijk perspectief als scope voor alle compilaties
