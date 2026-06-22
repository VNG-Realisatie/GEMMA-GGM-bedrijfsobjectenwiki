---
type: bedrijfsobject
naam: "WOZ-object"
domein: [Belastingen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "WOZ-object"
ggm_guid: EAID_CB7BA76D_0793_4d5a_9596_533C5BC56BBF
ggm_uml_type: Class
ggm_beleidsdomein: "RSGBPlus"
ggm_taakveld: "99 Kern"
ggm_diagram: [Vastgoed WOZ, Detaillering WOZ-objecttypen op hoofdlijnen, Detaillering WOZ-objecttypen met attributen, AANDUIDING ADRES OBJECT, AANDUIDING LIGGING OBJECT, ADRESSEERBAAR OBJECT AANDUIDING, KADASTRALE ONROERENDE ZAAK, OPENBARE RUIMTE, SUBJECT, WOZ-DEELOBJECT, WOZ-OBJECT, WOZ-WAARDE]
ggm_diagram_ids: [EAID_0CF01F05_D23F_454a_A0CD_042C2DD9EE7D, EAID_3F813481_9A40_4b1b_9B24_1FD069230A45, EAID_5E76FEEA_58F8_41fd_9FF1_B44274C80FA5, EAID_79A12E83_7204_4e76_9EFF_DE43AB9C5CF5, EAID_5AEC36BA_4A41_469d_948F_1F161CE8C49B, EAID_EB829228_B970_4bc9_A9B4_5E88B9EF07D3, EAID_54189494_EC52_4728_91F7_B868A5AF5919, EAID_974F321A_9A6C_473e_B44D_938E410712CA, EAID_FAA8B1DB_4AFE_4db0_8D32_1322C62344E8, EAID_8312FF96_BCFE_4913_B7AB_27E9F690F89D, EAID_4785522F_7798_4d8d_A437_48602B8ACA21, EAID_EB7771AD_FBE8_40e5_9CD7_2C8EED4A6C33]
ggm_definitie: "De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld."
ggm_toelichting: "Dit objecttype komt voort uit de objectafbakeningsvoorschriften van artikel 16 van de Wet WOZ.
De unieke identificatie van het WOZ-object is het WOZ-objectnummer. De WOZ-object-aanduiding, een secundaire identificatie, wordt samengesteld uit de adresgegevens van één van de, aan het WOZ-object via het WOZdeelobject, gerelateerde gebouwde objecten en/of benoemde terreinen dan wel van een nabij gelegen gebouwd object of benoemd terrein, in beide gevallen (eventueel) aangevuld met de locatie-omschrijving."
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "WOZObject"
ggm_gemma_guid: "3f1aeea3-a5a8-4df6-af1e-51d5ef4ad32f"
ggm_gemma_definitie: "De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-3f1aeea3-a5a8-4df6-af1e-51d5ef4ad32f"
ggm_gemma_bron: "BRWOZ"
ggm_gemma_alternate_name: ""
gemma_definitie: "Onroerende zaak waarvan de gemeente op grond van de Wet WOZ de waarde bepaalt en vaststelt."
definitie: De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld.
bedrijfsprocessen: [WOZ-taxatie, OZB-heffing, bezwaarbehandeling WOZ]
bedrijfsfuncties: [Belastingheffing, Waardering onroerende zaken]
status: concept
relaties:
  - type: associatie
    bedrijfsobject: "WOZ-waarde"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een WOZ-object heeft per waardepeildatum een WOZ-waarde"
  - type: associatie
    bedrijfsobject: Debiteur
    richting: bidirectioneel
    kardinaliteit: "1..*"
    beschrijving: "Via WOZ-Belang gekoppeld aan eigenaar en/of gebruiker"
---

# WOZ-object

De onroerende zaak waarvan de gemeente jaarlijks de woz-waarde vaststelt onder de Wet WOZ.

## GGM-bron

> **WOZ-object**: De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld.
> — *GGM v2.5.1, RSGBPlus (taakveld 99 Kern)*

**Entiteit:** WOZ-object (BRWOZ)
**Attributen:** WOZObjectnummer, geometrieWOZObject, statusWOZObject, grondoppervlakte, gebruikscode, soortobjectcode, vastgesteldeWaarde, datumWaardepeiling, datumBeginGeldigheidWOZObject, datumEindeGeldigheidWOZObject

## BO-definitie

Het bedrijfsobject WOZ-object komt overeen met de GGM-entiteit. Het is het centrale object in het WOZ-proces: het wordt getaxeerd, krijgt een waarde, en die waarde is de heffingsmaatstaf voor de OZB en andere heffingen.

De WOZ is een van de 11 basisregistraties in Nederland. Per WOZ-object worden gegevens bijgehouden over oppervlakte, bouwtype, bouwjaar, onderhoud, omgevingsfactoren, verkoop- en huurcijfers.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Heeft waarde | [[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo\|woz-waarde-bo]] | WOZ-object → WOZ-Waarde [0..*] | Geen |
| Heeft belanghebbende | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur\|debiteur]] | WOZ-object → WOZ-Belang → Rechtspersoon | Ingekort: WOZ-Belang is tussenliggend (onderscheidt eigenaar/gebruiker) |
| Bestaat uit | *(WOZ-deelobject)* | WOZ-object → WOZ-deelobject [1..*] | Deelobject niet als apart BO — te granulair voor bedrijfsniveau |
| Gerelateerd aan kadaster | *(KadastraleOnroerendeZaak)* | WOZ-object → KadastraleOnroerendeZaak [0..*] | Kadastrale objecten zijn basisregistratie, geen apart BO |

## Bedrijfsprocessen

- **WOZ-taxatie**: jaarlijkse waardebepaling via geautomatiseerde taxatiemodellen
- **OZB-heffing**: WOZ-waarde × tarief = belastingaanslag
- **Bezwaarbehandeling**: belastingplichtige kan bezwaar maken tegen de WOZ-waarde

## Bedrijfsfuncties

- Waardering onroerende zaken
- Belastingheffing

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/belastingtypen]]
- [[Wiki/Bronsamenvattingen/Belastingen/belastinggebied]]
- [[Wiki/Bronsamenvattingen/Belastingen/belastingpolitiek]]
- [[Wiki/Bronsamenvattingen/Belastingen/belastingverordening]]
- [[Wiki/Bronsamenvattingen/Belastingen/bevoegdhedenverdeling]]
- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding]]
- [[Wiki/Bronsamenvattingen/Belastingen/kostendekkende-tarieven]]
- [[Wiki/Bronsamenvattingen/Belastingen/wettelijke-grenzen]]
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-gemeentelijke-belastingen]]
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-kostenonderbouwing]]
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-woz]]
