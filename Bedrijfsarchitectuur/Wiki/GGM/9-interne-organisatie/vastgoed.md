---
type: ggm-beleidsdomein
naam: Vastgoed
definitie: "Het informatiedomein dat gegevens omvat over het beheer, onderhoud en de exploitatie van gebouwen en terreinen in eigendom van de organisatie."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 27
---

# GGM Beleidsdomein: Vastgoed

Beleidsdomein binnen taakveld "9 Interne Organisatie" (zie ../structuur-ggm.md).

## Entiteiten

### Vastgoed Domeinmodel 

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bouwdeel** | Zelfstandig en aanwijsbaar deel van een element, onderscheiden naar samenstelling of constructiewijze, bestaande uit één of meer componenten waaraan technische eigenschappen en een onderhoudshistorie kunnen worden gerelateerd (bron: Conditiemeting gebouwde omgeving - Deel 1: Methodiek, code: 3.3) | code, omschrijving | Nee | GGM |
| **Bouwdeelelement** | Onderdeeel van een bouwdeel | code, omschrijving | Nee | GGM |
| **Inspectie** | het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen. | datum, bevindingen | Nee | GGM |
| **MJOP** | Meerjaren Onderhoudsplanning | datum, omschrijving | Nee | GGM |
| **MJOP-Item** | Onderdeel van een MJOP | code, omschrijving, kosten, datumStart, datumEinde, opzegtermijnAanbieder, opzegtermijnOntvanger, datumOpzeggingAanbieder, datumOpzeggingOntvanger | Nee | GGM |
| **Prijzenboekitem** | Onderdeel van een prijzenboek | verrichting, prijs, datumStart, datumEindeGeldigheid | Nee | GGM |
| **Vastgoed Contract** | Een contract is een afspraak tussen 2 of meer partijen. Sluit u een contract, dan moet u een bepaalde prestatie leveren of u heeft recht op een prestatie. Een ander woord voor een contract is een overeenkomst. Daarnaast komt de term overeenkomst van opdracht ook voor. | datumStart, datumEinde, maandbedrag, beschrijving, status, type, identificatie, opzegtermijn | Nee | GGM |
| **Vastgoedobject** | Perceel of vastgoed waar de gemeente een zakelijk recht heeft, en optioneel verhuurd, verpacht of anderzinds aan een derde partij. | adresaanduiding, WOZWaarde, marktwaarde, boekwaarde, verzekerdeWaarde, omschrijving, portefeuille, naam, bedragAankoop, aantalEtages, afgekochteErfpacht, afkoopwaarde, asbestrapportageAanwezig, datumAfstoten, datumBerekeningOppervlak, deelportefeuille, objecttype, fiscaleWaarde, gearchiveerd, herbouwwaarde, monument, onderhoudscategorie, provincie, verkoopbedrag, waardeGrond, waardeOpstal, wijk, energielabel, energieverbruik, energiekosten, CO2Uitstoot, jaarLaatsteRenovatie, aantalRioleringen, oppervlakteKantoor, conditiescore, aantalParkeerplaatsen, verkoopbaarheid, afgesprokenConditiescore, kostenplaats, bovenliggendNiveau, bestemmingsplan, locatie, bouwjaar, objectstatuscode, objectstatus, objecttypecode, portefeuillecode, bovenliggendNiveaucode, hoofdstuk, identificatie, foto, toelichting, datumEigendom, datumVerkoop, bouwwerk, brutoVloeroppervlakte, verhuurbaarVloeroppervlak | Nee | GGM |
| **Verhuurbaar Eenheid** | Een Verhuurbare Eenheid (VHE) is een eenheid die individueel verhuurbaar is. Verhuurbaar komt voort uit 'exploitatie' | identificatie, naam, datumWerkelijkBegin, datumWerkelijkEinde, type, adres, datumStart, datumEinde, afmeting, opmerkingen, nettoOppervlak, nettoOmtrek, bezetting, huurprijs | Nee | GGM |
| **Werkbon** | Document waarin een heoveelheid werk is beschreven | *(geen attributen)* | Nee | GGM |
| **Zakelijk Recht** | Geeft een recht op een goed, zoals een onroerende zaak of een roerende zaak. | datumStart, datumEinde, soort, kosten | Nee | GGM |

