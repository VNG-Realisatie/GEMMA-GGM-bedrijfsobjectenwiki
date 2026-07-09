---
type: element
naam: Vacature (arbeidsmarkt)
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
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

bo_definitie: "Een openstaande arbeidsplaats bij een werkgever in de regio, gedeeld via VUM voor matching met werkzoekenden."
bo_toelichting: "Gemeenten registreren en delen arbeidsmarktvacatures via VUM (Verbeteren Uitwisseling Matchingsgegevens) over regio- en organisatiegrenzen. Dennis (instrumentengids werkgeversdienstverlening) ondersteunt dit proces."
bo_homoniemen:
  - bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/vacature|Vacature]]"
    ggm_entiteit: Vacature
    ggm_guid: EAID_DC978807_5F36_4148_B816_D6886D026DD8
    ggm_beleidsdomein: HR
    toelichting: "GGM-Vacature in HR is de gemeente als werkgever die eigen personeel zoekt (werving & selectie). Deze Vacature (arbeidsmarkt) is de gemeente als arbeidsmarktbemiddelaar die werkzoekenden matcht aan vacatures van werkgevers in de regio."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Werkzoekende]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "matching werkzoekende aan vacature"
  - type: associatie
    bedrijfsobject: "[[Instrument]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "instrument ingezet voor invulling vacature"
bedrijfsprocessen: [werkgeversdienstverlening, VUM-matching, arbeidstoeleiding]
bedrijfsfuncties: [werkgeversdienstverlening, arbeidsparticipatie]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Kern van matching en werkgeversdienstverlening |
| Herkenbaar voor domeinexperts | ✅ Werkcoaches en accountmanagers werken dagelijks met vacatures |
| Eigen bestaan | ✅ Openstaande positie bij werkgever met eisen en kenmerken |
| Meervoud | ✅ Honderden per arbeidsmarktregio |
| Levenscyclus | ✅ Aangemeld → openstaand → gematcht → vervuld/ingetrokken |
| Relaties | ✅ Werkzoekende (matching), Instrument, werkgever |

Score: **6/6**

## Beschrijving

Een arbeidsmarktvacature is een openstaande arbeidsplaats bij een werkgever in de regio die de gemeente actief inzet voor matching met werkzoekenden. Via VUM (Verbeteren Uitwisseling Matchingsgegevens) worden vacatures gedeeld over regio- en organisatiegrenzen heen, zodat werkzoekenden snel en duurzaam gekoppeld kunnen worden aan passend werk.

Per vacature worden geregistreerd: soort arbeidscontract, arbeidsmarktkwalificatie-eisen, sector, locatie, beschikbaarheidsperiode en contactgegevens werkgever.

## Naamkeuze

De naam "Vacature" is een homoniem — dezelfde naam wordt in GGM-beleidsdomein HR (taakveld 9 Interne Organisatie) gebruikt voor een ander concept. Dit BO heet **Vacature (arbeidsmarkt)**.

**Overwogen namen:**
- **Vacature (arbeidsmarkt)** — gekozen: maakt het domeinonderscheid expliciet
- Vacature (VUM) — te technisch, VUM is een programmanaam
- Arbeidsmarktvacature — eenduidig maar ongebruikelijk in de praktijk

**Verschil met [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/vacature|Vacature]] (HR):**
- **Vacature (HR):** de gemeente als werkgever zoekt eigen personeel. Relaties: Arbeidsfunctie, Sollicitatie. Proces: werving & selectie.
- **Vacature (arbeidsmarkt):** de gemeente als arbeidsmarktbemiddelaar matcht werkzoekenden aan werkgeversvacatures. Relaties: Werkzoekende, Instrument. Proces: werkgeversdienstverlening, VUM-matching.

## Procesbron

Afgeleid uit het SGR 19.0 (BKWI), conceptueel gegevensdeelmodel VUM (Verbeteren Uitwisseling Matchingsgegevens). Zie [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr|Wet SUWI en SGR]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| matching met [[Werkzoekende]] | naar dit BO | 0..* | SGR/VUM |
| [[Instrument]] ingezet voor invulling | naar dit BO | 0..* | SGR/Dennis |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr]]

## Terugmelding GGM

GGM-hiaat: het GGM Werk-domein heeft geen Vacature-entiteit voor arbeidsmarktmatching. De bestaande Vacature in HR (EAID_DC978807) betreft de gemeente als werkgever, niet als arbeidsmarktbemiddelaar. Homoniem teruggemeld als #87 in [[Wiki/Analyses/ggm-terugmeldingen]].
