---
type: element
naam: Alcoholoverlastgebied
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

bo_definitie: "Bij gemeentelijke verordening aangewezen gebied waarin, vanwege ernstige aantasting van de openbare orde, de leefomgeving of de volksgezondheid, aanvullende verboden of beperkingen gelden voor het verstrekken van alcoholhoudende drank (art. 25f Alcoholwet)."
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/preventie-en-handhavingsplan-alcohol|Preventie- en handhavingsplan alcohol]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Aanwijzing kan onderdeel zijn van de uitvoering van het handhavingsbeleid
bedrijfsprocessen: [Aanwijzen alcoholoverlastgebied]
bedrijfsfuncties: [Openbare orde en veiligheid]
---

# Alcoholoverlastgebied

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elk aangewezen gebied heeft een eigen begrenzing en verordening |
| Eigen attributen | Ja — aanwijzingsgrond, geldende verboden/beperkingen, geldigheidsduur/tijdsruimte |
| Levenscyclus | Ja — aangewezen bij verordening → van kracht → eventueel gewijzigd of ingetrokken |
| Gemeentelijk eigendom | Ja — de gemeenteraad wijst het gebied aan bij verordening |
| Wettelijke grondslag | Ja — Alcoholwet art. 25f |
| Registratieverplichting | Ja — vastgelegd in een gemeentelijke verordening, met expliciete grond en gevolgen |

Score: 6/6 criteria.

## Beschrijving

Een alcoholoverlastgebied is een bij gemeentelijke verordening aangewezen gebied waarin, bij ernstige aantasting van de openbare orde, de leefomgeving of de volksgezondheid, aanvullende regels gelden bovenop de generieke Alcoholwet-bepalingen. In het aangewezen gebied kan de verordening bepalen dat (art. 25f lid 2): het bedrijfsmatig verstrekken van zwak-alcoholhoudende drank voor gebruik elders dan ter plaatse wordt verboden of beperkt; de burgemeester aanvullende gronden heeft om een horeca- of slijtersvergunning te weigeren; of andere verboden en beperkingen gelden die de wet elders al toestaat (art. 25a, 25b, 25d), maar dan specifiek voor dit gebied.

De aanwijzing is gebiedsgebonden en tijdelijk van aard — de verordening kan worden gewijzigd of ingetrokken zodra de aantasting van openbare orde, leefomgeving of volksgezondheid niet langer aan de orde is.

## Procesbron

Het alcoholoverlastgebied ontstaat in het proces van gemeentelijke verordening-vaststelling, op grond van signalen van ernstige overlast. Zie [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/alcoholwet-wettekst|Alcoholwet — wettekst]], art. 25f.

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/preventie-en-handhavingsplan-alcohol\|Preventie- en handhavingsplan alcohol]] | ← | Kan onderdeel zijn van de uitvoering van het handhavingsbeleid |

## Bedrijfsprocessen

- **Aanwijzen alcoholoverlastgebied** — verordening voorbereiden, vaststellen, publiceren; periodiek evalueren

## Bronnen
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/alcoholwet-wettekst]]

## Terugmelding GGM

GGM-hiaat: gebiedsgebonden verordeningsinstrument zonder GGM-tegenhanger. Conceptueel verwant aan [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/gebiedsaanwijzing|Gebiedsaanwijzing]] (aanwijzing van een gebied met bijbehorende regels), maar met een andere juridische grondslag (Alcoholwet i.p.v. Omgevingswet) en een ander registratiesysteem (gemeentelijke verordening i.p.v. DSO/omgevingsplan) — daarom hier als zelfstandig BO vastgelegd in plaats van als specialisatie. Zie ook [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/veiligheidsrisicogebied|Veiligheidsrisicogebied]], een vergelijkbaar gebiedsinstrument met een derde grondslag (Gemeentewet). ⚠️ Ter discussie: of gebiedsaanduidingen met verschillende juridische kaders in een toekomstige ronde onder een overkoepelend generiek concept moeten worden gebracht.
