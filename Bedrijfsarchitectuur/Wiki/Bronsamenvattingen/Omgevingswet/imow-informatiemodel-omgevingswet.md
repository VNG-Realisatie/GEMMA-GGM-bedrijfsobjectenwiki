---
type: bronsamenvatting
titel: Informatiemodel Omgevingswet (IMOW) v3.0.1
onderwerp: [Omgevingswet]
datum_ingest: 2026-06-27
---

# Informatiemodel Omgevingswet (IMOW) v3.0.1

## Samenvatting

Het IMOW (Geonovum, december 2023) beschrijft de objecttypen die gemeenten en andere bevoegde gezagen aanleveren aan het Digitaal Stelsel Omgevingswet (DSO). Het model specificeert hoe omgevingsbesluiten worden voorzien van machine-leesbare aantekeningen, zodat regels op een kaart getoond en bevraagd kunnen worden.

Het IMOW werkt samen met STOP (documentstructuur), LVBB (aanlevering), TPOD's (regels per documenttype) en Basisgeometrie (GML). Alle objecten erven van OW-Object en hebben een NEN3610-identificatie, status en procedurestatus.

De kernobjecten vallen in drie groepen:

**Artikelsgewijze structuur** — objecten gekoppeld aan artikelen/leden in het omgevingsplan:
- [[Juridische Regel]] (abstract) met subtypes RegelVoorIedereen, Instructieregel, Omgevingswaarderegel
- [[Activiteit]] — gereguleerd menselijk handelen, hiërarchisch gestructureerd met tophaak-activiteit per gemeente
- [[Gebiedsaanwijzing]] — aanwijzing van gebied met beleid, subtypes Functie en Beperkingsgebied
- [[Omgevingsnorm]] en [[Omgevingswaarde]] — normwaarden per locatie, kwantitatief of kwalitatief

**Vrijetekststructuur** — objecten in omgevingsvisies en programma's: Divisie, Divisietekst, Tekstdeel, Hoofdlijn.

**Locatie-objecten** — Gebied, Lijn, Punt (individueel en als groep), Ambtsgebied. Gekoppeld via Geometrie (GML).

Daarnaast: Kaart/Kaartlaag (presentatie), Regeltekst (koppeling STOP↔OW), Regelingsgebied (totale werkingsgebied), Pons (overgangsrecht bestemmingsplannen).

## Kernbegrippen

- **[[Activiteit]]** — menselijk handelen/nalaten met gevolgen voor de fysieke leefomgeving; eigen NEN3610-ID, naam, groep, hiërarchische positie (bovenliggendeActiviteit)
- **[[Gebiedsaanwijzing]]** — aanwijzing van gebied met type, naam en groep; subtypes Functie en Beperkingsgebied; gekoppeld aan locatie
- **[[Omgevingsnorm]]** — norm met kwantitatieve of kwalitatieve normwaarden per locatie; type, eenheid, groep
- **[[Omgevingswaarde]]** — norm die gewenste staat/kwaliteit van fysieke leefomgeving vastlegt als beleidsdoel; structureel identiek aan Omgevingsnorm
- **[[Juridische Regel]]** — regel met juridische werkingskracht; subtypes RegelVoorIedereen, Instructieregel, Omgevingswaarderegel; gekoppeld aan Activiteit, Gebiedsaanwijzing, Omgevingsnorm
- **[[Toepasbare Regel]]** — vertaling van juridische regels naar interactieve vragenbomen voor burgers in het DSO; subtypes Conclusie, Indieningsvereisten, Maatregelen
- **Regeltekst** — koppelentiteit tussen STOP-artikelen en OW-juridische regels
- **Normwaarde** — individuele kwantitatieve of kwalitatieve waarde binnen een norm, met eigen locatie
- **Omgevingsdocument** — overkoepelend type voor alle Ow-instrumenten (visie, plan, programma, verordening, projectbesluit)
- **Locatie** — geografisch toepassingsgebied; types Gebied, Lijn, Punt, Ambtsgebied en groepen daarvan
- **Idealisatie** — hoe de begrenzing van een locatie moet worden geïnterpreteerd (exact of indicatief)
- **Thema** — kernachtige weergave van de grondgedachte achter een regel

## Relevantie voor bedrijfsarchitectuur

Het IMOW definieert de objecttypen die de gemeente als bronhouder beheert in het DSO. Elk object heeft een eigen NEN3610-identificatie en levenscyclus (actief → beëindigd, vastgesteld → ontwerp). Dit zijn de registreerbare objecten achter het omgevingsplan.

De objecttypen sluiten exact aan op het GGM Omgevingswet-domein (31 entiteiten). Activiteit, Gebiedsaanwijzing, Omgevingsnorm en Omgevingswaarde zijn de sterkste BO-kandidaten: meervoud per gemeente, eigen identiteit, eigen levenscyclus. Juridische Regel en Toepasbare Regel zijn herkenbare Omgevingswet-begrippen die gemeenten actief beheren.

> "Het IMOW beschrijft hoe aantekeningen bij omgevingsbesluiten dienen te worden aangeleverd. Dit informatiemodel specificeert de implementatie van concepten uit het CIM-OW." (IMOW, p. 1)

> "Activiteit: Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd." (IMOW/GGM)

## Bronnen
- [[Sources/Onderwerpen/Omgevingswet/imow-informatiemodel-omgevingswet]]
