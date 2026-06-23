---
type: ggm-beleidsdomein
naam: Model Dienstverlening
definitie: "Het informatiedomein dat gegevens omvat over meldingen, aanvragen, baliecontacten, telefonische afhandeling en digitale interacties die faciliterend zijn voor andere domeinen."
taakveld: "10 Dienstverlening"
aantal_entiteiten: 16
---

# GGM Beleidsdomein: Model Dienstverlening

Beleidsdomein binnen taakveld "10 Dienstverlening" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AanvraagOfMelding** | Komt overeen met een VJV Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID | afgehandeld, kanaal, soort, datumAfhandeling, categorie, identificatie, onderwerp, status, subcategorie, datumAanmaak, categoriecode, datumBeginStatus, datumEindeStatus, hoofdcategorie, hoofdcategoriecode, onderwerpcode, statuscode, statusVolgorde, subcategoriecode | Nee | GGM |
| **Aanvraagdata** | Bron: GEN_REQ_DATA ID: REQ_DATA icm VELD_NAAM | veld, data | Nee | GGM |
| **Afspraakstatus** | de toestand van de afspraak | status | Nee | GGM |
| **Artikel** | Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk | *(geen attributen)* | Nee | GGM |
| **Balieafspraak** | Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. | starttijdGepland, tijdAangemaakt, toelichting, tijdsduurGepland, wachttijdTotaal, eindtijdGepland, wachttijdVoorStartAfspraak, wachttijdNaStartAfspraak, werkelijkeTijdsduur, notitie | Nee | GGM |
| **ExterneBron** | Bron buiten de eigen organisatie | *(geen attributen)* | Nee | GGM |
| **Formuliersoort** | Bron: GEM_FORM ID: FORM_ID | naam, onderwerp, ingebruik | Nee | GGM |
| **Formuliersoortveld** | Bron: GEM_VELD ID: FORM_ID en VELD_NAAM | veldnaam, veldtype, helptekst, maxLengte, isVerplicht, label | Nee | GGM |
| **Klantbeoordeling** | goed- of afkeurende uitspraak; = mening, opvatting | ddBeoordeling, beoordeling, contactOpnemen, categorie, subCategorie, onderwerp, kanaal | Nee | GGM |
| **Klantbeoordelingreden** | Reden voor de beoordeling | reden | Nee | GGM |
| **MOR-AanvraagOfMelding** | Bericht van een inwoner over een gebrek of opvallendheid in de openbare ruimte | locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst | Nee | GGM |
| **Onderwerp** | Bron: GEM_VJV_ONDERWERP ID: ONDERWERP_ID | naam, toelichting, isActief | Nee | GGM |
| **ProductOfDienst** | Bron: QP_CALENDAR.CFM_SERVICES | naam, afhandeltijd, ingebruik | Nee | GGM |
| **Telefoononderwerp** | Onderwerp waarover het telefooncontact gaat | onderwerp | Nee | GGM |
| **Telefoonstatus** | ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon” DROPPEDCANCELED: “Opgehangen door systeem” ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ” CONNECTEDDIRECT: “Direct verbonden” CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap” AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap” DroppedBusy: “Opgehangen door systeem, te druk” REJECTED: “Geweigerd door systeem” Droppedoverload: “Opgehangen door systeem vanwege overbelasting” | contactConnectionState, status | Nee | GGM |
| **Telefoontje** | De telefoontgesprekken zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoongesprekken aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen. | starttijd, eindtijd, totaleTijdsduur, trackID, totaleWachttijd, totaleSpreektijd, totaleOnHoldTijd, afhandeltijdNaGesprek, deltaISDNConnectie | Nee | GGM |

## Overervingshiërarchie

```
AanvraagOfMelding (abstract)
    └── AOMMeldingWmoJeugd
    └── AOM_AanvraagWmoJeugd
    └── AanvraagOfMelding
    └── MOR-AanvraagOfMelding
    └── MORAanvraagOfMelding
    └── Melding
    └── VOMAanvraagOfMelding
    └── VTH-Melding
    └── WoonfraudeAanvraagOfMelding
    └── WoonoverlastAanvraagOfMelding
    └── Zorgmelding
```

## Relatiediagrammen

```
AanvraagOfMelding [1] ──── AOMStatus [1..*] (heeft)
AanvraagOfMelding [1] ──── Aanvraagdata [0..*] (heeft data)
AanvraagOfMelding [0..1] ──── Document [0..*] (heeft documenten)
AanvraagOfMelding [0..*] ──── Formuliersoort [0..1] (aanvraag met )
AanvraagOfMelding [0..*] ──── Indiener [1] (ingediend door)
AanvraagOfMelding [0..*] ──── Onderwerp [1..*] (betreft)
AanvraagOfMelding [1..*] ──── Rechtspersoon [0..1] (melder)
AanvraagOfMelding [0..1] ──── Zaak [0..*] (kan leiden tot)
Aanvraagdata [0..*] ──── Formuliersoortveld [1] (is conform)
Balieafspraak [0..*] ──── Afspraakstatus [1] (heeft)
Balieafspraak [0..1] ──── Klantcontact [0..1] (mondt uit in)
Balieafspraak [0..*] ──── Medewerker [0..1] (met)
Balieafspraak [0..*] ──── ProductOfDienst [0..*] (betreft)
Balieafspraak [0..*] ──── VestigingVanZaakbehandelendeOrganisatie [0..1] (locatie)
Balieafspraak [0..*] ──── Zaak [0..1] (heeft betrekking op)
Batch [0..*] ──── ExterneBron [1] (heeft herkomst)
Betrokkene [1] ──── Klantbeoordeling [0..*] (doet)
Formuliersoort [1] ──── Formuliersoortveld [0..*] (heeft velden)
Formuliersoort [0..*] ──── Zaaktype [0..*] (is aanleiding voor)
Klantbeoordeling [1] ──── Klantbeoordelingreden [0..*] (heeft)
Klantcontact [0..1] ──── AanvraagOfMelding [0..*] (kan leiden tot)
Klantcontact [0..*] ──── ProductOfDienst [0..*] (betreft)
Onderwerp [0..*] ──── Onderwerp [1] (hoofdonderwerp)
OrganisatorischeEenheid [1..*] ──── Klantbeoordeling [0..*] (heeft)
ProductOfDienst [1..*] ──── Klantbeoordeling [0..*] (heeft)
Telefoononderwerp [0..1] ──── Klantcontact [0..*] (heeft)
Telefoononderwerp [0..1] ──── Telefoontje [0..*] (heeft)
Telefoontje [0..1] ──── Klantcontact [0..*] (mondt uit in)
Telefoontje [0..*] ──── Telefoonstatus [1] (heeft)
Zaak [1] ──── Klantbeoordeling [0..1] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 16 entiteiten.
- Er zijn 11 generalisatierelaties aanwezig.
