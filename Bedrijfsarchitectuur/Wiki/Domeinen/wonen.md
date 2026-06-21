---
type: domein
naam: Wonen
status: in-behandeling
verwerkingsdatum: 2026-06-21
bronnen_count: 6
begrippen_count: 22
bo_count: 3
---

# Domein: Wonen

Het gemeentelijk woonbeleid stuurt op betaalbaar, passend en prettig wonen. De gemeente reguleert de woningvoorraad via vergunningen (huisvesting, omzetting, splitsing, woningvorming), stuurt op nieuwbouw via woningbouwprogrammering, en verdeelt schaarse sociale huurwoningen via een woonruimteverdelingssysteem (aanbodmodel, loting, bemiddeling). De Beleidsnota Wonen 2025–2030 en de Huisvestingsverordening vormen het beleidskader.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Woning]] | object | Zelfstandige woonruimte voor permanente huisvesting van één huishouden | ✅ | ja | 6/6 criteria, GGM: Gebouw | Sociale huurwoning, middenhuurwoning, koopwoning | ja |
| [[Woningbouwplan]] | object | Project waarin woningen worden geprogrammeerd en gerealiseerd | ✅ | ja | 6/6 criteria, GGM: Plan | Merwedekanaalzone, Cartesiusdriehoek | ja |
| [[Urgentverklaring]] | instrument | Beschikking waarmee woningzoekende voorrang krijgt bij toewijzing sociale huur | ✅ | ja | 6/6 criteria, governance-object, GGM-hiaat | Medische urgentie, dreigend dakloos | nee |
| sociale huurwoning | object | Huurwoning met huurprijs onder liberalisatiegrens (€900,07 in 2025) | — | ja | Subtype van [[Woning]], GGM: Huurwoningen | Corporatiewoning, kernvoorraad | ja |
| middenhuurwoning | object | Huurwoning €900–€1.185, 144–186 WWS-punten | — | ja | Subtype van [[Woning]], GGM-hiaat | Beleggershuurwoning | nee |
| betaalbare koopwoning | object | Koopwoning tot betaalbaarheidsgrens (€405.000 in 2025) | — | ja | Subtype van [[Woning]], GGM: Koopwoningen | Starterswoning met zelfbewoningsplicht | ja |
| studentenwoning | object | Woning met campuscontract voor studenten | — | ja | Subtype van [[Woning]], GGM: Studentenwoningen | Zelfstandige of onzelfstandige studentenkamer | ja |
| huisvestingsvergunning | instrument | Vergunning voor betrekken vergunningplichtige woonruimte | ❌ | ja | Vergunning, past bij VTH-domein | Vergunning sociale huur, middenhuur | nee |
| omzettingsvergunning | instrument | Vergunning voor omzetten zelfstandig naar onzelfstandig | ❌ | ja | Vergunning wijziging woonruimtevoorraad | Omzetting naar kamerverhuur | nee |
| splitsingsvergunning | instrument | Vergunning voor bouwkundig of kadastraal splitsen | ❌ | ja | Vergunning wijziging woonruimtevoorraad | Kadastrale splitsing appartement | nee |
| woningvormingsvergunning | instrument | Vergunning voor creëren extra woonruimten in bestaand gebouw | ❌ | ja | Vergunning wijziging woonruimtevoorraad | Bij optoppen/aanplakken | nee |
| verhuurvergunning | instrument | Vergunning voor verhuur na aankoop bij opkoopbescherming | ❌ | ja | Vergunning, specifiek opkoopbescherming | Verhuur in beschermd gebied | nee |
| toeristische verhuurregistratie | instrument | Registratieplicht voor vakantieverhuur, max 60 nachten | ❌ | ja | Registratie, past bij VTH-domein | Airbnb-registratie | nee |
| leefbaarheidstoets | instrument | Beoordeling fysiek en algemeen bij vergunningaanvragen | ❌ | nee | Processtap, geen zelfstandig object | Toets bij omzettingsaanvraag | nee |
| prestatieafspraken | instrument | Afspraken gemeente-corporaties-huurdersorganisaties | ❌ | ja | Governance-instrument, niet beoordeeld als BO | Jaarlijkse prestatieafspraken | nee |
| woningcorporatie | actor | Organisatie die sociale huurwoningen bouwt en beheert | ❌ | ja | Actor, geen business object | Mitros, Portaal, Bo-Ex, Woonin | nee |
| woningzoekende | doelgroep | Persoon ingeschreven bij WoningNet voor sociale huur | ❌ | ja | Rol van persoon, geen zelfstandig object | Actief woningzoekende op DĀK | nee |
| woonruimteverdeling | thema | Systeem van toewijzing sociale huurwoningen | ❌ | nee | Proces, geen object | Aanbodmodel, loting, bemiddeling | nee |
| opkoopbescherming | instrument | Regime dat verhuur na aankoop verbiedt in aangewezen wijken | ❌ | nee | Beleidsregime, geen registreerbaar object | Verbod verhuur 4 jaar, prijsgrens €611.000 | nee |
| zelfbewoningsplicht | instrument | Verplichting tot zelfbewoning bij nieuwbouw koop | ❌ | nee | Contractueel beding, attribuut van koopovereenkomst | 5 jaar na BRP-inschrijving | nee |
| antispeculatiebeding | instrument | Beding tegen speculatieve doorverkoop | ❌ | nee | Contractueel beding, attribuut van koopovereenkomst | 5 jaar geldingsduur | nee |
| woningdelen | thema | Meerdere huishoudens in één woning | ❌ | nee | Activiteit/proces, geen object | Max 3 personen vergunningvrij | nee |

