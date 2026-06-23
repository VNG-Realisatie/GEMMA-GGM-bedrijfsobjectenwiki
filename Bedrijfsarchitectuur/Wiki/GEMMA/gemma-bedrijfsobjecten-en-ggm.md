---
type: bronsamenvatting
titel: "GEMMA: Bedrijfsobjecten, procesarchitectuur, zaakgericht werken en het GGM"
domein: []
datum_ingest: 2026-06-18
begrippen_geextraheerd: []
---

# Bronsamenvatting: GEMMA bedrijfsobjecten, procesarchitectuur, zaakgericht werken en het GGM

**Bron:** Acht pagina's op gemmaonline.nl (VNG Realisatie), geraadpleegd 2026-06-18:
- Bedrijfsobjecten
- GEMMA en het Gemeentelijk Gegevensmodel
- Procesarchitectuur kennismodel
- Bedrijfsfuncties
- Bedrijfsarchitectuur
- Visie op zaakgericht werken
- Procesarchitectuur: relatie met zaakgericht werken
- Samenhang PDC, UPL, zaaktypen en verwerkingsregister

## Samenvatting

De GEMMA-referentiearchitectuur beschrijft hoe gemeentelijke processen, informatiesystemen, gegevens en infrastructuur samenhangen. De architectuur is opgebouwd in drie lagen:

1. **Bedrijfsarchitectuur** (top-down): bedrijfsfuncties, bedrijfsprocessen en bedrijfsobjecten
2. **Informatiearchitectuur**: applicatiecomponenten, services, standaarden
3. **Technische architectuur**: infrastructuur

### Bedrijfsobjecten: afgeleid uit het GGM

De GEMMA positioneert bedrijfsobjecten als "concepten die binnen een bepaald domein worden gebruikt en betekenis hebben" — het bedrijfsniveau. Het GGM positioneert dataobjecten als "samenhangende sets gegevens die geautomatiseerd kunnen worden verwerkt" — het applicatieniveau.

De kernafspraak: **GEMMA leidt bedrijfsobjecten af van GGM-dataobjecten**, om consistentie tussen de niveaus te borgen. Het GGM levert objecten in CSV-formaat, VNG retourneert GEMMA-bedrijfsobjecten met definities. Resultaat: 507 bedrijfsobjecten over 46 beleidsdomeinen.

### Procesarchitectuur: onafhankelijk van het GGM

De GEMMA-procesarchitectuur beschrijft via een kennismodel (ArchiMate-gebaseerd) hoe producten en diensten worden gerealiseerd:

- **Motivatielaag**: beleidskaders, visie, strategie, kernwaarden
- **Organisatielaag**: bedrijfsprocessen (hiërarchie: handeling → processtap → deelproces → bedrijfsproces → ketenproces), bedrijfsfuncties, actoren, rollen, bedrijfsobjecten

Bedrijfsfuncties (besturend, primair, ondersteunend) beschrijven wát gemeenten doen, onafhankelijk van hoe. Bedrijfsprocessen beschrijven de volgorde van activiteiten die tot een resultaat leiden.

### De verbindingslaag

Bedrijfsobjecten zijn de verbinding tussen de procesarchitectuur en het informatiemodel:
- Ze worden gerealiseerd door bedrijfsprocessen (die ze produceren en verbruiken)
- Ze worden ondersteund door bedrijfsfuncties (die ze beheren en gebruiken)
- Ze worden technisch geïmplementeerd als GGM-dataobjecten

De GEMMA noemt als vervolgstap: relaties aanbrengen tussen bedrijfsobjecten en bedrijfsfuncties/referentiecomponenten. Dit is nog niet gerealiseerd.

### Zaakgericht werken: de zaak als procesobject

De GEMMA beschrijft zaakgericht werken als de manier waarop gemeenten processen uitvoeren. De **zaak** is daarin het centrale concept:

> "Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden."

De zaak fungeert als **informatiecontainer** die de uitvoering van een bedrijfsproces begeleidt. Alle procesinformatie wordt vastgelegd in een gestandaardiseerd zaakdossier. Zaaktypen (vastgelegd in de ZTC, conform ImZTC) dienen als templates die statussen, doorlooptijden, rollen, documenten en resultaten definiëren.

Procesafronding = statusovergang: elk afgerond deelproces markeert een statusovergang in de zaak. Meerdere zaaktypen kunnen corresponderen met hetzelfde bedrijfsproces.

### Samenhang PDC, UPL, ZTC en verwerkingsregister

De GEMMA beschrijft vier samenhangende instrumenten voor gemeentelijke dienstverlening:

