---
type: domein
naam: gevaarlijke-stoffen
status: afgerond
verwerkingsdatum: 2026-06-20
bronnen_count: 1
begrippen_count: 9
bo_count: 3
---

## Beschrijving

Omgevingsveiligheid betreft de beheersing van risico's voor de leefomgeving als gevolg van het vervoer, de opslag en de verwerking van gevaarlijke stoffen. De gemeente Utrecht maakt beleidskeuzes over hoe zij haar inwoners en bezoekers beschermt tegen de gevaren van risicobronnen (bedrijven, buisleidingen, transportroutes). Het beleid is onderdeel van de Omgevingsvisie Utrecht en gebaseerd op het Besluit kwaliteit leefomgeving (Bkl) onder de Omgevingswet.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[Risicobron]] | object | Bedrijf, buisleiding of transportroute waar gevaarlijke stoffen worden verwerkt of vervoerd | ✅ | 6/6 criteria, partieel match | LPG-tankstation, aardgasleiding, A2 | partieel |
| [[Aandachtsgebied]] | object | Ruimtelijk gebied rond een risicobron waarbinnen mensen slachtoffer kunnen worden van een incident | ✅ | 6/6 criteria, partieel match | brandaandachtsgebied, explosieaandachtsgebied, gifwolkaandachtsgebied | partieel |
| [[Voorschriftengebied]] | object | Aangewezen deel van een aandachtsgebied met aanvullende bouweisen voor nieuwbouw | ✅ | 6/6 criteria, partieel match | brandvoorschriftengebied, explosievoorschriftengebied | partieel |
| plaatsgebonden risico | norm | Kans op overlijden op een bepaalde afstand van de risicobron | ❌ | Meetwaarde/norm, geen eigen bestaan als object | PR 10⁻⁶ contour | nee |
| groepsrisico | norm | Kans op overlijden van 10 of meer personen bij een incident | ❌ | Meetwaarde/norm | fN-curve | nee |
| oriëntatiewaarde | norm | Referentiewaarde voor toetsing van het groepsrisico | ❌ | Normwaarde, eigenschap van groepsrisico | — | nee |
| (beperkt) kwetsbare gebouwen | classificatie | Wettelijke indeling van gebouwen naar kwetsbaarheid | ❌ | Classificatie/eigenschap van gebouwen | woning, kantoor, sporthal | nee |
| zeer kwetsbare gebouwen | classificatie | Gebouwen voor mensen die niet zelfstandig kunnen vluchten | ❌ | Classificatie/eigenschap van gebouwen | basisschool, kinderopvang, ziekenhuis | nee |
| basisnet | instrument | Landelijk netwerk voor vervoer gevaarlijke stoffen | ❌ | Landelijk instrument, niet gemeentelijk | snelwegen, spoorwegen, waterwegen | nee |

## GGM-entiteitendekking

| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Omgevingswet | 34 | 0 | 0 | 34 | Generiek Omgevingswet-domein; 3 BO's matchen partieel op entiteiten uit dit domein (Gebiedsaanwijzing, Activiteit) maar zijn niet 1:1 overgenomen |

### GGM-dekkingsanalyse

Het GGM heeft geen specifiek beleidsdomein voor omgevingsveiligheid of gevaarlijke stoffen. De relevante entiteiten zitten in het generieke Omgevingswet-package (34 entiteiten). De drie BO's uit dit domein matchen partieel op bestaande GGM-entiteiten:

- **Risicobron** matcht partieel op `Activiteit` — een risicobron is een specifiek type activiteit met externe veiligheidsrisico's.
- **Aandachtsgebied** en **Voorschriftengebied** matchen partieel op `Gebiedsaanwijzing` — het zijn specialisaties van gebiedsaanwijzingen specifiek voor omgevingsveiligheid.

Dit patroon is structureel: het GGM modelleert generieke Omgevingswet-concepten, terwijl het gemeentelijk beleid per thema (geluid, veiligheid, etc.) specifiekere objecten hanteert.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/gevaarlijke-stoffen/beleidsnota-omgevingsveiligheid|Beleidsnota Omgevingsveiligheid Utrecht]]

## Nog te verwerken bronnen

Geen.

## Openstaande vragen

- Bij toekomstige GGM-releases: worden aandachtsgebieden en voorschriftengebieden als aparte entiteiten opgenomen, of blijven ze onder Gebiedsaanwijzing?
- De energietransitie (hoofdstuk 6 van de beleidsnota) introduceert nieuwe risicobronnen (buurtbatterijen, laadpalen, waterstofbuisleidingen) — deze zijn nog niet beleidsmatig uitgewerkt.
