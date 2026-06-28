---
type: bronsamenvatting
titel: Gemeenschappelijk Informatiemodel Zorg & Ondersteuning (GIZO)
onderwerp: [Maatschappelijke Ondersteuning]
datum_ingest: 2026-06-27
---

## Samenvatting

Eerste conceptversie van het Gemeenschappelijk Informatiemodel Zorg & Ondersteuning (GIZO), opgesteld door team Gegevensuitwisseling in de Zorg (GidZ) van Zorginstituut Nederland in samenwerking met het GGM-team en het Ketenbureau i-Sociaal Domein (21 november 2025). Het model beschrijft op conceptueel niveau de betekenis van en samenhang tussen gegevens die binnen iStandaarden (iWmo, iJw, iEb) worden uitgewisseld. Het doel is relaties leggen met het Gemeentelijk Gegevensmodel (GGM).

Het GIZO kent zes deelmodellen:

**Overzicht:** De kernentiteiten en hun relaties: Gemeente, [[Client]], [[Toewijzing]], [[Levering]], Declaratie, Verzoek, Eigen bijdrage, Aanbieder, CAK. Client valt onder verantwoordelijkheid van Gemeente; Toewijzing is opdracht tot levering; Levering wordt geleverd aan Client; Declaratie wordt door Aanbieder samengesteld; Eigen bijdrage wordt opgelegd aan Client en vastgesteld door CAK.

**Client:** Client (bsn, communicatie) komt overeen met GGM Client (NatuurlijkPersoon, NietNatuurlijkPersoon). Heeft Relatie, Gezagsdrager, Contactgegevens, Juridische status. Wettelijke verwijzing bepaalt het recht op zorg. [[Beschikking]] (beschikkingsnummer, ingangsdatum) wordt door Gemeente afgegeven.

**Toewijzing:** [[Toewijzing]] (toewijzingnummer, datum, tijd, ingangsdatum, einddatum[0..1], budget[0..1]) bevat Toegewezen product (productcategorie, productcode[0..1]) met Omvang (volume, eenheid, frequentie). Verzoek (referentienummer) leidt tot Toewijzing; Reden wijziging toewijzing registreert waarom gewijzigd. Regels: als Toewijzing een Toegewezen product met productcategorie of code bevat, moet het Product een Omvang bevatten; als Toewijzing een budget bevat, mag Toegewezen product alleen een productcategorie bevatten.

**Verzoek:** Verzoek om toewijzing en Verzoek om wijziging zijn specialisaties van Verzoek. Aanbieder doet het verzoek; Gemeente geeft antwoord (Verzoek antwoord: antwoord, reden afwijzing). Verwijzer (type, naam, agb-code) geeft de wettelijke verwijzing. Aangevraagd product (productcategorie, productcode) met Aangevraagde toewijzingsperiode (gewenste ingangsdatum, gewenste einddatum).

**Levering:** [[Levering]] (startdatum[1..*], stopdatum[0..*]) wordt geleverd aan Client op basis van Toewijzing. Kan meerdere start- en stopdatums hebben (tijdelijke beëindiging en hervatting). Reden beëindigen levering registreert de stopreden. Gerelateerd aan Periode eigen bijdrage abonnementstarief en Periode eigen bijdrage beschermd wonen.

**Declaratie:** Declaratie (declaratienummer, declaratieperiode, ingediend totaalbedrag, dagtekening) wordt door Aanbieder samengesteld en is bestemd voor Gemeente. Bevat Prestatie (ingediend bedrag, productperiode, debet of credit, geleverd product, geleverde omvang). Productperiode past binnen Levering. DeclaratieAntwoord (totaal toegekend bedrag) is antwoord van Gemeente. Productafspraak (producttarief, uitvoeringsvariant) is de contractuele afspraak tussen Gemeente en Aanbieder.

