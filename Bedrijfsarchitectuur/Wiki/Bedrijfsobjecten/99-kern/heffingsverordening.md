---
type: bedrijfsobject
naam: "Heffingsverordening"
domein: [Belastingen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Heffingsverordening"
ggm_guid: EAID_C29CCD49_04E2_44b4_A6B0_AD8B10552628
ggm_uml_type: Class
ggm_beleidsdomein: "1 Veiligheid en Vergunningen"
ggm_taakveld: "1 Veiligheid en Vergunningen"
ggm_diagram: [Diagram Vergunningen en Meldingen, Verkamering en Woonoverlast]
ggm_diagram_ids: [EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267, EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF]
ggm_definitie: "Een heffingsverordening is een door de gemeenteraad vastgestelde verordening die de heffing en invordering van gemeentelijke belastingen en rechten regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Heffingsverordening"
ggm_gemma_guid: "f94b299a-c9eb-4bdb-82e7-5752360494cd"
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Door de gemeenteraad vastgestelde verordening die de heffing en invordering van een gemeentelijke belasting of recht regelt."
relaties:
  - type: generalisatie
    bedrijfsobject: "*(Document)*"
    richting: "van-dit-BO"
    kardinaliteit: ""
    beschrijving: "Een heffingsverordening is een specialisatie van Document in het GGM"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/heffing|Heffing]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een heffingsverordening is de grondslag voor heffingen (via heffingsgrondslag)"
bedrijfsprocessen: [vaststelling belastingverordening, tariefbepaling, begrotingsbehandeling]
bedrijfsfuncties: [Belastingheffing, Gemeenteraad]
---

# Heffingsverordening

Door de gemeenteraad vastgestelde verordening die de heffing en invordering van een gemeentelijke belasting of recht regelt.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | De gemeente registreert elke verordening met belastingtype, tarieven, grondslag, looptijd |
| Meervoud | Elke gemeente heeft meerdere verordeningen (OZB, afvalstoffenheffing, rioolheffing, leges, etc.) |
| Levenscyclus | Ontwerp → vastgesteld door raad → inwerkingtreding → wijziging → intrekking |
| Eigendom | Vastgesteld door de gemeenteraad |
| Gemeentelijk belang | Juridische grondslag voor alle gemeentelijke belastinginkomsten |
| Bronnen | VNG-bronnen, beleidsregels DFM, alle belastingtype-bronnen |

## GGM-bron

> **Heffingsverordening**: Een heffingsverordening is een door de gemeenteraad vastgestelde verordening die de heffing en invordering van gemeentelijke belastingen en rechten regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden.
> — *GGM v2.5.1, 1 Veiligheid en Vergunningen*

**Entiteit:** Heffingsverordening (specialisatie van Document)
**Attributen:** *(geen eigen attributen, erft van Document)*
**Matchsterkte:** exact — de GGM-definitie komt volledig overeen met het begrip "belastingverordening" uit de beleidsbronnen.

## BO-definitie

De heffingsverordening is het juridische instrument waarmee de gemeenteraad belastingheffing mogelijk maakt. Elke gemeentelijke belasting vereist een eigen verordening. De verordening bevat de belastingplichtigen, het belastbare feit, de heffingsmaatstaf, het tarief, vrijstellingen en de wijze van heffing.

VNG-modelverordeningen dienen als basis; de gemeenteraad maakt per belastingtype keuzes binnen de wettelijke kaders.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Grondslag voor heffingen | [[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing]] | Heffingsverordening → Heffinggrondslag ← Heffing | Ingekort: Heffinggrondslag is tussenliggend |
| Specialisatie van | *(Document)* | Heffingsverordening → Document (generalisatie) | Document niet als apart BO |

## Bedrijfsprocessen

- **Vaststelling belastingverordening**: gemeenteraad stelt verordening vast, inclusief tarieven
- **Tariefbepaling**: jaarlijkse vaststelling/aanpassing tarieven binnen de verordening
- **Begrotingsbehandeling**: de begrote opbrengsten hangen af van de verordening

## Bedrijfsfuncties

- Belastingheffing
- Besluitvorming gemeenteraad

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/belastingverordening]]
- [[Wiki/Bronsamenvattingen/Belastingen/beleidsregels-gemeentelijke-belastingen-dfm]]
- [[Wiki/Bronsamenvattingen/Belastingen/onroerendezaakbelastingen]]
- [[Wiki/Bronsamenvattingen/Belastingen/retributies]]
- [[Wiki/Bronsamenvattingen/Belastingen/reinigingsheffingen]]
