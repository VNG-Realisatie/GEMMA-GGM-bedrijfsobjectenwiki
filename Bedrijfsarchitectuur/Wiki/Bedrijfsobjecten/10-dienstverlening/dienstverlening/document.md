---
type: element
naam: Document
onderwerp: [Dienstverlening, Informatiebeheer]
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
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: "KING (NEN 2082)"
ggm_gemma_naam: Document
ggm_gemma_guid: "10eaa33f-03bf-42b4-9310-56add2cb5a7b"
ggm_gemma_definitie: "Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-10eaa33f-03bf-42b4-9310-56add2cb5a7b"
ggm_gemma_bron:
ggm_gemma_alternate_name:
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Document** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Brondocumenten** (detail) — Detailgegeven
  - **Documenttype** (classificatie) — Typering/referentietabel
  - **EnkelvoudigDocument** (detail) — Detailgegeven
  - **Identificatiekenmerk** (detail) — Detailgegeven (geassocieerd met BO)
  - **MOOR-melding** (detail) — Detailgegeven
  - **Proces-verbaal-MOOR-melding** (detail) — Detailgegeven (geassocieerd met BO)
  - **Rapportagemoment** (detail) — Detailgegeven (geassocieerd met BO)
  - **SamengesteldDocument** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT."
bo_toelichting: "Document is de actieve fase: het informatieobject in gebruik bij taakuitvoering. Zodra een document de archiveringsfase ingaat (selectie, waardering, formele opname in het archiefsysteem), wordt het een Informatieobject. Na overbrenging naar de archiefbewaarplaats is het een Archiefstuk. Document, Informatieobject en Archiefstuk zijn daarmee drie fasen in één levenslijn — geen synoniemen."
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
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/informatieobject|Informatieobject]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: Na archivering (selectie, waardering) wordt een document een informatieobject
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|Archiefstuk]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: Na overbrenging naar de archiefbewaarplaats wordt een informatieobject een archiefstuk (Archiefwet)
bedrijfsprocessen:
  - Documentregistratie
  - Zaakafhandeling
  - Archivering
bedrijfsfuncties:
  - Informatiebeheer
  - Dienstverlening
---

# Document

Informatiedrager met eigen identiteit ongeacht vorm, ontvangen of opgemaakt bij de uitvoering van gemeentelijke taken. Document is de **actieve fase** in de informatielevenscyclus: het object zolang het in gebruik is bij taakuitvoering (zaakgericht werken, dienstverlening). Zodra het de archiveringsfase ingaat, transformeert het naar een [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/informatieobject|Informatieobject]]. Na overbrenging naar de archiefbewaarplaats wordt het een [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|Archiefstuk]].

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

## Informatielevenscyclus

Document, Informatieobject en Archiefstuk zijn drie fasen in één levenslijn — geen synoniemen.

| Fase | BO | Regime | Domein |
|---|---|---|---|
| **Actief** | Document | Wob/Woo, zaakgericht werken | Dienstverlening |
| **Gearchiveerd** | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/informatieobject\|Informatieobject]] | Archiefwet, selectielijst | Informatiebeheer |
| **Overgebracht** | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]] | Archiefwet-openbaarheid | Erfgoed |

De transitie **Document → Informatieobject** vindt plaats bij archivering: selectie en waardering op grond van de selectielijst, formele opname in het archiefsysteem met volledige metagegevens. Het GGM modelleert dit niet als aparte entiteit — Informatieobject is een GGM-hiaat.

De transitie **Informatieobject → Archiefstuk** vindt plaats bij overbrenging naar de archiefbewaarplaats (na 20 jaar conform Archiefwet 1995). Het **resultaattype** (ZTC2) bepaalt of het zaakdossier vernietigd of overgebracht wordt.

In het GGM erft Archiefstuk van Document (abstract), wat de doorlopende identiteit door de levenscyclus bevestigt.

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

## Gegevensobject als ondersteunend begrip

Het Nationaal Archief Overheidsinformatiemodel introduceert het **gegevensobject** als tussenlaag onder het informatieobject: een feit of aanwijzing met begrip en samenhang, maar nog zonder opzichzelfstaande archivale identiteit. Voorbeelden zijn klantgegevens of een boomregistratie (soort, locatie, gesteldheid). Gegevensobjecten worden gecombineerd tot een document zodra ze een taakgebonden identiteit krijgen (bijv. een vergunningaanvraag samengesteld uit persoonsgegevens + meetgegevens + locatiegegevens).

Het gegevensobject is **geen zelfstandig bedrijfsobject**: het heeft onvoldoende herkenbaarheid in het gemeentelijk domein en mist een expliciete levenscyclus als eigenstandige entiteit. Het GGM kent dit concept niet als objecttype.

Het NA-model legt ook de relatie met **metagegevens** vast: metagegevens zijn onlosmakelijk verbonden met zowel het gegevensobject als het document/informatieobject. In gemeentelijk verband zijn dit de registratiemetadata (documentidentificatie, datum, auteur, vertrouwelijkheidaanduiding) die de GGM-entiteit Document als attributen heeft.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Cultuur/memorie-van-toelichting-archiefwet]]
- [[Wiki/Bronsamenvattingen/Informatiebeheer/overheidsinformatiemodel]]
