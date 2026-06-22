---
type: bedrijfsobject
naam: Werknemer
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Werknemer
ggm_guid: EAID_BBBB63AC_B546_409b_B6D4_53DB561253B7
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects, Documenten, Sollicitaties, Relaties met Kern, Bezetting en Formatie]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53, EAID_E8C1CCDA_FF3C_498a_8FC9_FD6E461092FA, EAID_542C38C9_B92F_48de_87F1_F90F64FB5913, EAID_6409BBCD_026C_40ea_BC54_EE3B816D8CAB, EAID_0B1C1CCE_E0D1_413d_A38B_7A9B03A21610]
ggm_definitie: "De contractuele wederpartij van de werkgever bij de arbeidsovereenkomst."
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

gemma_definitie: "De contractuele wederpartij van de werkgever bij de arbeidsovereenkomst."
relaties:
  - type: associatie
    bedrijfsobject: "[[Dienstverband]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Werknemer heeft een of meer dienstverbanden"
  - type: associatie
    bedrijfsobject: "[[Verlof]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Werknemer heeft verlof"
  - type: associatie
    bedrijfsobject: "[[Verzuim]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Werknemer heeft verzuim"
  - type: associatie
    bedrijfsobject: "[[Declaratie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Werknemer dient declaratie in"
  - type: associatie
    bedrijfsobject: "[[Beoordeling]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Werknemer wordt beoordeeld"
  - type: associatie
    bedrijfsobject: "[[Sollicitatie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Werknemer solliciteert intern"
  - type: associatie
    bedrijfsobject: "[[Disciplinaire Maatregel]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Werknemer heeft disciplinaire maatregel"
bedrijfsprocessen: [Personeelsadministratie, Salarisadministratie, Werving en selectie, Gesprekscyclus, Verzuimbegeleiding]
bedrijfsfuncties: [Personeelsbeheer]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal object in personeelsadministratie |
| Herkenbaar voor domeinexperts | ✅ Iedereen kent het concept werknemer |
| Heeft eigen bestaan binnen het domein | ✅ Persoon met eigen dossier |
| Kan in meervoud bestaan | ✅ Duizenden per gemeente |
| Heeft eigen levenscyclus | ✅ In dienst → functiewijzigingen → uit dienst |
| Heeft relaties met andere concepten | ✅ Hub naar Dienstverband, Verlof, Verzuim, Declaratie, Beoordeling |

Score: **6/6**

## Beschrijving

De werknemer is de persoon die op basis van een arbeidsovereenkomst werkzaam is bij de gemeente. In het GGM erft Werknemer van het abstracte type Medewerker. Het werknemersdossier omvat alle personalia, dienstverbanden, verlof, verzuim, beoordelingen, declaraties en opleidingen.

Sinds de normalisering (Wnra, 2020) zijn gemeenteambtenaren werknemer in de zin van het BW. De Ambtenarenwet 2017 stelt aanvullende eisen aan integriteit (ambtseed, VOG).

## GGM-bron

> "De contractuele wederpartij van de werkgever bij de arbeidsovereenkomst."

- **Entiteit:** Werknemer (erft van abstract Medewerker)
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** naam, voornaam, geboortedatum, woonplaats
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Werknemer heeft [[Dienstverband]] | van dit BO | 1..* | GGM |
| Werknemer heeft [[Verlof]] | van dit BO | 0..* | GGM |
| Werknemer heeft [[Verzuim]] | van dit BO | 0..* | GGM |
| Werknemer dient [[Declaratie]] in | van dit BO | 0..* | GGM |
| Werknemer wordt [[Beoordeling\|beoordeeld]] | van dit BO | 0..* | GGM |
| Werknemer heeft [[Disciplinaire Maatregel]] | van dit BO | 0..* | GGM |
| Werknemer doet [[Sollicitatie]] | van dit BO | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsvoorwaarden]]
