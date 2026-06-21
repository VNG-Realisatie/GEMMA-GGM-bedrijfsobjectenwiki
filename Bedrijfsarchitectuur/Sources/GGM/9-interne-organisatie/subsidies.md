---
type: ggm-beleidsdomein
naam: Subsidies
definitie: "Het informatiedomein dat gegevens omvat over het proces van aanvragen, beoordelen, verstrekken, beheren en verantwoorden van subsidies door de organisatie, zowel in de rol van subsidieverstrekker als subsidieontvanger."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 9
---

# GGM Beleidsdomein: Subsidies

Beleidsdomein binnen taakveld "9 Interne Organisatie" (zie ../structuur-ggm.md).

## Entiteiten

### Subsidies

In het gegevensmodel voor subsidies staat ‘Subsidie’ centraal. Hiermee wordt een van een ingaande of uitgaande subsidie afgebeeld. Bij een ‘Subsidie’ is altijd een ‘Subsidieaanvraag’ en er kan een ‘Subsidiebeschikking’ aan gekoppeld zijn. Afhankelijk of het een inkomende of een uitgaande ‘Subsidie’ is een ‘Medewerker’ (van de Gemeente) aanvrager of behandelaar (via de relaties). Ook afhankelijk of het een Inkomende of uitgaande ‘Subsidie’ is een (extern) ‘Rechtspersoon’ aanvrager of verstrekker. Als aanvrager kan het een natuurlijk persoon zijn of een niet-natuurlijk persoon. Een verstrekker kan een willekeurige subsidieverstrekkende partij zijn. Op basis van een ‘Subsidie’ kunnen er meerdere voorschotten ontvangen/betaald worden, en kunnen er meerdere taken bij een ‘Medewerker’ van de gemeente liggen. Ook kunnen er meerdere rapportagemomenten aan een subsidie zijn gekoppeld. Een ‘Subsidie’ kan binnen een ‘Subsidieprogramma’ vallen, waarbinnen de doelstelling van dat programma is vastgelegd. Een ‘Subsidieprogramma’ is gekoppeld aan een 'Subsidiecomponent' die ieder een eigen ‘Kostenplaats’ kan hebben. Subsidies vallen binnen een bepaalde ‘Sector’.

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Rapportagemoment** | Een vantevoren bepaald tijdstip waarom een gegevensanalyse wordt uitgevoerd | datum, naam, omschrijving, termijn | Nee | GGM |
| **Sector** | Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid. | naam, omschrijving | Nee | GGM |
| **Subsidie** | Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten | niveau, deadlineIndiening, subsidiebedrag, coFinanciering, opmerkingen, status, accountantscontrole, datumStart, datumEinde, datumVerzendingEindeafrekening, gerealiseerdeProjectkosten, hoogteSubsidie, datumBehandeltermijn, datumSubsidievaststelling, subsidievaststellingBedrag, ontvangenBedrag, datumBewaartermijn, onderwerp, subsidiesoort, socialReturnVerplichting, socialReturnNagekomen, socialReturnBedrag, verantwoordenOp, uitgaandeSubsidie, prestatiesubsidie, doelstelling, opmerkingenVoorschotten | Nee | GGM |
| **Subsidieaanvraag** | Aanvraag voor een subsidie | datumIndiening, aangevraagdBedrag, ontvangstbevestiging, verwachteBeschikking, kenmerk | Nee | GGM |
| **Subsidiebeschikking** | Besluit over het al dan niet toekennen van een subsidie | beschiktBedrag, ontvangen, kenmerk, internKenmerk, opmerkingen, besluit, beschikkingsnummer | Nee | GGM |
| **Subsidiecomponent** | Onderdeel van een subisidie met een eigen kostenplaats. | toegekendBedrag, gereserveerdBedrag | Nee | GGM |
| **Subsidieprogramma** | Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang | naam, omschrijving, datumStart, datumEinde, programmabegroting | Nee | GGM |
| **Taak** | Een samenhangende set activiteiten in het kader van een subsidie. | datumStart, datumEinde, termijn, taakomschrijving | Nee | GGM |

### Subsidie en Kostenplaats

Dit diagram geeft de relatie tussen 'Subsidiecomponent' de betalingen en de geplande 'Betaalmomenten' weer. Een 'Subsidiecomponent' heeft 1 of meer 'Betaalmoment' waarmee de geplande betalingen worden uitgebeeld. Daarnaast vinden er in het kader van de 'Subsidie' betalingen plaats op bepaalde 'Kostenplaatsen'. Deze betalingen zijn uitgebeeld als 'Mutatie' uit het Model Financien.

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Betaalmoment** | Moment waarop er een bepaald deel van de subsidie betaald moet worden. | bedrag, datum, voorschot | Nee | GGM |

## Overervingshiërarchie

Geen overervingshiërarchie aanwezig in dit beleidsdomein.

## Relatiediagrammen

### Subsidies

```
Medewerker [0..1] ──── Subsidie [0..*] (aanvrager)
Rapportagemoment [0..1] ──── Document [0..*] (heeft)
Rechtspersoon [0..1] ──── Rapportagemoment [0..*] (projectleider)
Rechtspersoon [0..1] ──── Subsidie [0..*] (aanvrager)
Subsidie [0..*] ──── Document [0..1] (heeft)
Subsidie [0..*] ──── Kostenplaats [0..1] (heeft)
Subsidie [0..*] ──── Medewerker [0..1] (behandelaar)
Subsidie [1] ──── Rapportagemoment [0..*] (heeft)
Subsidie [0..*] ──── Rechtspersoon [0..1] (verstrekker)
Subsidie [0..*] ──── Sector [0..1] (valt binnen)
Subsidie [1] ──── Taak [0..*] (heeft)
Subsidie [0..1] ──── Zaak [0..1] (heeft)
Subsidieaanvraag [1] ──── Subsidie [1] (betreft)
Subsidieaanvraag [1] ──── Subsidiebeschikking [0..1] (mondt uit)
Subsidiebeschikking [0..1] ──── Subsidie [1] (betreft)
Subsidiecomponent [1] ──── Betaalmoment [1..*] (heeft)
Subsidiecomponent [0..*] ──── Kostenplaats [1] (heeft)
Subsidieprogramma [0..*] ──── OrganisatorischeEenheid [1] (verantwoordelijk voor)
Subsidieprogramma [0..1] ──── Subsidie [1..*] (gaat over)
Taak [0..*] ──── Rechtspersoon [0..1] (projectleider)
```

### Subsidie en Kostenplaats

```
Subsidiecomponent [1] ──── Betaalmoment [1..*] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 9 entiteiten.
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Subsidies (8), Subsidie en Kostenplaats (1).
