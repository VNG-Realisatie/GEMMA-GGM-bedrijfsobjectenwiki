---
type: element
naam: Veiligheidsrisicogebied
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

bo_definitie: "Door de burgemeester aangewezen gebied waarin, bij verstoring van de openbare orde door de aanwezigheid van wapens of ernstige vrees daarvoor, de officier van justitie preventief kan laten fouilleren (art. 151b/174b Gemeentewet)."
bo_toelichting:
bo_subtypes:
  - naam: "Reguliere aanwijzing (art. 151b)"
    omschrijving: "Aanwijzing na overleg met de officier van justitie in de lokale driehoek, voor een vooraf bepaalde duur; schriftelijk besluit."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Spoedeisende aanwijzing (art. 174b)"
    omschrijving: "Aanwijzing door de burgemeester in een onvoorziene, spoedeisende situatie, voor ten hoogste twaalf uur; kan mondeling worden gegeven en wordt zo spoedig mogelijk op schrift gesteld."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties: []
bedrijfsprocessen: [Aanwijzen veiligheidsrisicogebied]
bedrijfsfuncties: [Openbare orde en veiligheid]
---

# Veiligheidsrisicogebied

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elke aanwijzing heeft een eigen gebiedsomschrijving en geldigheidsduur |
| Eigen attributen | Ja — gebiedsomschrijving (incl. publiek toegankelijke gebouwen en erven), geldigheidsduur, aanwijzingsgrond |
| Levenscyclus | Ja — overleg driehoek → aanwijzing (schriftelijk of, spoedeisend, mondeling) → kennisgeving aan raad → intrekking zodra dreiging is geweken |
| Gemeentelijk eigendom | Ja — de burgemeester wijst het gebied aan, na verordening van de raad die deze bevoegdheid verleent |
| Wettelijke grondslag | Ja — Gemeentewet art. 151b (regulier) en art. 174b (spoedeisend) |
| Registratieverplichting | Ja — de aanwijzing wordt op schrift gesteld (of achteraf vastgelegd bij mondelinge spoedaanwijzing) en ter kennis gebracht van de raad en de officier van justitie |

Score: 6/6 criteria.

## Beschrijving

Een veiligheidsrisicogebied is een door de burgemeester aangewezen gebied — met inbegrip van de daarin gelegen publiek toegankelijke gebouwen en erven — waarin de officier van justitie preventief kan laten fouilleren op wapens (bevoegdheden uit art. 50, 51 en 52 Wet wapens en munitie). De raad moet de burgemeester deze aanwijzingsbevoegdheid eerst bij verordening hebben verleend.

De aanwijzing kent twee vormen. De reguliere aanwijzing (art. 151b) volgt na overleg met de officier van justitie in het lokale driehoeksoverleg, wordt schriftelijk vastgelegd met gebiedsomschrijving en geldigheidsduur, en niet langer of groter dan strikt noodzakelijk voor de handhaving van de openbare orde. De spoedeisende aanwijzing (art. 174b) geldt voor een onvoorziene, acute situatie: de burgemeester kan dan voor ten hoogste twaalf uur aanwijzen, desnoods mondeling, met een zo spoedig mogelijke schriftelijke bevestiging. In beide gevallen brengt de burgemeester de aanwijzing zo spoedig mogelijk ter kennis van de raad, en trekt hij de aanwijzing in zodra de verstoring van de openbare orde of de ernstige vrees daarvoor is geweken.

## Procesbron

Het veiligheidsrisicogebied ontstaat in het proces van openbare-ordehandhaving door de burgemeester, na overleg met de officier van justitie. Zie [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst|Gemeentewet — wettekst]], art. 151b en 174b, en de "Menukaart bestuurlijke interventies ondermijning" in [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/handreiking-apv-en-ondermijning|Handreiking APV en ondermijning]] (item 3).

## Bedrijfsprocessen

- **Aanwijzen veiligheidsrisicogebied** — driehoeksoverleg, aanwijzingsbesluit, kennisgeving aan de raad, monitoring en intrekking

## Bronnen
- [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst]]
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/handreiking-apv-en-ondermijning]]

## Terugmelding GGM

GGM-hiaat: gebiedsgebonden openbare-ordebevoegdheid zonder GGM-tegenhanger. Conceptueel verwant aan [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/alcoholoverlastgebied|Alcoholoverlastgebied]] (eveneens een aangewezen gebied met aanvullend regime) en aan [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/gebiedsaanwijzing|Gebiedsaanwijzing]] (Omgevingswet, andere grondslag en registratiesysteem — DSO/omgevingsplan). ⚠️ Ter discussie: of gebiedsaanduidingen met verschillende juridische kaders in een toekomstige ronde onder een overkoepelend generiek concept moeten worden gebracht.