**Eigen bijdrage:** Gemeente bepaalt welke producten eigen-bijdrageplichtig zijn. Eigen bijdrage wordt opgelegd aan [[Client]] en vastgesteld door CAK. Twee periodetypen: Periode eigen bijdrage abonnementstarief en Periode eigen bijdrage beschermd wonen (elk met startdatum, stopdatum). Kostprijs (bedrag, startdatum) hoort bij Wmo hulpmiddel of woningaanpassing.

## Kernbegrippen

- **[[Client]]** — bsn, communicatie; komt overeen met GGM Client/NatuurlijkPersoon/NietNatuurlijkPersoon
- **[[Beschikking]]** — beschikkingsnummer, ingangsdatum; afgegeven door Gemeente
- **[[Toewijzing]]** — toewijzingnummer, datum, ingangsdatum, einddatum, budget; bevat Toegewezen product met Omvang
- **[[Levering]]** — startdatum, stopdatum; kan meerdere start/stops hebben (tijdelijke beëindiging)
- **Declaratie** — declaratienummer, declaratieperiode, ingediend totaalbedrag, dagtekening; door Aanbieder, bestemd voor Gemeente
- **Prestatie/Declaratieregel** — ingediend bedrag, productperiode, debet/credit, geleverd product, geleverde omvang; onderdeel van Declaratie
- **Eigen bijdrage** — eigen bijdrage opgelegd aan Client, vastgesteld door CAK; twee periodetypen
- **Toegewezen product** — productcategorie, productcode; onderdeel van Toewijzing
- **Omvang** — volume, eenheid, frequentie; hoeveelheid bij product
- **Verzoek om toewijzing / Verzoek om wijziging** — specialisaties van Verzoek; door Aanbieder
- **Productafspraak** — producttarief, uitvoeringsvariant; contractuele afspraak Gemeente–Aanbieder
- **Verwijzer** — type, naam, agb-code; partij die wettelijke verwijzing afgeeft

## Relevantie voor bedrijfsarchitectuur

Het GIZO is de eerste poging om de concepten achter het iWmo/iJw/iEb-berichtenverkeer als conceptueel informatiemodel vast te leggen, expliciet afgestemd op het GGM. Dit maakt het bijzonder relevant:

1. **Bevestiging bestaande BO's:** Client, Beschikking, Toewijzing en Levering worden als kernentiteiten bevestigd met attributen en relaties die overeenkomen met de GGM-modellering.
2. **Herbeoordeling Declaratie:** Het GIZO modelleert Declaratie als first-class entiteit met eigen attributen en relatie tot Prestatie. Het GGM heeft eveneens Declaratie en Declaratieregel als Classes. Dit geeft aanleiding tot herbeoordeling als BO.
3. **Nieuwe BO-kandidaat Eigen bijdrage:** Expliciet gemodelleerd met relaties naar Client, Toewijzing, CAK en twee periodetypen. Het GGM heeft Eigen bijdrage als Class in Sociaal Domein Generiek.
4. **Procescontext:** Het model verduidelijkt de relaties tussen entiteiten (Toewijzing bevat Toegewezen product met Omvang; Levering kan meerdere start/stops hebben; Declaratie bevat Prestaties).
5. **GGM-aansluiting:** Diverse entiteiten verwijzen expliciet naar GGM-Classes (Client, NatuurlijkPersoon, NietNatuurlijkPersoon, Beschikking, Gemeente). De aansluiting is nog in uitwerking.

> "Het model is opgesteld door team Gegevensuitwisseling in de Zorg (GidZ) van Zorginstituut Nederland, in samenwerking met het Gemeentelijk Gegevensmodel (GGM) en het Ketenbureau."

> "Een Levering is alle ondersteuning die geleverd wordt op basis van een Toewijzing. Daarmee kan een Levering meerdere start- en stopdatums hebben."

> "Een toewijzing is altijd voor 1 cliënt, daarmee voor dit model de levering ook. In praktijk komen ook gezinsgerichte producten voor die geleverd worden. Deze situaties zijn buiten scope van dit model."

## Bronnen

- [[Sources/Onderwerpen/Maatschappelijke Ondersteuning/informatiemodel-gizo-concept]]
