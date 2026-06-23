---
type: ggm-beleidsdomein
naam: RGBZPlus
definitie: "Het subdomein dat gegevens omvat over gemeentelijke zaakgerichtheid, gebaseerd op RGBZ 1.0, met uitbreidingen voor specifieke toepassingen zoals leges en precario."
taakveld: "99 Kern"
aantal_entiteiten: 37
---

# GGM Beleidsdomein: RGBZPlus

### (Zaak)objecten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Object** | Het OBJECT waarop een ZAAK betrekking kan hebben zijnde één of meer voorkomens van de in het RSGB en het RGBZ onderscheiden objecttypen. | identificatie, objecttype, naam, adresBinnenland, adresBuitenland, kadastraleAanduiding, geometrie, toelichting, domein, indicatieRisico | Ja | GGM |

### Afspraken en Klantcontacten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Klantcontact** | Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. Hetzelfde geldt voor de telefoontjes, de klantcontacten komen uit levelOneData, dat zijn alle telefoontjes die werkelijk met een medewerker (of een gedelegeerde) hebben plaatsgevonden (soms zelfs meerdere binnen 1 telefoontje). | eindtijd, starttijd, tijdsduur, wachttijdTotaal, kanaal, toelichting, notitie | Nee | GGM |
| **Medewerker** | Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID. | medewerkerIdentificatie, achternaam, datumUitDienst, emailadres, functie, geslachtsaanduiding, medewerkerToelichting, roepnaam, telefoonnummer, voorletters, voorvoegselAchternaam, extern, datumInDienst | Nee | GGM |
| **VestigingVanZaakbehandelendeOrganisatie** | Een VESTIGING van een onderneming of rechtspersoon zijnde de zaakbehandelende organisatie. | *(geen attributen)* | Nee | GGM |
| **Zaak** | Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden. | zaakidentificatie, datumEinde, datumEindeGepland, omschrijving, omschrijvingResultaat, toelichtingResultaat, datumStart, toelichting, datumEindeUiterlijkeAfdoening, zaakniveau, indicatieDeelzaken, datumRegistratie, datumPublicatie, archiefnominatie, datumVernietigingDossier, indicatieBetaling, datumLaatsteBetaling, indicatieOpschorting, duurVerlenging, redenOpschorting, redenVerlenging, vertrouwelijkheid, leges, document, document | Nee | GGM |

### Archief Model

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Document** | Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT. | documentIdentificatie, datumCreatieDocument, datumOntvangstdocument, documentTitel, cocumentBeschrijving, datumVerzendingDocument, vertrouwelijkAanduiding, documentAuteur | Ja | GGM |

### Archief Relaties met Kern

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Documenttype** | Aanduiding van de aard van een DOCUMENT zoals gehanteerd door de zaakbehandelende organisatie | documenttypeOmschrijving, documenttypeOmschrijvingGeneriek, documentCategorie, documenttypeTrefwoord, datumBeginGeldigheidDocumenttype, datumEindeGeldigheidDocumenttype | Nee | GGM |
| **Identificatiekenmerk** | Nodig voor archivering om verschillende typen identificatie te kunnen onderscheiden: | kenmerk | Nee | GGM |

### Bedrijfsprocessen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bedrijfsproces** | Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of product of dienst. | Omschrijving, Datum_start, Datum_eind, Afgerond, Naam | Nee | GGM |
| **Bedrijfsprocestype** | soort Bedrijfsproces met bepaalde kenmerken | Omschrijving | Nee | GGM |
| **Deelproces** | Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd. | Datum_gepland, Datum_afgehandeld | Nee | GGM |
| **Deelprocestype** | soort Deelproces met bepaalde kenmerken | Omschrijving | Nee | GGM |
| **Zaaktype** | Generieke aanduiding van de aard van een zaak | zaaktypeOmschrijving, zaaktypeOmschrijvingGeneriek, trefwoord, doorlooptijdBehandeling, servicenormBehandeling, archiefcode, vertrouwelijkAanduiding, indicatiePublicatie, zaakcategorie, publicatietekst, datumBeginGeldigheidZaaktype, datumEindeGeldigheidZaaktype | Nee | GGM |

### Betrokkene

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Betrokkene** | Een SUBJECT, zijnde een NATUURLIJK PERSOON, NIET-NATUURLIJK PERSOON of VESTIGING, ORGANISATORISCHE EENHEID (binnen een vestiging van de zaak-behandelende niet-natuurlijk persoon), of MEDEWERKER (van die organisatorische eenheid) die een rol kan spelen bij een ZAAK. | naam, identificatie, adresBinnenland, adresBuitenland, rol, rol | Ja | GGM |
| **OrganisatorischeEenheid** | Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken. | organisatieIdentificatie, datumOntstaan, datumOpheffing, emailadres, faxnummer, naam, naamVerkort, omschrijving, telefoonnummer, toelichting, Formatie | Nee | GGM |

