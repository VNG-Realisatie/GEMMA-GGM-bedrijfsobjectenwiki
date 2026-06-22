---
type: domein
naam: evenementen
status: afgerond
verwerkingsdatum: 2026-06-20
bronnen_count: 2
begrippen_count: 9
bo_count: 3
---

# Domeinoverzicht: Evenementen

Gemeentelijk domein voor het organiseren, reguleren en faciliteren van buitenevenementen in de openbare ruimte. De gemeente verleent vergunningen, beheert evenementenlocaties met locatieprofielen, en stuurt op spreiding, kwaliteit en diversiteit van het evenementenaanbod via een reserveringskalender en beoordelingscriteria.

## Begrippentabel

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/evenementen/evenement\|Evenement]]|object|Georganiseerde activiteit met publiek in de openbare ruimte| ✅ | ja |6/6 criteria, partiële GGM-match|Festival, braderie, sportevenement, stadsfeest|ja (OpenbareActiviteit)|
|[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/evenementen/evenementenlocatie\|Evenementenlocatie]]|object|Aangewezen fysieke locatie waar evenementen mogen plaatsvinden| ✅ | ja |6/6 criteria, GGM-hiaat|Park, plein, recreatiegebied|nee|
|[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/evenementen/evenementenvergunning\|Evenementenvergunning]]|object|Toestemming van de gemeente om een evenement te organiseren| ✅ | ja |6/6 criteria, GGM-hiaat|Festivalvergunning, vergunning stadsfeest|nee|
|locatieprofiel|instrument|Set van regels per locatie: evenementendagen, omvang, geluid, rust| ❌ | nee |Governance-instrument, geen zelfstandig object|Profiel Maliebaan, profiel Griftpark|nee|
|reserveringskalender|instrument|Jaarlijkse kalender met toegewezen evenementen per locatie/datum| ❌ | nee |Planningsinstrument, geen zelfstandig bestaan los van evenementen|Kalender 2025|nee|
|beoordelingscriteria|regel|Vier criteria voor verdeling bij overaanmelding| ❌ | nee |Beleidsregels, geen object|Maatschappelijke waarde, inclusiviteit|nee|
|stads- en volksfeest|classificatie|Evenement onlosmakelijk verbonden met de stad| ❌ | ja |Classificatie van evenement, geen apart object|Koningsdag, Bevrijdingsdag, Canal Pride|nee|
|rustperiode|regel|Verplichte pauze tussen evenementen op een locatie| ❌ | nee |Regel in locatieprofiel, geen object|12 dagen verhard, 18 dagen onverhard|nee|
|winterbeperking|regel|Extra herstelperiode 1 nov–31 mrt in parken (vanaf 2027)| ❌ | nee |Seizoensregel, geen object|—|nee|

## GGM-entiteitendekking

| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Model VTH | 30 | 1 | 0 | 29 | Alleen OpenbareActiviteit relevant voor evenementen; overige VTH-entiteiten (BOA, Inspectie, Combibon, etc.) vallen buiten dit domein |

### GGM-dekkingsanalyse

Het GGM kent geen beleidsdomein "Evenementen". De enige relevante entiteit is **OpenbareActiviteit** in Model VTH (taakveld 1), een dunne entiteit met vijf attributen en geen relaties of diagrammen. De match met het BO Evenement is partieel: de GGM-definitie ("Activiteit in het publieke domein") is breder dan het evenementenbegrip in de gemeentelijke praktijk.

Evenementenlocatie en evenementenvergunning hebben geen GGM-grondslag. Het GGM kent generieke Locatie-entiteiten in diverse domeinen maar geen specifieke evenementenlocatie. Vergunningen zijn gefragmenteerd over domeinspecifieke entiteiten (Omgevingsvergunning, Parkeervergunning, Ligplaatsontheffing) zonder overkoepelend concept.

Dit patroon — beleidspraktijk rijker dan het datamodel — sluit aan bij het [[Wiki/Analyses/ggm-dekkingspatroon|structurele GGM-dekkingspatroon]].

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Evenementen/locatiebeleid-evenementen|Beleidsnota Locatiebeleid evenementen — Passende ruimte voor evenementen 2024-2030]] — Gemeente Utrecht, juni 2024 (hoofdbron)
- [[Wiki/Bronsamenvattingen/Evenementen/evenementenbeleid-utrecht|Evenementenbeleid Utrecht — overzichtspagina]] — Gemeente Utrecht, omgevingsvisie.utrecht.nl (secundair)

## Openstaande vragen of hiaten

- **Generiek Vergunning-BO**: het GGM kent vergunningen alleen als domeinspecifieke entiteiten. Er is behoefte aan een overkoepelend Vergunning-BO. Evenementenvergunning is voorlopig als apart BO opgenomen.
- **Beleidsdomein Evenementen ontbreekt in GGM**: het hele evenementendomein is niet als beleidsdomein gemodelleerd. OpenbareActiviteit staat geïsoleerd in VTH.

## Terugmeldingen richting GGM

Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
