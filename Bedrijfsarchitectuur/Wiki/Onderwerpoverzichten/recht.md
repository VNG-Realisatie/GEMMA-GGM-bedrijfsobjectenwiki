---
type: onderwerp
naam: Recht
status: afgerond
verwerkingsdatum: 2026-09-23
bronnen_count: 4
begrippen_count: 10
bo_count: 3
---

# Recht

## Beschrijving

Gemeentelijk onderwerp dat de juridische kaders bestrijkt waarbinnen gemeenten opereren: bestuursrecht, gemeentelijke organisatie, modelverordeningen, overheidsprivaatrecht (overeenkomsten, aansprakelijkheid) en subsidierecht. De bronnen zijn korte VNG-rubriekpagina's die doorverwijzen naar specifiekere kennisbanken (KDER, MDR) en portals.

Het merendeel van de bronnen is portaal-achtig en te dun om inhoudelijk te beoordelen. Eén bron (subsidierecht) legde een al gesignaleerde hiaat bloot: het GGM-beleidsdomein Subsidies (taakveld 9 Interne Organisatie) had ondanks rijke modellering nog geen enkel bedrijfsobject.

## Begrippentabel

| Begrip | Begripstype | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidie\|Subsidie]] | object | Aan derden toegekende financiële middelen voor het uitvoeren van activiteiten | ✅ | ja | 6/6 criteria, exact match | Partijsubsidie, loonkostensubsidie, cultuursubsidie | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidieaanvraag\|Subsidieaanvraag]] | object | Aanvraag van een (rechts)persoon voor een subsidie | ✅ | ja | 6/6 criteria, exact match | Schriftelijke/digitale subsidieaanvraag | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidiebeschikking\|Subsidiebeschikking]] | object | Besluit over het al dan niet toekennen van een subsidie | ✅ | ja | 6/6 criteria, exact match | Toekenningsbeschikking, afwijzingsbeschikking | ja |
| Model Algemene subsidieverordening (ASV) | governance-instrument | VNG-modelverordening voor subsidieverstrekking | ❌ | nee | Juridisch kader, geen zelfstandig object | ASV gemeente X | nee |
| Subsidieprogramma | object | Programma waarin meerdere subsidies vanuit samenhang worden verleend | ❌ | ja | GGM-entiteit gesignaleerd, geen brongrond in deze ingest | — | ja (niet beoordeeld) |
| Subsidiecomponent | object | Financiële deelcomponent van een subsidie (koppeling betaalmoment/kostenplaats) | ❌ | ja | GGM-entiteit gesignaleerd, geen brongrond in deze ingest | — | ja (niet beoordeeld) |
| Subsidieniveau | — | Enumeratie/classificatiewaarde van Subsidie | ❌ | nee | GGM-enumeratie, attribuutwaarde | Rijk, provincie, gemeente | ja (niet beoordeeld) |
| Overeenkomst (generiek) | object | Contractuele afspraak tussen gemeente en wederpartij | ❌ | ja | Al gedekt per contractsoort ([[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract\|Contract]], vastgoedcontract, detacheringsovereenkomst) | Contract, vastgoedcontract | ja (via specifieke entiteiten) |
| GIBIT | governance-instrument | Gemeentelijke inkoopvoorwaarden voor ICT-contracten | ❌ | nee | Al uitgebreid geïngest onder onderwerp Informatiesystemen, zie [[Wiki/Bronsamenvattingen/informatiesystemen/gibit-2025\|GIBIT 2025]] | GIBIT 2025 | nee |
| Onrechtmatige daad / causaal verband / relativiteit / formele rechtskracht | thema | Juridische toetsingscriteria uit het aansprakelijkheidsrecht | ❌ | nee | Beoordelingscriteria, geen registreerbaar object | — | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Recht/subsidierecht|Subsidierecht]]
- [[Wiki/Bronsamenvattingen/Recht/overeenkomsten|Overeenkomsten]]
- [[Wiki/Bronsamenvattingen/Recht/overheidsaansprakelijkheid|Overheidsaansprakelijkheid]]
- [[Wiki/Bronsamenvattingen/Recht/gemeentewet|Gemeentewet (VNG-rubriek)]] — inhoudelijk al gedekt door [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst|Gemeentewet — wettekst]] (Bestuur-domein)

5 bronnen zijn te dun bevonden voor een bronsamenvatting en verplaatst naar `Sources/Onderwerpen/Recht/Niet-relevant/`: algemene-wet-bestuursrecht-awb, algemene-plaatselijke-verordening-apv, modelverordeningen, rubriek-recht, portal-overheidsprivaatrecht.

## Openstaande vragen of hiaten

- **Subsidieprogramma, Subsidiecomponent, Subsidieniveau**: GGM-entiteiten in het beleidsdomein Subsidies zonder brongrond in deze ingest. Kandidaat voor een toekomstige, rijkere subsidierecht-bron (bijv. Model ASV-wettekst of Awb titel 4.2), analoog aan hoe de Gemeentewet-rubriekpagina werd aangevuld met de volledige wettekst.
- **GIBIT**: deze bron noemt het slechts terzijde (één zin); het instrument zelf is al rijk geïngest onder onderwerp Informatiesystemen ([[Wiki/Bronsamenvattingen/informatiesystemen/gibit-2025|GIBIT 2025]]) — geen dubbele beoordeling nodig.

## Terugmeldingen richting GGM

Geen formele terugmeldingen. Bij [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidiebeschikking|Subsidiebeschikking]] is ter context gedocumenteerd dat de generieke GGM-entiteit "Beschikking" ook voorkomt in de beleidsdomeinen Generiek Jeugd en Wmo en Diensten — geen naamcollisie (de entiteitnamen verschillen) en dus geen homoniem in formele zin, geen actie nodig.