### Vastgoed Relaties met Kern 

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Eigenaar** | Eigenaar is een persoon die de eigenaar is van een gebouw of stuk grond en ook alle rechten daarvan bezit. | *(geen attributen)* | Nee | GGM |
| **Huurder** | Een partij die een zaak of een gedeelte daarvan in gebruik verstrekt heeft gekregen en zich heeft verbonden tot een tegenprestatie. | *(geen attributen)* | Nee | GGM |
| **Pachter** | Een persoon die een pachtovereenkomst heeft met de eigenaar van een perceel voor het gebruik als landbouwgrond. | *(geen attributen)* | Nee | GGM |

### Vastgoed Leveranciers

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanbesteding Vastgoed** | Een procedure waarbij een opdrachtgever bekendmaakt dat hij een opdracht of concessie wil laten uitvoeren en bedrijven uitnodigt om een offerte in te dienen. Dit in het kader van werkzaamheden rondom vastgoed. | *(geen attributen)* | Nee | GGM |
| **Objectrelatie** | Relatie tot een object | rol | Nee | GGM |

### POC Vastgoed 

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Adresaanduiding** | De adresaanduiding van het WOZ-OBJECT | adres | Nee | GGM |

### Vastgoed verankering RSGB IMBAG

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **KpBetrokkenBij** | *(geen definitie in GGM)* | datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **KpOnstaanUit** | *(geen definitie in GGM)* | datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **Locatieonroerendezaak** | Locatie van een geregistreerd goed | locatieOmschrijving, cultuurcodeBebouwd, adrestype, datumBeginGeldigheid, datumEindeGeldigheid, geometrie | Nee | GGM |
| **NADAanvullingBRP** | *(geen definitie in GGM)* | opmerkingen | Nee | GGM |
| **Vastgoedcontractregel** | ONderdeel van een vastgoedcontract | type, omschrijving, status, datumStart, bedrag, datumEinde, frequentie, identificatie | Nee | GGM |

### Vastgoed WOZ

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **LocatieaanduidingWozObject** | Nadere aanduiding van het WOZ-object | locatieOmschrijving, datumBeginGeldigheid, datumEindeGeldigheid, primair | Nee | GGM |
| **WOZ-Belang** | hetgeen waaraan een persoon waarde hecht; zaak die of vorderingsrecht dat op geld waardeerbaar is, aan gevaar onderhevig en bij de wet niet uitgezonderd. De (rechts-)persoon die door de gemeente is aangewezen als "belanghebbende eigenaar", "belanghebbende gebruiker" of eventueel "medebelanghebbende" van het WOZ-object. | datumBeginGeldigheid, datumEindeGeldigheid, eigenaarGebruiker | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **CultuurOnbebouwd** | Een aanduiding voor de soort cultuur van het onbebouwde gedeelte van de onroerende zaak. | cultuurcodeOnbebouwd | Nee | GGM |
| **Gebruiksdoel** | Een aanduiding va alle waarden waarmee het gebruiksdoel van een object kan worden verbijzonderd. | gebruiksdoelGebouwdObject | Nee | GGM |
| **Offerte** | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
Aanbesteding (abstract)
    └── Aanbesteding Vastgoed
```

```
Nummeraanduiding (abstract)
    └── NADAanvullingBRP
```

```
Rechtspersoon (abstract)
    └── Eigenaar
    └── Huurder
    └── Pachter
```

```
Vastgoedobject (abstract)
    └── Locatie
```

```
ZakelijkRecht (abstract)
    └── Zakelijk Recht