### Diagram Aanvragen, Zaken en Besluiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Besluit** | Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval. | besluitidentificatie, datumBesluit, besluittoelichting, datumStart, datumVerval, redenVerval, datumPublicatie, datumVerzending, datumUiterlijkeReactie, omschrijving | Nee | GGM |

### Diagram Vergunningen en Meldingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Heffing** | Een door de overheid opgelegde verplichting tot betaling | bedrag, code, inrekening, gefactureerd, runnummer, datumIndiening, nummer | Nee | GGM |
| **Status** | Een aanduiding van de stand van zaken van een zaak op basis van betekenisvol behaald resultaat voor de initiator van de zaak. | datumStatusGezet, statustoelichting, indicatieIaatstGezetteStatus | Nee | GGM |
| **Statustype** | Generieke aanduiding van de aard van een STATUS | statustypeOmschrijving, statustypeVolgnummer, doorlooptijdStatus, statustypeOmschrijvingGeneriek, datumBeginGeldigheidStatustype, datumEindeGeldigheidStatustype | Nee | GGM |

### Documenten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **EnkelvoudigDocument** | Een DOCUMENT waarvan aard, omvang en/of vorm aanleiding geven het als één geheel te behandelen en te beheren. | documentFormaat, documentTaal, documentVersie, documentStatus, documentInhoud, documentLink, bestandsnaam | Nee | GGM |
| **SamengesteldDocument** | Een DOCUMENT waarbinnen twee of meer ENKELVOUDIGe DOCUMENTen onderscheiden worden die vanwege gezamenlijke vervaardiging en/of ontvangst en/of vanwege aard en/of omvang als één geheel beschouwd moeten worden dan wel behandeld worden., | *(geen attributen)* | Nee | GGM |

### Entiteiten Dienstverlening

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Betaling** | het onderhandigen of overboeken van geld in ruil voor goed of dienst | bedrag, datumtijd, valuta, omschrijving | Nee | GGM |

### Metagegevens

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Brondocumenten** | Indicatie of bij een opname, mutatie of verwijdering van de relatie het brondocument aangeduid wordt op basis waarvan de verandering van de relatie heeft plaatsgevonden en zo ja, de specificatie van de metagegevens waarmee het brondcument aangeduid wordt, zijnde één of meer van de volgende metagegevens: Documentidentificatie, Documentdatum, Documentcode, Documentomschrijving, Document- soort, Documenthouder. | documentGemeente, akteGemeente, documentOmschrijving, datumDocument, documentIdentificatie | Nee | GGM |
| **FormeleHistorie** | Indicatie of de formele historie van de attribuutsoort te bevragen is. Formele historie geeft aan wanneer in de administratie een verandering is verwerkt van de attribuutwaarde (wanneer was de verandering bekend en is deze verwerkt) | tijdstipRegistratieGegevens | Nee | GGM |
| **InOnderzoek** | De indicatie of te bevragen is dat er twijfel is of is geweest aan de juistheid van de attribuutwaarde en dat een onderzoek wordt of is uitgevoerd naar de juistheid van de attribuutwaarde. | aanduidingGegevensInOnderzoek | Nee | GGM |
| **MaterieleHistorie** | Indicatie of de materiële historie van de attribuutsoort te bevragen is. Materiële historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot veranderjng van de attribuutwaarde. | datumEindeGeldigheidGegevens, datumBeginGeldigheidGegevens | Nee | GGM |
| **StrijdigheidOfNietigheid** | De aanduiding of te bevragen is dat de attribuutwaarde strijdig met de openbare orde dan wel nietig is. | aanduidingStrijdigheidNietigheid | Nee | GGM |

