---
type: bedrijfsobject
naam: Horecabedrijf
domein: [Economie]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Vestiging"
ggm_guid: EAID_B60B8EF9_D1C0_4e36_BF9B_1C16F92518DD
ggm_uml_type: Class
ggm_beleidsdomein: "RSGBPlus"
ggm_taakveld: "99 Kern"
ggm_diagram: [KVK, Diagram Economie, Diagram Gebied Vestiging en Adres, Diagram Gebied Vestiging en Adres, BENOEMD OBJECT, Detaillering subjecten op hoofdlijnen, Detaillering WOZ-objecttypen op hoofdlijnen, Detaillering WOZ-objecttypen met attributen, Detaillering subjecten met attributen, Detaillering Subjecten , NHR, ADRESSEERBAAR OBJECT AANDUIDING, MAATSCHAPPELIJKE ACTIVITEIT, VESTIGING]
ggm_diagram_ids: [EAID_FC491653_1FBF_412a_A939_A705D501AE48, EAID_21D78104_E6EA_4d5c_9DBE_AB71F7DC99E7, EAID_50085E67_46AC_4f54_B204_436786266EE2, EAID_19D888BE_5EC7_4590_BE67_8F66D91245F1, EAID_515E0990_C193_43cb_8EAF_907796BD3B1F, EAID_BE50EA2F_917E_434f_91ED_0EB06CCBEFB6, EAID_3F813481_9A40_4b1b_9B24_1FD069230A45, EAID_5E76FEEA_58F8_41fd_9FF1_B44274C80FA5, EAID_EB4053EE_18A5_4578_8973_7FD5967CDFC8, EAID_71A3B7DD_0097_4a32_8E4B_09735D7404E8, EAID_A4A7A187_57B9_4ecb_9B3D_012C51E981E2, EAID_EB829228_B970_4bc9_A9B4_5E88B9EF07D3, EAID_0B75D3CA_1D93_46c7_9268_BD8276836FE2, EAID_3CAB7DD2_51D3_45b3_9CE1_61E0150F792D]
ggm_definitie: "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt."
ggm_toelichting: "Ofschoon de definitie in het NHR doet vermoeden dat het hier om een ruimtelijk object gaat, beschouwen we een VESTIGING in het RSGB als een specialisatie van SUBJECT. De toelichting in de catalogus NHR lijkt dit te bevestigen:
“De vestiging van een onderneming of een maatschappelijke activiteit (type niet onderneming) moet men opvatten als een (kleinste eenheid) bundeling van economische activiteiten. De vestiging is een combinatie van activiteiten en locatie. Wisseling van zowel de activiteiten als de locatie maakt dat er sprake is van een nieuwe vestiging. In de toekomstige situatie is er een eenduidige verwijzing naar een adresseerbaar object (een ligplaats, standplaats of verblijfsobject (BAG)) voor het bezoekadres. Als er sprake is van een inschrijfplichtige onderneming maar het adresseerbare object is nog niet bekend, omdat bijv. een bedrijfspand nog gebouwd wordt of er vanuit huis gewerkt wordt, kan als adres het woonadres (van de eigenaar) worden genomen. 
De vestiging kan aldus verhuizen, heeft een bezoekadres en een postadres en een naam. Allemaal zeer ongewone aspecten voor een locatie c.q. gebouwd object. Het lijkt dan ook meer weg te hebben van een subject (die activiteiten uitvoert) in een gebouwd object. Dit wordt versterkt doordat het wenselijk is bij het registreren van de WOZ-belanghebbende of een vergunningaanvraag een contactpersoon vast te leggen: iemand die werkzaam is in een vestiging (een NNP kent geen medewerkers) en voor dat geval optreedt als vertegenwoordiger van de vestiging van de onderneming/NNP.
De definitie beperkt de locaties van VESTIGINGen tot gebouwen, In het RSGB gaan we er van uit dat een VESTIGING haar activiteiten ook kan uitoefenen op een STANDPLAATS, op een LIGPLAATS, op een  OVERIG BENOEMD TERREIN of in een OVERIG GEBOUWD OBJECT. VESTIGING overerft gegevens van de generalisatie SUBJECT. Onder meer zijn dat de Datum begin geldigheid en Datum einde geldigheid voor resp. Datum in gebruikname en Datum beëindiging in het NHR. Ook het buitenlands adres indien een vestiging verplaatst wordt naar het buitenland."
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Vestiging"
ggm_gemma_guid: "b403d1ab-a0ee-4ca0-befa-01bbc54bf403"
ggm_gemma_definitie: "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-b403d1ab-a0ee-4ca0-befa-01bbc54bf403"
ggm_gemma_bron: "NHR"
ggm_gemma_alternate_name: ""
bo_definitie: "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt."
bo_toelichting: ''
bedrijfsprocessen: [horecavergunningverlening, handhaving horeca, horecabeleid]
bedrijfsfuncties: [vergunningverlening, handhaving, economisch beleid]
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Vestiging]]"
    richting: "van-dit-BO"
    kardinaliteit: 
    beschrijving: Horecabedrijf is een specialisatie van Vestiging
  - type: associatie
    bedrijfsobject: "[[Hotel]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een horecabedrijf kan een hotel exploiteren
  - type: associatie
    bedrijfsobject: "[[Terras]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een horecabedrijf kan een terras exploiteren
  - type: associatie
    bedrijfsobject: "[[Bed-and-breakfast]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een horecabedrijf kan een B&B exploiteren"
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal begrip in Verordening horeca en Ontwikkelingskader |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip voor vergunningverleners en beleidsmakers |
| Heeft een eigen bestaan | ✅ | Exploitatie op een fysieke locatie met vergunning |
| Kan in meervoud bestaan | ✅ | Honderden horecabedrijven in een gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanvraag → vergunning → exploitatie → sluiting |
| Heeft relaties met andere concepten | ✅ | Hotel, terras, vergunning, hinderprofiel |

