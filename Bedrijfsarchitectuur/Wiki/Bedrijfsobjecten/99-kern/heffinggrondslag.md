---
type: bedrijfsobject
naam: "Heffinggrondslag"
domein: [Belastingen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Heffinggrondslag"
ggm_guid: EAID_3D2D5426_653C_485c_A99C_8AD933E76D78
ggm_uml_type: Class
ggm_beleidsdomein: "1 Veiligheid en Vergunningen"
ggm_taakveld: "1 Veiligheid en Vergunningen"
ggm_diagram: [Diagram Vergunningen en Meldingen, Verkamering en Woonoverlast]
ggm_diagram_ids: [EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267, EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF]
ggm_definitie: "De maatstaf waarop een belasting is gebaseerd, het bedrag op basis waarvan een bepaalde belasting wordt geheven of de premie voor sociale zekerheid wordt vastgesteld."
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
gemma_definitie: "Tariefregel in een heffingsverordening die de maatstaf, het tarief en de berekening van een specifieke heffing vastlegt."
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening|Heffingsverordening]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een heffinggrondslag is vastgelegd in een heffingsverordening"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/heffing|Heffing]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een heffinggrondslag is de basis voor heffingen"
bedrijfsprocessen: [tariefbepaling, aanslagoplegging, begrotingsbehandeling]
bedrijfsfuncties: [Belastingheffing]
---

# Heffinggrondslag

Tariefregel in een heffingsverordening die de maatstaf, het tarief en de berekening van een specifieke heffing vastlegt.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | Gemeente registreert per verordening de grondslagen met domein, hoofdstuk, paragraaf, maatstaf en bedrag |
| Meervoud | Elke verordening bevat meerdere grondslagen (bijv. OZB-eigenaar, OZB-gebruiker, per tariefklasse) |
| Levenscyclus | Vastgesteld → jaarlijks gewijzigd (tariefaanpassing) → vervallen bij intrekking verordening |
| Eigendom | Gemeenteraad stelt vast als onderdeel van de verordening |
| Gemeentelijk belang | Bepaalt de belastinginkomsten per belastingtype |
| Bronnen | Belastingverordening, beleidsregels DFM, kostendekkende-tarieven bronnen |

## GGM-bron

> **Heffinggrondslag**: De maatstaf waarop een belasting is gebaseerd, het bedrag op basis waarvan een bepaalde belasting wordt geheven of de premie voor sociale zekerheid wordt vastgesteld.
> — *GGM v2.5.1, 1 Veiligheid en Vergunningen*

**Entiteit:** Heffinggrondslag
**Attributen:** domein, hoofdstuk, paragraaf, omschrijving, bedrag
**Matchsterkte:** exact — de GGM-entiteit koppelt Heffingsverordening aan Heffing en legt de tariefregel vast.

## BO-definitie

De heffinggrondslag is het tussenliggende object dat een verordening concreet maakt: het specificeert per tariefregel de heffingsmaatstaf (bijv. WOZ-waarde, oppervlakte, aantal), de berekeningswijze en het bedrag. Het GGM modelleert dit als een apart object met eigen attributen, niet als eigenschap van de verordening.

De attributen `domein`, `hoofdstuk` en `paragraaf` reflecteren de structuur van de tarieventabel in de verordening.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Vastgelegd in verordening | [[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening\|Heffingsverordening]] | Heffingsverordening → Heffinggrondslag | — |
| Basis voor heffingen | [[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing]] | Heffing → Heffinggrondslag | — |
| Gekoppeld aan zaaktype | *(Zaaktype)* | Zaaktype → Heffinggrondslag | Zaaktype niet als apart BO in dit domein |
| Gekoppeld aan activiteit | *(Activiteit Omgevingswet)* | Heffinggrondslag → Activiteit Omgevingswet | Bij leges Omgevingswet |

## Bedrijfsprocessen

- **Tariefbepaling**: jaarlijkse vaststelling/aanpassing tarieven per grondslag
- **Aanslagoplegging**: de grondslag bepaalt welk bedrag de belastingplichtige verschuldigd is
- **Begrotingsbehandeling**: de begrote opbrengsten worden berekend uit grondslagen × aantallen

## Bedrijfsfuncties

- Belastingheffing

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/belastingverordening]]
- [[Wiki/Bronsamenvattingen/Belastingen/kostendekkende-tarieven]]
- [[Wiki/Bronsamenvattingen/Belastingen/beleidsregels-gemeentelijke-belastingen-dfm]]
- [[Wiki/Bronsamenvattingen/Belastingen/onroerendezaakbelastingen]]
