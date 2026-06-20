---
type: domein
naam: Economie
status: in-behandeling
verwerkingsdatum: 2026-06-20
bronnen_count: 3
begrippen_count: 14
bo_count: 3
---

# Domein: Economie

Gemeentelijk beleid gericht op economische ontwikkeling, bedrijvigheid en ondernemerschap. Gemeenten zijn de "eerste overheid" voor ondernemers en spelen een rol als aanjager van economische transities, ruimtelijke facilitator en dienstverlener.

## GGM-taakveld

Taakveld 3 "Economie", beleidsdomein "Model Economie". Het GGM-model is zeer beperkt: 6 entiteiten zonder definities, gericht op hotel/retail-statistieken rond Vestiging (RSGB). Zie `Sources/GGM/economie.md`.

## Begrippen

### Normatief
- [[Wiki/Begrippen/brede-welvaart|brede-welvaart]] — maatschappelijk welzijn voorbij economische groei (waarde)

### Strategisch
- [[Wiki/Begrippen/vestigingsklimaat|vestigingsklimaat]] — aantrekkelijkheid gemeente/regio voor bedrijfsvestiging (doel)
- [[Wiki/Begrippen/arbeidsmarkt|arbeidsmarkt]] — vraag en aanbod van arbeid, regionaal perspectief (thema)
- [[Wiki/Begrippen/human-capital|human-capital]] — menselijk kapitaal, vaardigheden en inzetbaarheid (thema)

### Tactisch
- [[Wiki/Begrippen/ondernemersdienstverlening|ondernemersdienstverlening]] — gemeentelijke dienstverlening aan ondernemers (thema)
- [[Wiki/Begrippen/regeldruk|regeldruk]] — ervaren last van regelgeving voor ondernemers (thema)
- [[Wiki/Begrippen/economische-ruimte|economische-ruimte]] — fysieke ruimte beschikbaar voor bedrijvigheid (thema)
- [[Wiki/Begrippen/midden-en-kleinbedrijf|midden-en-kleinbedrijf]] — bedrijven tot 250 werknemers, ~60% werkgelegenheid (doelgroep)

### Operationeel
- [[Wiki/Begrippen/werklocatie|werklocatie]] — fysieke locatie voor bedrijvigheid (object)
- [[Wiki/Bedrijfsobjecten/3-economie/economie/standplaats|standplaats]] — aangewezen verkooplocatie in openbare ruimte, APV-gereguleerd (object)
- [[Wiki/Bedrijfsobjecten/3-economie/economie/warenmarkt|warenmarkt]] — periodieke georganiseerde verkoop, Marktverordening-gereguleerd (object)
- winkelgebied — aangewezen ruimtelijke concentratie van detailhandel (concept, geen BO)
- ambulante handel — overkoepelend voor warenmarkten en standplaatsen (categorie)
- detailhandelsvestiging — fysieke winkellocatie (concept, te generiek voor BO)

## Bedrijfsobjecten

| Begrip | Status | GGM-grondslag | Matchsterkte |
|---|---|---|---|
| [[Wiki/Begrippen/werklocatie]] | ✅ BO | Vestiging (RSGB) | partieel |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/standplaats]] | ✅ BO | Standplaats (GGM, Musea) | sterk |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/warenmarkt]] | ✅ BO | — (GGM-hiaat) | — |

## GGM-dekkingsanalyse

Het GGM modelleert economie zeer beperkt in Taakveld 3 "Economie", beleidsdomein "Model Economie":

| GGM-domein | Entiteiten | Status |
|---|---|---|
| **Taakveld 3 Economie** | Contact, Hotel, Hotelbezoek, Verkooppunt, Werkgelegenheid, Winkelvloeroppervlak (6 entiteiten) | Vestiging → werklocatie |
| **Taakveld 5 Musea** | Standplaats (3 attributen: beschrijving, adres, naamInstelling) | Standplaats → standplaats (sterk, maar domeinplaatsing betwistbaar) |
| **RSGB (Taakveld 99)** | Vestiging, Verblijfsobject, Rechtspersoon (bv. bedrijf) | Vestiging-grondslag voor werklocatie |

**GGM-hiaat Warenmarkt:** Warenmarkt ontbreekt als entiteit in het GGM. Het is een registreerbaar dataobject (locatie, frequentie, type, branchering) dat gemeenten beheren via de Marktverordening.

**Domeinplaatsing Standplaats:** De GGM-entiteit Standplaats staat onder Musea (taakveld 5) terwijl het een breed APV-concept is. Terugmelding overwegen.

**Structureel hiaat:** beleidsdomein Economie onder taakveld 3 dekt slechts statistieken en vestigingsgegevens. Ontbreken: ondernemersdienstverlening, MKB-classificatie, vestigingsklimaat, regeldruk, arbeidsmarktbeleid, regionale economie, warenmarkt.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Economie/economie-speerpunten-vng|economie-speerpunten-vng]] — VNG: vier speerpunten economisch beleid gemeenten
- [[Wiki/Bronsamenvattingen/Economie/ontwikkelingskader-detailhandel-2012|ontwikkelingskader-detailhandel-2012]] — Gemeente Utrecht: beleidskader detailhandel, markten, standplaatsen
- [[Wiki/Bronsamenvattingen/Economie/detailhandel-utrecht-2015|detailhandel-utrecht-2015]] — Gemeente Utrecht: statusrapportage detailhandel per wijk

## Raakvlakken met andere domeinen

- **Sociaal domein** (taakveld 6): beleidsdomein "Werk" (Participatiewet, re-integratie) raakt arbeidsmarkt en human capital
- **Onderwijs** (taakveld 4): scholing en vaardigheden raken human capital
- **Volkshuisvesting, Leefomgeving** (taakveld 8): ruimtelijke ordening en Omgevingswet raken economische ruimte en werklocaties
- **Veiligheid en Vergunningen** (taakveld 1): VTH-processen raken regeldruk en ondernemersdienstverlening
- **Dienstverlening** (taakveld 10): generieke interacties raken ondernemersdienstverlening

## Hiaten en openstaande vragen

- GGM taakveld 3 dekt een fractie van het beleidsveld — groot hiaat tussen beleidstaal en informatiemodel
- Geen GGM-entiteiten voor: ondernemersdienstverlening, MKB-classificatie, vestigingsklimaat, regeldruk, arbeidsmarktbeleid, regionale economie
- Beleidsdomein "Werk" (taakveld 6) bevat relevante entiteiten voor arbeidsmarkt maar vanuit sociaal-domein perspectief — overlap nog niet geanalyseerd
