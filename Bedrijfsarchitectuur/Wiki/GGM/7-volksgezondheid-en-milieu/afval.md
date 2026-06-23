---
type: ggm-beleidsdomein
naam: Afval
definitie: "Het informatiedomein dat gegevens bevat over de gemeentelijke taken ten aanzien van inzameling en verwerking van bedrijfs- en huishoudelijk afval"
taakveld: "7 Volksgezondheid en Milieu"
aantal_entiteiten: 16
---

# GGM Beleidsdomein: Afval

Beleidsdomein binnen taakveld "7 Volksgezondheid en Milieu" (zie ../structuur-ggm.md).

## Entiteiten

### Diagram Afval Ophalen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Container** | Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen | sensorID, containercode | Nee | GGM |
| **Containertype** | Typologie van container | naam, omschrijving | Nee | GGM |
| **Fractie** | Onderdeel, deeltje | naam, omschrijving | Nee | GGM |
| **Locatie** | Locaties die worden aangedaan tijdens het rijden van een route. Dit kunnen adressen zijn en/of GML-punten met een x- en y-coordinaat. Avalex hanteert op het moment van schrijven alleen adressen, ook voor de containers. | locatiePunt, locatiecode, adresaanduiding | Nee | GGM |
| **Ophaalmoment** | Een stop die een vuilniswagen maakt tijdens het doen van een rit. Bijgehouden wordt de gewichtstoename van de lading | gewichtstoename, tijdstip | Nee | GGM |
| **Prijsafspraak** | Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten. | datumStart, datumEinde, titel | Nee | GGM |
| **Prijsregel** | Een *prijsregel* is een **regel die aangeeft hoe de prijs van een product, dienst of prestatie wordt vastgesteld of toegepast**, bijvoorbeeld binnen een declaratie- of tariefstructuur. | bedrag, credit | Nee | GGM |
| **Rit** | Verplaatsing van een wegvoertuig over een wegpad | starttijd, eindtijd, ritcode | Nee | GGM |
| **Route** | Routes die gereden worden om bepaalde fracties vuilnis op te halen. Routes gaan langs locaties, waar afhankelijk van de routesoort een containers, bepaalde plekken of adressen worden aangedaan. huis-aan-huis: er worden locaties met adressen aangedaan illegale dumping, grofvuil: er worden locaties aangedaan (evt met adres) containters: er worden locaties met containers aangedaan | routecode, routesoort, geometrie | Nee | GGM |
| **Vuilniswagen** | Een vrachtwagen die gebruikt wordt om afval in te zamelen bij bedrijven en huishoudens (huisvuil) | code, type, kenteken | Nee | GGM |
| **Vulgraadmeting** | Mate waarin een (afval)container gevuld is | tijdstip, vulgraad, vullingGewicht | Nee | GGM |

### Diagram Afval Milieustraat

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Milieustraat** | Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil. | naam, omschrijving, adresaanduiding | Nee | GGM |
| **Pas** | klein kaartje met je naam en soms je foto erop, dat je toegang geeft tot bepaalde diensten | pasnummer, adresaanduiding | Nee | GGM |
| **Storting** | Activiteit, inhoudende a. het zich ontdoen van stoffen | datumtijd, gewicht | Nee | GGM |

### Diagram Afval Meldingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Categorie** | Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren | code, naam, omschrijving | Nee | GGM |
| **Melding** | De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend | illegaal, 24uurs, datumtijd, omschrijving, meldingnummer | Nee | GGM |

## Overervingshiërarchie

```
AanvraagOfMelding (abstract)
    └── Melding
```

## Relatiediagrammen

### Diagram Afval Ophalen

```
Container [0..*] ──── Containertype [0..1] (soort)
Container [0..*] ──── Fractie [1] (geschikt voor)
Container [0..*] ──── Locatie [1] (heeft)
Container [1] ──── Vulgraadmeting [0..*] (heeft)
Melding [0..*] ──── Containertype [0..1] (betreft)
Melding [0..*] ──── Fractie [0..1] (betreft)
Melding [0..*] ──── Locatie [1] (betreft)
Milieustraat [0..*] ──── Fractie [0..*] (inzamelpunt van)
Ophaalmoment [0..*] ──── Container [0..1] (gelost)
Ophaalmoment [0..*] ──── Locatie [1] (gestopt op)
Prijsafspraak [1] ──── Prijsregel [0..*] (heeft)
Prijsregel [1..*] ──── Fractie [1] (betreft)
Rit [1] ──── Ophaalmoment [0..*] (heeft)
Rit [0..*] ──── Route [0..1] (volgens)
Rit [0..*] ──── Vuilniswagen [1] (uitgevoerd met)
Route [0..*] ──── Fractie [1] (ophalen)
Route [0..1] ──── Locatie [0..*] (gaat langs)
Storting [0..*] ──── Fractie [1..*] (fractie)
Vuilniswagen [0..*] ──── Containertype [1..*] (geschikt voor)
```

### Diagram Afval Milieustraat

```
Milieustraat [0..*] ──── Fractie [0..*] (inzamelpunt van)
Pas [0..*] ──── Milieustraat [1..*] (geldig voor)
Pas [1] ──── Storting [0..*] (uitgevoerde storting)
Storting [0..*] ──── Fractie [1..*] (fractie)
Storting [0..*] ──── Milieustraat [1] (bij)
```

### Diagram Afval Meldingen

```
Melding [0..*] ──── Categorie [1] (hoofdcategorie)
Melding [0..*] ──── Categorie [1] (subcategorie)
Melding [0..*] ──── Containertype [0..1] (betreft)
Melding [0..*] ──── Fractie [0..1] (betreft)
Melding [0..*] ──── Locatie [1] (betreft)
```

## Observaties

- Dit beleidsdomein bevat 16 entiteiten.
- Entiteiten zijn gegroepeerd in 3 diagramgroepen: Diagram Afval Ophalen (11), Diagram Afval Milieustraat (3), Diagram Afval Meldingen (2).
- Er is 1 generalisatierelatie aanwezig.
