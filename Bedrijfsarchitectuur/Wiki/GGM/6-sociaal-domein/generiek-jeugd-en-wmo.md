---
type: ggm-beleidsdomein
naam: Generiek Jeugd en Wmo
definitie: "Alle generieke objecttypen die zowel voor de Wmo als voor uitvoering van de jeugdwet worden gebruikt"
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 27
---

# GGM Beleidsdomein: Generiek Jeugd en Wmo

### AanvraagOfMelding

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AOMMeldingWmoJeugd** | *AOMMeldingWMOJeugd* is een objecttype in het gemeentelijk gegevensmodel dat een **melding van een situatie of hulpvraag binnen het kader van de Wet maatschappelijke ondersteuning (Wmo) en/of Jeugdwet** representeert. | aanmelder, aanmeldingDoor, aanmeldingDoorLandelijk, aanmeldwijze, redenAfsluiting, isClientOpDeHoogte, deskundigheid, vervolg, onderzoekswijze, verwezen | Nee | GGM |
| **AOM_AanvraagWmoJeugd** | *AOM_AanvraagWmoJeugd* is een objecttype in het gegevensmodel voor Wmo en Jeugd dat een **aanvraagtraject voor ondersteuning onder de Wet maatschappelijke ondersteuning (Wmo) en/of Jeugdwet** representeert. | clientReactie, datumBeschikking, datumEersteAfspraak, datumPlanVastgesteld, datumStartAanvraag, datumEinde, deskundigheid, doorloopmethodiek, maximaleDoorlooptijd, redenAfsluiting | Nee | GGM |
| **Beschikking** | In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift. | datumAfgifte, code, grondslagen, commentaar, wet | Nee | GGM |

### Beperkingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Beperking** | Een stoornis of conditie ‚ lichamelijk, zintuiglijk en-of geestelijk ‚ die een normaal maatschappelijk functioneren belemmert en nadelige sociale gevolgen met zich meebrengt. | duur, categorie, commentaar, wet | Nee | GGM |
| **Beperkingscategorie** | Een categorisering van beperkingen | code, wet | Nee | GGM |
| **Beperkingscore** | Getalsmatige duiding van een beperking | score, commentaar, wet | Nee | GGM |
| **Beperkingscoresoort** | Typering van beperkingscores | vraag, wet | Nee | GGM |

### Relaties Sociaal Domein tot Kern

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Team** | Een groep personen die door middel van samenwerking een gezamenlijk doel nastreeft, waarbij de teamleden afhankelijk van elkaar zijn om het doel te bereiken. | naam, omschrijving | Nee | GGM |

### Sociaal Domein Beschikking en Voorziening: Domain Objects

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Beschikte Voorziening** | Een voorziening waarover een beschikking is gedaan. | omvang, eenheid, frequentie, wet, code, datumStart, datumEinde, leveringsvorm, status, redenEinde, datumEindeOorspronkelijk | Nee | GGM |
| **Budgetuitputting** | Overzicht van de te verwachte inkomsten en uitgaven over een bepaalde periode | datum, uitgenutBedrag | Nee | GGM |
| **Declaratie** | Een opgave van te vergoeden kosten. | declaratieBedrag, datumDeclaratie, declaratieStatus | Nee | GGM |
| **Declaratieregel** | Een *declaratieregel* is de **administratieve regel** waarin het **volume van één product of geleverde prestatie** binnen een bepaalde declaratieperiode voor één cliënt wordt vastgelegd. | code, bedrag, datumStart, datumEinde | Nee | GGM |
| **Levering** | Levering van zorg door leverancier. Is in het geval van resultaatverplichting steeds: 1 stuk In PxQ uren maal tarief | eenheid, frequentie, omvang, code, datumStart, datumStop, stopreden | Nee | GGM |
| **Leveringsvorm** | Zorg die onder de Wlz, de Zvw-Wijkverpleging of de Wmo 2015 valt, kan aan personen als zorg in natura (zin) worden geleverd of bekostigd worden uit een persoonsgebonden budget (pgb). | naam, wet, leveringsvormCode | Nee | GGM |
| **Melding Eigen bijdrage** | Aangifte van de evetuele eigen bijdrage | datumStart, datumStop | Nee | GGM |
| **PGB-Toekenning** | Betreft alleen toegekende voorzieningen met als leveringsvorm PGB Opgebouwd op basis van het TKB (Toekenninsgbericht) aan het SVB, en het BAB-bericht (budgetafsluiting). zie: https://istandaarden.nl/istandaarden/ipgb | datumToekenning, budget, datumEinde | Nee | GGM |
| **Tarief** | Hoogte van een bedrag voor een bepaald product of dient | datumStart, datumEinde, bedrag, wet, eenheid | Nee | GGM |
| **Toewijzing** | Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd. zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html | toewijzingnummer, datumToewijzing, datumStartToewijzing, datumEindeToewijzing, redenWijziging, omvang, commentaar, eenheid, frequentie, datumAanschaf, code, wet | Nee | GGM |
| **Verzoek om Toewijzing** | Verzoek tot toewijzing dat vanuit leverancier (via H10-portal) aan de gemeente wordt gestuurd. Zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html | referentieAanbieder, beschikkingsnummer, datumIngangBeschikking, datumIngangToewijzing, datumEindeToewijzing, volume, eenheid, frequentie, verwijzer, raamcontract, commentaar, datumOntvangst, soortVerwijzer | Nee | GGM |
| **Voorziening** | Middel om services/maatregelen in te vullen. | productcode, naam, omschrijving, wet, code, afhandelwijze | Nee | GGM |
| **Voorzieningsoort** | Typering van een voorziening | naam, omschrijving, wet, code, productcode, productcategoriecode, productcategorie | Nee | GGM |

