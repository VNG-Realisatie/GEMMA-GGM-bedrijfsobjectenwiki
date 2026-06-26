---
type: bedrijfsobject
naam: Inspectie
onderwerp: [Omgevingswet, Vastgoed]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Inspectie
ggm_guid: EAID_F73901FC_A78E_486f_B6C6_74CFCBE26CAB
ggm_uml_type: Class
ggm_beleidsdomein: "1 Veiligheid en Vergunningen"
ggm_taakveld: "1 Veiligheid en Vergunningen"
ggm_diagram: [Diagram Vergunningen en Meldingen, Verkamering en Woonoverlast]
ggm_diagram_ids: [EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267, EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF]
ggm_definitie: "Het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen."
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

ggm_duplicaat_entiteiten:
  - entiteit: Inspectie
    guid: EAID_A31C3B5D_EAC5_482d_8816_8B858EC4BE01
    beleidsdomein: Vastgoed
    taakveld: "9 Interne Organisatie"
    afwijkende_attributen: "alleen datum en bevindingen (minder attributen dan VTH-variant)"

gemma_definitie: "Periodieke controle waarbij de toestand van een bouwwerk, activiteit of situatie wordt vastgesteld — zowel in het kader van VTH-toezicht als vastgoedbeheer."
gemma_subtypes: []
relaties:
  - type: associatie
    bedrijfsobject: "[[VTH-zaak]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een inspectie hoort bij een VTH-zaak"
  - type: associatie
    bedrijfsobject: "[[Bevinding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een inspectie levert bevindingen op"
  - type: associatie
    bedrijfsobject: "[[MJOP]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Een vastgoedinspectie leidt tot een MJOP"
  - type: associatie
    bedrijfsobject: "[[Vastgoedobject]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Een vastgoedinspectie betreft een vastgoedobject"
bedrijfsprocessen: [toezicht op realisatie, toezicht op bestaande bouw, planmatig onderhoud vastgoed]
bedrijfsfuncties: [toezicht en handhaving, gebouwbeheer]
---

## BO-criteria toetsing

1. **Identificeerbare instanties** — elke inspectie heeft een eigen kenmerk, datum en type
2. **Eigen attributen** — datumInspectie, inspectietype, datumGepland, status, kenmerk, omschrijving, opmerkingen
3. **Levenscyclus** — gepland → uitgevoerd → afgerond, met hercontroles
4. **Meerdere processen** — toezicht op realisatie, toezicht op bestaande bouw, steekproeven Wkb
5. **Relevant op bedrijfsniveau** — wordt gemonitord op aantallen, thema's en resultaten in VTH-jaarplannen
6. **Gemeentelijk perspectief** — de gemeente voert inspecties uit als wettelijke taak

## Beschrijving

Een inspectie is een toezichtscontrole in de fysieke leefomgeving. Bij toezicht op de realisatie controleert de gemeente of bouwwerkzaamheden conform de verleende vergunning worden uitgevoerd, met focus op constructieve veiligheid, brandveiligheid en omgevingsveiligheid. Bij toezicht op bestaande bouw vindt controle plaats op basis van signalen (meldingen, handhavingsverzoeken) of steekproeven. De diepgang van de inspectie wordt bepaald door het toezichtsprotocol en de prioritering van het onderwerp.

> "Bij de toezichtsmomenten wordt er aandacht besteed aan de thema's waar wij als gemeente de grootste risico's van niet-naleving zien zoals de constructieve veiligheid en brandveiligheid." (bron: Uitvoeringsbeleid VTH Delft §5.4)

## GGM-duplicaten

De GGM-entiteit "Inspectie" komt voor in 3 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **1 Veiligheid en Vergunningen** | `EAID_F73901FC_A78E_486f_B6C6_74CFCBE26CAB` | **primair** — gekozen vanwege rijkere attributenset |
| Vastgoed | `EAID_A31C3B5D_EAC5_482d_8816_8B858EC4BE01` | duplicaat — minder attributen (datum, bevindingen) |
| Beheer Openbare Ruimte | *(reeds bekend)* | duplicaat — zelfde concept in BOR-context |

In het vastgoeddomein is de inspectie specifiek een NEN 2767-conditiemeting waarbij bouwdelen van een [[Vastgoedobject]] worden beoordeeld op technische staat. Het resultaat voedt de [[MJOP]].

## BO-definitie

De GGM-definitie verwijst naar boezemkades (waterbeheer-context). Voor VTH en vastgoed is de definitie:

> **GGM:** Het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen.

> **GEMMA:** Toezichtscontrole waarbij de toestand van een bouwwerk, activiteit of situatie in de fysieke leefomgeving wordt vastgesteld.

⚠️ Terugmelding: GGM-definitie is domeinspecifiek (waterbeheer) maar entiteit wordt breder gebruikt in VTH-domein.

## GGM-bron

> Het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen.

- **Entiteit:** Inspectie
- **Beleidsdomein:** 1 Veiligheid en Vergunningen
- **Attributen:** datumInspectie, inspectietype, datumGepland, status, kenmerk, omschrijving, opmerkingen, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor
- **Matchsterkte:** functioneel — entiteit past, definitie is domeinspecifiek

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | van-dit-BO | 1..* | Een inspectie hoort bij een VTH-zaak | GGM |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/bevinding\|Bevinding]] | naar-dit-BO | 0..* | Een inspectie levert bevindingen op | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | naar-dit-BO | 0..1 | Een vastgoedinspectie betreft een vastgoedobject | GGM (Vastgoed) |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | van-dit-BO | 0..1 | Een vastgoedinspectie leidt tot een MJOP | GGM (Vastgoed) |

## Bedrijfsprocessen

- Toezicht op realisatie van vergunde plannen
- Toezicht op bestaande bouw (signaaltoezicht, steekproeven)
- Brandveiligheidscontroles (in samenwerking met VRH)
- Steekproeven Wkb-meldingen

## Bronnen
- [[Wiki/Bronsamenvattingen/Omgevingswet/uitvoeringsbeleid-vth-delft]]
- [[Wiki/Bronsamenvattingen/Vastgoed/beleidsplan-vastgoed-hulst]]

## Terugmelding GGM

Definitie van Inspectie in GGM verwijst specifiek naar boezemkades (waterbeheer), maar de entiteit wordt in het VTH-domein breed ingezet voor toezichtscontroles op bouwwerken en de bestaande leefomgeving. Voorstel: generaliseer de definitie. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
