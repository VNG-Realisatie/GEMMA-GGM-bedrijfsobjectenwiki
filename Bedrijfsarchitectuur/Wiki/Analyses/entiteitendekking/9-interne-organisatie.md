---
type: analyse
titel: "Entiteitendekking: 9 Interne Organisatie"
datum: 2026-07-07
taakveld: "9 Interne Organisatie"
beleidsdomeinen:
  - Financien
  - HR
  - ICT
  - Inkoop
  - Organisatie-indeling
  - Subsidies
  - Vastgoed
totaal_entiteiten: 148
totaal_bo: 53
totaal_matches: 44
totaal_hiaten: 9
---

# Entiteitendekking: 9 Interne Organisatie

## Beoordeling

7 beleidsdomeinen, 148 GGM-entiteiten. Dekking: 138 van 148 (93%) — 44 met BO, 94 ondersteunend, 10 niet gedekt. 9 BO's zonder GGM-entiteit.

Niet-BO entiteiten: 2× actor, 13× classificatie, 7× component, 80× detail, 2× rol.

**Structurele patronen.** Het merendeel van de niet-BO entiteiten (80 van 104) is *detail*: attributen, regels en subdocumenten die aan een bestaand BO hangen (facturen, begrotingen, formulieren) en geen zelfstandig bedrijfsobject vormen. Daarnaast 13 *classificatie*-entiteiten (referentietabellen/typeringen) en 7 *component*-entiteiten (onderdelen van een groter geheel, zoals Bankafschriftregel, Factuurregel, Bouwdeelelement en MJOP-Item — dit laatste is bij deze beoordeling van detail naar component verplaatst omdat het letterlijk "onderdeel van een MJOP" is). Opvallend binnen ICT is een cluster van vijf UML-metamodelbegrippen — Attribuutsoort, Datatype, Generalisatie, Objecttype en Relatiesoort — die niet over gemeentelijke bedrijfsvoering gaan maar over de typering van het gegevensmodel zelf (stereotypen voor objecten, attributen en relaties). Ze zijn daarom als classificatie behandeld in plaats van detail, ook al hebben ze meer attributen dan een gewone referentietabel; ze horen thuis in de beschrijving van het GGM-metamodel, niet in de bedrijfsobjectenlaag, en zijn terecht geen BO.

**Functionele dekking.** ICT is het enige beleidsdomein in dit taakveld met echte hiaten: 9 van de 35 entiteiten zijn niet aan een BO te herleiden (Aanvraag, CMDB-item, Datatype, Inventaris, Log, Melding, Telefoniegegevens, Toegangsmiddel, Vervoersmiddel). Dit zijn stuk voor stuk objecten uit asset- en facilitair beheer (inventarisregistratie, telefonie, toegangspassen, wagenpark) waarvoor het GGM geen passend bedrijfsobject modelleert — samen de 9 GGM-hiaten van dit taakveld.

Subsidies springt er structureel uit: 9 entiteiten, 0 BO's, maar toch 100% "dekking" — elke entiteit wordt via een relatie naar een BO buiten het domein getraceerd (Medewerker, Kostenplaats, Document, Organisatorische eenheid). Dat is een schijndekking: geen enkel bedrijfsobject vertegenwoordigt het subsidieproces zelf. Met name **Subsidie** (27 attributen), samen met Subsidieaanvraag en Subsidiebeschikking, vormt een herkenbaar aanvraag-beoordeling-toekenning-cluster dat qua gewicht en zelfstandigheid een gemist BO-kandidaat lijkt. Dit wordt hier als vermoedelijke GGM/BO-hiaat gemeld — het entiteitstype is niet buiten de taxonomie gewijzigd, maar nadere beoordeling (bijv. via `/assess-bo Subsidie`) wordt aanbevolen.

**Cross-domein.** Inkoop en Subsidies delen eenzelfde detailpatroon van formulieren (FormulierInhuur, FormulierVerlengingInhuur, StartformulierAanbesteden, Aanvraag Inkooporder) die als detailgegeven bij een bestaand BO horen (Aanbesteding, Inkooporder, Kostenplaats). SelectietabelAanbesteding wijkt hiervan af: met 5 attributen en de functie van een tabel met drempelbedragen en procedures past dit beter bij classificatie (referentietabel) dan bij detail, en is dienovereenkomstig aangepast.

**Naamconflicten/disambiguatie.** Geen nieuwe naamoverlap-issues in de "Entiteiten zonder BO"-tabellen van dit taakveld. Bestaande naamconflicten (Functie/Arbeidsfunctie, Inschrijving/Aanbieding, Storing/Storing (ICT), Project/Archeologisch onderzoek) betreffen alleen de reeds gematchte BO's en zijn daar al zichtbaar in de kolom Naamoverlap.

## Financien

