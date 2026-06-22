---
type: bedrijfsobject
naam: Evenement
domein: [evenementen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "OpenbareActiviteit"
ggm_guid: EAID_B2B423C3_B9C9_4b4f_A47D_85D29417B9B4
ggm_uml_type: Class
ggm_beleidsdomein: "1 Veiligheid en Vergunningen"
ggm_taakveld: "1 Veiligheid en Vergunningen"
ggm_diagram: []
ggm_diagram_ids: [EAPK_0A4C6DE8_608E_4626_A40E_0C432A5B0F9C]
ggm_definitie: "Activiteit in het publieke domein"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "OpenbareActiviteit"
ggm_gemma_guid: "9ffbd7f6-a815-4edd-9252-5ed7e873c6a0"
ggm_gemma_definitie: "Activiteit in het publieke domein"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA2/0.9/id-9ffbd7f6-a815-4edd-9252-5ed7e873c6a0"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Georganiseerde activiteit met publiek in de openbare ruimte, waarvoor de gemeente een vergunning verleent en die plaatsvindt op een aangewezen locatie."
bedrijfsprocessen: ""
bedrijfsfuncties: ""
bronnen: [Wiki/Bronsamenvattingen/Evenementen/locatiebeleid-evenementen, Wiki/Bronsamenvattingen/Evenementen/evenementenbeleid-utrecht]
relaties:
  - type: associatie
    bedrijfsobject: "[[Evenementenlocatie]]"
    richting: "van-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Evenement vindt plaats op een evenementenlocatie
  - type: associatie
    bedrijfsobject: "[[Evenementenvergunning]]"
    richting: "van-dit-BO"
    kardinaliteit: 1..1
    beschrijving: Evenement vereist een evenementenvergunning
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Kern van het evenementenbeleid |
| Herkenbaar voor domeinexperts | ✅ | Universeel begrepen begrip |
| Heeft een eigen bestaan | ✅ | Een evenement bestaat onafhankelijk van andere objecten |
| Kan in meervoud bestaan | ✅ | ~1000 evenementen per jaar in Utrecht |
| Heeft een eigen levenscyclus | ✅ | Aanmelding → beoordeling → reservering → vergunning → uitvoering → evaluatie |
| Heeft relaties met andere concepten | ✅ | Locatie, vergunning, organisator, beoordelingscriteria |

**6/6 criteria van toepassing.**

## Beschrijving

Een evenement is een georganiseerde activiteit met publiek in de openbare ruimte. De gemeente onderscheidt evenementen naar omvang (klein <500, middelgroot, groot, groot internationaal) en naar type (cultureel, sport, stadsfeest, herdenking). Evenementen worden jaarlijks aangemeld via de reserveringskalender en beoordeeld op vier criteria: maatschappelijke waarde, bijdrage aan pluriform aanbod, inclusiviteit en duurzaamheid.

Zeven stads- en volksfeesten hebben een vaste plek op de reserveringskalender: Koningsnacht/-dag, Nationale Dodenherdenking, Bevrijdingsdag, Keti Koti, Utrecht Canal Pride, Sint Maarten en Sinterklaasintocht.

## GGM-bron

> **OpenbareActiviteit** — "Activiteit in het publieke domein"
> Beleidsdomein: Model VTH (taakveld 1 Veiligheid en Vergunningen)
> Attributen: datumStart, datumEinde, evenmentnaam, locatieOmschrijving, status
> Geen relaties, geen diagrammen.

**Matchsterkte: partieel.** OpenbareActiviteit dekt het basisconcept (activiteit in publiek domein met start/eind, naam, locatie, status), maar is veel dunner dan wat gemeenten in de praktijk registreren. De GGM-entiteit heeft geen relaties met locaties, vergunningen of organisatoren, en mist attributen als omvang, type, beoordelingscriteria. De naam "OpenbareActiviteit" is breder dan "Evenement" — het kan ook betogingen of markten omvatten die in het beleid juist worden uitgesloten.

## BO-definitie

De GEMMA-definitie wijkt af van de GGM-definitie:

- **GGM**: "Activiteit in het publieke domein" — te breed, omvat ook activiteiten die geen evenement zijn
- **GEMMA**: "Georganiseerde activiteit met publiek in de openbare ruimte, waarvoor de gemeente een vergunning verleent en die plaatsvindt op een aangewezen locatie" — specifieker, sluit aan bij gemeentelijke praktijk

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Evenementenlocatie]] | associatie | → | \*..\* | Beleidsnota: evenement vindt plaats op locatie |
| [[Evenementenvergunning]] | associatie | → | 1..1 | Beleidsnota: evenement vereist vergunning |

## Bedrijfsprocessen

- **Evenementenaanmelding** — organisatoren melden evenementen aan in de jaarlijkse aanmeldperiode (1-31 augustus)
- **Beoordeling en verdeling** — bij overaanmelding beoordeelt de gemeente op vier criteria
- **Vergunningverlening** — na plaatsing op de reserveringskalender vraagt de organisator een vergunning aan
- **Toezicht en handhaving** — gemeente houdt toezicht op naleving locatieprofielen
- **Monitoring en evaluatie** — tweejaarlijkse inwonersenquête, vierjaarlijks bewonersonderzoek

## Terugmelding GGM

**Definitieverbetering OpenbareActiviteit.** De huidige GGM-definitie "Activiteit in het publieke domein" is te breed. Een specifiekere definitie en uitbreiding met relaties naar locatie en vergunning zou de bruikbaarheid vergroten. Zie [[Wiki/Analyses/ggm-terugmeldingen]].

⚠️ **Aantekening**: er is behoefte aan een generiek BO **Vergunning** dat domeinoverstijgend werkt. Het GGM kent diverse vergunninggerelateerde entiteiten (VOMAanvraagOfMelding, VTHzaak, Omgevingsvergunning, Parkeervergunning, Ligplaatsontheffing) maar geen overkoepelend vergunningsconcept. [[Evenementenvergunning]] is voorlopig als apart BO opgenomen.
