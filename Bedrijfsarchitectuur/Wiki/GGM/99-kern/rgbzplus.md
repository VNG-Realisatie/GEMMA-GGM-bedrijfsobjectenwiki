---
type: ggm-beleidsdomein
naam: RGBZPlus
definitie: "Het subdomein dat gegevens omvat over gemeentelijke zaakgerichtheid, gebaseerd op RGBZ 1.0, met uitbreidingen voor specifieke toepassingen zoals leges en precario."
taakveld: "99 Kern"
aantal_entiteiten: 39
---

# GGM Beleidsdomein: RGBZPlus

Beleidsdomein binnen taakveld "99 Kern" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AfwijkendBuitenlandsCorrespondentieadresRol** | De gegevens van het adres in het buitenland waarop BETROKKENE in zijn/haar ROL in de ZAAK in de regel schriftelijk bereikbaar is indien dat afwijkt van het reguliere buitenlandse correspondentieadres van BETROKKENE | adresBuitenland1, adresBuitenland2, adresBuitenland3, landPostadres | Nee | GGM |
| **AfwijkendCorrespondentiePostadresRol** | De gegevens die tezamen een postbusadres of antwoordnummeradres vormen waarvan BETROKKENE, geen ORGANISATORISCHE EENHEID en MEDEWERKER ziinde, heeft aangegeven schriftelijk bereikbaar te zijn in verband met zijn/haar ROL in de ZAAK en dat afwijkt van de reguliere correspondentiegegevens van BETROKKENE. | postcodePostadres, postadresType, postbusOfAntwoordnummer | Nee | GGM |
| **AnderZaakobjectZaak** | Aanduiding van het object (of de objecten) waarop de ZAAK betrekking heeft indien dat object (of die objecten) niet aangeduid kan worden met de relatie "heeft betrekking op ZAAKOBJECT". | anderZaakobjectRegistratie, anderZaakobjectOmschrijving, anderZaakobjectAanduiding, anderZaakobjectLocatie | Nee | GGM |
| **Bedrijfsproces** | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of product of dienst. | Omschrijving, Datum_start, Datum_eind, Afgerond, Naam | Nee | GGM |
| **Bedrijfsprocestype** | soort Bedrijfsproces met bepaalde kenmerken | Omschrijving | Nee | GGM |
| **Besluit** | Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval. | besluitidentificatie, datumBesluit, besluittoelichting, datumStart, datumVerval, redenVerval, datumPublicatie, datumVerzending, datumUiterlijkeReactie, omschrijving | Nee | GGM |
| **Besluittype** | Generieke aanduiding van de aard van een besluit | besluittypeOmschrijving, besluittypeOmschrijvingGeneriek, besluitcategorie, reactietermijn, indicatiePublicatie, publicatietekst, publicatietermijn, datumBeginGeldigheidBesluittype, datumEindeGeldigheidBesluittype | Nee | GGM |
| **Betaling** | het onderhandigen of overboeken van geld in ruil voor goed of dienst | bedrag, datumtijd, valuta, omschrijving | Nee | GGM |
| **Betrokkene** | Een SUBJECT, zijnde een NATUURLIJK PERSOON, NIET-NATUURLIJK PERSOON of VESTIGING, ORGANISATORISCHE EENHEID (binnen een vestiging van de zaak-behandelende niet-natuurlijk persoon), of MEDEWERKER (van die organisatorische eenheid) die een rol kan spelen bij een ZAAK. | naam, identificatie, adresBinnenland, adresBuitenland, rol, rol | Ja | GGM |
| **Brondocumenten** | Indicatie of bij een opname, mutatie of verwijdering van de relatie het brondocument aangeduid wordt op basis waarvan de verandering van de relatie heeft plaatsgevonden en zo ja, de specificatie van de metagegevens waarmee het brondcument aangeduid wordt, zijnde één of meer van de volgende metagegevens: Documentidentificatie, Documentdatum, Documentcode, Documentomschrijving, Document- soort, Documenthouder. | documentGemeente, akteGemeente, documentOmschrijving, datumDocument, documentIdentificatie | Nee | GGM |
| **ContactpersoonRol** | De gegevens van de persoon die anderen desgevraagd in contact brengt met medewerkers van de BETROKKENE, een NIET-NATUURLIJK PERSOON of VESTIGING zijnde, of met BETROKKENE zelf, een NATUURLIJK PERSOON zijnde, vanuit het belang van BETROKKENE in haar ROL bij een ZAAK,. | Contactpersoonnaam, contactpersoonFunctie, contactpersoonTelefoonnummer, contactpersoonEmailadres | Nee | GGM |
| **Deelproces** | Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd. | Datum_gepland, Datum_afgehandeld | Nee | GGM |
| **Deelprocestype** | soort Deelproces met bepaalde kenmerken | Omschrijving | Nee | GGM |
| **Document** | Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT. | documentIdentificatie, datumCreatieDocument, datumOntvangstdocument, documentTitel, cocumentBeschrijving, datumVerzendingDocument, vertrouwelijkAanduiding, documentAuteur | Ja | GGM |
| **Documenttype** | Aanduiding van de aard van een DOCUMENT zoals gehanteerd door de zaakbehandelende organisatie | documenttypeOmschrijving, documenttypeOmschrijvingGeneriek, documentCategorie, documenttypeTrefwoord, datumBeginGeldigheidDocumenttype, datumEindeGeldigheidDocumenttype | Nee | GGM |
| **EnkelvoudigDocument** | Een DOCUMENT waarvan aard, omvang en/of vorm aanleiding geven het als één geheel te behandelen en te beheren. | documentFormaat, documentTaal, documentVersie, documentStatus, documentInhoud, documentLink, bestandsnaam | Nee | GGM |
| **FormeleHistorie** | Indicatie of de formele historie van de attribuutsoort te bevragen is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de attribuutwaarde (wanneer was de verandering bekend en is deze verwerkt) | tijdstipRegistratieGegevens | Nee | GGM |
| **Heffing** | Een door de overheid opgelegde verplichting tot betaling | bedrag, code, inrekening, gefactureerd, runnummer, datumIndiening, nummer | Nee | GGM |
| **Identificatiekenmerk** | Nodig voor archivering om verschillende typen identificatie te kunnen onderscheiden: | kenmerk | Nee | GGM |
| **InOnderzoek** | De indicatie of te bevragen is dat er twijfel is of is geweest aan de juistheid van de attribuutwaarde en dat een onderzoek wordt of is uitgevoerd naar de juistheid van de attribuutwaarde. | aanduidingGegevensInOnderzoek | Nee | GGM |
| **KenmerkenZaak** | Identificatie-gegevens over de zaak in andere administraties | kenmerkBron, kenmerk | Nee | GGM |
| **Klantcontact** | Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. Hetzelfde geldt voor de telefoontjes, de klantcontacten komen uit levelOneData, dat zijn alle telefoontjes die werkelijk met een medewerker (of een gedelegeerde) hebben plaatsgevonden (soms zelfs meerdere binnen 1 telefoontje). | eindtijd, starttijd, tijdsduur, wachttijdTotaal, kanaal, toelichting, notitie | Nee | GGM |
| **MaterieleHistorie** | Indicatie of de materiële historie van de attribuutsoort te bevragen is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot veranderjng van de attribuutwaarde. | datumEindeGeldigheidGegevens, datumBeginGeldigheidGegevens | Nee | GGM |
| **Medewerker** | Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID. | medewerkerIdentificatie, achternaam, datumUitDienst, emailadres, functie, geslachtsaanduiding, medewerkerToelichting, roepnaam, telefoonnummer, voorletters, voorvoegselAchternaam, extern, datumInDienst | Nee | GGM |
| **Object** | Het OBJECT waarop een ZAAK betrekking kan hebben zijnde één of meer voorkomens van de in het RSGB en het RGBZ onderscheiden objecttypen. | identificatie, objecttype, naam, adresBinnenland, adresBuitenland, kadastraleAanduiding, geometrie, toelichting, domein, indicatieRisico | Ja | GGM |
| **Offerte** | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. | *(geen attributen)* | Nee | GGM |
| **OpschortingZaak** | Gegevens omtrent het tijdelijk opschorten van de behandeling van de ZAAK | indicatieOpschorting, redenOpschorting | Nee | GGM |
| **OrganisatorischeEenheid** | Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken. | organisatieIdentificatie, datumOntstaan, datumOpheffing, emailadres, faxnummer, naam, naamVerkort, omschrijving, telefoonnummer, toelichting, Formatie | Nee | GGM |
| **RSGB** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **RSGB** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **SamengesteldDocument** | Een DOCUMENT waarbinnen twee of meer ENKELVOUDIGe DOCUMENTen onderscheiden worden die vanwege gezamenlijke vervaardiging en/of ontvangst en/of vanwege aard en/of omvang als één geheel beschouwd moeten worden dan wel behandeld worden., | *(geen attributen)* | Nee | GGM |
| **Status** | Een aanduiding van de stand van zaken van een zaak op basis van betekenisvol behaald resultaat voor de initiator van de zaak. | datumStatusGezet, statustoelichting, indicatieIaatstGezetteStatus | Nee | GGM |
| **Statustype** | Generieke aanduiding van de aard van een STATUS | statustypeOmschrijving, statustypeVolgnummer, doorlooptijdStatus, statustypeOmschrijvingGeneriek, datumBeginGeldigheidStatustype, datumEindeGeldigheidStatustype | Nee | GGM |
| **StrijdigheidOfNietigheid** | De aanduiding of te bevragen is dat de attribuutwaarde strijdig met de openbare orde dan wel nietig is. | aanduidingStrijdigheidNietigheid | Nee | GGM |
| **VerlengingZaak** | Gegevens omtrent het verlengen van de doorlooptijd van de behandeling van de ZAAK | redenVerlenging, duurVerlenging | Nee | GGM |
| **VestigingVanZaakbehandelendeOrganisatie** | Een VESTIGING van een onderneming of rechtspersoon zijnde de zaakbehandelende organisatie. | *(geen attributen)* | Nee | GGM |
| **ZAAK - Origineel** | Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden. | zaakidentificatie, datumEinde, datumEindeGepland, omschrijving, kenmerk, omschrijvingResultaat, toelichtingResultaat, datumStart, toelichting, datumEindeUiterlijkeAfdoening, zaakniveau, indicatieDeelzaken, datumRegistratie, datumPublicatie, archiefnominatie, datumVernietigingDossier, indicatieBetaling, datumLaatsteBetaling, opschorting, verlenging, anderZaakobject | Nee | GGM |
| **Zaak** | Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden. | zaakidentificatie, datumEinde, datumEindeGepland, omschrijving, omschrijvingResultaat, toelichtingResultaat, datumStart, toelichting, datumEindeUiterlijkeAfdoening, zaakniveau, indicatieDeelzaken, datumRegistratie, datumPublicatie, archiefnominatie, datumVernietigingDossier, indicatieBetaling, datumLaatsteBetaling, indicatieOpschorting, duurVerlenging, redenOpschorting, redenVerlenging, vertrouwelijkheid, leges, document, document | Nee | GGM |
| **Zaaktype** | Generieke aanduiding van de aard van een zaak | zaaktypeOmschrijving, zaaktypeOmschrijvingGeneriek, trefwoord, doorlooptijdBehandeling, servicenormBehandeling, archiefcode, vertrouwelijkAanduiding, indicatiePublicatie, zaakcategorie, publicatietekst, datumBeginGeldigheidZaaktype, datumEindeGeldigheidZaaktype | Nee | GGM |