24 entiteiten, 10 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/financien\|Activa]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa\|Activa]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Begroting]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Debiteur]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur\|Debiteur]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Doelstelling]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling\|Doelstelling]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Factuur]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/factuur\|Factuur]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Inkooporder]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder\|Inkooporder]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Kostenplaats]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Product]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product\|Product]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Taakveld]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/taakveld\|Taakveld]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/financien\|Werkorder]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/werkorder\|Werkorder]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/financien\|Activasoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa\|Activa]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/financien\|Bankafschriftregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling\|Betaling]] | Component |
| [[Wiki/GGM/9-interne-organisatie/financien\|Batchregel]] | component | via Batch → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Component |
| [[Wiki/GGM/9-interne-organisatie/financien\|Begrotingregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] | Component |
| [[Wiki/GGM/9-interne-organisatie/financien\|Factuurregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/factuur\|Factuur]] | Component |
| [[Wiki/GGM/9-interne-organisatie/financien\|Bankafschrift]] | detail | via Bankafschriftregel → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling\|Betaling]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/financien\|Bankrekening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling\|Betaling]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/financien\|Batch]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/financien\|Hoofdrekening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa\|Activa]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/financien\|Hoofdstuk]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling\|Doelstelling]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/financien\|Mutatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/financien\|Subrekening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/financien\|Opdrachtgever]] | rol | n.v.t. | Functie/verantwoordelijkheid |
| [[Wiki/GGM/9-interne-organisatie/financien\|Opdrachtnemer]] | rol | n.v.t. | Functie/verantwoordelijkheid |

## HR

31 entiteiten, 11 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/hr\|Beoordeling]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/beoordeling\|Beoordeling]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Declaratie]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/declaratie\|Declaratie]] ✅ | — | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/zorgdeclaratie|Zorgdeclaratie]] | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Dienstverband]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/dienstverband\|Dienstverband]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Disciplinaire Maatregel]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/disciplinaire-maatregel\|Disciplinaire Maatregel]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Formatieplaats]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/formatieplaats\|Formatieplaats]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Functie]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/arbeidsfunctie\|Arbeidsfunctie]] ✅ | synoniem |  | BO hernoemd: Arbeidsfunctie |
| [[Wiki/GGM/9-interne-organisatie/hr\|Sollicitatie]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/sollicitatie\|Sollicitatie]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Vacature]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/vacature\|Vacature]] ✅ | — | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt|Vacature (arbeidsmarkt)]] | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Verlof]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/verlof\|Verlof]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Verzuim]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/verzuim\|Verzuim]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/hr\|Werknemer]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/hr\|Declaratiesoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/declaratie\|Declaratie]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/hr\|KeuzebudgetBestedingsoort]] | classificatie | via KeuzebudgetBesteding → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/hr\|SoortDisciplinaireMaatregel]] | classificatie | typering [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/disciplinaire-maatregel\|Disciplinaire Maatregel]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/hr\|Verlofsoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/verlof\|Verlof]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/hr\|Verzuimsoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/verzuim\|Verzuim]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/hr\|Functiehuis]] | detail | via NormProfiel → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/arbeidsfunctie\|Arbeidsfunctie]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/hr\|GenotenOpleiding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Geweldsincident]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Individueel Keuzebudget]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Inzet]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/dienstverband\|Dienstverband]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|KeuzebudgetBesteding]] | detail | via Individueel Keuzebudget → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/hr\|NormProfiel]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/arbeidsfunctie\|Arbeidsfunctie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Onderwijsinstituut]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Opleiding]] | detail | via GenotenOpleiding → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/hr\|OrganisatorischeEenheidHR]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Relatie]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Rol]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Sollicitant]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Sollicitatiegesprek]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/sollicitatie\|Sollicitatie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/hr\|Uren]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/dienstverband\|Dienstverband]] | Detailgegeven (geassocieerd met BO) |

## ICT

35 entiteiten, 10 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/ict\|Applicatie]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/ict\|Database]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database\|Database]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/ict\|Hardware]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/hardware\|Hardware]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/ict\|Koppeling]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/koppeling\|Koppeling]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/ict\|Licentie]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/licentie\|Licentie]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/ict\|Nertwerkcomponent]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/netwerkcomponent\|Netwerkcomponent]] ✅ | synoniem |  | BO hernoemd: Netwerkcomponent |
| [[Wiki/GGM/9-interne-organisatie/ict\|Server]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/ict\|Software]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/software\|Software]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/ict\|Storing]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/storing-ict\|Storing (ICT)]] ✅ | synoniem |  | BO hernoemd: Storing (ICT) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Wijzigingsverzoek]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/wijzigingsverzoek\|Wijzigingsverzoek]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/ict\|Aanvraag]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Attribuutsoort]] | classificatie | via Objecttype → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Typering/metamodelconcept |
| [[Wiki/GGM/9-interne-organisatie/ict\|CMDB-item]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Classificatie]] | detail | via Gegeven → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Datatype]] | classificatie | ⚠️ geen BO bereikbaar | Typering/metamodelconcept |
| [[Wiki/GGM/9-interne-organisatie/ict\|Dienst]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Domein/Taakveld]] | detail | via Dienst → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Externe Bron]] | detail | via Gegeven → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Gegeven]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Generalisatie]] | classificatie | via Objecttype → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Typering/metamodelconcept |
| [[Wiki/GGM/9-interne-organisatie/ict\|Inventaris]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Linkbaar CMDB-item]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/koppeling\|Koppeling]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Log]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Melding]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Notitie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Objecttype]] | classificatie | via Gegeven → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Typering/metamodelconcept |
| [[Wiki/GGM/9-interne-organisatie/ict\|Onderwerp]] | detail | via Dienst → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Package]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Prijzenboek]] | detail | via Product → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Product]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Relatiesoort]] | classificatie | via Objecttype → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Typering/metamodelconcept |
| [[Wiki/GGM/9-interne-organisatie/ict\|Telefoniegegevens]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Toegangsmiddel]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Versie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/ict\|Vervoersmiddel]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |

