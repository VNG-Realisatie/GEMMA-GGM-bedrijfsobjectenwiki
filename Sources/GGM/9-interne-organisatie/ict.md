---
type: ggm-beleidsdomein
naam: ICT
definitie: "Het informatiesubdomein dat gegevens omvat over de informatietechnologie en communicatiesystemen die de interne processen en informatievoorziening van een organisatie ondersteunen."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 36
---

# GGM Beleidsdomein: ICT

Beleidsdomein binnen taakveld "9 Interne Organisatie" (zie ../structuur-ggm.md).

## Entiteiten

### Basismodel CMDB-Items

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Applicatie** | Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers. | naam, categorie, beheerstatus, packagingstatus, applicatieURL, guid, omschrijving, beleidsdomein | Nee | GGM |
| **CMDB-item ** | Item in een Configuratie Management DataBase | naam, beschrijving | Nee | GGM |
| **Database** | Een applicatiecomponent die een dataset bevat. | databaseInstantie, omschrijving, DBMS, architectuur, OTAP, databaseVersie, vlan | Nee | GGM |
| **Koppeling** | Verbinding tussen twee systemen | direct, beschrijving, toelichting | Nee | GGM |
| **Linkbaar CMDB-item** | Niet opnemen | *(geen attributen)* | Nee | GGM |
| **Log** | Registratie van gegevens. | tijd, korteOmschrijving, omschrijving | Nee | GGM |
| **Notitie** | Korte, zakelijke uiteenzetting op schrift | datum, inhoud | Nee | GGM |
| **Package** | Een samengesteld bestand of een directory die een aantal bestanden bevat, maar welke als één bestand aan de gebruiker getoond word | naam, status, proces, project, toelichting | Nee | GGM |
| **Server** | Computer die in een netwerk een ondersteunende taak vervult. | serverID, organisatie, servertype, IPAdres, vlan, serienummer, locatie, actief | Nee | GGM |
| **Versie** | De versie-aanduiding van een object. | versienummer, status, datumEindeSupport, licentie, aantal, kosten | Nee | GGM |

