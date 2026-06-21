---
type: ggm-beleidsdomein
naam: Omgevingswet
definitie: "Het informatiedomein dat gegevens omvat over de uitvoering van de Omgevingswet, gericht op het integraal beheren en ontwikkelen van de fysieke leefomgeving."
taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
aantal_entiteiten: 31
---

# GGM Beleidsdomein: Omgevingswet

Beleidsdomein binnen taakveld "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing" (zie ../structuur-ggm.md).

## Entiteiten

### Omgevingswet Verzoeken (IMAM)

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bevoegd Gezag** | Bestuursorgaan dat bevoegd is tot het geven van een beschikking of het nemen van een ander besluit. | *(geen attributen)* | Nee | GGM |
| **Gemachtigde** | Een Natuurlijk Persoon of een Niet Natuurlijk Persoon die als vertegenwoordiger van een Initiatiefnemer optreedt. | *(geen attributen)* | Nee | GGM |
| **Initiatiefnemer** | Een Natuurlijk Persoon of een Niet Natuurlijk Persoon die het initiatief neemt tot (fysieke) ingrepen in de (leef)omgeving en daartoe een Verzoek bij het Bevoegd Gezag indient. | *(geen attributen)* | Nee | GGM |
| **Project** | Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat. | naam, omschrijving | Nee | GGM |
| **Projectlocatie** | Fysieke locatie waar een project betrekking op heeft of wordt uitgevoerd. | adres, kadastraalPerceel, kadastraleGemeente, kadastraleSectie | Nee | GGM |
| **Specificatie** | Gesplitste opgave, vermelding van de afzonderlijke onderdelen waaruit een verzameling of een totaal bestaat | antwoord, groepering, publiceerbaar, vraagID, vraagClassificatie, vraagreferentie, vraagtekst | Nee | GGM |
| **Uitvoerende instantie** | Onderdeel van het bevoegd gezag dat uitvoering geeft aan wetten en besluiten | naam | Nee | GGM |
| **Verzoek** | Een vraag aan het bevoegd gezag om een speficieke product of dienst te leveren. | akkoordverklaring, ambtshalve, doel, datumIndiening, naam, referentieAanvrager, toelichtingLaterAanTeLeverenInformatie, toelichtingNietAanTeLeverenInformatie, toelichtingVerzoek, type, verzoeknummer, volgnummer | Nee | GGM |

### Omgevingswet Verzoek met Project (IMAM)

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Projectactiviteit** | Activiteit binnen het project | *(geen attributen)* | Nee | GGM |

### Omgevingswet Omgevingsplan StOP TPOD

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Juridische Regel** | De beschrijving van een regel met juridische werkingskracht. Een regel betreft binnen de Omgevingswet veelal activiteiten, en/of normen en/of functies en/of beperkingengebieden. | omschrijving, thema, regeltekst, datumStart, datumEindeGeldigheid, datumInWerking, datumBekend | Nee | GGM |
| **Omgevingsdocument** | In artikel 16.2 van de Omgevingswet aangemerkt instrument te weten: Omgevingsvisie, programma, omgevingsplan, waterschapsverordening, omgevingsverordening, projectbesluit of bij Algemene Maatregel van Bestuur (Omgevingsbesluit) aangewezen ander besluit of ander rechtsfiguur. | *(geen attributen)* | Nee | GGM |
| **Regeltekst** | De kleinste zelfstandige eenheid van (een of meer) bij elkaar horende juridische regels: een artikel en lid. | tekst, identificatie, omschrijving | Nee | GGM |
| **Thema** | Kernachtige weergave van de grondgedachte achter een regel. | naam, omschrijving | Nee | GGM |