## Inkoop

20 entiteiten, 7 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Aanbesteding]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Contract]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract\|Contract]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Gunning]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/gunning\|Gunning]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Inkooppakket]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/inkooppakket\|Inkooppakket]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Inschrijving]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbieding\|Aanbieding]] ✅ | synoniem | [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/opleidingsinschrijving|Opleidingsinschrijving]] | BO hernoemd: Aanbieding |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Leverancier]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Offerte]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/offerte\|Offerte]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Aanbesteding Inhuur]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/gunning\|Gunning]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Aankondiging]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] | GGM-component van Aanbesteding |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Aanvraag Inkooporder]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder\|Inkooporder]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|CPV-code]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/inkooppakket\|Inkooppakket]] | EU-referentietabel, geen gemeentelijk object |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Categorie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|FormulierInhuur]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|FormulierVerlengingInhuur]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder\|Inkooporder]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Kandidaat]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/gunning\|Gunning]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Kwalificatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Offerteaanvraag]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] | GGM-component van Aanbesteding |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|SelectietabelAanbesteding]] | classificatie | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|StartformulierAanbesteden]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/inkoop\|Uitnodiging]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | Detailgegeven (geassocieerd met BO) |

## Organisatie-indeling

2 entiteiten, 1 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/organisatie-indeling\|Project]] | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologisch-onderzoek\|Archeologisch onderzoek]] ✅ | synoniem |  | BO hernoemd: Archeologisch onderzoek |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/organisatie-indeling\|Programma]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/bouwen-en-wonen/woningbouwplan\|Woningbouwplan]] | Component van [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] |

## Subsidies

9 entiteiten, 0 Entiteiten met BO.

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Betaalmoment]] | detail | via Subsidiecomponent → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Rapportagemoment]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Sector]] | detail | via Subsidie → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Subsidie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Subsidieaanvraag]] | detail | via Subsidie → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Subsidiebeschikking]] | detail | via Subsidie → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Subsidiecomponent]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Subsidieprogramma]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/subsidies\|Taak]] | detail | via Subsidie → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Detailgegeven (weinig attributen) |

## Vastgoed

27 entiteiten, 5 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|MJOP]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Vastgoed Contract]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] ✅ | synoniem |  | BO hernoemd: Vastgoedcontract |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Vastgoedobject]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] ✅ | — |  | Exact match |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Verhuurbaar Eenheid]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/verhuurbare-eenheid\|Verhuurbare Eenheid]] ✅ | synoniem |  | BO hernoemd: Verhuurbare Eenheid |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Werkbon]] | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/werkbon\|Werkbon]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Eigenaar]] | actor | n.v.t. | Rol/generalisatie van Rechtspersoon |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Huurder]] | actor | n.v.t. | Rol/generalisatie van Rechtspersoon |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Locatieonroerendezaak]] | classificatie | via AdresseerbaarObject → [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | Typering/referentietabel |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Bouwdeelelement]] | component | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/werkbon\|Werkbon]] | Component |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Vastgoedcontractregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] | Component |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Aanbesteding Vastgoed]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Adresaanduiding]] | detail | via KadastraleOnroerendeZaak → [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Bouwdeel]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | GGM-component van Vastgoedobject |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|CultuurOnbebouwd]] | detail | via KadastraleOnroerendeZaak → [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Gebruiksdoel]] | detail | ⚠️ geen BO bereikbaar | attribuut |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Inspectie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|KpBetrokkenBij]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|KpOnstaanUit]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|LocatieaanduidingWozObject]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Detailgegeven |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|MJOP-Item]] | component | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | Component |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|NADAanvullingBRP]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Objectrelatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Offerte]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/offerte\|Offerte]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Pachter]] | detail | via Rechtspersoon → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Prijzenboekitem]] | detail | via MJOP-Item → [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|WOZ-Belang]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/9-interne-organisatie/vastgoed\|Zakelijk Recht]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | Detailgegeven (geassocieerd met BO) |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/algemeenbelangbesluit\|Algemeenbelangbesluit]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/dataproduct\|Dataproduct]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/detacheringsovereenkomst\|Detacheringsovereenkomst]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/financiele-voorziening\|Financiële Voorziening]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/jaarrekening\|Jaarrekening]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/marktconsultatie\|Marktconsultatie]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve\|Reserve]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/sla\|Service Level Agreement]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/verbonden-partij\|Verbonden Partij]] | nee | procesobject | **Alleen GEMMA-BO** |
