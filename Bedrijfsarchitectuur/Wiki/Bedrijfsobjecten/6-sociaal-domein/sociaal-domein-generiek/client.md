---
type: element
naam: Client
onderwerp:
- maatschappelijke ondersteuning
- sociaal domein
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Client
ggm_guid: EAID_DAF09055_A5A6_4ff4_A158_21B20567B296
ggm_uml_type: Class
ggm_beleidsdomein: Sociaal Domein Generiek
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Sociaal Domein Domain
- 'Sociaal Domein Beschikking en Voorziening: Domain Objects'
ggm_diagram_ids:
- EAID_FD6966FF_E4FC_437d_983E_71B33445A62C
- EAID_5AE29494_3572_4924_B2B8_3206E55D71BB
ggm_definitie: Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente.
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM
ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:
bo_via_kandidaten:
- ggm_entiteit: Profiel
  ggm_guid: EAID_D8F2EAAD_7C80_4164_8171_C632F18A6742
  reden: "Client [1] heeft Profiel [1..*] rechtstreeks (GGM-relatie); Profiel heeft geen eigen GGM-definitie en is structureel de container die aan Client hangt, niet aan Vermogenscomponent."
- ggm_entiteit: Inkomstenverhouding
  ggm_guid: EAID_0463EA7D_FFD9_AD19_0405_294621AE933F
  reden: "GGM-definitie: 'Inkomstenverhoudingen worden geadministreerd in het profiel van de klant. De klant is de ontvanger van de inkomsten.' Gaat over inkomstenstromen van de client, niet over een vermogensbestanddeel."
- ggm_entiteit: Reden aanvraag
  ggm_guid: EAID_cac6d8c1_42e6_41cb_9907_3c65c081afba
  reden: "Classificatie van de levensomstandigheid van de client die tot een aanvraag leidt (bijv. gestopt betaald werk, overleden partner) — profielgegeven van de client, geen vermogensbestanddeel."
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Client** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Aanvraagtype** (classificatie) — Typering/referentietabel
  - **Betalingsblokkade** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Dienst** (detail) — Detailgegeven (geassocieerd met BO)
  - **Doelgroep** (detail) — Detailgegeven (geassocieerd met BO)
  - **Huishouden** (detail) — Cross-cutting sociaal domein, eenheid voor beoordeling
  - **Individuele plicht** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Inkomstenverhouding** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Leefgebied** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Leveringsopdracht** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Profiel** (detail) — Detailgegeven (geassocieerd met BO)
  - **Reden aanvraag** (classificatie) — Typering/referentietabel
  - **Referteperiode** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Regelingsoort** (classificatie) — Typering/referentietabel
  - **Relatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Relatiesoort** (classificatie) — Typering/referentietabel
  - **Score** (detail) — Detailgegeven (geassocieerd met BO)
  - **Scoresoort** (classificatie) — Typering/referentietabel
bo_definitie: "Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente."
bo_toelichting:
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
  richting: van-dit-BO
  kardinaliteit: "0..*"
  beschrijving: heeft beschikking(en)
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier|SociaalTeamDossier]]"
  richting: van-dit-BO
  kardinaliteit: "0..*"
  beschrijving: heeft dossier(s)
- type: generalisatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]]"
  richting: naar-dit-BO
  kardinaliteit:
  beschrijving: specialisatie van IngeschrevenPersoon
bedrijfsprocessen:
- intake sociaal domein
- ondersteuningsplan opstellen
- voortgang monitoren
bedrijfsfuncties:
- cliëntregistratie
- toegang sociaal domein
---

# Client

Inwoner die gebruik maakt van ondersteuning, zorg of diensten van de gemeente in het sociaal domein. Client is een cross-cutting concept dat in meerdere beleidsdomeinen (Wmo, Jeugdwet, participatie) terugkomt als specialisatie van IngeschrevenPersoon.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | De gemeente registreert cliënten in de Wmo/Jeugd-suite met code, status en gezagsrelaties |
| Meervoud | Duizenden cliënten per gemeente met actieve ondersteuning |
| Levenscyclus | Aanmelding → intake → actieve ondersteuning → afsluiting |
| Eigendom | De gemeente is verantwoordelijk voor de registratie en het toewijzen van ondersteuning |
| Gemeentelijk belang | Wordt besproken in raadsinformatie over Wmo en Jeugdhulp |
| Bronnen | Beleidsnota Jeugd Utrecht, beleidsregels Jeugdhulp Oost Gelre |

## Beschrijving

Client is het centrale subject in het sociaal domein. Elke inwoner die een melding doet, een aanvraag indient of via een verwijzing in beeld komt bij de gemeente, wordt als cliënt geregistreerd zodra er ondersteuning wordt geboden. Het begrip overstijgt de afzonderlijke wetten (Wmo 2015, Jeugdwet, Participatiewet) en vormt de verbindende schakel tussen de verschillende domeinen.

De GGM modelleert Client als specialisatie van IngeschrevenPersoon, met attributen die specifiek zijn voor de zorgrelatie: code, gezagsdragerGekend, juridischeStatus en wettelijkeVertegenwoordiging.

## GGM-bron

> Een ingeschreven persoon die gebruik maakt van producten en diensten van de gemeente.

- **Entiteit:** Client
- **Beleidsdomein:** Sociaal Domein Generiek (taakveld 6 — Sociaal Domein)
- **Attributen:** code, gezagsdragerGekend, juridischeStatus, wettelijkeVertegenwoordiging
- **Overerving:** IngeschrevenPersoon → Client
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Richting | Kardinaliteit |
|---|---|---|---|
| Heeft beschikking(en) | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | → | 0..* |
| Heeft dossier(s) | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | → | 0..* |
| Woonsituatie | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/dak-en-thuislozen/dakloosheid\|Dakloosheid]] | → | 0..1 |
| Maakt deel uit van | Huishouden | → | 0..1 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsregels-jeugdhulp-oost-gelre]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015]]