```

## Relatiediagrammen

### Vastgoed Domeinmodel 

```
Aanbesteding Vastgoed [0..1] ──── Werkbon [0..*] (uitvoering van)
Bouwdeel [1] ──── Bouwdeelelement [0..*] (bestaat uit)
Huurder [0..*] ──── Zakelijk Recht [1..*] (heeft huurrecht)
Inkooporder [1] ──── Werkbon [0..*] (hoort bij)
Inspectie [0..1] ──── MJOP [0..1] (leidt tot)
Kostenplaats [1] ──── Vastgoedobject [0..*] (heeft)
Leverancier [1] ──── Werkbon [0..*] (voert werk uit conform)
MJOP [1] ──── MJOP-Item [0..*] (bestaat uit)
MJOP [0..*] ──── Vastgoedobject [1] (betreft)
MJOP [1] ──── Werkbon [0..*] (gerealiseerd door)
MJOP-Item [0..*] ──── Bouwdeel [0..1] (betreft)
MJOP-Item [0..*] ──── Bouwdeelelement [0..1] (betreft)
MJOP-Item [0..*] ──── Prijzenboekitem [1] (op basis van)
MJOP-Item [0..*] ──── Vastgoedobject [1] (betreft)
Pand [1] ──── Vastgoedobject [1] (heeft)
Vastgoed Contract [0..*] ──── Rechtspersoon [1] (heeft)
Vastgoedcontractregel [1..*] ──── Vastgoed Contract [1] (heeft)
Vastgoedobject [1] ──── Bouwdeel [0..*] (bestaat uit)
Vastgoedobject [1] ──── Inspectie [0..*] (betreft)
Vastgoedobject [0..*] ──── KadastraalPerceel [0..*] (betreft)
Vastgoedobject [0..*] ──── KadastraleOnroerendeZaak [0..*] (betreft)
Vastgoedobject [1] ──── Objectrelatie [0..*] (heeft)
Vastgoedobject [0..1] ──── Pand [0..1] (betreft)
Vastgoedobject [1..] ──── Vastgoedcontractregel [0..1] (heeft)
Vastgoedobject [1] ──── Verhuurbaar Eenheid [0..*] (heeft)
Vastgoedobject [1..*] ──── Zakelijk Recht [0..*] (betreft)
Verblijfsobject [1] ──── Vastgoedobject [1] (heeft)
Verhuurbaar Eenheid [0..1] ──── Vastgoedcontractregel [1] (betreft)
Werkbon [0..*] ──── Bouwdeel [0..*] (betreft)
Werkbon [0..*] ──── Bouwdeelelement [0..*] (betreft)
Werkbon [0..*] ──── Vastgoedobject [1] (betreft)
Zakelijk Recht [0..*] ──── Eigenaar [0..*] (heeft eigenaar)
Zakelijk Recht [0..*] ──── Kostenplaats [1] (heeft)
Zakelijk Recht [1..*] ──── Pachter [0..*] (pacht)
```

### Vastgoed Relaties met Kern 

```
Huurder [0..*] ──── Zakelijk Recht [1..*] (heeft huurrecht)
Zakelijk Recht [0..*] ──── Eigenaar [0..*] (heeft eigenaar)
Zakelijk Recht [1..*] ──── Pachter [0..*] (pacht)
```

### Vastgoed Leveranciers

```
Aanbesteding Vastgoed [0..1] ──── Werkbon [0..*] (uitvoering van)
Leverancier [0..*] ──── Aanbesteding Vastgoed [0..*] (heeft gekwalificeerd)
Rechtspersoon [1] ──── Objectrelatie [0..*] (heeft)
Vastgoedobject [1] ──── Objectrelatie [0..*] (heeft)
```

### POC Vastgoed 

```
KadastraleOnroerendeZaak [1..*] ──── Adresaanduiding [0..*] (heeft adres)
```

### Vastgoed verankering RSGB IMBAG

```
KpBetrokkenBij [0..*] ──── Appartementsrechtsplitsing [1]
KpBetrokkenBij [0..*] ──── ZakelijkRecht [1] (is betrokken bij)
KpOnstaanUit [0..*] ──── Appartementsrechtsplitsing [1]
KpOnstaanUit [0..*] ──── ZakelijkRecht [1] (is ontstaan uit)
Locatieonroerendezaak [0..*] ──── AdresseerbaarObject [1] (heeft Adresseerbaar object)
Locatieonroerendezaak [0..*] ──── KadastraleOnroerendeZaak [1] (heeft adres)
Vastgoedcontractregel [1..*] ──── Vastgoed Contract [1] (heeft)
Vastgoedobject [1..] ──── Vastgoedcontractregel [0..1] (heeft)
Verhuurbaar Eenheid [0..1] ──── Vastgoedcontractregel [1] (betreft)
```

### Vastgoed WOZ

```
LocatieaanduidingWozObject [1] ──── WOZ-object [1] (heeft)
Nummeraanduiding [0..1] ──── LocatieaanduidingWozObject [1] (verwijst naar)
Rechtspersoon [1] ──── WOZ-Belang [1..*] (heeft)
WOZ-object [1] ──── WOZ-Belang [1..*] (heeft)
```

### Overig

```
GebouwdObject [1] ──── Gebruiksdoel [1..*] (heeft)
KadastraleOnroerendeZaak [1] ──── CultuurOnbebouwd [0..*] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 27 entiteiten.
- Entiteiten zijn gegroepeerd in 7 diagramgroepen: Vastgoed Domeinmodel  (11), Vastgoed Relaties met Kern  (3), Vastgoed Leveranciers (2), POC Vastgoed  (1), Vastgoed verankering RSGB IMBAG (5), Vastgoed WOZ (2), Overig (3).
- Er zijn 7 generalisatierelaties aanwezig.
