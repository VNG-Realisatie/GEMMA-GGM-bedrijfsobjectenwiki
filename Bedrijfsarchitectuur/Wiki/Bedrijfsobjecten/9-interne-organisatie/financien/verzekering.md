---
type: element
naam: Verzekering
onderwerp: [Risicobeheer, Financien]
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

bo_definitie: "Overeenkomst waarmee de gemeente zich, tegen betaling van premie, verzekert tegen schade die zij niet kan voorkomen en waarvan de gevolgen te groot zijn om zelf te dragen."
bo_toelichting: "Gemeenten verzekeren zich in principe alleen aanvullend op de verplichte verzekeringen, en alleen voor risico's die te groot zijn om zelf te dragen — kleinere, goed te dragen risico's worden bewust niet verzekerd (zelf gedragen risico, evt. afgedekt door een reserve)."
bo_subtypes:
  - naam: "Aansprakelijkheidsverzekering"
    omschrijving: "Dekt schade aan derden waarvoor de gemeente als overheid aansprakelijk is."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Bestuurdersaansprakelijkheidsverzekering"
    omschrijving: "Dekt wettelijke aansprakelijkheid van bestuurders en commissarissen, ook bij nevenfuncties namens de gemeente."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Milieuaansprakelijkheidsverzekering"
    omschrijving: "Dekt milieuaansprakelijkheidsrisico's; in principe niet standaard afgedekt, tenzij het financiële risico aannemelijk fors is."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Constructie All Risk (CAR)-verzekering"
    omschrijving: "Dekt aansprakelijkheid voortvloeiend uit bouwactiviteiten, afgesloten door opdrachtgever of opdrachtnemer."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Vrijwilligersverzekering"
    omschrijving: "Dekt vrijwilligers en mantelzorgers die werkzaamheden binnen de gemeentegrens verrichten."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Opstal-/inventarisverzekering"
    omschrijving: "Dekt opstallen (tegen herbouw- of sloopwaarde) en inventaris (tegen nieuwwaarde) tegen brand-, vliegtuig- en stormschade."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Machinebreukverzekering"
    omschrijving: "Dekt installaties en machines tegen technische schade; wordt gecombineerd met de opstal-/inventarispolis."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico|Risico]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een verzekering dekt een of meer risico's af
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject|Vastgoedobject]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Opstallen en inventaris zijn veelvoorkomende verzekerde objecten
bedrijfsprocessen: [Verzekeringsbeheer]
bedrijfsfuncties: [Risicobeheer, Financieel beheer]
---

# Verzekering

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elke polis is een afzonderlijke overeenkomst met een eigen verzekeraar en voorwaarden |
| Eigen attributen | Ja — verzekerd bedrag, eigen risico, dekking, premie, indexering |
| Levenscyclus | Ja — afsluiten → jaarlijkse indexering/premiebetaling → eventuele schademelding en -afhandeling → opzeggen of vernieuwen |
| Gemeentelijk eigendom | Ja — het college stelt het verzekeringsbeleid vast en sluit de polissen af |
| Wettelijke grondslag | Ja — onderdeel van het gemeentelijk verzekeringsbeleid, indirect verbonden aan de risicobeheersingsverplichting (art. 11 BBV) |
| Registratieverplichting | Ja — polissen, verzekerde bedragen en eigen risico's worden vastgelegd in het verzekeringsbeleid en bij de verzekeraar |

Score: 6/6 criteria.

## Beschrijving

Een verzekering is een overeenkomst waarmee de gemeente tegen betaling van premie een risico overdraagt aan een verzekeraar. Gemeenten hanteren daarbij als hoofdregel: naast de wettelijk verplichte verzekeringen wordt alleen verzekerd voor schades die de gemeente niet kan voorkomen en waarvan de gevolgen te groot zijn om zelf te dragen. Kleinere risico's worden bewust zelf gedragen (eigen risico), mede omdat een hoger eigen risico vaak een lagere premie oplevert.

Het verzekeringsbeleid legt de uitgangspunten vast: verzekerde bedragen voor materiële zaken op nieuwwaarde/herbouwwaarde, letsel- en vermogensschade op de in de branche gangbare standaardbedragen, en eigen-risicobedragen op basis van een retentieonderzoek (afweging tussen bruto schadelast en netto premie). Veelvoorkomende polissen bij gemeenten zijn de aansprakelijkheidsverzekering (schade aan derden), de bestuurdersaansprakelijkheidsverzekering, de CAR-verzekering bij bouwprojecten, de vrijwilligersverzekering, en de opstal-/inventarisverzekering voor gemeentelijke gebouwen. Sommige risico's — zoals verlies van geld/geldswaarden of fraude — worden doorgaans bewust niet verzekerd.

Gemeenten kunnen daarnaast collectief risico's overdragen via een gezamenlijke voorziening (bijv. een risicobeheerfonds), waarmee kennis, data en schadelast worden gedeeld tussen deelnemende gemeenten.

## Specialisaties

Zie `bo_subtypes` in de frontmatter voor de zeven herkende verzekeringstypen; geen van deze heeft een eigen BO-pagina, ze zijn uitwisselbare varianten van hetzelfde onderliggende concept (polis met verzekerd bedrag, eigen risico en dekking).

## Procesbron

De verzekering ontstaat in het proces van gemeentelijk verzekeringsbeheer, op grond van het door het college vastgestelde verzekeringsbeleid. Zie [[Wiki/Bronsamenvattingen/Risicobeheer/verzekeringsbeleid-eindhoven-2022|Verzekeringsbeleid gemeente Eindhoven 2022]].

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico\|Risico]] | → | Dekt een of meer risico's af |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | → | Opstallen/inventaris zijn veelvoorkomende verzekerde objecten |

## Bedrijfsprocessen

- **Verzekeringsbeheer** — polissen afsluiten, jaarlijks indexeren, schademelding en -afhandeling, herzien op basis van retentieonderzoek

## Bronnen
- [[Wiki/Bronsamenvattingen/Risicobeheer/verzekeringsbeleid-eindhoven-2022]]

## Terugmelding GGM

GGM-hiaat: geen entiteit voor de gemeentelijke verzekering als beheersmaatregel voor risico's, terwijl elke gemeente een verzekeringsportefeuille beheert. Verwant aan het eveneens ontbrekende [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico|Risico]].
