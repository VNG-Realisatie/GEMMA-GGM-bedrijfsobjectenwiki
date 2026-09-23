---
type: element
naam: Bibob-toets
onderwerp: [Openbare Orde en Veiligheid]
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

bo_definitie: "Beoordeling van de mate van gevaar dat een beschikking, overheidsopdracht of vastgoedtransactie wordt gebruikt om uit strafbare feiten verkregen voordelen te benutten of strafbare feiten te plegen (Wet Bibob)."
bo_toelichting: "De toets bestaat uit eigen onderzoek door het bestuursorgaan (art. 7a) en/of een adviesaanvraag bij het Landelijk Bureau Bibob (art. 9). Beide sporen kunnen los of gecombineerd worden ingezet."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Actoren/landelijk-bureau-bibob|Landelijk Bureau Bibob]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Kan om een Bibob-advies worden gevraagd als onderdeel van de toets
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies|Advies]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Het Bibob-advies van het Landelijk Bureau Bibob is een specialisatie van Advies
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit|Besluit]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Uitkomst van de toets kan grond zijn voor weigering of intrekking van een beschikking
bedrijfsprocessen: [Bibob-toetsing]
bedrijfsfuncties: [Vergunningverlening, Handhaving, Aanpak ondermijning]
---

# Bibob-toets

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elke toets heeft een eigen betrokkene, aanleiding (vergunning/subsidie/opdracht/vastgoedtransactie) en dossier |
| Eigen attributen | Ja — betrokkene, grondslag (vergunning/subsidie/aanbesteding/vastgoedtransactie), mate van gevaar, conclusie |
| Levenscyclus | Ja — aanleiding → eigen onderzoek → (evt.) adviesaanvraag → advies binnen 8 weken → gebruik als weigerings-/intrekkingsgrond |
| Gemeentelijk eigendom | Ja — het college of de burgemeester voert de toets uit of vraagt deze aan |
| Wettelijke grondslag | Ja — Wet Bibob (art. 3, 7a, 9) |
| Registratieverplichting | Ja — bestuursorgaan meldt eigen conclusies aan het Bureau (art. 7a lid 7), Bureau registreert gegevens vijf jaar (art. 19, 11a) |

Score: 6/6 criteria.

## Beschrijving

De Bibob-toets is de beoordeling van de mate van gevaar dat een gemeentelijke beschikking (vergunning, subsidie, ontheffing), een overheidsopdracht of een vastgoedtransactie wordt gebruikt om uit strafbare feiten verkregen voordelen te benutten, of om strafbare feiten te plegen. De toets vindt plaats voorafgaand aan of tijdens de behandeling van een aanvraag, en kan ook worden ingezet bij een voorgenomen intrekking.

De gemeente kan zelf onderzoek doen (eigen onderzoek, art. 7a): de betrokkene levert daarvoor gegevens aan (identiteit, KvK-inschrijving, leidinggevenden, vermogensverschaffers, financieringswijze). Bij onvoldoende zekerheid of behoefte aan aanvullende bronnen kan het bestuursorgaan advies vragen aan het [[Wiki/Actoren/landelijk-bureau-bibob|Landelijk Bureau Bibob]], dat binnen acht weken (eenmalig verlengbaar met vier weken) een advies uitbrengt over de mate van gevaar. Bij "ernstig gevaar" kan de beschikking worden geweigerd of ingetrokken; bij "mindere mate van gevaar" kan het bestuursorgaan in plaats daarvan voorschriften aan de beschikking verbinden.

De weigering van betrokkene om het Bibob-formulier volledig in te vullen of aanvullende gegevens te verschaffen, wordt zelf aangemerkt als een ernstig gevaar (art. 4). Een bestuursorgaan dat op basis van eigen onderzoek concludeert tot gevaar zonder advies te vragen, meldt dit onverwijld aan het Bureau (art. 7a lid 7).

## Procesbron

De Bibob-toets ontstaat in het proces van vergunningverlening, subsidieverstrekking, aanbesteding of vastgoedtransactie, wanneer het bestuursorgaan gebruikmaakt van de bevoegdheid uit de Wet Bibob. Gedocumenteerd in [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/wet-bibob-bwbr0013798|Wet Bibob]] en toegepast in de praktijk beschreven in [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/handreiking-apv-en-ondermijning|Handreiking APV en ondermijning]] ("Menukaart bestuurlijke interventies ondermijning", items 1a-1c, 17).

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Actoren/landelijk-bureau-bibob\|Landelijk Bureau Bibob]] | ← | Kan om advies worden gevraagd |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies\|Advies]] | → | Het Bibob-advies is een specialisatie van Advies |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit\|Besluit]] | → | Uitkomst kan weigerings-/intrekkingsgrond zijn |

## Bedrijfsprocessen

- **Bibob-toetsing** — eigen onderzoek, eventuele adviesaanvraag, beoordeling mate van gevaar, verwerking in besluitvorming

## Bronnen
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/wet-bibob-bwbr0013798]]
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/handreiking-apv-en-ondermijning]]

## Terugmelding GGM

GGM-hiaat: de Wet Bibob is een centraal instrument in de gemeentelijke aanpak van ondermijning, maar de Bibob-toets en het Landelijk Bureau Bibob ontbreken volledig in het GGM. Mogelijk te modelleren binnen een nieuw of bestaand beleidsdomein Openbare Orde en Veiligheid, met relaties naar Besluit en Advies.
