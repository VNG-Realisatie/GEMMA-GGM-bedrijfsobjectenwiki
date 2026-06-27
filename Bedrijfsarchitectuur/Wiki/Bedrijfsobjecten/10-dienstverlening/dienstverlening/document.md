---
type: bedrijfsobject
naam: Document
domein: [Dienstverlening, Informatiebeheer]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Document
ggm_guid: EAID_5641C50A_C0FA_4e71_B07B_26C7B1CE94ED
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Catalogus RGBZ]
ggm_diagram_ids: [EAID_A7DD83EA_D15D_46a9_9F35_4005FE06648A]
ggm_definitie: "Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "KING (NEN 2082)"
ggm_gemma_naam: Document
ggm_gemma_guid: "10eaa33f-03bf-42b4-9310-56add2cb5a7b"
ggm_gemma_definitie: "Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-10eaa33f-03bf-42b4-9310-56add2cb5a7b"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
bo_definitie: "Informatiedrager met eigen identiteit, ongeacht vorm, die de gemeente ontvangt of opmaakt bij de uitvoering van taken."
bo_subtypes:
  - naam: Enkelvoudig document
    omschrijving: Document dat als één geheel wordt behandeld en beheerd
    ggm_entiteit: EnkelvoudigDocument
    ggm_guid: EAID_547FD48D_F885_4816_BCFA_4048995C8D83
  - naam: Samengesteld document
    omschrijving: Document dat uit twee of meer enkelvoudige documenten bestaat
    ggm_entiteit: SamengesteldDocument
    ggm_guid: EAID_47DA1FC8_F181_41bc_B16A_CE80D2CA13B1
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een zaak kent een of meer documenten
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|Aanvraag of melding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een aanvraag of melding heeft documenten als bijlagen
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|Archiefstuk]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: Na overbrenging naar de archiefbewaarplaats wordt een document een archiefstuk (Archiefwet)
bedrijfsprocessen:
  - Documentregistratie
  - Zaakafhandeling
  - Archivering
bedrijfsfuncties:
  - Informatiebeheer
  - Dienstverlening
---

# Document

Informatiedrager met eigen identiteit ongeacht vorm, ontvangen of opgemaakt bij de uitvoering van gemeentelijke taken. De GGM-entiteit heet "Document" (RGBZ 1.0-terminologie); in de ZGW API's en ZTC2 is dezelfde entiteit hernoemd naar "informatieobject" om uit te drukken dat het breder is dan het dagelijkse begrip "document": ook een XML-bericht, dataset, foto, geluidsopname, CAD-tekening of e-mail met bijlagen is een informatieobject.

De definities zijn identiek. In de praktijk gebruikt de gemeente het woord "document" voor de dagelijkse informatiedragers, maar het RGBZ-concept omvat alles wat aan een zaak gerelateerd kan worden — ook informatie die niet in het RGBZ gespecificeerd is (conform de Baseline Informatiehuishouding).

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernelement van zaakgericht werken en informatiebeheer |
| Herkenbaar voor experts | ✅ | Universeel begrip; informatiespecialisten, archivisten, behandelaars kennen dit |
| Eigen bestaan | ✅ | Elk document heeft een eigen identificatie (documentnummer) |
| Meervoud | ✅ | Miljoenen documenten per gemeente per jaar |
| Eigen levenscyclus | ✅ | Creatie/ontvangst → registratie → gebruik → archivering → vernietiging of overbrenging |
| Relaties | ✅ | Met Zaak, Documenttype, AanvraagOfMelding, Besluit, Identificatiekenmerk |

## GGM-bron

> **Document**: Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Document
**Matchsterkte:** exact
**Herkomst:** KING (NEN 2082) → RGBZ 1.0 → GGM

## Document / informatieobject en archiefstuk

Document (GGM) en informatieobject (ZGW API's) zijn dezelfde entiteit met dezelfde definitie. De naamwijziging maakt expliciet dat het concept breder is dan "document" in dagelijks spraakgebruik.

| Fase | Naam | Regime | Domein |
|---|---|---|---|
| **Lopend** | Document / informatieobject | Wob, zaakgericht werken | Dienstverlening |
| **Overgebracht** | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]] | Archiefwet-openbaarheid | Erfgoed + informatiebeheer |

Het GGM modelleert de generalisatie Archiefstuk → Document (abstract), wat bevestigt dat een archiefstuk een specialisatie is van document/informatieobject.

Het scharnierpunt is de **overbrenging** naar de archiefbewaarplaats (na 20 jaar, Archiefwet 1995). Het **resultaattype** (ZTC2) bepaalt of het zaakdossier met zijn documenten/informatieobjecten wordt vernietigd of overgebracht.

## Subtypes

- **Enkelvoudig document** — Document dat als één geheel wordt behandeld en beheerd
- **Samengesteld document** — Document dat uit twee of meer enkelvoudige documenten bestaat

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Hoort bij zaak | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Zaak → Document [1..*] | Documenten vormen samen het zaakdossier |
| Bijlage bij | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | AanvraagOfMelding → Document [0..*] | Aanvraag met bijgevoegde documenten |
| Wordt archiefstuk | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]] | Archiefstuk → Document (generalisatie) | Na overbrenging conform Archiefwet |
| Is vastlegging van | *(Besluit)* | Besluit → Document [0..*] | Een besluit wordt vastgelegd als document |
| Is van type | *(Documenttype)* | Document → Documenttype [1] | Classificatie |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Cultuur/memorie-van-toelichting-archiefwet]]
