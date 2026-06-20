---
type: analyse
titel: "GGM-dekkingspatroon: objecten wel, processen en governance niet"
datum: 2026-06-18
aanleiding: Terugkerend patroon bij mapping van VNG-beleidsbegrippen op het GGM, waargenomen over vijf domeinen (Belastingen, Financiën, Economie, Bedrijfsvoering, Dienstverlening)
---

# GGM-dekkingspatroon: objecten wel, processen en governance niet

## Bevinding

Bij het systematisch mappen van begrippen uit VNG-beleidsdocumenten op het Gemeentelijk Gegevensmodel (GGM v2.5.1) tekent zich een consistent patroon af. Het GGM dekt de **data-objecten** die in gemeentelijke informatiesystemen worden geregistreerd, maar niet de **processen** waarbinnen die objecten ontstaan en niet de **governance-instrumenten** die die processen aansturen.

Dit patroon is niet domeinspecifiek — het is zichtbaar in elk domein dat tot nu toe is geanalyseerd.

## Bewijs per domein

### Belastingen

| Laag | Voorbeeld | GGM |
|---|---|---|
| Basisregistratie | WOZ-object, WOZ-Waarde, Rechtspersoon | **Aanwezig** (RSGB) — de grondslag voor heffing is volledig gemodelleerd |
| Procesmodel | Verordening → tarief → maatstaf → aanslag → belastingplichtige | **Afwezig** — het heffingsproces dat elke belastingapplicatie ondersteunt, ontbreekt als samenhangend model |
| Governance | Belastingverordening, belastingmix, kostendekkend tarief | **Afwezig** — de juridische en beleidsmatige kaders die het proces aansturen |

Het GGM levert de ingrediënten (wie bezit welk WOZ-object met welke waarde) maar niet het recept (hoe wordt daaruit een aanslag berekend en opgelegd).

Zie [[Wiki/Analyses/ggm-hiaten-belastingendomein|ggm-hiaten-belastingendomein]] voor de volledige analyse.

### Financiën

| Laag | Voorbeeld | GGM |
|---|---|---|
| Boekhoudkundige objecten | Begroting, Kostenplaats, Factuur, Activa, Debiteur | **Aanwezig** (beleidsdomein Financien, tv9) — 24 entiteiten, 10 bedrijfsobjecten afgeleid |
| Procesmodel | Kadernota → begroting → tussenrapportages → jaarrekening | **Afwezig** — de begrotingscyclus die de hele financiële huishouding structureert |
| Governance | Budgetrecht, financiële verordening (art. 212), BBV | **Afwezig** — de bevoegdheden en spelregels die bepalen hoe de cyclus werkt |
| Inkomstenbronnen | Gemeentefonds, algemene uitkering, specifieke uitkering | **Afwezig** — de structuur van de gemeentelijke inkomsten |
| Kengetallen | Solvabiliteitsratio, netto schuldquote, onbenutte belastingcapaciteit | **Afwezig** (maar afleidbaar uit bestaande objecten) |

Het GGM levert de financiële administratie maar niet de planning-en-controlcyclus die erop stuurt.

### Economie

| Laag | Voorbeeld | GGM |
|---|---|---|
| Registratie-objecten | Vestiging (RSGB), Hotel, Werkgelegenheid | **Aanwezig** — maar slechts 6 entiteiten, gericht op statistieken rond vestigingen |
| Beleidsveld | Ondernemersdienstverlening, vestigingsklimaat, arbeidsmarkt, werklocatie | **Afwezig** — de breedte van het taakveld ("economische ontwikkeling, bedrijvigheid en innovatie") is niet gedekt |
| Waarden en doelen | Brede welvaart, versterking vestigingsklimaat | **Afwezig** (verwacht — normatief/strategisch) |

Hier is het hiaat breder: niet alleen processen en governance ontbreken, maar ook een groot deel van de operationele objecten. Zie [[Wiki/Bronsamenvattingen/Economie/economie-speerpunten-vng|economie-speerpunten-vng]].

### Bedrijfsvoering

| Laag | Voorbeeld | GGM |
|---|---|---|
| Operationele objecten | Inkooporder, Factuur, Werkorder | **Aanwezig** (beleidsdomein Financien, tv9) |
| Procesmodel | Inkoopproces, aanbestedingsprocedure | **Afwezig** |
| Beleidsinstrumenten | MVOI, Aanbestedingswet, Manifest MVOI | **Afwezig** |

Zelfde patroon: de output van het inkoopproces (orders, facturen) is er, het proces zelf niet.

### Dienstverlening

| Laag | Voorbeeld | GGM |
|---|---|---|
| Zaak-runtime | Zaak, Status, Besluit, Document, Betrokkene, Medewerker | **Aanwezig** (RGBZPlus, tv99) — 25 entiteiten, de kern van zaakgericht-werken |
| Zaaktype-configuratie | CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE, ZAAKOBJECTTYPE | **Afwezig** — de ZTC2-configuratielaag die bepaalt *hoe* zaaktypen worden ingericht |
| Klantcontact | Klantcontact, Balieafspraak | **Aanwezig** (RGBZPlus + tv10 Dienstverlening) |
| Procesarchitectuur | Bedrijfsproces, Deelproces | **Aanwezig** (RGBZPlus) — het GGM heeft deze als uitbreiding op het RGBZ toegevoegd |

