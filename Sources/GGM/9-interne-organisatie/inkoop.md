---
type: ggm-beleidsdomein
naam: Inkoop
definitie: "Het informatiesubdomein dat gegevens omvat over het proces van het verwerven van goederen, diensten en werken door een organisatie."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 20
---

# GGM Beleidsdomein: Inkoop

Beleidsdomein binnen taakveld "9 Interne Organisatie" (zie ../structuur-ggm.md).

## Entiteiten

### Diagram Verlengen Inhuur

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Contract** | Bindende overeenkomst | contractRevisie, internContractID, internContractRevisie, status, groep, type, categorie, classificatie, voorwaarde, beschrijving, zoekwoorden, autorisatiegroep, opmerkingen, datumStart, datumEinde, datumCreatie | Nee | GGM |
| **FormulierVerlengingInhuur** | Formulier ten behoeve van verlenging inhuur personeel | datumEindeNieuw, indicatieVerhogenInkooporder, indicatieRedenInhuurGewijzigd, toelichting | Nee | GGM |
| **Leverancier** | Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie | naam, nummer | Nee | GGM |

### Diagram Inkoop Inhuur

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanbesteding Inhuur** | Aanbesteding voor inhuur van personen of diensten | datumVerzending, status, titel, type, publicatie, perceel, datumSluiting, aanvraagnummer, omschrijving, hoogsteTarief, laagsteTarief, datumOpeningKluis, datumCreatie, referentie, procedure, projectreferentie, projectnaam, aanvraagGesloten, fase | Nee | GGM |
| **Categorie** | Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren | code, omschrijving | Nee | GGM |
| **FormulierInhuur** | Formulier ten behoeve van inhuur personeel | functienaamInhuur, datumIngangInhuur, akkoordHRAdviseur, akkoordFinancieelAdviseur | Nee | GGM |
| **Gunning** | Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding Of voor levering personeel | datumGunning, bericht, datumVoorlopigeGunning, gegundePrijs, datumPublicatie | Nee | GGM |
| **Kandidaat** | Iemand die een bepaalde baan of functie wil | datumIngestuurd | Nee | GGM |
| **Uitnodiging** | Een verzoek om iets bij te wonen. | datum, afgewezen, geaccepteerd | Nee | GGM |

### Diagram Inkoop Geen Inhuur

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanbesteding** | Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding | naam, tendernedKenmerk, status, datumStart, volgendeSluiting, type, procedure, digitaal, referentienummer, datumPublicatie, scoreMaximaal | Nee | GGM |
| **Aankondiging** | Aankondiging van een Nationale of Europese aanbesteding | datum, naam, beschrijving, type, categorie | Nee | GGM |
| **CPV-code** | De Common Procurement Vocabulary (CPV-codes) is een gemeenschappelijke woordenlijst van de EU, alle mogelijke soorten overheidsopdrachten voor diensten, leveringen en werken hebben een eigen code gekregen. Aanbestedende diensten moeten bij Europese aanbestedingen dit classificatiesysteem toepassen. | code, omschrijving | Nee | GGM |
| **Inkooppakket** | Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd. | code, naam, type | Nee | GGM |
| **Inschrijving** | Inschrijving op een nationale of Europese aanbesteding | datum, prijs, score | Nee | GGM |
| **Kwalificatie** | Kwalifificatie voor een nationale of europese aanbesteding | startGeldigheid, eindeGeldigheid | Nee | GGM |
| **Offerte** | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. | prijs, datumOfferte, naam, omschrijving | Nee | GGM |
| **Offerteaanvraag** | Aanbesteding bij inschrijving | datumAanvraag, datumSluiting, naam, omschrijving | Nee | GGM |
| **SelectietabelAanbesteding** | Gebaseerd op het procedureoverzicht inkoop. Hierin kan de tabel met drempelbedragen en bijbehorende procedures worden opgeslagen | opdrachtcategorie, drempelbedragVanaf, drempelbedragTot, aanbestedingsoort, openbaar | Nee | GGM |
| **StartformulierAanbesteden** | Formulier voor het starten van een aanbeseding | omschrijving, indicatorOverkoepelendProject, opdrachtsoort, opdrachtcategorie, indicatieEenmaligeLos, indicatieMeerjarigRepeterend, indicatieMeerjarigeRaamovereenkomst, toelichtingEenmaligOfRepeterend, indicatieAanvullendeOpdrachtLeverancier, toelichtingAanvullendeOpdracht, beoogdeLooptijd, beoogdeTotaleOpdrachtwaarde, indicatieBeoogdeAanbestedingOnderhands, indicatieBeoogdeProcKomtOvereen | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanvraag Inkooporder** | het betreft hier het formulier 'Aanvraag Inkooporder' | correspondentienummer, onderwerp, omschrijving, leveringOfDienst, wijzeVanInhuur, inhuurAnders, betalingOverMeerJaren, nettoTotaalBedrag, reactie, status | Nee | GGM |

