---
type: bedrijfsobject
naam: Vroegsignaal
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vroegsignaal
ggm_guid: EAID_C6DA2586_C0E3_4868_93E8_64AF6D118092
ggm_uml_type: Class
ggm_beleidsdomein: Vroegsignalering
ggm_taakveld: "Schulden"
ggm_diagram: [Vroegsignalering, Vroegsignalering Details, Vroegsignalering Klein]
ggm_definitie: "Een Vroegsignaal is een bericht dat door een signaalpartner aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner."
ggm_herkomst: GGM

gemma_definitie: "Melding van een signaalpartner aan de gemeente over een betalingsachterstand van een inwoner, als startpunt van vroegsignalering."
gemma_subtypes: []
relaties:
  - type: associatie
    bedrijfsobject: "[[signaalpartner]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Verzonden door één signaalpartner"
  - type: associatie
    bedrijfsobject: "[[vroegsignaalzaak]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Opgepakt in een vroegsignaalzaak"
  - type: associatie
    bedrijfsobject: "[[client]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Betreft één cliënt/inwoner"
bedrijfsprocessen: [vroegsignalering]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Wettelijk verplichte melding (Wgs art. 2.2.1, sinds 1-1-2021). Eigen attributen (bedrag, signaaldatum, status, crisissignaal). Den Haag ontvangt 4.000-4.500 per maand. Eigen levenscyclus (ontvangen → beoordeeld → opgepakt/afgesloten).

## Beschrijving

Een vroegsignaal is een bericht van een signaalpartner (zorgverzekeraar, energieleverancier, drinkwaterbedrijf, woningverhuurder) aan de gemeente over een betalingsachterstand. De juridische grondslag is art. 2.2.1 van de Wet gemeentelijke schuldhulpverlening. De gemeente is verplicht deze signalen op te pakken en de inwoner een hulpaanbod te doen.

Vroegsignalen worden afhankelijk van urgentie opgepakt via e-mail, kaartje, telefoontje of huisbezoek.

## GGM-bron

> "Een Vroegsignaal is een bericht dat door een signaalpartner aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner."

- **Entiteit:** Vroegsignaal
- **Beleidsdomein:** Vroegsignalering (taakveld Schulden)
- **Attributen:** crisissignaal, warmeOverdracht, bedrag, ontstaansdatum, signaaldatum, status
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[signaalpartner\|Signaalpartner]] | 1 | Verzonden door |
| associatie | [[vroegsignaalzaak\|Vroegsignaalzaak]] | 0..1 | Opgepakt in |
| associatie | [[client\|Cliënt]] | 1 | Betreft inwoner |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/vroegsignaleringsaanpak-gemeenten-divosa-2024]]
