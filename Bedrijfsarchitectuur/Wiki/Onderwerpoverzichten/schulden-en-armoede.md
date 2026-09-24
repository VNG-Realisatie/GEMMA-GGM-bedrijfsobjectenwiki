---
type: onderwerp
naam: schulden en armoede
status: afgerond
verwerkingsdatum: 2026-06-25
bronnen_count: 5
begrippen_count: 34
bo_count: 10
---

# Schulden en armoede

Gemeentelijke schuldhulpverlening: het begeleiden van inwoners met problematische schulden naar financiële stabiliteit. Wettelijke grondslag: Wet gemeentelijke schuldhulpverlening (Wgs, 2012/2021). Omvat het volledige traject van preventie en vroegsignalering tot schuldregeling en nazorg. GGM-beleidsdomein Schulden (taakveld 6 Sociaal Domein) bevat 33 Objecttype-entiteiten verdeeld over twee sub-domeinen: Schuldhulpverlening (27) en Vroegsignalering (6).

## Begrippen

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | object | Volledig begeleidingstraject van aanmelding tot uitstroom | ✅ | ja | 6/6, centraal procesverloop | Minnelijk traject 2024-001 | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuld\|Schuld]] | object | Financiële verplichting aan een schuldeiser | ✅ | ja | 6/6, eigen bedrag/peildatum | Huurschuld €3.200, belastingschuld €12.000 | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldregeling\|Schuldregeling]] | object | Overeenkomst schuldenaar-schuldeisers | ✅ | ja | 6/6, eigen status en levenscyclus | Minnelijke regeling, dwangakkoord | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldeiser\|Schuldeiser]] | actor | Bedrijf of persoon met recht op betaling | ✅ | ja | 6/6, actor met eigen registratie | Belastingdienst, Eneco, VGZ | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/moratorium\|Moratorium]] | object | Tijdelijke blokkering inningsmogelijkheden (art. 287b Fw) | ✅ | ja | 6/6, juridisch instrument met eigen lifecycle | Moratorium huisuitzetting, max 6 mnd | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/wsnp-traject\|WSNP-traject]] | object | Wettelijk schuldsaneringstraject onder bewindvoerder | ✅ | ja | 6/6, apart wettelijk traject | WSNP-traject na weigering minnelijke regeling | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaal\|Vroegsignaal]] | object | Melding betalingsachterstand door signaalpartner | ✅ | ja | 6/6, wettelijk verplicht (Wgs art. 2.2.1) | Signaal zorgverzekeraar, energieleverancier | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaalzaak\|Vroegsignaalzaak]] | object | Zaak voor behandeling vroegsignalen | ✅ | ja | 6/6, specialisatie van Zaak | Zaak bundeling 3 signalen inwoner X | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/signaalpartner\|Signaalpartner]] | actor | Organisatie bevoegd tot melden betalingsachterstanden | ✅ | ja | 6/6, wettelijk gedefinieerde actor | Zorgverzekeraar, woningcorporatie | ja |
| [[Wiki/Rollen/contactpersoon\|Contactpersoon]] | rol | Contactpersoon van een organisatie | ❌ | ja | Rol, geen entiteit; gegevens als BO-tegenhanger [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpersoon\|Contactpersoon (BO)]] | Contactpersoon bij signaalpartner | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpoging\|Contactpoging]] | object | Actie om inwoner te bereiken n.a.v. vroegsignaal | ✅ | ja | 6/6, eigen attributen, meest bepalend voor bereik | Huisbezoek, belpoging, WhatsApp-bericht | ja |
| aanmelding | object | Startmoment schuldhulptraject | ❌ | ja | Procesfase van Schuldhulptraject | Telefonische aanmelding, HDG-gesprek | ja |
| intake | object | Fase inventarisatie hulpbehoefte | ❌ | ja | Procesfase van Schuldhulptraject | Intakegesprek week 2 | ja |
| stabilisatie | object | Fase evenwicht inkomsten/uitgaven | ❌ | ja | Procesfase van Schuldhulptraject | Stabilisatie 3 maanden | ja |
| nazorg | object | Ondersteuning na afronding traject | ❌ | ja | Procesfase van Schuldhulptraject | 6 maanden nazorg | ja |
| crisisinterventie | object | Afwending acute situatie | ❌ | ja | Procesfase van Schuldhulptraject | Voorkomen huisuitzetting | ja |
| oplossing | object | Resultaat schuldregeling (saneringskrediet, schuldbemiddeling) | ❌ | ja | Onderdeel van Schuldhulptraject, 1:1 met traject | Saneringskrediet €18.000 | ja |
| saneringskrediet | object | Lening van GKB om schuldeisers in één keer af te betalen | ❌ | ja | Specialisatie van oplossing | GKB-krediet 18 maanden | nee |
| schuldbemiddeling | object | Periodieke aflossing aan schuldeisers gedurende looptijd | ❌ | ja | Specialisatie van oplossing | Bemiddeling 18 maanden | nee |
| budgetbegeleiding | object | Intensieve begeleiding inkomen/uitgaven | ❌ | ja | Activiteit, geen zelfstandig BO | Mijn Geldzaken-traject | nee |
| beschermingsbewind | instrument | Financieel beheer via rechterlijke machtiging | ❌ | nee | Juridisch instrument, niet gemeentelijk geregistreerd | Schuldenbewind, curator | nee |
| basisdienstverlening | instrument | Landelijk akkoord uniforme minimumkwaliteit SHV | ❌ | nee | Beleidskader, geen data-object | Akkoord VNG/NVVK/Divosa 2024 | nee |
| beslagvrije voet | instrument | Wettelijk beschermd minimuminkomen | ❌ | nee | Norm/parameter, geen zelfstandig object | Wvbvv-berekening | nee |
| collectief schuldregelen | instrument | Methode vooraf akkoord schuldeisers | ❌ | nee | Werkwijze/methode, geen object | NVVK/VNG-methode | nee |
| pauzeknop | instrument | Tijdelijk stopzetten invorderingsacties | ❌ | nee | Instrument binnen traject | Pauze 3 maanden | nee |
| helpdesk geldzaken | object | Laagdrempelige locatie voor financieel advies | ❌ | nee | Kanaal/servicelocatie, geen data-object | 39 locaties Den Haag | nee |
| financiële educatie | thema | Lesprogramma's financiële vaardigheden | ❌ | nee | Activiteit/thema | Lessen 14-18 jaar, SchuldZero | nee |
| vroegsignalering | thema | Proces vroegtijdig signaleren betalingsachterstanden | ❌ | nee | Proces/thema, geen object | Wettelijke plicht sinds 2021 | nee |
| problematische schulden | thema | Situatie waarin schulden niet afgelost kunnen worden | ❌ | nee | Situatie/classificatie | >36 maanden, NVVK-definitie | nee |
| armoede | thema | Structureel tekort aan middelen | ❌ | nee | Breed maatschappelijk thema | — | nee |
| hulpacceptatie | object | Status/uitkomst: inwoner accepteert hulpaanbod | ❌ | nee | Resultaat-attribuut van vroegsignaalzaak | Quick-fix, doorverwijzing | nee |
| drempelbedrag | object | Ondergrens schuldbedrag voor signaalopvolging | ❌ | nee | Parameter/instelling, geen zelfstandig object | €50, €75, €100 | nee |
| laatsignaal | object | Signaal na escalatie (eindelevering, huisuitzetting) | ❌ | ja | Specialisatie: crisissignaal-attribuut op Vroegsignaal | Eindeleveringssignaal energie | ja |
| BRP-koppeling | object | Automatische controle inschrijving bij signaalverwerking | ❌ | nee | Technische integratie, geen data-object | RIS/VPS BRP-koppeling | nee |
| CAK-lijst | object | Overzicht inwoners met achterstand zorgpremie | ❌ | nee | Externe databron, niet gemeentelijk beheerd | CAK-bestand per kwartaal | nee |
| bereikpercentage | object | Aandeel meldingen met succesvol contact | ❌ | nee | KPI/maatstaf, geen data-object | 20% bereik, landelijk gemiddelde | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028|Beleidsplan Schuldhulpverlening Den Haag 2024-2028]]
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/vng-schulden-en-armoede|VNG — Schulden en armoede (rubriek + programma's)]]
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/vroegsignaleringsaanpak-gemeenten-divosa-2024|Divosa — Vroegsignaleringsaanpak gemeenten (2024)]]

## Niet-relevante bronnen

- hersteloperatie-kinderopvangtoeslag.md — specifiek herstelprogramma, geen generieke schuldhulpverlening

## Cross-domein

- [[Wiki/Onderwerpoverzichten/terug-en-invordering|Terug-en-invordering]] — vorderingenbeheer vanuit gemeenteperspectief (de gemeente als schuldeiser). Complementair: dit onderwerp beschrijft de gemeente als schuldhulpverlener.
- [[Wiki/Onderwerpoverzichten/maatschappelijke-ondersteuning|Maatschappelijke ondersteuning]] — Wmo, dakloosheid, buurtteams. Schulden gaan vaak gepaard met problemen op andere leefgebieden.
- [[Wiki/Onderwerpoverzichten/belastingen|Belastingen]] — belastingschuld is meest voorkomende schuld. Kwijtschelding en invordering raken beide domeinen.
