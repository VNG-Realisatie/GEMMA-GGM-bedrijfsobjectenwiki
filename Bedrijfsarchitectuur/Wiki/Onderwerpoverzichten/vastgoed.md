---
type: onderwerp
naam: Vastgoed
status: afgerond
verwerkingsdatum: 2026-09-24
bronnen_count: 3
begrippen_count: 26
bo_count: 7
---

# Vastgoed

Gemeentelijk vastgoed omvat het beheer, de verhuur en het onderhoud van gebouwen, terreinen en percelen die eigendom zijn van de gemeente. Het domein bestrijkt de volledige levenscyclus: verwerving, exploitatie (verhuur), beheer (inspecties en onderhoud) en afstoting. In het GGM valt dit onder taakveld 9 (Interne Organisatie), beleidsdomein Vastgoed (27 entiteiten).

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | object | Perceel, gebouw of terrein waar de gemeente een zakelijk recht op heeft | ✅ | ja | 6/6, exact match | Stadhuis, buurthuis, grondperceel | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/verhuurbare-eenheid\|Verhuurbare Eenheid]] | object | Individueel verhuurbaar deel van een vastgoedobject | ✅ | ja | 6/6, exact match | Zaal in buurthuis, verdieping kantoor | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] | object | Huurovereenkomst over gebruik van een vastgoedobject | ✅ | ja | 6/6, exact match | ROZ-huurcontract, tijdelijke verhuur | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | object | Meerjaren onderhoudsplanning per vastgoedobject | ✅ | ja | 6/6, exact match | 15-jarenplan gebouw | ja |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]] | object | Periodieke controle van de technische staat | ✅ | ja | 6/6, exact match; samengevoegd met VTH-inspectie | NEN 2767-conditiemeting | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/werkbon\|Werkbon]] | object | Document dat een hoeveelheid uit te voeren werk beschrijft | ✅ | ja | 6/6, exact match | Reparatie verwarmingsketel | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/algemeenbelangbesluit\|Algemeenbelangbesluit]] | instrument | Raadsbesluit dat verhuur onder de kostprijs mogelijk maakt | ✅ | nee | 6/6, governance-object, GGM-hiaat | Besluit verhuur kinderopvang onder kostprijs | nee |
| vastgoedportefeuille | thema | Totaal van vastgoedobjecten, gecategoriseerd naar gebruik | ❌ | nee | Groepering, geen zelfstandig object | — | nee |
| huurprijssystematiek | thema | Methodiek voor berekening kostprijsdekkende huur | ❌ | nee | Beleid/methodiek, geen object | — | nee |
| kostprijsdekkende huur | waarde | Huurprijs die de integrale kosten dekt | ❌ | nee | Berekende waarde, attribuut van contract | — | nee |
| erfstuk | object | Monumentaal vastgoed dat niet verkocht kan worden | ❌ | ja | Subtype van Vastgoedobject | Kerktoren, vestingwerk | nee |
| bezettingsgraad | object | Mate van gebruik van een pand | ❌ | ja | Attribuut/KPI van Verhuurbare Eenheid | — | nee |
| conditiescore | object | NEN 2767-score voor technische staat | ❌ | ja | Enumeratie, attribuut van inspectie/bouwdeel | Score 1-6 | ja (enum) |
| energielabel | object | Classificatie energieprestatie gebouw | ❌ | ja | Enumeratie, attribuut van Vastgoedobject | Label A-G | ja (enum) |
| bouwdeel | object | Aanwijsbaar deel van een gebouw | ❌ | ja | GGM-component van Vastgoedobject | Dak, gevel, installatie | ja |
| gebouwbeheersysteem | thema | Informatiesysteem voor vastgoedregistratie | ❌ | nee | Systeem, geen bedrijfsobject | Planon | nee |
| [[Wiki/Rollen/eigenaar|Eigenaar]] | rol | Persoon die eigenaar is van vastgoed | ❌ | ja | Rol/generalisatie van Rechtspersoon; vastgelegd als rol-pagina | — | ja |
| [[Wiki/Rollen/huurder|Huurder]] | rol | Partij die een zaak in gebruik heeft | ❌ | ja | Rol/generalisatie van Rechtspersoon; vastgelegd als rol-pagina | — | ja |
| Asset, Object | object | GEBORA-begrippen voor de boekhoudkundige resp. fysieke representatie van vastgoed | ❌ | ja | Duplicaat van bestaand BO [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | Stadhuis als asset/object | nee |
| Assetplan | object | Strategisch plan voor beheer/onderhoud van een asset (GEBORA) | ❌ | ja | Duplicaat van bestaand BO [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | 15-jarenplan | ja |
| Assetinitiatief | object | Aanvangsfase van een assetontwikkeling (GEBORA) | ❌ | nee | Geen zelfstandig registerobject; procesmoment vóór een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] of nieuwbouwproject | Idee voor renovatie | nee |
| Instandhouding, Onderhoud, Conditie/Toestand | thema | Vastgoedbeheerprocessen en -toestand (GEBORA) | ❌ | nee/ja | Onderhoud/Instandhouding zijn processen; Conditie komt overeen met bestaand niet-BO-begrip conditiescore ([[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]]/[[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/werkbon\|Werkbon]] dekken de registreerbare objecten) | NEN 2767-score | ja (enum, GGM: NEN2767 Conditiescore) |
| Vergunning | object | Generieke vergunning voor bouw-/verbouw-/sloopwerkzaamheden (GEBORA) | ❌ | ja | Duplicaat van bestaand BO [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen\|Vergunningen en ontheffingen]] | Omgevingsvergunning bouwen | nee |
| Koop/Verkoop | thema | Eigendomsoverdracht van vastgoed (GEBORA) | ❌ | nee | Proces/gebeurtenis; rechtswijziging loopt via BRK-registratie (Akte/Zakelijk Recht), geen eigen BO nodig | Aankoop grondperceel | nee |
| Huur/Verhuur | object | Gebruiksrecht tegen vergoeding (GEBORA) | ❌ | ja | Duplicaat van bestaand BO [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] | ROZ-huurcontract | ja |
| Zone, Bestemming, Gebied | object | Ruimtelijke-ordeningsbegrippen (GEBORA) | — | — | Hoort primair bij het Omgevingswet-domein, hier niet beoordeeld (verhuisregel) | Bestemmingsplan | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam|Vastgoedstrategie Amsterdam]] — strategisch beleidsdocument Gemeente Amsterdam over ~1.000 panden, huurprijssystematiek, verduurzaming
- [[Wiki/Bronsamenvattingen/Vastgoed/beleidsplan-vastgoed-hulst|Beleidsplan Vastgoed Hulst]] — operationeel beleidsplan Gemeente Hulst over ~50 gebouwen, inspecties, MJOP, onderhoud
- [[Wiki/Bronsamenvattingen/Standaarden/gebora-conceptueel-informatiemodel|GEBORA: Gebouwde Omgeving Referentie Architectuur]] — verificatiebron, geen nieuw beleidsdocument