## Overervingshiërarchie

```
Document (abstract)
    └── Archiefstuk
    └── EnkelvoudigDocument
    └── Heffingsverordening
    └── SamengesteldDocument
```

```
Medewerker (abstract)
    └── Clientbegeleider
    └── Leerplichtambtenaar
    └── Samensteller
    └── Werknemer
```

```
Object (abstract)
    └── AdresseerbaarObject
    └── BenoemdObject
    └── KadastraleOnroerendeZaak
    └── Nummeraanduiding
    └── Onbestemd Adres
```

```
OrganisatorischeEenheid (abstract)
    └── OrganisatorischeEenheidHR
```

```
Rechtspersoon (abstract)
    └── Betrokkene
```

```
Zaak (abstract)
    └── VTHzaak
    └── Vroegsignaalzaak
```

## Relatiediagrammen

```
Aanbesteding [0..*] ──── Medewerker [0..1] (procesleider)
Aanbesteding [0..1] ──── Zaak [0..1] (betreft)
Aanbesteding Inhuur [0..*] ──── Medewerker [0..1] (eigenaar)
Aanvraag Inkooporder [0..*] ──── Medewerker [1] (ingediend bij)
Aanvraag Inkooporder [0..*] ──── OrganisatorischeEenheid [1] (afgehandeld door)
Aanvraag Inkooporder [0..1] ──── Zaak [0..1] (afhandeling)
AanvraagOfMelding [0..1] ──── Document [0..*] (heeft documenten)
AanvraagOfMelding [0..1] ──── Zaak [0..*] (kan leiden tot)
Applicatie [0..*] ──── Document [0..*] (heeft documenten)
Applicatie [0..*] ──── Medewerker [0..*] (rollen)
Balieafspraak [0..1] ──── Klantcontact [0..1] (mondt uit in)
Balieafspraak [0..*] ──── Medewerker [0..1] (met)
Balieafspraak [0..*] ──── VestigingVanZaakbehandelendeOrganisatie [0..1] (locatie)
Balieafspraak [0..*] ──── Zaak [0..1] (heeft betrekking op)
Bankrekening [1] ──── Betaling [0..*] (van)
Bankrekening [1] ──── Betaling [0..*] (naar)
Bedrijfsproces [1..*] ──── Bedrijfsprocestype [1..] (is van)
Bedrijfsproces [1..*] ──── Zaak [1..*] (uitgevoerd binnen)
Bedrijfsprocestype [0..*] ──── Bedrijfsprocestype [0..*] (is onderdeel van)
Bedrijfsprocestype [1] ──── Producttype [1..*] (heeft)
Bedrijfsprocestype [1] ──── Zaaktype [1..*] (heeft)
Besluit [0..*] ──── Besluittype [1] (is van)
Besluit [0..*] ──── Document [0..*] (kan vastgelegd zijn als)
Besluit [0..1] ──── Document [0..1] (is vastgelegd in)
Besluit [0..*] ──── Zaak [1] (is uitkomst van)
Betaling [0..*] ──── Bankafschriftregel [0..1] (komt voor op)
Betrokkene [1] ──── Klantbeoordeling [0..*] (doet)
Betrokkene [0..1] ──── Medewerker [1] (is)
Betrokkene [0..1] ──── NatuurlijkPersoon [1] (is)
Betrokkene [0..1] ──── NietNatuurlijkPersoon [1] (is)
Betrokkene [0..1] ──── OrganisatorischeEenheid [1] (is)
Betrokkene [1..*] ──── Zaak [1..*] (oefent uit)
Deelproces [1..] ──── Bedrijfsproces [1] (is deel van)
Deelproces [1] ──── Deelprocestype [1] (is van)
Deelprocestype [1] ──── Bedrijfsprocestype [1] (is deel van)
Dienst [0..*] ──── Zaaktype [0..1] (start)
Dienstverband [0..*] ──── VestigingVanZaakbehandelendeOrganisatie [0..*] (is op vestiging)
Document [0..*] ──── Documenttype [1] (is van)
Document [0..*] ──── Identificatiekenmerk [1] (heeft kenmerk)
FormulierInhuur [0..*] ──── Medewerker [1] (aanvrager)
FormulierVerlengingInhuur [0..*] ──── Medewerker [1] (aanvrager)
FormulierVerlengingInhuur [0..*] ──── Medewerker [1] (betreft)
Formuliersoort [0..*] ──── Zaaktype [0..*] (is aanleiding voor)
Grondslag [1..*] ──── Zaak [1..*] (Heeft)
Gunning [0..*] ──── Medewerker [0..1] (inhuur)
Heffing [0..*] ──── Heffinggrondslag [1] (heeft grondslag)
Heffing [0..*] ──── Heffingsoort [1] (soort)
Heffing [0..1] ──── Vorderingregel [1..] (betreft)
Klantcontact [0..1] ──── AanvraagOfMelding [0..*] (kan leiden tot)
Klantcontact [0..*] ──── Betrokkene [0..1] (heeft klantcontacten)
Klantcontact [0..*] ──── Medewerker [0..1] (is gevoerd door)
Klantcontact [0..*] ──── ProductOfDienst [0..*] (betreft)
Klantcontact [1] ──── Soorten Klantcontact [0..*] (is van soort)
Klantcontact [0..*] ──── VestigingVanZaakbehandelendeOrganisatie [0..1] (locatie)
Klantcontact [0..*] ──── Zaak [0..1] (heeft betrekking op)
Medewerker [1] ──── Aanvraag Inkooporder [0..*] (vraagt aan)
Medewerker [0..*] ──── Leverancier [0..1] (geleverd via)
Medewerker [0..1] ──── OrganisatorischeEenheid [0..1] (is contactpersoon voor)
Medewerker [0..*] ──── OrganisatorischeEenheid [0..*] (hoort bij)
Medewerker [0..1] ──── OrganisatorischeEenheid [0..1] (is verantwoordelijk voor)
Medewerker [1] ──── Proces-verbaal-MOOR-melding [0..*] (verleent)
Medewerker [1] ──── Schouwronde [0..*] (voert uit)
Medewerker [1] ──── StartformulierAanbesteden [0..*] (dient in)
Medewerker [1] ──── Stremming [0..*] (ingevoerd door)
Medewerker [0..1] ──── Stremming [0..*] (gewijzigd door)
Medewerker [0..1] ──── Subsidie [0..*] (aanvrager)
Medewerker [0..*] ──── Uitvoerende instantie [1] (werkt bij)
Medewerker [0..1] ──── Zaaktype [0..*] (is verantwoordelijke voor)
Melding [0..*] ──── Medewerker [0..1] (melder)
Melding [0..*] ──── Medewerker [0..1] (uitvoerder)
Notitie [0..*] ──── Medewerker [1] (auteur)
Object [0..1] ──── Besluit [1..] (is)
Object [0..1] ──── Buurt [0..*] (is)
Object [0..1] ──── Huishouden [1] (is)
Object [0..1] ──── Ingezetene [1] (Is)
Object [0..1] ──── Inrichtingselement [0..*] (is)
Object [0..1] ──── KadastraalPerceel [0..*] (is)
Object [0..1] ──── KadastraleOnroerendeZaak [0..*] (is)
Object [0..1] ──── Kunstwerkdeel [0..*] (is)
Object [0..1] ──── Ligplaats [0..*] (is)
Object [0..1] ──── MaatschappelijkeActiviteit [0..*] (is)
Object [0..1] ──── NatuurlijkPersoon [0..*] (is)
Object [0..1] ──── NietNatuurlijkPersoon [0..*] (is)
Object [0..1] ──── OpenbareRuimte [0..*] (is)
Object [0..1] ──── Pand [0..*] (is)
Object [0..1] ──── Standplaats [0..*] (is)
Object [0..1] ──── Vaartuig [0..1] (is)
Object [0..1] ──── Voertuig [0..1] (is)
Object [0..1] ──── Waterdeel [0..*] (is)
Object [0..1] ──── Zaak [1] (betreft)
OrganisatorischeEenheid [1..*] ──── Klantbeoordeling [0..*] (heeft)
OrganisatorischeEenheid [0..1] ──── Kostenplaats [1] (heeft)
OrganisatorischeEenheid [1] ──── OrganisatorischeEenheid [0..1] (Is deel van)
OrganisatorischeEenheid [1..*] ──── VestigingVanZaakbehandelendeOrganisatie [1] (is gehuisvest in)
OrganisatorischeEenheid [0..1] ──── Zaaktype [0..*] (is verantwoordelijke voor)
Parkeerscan [0..*] ──── Medewerker [1] (uitgevoerd door)
Proces-verbaal-MOOR-melding [0..*] ──── Document [0..1] (heeft)
Product [0..1] ──── Zaaktype [0..*] (betreft)
Rapportagemoment [0..1] ──── Document [0..*] (heeft)
SamengesteldDocument [0..1] ──── EnkelvoudigDocument [2..*] (omvat)
StartformulierAanbesteden [0..*] ──── Zaak [0..1] (betreft)
Status [0..*] ──── Statustype [1] (is van)
Subsidie [0..*] ──── Document [0..1] (heeft)
Subsidie [0..*] ──── Medewerker [0..1] (behandelaar)
Subsidie [0..1] ──── Zaak [0..1] (heeft)
Subsidieprogramma [0..*] ──── OrganisatorischeEenheid [1] (verantwoordelijk voor)
Telefoononderwerp [0..1] ──── Klantcontact [0..*] (heeft)
Telefoontje [0..1] ──── Klantcontact [0..*] (mondt uit in)
VTH-Melding [0..*] ──── Object [0..*] (betreft)
Verkeersbesluit [1] ──── Document [1] (is vastgelegd in)
Verzoek [0..1] ──── Zaak [0..1] (leidt tot)
ZAAK - Origineel  ──── ZAAK - Origineel [0..*] (heeft betrekking op andere)
ZAAK - Origineel  ──── ZAAK - Origineel [0..1] (is deelzaak van)
Zaak [0..1] ──── Betaling [0..*] (heeft betaling)
Zaak [0..*] ──── Document [1..*] (kent)
Zaak [1] ──── Heffing [0..1] (heeft)
Zaak [1] ──── KenmerkenZaak [0..*] (heeft kenmerken)
Zaak [1] ──── Klantbeoordeling [0..1] (heeft)
Zaak [0..*] ──── Medewerker [0..*] (afhandelend medewerker)
Zaak [1] ──── Producttype [1] (heeft product)
Zaak [0..*] ──── Project [0..1] (betreft)
Zaak [1] ──── Status [0..*] (heeft)
Zaak [1] ──── Zaak [0..1] (is deelzaak van)
Zaak [1] ──── Zaak [0..*] (heeft betrekking op andere)
Zaak [0..*] ──── Zaaktype [1] (is van)
Zaaktype [1] ──── Heffinggrondslag [0..*] (heeft)
Zaaktype [1] ──── Producttype [1] (heeft)
Zaaktype [1] ──── Statustype [1..*] (heeft)
Zorgmelding [0..*] ──── Medewerker [0..*] (betrokken professional)
```

## Observaties

- Dit beleidsdomein bevat 39 entiteiten.
- Er zijn 17 generalisatierelaties aanwezig.
- 3 entiteiten zijn abstract.
