---
type: bedrijfsobject
naam: Partijsubsidie
onderwerp: [Bestuur]
archimate_type: business-object
grondslag: procesobject
ggm_entiteit: "~"
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: "Politiek (niet in GGM)"
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "~"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Door de gemeente verstrekte subsidie aan een decentrale politieke partij ter ondersteuning van de partijorganisatie en versterking van de lokale democratie."
bedrijfsprocessen:
  - Subsidieaanvraag beoordelen
  - Subsidie vaststellen en uitbetalen
  - Transparantieverplichtingen monitoren
bedrijfsfuncties:
  - Democratische ondersteuning
  - Subsidieverstrekking
relaties:
  - type: associatie
    bedrijfsobject: "[[Verkiezing]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: Subsidiebedrag is gebaseerd op de zetelverdeling uit de laatstgehouden verkiezing
---

# Partijsubsidie

## BO-criteria toetsing

| Criterium | Van toepassing? | Opmerkingen |
|---|---|---|
| Betekenis binnen domein | ✅ | Instrument ter versterking van lokale democratie; door Tweede Kamer geïnitieerd, door gemeenten uitgevoerd |
| Herkenbaar voor experts | ✅ | Raadsleden, griffiers, subsidieambtenaren en partijbestuurders herkennen dit direct |
| Eigen bestaan | ✅ | Zelfstandig besluit van het college, eigen regeling, eigen geldstroom |
| Kan in meervoud bestaan | ✅ | Elke gemeente verstrekt meerdere partijsubsidies (één per partij met raadszetel) |
| Eigen levenscyclus | ✅ | Regeling vaststellen → aanvraag ontvangen → beoordelen → vaststellen → uitbetalen → verantwoording monitoren |
| Relaties met andere objecten | ✅ | Relatie met [[Verkiezing]] (zetelverdeling), politieke partij (aanvrager), ASV (juridische grondslag) |

**Conclusie:** 6/6 criteria ✅ — sterke BO-kandidaat.

## Beschrijving

Een partijsubsidie is een door de gemeente verstrekte financiële bijdrage aan een decentrale politieke partij — een lokale partij of lokale afdeling van een landelijke partij met ten minste één raadszetel. De subsidie is bestemd voor de partijorganisatie: politieke vorming, ledenwerving, kandidaatwerving, informatievoorziening en verkiezingscampagnes.

De partijsubsidie is nadrukkelijk iets anders dan fractieondersteuning (art. 33 Gemeentewet). Het zijn twee gescheiden geldstromen met verschillende aanvragers (partijen vs. fracties), verschillende doelen (partijorganisatie vs. raadswerk) en verschillende juridische grondslagen.

Het subsidiebedrag wordt berekend per raadszetel, in zes tariefklassen op basis van het inwoneraantal van de gemeente (€488–€1.195 per zetel). Het college stelt de regeling vast en ambtenaren voeren uit; de griffie heeft geen rol.

Subsidieontvangers hebben transparantieverplichtingen: openbaarmaking van statuten, bestuurssamenstelling, kandidaatstellingsprocedure, financieel verslag en activiteitenverslag. Giften boven €250 cumulatief per donateur per jaar moeten worden geregistreerd.

De huidige regeling is tijdelijk — een pilot vooruitlopend op de Wet op de politieke partijen (Wpp, streefdatum 1 januari 2028). Bij inwerkingtreding van de Wpp vervalt de gemeentelijke regeling van rechtswege.

## Procesbron

Dit BO ontstaat in het subsidieproces voor decentrale politieke partijen:

1. **College stelt subsidieregeling vast** op basis van VNG-modelverordening en ASV-delegatiegrondslag
2. **Partij dient aanvraag in** met geregistreerde aanduiding, aantal zetels, IBAN en organisatiegegevens
3. **Subsidieambtenaar beoordeelt** aanvraag op volledigheid en zetelverdeling
4. **College stelt subsidie direct vast** (geen voorafgaande verlening of verantwoording)
5. **Financiële afdeling betaalt uit**
6. **Partij publiceert** financieel verslag (uiterlijk 30 juni) en activiteitenverslag (uiterlijk 31 augustus)

Het GGM modelleert generieke subsidie-entiteiten onder taakveld 9 (Subsidie, Subsidieaanvraag, Subsidiebeschikking). De partijsubsidie wijkt af van het generieke subsidieproces: directe vaststelling (geen verlening→verantwoording→vaststelling), zetelafhankelijk bedrag, en transparantieverplichtingen die verder gaan dan de standaard ASV.

## BO-definitie

> **Partijsubsidie** — Door de gemeente verstrekte subsidie aan een decentrale politieke partij ter ondersteuning van de partijorganisatie en versterking van de lokale democratie, met bedragen per raadszetel en specifieke transparantieverplichtingen.

## Relaties

| Relatie | Object | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[Verkiezing]] | 1 | Zetelverdeling uit laatstgehouden verkiezing bepaalt aanspraken en bedragen |

## Bedrijfsprocessen

1. **Subsidieregeling vaststellen** — college neemt collegevoorstel aan op basis van VNG-model
2. **Subsidieaanvraag beoordelen** — controleren zetelverdeling, rechtsvorm, volledigheid gegevens
3. **Subsidie vaststellen en uitbetalen** — directe vaststelling, uitbetaling door financiële afdeling
4. **Transparantie monitoren** — controleren publicatie financieel verslag en activiteitenverslag

## Bedrijfsfuncties

- **Democratische ondersteuning** — versterking van de positie van decentrale politieke partijen
- **Subsidieverstrekking** — financiële ondersteuning vanuit gemeentelijke middelen

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/model-subsidieregeling-politieke-partijen]]
- [[Wiki/Bronsamenvattingen/Bestuur/implementatiehandleiding-subsidieregeling-politieke-partijen]]

## Terugmelding GGM

Het GGM heeft geen entiteiten voor politieke partijen of partijfinanciering onder taakveld 0. De entiteit "Raadslid" (Griffie-domein) heeft een attribuut "fractie" maar partijen zijn niet als zelfstandig object gemodelleerd. Met de komst van de Wpp en de gemeentelijke uitvoeringsrol wordt dit een structureel hiaat.