## Overervingshiërarchie

```
Aanbesteding (abstract)
    └── Aanbesteding Vastgoed
```

```
Leverancier (abstract)
    └── Belprovider
    └── Uitvoerder Graafwerkzaamheden
    └── Vervoerder
```

```
Rechtspersoon (abstract)
    └── Leverancier
```

## Relatiediagrammen

### Diagram Verlengen Inhuur

```
Aanvraag Inkooporder [0..*] ──── Contract [1] (betreft)
Aanvraag Inkooporder [0..*] ──── Leverancier [1] (betreft)
Applicatie [0..*] ──── Leverancier [0..1] (heeft leverancier)
Contract [0..*] ──── Contract [0..1] (bovenliggend)
Contract [1] ──── Tarief [0..*] (bevat)
Factuur [0..*] ──── Leverancier [1] (crediteur)
FormulierVerlengingInhuur [0..*] ──── Inkooporder [1] (betreft)
FormulierVerlengingInhuur [0..*] ──── Leverancier [1] (ingehuurd via)
FormulierVerlengingInhuur [0..*] ──── Medewerker [1] (aanvrager)
FormulierVerlengingInhuur [0..*] ──── Medewerker [1] (betreft)
Inkooporder [0..1] ──── Contract [1] (betreft)
Inkooporder [0..*] ──── Leverancier [1] (verplichting aan)
Leverancier [0..*] ──── Aanbesteding Vastgoed [0..*] (heeft gekwalificeerd)
Leverancier [0..*] ──── Categorie [0..*] (gekwalificeerd)
Leverancier [1] ──── Contract [0..*] (heeft)
Leverancier [1] ──── Contract [0..*] (contractant)
Leverancier [1] ──── Inschrijving [0..*] (heeft)
Leverancier [1] ──── Kandidaat [0..*] (biedt aan)
Leverancier [1] ──── Kwalificatie [0..*] (heeft)
Leverancier [1] ──── Werkbon [0..*] (voert werk uit conform)
Medewerker [0..*] ──── Leverancier [0..1] (geleverd via)
Melding [0..*] ──── Leverancier [0..1] (uitvoerder)
Offerte [0..*] ──── Leverancier [1] (ingediend door)
Offerteaanvraag [0..*] ──── Leverancier [1] (gericht aan)
Product [0..*] ──── Leverancier [0..1] (leverancier)
Productie-eenheid [0..*] ──── Leverancier [0..1] (betreft)
Server [0..*] ──── Leverancier [0..1] (heeft leverancier)
Uitnodiging [0..*] ──── Leverancier [1] (gericht aan)
```

### Diagram Inkoop Inhuur

