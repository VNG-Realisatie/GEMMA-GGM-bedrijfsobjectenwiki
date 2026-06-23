---
type: ggm-beleidsdomein
naam: Subsidies
definitie: "Het informatiedomein dat gegevens omvat over het proces van aanvragen, beoordelen, verstrekken, beheren en verantwoorden van subsidies door de organisatie, zowel in de rol van subsidieverstrekker als subsidieontvanger."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 9
---

# GGM Beleidsdomein: Subsidies

### Subsidie en Kostenplaats

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Betaalmoment** | Moment waarop er een bepaald deel van de subsidie betaald moet worden. | bedrag, datum, voorschot | Nee | GGM |
| **Subsidie** | Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten | niveau, deadlineIndiening, subsidiebedrag, coFinanciering, opmerkingen, status, accountantscontrole, datumStart, datumEinde, datumVerzendingEindeafrekening, gerealiseerdeProjectkosten, hoogteSubsidie, datumBehandeltermijn, datumSubsidievaststelling, subsidievaststellingBedrag, ontvangenBedrag, datumBewaartermijn, onderwerp, subsidiesoort, socialReturnVerplichting, socialReturnNagekomen, socialReturnBedrag, verantwoordenOp, uitgaandeSubsidie, prestatiesubsidie, doelstelling, opmerkingenVoorschotten | Nee | GGM |
| **Subsidiecomponent** | Onderdeel van een subisidie met een eigen kostenplaats. | toegekendBedrag, gereserveerdBedrag | Nee | GGM |
| **Subsidieprogramma** | Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang | naam, omschrijving, datumStart, datumEinde, programmabegroting | Nee | GGM |

### Subsidies

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Rapportagemoment** | Een vantevoren bepaald tijdstip waarom een gegevensanalyse wordt uitgevoerd | datum, naam, omschrijving, termijn | Nee | GGM |
| **Sector** | Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid. | naam, omschrijving | Nee | GGM |
| **Subsidieaanvraag** | Aanvraag voor een subsidie | datumIndiening, aangevraagdBedrag, ontvangstbevestiging, verwachteBeschikking, kenmerk | Nee | GGM |
| **Subsidiebeschikking** | Besluit over het al dan niet toekennen van een subsidie | beschiktBedrag, ontvangen, kenmerk, internKenmerk, opmerkingen, besluit, beschikkingsnummer | Nee | GGM |
| **Taak** | Een samenhangende set activiteiten in het kader van een subsidie. | datumStart, datumEinde, termijn, taakomschrijving | Nee | GGM |

## Relatiediagrammen

```
Subsidie ──── Rapportagemoment
Subsidie ──── Sector
Subsidie ──── Taak
Subsidieaanvraag ──── Subsidie
Subsidieaanvraag ──── Subsidiebeschikking
Subsidiebeschikking ──── Subsidie
Subsidiecomponent ──── Betaalmoment
Subsidieprogramma ──── Subsidie
```

## Observaties

- Dit beleidsdomein bevat 9 Objecttype-entiteiten (+ 1 Enumeraties).
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Subsidie en Kostenplaats (4), Subsidies (8).
