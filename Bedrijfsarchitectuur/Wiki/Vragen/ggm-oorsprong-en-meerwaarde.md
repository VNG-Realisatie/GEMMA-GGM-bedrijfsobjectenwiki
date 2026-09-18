---
type: analyse
titel: "Van data-inventarisatie naar bedrijfsarchitectuur: het GGM in de GEMMA-context"
datum: 2026-06-18
aanleiding: Reflectie op de oorsprong van het GGM (bottom-up uit bestaande informatiemodellen en databases), de oprekking naar transactioneel gebruik, en de consequenties voor de GEMMA-referentiearchitectuur
---

# Van data-inventarisatie naar bedrijfsarchitectuur

## Wat het GGM heeft opgeleverd

Het Gemeentelijk Gegevensmodel is ontstaan vanuit een concrete behoefte: gemeenten wilden managementinformatie afleiden uit hun bestaande systemen. De werkgroep (gestart bij Gemeente Delft) heeft dit bottom-up opgebouwd uit twee soorten bronnen:

1. **Bestaande informatiemodellen** — de kern (taakveld 99) is gebaseerd op het RSGB, dat op zijn beurt is gebouwd op de catalogi van zes basisregistraties (BRP, BAG, BRK, BRWOZ, NHR, BGT/IMGeo) aangevuld met gemeentespecifieke gegevens. Het RSGB is zelf al een integratiemodel: het verbindt de basisregistraties onderling en vult ze aan met wat gemeenten méér nodig hebben dan wat het landelijk stelsel biedt. RGBZ (zaakgericht werken) en domeinspecifieke informatiemodellen uit StUF-koppelvlakken leveren eveneens input.

2. **Bestaande databases** — de domeinmodellen (Sociaal Domein, Financiën, Beheer Openbare Ruimte, etc.) zijn opgebouwd door te inventariseren welke gegevens gemeenten in hun taakspecifieke systemen registreren. Deze laag gaat verder dan het RSGB: het RSGB beschrijft wat de gemeente met basisregistraties uitwisselt, de domeinmodellen beschrijven wat de gemeente intern registreert.

Dit heeft waardevol resultaat opgeleverd:

- **Één gedeelde taal voor data** — 46 beleidsdomeinen, honderden entiteiten met definities en attributen
- **Dekking van basisregistraties** — de RSGB-kern vormt een betrouwbaar, gestandaardiseerd fundament dat aansluit op het landelijk stelsel
- **Dekking van domeinregistraties** — Sociaal Domein, Financiën, Beheer Openbare Ruimte, Onderwijs en andere domeinen zijn uitgewerkt op logisch dataniveau
- **MIM-conformiteit** — het model volgt het Metamodel voor Informatiemodellen, wat uitwisselbaarheid en vergelijkbaarheid waarborgt
- **Adoptie in de GEMMA** — VNG Realisatie heeft het GGM overgenomen als basis voor het GEMMA bedrijfsobjectenmodel (507 bedrijfsobjecten, 46 beleidsdomeinen, 40 modellen)

De kracht van de aanpak is dat het model geworteld is in de werkelijkheid: het bouwt voort op gevestigde informatiestandaarden (RSGB, RGBZ, basisregistratiecatalogi) en vult die aan met wat gemeenten daadwerkelijk in hun systemen registreren.

## De oprekking: van MI naar transactioneel

De oorspronkelijke toepassing — managementinformatie afleiden — stelt andere eisen aan een model dan het ontwerpen of specificeren van transactionele systemen.

| Aspect | MI-toepassing (oorsprong) | Transactionele toepassing (oprekking) |
|---|---|---|
| Kernvraag | Welke data hebben we? | Wat moet er met die data gebeuren? |
| Richting | Achteraf: rapportage en analyse | Vooraf: wat mag, wie doet het, wanneer |
| Modelleert | Entiteiten, attributen, relaties | + statusovergangen, business rules, rollen, events |
| Bron | Bestaande informatiemodellen en databases | Procesbeschrijvingen, wetgeving, beleid |
| Perspectief | Data als feit (wat is er) | Data als artefact (hoe ontstaat het, hoe stroomt het) |