## GGM-entiteitendekking

| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Bouwen en Wonen | 7 | 2 | 3 | 2 | Projectleider en Projectontwikkelaar zijn actoren, niet beoordeeld als BO-kandidaat voor wonen |

### GGM-dekkingsanalyse

Het GGM-beleidsdomein "Bouwen en Wonen" bevat 7 entiteiten gericht op woningbouwprojecten. Twee entiteiten matchen direct op wiki-BO's: Gebouw → [[Woning]], Plan → [[Woningbouwplan]]. Drie subtypes (Huurwoningen, Koopwoningen, Studentenwoningen) zijn vastgelegd als specialisaties van [[Woning]]. Projectleider en Projectontwikkelaar zijn actoren die niet als BO zijn beoordeeld.

**Hiaten:**
- **Middenhuurwoning** ontbreekt als subtype van Gebouw. Sinds de Wet betaalbare huur (2024) is dit een wettelijk gereguleerd segment.
- **Urgentverklaring** ontbreekt volledig. Een beschikking met eigen levenscyclus en 9 categorieën.
- Het GGM modelleert geen toewijzings- of verdelingsinstrumenten (huisvestingsvergunning, urgentverklaring, woonruimteverdeling). Dit is consistent met het GGM-patroon dat governance en processen buiten scope vallen.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Wonen/beleidsnota-wonen-utrecht|Beleidsnota Wonen in Utrecht 2025-2030]]
- [[Wiki/Bronsamenvattingen/Wonen/huisvestingsverordening-utrecht|Huisvestingsverordening gemeente Utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/nadere-regel-huisvestingsverordening|Nadere regel Huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/beleidsregel-huisvestingsverordening|Beleidsregel Huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-betaalbare-koopwoningen|Actieplan betaalbare koopwoningen 2021]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-middenhuur|Actieplan Middenhuur 2017]]
- [[Wiki/Bronsamenvattingen/Wonen/werkwijze-extra-woningen|Werkwijze extra woningen toevoegen]]

## Nog te verwerken bronnen

- [actieplan-middenhuur.md](Sources/Onderwerpen/Ruimte Wonen en Mobiliteit/converted_pdf/actieplan-middenhuur.md) — volledig opgenomen in beleidsnota, bronsamenvatting gemaakt

## Openstaande vragen of hiaten

- De vergunningen rond woonruimtevoorraad (omzetting, splitsing, woningvorming, verhuur) zijn hier als instrumenten vastgelegd maar niet als BO beoordeeld. Bij een toekomstige VTH-ingest kunnen deze als BO-kandidaten terugkomen.
- Prestatieafspraken zijn een governance-instrument dat mogelijk een eigen BO rechtvaardigt. Nog niet beoordeeld.

## Terugmeldingen richting GGM

- **Middenhuurwoning** — Ontbreekt als subtype van Gebouw. Wettelijk gereguleerd segment sinds 2024.
- **Urgentverklaring** — Ontbreekt als objecttype. Beschikking met eigen levenscyclus en categorieën.

Zie [[Wiki/Analyses/ggm-terugmeldingen]] voor het volledige overzicht.