## Openstaande vragen

- De GGM-entiteiten rond WOZ (WOZ-Belang, LocatieaanduidingWozObject) overlappen met het Belastingen-domein — afstemming nodig
- Aanbesteding Vastgoed is een specialisatie van generiek Aanbesteding (Inkoop-domein) — mogelijk samenvoegen bij toekomstige ingest van Inkoop

## Verificatie-update (2026-09-24)

Het digiGO-informatiemodel GEBORA ([[Wiki/Bronsamenvattingen/Standaarden/gebora-conceptueel-informatiemodel]]) is verwerkt als verificatiebron voor de bestaande BO's in dit domein. Geen nieuwe BO's: alle gemeentelijk-relevante GEBORA-begrippen (Asset, Assetplan, Vergunning, Huur/Verhuur) blijken duplicaten van reeds vastgelegde BO's (Vastgoedobject, MJOP, Vergunningen en ontheffingen, Vastgoedcontract). Assetinitiatief, Instandhouding/Onderhoud/Conditie en Koop/Verkoop zijn procesmatig van aard en halen de BO-criteria niet zelfstandig. Zone/Bestemming/Gebied horen primair bij het Omgevingswet-domein. Bouwsector-procesobjecten van GEBORA (Product, Materiaal, Materieel, Personeel, Werkcontract, Order, Transport, Logistiek, Boekhouding, Organisatie) vallen buiten het gemeentelijk perspectief ([WC5]) en zijn niet beoordeeld.
