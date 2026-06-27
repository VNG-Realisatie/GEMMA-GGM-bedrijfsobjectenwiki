---
type: bedrijfsobject
naam: Leverancier
onderwerp: [inkoop]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Leverancier
ggm_guid: EAID_EA7FE08E_34F7_45d2_BE2E_E4E3B8333BF3
ggm_uml_type: Class
ggm_beleidsdomein: Inkoop
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Model Parkeren, Diagram Beslissingen Leerplicht, Prinsenhof Verkoop, Prinsenhof Events en Relaties, Schouwrondes Beheersobjecten, Meldingen Graafwerkzaamheden, Basismodel CMDB-Items, Vastgoed Relaties met Kern, Vastgoed Leveranciers, Financien Verplichtingen en Facturen, Diagram Verlengen Inhuur, Diagram Inkoop Inhuur, Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2, EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308, EAID_3913ADF8_4B30_48c0_A0AE_59BAAC281EF2, EAID_22110445_1906_4602_8004_6BA4D6C063D0, EAID_F9907E9B_BD04_439e_A0A9_C6E7BA7F6623, EAID_1D1CC6D9_472B_4f91_8096_0260E27F641C, EAID_4F14E8D8_5502_4880_9E83_D912BE451EB1, EAID_EFF3FBED_B92D_4172_B142_567C2B6ACF01, EAID_06E44472_8C2A_40eb_9965_DCF91A1322C9, EAID_0723EB5C_4A2C_44d4_B15B_37AC71B5D711, EAID_21AD192F_EEF1_493b_9BFD_D37EF6C93236, EAID_1172FBF0_04B4_46c7_9FB5_F34730E060FB, EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie"
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
  - entiteit: Leverancier
    guid: EAID_51A266C7_3BDA_457c_9A32_CD1B166CA5BF
    beleidsdomein: Inkoop
    taakveld: "9 Interne Organisatie"
    afwijkende_attributen: "Beperktere diagram-set (Sociaal Domein, Verplichtingen, Relaties Sociaal Domein tot Kern)"

bo_definitie: "Niet-natuurlijk persoon die goederen, diensten of werken levert aan de gemeente op basis van een contract of opdracht."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Contract]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "contractant bij"
  - type: associatie
    bedrijfsobject: "[[Offerte]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "dient in"
  - type: associatie
    bedrijfsobject: "[[Inschrijving]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "heeft"
bedrijfsprocessen: [Inkopen, Contracteren, Bewaken]
bedrijfsfuncties: [Inkoopfunctie, Contractmanagement]
---

## BO-criteria toetsing

1. **Heeft betekenis binnen het onderwerp** — ja, wederpartij van de gemeente bij inkoop
2. **Is herkenbaar voor domeinexperts** — ja, inkopers en contractmanagers werken dagelijks met leveranciers
3. **Heeft een eigen bestaan** — ja, leverancier bestaat onafhankelijk van specifieke contracten
4. **Kan in meervoud bestaan** — ja, gemeente heeft honderden leveranciers
5. **Heeft een eigen levenscyclus** — ja: registratie → kwalificatie → contractrelatie → beëindiging
6. **Heeft relaties met andere concepten** — ja: Contract, Offerte, Inschrijving, Gunning

Score: 6/6

## Beschrijving

Een leverancier is een niet-natuurlijk persoon die producten, diensten of werken levert aan de gemeente. Leveranciers worden geregistreerd in het leveranciersbestand en kunnen zich kwalificeren voor deelname aan aanbestedingen.

De gemeente streeft naar onafhankelijkheid ten opzichte van leveranciers en toetst hun integriteit via uitsluitingsgronden, de Gedragsverklaring Aanbesteden, of een Bibob-toets. Bij lokale en regionale inkopen heeft de gemeente oog voor lokale ondernemers, MKB en sociale ondernemingen.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Leverancier. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Kandidaat** — persoon die wordt aangeboden door een leverancier voor inhuur; eigen attribuut datumIngestuurd
- **Uitnodiging** — verzoek aan een leverancier om deel te nemen aan een aanbesteding inhuur

## GGM-bron

> "Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie" (GGM, beleidsdomein Inkoop)

**Matchsterkte:** exact — GGM-entiteit en BO zijn hetzelfde concept.

**Attributen:** naam, nummer

Leverancier is een specialisatie van Rechtspersoon (abstract) in het GGM.

## GGM-duplicaten

De GGM-entiteit "Leverancier" komt voor met 2 GUIDs:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **Inkoop** | `EAID_EA7FE08E_34F7_45d2_BE2E_E4E3B8333BF3` | **primair** — gekozen als canonieke mapping omdat deze op 13 diagrammen voorkomt, waaronder alle Inkoop-diagrammen |
| Inkoop | `EAID_51A266C7_3BDA_457c_9A32_CD1B166CA5BF` | duplicaat — beperktere diagram-set (Sociaal Domein, Verplichtingen) |

Teruggemeld als #78 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Contract\|Contract]] | contractant bij | → | 0..* | GGM |
| [[Offerte\|Offerte]] | dient in | → | 0..* | GGM |
| [[Inschrijving\|Inschrijving]] | heeft | → | 0..* | GGM |

## Bedrijfsprocessen

- **Inkopen** — selecteren en beoordelen van leveranciers
- **Contracteren** — vastleggen leveranciersrelatie
- **Bewaken** — monitoren prestaties en integriteit

## Bedrijfsfuncties

- **Inkoopfunctie** — beheer leveranciersbestand
- **Contractmanagement** — relatiebeheer leveranciers

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]