### Basismodel ICT Applicatie en Gegevens

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Attribuutsoort** | Attribuutsoort – Stereotype «Attribuutsoort»: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass). Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in §2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype «Attribuutsoort». Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip ‘gegeven’. | naam, herkomst, definitie, herkomstDefinitie, datumOpname, domein, lengte, patroon, toelichting, indicatieMaterieleHistorie, kardinaliteit, authentiek, indicatieAfleidbaar, mogelijkGeenWaarde, identificerend, id, stereotype, precisie, ea_guid | Nee | GGM |
| **Classificatie** | Ordening van informatieobjecten in een logisch verband, zoals vastgelegd in een classificatieschema. | bevatPersoonsgegevens, gerelateerdPersoonsgegevens | Nee | GGM |
| **Datatype** | Attribuutsoort – Stereotype «Attribuutsoort»: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass). Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in §2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype «Attribuutsoort». Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip ‘gegeven’. | naam, herkomst, definitie, datumOpname, domein, lengte, patroon, toelichting, id, ea_guid, kardinaliteit | Nee | GGM |
| **Externe Bron** | Bron buiten de eigen organisatie | guid, naam | Nee | GGM |
| **Gegeven** | bekend feit waaruit je gevolgtrekkingen kunt maken | id, naam, alias, toelichting, stereotype, ea_guid | Nee | GGM |
| **Generalisatie** | De typering van het hiërarchische verband tussen een meer generiek object van een objecttype en een meer specifiek object van een ander objecttype waarbij het laatstgenoemde object eigenschappen van het eerstgenoemde object overerft. Toelichting Een generalisatierelatie geeft aan dat bepaalde eigenschappen van een objecttype (vaak attribuutsoorten en/of relatiesoorten) ook gelden voor de gerelateerde objecttypen, én dat deze qua semantiek, structuur en syntax gelijk zijn. We spreken dan van een supertype met subtypen. De modelelementen die generiek gelden worden in een generiek objecttype, het supertype, gemodelleerd en deze worden overerft door elk subtype (minimaal twee) die de generalisatie relatie legt naar dit generieke objecttype. Voorbeeld: PERCEEL is specialisatie van KADASTRAAL ONROERENDE ZAAK, APPARTEMENTSRECHT is specialisatie van KADASTRAAL ONROERENDE ZAAK. PERCEEL en APPARTEMENTSRECHT hebben beide ‘Kadastrale aanduiding’ en een ‘relatie met ONROERENDE ZAAK FILIATIE’. | naam, herkomst, definitie, herkomstDefinitie, datumOpname, id, ea_guid, toelichting, indicatieMaterieleHistorie | Nee | GGM |
| **MIMDomein** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Objecttype** | De typering van een groep objecten (in de werkelijkheid) die binnen een domein relevant zijn en als gelijksoortig worden beschouwd. Toelichting Jan, Piet en Marie zijn mensen die vanuit het Burgerzaken-domein beschouwd worden als objecten van het type ‘natuurlijk persoon’. In een ander domein, ‘de volksmond’, noemen we dit ‘mens’ wat ook een objecttype is. In weer een ander domein is Jan van het type ‘vergunninghouder’ en Piet en Marie niet, omdat aan hen (nog) nooit een vergunning verleend is. Objecttypen zijn een abstractie van de werkelijkheid oftewel we beogen hiermee de werkelijkheid zo getrouw mogelijk te beschrijven, binnen de context van het domein. Dit staat geheel los van het vastleggen van gegevens over objecten van een type in een registratie. Daartoe is veelal een interpretatie nodig (van die werkelijkheid cq. die objecttypen) naar eenheden die in een registratie vastgelegd kunnen worden (records, entiteiten e.d.) op basis van andere overwegingen. | naam, herkomst, definitie, herkomstDefinitie, datumOpname, uniekeAanduiding, populatie, kwaliteit, toelichting, indicatieAbstract, id, stereotype, ea_guid | Nee | GGM |
| **Relatiesoort** | De typering van het structurele verband tussen een object van een objecttype en een (ander) object van een ander (of hetzelfde) objecttype. Toelichting Objecten hebben eigenschappen die gemodelleerd kunnen worden met attribuutsoorten maar ook met relatiesoorten naar andere objecttypen. Als het voor het desbetreffende domein van belang is om die eigenschap te modelleren als onderdeel van een ander objecttype, dan maakt de relatiesoort die eigenschap beschikbaar voor het eerstgenoemde objecttype. Bijvoorbeeld, een attribuutsoort van het objecttype PERSOON zou kunnen zijn ‘Naam geregistreerd partner’ (naast de attribuutsoort ‘Naam’ van PERSOON). De naam van de geregistreerde partner komt evenwel ook beschikbaar met een relatiesoort van PERSOON naar PERSOON: “heeft geregistreerd partnerschap met”. Zie ook het eerder genoemde voorbeeld van SCHIP en MOTOR. Voorbeeld: relatiesoorten “VERBLIJFSOBJECT is gelegen in een PAND” en “SUBJECT heeft als correspondentieadres WOONPLAATS”, of korter, “gelegen in”, “postadres”. Wanneer een relatie (UML-assocation) gebruikt wordt om objecten aan elkaar te verbinden, zonder dat er eigenschappen over deze relatie worden vastgelegd, dan heeft deze het stereotype «Relatiesoort». | naam, herkomst, definitie, herkomstDefinitie, datumOpname, toelichting, indicatieMaterieleHistorie, kardinaliteit, authentiek, unidirectioneel, id, indicatieAfleidbaar, ea_guid, mogelijkGeenWaarde | Nee | GGM |

### Basismodel CMDB-Items Diversen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Hardware** | Alle fysieke componenten of onderdelen die in een computer een rol spelen. | *(geen attributen)* | Nee | GGM |
| **Inventaris** | Een inboedel of een opsomming van voorwerpen op een bepaalde plaats, gemaakt volgens een vaste procedure. | *(geen attributen)* | Nee | GGM |
| **Licentie** | Een gebruiksrecht en autorisatie om van een product of dienst gebruik te maken binnen bepaalde voorwaarden | *(geen attributen)* | Nee | GGM |
| **Nertwerkcomponent** | Een *netwerkcomponent* is een hardware- of softwareonderdeel dat een **specifieke functie vervult binnen een netwerk** om communicatie, gegevensuitwisseling of het beheer van netwerkverkeer mogelijk te maken. | *(geen attributen)* | Nee | GGM |
| **Software** | Een geheel van computerprogramma's met bijbehorende data, die bewerkingen en taken uitvoeren | *(geen attributen)* | Nee | GGM |
| **Toegangsmiddel** | Een middel waarmee men zich toegang tot iets kan verschaffen. | *(geen attributen)* | Nee | GGM |
| **Vervoersmiddel** | Een voertuig dat zich over het land verplaatst. | *(geen attributen)* | Nee | GGM |