### Omgevingswet Toepasbare Regels

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Activiteit** | Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd. | naam, groep, NEN3610ID | Nee | GGM |
| **Conclusie** | Conclusie van de check. Antwoord op de vraag of ik een melding moet doen of een vergunning aan moet vragen voor een bepaalde activiteit. | *(geen attributen)* | Nee | GGM |
| **Indieningsvereisten** | Dat wat de initiatiefnemer moet aanleveren om het bevoegd gezag een aanvraag te kunnen laten beoordelen. De indieningsvereisten is de set aan informatie (gegevens en / of bijlagen) die aan een aanvraag moet worden toegevoegd voor een bepaalde vergunning of melding. | *(geen attributen)* | Nee | GGM |
| **Maatregelen** | Beschrijft welke handelingen iemand moet uitvoeren om aan Voorschriften te kunnen voldoen. | *(geen attributen)* | Nee | GGM |
| **Toepasbare Regel** | Vanwege de leesbaarheid wordt gewerkt met de term Toepasbare regel ipv regelbeheersobject Een regelbeheerobject heeft een koppeling met een samenhangende set met regels om een afleiding te kunnen doen. Het regelbeheerobject ‘conclusie gevelaanpassing’ kan een vraag beantwoorden zoals: “Heb ik een vergunning nodig voor het veranderen van een kozijn, kozijninvulling of gevelpaneel”. Het regelbeheerobject ‘melding lozing’ beantwoordt de vraag “Wat moet ik aan informatie (gegevens en documenten) aanleveren als ik ga lozen vanuit particuliere huishoudens”. Het regelbeheerobject “Opslaan van gasolie smeerolie of afgewerkte olie in een bovengrondse opslagtank” geeft aan welke maatregelen genomen dienen te worden. Het regelbeheerobject is onderdeel van de functionele structuur. De set met regels is gedefinieerd in het Toepasbare regelbestand2. | naam, omschrijving, domein, toestemming, soortAansluitpunt, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **ToepasbareRegelBestand** | Bestand met aangeleverde toepasbare regels | datumStart, datumEindeGeldigheid | Nee | GGM |
| **Uitvoeringsregel** | De uitvoeringsregels bepalen hoe de benodigde gegevens (input data) wordt uitgevraagd. Dit kan op verschillende manieren gebeuren zoals een vraag aan een initiatiefnemer of een bevraging van een registratie. | naam, omschrijving, regel | Nee | GGM |

### Omgevingswet Verzoek Activiteit op Locatie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Beperkingsgebied** | Een bij of krachtens de wet aangewezen gebied, waar vanwege de aanwezigheid van een werk of object regels gelden, ten aanzien van het beperken van activiteiten die gevolgen hebben of kunnen hebben voor dat werk of object. | naam, groep | Nee | GGM |
| **Functie** | Een samenhangende verzameling van rollen | naam, groep | Nee | GGM |
| **Gebiedsaanwijzing** | Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels. | NEN3610ID, groep, naam | Nee | GGM |

### Omgevingswet Juridsiche regels en Idealisatie en Thema (CIMOW)

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Idealisatie** | Vastlegging van de manier de begrenzing van Locatie voor deze Juridische regel ge&#239;nterpreteerd moet worden en door het bevoegd gezag bedoeld is. | naam, omschrijving | Nee | GGM |

### Omgevingswet Juridische Regels (CIMOW)

