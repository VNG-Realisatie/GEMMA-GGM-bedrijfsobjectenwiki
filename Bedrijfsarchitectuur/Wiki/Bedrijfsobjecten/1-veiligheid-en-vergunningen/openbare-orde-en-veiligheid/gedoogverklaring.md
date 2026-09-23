---
type: element
naam: Gedoogverklaring
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

bo_definitie: "Persoons- en locatiegebonden verklaring van de burgemeester dat niet strafrechtelijk zal worden opgetreden tegen de verkoop van softdrugs vanuit een coffeeshop, mits de AHOJGI-criteria en eventuele aanvullende gedoogvoorwaarden worden nageleefd."
bo_toelichting: "Aanvullend op, en los van, de exploitatievergunning (art. 2:28 Apv) voor de openbare inrichting: beide zijn vereist om een coffeeshop te mogen exploiteren, maar de gedoogverklaring heeft een eigen grondslag (art. 13b Opiumwet, Aanwijzing Opiumwet OM), eigen criteria (AHOJGI) en is — anders dan de exploitatievergunning — nooit overdraagbaar of aan een rechtspersoon te verstrekken."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/bibob-toets|Bibob-toets]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Wordt toegepast voorafgaand aan het verlenen van de bijbehorende exploitatievergunning"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/sluitingsbesluit|Sluitingsbesluit]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Een sluiting op grond van art. 13b Opiumwet is grond voor intrekking van de gedoogverklaring"
  - type: associatie
    bedrijfsobject: "[[Vergunningen en ontheffingen]]"
    richting: bidirectioneel
    kardinaliteit: "1 → 1"
    beschrijving: "Vereist naast, en onafhankelijk van, de exploitatievergunning (subtype Horecavergunning) voor dezelfde coffeeshop"
bedrijfsprocessen: [Coffeeshopbeleid]
bedrijfsfuncties: [Vergunningverlening, Handhaving, Aanpak ondermijning]
---

# Gedoogverklaring

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elke gedoogverklaring betreft één specifieke exploitant op één specifieke locatie, met eigen dossier |
| Eigen attributen | Ja — exploitant, leidinggevende(n), locatie, ingangsdatum, aanvullende gedoogvoorwaarden, status |
| Levenscyclus | Ja — verzoek (met acht weken beslistermijn) → afgifte (onbepaalde tijd) → wijziging leidinggevende → intrekking (bij overtreding, 13b-sluiting, twaalf weken non-gebruik) |
| Gemeentelijk eigendom | Ja — uitsluitend de burgemeester is bevoegd tot afgifte en intrekking |
| Wettelijke grondslag | Ja — art. 13b Opiumwet, Aanwijzing Opiumwet (OM), lokaal coffeeshopbeleid |
| Registratieverplichting | Ja — schriftelijk document, te allen tijde in de inrichting aanwezig en te tonen aan toezichthouders |

Score: 6/6 criteria.

## Beschrijving

Voor het exploiteren van een coffeeshop is, naast de exploitatievergunning voor een openbare inrichting (art. 2:28 Apv), een gedoogverklaring van de burgemeester vereist. De gedoogverklaring is het document waarmee de burgemeester verklaart dat niet strafrechtelijk zal worden opgetreden tegen de verkoop van softdrugs vanuit de coffeeshop, zolang de landelijke AHOJGI-criteria (Aanwijzing Opiumwet OM: geen Affichering, geen Harddrugs, geen Overlast, geen verkoop aan Jeugdigen, slechts Geringe hoeveelheden, geen verkoop aan niet-Ingezetenen) en eventuele lokale aanvullende gedoogvoorwaarden (bijv. openingstijden, aanwezigheidsplicht, afstandscriterium tot scholen en jongerenvoorzieningen) worden nageleefd.

De gedoogverklaring is persoons- en locatiegebonden, niet overdraagbaar en kan — anders dan een reguliere vergunning — niet aan een rechtspersoon worden verstrekt. Zij wordt, net als de exploitatievergunning, voor onbepaalde tijd afgegeven. Veel gemeenten hanteren een maximumstelsel (in de bronbeleidsgemeente: maximaal één gedoogverklaring). Voorafgaand aan afgifte van de gekoppelde exploitatievergunning wordt doorgaans een [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/bibob-toets|Bibob-toets]] uitgevoerd. Een bestuursrechtelijke sluiting op grond van art. 13b Opiumwet ([[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/sluitingsbesluit|Sluitingsbesluit]]) is grond voor intrekking van zowel de exploitatievergunning als de gedoogverklaring, omdat er dan langer dan twaalf weken geen gebruik van wordt gemaakt.

## Procesbron

De gedoogverklaring ontstaat in het proces van coffeeshopregulering, op basis van het lokale coffeeshopbeleid dat de gemeente vaststelt binnen het landelijke kader van art. 13b Opiumwet en de Aanwijzing Opiumwet. Zie [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/coffeeshopbeleid-2024-vijfheerenlanden|Coffeeshopbeleid 2024]], hoofdstuk 4 (Beleidsregels).

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/bibob-toets\|Bibob-toets]] | ← | Toegepast voorafgaand aan de gekoppelde exploitatievergunning |
| associatie | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/sluitingsbesluit\|Sluitingsbesluit]] | → | 13b-sluiting is grond voor intrekking |
| associatie | [[Vergunningen en ontheffingen]] | ↔ | Vereist naast de exploitatievergunning (Horecavergunning-subtype), zelfde coffeeshop |

## Bedrijfsprocessen

- **Coffeeshopbeleid** — verzoek, toetsing AHOJGI-criteria en aanvullende gedoogvoorwaarden, afgifte, controle, handhaving, eventuele intrekking

## Bronnen
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/coffeeshopbeleid-2024-vijfheerenlanden]]

## Terugmelding GGM

GGM-hiaat: geen GGM-entiteit voor de gedoogverklaring of het bredere coffeeshopregulering-instrumentarium (exploitatievergunning, AHOJGI-toetsing). Conceptueel verwant aan het generieke BO [[Vergunningen en ontheffingen]], maar met een eigen wettelijke grondslag (art. 13b Opiumwet) en eigen kenmerken (persoonsgebonden, niet overdraagbaar, geen rechtspersoon) die een zelfstandig BO rechtvaardigen in plaats van een subtype.