Voor MI is het voldoende om te weten *dát* er een Begroting-entiteit is met bepaalde attributen. Voor een transactioneel systeem moet je ook weten: hoe komt een begroting tot stand (begrotingscyclus), wie autoriseert deze (budgetrecht, raad), welke spelregels gelden (BBV, financiële verordening), en welke statusovergangen het document doormaakt (concept → vastgesteld → gewijzigd).

Het GGM levert het eerste. Het tweede is er nog niet — en dat is geen tekortkoming maar een gevolg van de oorsprong.

## Wat dit betekent in de GEMMA

De GEMMA-referentiearchitectuur werkt top-down. Het procesarchitectuur-kennismodel beschrijft een keten van producten → diensten → bedrijfsprocessen → processtappen → handelingen, uitgevoerd door actoren in rollen, ondersteund door bedrijfsfuncties. Dit is precies het organisatiegedrag dat het GGM niet modelleert.

Tegelijkertijd leidt GEMMA zijn bedrijfsobjecten af uit het GGM (zie gemmaonline.nl/wiki/GEMMA_en_het_Gemeentelijk_Gegevensmodel). De formele afspraak: het GGM levert objecten en relaties in CSV-formaat, VNG Realisatie retourneert GEMMA-bedrijfsobjecten met definities.

Dit creëert een structurele asymmetrie:

```
GEMMA (top-down)                          GGM (bottom-up)
─────────────────                         ──────────────────

Producten, Diensten                       
    ↓                                     
Bedrijfsprocessen                         
    ↓                                     
Bedrijfsfuncties, Rollen                  
    ↓                                     
Bedrijfsobjecten          ◄── afgeleid uit ──►  GGM-entiteiten
                                                    ↑
                                              Bestaande databases
```

De processen, functies en rollen zijn in de GEMMA onafhankelijk gedefinieerd. Maar de objecten waar deze processen mee werken, komen uit het GGM. En omdat het GGM alleen data-objecten bevat, ontbreken in het bedrijfsobjectenmodel:

- **Procesobjecten** — artefacten die in processen ontstaan maar niet als zodanig in databases staan (belastingaanslag als heffingsbesluit, kadernota als sturingsdocument)
- **Governance-objecten** — juridische en beleidsmatige kaders die processen aansturen (belastingverordening, financiële verordening, budgetrecht)
- **Rollen en bevoegdheden** — wie wat mag doen (heffingsambtenaar, invorderingsambtenaar)

Hierdoor kan de GEMMA-procesarchitectuur wél beschrijven *dat* er een heffingsproces is, maar de bedrijfsobjecten die dat proces produceert en verbruikt zijn niet allemaal beschikbaar als benoemde objecten in het model.

## Waar de meerwaarde ligt

De twee perspectieven — bottom-up (GGM) en top-down (GEMMA-procesarchitectuur) — zijn complementair. De meerwaarde ontstaat door ze expliciet te verbinden.

### 1. Verrijking van het bedrijfsobjectenmodel

Het GEMMA-bedrijfsobjectenmodel (507 objecten) is nu volledig GGM-afgeleid. Uitbreiding met objecten uit de proces- en governance-laag maakt het model bruikbaar voor de volle breedte van de GEMMA:

| Huidige situatie | Mogelijke verrijking |
|---|---|
| Bedrijfsobjecten = GGM-entiteiten | + procesobjecten (uit procesarchitectuur) |
| Alleen data-objecten | + governance-objecten (uit beleidsbronnen) |
| Geen rollen/bevoegdheden | + actoren met bevoegdheden (uit wetgeving) |

Concreet voorbeeld — het belastingendomein:

| Aanwezig (GGM-afgeleid) | Ontbreekt (proces/governance) |
|---|---|
| WOZ-object, WOZ-Waarde | Belastingaanslag, Tarief |
| Debiteur, Begroting | Belastingverordening, Heffingsmaatstaf |
| Vordering, Kwijtschelding | Heffingsambtenaar, Invorderingsambtenaar |