### Referentiemodel Gemeentelijke Basisgegevens Zaken in schema

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Besluittype** | Generieke aanduiding van de aard van een besluit | besluittypeOmschrijving, besluittypeOmschrijvingGeneriek, besluitcategorie, reactietermijn, indicatiePublicatie, publicatietekst, publicatietermijn, datumBeginGeldigheidBesluittype, datumEindeGeldigheidBesluittype | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AfwijkendBuitenlandsCorrespondentieadresRol** | De gegevens van het adres in het buitenland waarop BETROKKENE in zijn/haar ROL in de ZAAK in de regel schriftelijk bereikbaar is indien dat afwijkt van het reguliere buitenlandse correspondentieadres van BETROKKENE | adresBuitenland1, adresBuitenland2, adresBuitenland3, landPostadres | Nee | GGM |
| **AfwijkendCorrespondentiePostadresRol** | De gegevens die tezamen een postbusadres of antwoordnummeradres vormen waarvan BETROKKENE, geen ORGANISATORISCHE EENHEID en MEDEWERKER ziinde, heeft aangegeven schriftelijk bereikbaar te zijn in verband met zijn/haar ROL in de ZAAK en dat afwijkt van de reguliere correspondentiegegevens van BETROKKENE. | postcodePostadres, postadresType, postbusOfAntwoordnummer | Nee | GGM |
| **AnderZaakobjectZaak** | Aanduiding van het object (of de objecten) waarop de ZAAK betrekking heeft indien dat object (of die objecten) niet aangeduid kan worden met de relatie "heeft betrekking op ZAAKOBJECT". | anderZaakobjectRegistratie, anderZaakobjectOmschrijving, anderZaakobjectAanduiding, anderZaakobjectLocatie | Nee | GGM |
| **ContactpersoonRol** | De gegevens van de persoon die anderen desgevraagd in contact brengt met medewerkers van de BETROKKENE, een NIET-NATUURLIJK PERSOON of VESTIGING zijnde, of met BETROKKENE zelf, een NATUURLIJK PERSOON zijnde, vanuit het belang van BETROKKENE in haar ROL bij een ZAAK,. | Contactpersoonnaam, contactpersoonFunctie, contactpersoonTelefoonnummer, contactpersoonEmailadres | Nee | GGM |
| **KenmerkenZaak** | Identificatie-gegevens over de zaak in andere administraties | kenmerkBron, kenmerk | Nee | GGM |
| **Offerte** | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. | *(geen attributen)* | Nee | GGM |
| **OpschortingZaak** | Gegevens omtrent het tijdelijk opschorten van de behandeling van de ZAAK | indicatieOpschorting, redenOpschorting | Nee | GGM |
| **VerlengingZaak** | Gegevens omtrent het verlengen van de doorlooptijd van de behandeling van de ZAAK | redenVerlenging, duurVerlenging | Nee | GGM |
| **ZAAK - Origineel** | Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden. | zaakidentificatie, datumEinde, datumEindeGepland, omschrijving, kenmerk, omschrijvingResultaat, toelichtingResultaat, datumStart, toelichting, datumEindeUiterlijkeAfdoening, zaakniveau, indicatieDeelzaken, datumRegistratie, datumPublicatie, archiefnominatie, datumVernietigingDossier, indicatieBetaling, datumLaatsteBetaling, opschorting, verlenging, anderZaakobject | Nee | GGM |

## Overervingshiërarchie

```
Document (abstract)
    └── EnkelvoudigDocument
    └── SamengesteldDocument
```

```
Rechtspersoon (abstract)
    └── Betrokkene
```

## Relatiediagrammen

