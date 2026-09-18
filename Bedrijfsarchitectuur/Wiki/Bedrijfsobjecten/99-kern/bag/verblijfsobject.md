---
type: element
naam: Verblijfsobject
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Verblijfsobject
ggm_guid: EAID_461EFCF0_E65E_4c7c_B44D_8F36C36FDCE4
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Diagram Gebied Vestiging en Adres", "Diagram Sportbeleid Locaties", "Ruimte Adressen, gebouwen en terreinen", "Vastgoed verankering RSGB IMBAG", "BAG", "ONDERZOEK"]
ggm_diagram_ids: ["EAID_50085E67_46AC_4f54_B204_436786266EE2", "EAID_BA23F316_FE48_49a8_A26D_9B1D14713F76", "EAID_7561B00D_273B_425a_B2FE_1C3AE499ED2E", "EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3", "EAID_9B0FEF1A_4146_409e_8B71_B12D4B4AB8A8"]
ggm_definitie: "Een verblijfsobject is een kleinste binnen één of meer panden gelegen en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is."
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

ggm_duplicaat_entiteiten:
  - entiteit: Verblijfsobject
    guid: EAID_A33151CE_37B2_4026_B0AF_B541687B5B7C
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (verblijfsobjectidentificatie, verblijfsobjectstatus, etc.); minder attributen (geen geometrie, gebruiksdoel, oppervlakte, documentvelden); voegt inOnderzoek toe"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Verblijfsobject** als directe tegenhanger. Daarnaast is **Verblijfsobject** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Kleinste binnen een of meer panden gelegen eenheid van gebruik, ontsloten via een eigen afsluitbare toegang, met een of meer gebruiksdoelen, geregistreerd in de BAG."
bo_toelichting:
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Pand]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een verblijfsobject maakt deel uit van een of meer panden"
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een verblijfsobject heeft een hoofdadres en optioneel nevenadressen"
  - type: associatie
    bedrijfsobject: "[[WOZ-object]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "WOZ-objecten kunnen gekoppeld zijn aan verblijfsobjecten"
bedrijfsprocessen: [BAG-registratie, Bouwvergunningverlening, WOZ-waardering, BRP-adresregistratie]
bedrijfsfuncties: [Basisregistratie, Vergunningverlening, Belastingheffing]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (de eenheid waar mensen wonen of werken), herkenbaar voor domeinexperts (woning, kantoor, winkel), eigen bestaan (fysieke ruimte binnen pand), meervoud (honderdduizenden per gemeente), eigen levenscyclus (gevormd → in gebruik → ingetrokken), relaties met [[Pand]], [[Nummeraanduiding]], [[WOZ-object]].

## Beschrijving

Een verblijfsobject is de gebruikseenheid binnen een of meer [[Pand]]en. Het is datgene wat een adres krijgt: een woning, een kantoorruimte, een winkel. Elk verblijfsobject heeft minstens één gebruiksdoel (wonen, kantoor, winkel, industrie, logies, etc.) en een oppervlakte.

De afbakening is complex. Een verblijfsobject moet: bestaan uit binnenruimten binnen panden, samenhangend gebruik hebben met de vereiste basisvoorzieningen (wonen: keuken/douche/toilet; kantoor: water/toilet; industrie: geen vereisten), ontsloten worden via een eigen afsluitbare toegang, onderwerp kunnen zijn van goederenrechtelijke handelingen (verkoop/verhuur), en de kleinste eenheid zijn.

Hotelkamers, verzorgingshuiskamers en cellen zijn géén verblijfsobject — ze kunnen niet zelfstandig worden verkocht. Een verblijfsobject kan zich over meerdere panden uitstrekken (na verbouwing).

## GGM-bron

> "Een verblijfsobject is een kleinste binnen één of meer panden gelegen en voor woon-, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is." (GGM, entiteit Verblijfsobject, beleidsdomein BAG)

- **Entiteit:** Verblijfsobject
- **Beleidsdomein:** BAG
- **Attributen:** identificatie, status, geconstateerd, hoogsteBouwlaag, laagsteBouwlaag, toegangBouwlaag, soortWoonobject, aantalKamers, ontsluitingVerdieping, documentnummer, documentdatum, geometrie, versie, gebruiksdoel, beginGeldigheid, eindGeldigheid, datumEinde, datumIngang, oppervlakte
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Verblijfsobject" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_461EFCF0_E65E_4c7c_B44D_8F36C36FDCE4` | **primair** — BAG is de bronregistratie voor verblijfsobjecten |
| RSGBPlus | `EAID_A33151CE_37B2_4026_B0AF_B541687B5B7C` | duplicaat — domein-geprefixte attribuutnamen; minder attributen (geen geometrie, gebruiksdoel, oppervlakte, documentvelden); voegt inOnderzoek toe |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## BO-definitie

De GGM-definitie beschrijft technische implementatiedetails in plaats van het concept zelf. De BO-definitie beschrijft het begrip vanuit de gemeentelijke praktijk.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Pand]] | maakt deel uit van | 1..* | GGM + BAG Catalogus |
| [[Nummeraanduiding]] | heeft als adres | 1..* | GGM + BAG Catalogus |
| [[WOZ-object]] | wordt gewaardeerd als | 0..* | GGM |

## Bedrijfsprocessen

- **BAG-registratie** — bijhouden op basis van vergunningen en constateringen
- **Bouwvergunningverlening** — splitsing/samenvoeging leidt tot nieuwe verblijfsobjecten
- **WOZ-waardering** — verblijfsobject is basis voor WOZ-objectafbakening
- **BRP-adresregistratie** — personen worden ingeschreven op het adres van een verblijfsobject

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
