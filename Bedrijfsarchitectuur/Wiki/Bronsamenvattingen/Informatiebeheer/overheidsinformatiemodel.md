---
type: bronsamenvatting
titel: "Overheidsinformatiemodel — Nationaal Archief kennisbank"
onderwerp: [Informatiebeheer]
datum_ingest: 2026-07-07
---

# Overheidsinformatiemodel (Nationaal Archief)

Het overheidsinformatiemodel is een conceptueel model dat de werelden van archiveren en gegevensmanagement samenvoegt. Het definieert vijf objecten en hun onderlinge relaties als gemeenschappelijk vertrekpunt voor informatie- en dataprofessionals. Het model is in ArchiMate beschreven en typeert [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]] (informatieobject) expliciet als *bedrijfsinformatie*.

## Kernbegrippen

**Ruwe gegevensobject** — Onbewerkte bit-reeksen zonder definitie of context. Worden opgewaardeerd tot gegevensobject zodra er interpretatie aan toegevoegd wordt. Gemeentelijk voorbeeld: ruwe metingen van uitstoot, die pas betekenis krijgen in de context van een omgevingsvergunningaanvraag.

**Gegevensobject** — Objectief waarneembare neerslag van een feit, begrip of aanwijzing, voorzien van begrip en samenhang. Voorbeelden: klantgegevens, registratie van een boom (soort, locatie, gesteldheid). Gegevensobjecten zijn *ondersteunend* aan [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]]: ze worden gecombineerd tot een informatieobject wanneer ze een taakgebonden identiteit krijgen. Het GGM kent geen eigen entiteit voor gegevensobject.

> "Een objectief waarneembare neerslag van een feit, begrip of aanwijzing, op een bepaald medium geschikt voor overdracht, interpretatie, beheer of verwerking door een persoon of apparaat."
> — *Nationaal Archief kennisbank: Het gegevensobject*

**Informatieobject** — Een opzichzelfstaand geheel van gegevensobjecten met een eigen identiteit. Dit is de NA-term voor wat het GGM [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]] noemt. De nieuwe Archiefwet gebruikt "document" als synoniem; de huidige Archiefwet gebruikt "archiefbescheiden".

> "Een opzichzelfstaand geheel van gegevensobjecten met een eigen identiteit. Bijvoorbeeld een document, databasegegeven, e-mailbericht (met bijlagen), (zaak)dossier, internetsite (of een deel ervan), foto/afbeelding, geluidsopname, wiki, blog enzovoort."
> — *Nationaal Archief kennisbank: Het informatieobject*

**Digitaal bestand / Fysiek bestand** — Representatievormen van een informatieobject. Een informatieobject kan meerdere digitale bestanden bevatten (bijv. e-mail + bijlagen). Techniekneutraal begrip.

**Metagegevens** — Gegevens die context, inhoud, structuur en vorm van informatie beschrijven door de tijd heen. Onlosmakelijk verbonden met gegevensobject, informatieobject én digitaal bestand. Geen zelfstandig bedrijfsobject: altijd afhankelijk van het object dat ze beschrijven.

> "Gegevens die context, inhoud, structuur en vorm van informatie en het beheer ervan door de tijd heen beschrijven."
> — *Nationaal Archief kennisbank: Metagegevens (NORA-definitie)*

## Relaties tussen de objecten

```
Ruwe gegevensobject
  → (opwaarderen) → Gegevensobject
                      → (bevat / verwijst naar) → Informatieobject
                                                      ← metagegevens (onlosmakelijk verbonden)
                                                      → Digitaal bestand / Fysiek bestand
```

Metagegevens zijn ook onlosmakelijk verbonden met gegevensobject en digitaal bestand.

## Relevantie voor bedrijfsarchitectuur

**Drie fasen in één levenslijn — geen synoniemen.** Document, Informatieobject en Archiefstuk zijn opeenvolgende fasen:
- [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]] — actieve fase: in gebruik bij taakuitvoering (RGBZ/GGM-terminologie)
- [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/informatieobject|Informatieobject]] — gearchiveerde fase: na selectie en waardering formeel opgenomen in archiefsysteem met volledige metagegevens (NA/Archiefwet-terminologie)
- [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|Archiefstuk]] — overgebrachte fase: na overbrenging naar archiefbewaarplaats

**GGM-hiaat: Informatieobject ontbreekt.** Het GGM modellert de archiveringstransitie niet als aparte entiteit. Document (abstract) is direct parent van Archiefstuk, waardoor de archivale beheerfase (informatieobject) niet zichtbaar is. Informatieobject scoort 6/6 BO-criteria en is een GGM-hiaat.

**ArchiMate-type bevestigd.** Het NA-model beschrijft informatieobjecten als *bedrijfsinformatie* — consistent met archimate_type `business-object` voor alle drie de fasen.

**Gegevensobject: geen nieuw BO.** Het NA-gegevensobject heeft geen GGM-equivalent en scoort onvoldoende op herkenbaarheid en eigen bestaan in gemeentelijk domein. Het is een informatiekundig ondersteunend concept, niet een zelfstandig bedrijfsobject.

**GGM-Metagegevens ≠ NA-metagegevens.** Het GGM-package "Metagegevens" (FormeleHistorie, MaterieleHistorie, InOnderzoek, StrijdigheidOfNietigheid) bevat RGBZ-modelleerpatronen, niet metadata in de NA-zin.

## Bronnen

- [[Sources/informatiebeheer/overheidsinformatiemodel]]
