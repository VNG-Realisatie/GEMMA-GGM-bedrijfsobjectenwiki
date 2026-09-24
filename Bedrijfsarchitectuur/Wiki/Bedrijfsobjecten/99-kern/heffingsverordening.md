---
type: element
naam: "Heffingsverordening"
onderwerp: [Belastingen]
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
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Heffingsverordening"
ggm_gemma_guid: "f94b299a-c9eb-4bdb-82e7-5752360494cd"
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Heffingsverordening** als directe tegenhanger.
bo_definitie: "Een heffingsverordening is een door de gemeenteraad vastgestelde verordening die de heffing en invordering van gemeentelijke belastingen en rechten regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden."
bo_toelichting:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "*(Document)*"
    richting: "van-dit-BO"
    kardinaliteit:
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

## Specialisaties

Herkende specialisaties van Heffingsverordening. Elke gemeente heeft een set verordeningen per belastingtype. Geen apart BO, tenzij anders vermeld.

**Belastingverordeningen** (algemene belastingen):
- **OZB-verordening** — twee tarieven: eigenaar en gebruiker; heffingsmaatstaf is WOZ-waarde
- **Hondenbelastingverordening** — tarief per hond, eventueel kennel-tarief
- **Reclamebelastingverordening** — tarief per openbare aankondiging, vaak gebiedsgericht
- **Precariobelastingverordening** — tarief per voorwerp op openbare grond
- **Parkeerbelastingverordening** — tarief incidenteel parkeren en vergunningen

**Bestemmingsheffingsverordeningen**:
- **Afvalstoffenverordening** — verordening voor afvalstoffenheffing (apart BO: [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/afvalstoffenverordening|Afvalstoffenverordening]])
- **Rioolheffingverordening** — verordening voor riool- en waterzorgheffing
- **BIZ-verordening** — verordening op verzoek ondernemers, met draagvlakmeting

**Toeristische heffingsverordeningen**:
- **Toeristenbelastingverordening** — tarief per overnachting
- **Forensenbelastingverordening** — tarief voor verblijf >90 dagen niet-ingezetenen

**Retributieverordeningen**:
- **Legesverordening** — door de raad vastgestelde verordening voor de heffing van leges op gemeentelijke dienstverlening; gesloten circuit met voorziening om fluctuaties op te vangen
- **Marktgeldverordening** — tarief per standplaats op markten
- **Havengeldverordening** — tarief voor gebruik waterwegen en havens
- **Lijkbezorgingsrechtenverordening** — tarief voor begraafplaats en crematorium

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Bevat grondslagen | [[Wiki/Bedrijfsobjecten/99-kern/heffinggrondslag\|Heffinggrondslag]] | Heffingsverordening → Heffinggrondslag | — |
| Grondslag voor heffingen | [[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing]] | Heffingsverordening → Heffinggrondslag ← Heffing | Via Heffinggrondslag |
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
- [[Wiki/Bronsamenvattingen/Omgevingswet/uitvoeringsbeleid-vth-delft]]
