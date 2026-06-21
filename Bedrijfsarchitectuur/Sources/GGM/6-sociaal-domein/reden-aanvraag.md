---
type: ggm-beleidsdomein
naam: Reden aanvraag
definitie: "Het onderdeel Reden aanvraag richt zich op de registratie en categorisatie van redenen waarom een cli&#235;nt een inkomensvoorziening aanvraagt. Dit model biedt een overzicht van de verschillende soorten redenen en hun onderlinge relaties, waardoor gemeenten deze informatie gestructureerd kunnen vastleggen en verwerken."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 22
---

# GGM Beleidsdomein: Reden aanvraag

Onderdeel van beleidsdomein **Inkomen** binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

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
| **Reden aanvraag** | Reden waarom dienst wordt aanvraagd bij gemeente. | Diensttype, Gewenste ingangsdatum | Nee | GGM |
| **Reden aanvraag Levensonderhoud** | *Reden aanvraag Levensonderhoud* is een categorie binnen het GBI-Ontologiemodel die aangeeft dat een cliënt een inkomensdienst aanvraagt vanwege een situatie waarin **middelen voor levensonderhoud ontbreken of zijn weggevallen**, en deze aanleiding geeft voor ondersteuning. | Onvoldoende inkomen, Reden, Verblijfstatus, Wijziging gezin, Zelfstandige | Nee | GGM |
| **Reden afwijkende startdatum** | *Reden afwijkende startdatum* is een categorie binnen het GBI-Ontologiemodel die aangeeft **waarom de ingangsdatum van een dienst of uitkering afwijkt van de standaard startdatum** (bijv. de datum van eerste melding). | Reden afwijking aanwezig, Reden Niet Eerder Aanvragen, RedenAfwijkendeStartdatumType | Nee | GGM |
| **Verbroken relatie** | *Verbroken relatie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt doordat **de (huwelijkse/samenlevings)relatie is beëindigd**, met financiële gevolgen voor het levensonderhoud. | Afspraak onderhoudsbijdrage gemaakt, Datum relatie verbroken, Geregistreerde partner, Opgave financiële ondersteuning | Nee | GGM |
| **Vertrek uit asielzoekerscentrum** | *Vertrek uit asielzoekerscentrum* is een subtype van **Reden aanvraag** in het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **recentelijk een asielzoekerscentrum heeft verlaten**, waardoor de financiële situatie is veranderd. | Bedrag weekgeld COA, Einddatum weekgeld COA, Ingangsdatum huurcontract, Weekgeld COA, Weekgeld COA stopt | Nee | GGM |
| **Wachten DigiD** | *Wachten DigiD* is een subtype van **Reden afwijkende startdatum** binnen het GBI-Ontologiemodel dat aangeeft dat de ingangsdatum van een inkomensdienst **vertraging oploopt doordat een DigiD nog niet is aangevraagd, geactiveerd of bruikbaar is**. | Aanvraagdatum DigiD | Nee | GGM |
| **Wachten beslissing instantie** | *Wachten beslissing instantie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **moet wachten op een besluit van een externe instantie**, waardoor de startdatum van de dienst afwijkt van de standaardprocedure. | Ontvangstdatum beslissing instantie | Nee | GGM |

## Overervingshiërarchie

```
Diensten::Aanvraag (abstract)
    └── Diensten::Aanvraag levensonderhoud
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

## Relatiediagrammen

```
Levenssituatie::Levenssituatie [0..1] ──── Reden aanvraag [0..*] (Is reden tot)
Profiel [1] ──── Reden aanvraag [0..1] (bevat)
```

## Observaties

- Dit beleidsdomein bevat 22 entiteiten.
- Er zijn 17 generalisatierelaties aanwezig.