De linkerkolom beschrijft wat er in systemen staat. De rechterkolom beschrijft wat het bedrijfsproces nodig heeft. Samen vormen ze een compleet beeld.

### 2. Domeinen waar het GGM nog niet is

Het GGM dekt niet alle gemeentelijke domeinen. Uit een eerdere mapping van de 26 VNG-rubrieken op GGM-taakvelden bleek dat domeinen als Belastingen, Energietransitie, Openbare gezondheid en Risicobeheer hiaten hebben (analyse verwijderd 2026-09-17, zie noot onderaan deze pagina). Voor deze domeinen kan het bedrijfsobjectenmodel top-down worden opgebouwd vanuit beleidsbronnen en procesbeschrijvingen, als aanvulling op het GGM. Zodra het GGM deze domeinen uitwerkt, kunnen de bottom-up entiteiten worden gekoppeld aan de top-down bedrijfsobjecten.

### 3. Koppeling processen ↔ objecten

De GEMMA-procesarchitectuur beschrijft processen, maar de koppeling naar bedrijfsobjecten is niet altijd expliciet. Door per proces te benoemen welke objecten het verbruikt en produceert — inclusief objecten die niet uit het GGM komen — wordt de procesarchitectuur concreter en bruikbaarder voor implementatie.

### 4. Transactionele toepasbaarheid

Als het GGM wordt ingezet voor het specificeren van transactionele systemen (de oprekking), dan levert de aanvulling met procesobjecten en governance-objecten precies wat er nodig is:

| Wat een transactioneel systeem nodig heeft | Bron |
|---|---|
| Datamodel (entiteiten, attributen, relaties) | GGM |
| Statusovergangen (concept → definitief → betaald) | Procesobjecten |
| Business rules (opbrengsten ≤ kosten) | Governance-objecten |
| Autorisatie (wie mag wat) | Rollen/bevoegdheden |
| Procesflow (welke stappen, in welke volgorde) | GEMMA-procesarchitectuur |

Zonder de aanvulling ontwerp je een database. Met de aanvulling ontwerp je een applicatie.

## Hoe het GGM-dekkingspatroon helpt

Uit de systematische mapping van VNG-beleidsbegrippen op het GGM is een voorspelbaar patroon gebleken: procesobjecten en governance-objecten zijn in het GGM niet compleet gedekt. Dit patroon maakt het mogelijk om voor nieuwe domeinen vooraf in te schatten waar het GGM zal dekken en waar aanvulling nodig is:

| Begripstype | GGM-match verwacht? | Aanvulling nodig? |
|---|---|---|
| object (data) | Ja | Nee — GGM dekt dit |
| doelgroep | Deels (personen via RSGB) | Rol-perspectief aanvullen |
| actor | Zelden | Ja — rollen en bevoegdheden |
| instrument | Nee | Ja — governance-objecten |
| thema | Nee | Ja — procescontexten |

Dit is geen kritiek op het GGM — het is een logisch gevolg van de bottom-up oorsprong en tegelijkertijd een routekaart voor gerichte aanvulling.

## De zaak als bestaand verbindingsmechanisme

De GEMMA kent al een mechanisme dat processen verbindt met informatie: **zaakgericht werken**. De zaak is "een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat." De zaak fungeert als informatiecontainer die de uitvoering van een bedrijfsproces begeleidt; het zaaktype definieert statussen, rollen, documenten en resultaten.

In de terminologie van deze wiki is de zaak een **procesobject** (het ontstaat in een proces) en het zaaktype een **governance-object** (het stuurt het proces aan). De GEMMA erkent de behoefte aan deze objecttypes dus al — maar alleen binnen het domein van zaakgericht werken, niet als generiek patroon in het bedrijfsobjectenmodel.