### Sociale team:Domeinmodel

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Leefgebied** | Gebied waarin alle activiteiten van een inwoner zich kunnen afspelen | naam | Nee | GGM |
| **Score** | Het aantal behaalde punten | datum | Nee | GGM |
| **Scoresoort** | Typologie van score | niveau | Nee | GGM |
| **Zelfredzaamheidmatrix** | Een geordend systeem waarbij aan elf domeinen van het dagelijks leven (zoals inkomen en dagbesteding; zie figuur) een waarde voor zelfredzaamheid wordt toegekend. | naam, omschrijving, datumStartGeldigheid, datumEindeGeldigheid | Nee | GGM |

### Verplichtingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Verplichting Wmo Jeugd** | *Verplichting Wmo Jeugd* is de wettelijke plicht van gemeenten om inwoners ondersteuning, hulp of zorg te bieden wanneer zij dat nodig hebben op grond van de Wet maatschappelijke ondersteuning (Wmo) en de Jeugdwet. | budgetsoortgroep, Budgetsoort, Feitelijke Einddatum, verplichtingsoort, Periodiciteit, Einddatumgepland, Jaar | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Beschikkingsoort** | Typering van een beschikking | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
AanvraagOfMelding (abstract)
    └── AOMMeldingWmoJeugd
    └── AOM_AanvraagWmoJeugd
```

```
Inkooporder (abstract)
    └── Verplichting Wmo Jeugd
```

## Relatiediagrammen

```
AOM_AanvraagWmoJeugd [0..1] ──── Beschikking [0..*] (leidt_tot)
Beperking [0..*] ──── Beperkingscategorie [0..1] (is een)
Beperking [0..1] ──── Beperkingscore [0..*]
Beperking [0..*] ──── Beschikking [0..1] (is gebaseerd op)
Beperkingscore [0..*] ──── Beperkingscoresoort [0..1] (is een)
Beschikking [0..*] ──── AOMMeldingWmoJeugd [0..*] (betreft)
Beschikking [1..1] ──── Beschikte Voorziening [1..*] (heeft voorzieningen)
Beschikking [1] ──── Toewijzing [0..*] (toewijzing)
Beschikte Voorziening [0..*] ──── Leveringsvorm [1..1] (heeft)
Beschikte Voorziening [1..*] ──── Toewijzing [0..1] (Toegewezen Product)
Beschikte Voorziening [0..*] ──── Voorziening [1..1] (is voorziening)
Declaratieregel [0..*] ──── Beschikking [1..1] (is voor)
Declaratieregel [0..*] ──── Declaratie [1..1] (valt binnen)
Levering [0..*] ──── Beschikking [0..1] (geleverde prestatie)
Levering [0..*] ──── Toewijzing [0..1] (geleverde zorg)
Levering [0..*] ──── Voorziening [1] (voorziening)
Melding Eigen bijdrage [0..*] ──── Beschikking [1] (betreft)
PGB-Toekenning [0..*] ──── Beschikte Voorziening [1] (betreft)
PGB-Toekenning [1] ──── Budgetuitputting [0..*] (betreft)
Score [0..*] ──── Leefgebied [1..1] (score bij leeggebied)
Score [0..*] ──── Scoresoort [1..1] (hoogte score)
Toewijzing [1..1] ──── Declaratieregel [0..*] (is op basis van)
Verplichting Wmo Jeugd [1] ──── AOM_AanvraagWmoJeugd [0..1]
Verplichting Wmo Jeugd [1] ──── Beschikte Voorziening [0..1]
Verzoek om Toewijzing [0..*] ──── Beschikking [0..1] (leidt tot)
Verzoek om Toewijzing [0..*] ──── Voorziening [1] (betreft)
Voorziening [1..1] ──── Tarief [1..*] (heeft)
Voorziening [0..*] ──── Voorzieningsoort [1..1] (valt binnen)
Zelfredzaamheidmatrix [1..*] ──── Leefgebied [1..*] (onderkent leefgebiieden)
Zelfredzaamheidmatrix [1..*] ──── Scoresoort [1..*] (onderkent scores)
```

## Observaties

- Dit beleidsdomein bevat 27 Objecttype-entiteiten (+ 6 Enumeraties).
- Entiteiten zijn gegroepeerd in 6 diagramgroepen: AanvraagOfMelding (3), Beperkingen (5), Relaties Sociaal Domein tot Kern (1), Sociaal Domein Beschikking en Voorziening: Domain Objects (14), Sociale team:Domeinmodel (4), Verplichtingen (3).
- Er zijn 3 generalisatierelaties aanwezig.
