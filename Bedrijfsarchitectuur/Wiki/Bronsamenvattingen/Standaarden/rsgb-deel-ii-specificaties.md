---
type: bronsamenvatting
titel: "RSGB 2.02 Deel II: Specificaties"
onderwerp: ["Standaarden"]
datum_ingest: 2026-09-23
---

# Bronsamenvatting: RSGB 2.02 Deel II — Specificaties

**Bron:** Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB), versie 2.02, Deel II: Specificaties (VNG Realisatie/KING, april 2018)

## Samenvatting

Waar [[Wiki/Bronsamenvattingen/Standaarden/rsgb-en-informatiemodellen]] (Deel I) het RSGB op hoofdlijnen beschrijft, bevat Deel II de daadwerkelijke gegevenscatalogus: 62 objecttypen met hun attribuutsoorten en relatiesoorten. Voor objecttypen die al in een landelijke basisregistratie-catalogus staan (BAG, BRP, BRK, NHR, WOZ, BGT/IMGeo) is de herkomst "Herkomst objecttype" naar die registratie vermeld — deze zijn in de wiki al via de eigen basisregistratie-bronnen gedekt (bijv. Pand, Verblijfsobject, Kadastraal Perceel, Ingeschreven Persoon, Maatschappelijke Activiteit, Wegdeel).

Het document bevat daarnaast objecttypen met herkomst "Door KING toegevoegd" — dit zijn de RSGB-specifieke aanvullingen die geen deel uitmaken van een basisregistratie, maar die de gemeentelijke informatievoorziening nodig heeft om de basisregistraties te kunnen combineren en te ontsluiten. Twee soorten:

1. **Generalisaties** die meerdere specialisaties bundelen tot één abstract objecttype, zodat gemeenschappelijke attributen en relaties (zoals "ligt in BUURT") maar één keer gespecificeerd hoeven te worden:
   - **SUBJECT** = RECHTSPERSOON of VESTIGING (bundelt alle "met wie communiceert de gemeente"-objecten)
   - **RECHTSPERSOON** = NATUURLIJK PERSOON of NIET-NATUURLIJK PERSOON (specialisatie van SUBJECT)
   - **BENOEMD OBJECT** = GEBOUWD OBJECT of BENOEMD TERREIN ("alle objecten met een adres")
   - **GEBOUWD OBJECT** = VERBLIJFSOBJECT of OVERIG GEBOUWD OBJECT (specialisatie van BENOEMD OBJECT)
   - **BENOEMD TERREIN** = STANDPLAATS, LIGPLAATS of OVERIG TERREIN (specialisatie van BENOEMD OBJECT)
   - **ADRESSEERBAAR OBJECT** = VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS (BAG-generalisatie, referentie-only)
   - **TERREINDEEL** (IMGeo) = generalisatie boven de reeds ge-ingeste BGT-terreindelen

2. **Detailentiteiten/referentietabellen** die de basisregistraties aanvullen met gemeentelijk relevante gegevens die daar zelf niet in voorkomen: bijv. HUISHOUDEN, HUISHOUDENRELATIE, FUNCTIONARIS, INGEZETENE, NIET-INGEZETENE, KADASTRALE GEMEENTE, LAND, NATIONALITEIT, ACADEMISCHE TITEL, OVERIG GEBOUWD OBJECT, OVERIG TERREIN, GEMEENTELIJKE OPENBARE RUIMTE, WOZ-BELANG.

Elk objecttype is gespecificeerd volgens een vast schema: naam, mnemonic (StUF-BG-afkorting), herkomst, definitie, toelichting, unieke aanduiding, en overzichten van attribuutsoorten en relatiesoorten (met per item de herkomst-registratie).

## Kernbegrippen (generalisaties — batch 1)

- **Subject**: RECHTSPERSOON of VESTIGING. "Kenmerkend voor een subject is dat daarmee gecommuniceerd kan worden" (correspondentiegegevens, postadres, telefoon, e-mail). Door KING toegevoegd, ontleend aan GFO BG.
- **Rechtspersoon**: NATUURLIJK PERSOON of NIET-NATUURLIJK PERSOON; specialisatie van Subject. "Verzameling van alle natuurlijke en niet-natuurlijke personen waarvan het gegevensbeheer van essentieel belang is voor de uitoefening van de gemeentelijke taken."
- **Benoemd object**: GEBOUWD OBJECT of BENOEMD TERREIN — "alle objecten met een adres" (nummeraanduiding).
- **Gebouwd object**: VERBLIJFSOBJECT of OVERIG GEBOUWD OBJECT; specialisatie van Benoemd object.
- **Adresseerbaar object**: BAG-generalisatie van VERBLIJFSOBJECT, STANDPLAATS, LIGPLAATS — "enkel opgenomen als referentie naar de BAG", geen eigen attributen.
- **Terreindeel** (IMGeo): "kleinste functioneel onafhankelijk stukje van een door een type landgebruik gekarakteriseerd zichtbaar begrensd stuk grond" — generalisatie boven de BGT-terreindelen ([[Wiki/Bedrijfsobjecten/99-kern/bgt/begroeid-terreindeel]], [[Wiki/Bedrijfsobjecten/99-kern/bgt/onbegroeid-terreindeel]]).

## Relevantie voor bedrijfsarchitectuur

Dit is de bron voor het "RSGBPlus overig"-resthiaat uit `ToDo/ingest-backlog.md`: de detailentiteiten en generalisaties die het GGM-beleidsdomein RSGBPlus bevat maar die niet uit een eigen basisregistratie-catalogus komen. Batch 1 (deze ingest) behandelt de generalisaties; de resterende ~26 detailentiteiten/referentietabellen volgen in een latere batch.

## Citaten

> "Dit deel II bevat de specificaties van de componenten waaruit versie 2.02 van het RSGB is opgebouwd: objecttypen (hoofdstuk 1), attribuutsoorten en relatiesoorten (hoofdstuk 2)." (bron: RSG_Basisgegevens_2.02_deel_II)

> "Het betreft de verzameling van alle natuurlijke personen, niet-natuurlijke personen en vestigingen waarvan het gegevensbeheer van essentieel belang is voor de uitoefening van de gemeentelijke taken." (SUBJECT, bron: RSG_Basisgegevens_2.02_deel_II)

> "Een gebouwd object is de groepering van de authentieke verblijfsobjecten en de overige gebouwde objecten [...] voor zover dat door de gemeente als relevant wordt gezien." (GEBOUWD OBJECT, bron: RSG_Basisgegevens_2.02_deel_II)

## Bronnen

- [[Sources/Standaarden/RSG_Basisgegevens_2.02_deel_II_(in_gebruik)]]
