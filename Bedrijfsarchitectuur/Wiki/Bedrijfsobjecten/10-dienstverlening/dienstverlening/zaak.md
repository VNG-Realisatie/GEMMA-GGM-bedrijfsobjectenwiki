---
type: bedrijfsobject
naam: Zaak
domein: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Zaak
ggm_guid: EAID_649EFD86_ED52_4293_8577_DBE5445845BF
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Catalogus RGBZ]
ggm_diagram_ids: [EAID_A7DD83EA_D15D_46a9_9F35_4005FE06648A]
ggm_definitie: "Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GFO Zaken"
ggm_gemma_naam: Zaak
ggm_gemma_guid: "7d5124d4-f23d-432d-ad5a-dc7c1b0fac44"
ggm_gemma_definitie: "Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-7d5124d4-f23d-432d-ad5a-dc7c1b0fac44"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
bo_definitie: "Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Een zaak kent een of meer documenten (informatieobjecten)
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|Aanvraag of melding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een aanvraag of melding kan leiden tot een zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst|Product of dienst]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: Een zaak levert een product of dienst
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak|Balieafspraak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een balieafspraak kan betrekking hebben op een zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit|Besluit]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Besluiten zijn uitkomst van een zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype|Zaaktype]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: Elke zaak is van een zaaktype
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact|Klantcontact]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Klantcontacten hebben betrekking op een zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker|Medewerker]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Medewerkers behandelen de zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling|Betaling]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Betalingen gekoppeld aan de zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces|Bedrijfsproces]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Bedrijfsprocessen uitgevoerd binnen de zaak
bedrijfsprocessen:
  - Zaakafhandeling
  - Dienstverleningsproces
bedrijfsfuncties:
  - Zaakgericht werken
  - Dienstverlening
---

# Zaak

Centrale werkeenheid in het gemeentelijk dienstverleningsproces. Een zaak bundelt alle informatie over de afhandeling van een aanvraag, melding of ambtshalve handeling: documenten, betrokkenen, statussen, besluiten en het resultaat. Het concept komt uit het GFO Zaken (2004) en is gestandaardiseerd in het RGBZ.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernobject van zaakgericht werken, organiserend principe voor gemeentelijke dienstverlening |
| Herkenbaar voor experts | ✅ | Elke gemeenteambtenaar kent het zaakconcept; het is de basis van de informatiehuishouding |
| Eigen bestaan | ✅ | Een zaak bestaat onafhankelijk met eigen zaakidentificatie |
| Meervoud | ✅ | Gemeenten verwerken jaarlijks honderdduizenden tot miljoenen zaken |
| Eigen levenscyclus | ✅ | Aanleiding → registratie → behandeling → besluit → afsluiting → archivering |
| Relaties | ✅ | Met Document, AanvraagOfMelding, Besluit, Status, Betrokkene, ProductOfDienst |

## GGM-bron

> **Zaak**: Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Zaak
**Matchsterkte:** exact
**Herkomst:** GFO Zaken → RGBZ 1.0 → GGM

## Zaakdossier en archivering

Het **zaakdossier** is geen apart objecttype maar een impliciet concept: de verzameling van alle documenten (informatieobjecten) bij een zaak, samen met de zaakkenmerken. Bij afsluiting van de zaak bepaalt het **resultaattype** (ZTC2) het archiefregime:

- **Vernietigen** — na afloop van de archiefactietermijn worden het zaakdossier en bijbehorende documenten vernietigd
- **Bewaren** — na afloop van de overbrengingstermijn (20 jaar, Archiefwet 1995) worden de documenten overgebracht naar de archiefbewaarplaats

Dit is het scharnierpunt tussen zaakgericht werken (informatiebeheer) en archief (erfgoed): documenten die als informatieobject in een zaakdossier zitten, worden na overbrenging [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|archiefstukken]].

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Kent documenten | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Zaak → Document [1..*] | Alle informatieobjecten bij de zaak |
| Gestart door | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | AanvraagOfMelding → Zaak [0..*] | Aanleiding voor de zaak |
| Levert | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|Product of dienst]] | Zaak → Producttype [1] | Resultaat van de zaak |
| Heeft betrekking op | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]] | Balieafspraak → Zaak [0..1] | Afspraak gekoppeld aan zaak |
| Is uitkomst van | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit\|Besluit]] | Besluit → Zaak [1] | Beschikking, vergunning, etc. |
| Is van type | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Zaak → Zaaktype [1] | Configuratie en archiefregime |
| Klantcontacten | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Klantcontact → Zaak [0..1] | Contactmomenten bij de zaak |
| Behandeld door | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Zaak → Medewerker [0..*] | Afhandelend medewerker |
| Betalingen | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling\|Betaling]] | Zaak → Betaling [0..*] | Financiële transacties |
| Processen | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]] | Bedrijfsproces → Zaak [1..*] | Procesuitvoering |
| Is deelzaak van | Zaak | Zaak → Zaak [0..1] | Hiërarchie van hoofd- en deelzaken |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel]]
