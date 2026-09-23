---
type: element
naam: Informatieobject
onderwerp: [Informatiebeheer]
archimate_type: business-object
grondslag: procesobject
ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:
ggm_duplicaat_entiteiten: []
bo_definitie: "Een opzichzelfstaand geheel van gegevensobjecten met een eigen identiteit dat de archiveringsfase is ingegaan: geselecteerd, gewaardeerd en formeel opgenomen in het archiefsysteem met volledige metagegevens."
bo_toelichting: "Informatieobject is de tweede fase in de informatielevenscyclus: het document nadat het de archivering heeft doorlopen. De transitie Document → Informatieobject vindt plaats bij selectie en waardering op grond van de selectielijst en formele opname in het archiefsysteem. Na overbrenging naar de archiefbewaarplaats wordt het een Archiefstuk. Het GGM kent geen aparte entiteit voor deze fase — de archiveringstransitie is een GGM-hiaat."
bo_subtypes: []
bo_synoniemen:
  - Archiefbescheiden
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: Een document wordt een informatieobject na archivering
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|Archiefstuk]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een informatieobject wordt een archiefstuk na overbrenging naar de archiefbewaarplaats
bedrijfsprocessen:
  - Archivering (selectie en waardering)
  - Archiefbeheer
  - Vernietiging of overbrenging
bedrijfsfuncties:
  - Informatiebeheer
---

# Informatieobject

Formeel gearchiveerd informatie-object met eigen identiteit: een [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]] dat de archiveringsfase heeft doorlopen en nu onder archivaal beheer staat met volledige metagegevens. Na overbrenging naar de archiefbewaarplaats wordt het een [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|Archiefstuk]].

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernobject in informatiebeheer en archivering; herkend begrip in de Archiefwet en NA-model |
| Herkenbaar voor experts | ✅ | Records managers, archivarissen, informatiebeheerders werken dagelijks met informatieobjecten |
| Eigen bestaan | ✅ | Bestaat onafhankelijk van het werkproces dat het creëerde; heeft eigen archivale identiteit en registratie |
| Meervoud | ✅ | Gemeente beheert duizenden tot miljoenen informatieobjecten in DMS/RMA en e-depot |
| Eigen levenscyclus | ✅ | Archivering (selectie/waardering) → archivaal beheer → vernietiging of overbrenging |
| Relaties | ✅ | Met Document (voorgaande fase), Archiefstuk (volgende fase), Zaak, Metagegevens |

**Oordeel: 6/6 — Bedrijfsobject.**

## GGM-hiaat

Het GGM kent geen aparte entiteit "Informatieobject". De GGM-entiteit **Document** (abstract) is direct parent van **Archiefstuk**, waardoor de archivale beheerfase tussen taakuitvoering en overbrenging niet als eigen object zichtbaar is:

```
GGM-model:      Document (abstract) ← Archiefstuk
Lifecycle:      Document → Informatieobject → Archiefstuk
```

De NA-term "informatieobject" dekt wat het GGM in de Archiefwet-terminologie "archiefbescheiden" noemt: alle informatie die conform de Archiefwet bewaard en beheerd wordt, ongeacht of ze al overgebracht is.

### Terugmelding GGM

De overgang Document → Informatieobject is een conceptueel gat in het GGM. De archivale beheerfase (vóór overbrenging) ontbreekt als eigen objecttype. Aanbevolen: voeg Informatieobject toe als objecttype in het GGM, als tussenliggende fase in het Model Kern RGBZ of als apart domein Informatiebeheer.

Teruggemeld als #98 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Informatielevenscyclus

| Fase | BO | Transitie | Grondslag |
|---|---|---|---|
| Actief | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | → archivering → | Selectielijst, ZTC2-resultaattype |
| Gearchiveerd | **Informatieobject** | → overbrenging → | Archiefwet art. 12 (20 jaar) |
| Overgebracht | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]] | | Archiefwet, bewaarplaats |

## Definitie (Nationaal Archief)

> "Een opzichzelfstaand geheel van gegevensobjecten met een eigen identiteit. Bijvoorbeeld een document, databasegegeven, e-mailbericht (met bijlagen), (zaak)dossier, internetsite (of een deel ervan), foto/afbeelding, geluidsopname, wiki, blog enzovoort."
> — *Nationaal Archief kennisbank: Het informatieobject*

De NA-definitie beschrijft de informatiekundige identiteit (opzichzelfstaand, eigen identiteit). De aanvulling vanuit de levenscyclus: dit opzichzelfstaand geheel bestaat als informatieobject zodra het de archiveringsfase ingaat.

## Relaties

| Relatie | Bedrijfsobject | Toelichting |
|---|---|---|
| Voorgaande fase | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Document → informatieobject bij archivering |
| Volgende fase | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]] | Informatieobject → archiefstuk bij overbrenging |
| Behoort tot zaak | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Zaakdossier bestaat uit informatieobjecten |
| Beschreven door | *(Metagegevens)* | Metagegevens zijn onlosmakelijk verbonden met het informatieobject (NA-model) |

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiebeheer/overheidsinformatiemodel]]
- [[Wiki/Bronsamenvattingen/Cultuur/memorie-van-toelichting-archiefwet]]
- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
