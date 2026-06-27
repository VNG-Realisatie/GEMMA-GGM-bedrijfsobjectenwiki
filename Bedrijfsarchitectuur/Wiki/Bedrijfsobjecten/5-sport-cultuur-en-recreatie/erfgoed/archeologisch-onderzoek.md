---
type: bedrijfsobject
naam: Archeologisch onderzoek
domein:
- Cultuur
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Project
ggm_guid: EAID_7087D528_7024_4569_876A_C4605A00546D
ggm_uml_type: Class
ggm_beleidsdomein: Organisatie-indeling
ggm_taakveld: 9 Interne Organisatie
ggm_diagram: []
ggm_diagram_ids:
- EAPK_2883DC11_62ED_42cd_A0D6_855258F32079
ggm_definitie: Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat.
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: Project
ggm_gemma_guid: 132ee7cb-0cfc-47d1-a50c-dd7e3a656651
ggm_gemma_definitie: Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat.
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-132ee7cb-0cfc-47d1-a50c-dd7e3a656651
ggm_gemma_bron: ''
ggm_gemma_alternate_name: Project (Organisatie)

ggm_duplicaat_entiteiten:
  - "EAID_E42A32F7_262F_4005_9EB9_4674B76E8825"
  - "EAID_E1FAE16A_42AE_4b7d_88FC_F429079D1C4D"

bo_definitie: Archeologisch onderzoeksproject dat door of in opdracht van de gemeente als bevoegd gezag wordt uitgevoerd, met bijbehorende besluiten, documentatie en vondsten.
bedrijfsprocessen:
- Archeologisch onderzoek
- Vergunningverlening
- Selectiebesluit
bedrijfsfuncties:
- Erfgoedbeheer
- Vergunningverlening
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vindplaats|Archeologische vindplaats]]'
  richting: van-dit-BO
  kardinaliteit: 0..1
  beschrijving: Een onderzoek vindt plaats op een vindplaats
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vondst|Archeologische vondst]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: Een onderzoek levert vondsten op
---

# Archeologisch onderzoek

Onderzoeksproject waarbij de gemeente als bevoegd gezag archeologisch veldwerk begeleidt of zelf uitvoert. Omvat het geheel van opgravingsactiviteiten, documentatie en besluiten binnen een afgebakend gebied en tijdsperiode.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Gemeente voert en begeleidt onderzoek als wettelijke taak |
| Herkenbaar voor experts | ✅ | Standaardbegrip in erfgoeddomein |
| Eigen bestaan | ✅ | Een onderzoeksproject bestaat als afgebakend geheel |
| Meervoud | ✅ | Utrecht heeft 50 jaar aan onderzoeksprojecten |
| Eigen levenscyclus | ✅ | Programma van eisen → veldwerk → rapportage → depot |
| Relaties | ✅ | Met vindplaats, vondsten, besluiten, locatie |

## GGM-bron

> **Project**: Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat.
> — *GGM v2.5.1, Archeologie (taakveld 5 Sport, Cultuur en Recreatie)*

**Entiteit:** Project
**Attributen:** projectCD, naam, datumStart, datumEinde, naamcode, toponiem, locatie, coordinaten, jaarVan, jaarTot, trefwoorden
**Matchsterkte:** sterk

De GGM-definitie is generiek ("project"); in het GGM-archeologie-model is dit specifiek een archeologisch onderzoeksproject. De naamkeuze "Archeologisch onderzoek" sluit beter aan bij het gemeentelijk taalgebruik.

### Aggregatie

De operationele opgravingshiërarchie (Put → Vlak → Spoor → Vulling) en onderzoekstechnieken (boring) zijn in het GGM gedetailleerd uitgewerkt. Op bedrijfsniveau zijn dit details van het onderzoeksproject, niet zelfstandige bedrijfsobjecten. Ook het **Archeologiebesluit** (EAID_836E51BF, "professioneel oordeel") is een uitkomst van het adviesproces, geaggregeerd in dit BO.

> "We bewaken en bestuderen het Utrechtse bodemarchief door te adviseren bij voorgenomen werkzaamheden in de ondergrond, door archeologisch onderzoek als bevoegd gezag te begeleiden en door zelf onderzoek uit te voeren." (bron: [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht|Erfgoednota 'Utrechts erfgoed verbindt mensen en tijden']])

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Vindt plaats op | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vindplaats\|archeologische-vindplaats]] | Vindplaats → Project [1] | Geen |
| Levert op | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vondst\|archeologische-vondst]] | Project → Put → Vlak → Spoor → Vulling → Vondst (indirect) | Ingekort naar directe relatie |
| Heeft besluiten | *(Archeologiebesluit — geaggregeerd)* | Project → Archeologiebesluit [0..*] | Geaggregeerd in dit BO |

## Bedrijfsprocessen

- **Archeologisch onderzoek**: veldwerk, documentatie, rapportage
- **Vergunningverlening**: adviseren over archeologische waarden bij vergunningaanvragen
- **Selectiebesluit**: beoordeling noodzaak onderzoek op basis van beleidskaart

## Bedrijfsfuncties

- Erfgoedbeheer
- Vergunningverlening

## Bronnen

- [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht]]
