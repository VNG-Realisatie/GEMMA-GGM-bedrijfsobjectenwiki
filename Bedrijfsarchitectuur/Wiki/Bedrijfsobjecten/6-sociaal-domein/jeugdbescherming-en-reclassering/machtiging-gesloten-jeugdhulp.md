---
type: element
naam: Machtiging Gesloten Jeugdhulp
onderwerp: [Maatschappelijke Ondersteuning]
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

bo_definitie: "Rechterlijke machtiging voor opname en verblijf van een jeugdige in een gesloten accommodatie vanwege ernstige opgroei- of opvoedingsproblemen."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft jeugdige"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/kinderbeschermingsmaatregel|Kinderbeschermingsmaatregel]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "kan voortvloeien uit kinderbeschermingsmaatregel"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan|Hulpverleningsplan]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "vereist hulpverleningsplan"
bedrijfsprocessen: [gesloten jeugdhulp organiseren, machtiging aanvragen]
bedrijfsfuncties: [jeugdbescherming, toegang sociaal domein]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Rechterlijke machtiging die de gemeente registreert en op basis waarvan zij handelt |
| Besproken op bestuurlijk niveau | ✅ | Politiek gevoelig; aantallen in jaarverslagen en raadsinformatie |
| Vastgelegd in systemen | ✅ | Geregistreerd in jeugd-applicatie met type, datum en duur |
| Eigen attributen | ✅ | Type (gewoon/spoed/voorwaardelijk), datum, duur, instemming gedragswetenschapper |
| Relaties met andere objecten | ✅ | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/kinderbeschermingsmaatregel\|Kinderbeschermingsmaatregel]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan\|Hulpverleningsplan]] |
| Levenscyclus | ✅ | Verzoek → verlening → verlenging → beëindiging/verval |

## Beschrijving

De machtiging gesloten jeugdhulp is een rechterlijke beslissing die opname en verblijf in een gesloten accommodatie mogelijk maakt. De kinderrechter verleent de machtiging als jeugdhulp noodzakelijk is vanwege ernstige opgroei- of opvoedingsproblemen, de opneming noodzakelijk is om onttrekking te voorkomen, en er geen minder ingrijpende mogelijkheden zijn (art. 6.1.2).

De gemeente is niet de verstrekkende instantie — dat is de kinderrechter — maar registreert de machtiging, bekostigt de plaatsing en is verantwoordelijk voor de jeugdhulp die eruit voortvloeit (art. 2.4 lid 2b).

## Specialisaties

Herkende specialisaties van Machtiging Gesloten Jeugdhulp. Gevonden in de Jeugdwet. Geen apart BO.

- **Spoedmachtiging** — verleend als reguliere machtiging niet kan worden afgewacht; geldt direct (art. 6.1.3)
- **Voorwaardelijke machtiging** — verleend onder voorwaarden; bij niet-naleving kan de jeugdige alsnog worden opgenomen (art. 6.1.4)

## Procesbron

De machtiging ontstaat via een verzoek aan de kinderrechter, doorgaans door de gecertificeerde instelling of de Raad voor de Kinderbescherming. Het verzoek vereist instemming van een gekwalificeerde gedragswetenschapper die de jeugdige kort tevoren heeft onderzocht.

> "De kinderrechter kan op verzoek een machtiging verlenen om een jeugdige in een gesloten accommodatie te doen opnemen en te doen verblijven." (art. 6.1.2 lid 1)

> "Een machtiging kan slechts worden verleend indien naar het oordeel van de kinderrechter: a. jeugdhulp noodzakelijk is in verband met ernstige opgroei- of opvoedingsproblemen die de ontwikkeling van de jeugdige naar volwassenheid ernstig belemmeren" (art. 6.1.2 lid 2)

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | betreft jeugdige | naar dit BO | Jeugdwet art. 6.1.2 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/kinderbeschermingsmaatregel\|Kinderbeschermingsmaatregel]] | kan voortvloeien uit OTS/voogdij | naar dit BO | Jeugdwet art. 6.1.2 lid 3 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan\|Hulpverleningsplan]] | vereist hulpverleningsplan | van dit BO | Jeugdwet art. 6.1.2 lid 4b |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | bekostiging via beschikking | naar dit BO | Jeugdwet art. 2.4 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]

## Terugmelding GGM

Het GGM modelleert geen entiteit voor machtigingen gesloten jeugdhulp. Het beleidsdomein Jeugdbescherming en reclassering bevat alleen Zorgmelding-gerelateerde entiteiten. De machtiging is een zelfstandig registratieobject met eigen attributen (type, duur, instemming) en levenscyclus dat in het GGM ontbreekt.