De objecttypen uit dit diagram zijn afgeleid van CIMOW v0.98-kern, zie https://www.geonovum.nl/over-geonovum/actueel/cimow-en-imow-versie-098-beta-beschikbaar Het Conceptueel Informatiemodel voor de Omgevingswet (CIMOW) beschrijft het domein van de Omgevingswet. Dit beperkt zich tot de informatie die in dit domein wordt vastgelegd en vastgesteld en in ketens wordt uitgewisseld ten behoeve van het digitaal stelsel van de Omgevingswet (DSO). CIMOW beschrijft sec de informatie. Hoe en waar deze informatie precies gebruikt wordt is geen onderdeel van dit informatiemodel. Anders gezegd, de informatie zoals beschreven in dit model mag overal waar dit nuttig is gebruikt en toegepast worden. In tekstvorm, in een document, in een keten, in processen, in een product of API, in een technisch formaat zoals XML of JSON et cetera. Het CIM is implementatieonafhankelijk en los van de techniek opgezet. Dit maakt het mogelijk om de informatie in verschillende ketens en in verschillende technieken met behoud van betekenis te implementeren. In de context van Omgevingswet zijn in de ketens uitwisselstandaarden aan de orde, te weten STOP, STTR en STAM. Bevoegde gezagen en het DSO gaan bij de Omgevingswet in de volle breedte integreren op basis van concepten als: regel, locatie, functie, activiteit, norm, et cetera, CIMOW speelt hierin een centrale rol bij de inrichting van de informatievoorziening, door het verbinden van verschillende disciplines, standaarden en systemen, met behulp van centrale informatie definities. Wat wel en wat niet? • CIMOW bevat minimaal alle Omgevingswet gerelateerde informatie die uitgewisseld wordt in de keten van plan tot publicatie (via het bronhouders koppelvlak van de LVBB); • CIMOW beschrijft niet het domein van offici&#235;le overheidspublicaties (OP) zelf. Concepten zoals artikel of een besluit zijn wel relevant voor het DSO, staan in CIMOP gedefinieerd en niet (nogmaals) in CIMOW. • In CIMOW is geen specificatie voor welke informatie wel of niet mag voorkomen, of juist moet voorkomen, in een bepaald type instrument (ook wel omgevingsdocument genoemd); • Als er sprake is van een koppelvlak met een uitwisselingsmodel waarin delen uit het domein van Offici&#235;le Publicaties (OP) en delen uit het Omgevingswet (OW) domein bij elkaar komen, dan kan hiervoor CIMOW gebruikt worden als bron, alsmede CIMOP (alsmede andere modellen van nog andere domeinen); • Niet binnen scope is informatie die primair de implementatie ondersteunt, zoals de informatie die nodig is voor weergave. Een symbool voor de weergave of een kleurcode voor de weergave op de kaart zit niet in het CIMOW. Wat wel in het CIMOW zit is de informatie die weergegeven wordt, zoals een functiegroep of een activiteitengroep.

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Instructieregel** | Objecttype Instructieregel Naam Definitie Toelichting Instructieregel De beschrijving van een juridische regel die een instructie is voor een extern omgevingsdocument of een orgaan. Het betreft hier juridische regel die instructie geeft aan andere overheden, gericht op externe omgevingsdocumenten, of een taakuitoefening. Een ander omgevingsdocument is bijvoorbeeld een Omgevingsplan, Omgevingsverordening en Waterschapsverordening. Een taakuitoefening is voor bijvoorbeeld een gemeentebestuur of een wildbeheereenheid. Een instructieregel is alleen gericht op een Omgevingsnorm of een Gebiedsaanduiding, zoals een Functie of een Beperkingengebied (en eventueel meerdere). | instructieregelInstrument, instructieregelTaakuitoefening | Nee | GGM |
| **Norm** | Omgevingswaarde of een omgevingsnorm, met een normatief karakter, die beschreven worden middels normwaarden. Een normwaarde kan kwalitatief of kwantitatief zijn. | NEN3610ID | Nee | GGM |
| **Normwaarde** | Een van de kwantitatieve of kwalitatieve waarden van een norm. De normwaarde geeft aan wat de specifieke kwantitatieve of kwalitatieve eisen zijn, inclusief de toewijzing ervan aan de specifieke locatie(s) waar de normwaarde voor geldt. | kwalitatieveWaarde, kwantitatieveWaardeOmvang, kwantitatieveWaardeEenheid | Nee | GGM |
| **Omgevingsnorm** | Een norm over de fysieke leefomgeving die in een kwantitatieve of kwalitatieve waarde wordt uitgedrukt en geen omgevingswaarde is. | naam, omgevingsnormGroep | Nee | GGM |
| **Omgevingswaarde** | Een norm die voor (een onderdeel van) de fysieke leefomgeving de gewenste staat of kwaliteit, de toelaatbare belasting door activiteiten en/of de toelaatbare concentratie of depositie van stoffen als beleidsdoel vastlegt. | naam, omgevingswaardeGroep | Nee | GGM |
| **Omgevingswaarderegel** | De beschrijving van een juridische regel gericht op een gestelde omgevingswaarde. Het betreft hier een juridische regel die verplichtingen oplegt aan het bevoegd gezag dat deze regel opstelt. Een omgevingswaarderegel is alleen gericht op een Omgevingswaarde (eventueel meerdere). | naam, groep | Nee | GGM |
| **Regel voor Iedereen** | Een Juridische regel die voor eenieder werking heeft | activiteitRegelKwalificatie | Nee | GGM |

