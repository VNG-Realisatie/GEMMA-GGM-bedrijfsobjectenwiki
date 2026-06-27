---
type: bedrijfsobject
naam: Standplaats (BAG)
onderwerp: [Basisregistraties, BAG, Wonen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Standplaats
ggm_guid: EAID_86952BDA_ADF6_4ff0_B8C7_BA3AA889A40B
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Objecten bij Vergunningaanvraag", "Ruimte Adressen, gebouwen en terreinen", "Vastgoed verankering RSGB IMBAG", "BAG", "ONDERZOEK", "Detaillering adressen, gebouwen en terreinen op hoofdlijnen"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E", "EAID_7561B00D_273B_425a_B2FE_1C3AE499ED2E", "EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3", "EAID_9B0FEF1A_4146_409e_8B71_B12D4B4AB8A8", "EAID_00CCCF33_A542_47e6_AFA6_2F9F4E2670D8"]
ggm_definitie: "Een standplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte."
ggm_toelichting: "Een terrein of een deel daarvan dat moet kunnen worden gebruikt om langere tijd een object neer te zetten. Dit object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Het moet verplaatsbaar zijn en mag dus niet helemaal vastgemaakt worden aan de grond. Bijvoorbeeld een woonwagen of strandtent. De gemeente mag zeggen of er voor de BAG ergens een standplaats komt."
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
  - entiteit: Standplaats
    guid: EAID_B1C6CA45_49C9_45f0_8B14_A721AD505C50
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (standplaatsidentificatie, standplaatsstatus, indicatieGeconstateerdeStandplaats); minder attributen, geen geometrie/versie/documentvelden"

bo_definitie: "Door de gemeente aangewezen terrein voor het permanent plaatsen van een verplaatsbare ruimte voor woon-, bedrijfsmatige of recreatieve doeleinden (bijv. woonwagen), als adresseerbaar object opgenomen in de BAG."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een standplaats heeft een hoofdadres en optioneel nevenadressen"
bedrijfsprocessen: [BAG-registratie, Woonwagenbeleid, Adresbeheer]
bedrijfsfuncties: [Basisregistratie, Woonbeleid]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (adresseerbaar BAG-object voor woonwagens e.d.), herkenbaar voor domeinexperts (woonwagenstandplaats), eigen bestaan (formeel aangewezen terrein), meervoud (tientallen per gemeente), eigen levenscyclus (aanwijzen, in gebruik nemen, intrekken), relaties met [[Nummeraanduiding]].

## Beschrijving

Een standplaats in de BAG is een door de gemeente aangewezen terrein voor het permanent plaatsen van een verplaatsbaar object — typisch een woonwagen of strandtent. Het object op de standplaats is niet direct en niet duurzaam met de aarde verbonden (anders zou het een [[Pand]] zijn).

De standplaats is een van de drie adresseerbare objecttypen in de BAG (naast [[Verblijfsobject]] en [[Ligplaats]]). De afbakening volgt uit formele aanwijzing door het bevoegde gemeentelijke orgaan; het daadwerkelijk gebruik van het terrein is niet relevant voor de afbakening.

**Let op:** dit is een ander object dan [[Marktstandplaats]], die gaat over locaties voor ambulante handel in de openbare ruimte (APV-gereguleerd). De GGM-entiteit "Standplaats" in RSGBPlus verwijst naar dit BAG-object, niet naar marktstandplaatsen.

## GGM-bron

> "Een standplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte." (GGM, entiteit Standplaats, beleidsdomein BAG)

- **Entiteit:** Standplaats
- **Beleidsdomein:** BAG
- **Attributen:** Identificatie, Geconstateerd, Status, Versie, Geometrie, documentdatum, documentnummer, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Standplaats" komt voor in 3 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_86952BDA_ADF6_4ff0_B8C7_BA3AA889A40B` | **primair** — BAG is de bronregistratie voor adresseerbare objecten |
| RSGBPlus | `EAID_B1C6CA45_49C9_45f0_8B14_A721AD505C50` | duplicaat — zelfde concept met domein-geprefixte attribuutnamen (standplaatsidentificatie, standplaatsstatus) en minder attributen (geen geometrie, versie, documentvelden) |

RSGBPlus voegt `inOnderzoek` niet toe als attribuut (Standplaats BAG heeft dat ook niet — het loopt via de aparte Onderzoek-entiteit).

**Homoniem:** de GGM-entiteit "Standplaats" in beleidsdomein Musea (`EAID_98F3132E_F97A_4f49_B4F5_28618BB693F8`) is een ander concept: een locatie voor het te koop aanbieden van goederen of diensten met fysieke middelen. Zie [[Marktstandplaats]] voor het verwante BO in het economiedomein.

Teruggemeld als #59 en #60 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Nummeraanduiding]] | heeft als adres | 1..* | GGM + BAG Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