```
Aanbesteding [0..1] ──── Gunning [0..1] (mondt uit)
Aanbesteding Inhuur [0..*] ──── CPV-code [1] (valt onder)
Aanbesteding Inhuur [0..*] ──── Categorie [1] (valt binnen)
Aanbesteding Inhuur [1] ──── Gunning [0..1] (mondt uit)
Aanbesteding Inhuur [0..*] ──── Medewerker [0..1] (eigenaar)
FormulierInhuur [0..1] ──── Aanbesteding Inhuur [0..1] (mondt uit in)
FormulierInhuur [0..*] ──── Kostenplaats [1] (heeft)
FormulierInhuur [0..*] ──── Medewerker [1] (aanvrager)
Gunning [0..1] ──── Inschrijving [0..1] (betreft)
Gunning [0..1] ──── Kandidaat [1] (betreft)
Gunning [0..*] ──── Medewerker [0..1] (inhuur)
Gunning [0..1] ──── Offerte [0..1] (betreft)
Kandidaat [0..*] ──── Aanbesteding Inhuur [1] (ingediend voor)
Kandidaat [0..*] ──── NatuurlijkPersoon [1] (betreft)
Leverancier [0..*] ──── Categorie [0..*] (gekwalificeerd)
Leverancier [1] ──── Kandidaat [0..*] (biedt aan)
Uitnodiging [0..*] ──── Aanbesteding Inhuur [1] (betreft)
Uitnodiging [0..*] ──── Leverancier [1] (gericht aan)
```

### Diagram Inkoop Geen Inhuur

```
Aanbesteding [0..1] ──── Gunning [0..1] (mondt uit)
Aanbesteding [0..*] ──── Medewerker [0..1] (procesleider)
Aanbesteding [0..1] ──── Zaak [0..1] (betreft)
Aanbesteding Inhuur [0..*] ──── CPV-code [1] (valt onder)
Aankondiging [0..*] ──── Aanbesteding [0..1] (mondt uit)
CPV-code [1] ──── Aanbesteding [0..*] (valt onder)
Gunning [0..1] ──── Inschrijving [0..1] (betreft)
Gunning [0..1] ──── Offerte [0..1] (betreft)
Inkooporder [0..*] ──── Inkooppakket [1] (heeft)
Inkooppakket [0..*] ──── CPV-code [1..*] (heeft)
Inschrijving [0..*] ──── Aanbesteding [1] (betreft)
Kwalificatie [0..*] ──── Aanbesteding [1] (betreft)
Leverancier [1] ──── Inschrijving [0..*] (heeft)
Leverancier [1] ──── Kwalificatie [0..*] (heeft)
Medewerker [1] ──── StartformulierAanbesteden [0..*] (dient in)
Offerte [0..*] ──── Aanbesteding [1] (betreft)
Offerte [0..*] ──── Leverancier [1] (ingediend door)
Offerteaanvraag [0..*] ──── Aanbesteding [1] (betreft)
Offerteaanvraag [0..*] ──── Leverancier [1] (gericht aan)
StartformulierAanbesteden [0..1] ──── Aanbesteding [0..1] (mondt uit)
StartformulierAanbesteden [0..1] ──── Aankondiging [0..*] (mondt uit)
StartformulierAanbesteden [0..*] ──── Zaak [0..1] (betreft)
```

### Overig

```
Aanvraag Inkooporder [0..*] ──── Contract [1] (betreft)
Aanvraag Inkooporder [0..*] ──── Inkooporder [0..1] (mondt uit in )
Aanvraag Inkooporder [0..*] ──── Leverancier [1] (betreft)
Aanvraag Inkooporder [0..*] ──── Medewerker [1] (ingediend bij)
Aanvraag Inkooporder [0..*] ──── OrganisatorischeEenheid [1] (afgehandeld door)
Aanvraag Inkooporder [0..1] ──── Zaak [0..1] (afhandeling)
Medewerker [1] ──── Aanvraag Inkooporder [0..*] (vraagt aan)
```

## Observaties

- Dit beleidsdomein bevat 20 entiteiten.
- Entiteiten zijn gegroepeerd in 4 diagramgroepen: Diagram Verlengen Inhuur (3), Diagram Inkoop Inhuur (6), Diagram Inkoop Geen Inhuur (10), Overig (1).
- Er zijn 5 generalisatierelaties aanwezig.
