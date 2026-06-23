---
type: ggm-beleidsdomein
naam: 10 Dienstverlening
definitie: "Het informatiedomein dat gegevens omvat over meldingen, aanvragen, baliecontacten, telefonische afhandeling en digitale interacties die faciliterend zijn voor andere domeinen."
taakveld: "10 Dienstverlening"
aantal_entiteiten: 16
---

# GGM Beleidsdomein: 10 Dienstverlening

### AanvraagOfMelding

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AanvraagOfMelding** | Komt overeen met een VJV Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID | afgehandeld, kanaal, soort, datumAfhandeling, categorie, identificatie, onderwerp, status, subcategorie, datumAanmaak, categoriecode, datumBeginStatus, datumEindeStatus, hoofdcategorie, hoofdcategoriecode, onderwerpcode, statuscode, statusVolgorde, subcategoriecode | Nee | GGM |

### Afspraken en Klantcontacten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Afspraakstatus** | de toestand van de afspraak | status | Nee | GGM |
| **Balieafspraak** | Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. | starttijdGepland, tijdAangemaakt, toelichting, tijdsduurGepland, wachttijdTotaal, eindtijdGepland, wachttijdVoorStartAfspraak, wachttijdNaStartAfspraak, werkelijkeTijdsduur, notitie | Nee | GGM |
| **ProductOfDienst** | Bron: QP_CALENDAR.CFM_SERVICES | naam, afhandeltijd, ingebruik | Nee | GGM |
| **Telefoononderwerp** | Onderwerp waarover het telefooncontact gaat | onderwerp | Nee | GGM |
| **Telefoonstatus** | ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon” DROPPEDCANCELED: “Opgehangen door systeem” ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ” CONNECTEDDIRECT: “Direct verbonden” CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap” AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap” DroppedBusy: “Opgehangen door systeem, te druk” REJECTED: “Geweigerd door systeem” Droppedoverload: “Opgehangen door systeem vanwege overbelasting” | contactConnectionState, status | Nee | GGM |
| **Telefoontje** | De telefoontgesprekken zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoongesprekken aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen. | starttijd, eindtijd, totaleTijdsduur, trackID, totaleWachttijd, totaleSpreektijd, totaleOnHoldTijd, afhandeltijdNaGesprek, deltaISDNConnectie | Nee | GGM |

### Entiteiten Dienstverlening

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanvraagdata** | Bron: GEN_REQ_DATA ID: REQ_DATA icm VELD_NAAM | veld, data | Nee | GGM |
| **Formuliersoort** | Bron: GEM_FORM ID: FORM_ID | naam, onderwerp, ingebruik | Nee | GGM |
| **Formuliersoortveld** | Bron: GEM_VELD ID: FORM_ID en VELD_NAAM | veldnaam, veldtype, helptekst, maxLengte, isVerplicht, label | Nee | GGM |
| **Onderwerp** | Bron: GEM_VJV_ONDERWERP ID: ONDERWERP_ID | naam, toelichting, isActief | Nee | GGM |

### Financien Verwerken Mutaties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **ExterneBron** | Bron buiten de eigen organisatie | *(geen attributen)* | Nee | GGM |

### Klantbeoordelingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Klantbeoordeling** | goed- of afkeurende uitspraak; = mening, opvatting | ddBeoordeling, beoordeling, contactOpnemen, categorie, subCategorie, onderwerp, kanaal | Nee | GGM |
| **Klantbeoordelingreden** | Reden voor de beoordeling | reden | Nee | GGM |

### MOR 2.0

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **MOR-AanvraagOfMelding** | Bericht van een inwoner over een gebrek of opvallendheid in de openbare ruimte | locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Artikel** | Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
AanvraagOfMelding (abstract)
    └── MOR-AanvraagOfMelding
```

## Relatiediagrammen

```
AanvraagOfMelding [1..1] ──── Aanvraagdata [0..*]
AanvraagOfMelding [0..*] ──── Formuliersoort [0..1]
AanvraagOfMelding [0..*] ──── Onderwerp [1..*]
Aanvraagdata [0..*] ──── Formuliersoortveld [1..1]
Balieafspraak [0..*] ──── Afspraakstatus [1..1]
Balieafspraak [0..*] ──── ProductOfDienst [0..*]
Formuliersoort [1..1] ──── Formuliersoortveld [0..*]
Klantbeoordeling ──── Klantbeoordelingreden
Onderwerp [0..*] ──── Onderwerp [1..1]
ProductOfDienst ──── Klantbeoordeling
Telefoononderwerp [0..1] ──── Telefoontje [0..*]
Telefoontje [0..*] ──── Telefoonstatus [1..1]
```

## Observaties

- Dit beleidsdomein bevat 16 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 16 diagramgroepen: AanvraagOfMelding (1), Afspraken en Klantcontacten (6), Brede Handhaving (1), Diagram Aanvragen, Zaken en Besluiten (1), Diagram Afval Meldingen (1), Diagram Beslissingen Leerplicht (1), Diagram Vergunningen en Meldingen (1), Dienstverlening en Klanten (1), Entiteiten Dienstverlening (6), Entiteiten Klantcontact (11), Financien Verwerken Mutaties (1), Klantbeoordelingen (3), MOR 2.0 (2), Verkamering en Woonoverlast (1), Zorgmelding (2), Zorgmelding Detail (1).
- Er zijn 1 generalisatierelaties aanwezig.
