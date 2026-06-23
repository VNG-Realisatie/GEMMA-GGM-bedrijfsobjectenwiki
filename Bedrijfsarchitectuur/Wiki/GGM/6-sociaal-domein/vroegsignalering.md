---
type: ggm-beleidsdomein
naam: Vroegsignalering
definitie: "Beleidsdomein Vroegsignalering binnen taakveld Schulden."
taakveld: "Schulden"
aantal_entiteiten: 6
---

# GGM Beleidsdomein: Vroegsignalering

### Vroegsignalering

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Contactpoging** | Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen). | soort, bereikt, datum, dagdeel | Nee | GGM |
| **Signaalpartner** | Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders. Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering. | type | Nee | GGM |
| **Vroegsignaal** | Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden. De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs). Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden. | crisissignaal, warmeOverdracht, bedrag, ontstaansdatum, signaaldatum, status | Nee | GGM |
| **Vroegsignaalzaak** | Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van één of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning. | resultaat, matchingsdatum, startdatum_matchtingperiode, datum_opgepakt, einddatum_matchingperiode | Nee | GGM |

### Vroegsignalering Klein

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AanleverendeOrganisatie** | Organisatie de data aanlevert aan het CBS. Het kan hier gaan om de gemeente zelf, of een partij die namens de gemeente uitvoering geeft aan de afhandeling van vroegsignalen. | naam, kvk-nummer | Nee | GGM |
| **Contactpersoon** | Contactpersoon bij de aanleverende organisatie. | naam, telefoonnummer, email, functietitel | Nee | GGM |

## Overervingshiërarchie

```
Rechtspersoon (abstract)
    └── Signaalpartner
```

```
Zaak (abstract)
    └── Vroegsignaalzaak
```

## Relatiediagrammen

```
AanleverendeOrganisatie [1..1] ──── Contactpersoon [1..*] (contactpersonen)
Vroegsignaal [0..*] ──── Signaalpartner [1] (verzondenDoor)
Vroegsignaal [1..*] ──── Vroegsignaalzaak [0..1] (opgepaktIn)
Vroegsignaalzaak [1] ──── Contactpoging [0..*] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 6 Objecttype-entiteiten (+ 5 Enumeraties, 1 diagramhulpobjecten zonder stereotype).
- Entiteiten zijn gegroepeerd in 3 diagramgroepen: Vroegsignalering (4), Vroegsignalering Details (4), Vroegsignalering Klein (6).
- Er zijn 2 generalisatierelaties aanwezig.