| Instrument | Beschrijving | Gericht op |
|---|---|---|
| **PDC** | Producten- en dienstencatalogus op de website | Burgers/bedrijven |
| **UPL** | Uniforme Productnamenlijst (landelijk, met wettelijke grondslag) | Burgers/bedrijven |
| **ZTC** | Zaaktypecatalogus (structuur zaakafhandeling) | Medewerkers |
| **Verwerkingsregister** | AVG-register verwerkingen persoonsgegevens | Medewerkers/toezicht |

De **wettelijke grondslag** is het verbindend element tussen deze instrumenten. Het aggregatieniveau van verwerkingsactiviteiten in het verwerkingsregister is vergelijkbaar met GEMMA-deelprocessen.

De ZTC-visie evolueert van productspecifieke zaaktypen (honderden) naar generieke zaaktypen (Aanvragen, Meldingen, Aangiften) — een beperkt aantal standaard templates.

### Procesmodel hiërarchie

| Niveau | Definitie |
|---|---|
| Bedrijfsproces | End-to-end, klant tot klant, onder verantwoordelijkheid van één organisatie |
| Deelproces | Onder verantwoordelijkheid van één bedrijfsfunctie |
| Processtap | Onder verantwoordelijkheid van één rol |
| Handeling | Kleinste werkeenheid, één persoon/machine |

## Relevantie voor de wiki

Deze bronnen zijn de basis voor de analyse [[Wiki/Analyses/ggm-oorsprong-en-meerwaarde|ggm-oorsprong-en-meerwaarde]]. Drie kernbevindingen:

**1. Bedrijfsobjecten = GGM-afgeleid.** Omdat GEMMA bedrijfsobjecten afleidt uit het GGM, en het GGM bottom-up is opgebouwd uit bestaande databases, bevat het bedrijfsobjectenmodel alleen data-objecten. Objecten die in processen en governance-instrumenten ontstaan (belastingaanslag, financiële verordening, kadernota) zijn niet als bedrijfsobject beschikbaar, terwijl de procesarchitectuur er wel mee werkt.

**2. De zaak is het bestaande verbindingsmechanisme.** De GEMMA verbindt processen al met informatie via het zaak-concept. De zaak is in feite een **procesobject** — het ontstaat in een proces, bevat procesinformatie, en wordt bestuurd door een zaaktype (governance-object). Dit toont dat de GEMMA de behoefte aan procesobjecten en governance-objecten al erkent, maar alleen voor de zaakgerichte processen en niet voor het volledige bedrijfsobjectenmodel.

**3. De verbetervoorstellen wijzen dezelfde richting.** De GEMMA noemt expliciet als verbetervoorstel: "Breid GEMMA-bedrijfsarchitectuur uit waar verwerkingsactiviteiten niet aan processen gekoppeld kunnen worden." En: "Breng relaties aan tussen bedrijfsobjecten en bedrijfsfuncties." Dit is precies de top-down aanvulling die de wiki levert.

De wiki vult dit aan door bedrijfsobjecten ook top-down af te leiden uit beleidsbronnen, met de `grondslag`-classificatie (ggm-entiteit, ggm-afgeleid, procesobject, governance-object).

**Aanvullende bronnen voor zaakgericht werken:**
- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel|Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) 1.0]] — het RGBZ als datamodel achter de zaak
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel|GEMMA Zaaktypecatalogus 2 (ZTC2) — Informatiemodel v2.1]] — de ZTC2 als configuratielaag: zaaktypecatalogi, resultaattypes, roltypes
- De ZTC2-configuratielaag ontbreekt in het GGM — zie [[Wiki/Analyses/ggm-dekkingspatroon|ggm-dekkingspatroon]] (sectie Dienstverlening)

## Citaten

> "Om een consistente relatie tussen beide te borgen, leidt de GEMMA bedrijfsobjecten af van de GGM-dataobjecten."
> — *GEMMA en het Gemeentelijk Gegevensmodel, gemmaonline.nl*

> "GEMMA's bedrijfsobjecten geven een meer conceptuele weergave van informatie (bedrijfsniveau), terwijl GGM's dataobjecten informatie vertalen naar een technischer niveau (applicatieniveau). Dataobjecten zijn te zien als de technische tegenhangers van bedrijfsobjecten."
> — *GEMMA en het Gemeentelijk Gegevensmodel, gemmaonline.nl*

> "Een zaak is een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden."
> — *Visie op zaakgericht werken, gemmaonline.nl*

> "Producten en diensten worden gerealiseerd door bedrijfsprocessen."
> — *Procesarchitectuur kennismodel, gemmaonline.nl*

> "Breid GEMMA-bedrijfsarchitectuur uit waar verwerkingsactiviteiten niet aan processen gekoppeld kunnen worden."
> — *Samenhang PDC, UPL, zaaktypen en verwerkingsregister, gemmaonline.nl*

## Bronnen

- [[Sources/GEMMA/gemma-bedrijfsobjecten-en-ggm]]