### Diagram Domeinen, PDC en zaken

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Dienst** | Het uitvoeren van werkzaamheden met een continu of periodiek karakter om waarde te realiseren voor een afnemer. | *(geen attributen)* | Nee | GGM |
| **Domein/Taakveld** | Kennisgebied of activiteit gekarakteriseerd door een verzameling van concepten, begrippen en/of waarden | *(geen attributen)* | Nee | GGM |
| **Onderwerp** | Op de meest karakteristieke elementen gebaseerde en in woord of eenvoudige zinstructuur samengevatte aanduiding van de inhoud van een document | *(geen attributen)* | Nee | GGM |
| **Prijzenboek** | Beschrijving van gangbare onderhoudsactiviteiten met de bijbehorende, actuele prijzen en normen voor de uitvoering. | *(geen attributen)* | Nee | GGM |
| **Product** | Het resultaat van een proces dat in het economisch verkeer een waarde bezit. | *(geen attributen)* | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanvraag** | (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht. | *(geen attributen)* | Nee | GGM |
| **Melding** | De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend | *(geen attributen)* | Nee | GGM |
| **Storing** | Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren. | *(geen attributen)* | Nee | GGM |
| **Telefoniegegevens** | Gegevens die worden bewaard van telefoongesprekken | *(geen attributen)* | Nee | GGM |
| **Wijzigingsverzoek** | Een aanvraag voor wijziging | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
CMDB-item  (abstract)
    └── Hardware
    └── Inventaris
    └── Licentie
    └── Linkbaar CMDB-item
    └── Nertwerkcomponent
    └── Software
    └── Toegangsmiddel
    └── Vervoersmiddel
```

```
Linkbaar CMDB-item (abstract)
    └── Applicatie
    └── Database
    └── Server
```

## Relatiediagrammen

### Basismodel CMDB-Items

```
Applicatie [1] ──── Batch [0..*] (heeft herkomst)
Applicatie [0..*] ──── Document [0..*] (heeft documenten)
Applicatie [0..1] ──── Gegeven [0..*] (bevat)
Applicatie [0..*] ──── Leverancier [0..1] (heeft leverancier)
Applicatie [0..*] ──── Medewerker [0..*] (rollen)
Applicatie [1] ──── Notitie [0..*] (heeft notities)
Applicatie [1] ──── Package [0..*] (heeft packages)
Applicatie [1] ──── Versie [1..*] (heeft versies)
CMDB-item  [1] ──── Log [0..*] (heeft changelog)
Database [0..*] ──── Server [1] (server van database)
Koppeling [0..*] ──── Linkbaar CMDB-item [1] (link naar)
Linkbaar CMDB-item [1] ──── Koppeling [0..*] (link van)
Notitie [0..*] ──── Medewerker [1] (auteur)
Server [0..*] ──── Leverancier [0..1] (heeft leverancier)
```

### Basismodel ICT Applicatie en Gegevens

```
Applicatie [0..1] ──── Gegeven [0..*] (bevat)
Attribuutsoort [0..*] ──── Datatype [0..1] (heeft)
Externe Bron [0..1] ──── Gegeven [0..*] (levert)
Gegeven [0..*] ──── Classificatie [0..*] (geclassificeerd als)
Gegeven [0..*] ──── Objecttype [0..1] (gedefinieerd door)
Objecttype [0..1] ──── Attribuutsoort [0..*] (bezit)
Objecttype [1] ──── Generalisatie [0..1]
Objecttype [1] ──── Relatiesoort [0..*] (bezit)
Relatiesoort [0..*] ──── Objecttype [1] (gerelateerdObjecttype)
```

### Diagram Domeinen, PDC en zaken

```
Dienst [0..*] ──── Domein/Taakveld [1] (valt binnen)
Dienst [0..*] ──── Onderwerp [1] (heeft)
Dienst [0..*] ──── Product [0..1] (betreft)
Dienst [0..*] ──── Zaaktype [0..1] (start)
Domein/Taakveld [1] ──── Onderwerp [0..*] (valt binnen)
Domein/Taakveld [1] ──── Product [0..*] (valt binnen)
Prijzenboek [0..*] ──── Product [0..*] (heeft prijs)
Product [0..1] ──── Zaaktype [0..*] (betreft)
```

## Observaties

- Dit beleidsdomein bevat 36 entiteiten.
- Entiteiten zijn gegroepeerd in 5 diagramgroepen: Basismodel CMDB-Items (10), Basismodel ICT Applicatie en Gegevens (9), Basismodel CMDB-Items Diversen (7), Diagram Domeinen, PDC en zaken (5), Overig (5).
- Er zijn 11 generalisatierelaties aanwezig.