6/6 criteria — BO.

## Beschrijving

Een horecabedrijf is een onderneming die zich richt op het verstrekken van eten, drinken en/of logies. De gemeente reguleert horecabedrijven via de Verordening horeca, het Ontwikkelingskader Horeca en een vergunningenstelsel. Kernafwegingen zijn leefbaarheid (hinderprofiel), balans met detailhandel en wonen, en spreiding over de stad.

Het Utrechtse beleid stimuleert horeca buiten de historische binnenstad en beoordeelt horecaontwikkeling in het centrum kritisch.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Horecavergunning | Vergunning voor exploitatie van een horecabedrijf | — |

De horecavergunning is een subtype van vergunning, hier vastgelegd vanwege de directe koppeling met het horecabedrijf.

## GGM-bron

> "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt." — GGM (Vestiging), RSGB

- **Entiteit**: Vestiging
- **Beleidsdomein**: RSGBPlus (Kern)
- **Matchsterkte**: **partieel** — Vestiging is het generieke concept; horecabedrijf is een specialisatie die het GGM niet apart modelleert

Het GGM kent geen specifieke horecaentiteit. Horecabedrijf is een specialisatie van Vestiging, herkenbaar via SBI-code. De GGM-entiteit Hotel is een aparte specialisatie van Vestiging.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Vestiging]] | generalisatie | Horecabedrijf → Vestiging | — | GGM (overerving) |
| [[Hotel]] | associatie | Horecabedrijf → Hotel | 0..* | Beleid |
| [[Terras]] | associatie | Horecabedrijf → Terras | 0..* | Beleidsregel terrassen |
| [[Bed-and-breakfast]] | associatie | Horecabedrijf → B&B | 0..* | Beleid |

## Bronnen

- [[Wiki/Bronsamenvattingen/Economie/economie-speerpunten-vng]]
- [[Wiki/Bronsamenvattingen/Economie/ontwikkelingskader-detailhandel-2012]]
- [[Wiki/Bronsamenvattingen/Economie/detailhandel-utrecht-2015]]
- [[Wiki/Bronsamenvattingen/Economie/horecabeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/actualisatie-marktruimte-hotelnota]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-terrassen-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregel-hotels-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-short-stay-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsnota-werklocaties-2035]]