De GEMMA beschrijft ook de samenhang tussen PDC, UPL, ZTC en verwerkingsregister. De **wettelijke grondslag** is daarin het verbindend element. De verwerkingsactiviteiten in het verwerkingsregister corresponderen qua aggregatieniveau met GEMMA-deelprocessen. En de GEMMA noemt expliciet als verbetervoorstel:

> "Breid GEMMA-bedrijfsarchitectuur uit waar verwerkingsactiviteiten niet aan processen gekoppeld kunnen worden."

Dit wijst dezelfde richting: het bedrijfsobjectenmodel moet worden aangevuld met objecten die niet uit de datalaag komen maar uit de proces- en governance-laag.

## Samenvatting

Het GGM heeft een stevig fundament gelegd door bottom-up te inventariseren wat gemeenten registreren. De GEMMA bouwt daar top-down op voort met processen, functies en rollen. De verbindingslaag — het bedrijfsobjectenmodel — is nu eenzijdig gevuld vanuit de data-kant. Zaakgericht werken toont dat de GEMMA het patroon van procesobjecten en governance-objecten al kent, maar het is nog niet doorgetrokken naar het volledige bedrijfsobjectenmodel.

Door het model breder aan te vullen met objecten uit de proces- en governance-kant ontstaat een compleet architectuurplaatje dat:

1. Bevestigt wat het GGM al dekt (de data-objecten)
2. Expliciet maakt wat er nog ontbreekt (procesobjecten, governance, rollen)
3. Zaakgericht werken generaliseert als patroon voor alle processen, niet alleen zaakgerichte
4. De GEMMA-procesarchitectuur concreter maakt door de koppeling met objecten
5. De weg vrijmaakt voor transactionele toepassing van het GGM

De twee perspectieven concurreren niet — ze vullen elkaar aan.

## Bronnen

- GGM v2.5.1, Gemeente Delft (github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel)
- GEMMA Bedrijfsobjecten (gemmaonline.nl/wiki/Bedrijfsobjecten) — 507 bedrijfsobjecten uit GGM
- GEMMA en het Gemeentelijk Gegevensmodel (gemmaonline.nl/wiki/GEMMA_en_het_Gemeentelijk_Gegevensmodel) — formele afspraken
- GEMMA Procesarchitectuur Kennismodel (gemmaonline.nl/wiki/Procesarchitectuur_kennismodel) — koppeling processen, functies, rollen, objecten
- GEMMA Bedrijfsfuncties (gemmaonline.nl/wiki/Bedrijfsfuncties) — besturende, primaire en ondersteunende functies
- GEMMA Visie op zaakgericht werken (gemmaonline.nl/wiki/Visie_op_zaakgericht_werken) — zaak als informatiecontainer
- GEMMA Procesarchitectuur relatie met zaakgericht werken (gemmaonline.nl/wiki/Procesarchitectuur_Relatie_met_zaakgericht_werken) — zaaktype als procestemplate
- GEMMA Samenhang PDC, UPL, zaaktypen en verwerkingsregister (gemmaonline.nl/wiki/Samenhang_PDC,_UPL,_zaaktypen_en_verwerkingsregister) — wettelijke grondslag als verbindend element
- RSGB 2.02 Deel I (KING, 2018) — referentiemodel stelsel van gemeentelijke basisgegevens
- VNG Informatiemodellen (standaarden.vng.nl/Informatiemodellen) — overzicht RSGB, RGBZ, ImZTC
- VNG-beleidsbronnen: 19 verwerkte bronnen over Belastingen, Financiën, Economie, Bedrijfsvoering
- Wiki-analyses: [[Wiki/Analyses/ggm-terugmeldingen|ggm-terugmeldingen]], [[Wiki/Analyses/entiteitendekking/totaaloverzicht|entiteitendekking/totaaloverzicht]] — de drie oorspronkelijk hier genoemde analysepagina's (ggm-dekkingspatroon, ggm-hiaten-belastingendomein, vng-rubrieken-mapping) zijn op 2026-09-17 verwijderd (commit `df096d8`); zie `Wiki/log.md` 2026-09-18
