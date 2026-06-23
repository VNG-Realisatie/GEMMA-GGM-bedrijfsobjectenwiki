---
type: analyse
titel: "GGM-dekking: welke beleidsdomeinen hebben bronnen, welke niet"
datum: 2026-06-23
source: "Coverage uit alle wiki-domeinen"
---

# GGM-dekking per beleidsdomein

Overzicht van GGM-entiteiten per beleidsdomein, ingedeeld naar:
- **BO**: bedrijfsobjecten (GGM-entiteiten die in wiki als BO zijn vastgelegd)
- **Niet-BO**: beoordeelde GGM-entiteiten die geen BO zijn (te granulair, classificaties, operationeel)
- **Niet beoordeeld**: GGM-entiteiten zonder beleidsbron (dus nog niet beoordeeld; potentiële toekomstige BO's)

**Waarom centraal, niet per wiki-domein:** GGM-beleidsdomeinen en wiki-domeinen lopen niet 1-op-1. Een wiki-domein kan meerdere GGM-beleidsdomeinen raken (bijv. cultuur → Monumenten + Archief + Archeologie + Musea). Dit overzicht werkt vanuit de GGM-structuur en maakt per beleidsdomein zichtbaar:
- **Bronnen**: aantal verwerkte bronsamenvattingen dat dit beleidsdomein raakt (geeft aan of er voldoende materiaal is om entiteiten te beoordelen)
- **Wiki-domein(en)**: welke wiki-domeinen dit domein afdekken (navigeerbaar)
- **Reden niet beoordeeld**: waarom entiteiten nog niet zijn beoordeeld (geen bron, procesobject, ander subdomein, etc.)

## GGM-entiteitendekking per beleidsdomein

| Taakveld | Beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld | Wiki-domein(en) | Bronnen |
|:--------:|:-------------:|:----------:|:--:|:-------:|:---------------:|:---------------------:|:----------------:|:-------:|
| 0 | Politiek/Bestuur | Verkiezing, Referendum, Stembureau, Gemeenschappelijke Regeling | 0 | 0 | 4 | Procesobjecten en governance-objecten buiten GGM-scope | [[Wiki/Domeinen/bestuur\|bestuur]] | — |
| 1 | Model VTH | OpenbareActiviteit + 29 overige VTH-entiteiten | 1 | 0 | 29 | Alleen OpenbareActiviteit relevant; overige VTH-entiteiten buiten scope evenementen | [[Wiki/Domeinen/evenementen\|evenementen]] | — |
| 2 | Mobiliteit | OVChauffeursGroep, OVLijn, OVStopplaats, Route, Routetraject, Tramroute, Tram(lijn) + 4 overige | 4 | 7 | 0 | — | [[Wiki/Domeinen/mobiliteit\|mobiliteit]] | 13 |
| 2 | Parkeren | Naheffing, Parkeerrecht, Parkeervergunning, Parkeerzone, Parkeervlak + 10 overige | 9 | 6 | 0 | — | [[Wiki/Domeinen/mobiliteit\|mobiliteit]] | 13 |
| 3 | Taakveld 3 Economie | Hotel, Hotelbezoek, Vestiging + 3 overige | 1 | 0 | 5 | Hotel → BO; Hotelbezoek → meting; Vestiging → werklocatie | [[Wiki/Domeinen/economie\|economie]] | 10 |
| 4 | Onderwijs | Leerling, Leraar, Mentor, Klasse, Schema, Schooljaar + 6 overige | 5 | 7 | 0 | — | [[Wiki/Domeinen/onderwijs\|onderwijs]] | 4 |
| 4 | Leerplicht en Leerlingenvervoer | Vervoerroute, Vervoervoertuig, Concessie, Leerlingvervoerder + 11 overige | 5 | 10 | 0 | — | [[Wiki/Domeinen/onderwijs\|onderwijs]] | 4 |
| 5 | Monumenten | Monument, BeschermdeStatus + 4 overige | 1 | 5 | 0 | — | [[Wiki/Domeinen/cultuur\|cultuur]], [[Wiki/Domeinen/welstand\|welstand]] | 10 |
| 5 | Archief | ArchiefrepertoireMap, Archiefopstelling, Archiefagenda + 5 overige | 1 | 3 | 4 | Geen beleidsbron over archieflogistiek | [[Wiki/Domeinen/cultuur\|cultuur]] | 10 |
| 5 | Archeologie | ArcheologischWerkstuk, ArcheologischeVondst, Opgraving + 14 overige | 3 | 14 | 0 | Volledig beoordeeld o.b.v. erfgoednota Utrecht | [[Wiki/Domeinen/cultuur\|cultuur]] | 10 |
| 5 | Generiek Erfgoed | Erfgoedwaarde, Objecttype + 2 overige | 0 | 1 | 3 | Abstract parent-entiteit | [[Wiki/Domeinen/cultuur\|cultuur]] | 10 |
| 5 | Musea | MuseumExhibitie, Kunstwerk, Expositie + 29 overige | 1 | 9 | 22 | Prinsenhof-specifieke entiteiten; geen museale beleidsbron | [[Wiki/Domeinen/cultuur\|cultuur]] | 10 |
| 5 | Sport | Sportaccommodatie, Sportterrein, Sporthal, Zwembad + 9 overige | 6 | 5 | 2 | Bezetting en Onderhoudskosten: meetwaarde/financieel | [[Wiki/Domeinen/sport-en-bewegen\|sport-en-bewegen]] | 2 |
| 5 | Model VTH (Welstand) | 30 VTH-entiteiten | 0 | 0 | 30 | Geen VTH-specifieke bronnen verwerkt | [[Wiki/Domeinen/welstand\|welstand]] | 2 |
| 5 | Monumenten (Welstand) | Monument, BeschermdeStatus + 4 overige | 1 | 0 | 5 | Classificaties bij Beschermde Status | [[Wiki/Domeinen/welstand\|welstand]] | 2 |
| 6 | Inburgering | InburgeringCursus, Inburgeringcertificaat, Leerprogramma + 32 overige | 13 | 18 | 4 | Volledige GGM-dekking voor inburgering | [[Wiki/Domeinen/inburgering-en-asielopvang\|inburgering-en-asielopvang]] | 1 |
| 6 | Asielopvang | — | 2 | 0 | 0 | GGM-hiaat: geen dekking voor asielopvang | [[Wiki/Domeinen/inburgering-en-asielopvang\|inburgering-en-asielopvang]] | 1 |
| 6 | Generiek Jeugd en Wmo | Programmabudget, Zorgmelding, Ondersteuningsplan + 24 overige | 5 | 8 | 14 | Classificatie-entiteiten en financieel-administratief | [[Wiki/Domeinen/maatschappelijke-ondersteuning\|maatschappelijke-ondersteuning]] | 1 |
| 6 | Sociaal Domein Generiek | Inkomenscomponent (33x), Regelgeving, Uitkering + 20 overige | 1 | 5 | 50 | Groot deel Inkomen-domein; 33 inkomstencomponenten | [[Wiki/Domeinen/maatschappelijke-ondersteuning\|maatschappelijke-ondersteuning]] | 1 |
| 6 | Sociale Teams | Zorgmelding, Buurtteam, Preventief + 6 overige | 1 | 0 | 8 | Operationele entiteiten | [[Wiki/Domeinen/maatschappelijke-ondersteuning\|maatschappelijke-ondersteuning]] | 1 |
| 6 | Jeugdbescherming en reclassering | Reclassering, Toezicht, Vaststellingsbesluit + 1 overige | 1 | 0 | 3 | Ondersteunend bij Zorgmelding | [[Wiki/Domeinen/maatschappelijke-ondersteuning\|maatschappelijke-ondersteuning]] | 1 |
| 6 | Dak- en thuislozen | Opvangplek | 1 | 0 | 0 | — | [[Wiki/Domeinen/maatschappelijke-ondersteuning\|maatschappelijke-ondersteuning]] | 1 |
| 6 | Generiek Jeugd en Wmo (Sociaal Domein) | 27 entiteiten | 0 | 0 | 27 | Wmo/Jeugd-beleid nog niet als eigen bron verwerkt | [[Wiki/Domeinen/sociaal-domein\|sociaal-domein]] | 1 |
| 6 | Sociale Teams (Sociaal Domein) | 9 entiteiten | 0 | 0 | 9 | Buurtteams nog niet als eigen bron verwerkt | [[Wiki/Domeinen/sociaal-domein\|sociaal-domein]] | 1 |
| 6 | Sport (Sociaal Domein) | Sportaccommodatie (Binnenlocatie), Sportpark + 11 overige | 2 | 0 | 11 | Subtypes Binnenlocatie, Sportpark | [[Wiki/Domeinen/sociaal-domein\|sociaal-domein]] | 1 |
| 6 | Onderwijs (Sociaal Domein) | School (subtype) + 11 overige | 1 | 0 | 11 | Subtype School | [[Wiki/Domeinen/sociaal-domein\|sociaal-domein]] | 1 |
| 6 | Dak- en thuislozen (Sociaal Domein) | Opvangplek | 0 | 0 | 1 | Opvangbeleid nog niet als eigen bron verwerkt | [[Wiki/Domeinen/sociaal-domein\|sociaal-domein]] | 1 |
| 6 | Terug- en invordering | Terugvordering, Invorderingszaak, Dwangmiddel, Invorderingskosten + 3 overige | 7 | 0 | 0 | **100% GGM-dekking** | [[Wiki/Domeinen/terug-en-invordering\|terug-en-invordering]] | 1 |
| 7 | Afval | AfvalContainer, Afvalroute, Inzameling + 11 overige | 4 | 12 | 0 | — | [[Wiki/Domeinen/milieu\|milieu]] | 1 |
| 7 | Afval (Dierenwelzijn) | 14 entiteiten | 0 | 0 | 14 | Ander subdomein; geen beleidsbron over afvalbeheer | [[Wiki/Domeinen/dierenwelzijn\|dierenwelzijn]] | — |
| 7 | Afval (Energie en Klimaat) | 14 entiteiten | 0 | 0 | 14 | Ander subdomein; geen beleidsbron over afvalbeheer | [[Wiki/Domeinen/energie-en-klimaat\|energie-en-klimaat]] | 7 |
| 7 | Beheer Openbare Ruimte (Geluid) | Geluidsscherm (1 relevant van 82) | 1 | 0 | 81 | Overige BOR-entiteiten buiten scope geluidbeleid | [[Wiki/Domeinen/geluid\|geluid]] | 2 |
| 7 | Omgevingswet (Geluid) | 31 entiteiten (geluidnormen) | 0 | 0 | 31 | Geluidnormen zijn geen apart BO | [[Wiki/Domeinen/geluid\|geluid]] | 2 |
| 7 | Beheer Openbare Ruimte (Openbare Gezondheid) | Begraafplaats | 0 | 1 | 0 | Begraafplaats hoort bij BOR | [[Wiki/Domeinen/openbare-gezondheid\|openbare-gezondheid]] | — |
| 8 | Beheer Openbare Ruimte | Boom, Groen, Verhardingelement, Verlichtingsmast + veel subentiteiten (200 totaal) | 9 | 0 | 191 | Subdomeinen: bomen, groen, verhardingen, civiele constructies, verlichting, VRI, speeltoestellen; water, riolering, kabels/leidingen, sensoren nog open | [[Wiki/Domeinen/beheer-openbare-ruimte\|beheer-openbare-ruimte]] | 1 |
| 8 | Bouwen en Wonen | Bouwwerk, Bouwdeelnaam, Bouwactie + 4 overige | 2 | 3 | 2 | Projectleider/Projectontwikkelaar zijn actoren | [[Wiki/Domeinen/wonen\|wonen]] | 2 |
| 8 | VTH (Vaartuig) | Woonboot | 1 | 0 | 0 | Vaartuig → Woonboot | [[Wiki/Domeinen/wonen\|wonen]] | 2 |
| 8 | BAG (Ligplaats) | Ligplaats | 1 | 0 | 0 | Ligplaats exact match | [[Wiki/Domeinen/wonen\|wonen]] | 2 |
| 8 | Omgevingswet (Gevaarlijke Stoffen) | 34 entiteiten | 0 | 0 | 34 | 3 BO's matchen partieel op Gebiedsaanwijzing, Activiteit | [[Wiki/Domeinen/gevaarlijke-stoffen\|gevaarlijke-stoffen]] | 1 |
| 9 | HR | Medewerker, Arbeidscontract, Betrokkenheid, Functie + 27 overige | 11 | 20 | 0 | — | [[Wiki/Domeinen/arbeidszaken\|arbeidszaken]] | 3 |
| 9 | Taakveld 9 Interne Organisatie / Financien | Rekeningkost, Begrotingsfase, Budgetregel, Budget + 20 overige | 10 | 0 | 14 | Boekhoudkundige kern goed gedekt | [[Wiki/Domeinen/financien\|financien]] | 4 |
| 10 | Model Dienstverlening | DienstverleningsProduct, KwaliteitsIndicator + 14 overige | 3 | 9 | 4 | Operationeel/kwaliteitsregistratie | [[Wiki/Domeinen/dienstverlening\|dienstverlening]] | 2 |
| 10 | RGBZPlus | Dossiercomponent, Dossier, Betrokken Partij + 22 overige | 2 | 23 | 0 | — | [[Wiki/Domeinen/dienstverlening\|dienstverlening]] | 2 |
| 99 | RSGBPlus (99 Kern) | WOZ-object, WOZ-Waarde (+ WOZ-deelobject, SoortWOZObject) | 2 | 0 | 0 | — | [[Wiki/Domeinen/belastingen\|belastingen]] | 1 |
| 99 | Vastgoed (9 Int. Org.) | WOZ-Belang, LocatieaanduidingWozObject | 0 | 2 | 0 | Technische tussenentiteiten | [[Wiki/Domeinen/belastingen\|belastingen]] | 1 |
| 99 | Financien (9 Int. Org.) | Debiteur, Kostenplaats | 1 | 1 | 0 | Debiteur → BO; Kostenplaats is ondersteunend | [[Wiki/Domeinen/belastingen\|belastingen]] | 1 |
| 99 | Parkeren (2 V&V) | Naheffing, Parkeerrecht, Parkeervergunning, Parkeerzone, Parkeervlak | 3 | 2 | 0 | — | [[Wiki/Domeinen/belastingen\|belastingen]] | 1 |
| 99 | VTH (1 Veiligheid) | Heffing, Heffingsverordening, Heffinggrondslag, Precario | 2 | 2 | 0 | Heffing en Heffingsverordening → BO | [[Wiki/Domeinen/belastingen\|belastingen]] | 1 |

## Samenvattende statistieken

**Geanalyseerd:** 24 wiki-domeinen, 48 beleidsdomeinen
- **Totale GGM-entiteiten**: 922
- **Bedrijfsobjecten (BO's)**: 122 (13,2%)
- **Niet-BO's**: 173 (18,8%)
- **Niet beoordeeld**: 627 (68%)

### Volledig GGM-gedekte beleidsdomeinen (100% beoordeeld)

- **Taakveld 2:** Mobiliteit (4 BO's), Parkeren (9 BO's)
- **Taakveld 6:** Asielopvang (2 BO's), Dak- en thuislozen (1 BO), Terug- en invordering (7 BO's)
- **Taakveld 8:** BAG/Ligplaats (1 BO), VTH/Vaartuig (1 BO)
- **Taakveld 10:** RGBZPlus (2 BO's)

### Beleidsdomeinen zonder bronnen

Geen huidige wiki-bronnen beschikbaar:

- Taakveld 0: Politiek/Bestuur
- Taakveld 1: Model VTH (evenementen)
- Taakveld 7: Afval (Dierenwelzijn), Beheer Openbare Ruimte (Openbare Gezondheid)
- Taakveld 8: (alle hebben bronnen)
- Taakveld 10: (beide hebben bronnen)

Dit zijn kandidaten voor toekomstige bronnenverzamelingen.

### Opvallende hiaten

| Taakveld | Beleidsdomein | Issue | Impact |
|:--------:|:-------------:|:-----:|:------:|
| 1 | Evenementen (Model VTH) | Slechts 1 van 30 entiteiten relevant | Te veel overhead voor evenementen-specifieke objecten |
| 5 | Welstand (Model VTH) | 30 VTH-entiteiten niet beoordeeld | Geen welstand-specifieke beleidsbronnen verwerkt |
| 5 | Musea | 22 van 32 entiteiten niet beoordeeld | Prinsenhof-specifieke entiteiten; geen generieke museale beleidsbronnen |
| 6 | Sociaal Domein (Inkomenscomponent) | 50 van 56 inkomenscomponenten niet beoordeeld | Inkomensdomein nog niet volledig vanuit bronnen ingesteld |
| 7 | Milieu & Omgeving | Dierenwelzijn, Energie/Klimaat geen beleidsdomeinen | Structureel hiaat GGM |
| 8 | Beheer Openbare Ruimte | 191 van 200 entiteiten niet beoordeeld | Water, riolering, kabels/leidingen, sensoren nog open |

## Actielijst: waar moeten beleidsdocumenten gezocht worden?

Beleidsdomeinen met 0 bronnen en veel niet-beoordeelde entiteiten zijn prioritair:

1. **Taakveld 0**: Bestuur/Politiek-beleidsdocumenten
2. **Taakveld 7**: Dierenwelzijn-specifieke beleidsnota's, Energie/Klimaat-specifieke documenten
3. **Taakveld 5**: Welstand-specifieke bronnen voor VTH-matching
4. **Taakveld 8**: Water-, riolerings-, kabelgebruik -specifieke beleidsdocumenten voor BOR-detailniveaus
5. **Taakveld 6**: Wmo/Jeugd-beleidsnota's, Sociale Teams-beleidsraamwerk