## Overervingshiërarchie

```
Gebiedsaanwijzing (abstract)
    └── Beperkingsgebied
    └── Functie
```

```
Juridische Regel (abstract)
    └── Instructieregel
    └── Omgevingswaarderegel
    └── Regel voor Iedereen
```

```
Norm (abstract)
    └── Omgevingsnorm
    └── Omgevingswaarde
```

```
Rechtspersoon (abstract)
    └── Bevoegd Gezag
    └── Gemachtigde
    └── Initiatiefnemer
```

```
Toepasbare Regel (abstract)
    └── Conclusie
    └── Indieningsvereisten
    └── Maatregelen
```

## Relatiediagrammen

### Omgevingswet Verzoeken (IMAM)

```
Gemachtigde [0..1] ──── Verzoek [1..*] (dient in )
Initiatiefnemer [1] ──── Verzoek [1..*] (heeft als verantwoordelijke)
Medewerker [0..*] ──── Uitvoerende instantie [1] (werkt bij)
Project [1] ──── Projectactiviteit [0..*] (heeft)
Project [1] ──── Projectlocatie [0..*] (heeft)
Projectactiviteit [1..*] ──── Projectlocatie [1] (uitgevoerd op)
Projectlocatie [0..*] ──── Locatie [0..1] (betreft)
Specificatie [1..*] ──── Projectactiviteit [0..1] (gedefinieerd door)
Verzoek [0..*] ──── Activiteit [1..*] (betreft)
Verzoek [0..*] ──── Bevoegd Gezag [1] (verantwoordelijke)
Verzoek [0..*] ──── Locatie [1..*] (betreft)
Verzoek [1..*] ──── Project [1..] (betreft)
Verzoek [1..*] ──── Projectactiviteit [0..*] (betreft)
Verzoek [1] ──── Specificatie [0..*] (bevat)
Verzoek [0..*] ──── Uitvoerende instantie [0..1] (behandelaar)
Verzoek [0..1] ──── Verzoek [0..*] (betreft eerder verzoek)
Verzoek [0..1] ──── Zaak [0..1] (leidt tot)
Zaak [0..*] ──── Project [0..1] (betreft)
```

### Omgevingswet Verzoek met Project (IMAM)

```
Project [1] ──── Projectactiviteit [0..*] (heeft)
Projectactiviteit [1..*] ──── Projectlocatie [1] (uitgevoerd op)
Specificatie [1..*] ──── Projectactiviteit [0..1] (gedefinieerd door)
Verzoek [1..*] ──── Projectactiviteit [0..*] (betreft)
```

### Omgevingswet Omgevingsplan StOP TPOD

