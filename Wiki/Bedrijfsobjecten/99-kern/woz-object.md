---
type: bedrijfsobject
naam: WOZ-object
domein: [Belastingen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: WOZ-object
ggm_beleidsdomein: RSGBPlus (Kern)
definitie: De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld.
gerelateerde_begrippen: [onroerende-zaak, woz-waarde, woz-beschikking, belastingplichtige]
relaties:
  - type: associatie
    bedrijfsobject: WOZ-waarde
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een WOZ-object heeft per waardepeildatum een WOZ-waarde
  - type: associatie
    bedrijfsobject: Debiteur
    richting: bidirectioneel
    kardinaliteit: "1..*"
    beschrijving: Via WOZ-Belang gekoppeld aan eigenaar en/of gebruiker
bedrijfsprocessen: [WOZ-taxatie, OZB-heffing, bezwaarbehandeling WOZ]
bedrijfsfuncties: [Belastingheffing, Waardering onroerende zaken]
status: concept
---

# WOZ-object

De onroerende zaak waarvan de gemeente jaarlijks de [[woz-waarde]] vaststelt onder de Wet WOZ.

## GGM-bron

> **WOZ-object**: De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld.
> — *GGM v2.5.1, RSGBPlus (taakveld 99 Kern)*

**Entiteit:** WOZ-object (BRWOZ)
**Attributen:** WOZObjectnummer, geometrieWOZObject, statusWOZObject, grondoppervlakte, gebruikscode, soortobjectcode, vastgesteldeWaarde, datumWaardepeiling, datumBeginGeldigheidWOZObject, datumEindeGeldigheidWOZObject

## BO-definitie

Het bedrijfsobject WOZ-object komt overeen met de GGM-entiteit. Het is het centrale object in het WOZ-proces: het wordt getaxeerd, krijgt een waarde, en die waarde is de [[heffingsmaatstaf]] voor de OZB en andere heffingen.

De WOZ is een van de 11 basisregistraties in Nederland. Per WOZ-object worden gegevens bijgehouden over oppervlakte, bouwtype, bouwjaar, onderhoud, omgevingsfactoren, verkoop- en huurcijfers.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Heeft waarde | [[woz-waarde-bo]] | WOZ-object → WOZ-Waarde [0..*] | Geen |
| Heeft belanghebbende | [[debiteur]] | WOZ-object → WOZ-Belang → Rechtspersoon | Ingekort: WOZ-Belang is tussenliggend (onderscheidt eigenaar/gebruiker) |
| Bestaat uit | *(WOZ-deelobject)* | WOZ-object → WOZ-deelobject [1..*] | Deelobject niet als apart BO — te granulair voor bedrijfsniveau |
| Gerelateerd aan kadaster | *(KadastraleOnroerendeZaak)* | WOZ-object → KadastraleOnroerendeZaak [0..*] | Kadastrale objecten zijn basisregistratie, geen apart BO |

## Bedrijfsprocessen

- **WOZ-taxatie**: jaarlijkse waardebepaling via geautomatiseerde taxatiemodellen
- **OZB-heffing**: WOZ-waarde × tarief = [[belastingaanslag]]
- **Bezwaarbehandeling**: belastingplichtige kan bezwaar maken tegen de WOZ-waarde

## Bedrijfsfuncties

- Waardering onroerende zaken
- Belastingheffing
