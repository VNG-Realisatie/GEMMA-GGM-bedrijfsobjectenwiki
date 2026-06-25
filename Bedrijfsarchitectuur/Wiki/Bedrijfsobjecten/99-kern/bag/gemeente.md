---
type: bedrijfsobject
naam: Gemeente
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Gemeente
ggm_guid: EAID_EA6F820F_C458_4b24_8055_5C2CC76F5904
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Schuldhulpproces", "Vroegsignalering", "Vroegsignalering Details", "Vroegsignalering Klein", "Vastgoed verankering RSGB IMBAG", "BAG"]
ggm_diagram_ids: ["EAID_BBE1A03C_2D40_48cb_91AE_EF630304F490", "EAID_07334A5A_E2F0_41ce_8510_B41BAF6876BD", "EAID_6D5829BF_AF12_4464_9EAD_E336DEFDF442", "EAID_AFFABC16_BCDB_44c6_8E2F_C3D8C49884A5", "EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3"]
ggm_definitie: "Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie)."

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
  - entiteit: Gemeente
    guid: EAID_B0D9792B_46E7_4b88_B267_C72691616733
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (gemeenteGeometrie, datumBeginGeldigheidGemeente, etc.); minder attributen (geen Geconstateerd, versie, datumIngang, datumEinde)"

gemma_definitie: "Gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet, als hoogste niveau van de gemeentelijke gebiedsindeling."
relaties:
  - type: associatie
    bedrijfsobject: "[[Woonplaats]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een gemeente bevat een of meer woonplaatsen"
  - type: associatie
    bedrijfsobject: "[[Gemeente]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Bij herindeling gaat een gemeente op in nieuwe gemeenten"
bedrijfsprocessen: [Gebiedsindeling, Gemeentelijke herindeling]
bedrijfsfuncties: [Basisregistratie, Bestuur]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (het bestuurlijk grondgebied waarbinnen alle gemeentelijke processen plaatsvinden), herkenbaar voor domeinexperts (gemeentenaam), eigen bestaan (grondwettelijk ingesteld), meervoud (344 gemeenten in Nederland, 2024), eigen levenscyclus (instelling, herindeling, opheffing), relaties met [[Woonplaats]].

## Beschrijving

Een gemeente is het hoogste niveau van de gemeentelijke gebiedsindeling. Het is een grondwettelijk ingesteld gedeelte van het Nederlandse grondgebied (artikel 123 Grondwet). Elke gemeente heeft een gemeentecode, naam en geometrie.

De gemeente is geen formeel BAG-objecttype maar wordt in het GGM-BAG-beleidsdomein gemodelleerd als het bovenliggende niveau van de ruimtelijke hiërarchie. Bij gemeentelijke herindeling kan een gemeente opgaan in een of meer nieuwe gemeenten — het GGM modelleert deze zelf-refererende relatie.

## Generalisatie

Gemeente is het hoogste niveau van de gemeentelijke gebiedsindelingshiërarchie: **Gemeente** → [[Woonplaats]] → [[Wijk]] → [[Buurt]]. Alle niveaus delen hetzelfde patroon: code, naam, geometrie, geldigheidsperiode. Gemeente onderscheidt zich door de grondwettelijke basis en de bestuurlijke status.

## GGM-bron

> "Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet." (GGM, entiteit Gemeente, beleidsdomein BAG)

- **Entiteit:** Gemeente
- **Beleidsdomein:** BAG
- **Herkomst:** Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie).
- **Attributen:** gemeentecode, gemeentenaam, gemeentenaam NEN, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, datumEinde, versie, Geconstateerd
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Gemeente" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_EA6F820F_C458_4b24_8055_5C2CC76F5904` | **primair** — BAG is de bronregistratie voor de gebiedsindeling |
| RSGBPlus | `EAID_B0D9792B_46E7_4b88_B267_C72691616733` | duplicaat — domein-geprefixte attribuutnamen (gemeenteGeometrie, datumBeginGeldigheidGemeente); minder attributen (geen Geconstateerd, versie, datumIngang, datumEinde) |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Woonplaats]] | bevat | 1..* | GGM |
| Gemeente (opvolger) | gaat op in | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