```
Juridische Regel [1..*] ──── Activiteit [1..*] (geldt voor)
Juridische Regel [0..*] ──── Idealisatie [0..*] (heeft idealisatie)
Juridische Regel [0..*] ──── Locatie [1..*] (werkingsgebied)
Juridische Regel [1..*] ──── Regeltekst [1] (is opgenomen in)
Juridische Regel [0..*] ──── Thema [0..*] (heeft thema)
Omgevingsdocument [1] ──── Regeltekst [1..*] (bevat)
Regeltekst [0..*] ──── Idealisatie [0..*] (heeft idealisatie)
Regeltekst [0..*] ──── Locatie [0..*] (werkingsgebied)
Regeltekst [0..1] ──── Regeltekst [0..*] (werkingsgebied)
Regeltekst [0..1] ──── Regeltekst [0..*] (is gerelateerd)
Regeltekst [0..*] ──── Thema [0..*] (heeft thema)
Thema [0..1] ──── Thema [0..*] (subthema)
Toepasbare Regel [0..*] ──── Juridische Regel [1..*] (komt voort uit)
```

### Omgevingswet Toepasbare Regels

```
Activiteit [1] ──── Activiteit [0..1] (gerelateerde activiteit)
Activiteit [1] ──── Activiteit [0..1] (bovenliggende activiteit)
Activiteit [0..*] ──── Locatie [1..*] (is verbonden met)
Juridische Regel [1..*] ──── Activiteit [1..*] (geldt voor)
Regel voor Iedereen [1..*] ──── Activiteit [0..*] (beschrijft activiteit)
Toepasbare Regel [0..*] ──── Activiteit [1] (betreft)
Toepasbare Regel [0..*] ──── Juridische Regel [1..*] (komt voort uit)
Toepasbare Regel [0..*] ──── Locatie [0..*] (betreft)
Toepasbare Regel [0..*] ──── ToepasbareRegelBestand [1] (heeft)
Toepasbare Regel [1] ──── Uitvoeringsregel [0..*] (heeft)
ToepasbareRegelBestand [1] ──── Uitvoeringsregel [0..*] (bevat)
Verzoek [0..*] ──── Activiteit [1..*] (betreft)
```

### Omgevingswet Verzoek Activiteit op Locatie

```
Gebiedsaanwijzing [0..*] ──── Locatie [1..*] (verwijst naar)
Instructieregel [0..*] ──── Gebiedsaanwijzing [0..*] (beschrijft gebiedsaanwijzing)
Regel voor Iedereen [0..*] ──── Gebiedsaanwijzing [0..*] (beschrijft gebiedsaanwijzing)
```

### Omgevingswet Juridsiche regels en Idealisatie en Thema (CIMOW)

```
Juridische Regel [0..*] ──── Idealisatie [0..*] (heeft idealisatie)
Regeltekst [0..*] ──── Idealisatie [0..*] (heeft idealisatie)
```

### Omgevingswet Juridische Regels (CIMOW)

```
Instructieregel [0..*] ──── Gebiedsaanwijzing [0..*] (beschrijft gebiedsaanwijzing)
Norm [1] ──── Normwaarde [1..*] (bevat)
Normwaarde [0..*] ──── Locatie [1..*] (geldt voor)
Omgevingswaarderegel [1..*] ──── Omgevingsnorm [0..*] (beschrijft)
Omgevingswaarderegel [1..*] ──── Omgevingswaarde [0..*] (beschrijft)
Regel voor Iedereen [1..*] ──── Activiteit [0..*] (beschrijft activiteit)
Regel voor Iedereen [0..*] ──── Gebiedsaanwijzing [0..*] (beschrijft gebiedsaanwijzing)
Regel voor Iedereen [0..*] ──── Omgevingsnorm [0..*] (beschrijft norm)
```

## Observaties

- Dit beleidsdomein bevat 31 entiteiten.
- Entiteiten zijn gegroepeerd in 7 diagramgroepen: Omgevingswet Verzoeken (IMAM) (8), Omgevingswet Verzoek met Project (IMAM) (1), Omgevingswet Omgevingsplan StOP TPOD (4), Omgevingswet Toepasbare Regels (7), Omgevingswet Verzoek Activiteit op Locatie (3), Omgevingswet Juridsiche regels en Idealisatie en Thema (CIMOW) (1), Omgevingswet Juridische Regels (CIMOW) (7).
- Er zijn 13 generalisatierelaties aanwezig.