```
Bedrijfsproces ──── Bedrijfsprocestype
Bedrijfsproces ──── Zaak
Bedrijfsprocestype [0..*] ──── Bedrijfsprocestype [0..*]
Bedrijfsprocestype ──── Zaaktype
Besluit ──── Besluittype (Aanduiding van de aard van het BESLUIT.)
Besluit ──── Document (Aanduiding van het (de) DOCUMENT(en) waarin het BESLUIT beschreven is.)
Besluit ──── Zaak (Aanduiding van de ZAAK waarbinnen het BESLUIT genomen is.)
Betrokkene ──── Medewerker (Een MEDEWERKER als specialisatie van BETROKKENE.)
Betrokkene ──── OrganisatorischeEenheid (Een ORGANISATORISCHE EENHEID als specialisatie van BETROKKENE)
Betrokkene ──── Zaak (De ROLlen die BETROKKENE heeft in de zaken waarin BETROKKENE een ROL speelt.)
Deelproces ──── Bedrijfsproces
Deelproces ──── Deelprocestype
Deelprocestype ──── Bedrijfsprocestype
Document ──── Documenttype (Aanduiding van de aard van het DOCUMENT.)
Document [0..*] ──── Identificatiekenmerk [1..1]
Klantcontact [0..*] ──── Betrokkene [0..1]
Klantcontact [0..*] ──── Medewerker [0..1]
Klantcontact [0..*] ──── VestigingVanZaakbehandelendeOrganisatie [0..1]
Klantcontact [0..*] ──── Zaak [0..1]
Medewerker ──── OrganisatorischeEenheid (De MEDEWERKER die anderen desgevraagd in contact brengt met (andere) medewerkers van deze ORGANISATORISCHE EENHEID.)
Medewerker [0..1] ──── Zaaktype [0..*] (De MEDEWERKER die verantwoordelijk is voor ZAAKen van het ZAAKTYPE.)
Object ──── Besluit (Een BESLUIT als specialisatie van OBJECT.)
Object ──── Zaak (De ZAAKen die betrekking hebben op het OBJECT)
OrganisatorischeEenheid ──── OrganisatorischeEenheid
OrganisatorischeEenheid ──── VestigingVanZaakbehandelendeOrganisatie (De VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE waar de ORGANISATORISCHE EENHEID haar activiteiten uitvoert.)
OrganisatorischeEenheid ──── Zaaktype (De ORGANISATORISCHE EENHEID die verantwoordelijk is voor ZAAKen van het ZAAKTYPE.)
SamengesteldDocument ──── EnkelvoudigDocument (De ENKELVOUDIGe DOCUMENTen die deel uit maken van het SAMENGESTELD DOCUMENT.)
Status ──── Statustype (Aanduiding van de aard van de STATUS.)
ZAAK - Origineel ──── ZAAK - Origineel (De andere ZAAKen die het onderwerp zijn van de ZAAK.)
Zaak [0..1] ──── Betaling [0..*]
Zaak ──── Document
Zaak ──── Heffing
Zaak [1..1] ──── KenmerkenZaak [0..*]
Zaak ──── Medewerker
Zaak ──── Status (De STATUSsen die bereikt zijn gedurende de behandeling van de ZAAK.)
Zaak ──── Zaak (De verwijzing naar de ZAAK, waarom verzocht is door de initiator daarvan, die door de zaakbehandelende organisatie is opgedeeld in twee of meer separaat te behandelen zaken waarvan de onderhavige zaak er één is.)
Zaak ──── Zaaktype (Aanduiding van de aard van de ZAAK.)
Zaaktype ──── Statustype (De STATUSTYPEn die bereikt kunnen worden bij behandeling van ZAAKen van het ZAAKTYPE.)
```

## Observaties

- Dit beleidsdomein bevat 37 Objecttype-entiteiten (+ 4 Enumeraties, 2 diagramhulpobjecten zonder stereotype).
- Entiteiten zijn gegroepeerd in 50 diagramgroepen: (Zaak)objecten (1), Afspraken en Klantcontacten (4), Archief Model (1), Archief Relaties met Kern (3), Basismodel CMDB-Items (2), Bedrijfsprocessen (6), Betrokkene (3), Bezetting en Formatie (1), Brede Handhaving (1), Diagram Aanvragen, Zaken en Besluiten (3), Diagram Domeinen, PDC en zaken (1), Diagram Griffie (1), Diagram Inkoop Geen Inhuur (4), Diagram Inkoop Inhuur (3), Diagram Monumenten Detail (1), Diagram Sportbeleid Locaties (1), Diagram Vergunningen en Meldingen (9), Diagram Verlengen Inhuur (3), Dienstverlening en Klanten (3), Documenten (4), Domain Objects (2), Entiteiten Dienstverlening (8), Entiteiten Klantcontact (1), Erfgoed: Archeologie Domeinmodel (1), Financien Verplichtingen en Facturen (1), Financien Verwerken Mutaties (1), Kern:Klantcontact (4), Klantbeoordelingen (3), Meldingen Graafwerkzaamheden (2), Metagegevens (5), Model Parkeren (1), Objecten bij Vergunningaanvraag (1), Omgevingswet Verzoek met Project (IMAM) (1), Omgevingswet Verzoeken (IMAM) (4), Onderwijs: Relaties met Kern (1), Prinsenhof Collectie (1), Referentiemodel Gemeentelijke Basisgegevens Zaken in schema (15), Relaties Sociaal Domein tot Kern (1), Relaties met Kern (1), Ruimte WOZ en Benoemd Object (1), Schouwrondes Beheersobjecten (1), Sociaal Domein Beschikking en Voorziening: Domain Objects (1), Sollicitaties (1), Subsidies (4), Verkamering en Woonoverlast (9), Verkeer en Vervoer: Stremmingen (1), Verkeersbesluiten (1), Vroegsignalering (1), Vroegsignalering Klein (1), Zorgmelding (4).
- Er zijn 3 generalisatierelaties aanwezig.
