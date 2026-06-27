---
type: bedrijfsobject
naam: Register (omgevingsplan)
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
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

ggm_duplicaat_entiteiten: []

bo_definitie: "Verzameling van geordende feitelijke informatie over een onderwerp, beheerd door de gemeente ten behoeve van de toepassing van planregels in het omgevingsplan."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[VTH-zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Register levert feitelijke informatie voor toetsing van activiteiten"
  - type: associatie
    bedrijfsobject: "[[Inspectie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Inspectieresultaten kunnen register actualiseren"
bedrijfsprocessen: [vergunningverlening, toezicht en handhaving, omgevingsplanbeheer]
bedrijfsfuncties: [ruimtelijke ordening, vergunningverlening]
---

## BO-criteria toetsing

| Criterium | Score | Toelichting |
|---|---|---|
| Herkenbaarheid | ✅ | Herkenbaar concept, jurisprudentie ABRvS (Lage Weide, Oosterwold), VNG-factsheet |
| Meervoud | ✅ | Meerdere per gemeente: register studentenhuisvesting, geurruimteboekhouding, bodemkwaliteit, monumenten |
| Levenscyclus | ✅ | Instellen → vullen → actualiseren → (opheffen); jaarlijkse verantwoording aan raad |
| Relaties | ✅ | Met omgevingsplan (planregels), activiteiten, beleidsregels, VTH-zaken |
| Attributen | ✅ | Type (statisch/dynamisch), thema, scope, beheerder, grondslag (planregel), openbaarheidsvorm |
| Data-object | ✅ | B&W beheert actief, openbaar, elektronisch raadpleegbaar, juridisch toetsbaar |

## Beschrijving

Een register bij het omgevingsplan is een door de gemeente beheerde verzameling feitelijke informatie over een onderwerp in de fysieke leefomgeving. Het dient de toepassing van planregels: het biedt de feitelijke basis voor het toetsen van activiteiten, het verlenen van vergunningen en het handhaven.

Een register is vormvrij en geen omgevingsdocument — het is niet opgenomen in het Digitaal Stelsel Omgevingswet (DSO). Het is een op zichzelf staand instrument dat buiten de planregels om wordt geactualiseerd. Een wijziging van een register is geen wijziging van het omgevingsplan.

Er zijn twee typen: een **statisch register** legt de situatie vast op het moment van een wijzigingsbesluit, terwijl een **dynamisch register** continu wordt bijgewerkt en de actuele stand weergeeft. Het type hangt af van de planregel.

Een register kan op vijf manieren in planregels worden opgenomen: als beheerobject, als toetsingsverwijzing, als onderdeel van een norm, als toepassingsbereikbepaler, of als onderdeel van een beleidsregel. Ook zonder verwijzing in planregels kan een register worden ingezet bij besluitvorming (art. 3:2 Awb).

## Subtypes

Herkende specialisaties van Register. Geen apart BO.

- **Statisch register** — snapshot op een bepaald moment, gekoppeld aan wijzigingsbesluit
- **Dynamisch register** — continu bijgewerkt, beweegt mee met ontwikkelingen

## Procesbron

Het register ontstaat in het proces van omgevingsplanbeheer. De gemeente stelt een register in wanneer planregels feitelijke informatie vereisen voor hun toepassing. B&W zijn bestuurlijk en juridisch verantwoordelijk voor juistheid en volledigheid.

Juridische grondslag: art. 3:2 Awb (zorgvuldigheidsbeginsel), art. 4.1/4.2 Omgevingswet, art. 20.10 Ow (optionele AMvB). Jurisprudentie: ABRvS Utrecht – Lage Weide (ECLI:NL:RVS:2022:2753), ABRvS Almere – Oosterwold (ECLI:NL:RVS:2017:1447).

## Relaties

| Gerelateerd BO | Relatie | Richting | Toelichting |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | levert informatie voor | naar-dit-BO | Feitelijke basis voor toetsing activiteiten |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]] | wordt geactualiseerd door | naar-dit-BO | Inspectieresultaten kunnen register bijwerken |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/bevinding\|Bevinding]] | kan leiden tot wijziging van | naar-dit-BO | Bevindingen kunnen feitelijke situatie wijzigen |

## Bronnen

- [[Wiki/Bronsamenvattingen/Omgevingswet/factsheet-omgevingsplan-register]]

## Terugmelding GGM

Register (omgevingsplan) ontbreekt in het GGM. Het is expliciet géén omgevingsdocument. Het GGM-beleidsdomein Omgevingswet (31 entiteiten) bevat geen entiteit voor dit concept. Het is een informatieobject dat gemeenten actief beheren bij de uitvoering van de Omgevingswet, maar dat buiten het DSO valt.

Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