Dit domein toont een variant op het patroon: het GGM dekt de zaak-*runtime* goed (wat wordt geregistreerd) maar niet de zaaktype-*configuratie* (hoe zaaktypen worden gedefinieerd). De zaaktypecatalogus is een apart informatiemodel (ZTC2) dat het RGBZ aanvult maar niet in het GGM is opgenomen. Het resultaattype — cruciaal voor archivering — ontbreekt daarmee ook. Zie [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel]].

## Het patroon

```
          VNG-beleidstaal                      GGM
          ──────────────                      ─────
          
  Normatief    ┃  waarden, principes         (buiten scope — logisch)
               ┃
  Strategisch  ┃  doelen, speerpunten        (buiten scope — logisch)
               ┃
  Tactisch     ┃  instrumenten, governance   ◄── HIAAT: wél relevant
               ┃  verordeningen, cycli            voor bedrijfsarchitectuur,
               ┃  budgetrecht, beleidsmix         niet gemodelleerd
               ┃
  Operationeel ┃  processen, ketens          ◄── HIAAT: deels relevant
               ┃  heffingsproces,                 voor informatiemodel,
               ┃  begrotingscyclus                niet gemodelleerd
               ┃
               ┃  data-objecten              ◄── GEDEKT: basisregistraties,
               ┃  WOZ-object, Begroting,          boekhoudkundige objecten,
               ┃  Factuur, Debiteur                registratie-entiteiten
```

De grens loopt niet tussen "operationeel" en "tactisch" maar tussen **data** (wat systemen opslaan) en **dynamiek** (hoe data ontstaat, stroomt en wordt bestuurd). Het GGM is een informatiemodel — het modelleert de staat van systemen, niet het gedrag van de organisatie. Dat is geen fout; het is een scopekeuze.

## Waarom dit ertoe doet

De bedrijfsarchitectuur (ArchiMate) heeft alle lagen nodig:

| ArchiMate-laag | Wat het beschrijft | GGM-dekking |
|---|---|---|
| Business objects | Wat wordt geregistreerd | **Goed** |
| Business processes | Hoe werk verloopt | **Ontbreekt** |
| Business rules | Welke regels gelden | **Ontbreekt** |
| Business roles/actors | Wie wat doet | **Grotendeels ontbreekt** |
| Business functions | Welke functies de organisatie vervult | **Ontbreekt** |

Het GGM levert het fundament (business objects), maar de bedrijfsarchitectuur moet de bovenliggende lagen zelf invullen. De wiki doet dat door:

1. **Begrippen** te extraheren uit beleidsdocumenten — dit levert de tactische en operationele taal die het GGM mist
2. **Bedrijfsobjecten** af te leiden die het GGM wél dekt — dit verankert de architectuur in het informatiemodel
3. **Hiaten** te signaleren waar begrippen geen GGM-grondslag hebben — dit stuurt waar de architectuur moet aanvullen

## Consequenties voor de wiki

### Wat de wiki wél kan afleiden uit het GGM

- Business objects met attributen en relaties
- Taxonomieën van objecten (generalisatiehiërarchieën)
- Relaties tussen objecten (associaties, composities)
- Basisregistratie-grondslag (herkomst per entiteit)

### Wat de wiki zelf moet opbouwen uit beleidsbronnen

- Procesmodellen (welke stappen, in welke volgorde, door wie)
- Governance-structuur (welke verordening/wet regelt wat)
- Actoren en rollen (wie heeft welke bevoegdheid)
- Beleidsinstrumenten (welke knoppen heeft de gemeente)
- Koppelingen tussen niveaus (welk beleidsdoel wordt gediend door welk proces dat welke objecten produceert)

### Verwachting bij nieuwe domeinen

Bij het verwerken van bronnen voor nieuwe domeinen (Schuldhulpverlening, Cultuur, Dienstverlening, etc.) is de verwachting dat hetzelfde patroon optreedt:
- De GGM-objecten zullen de registratie-kant dekken
- De procesmodellen en governance-instrumenten uit beleidsdocumenten zullen geen GGM-match hebben
- De wiki zal de brug moeten slaan

## Bronnen

Gebaseerd op de verwerking van:
- 19 VNG-bronnen over Belastingen, Financiën, Economie, Bedrijfsvoering
- 2 GEMMA-standaarden: RGBZ 1.0 en ZTC2 v2.1 (Dienstverlening)
- GGM v2.5.1: taakvelden 3, 5, 6, 9, 10, 99 (zie Sources/GGM/)
- 54 wiki-begrippen en 19 bedrijfsobjecten
