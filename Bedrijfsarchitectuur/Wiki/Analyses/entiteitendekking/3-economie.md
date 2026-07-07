---
type: analyse
titel: "Entiteitendekking: 3 Economie"
datum: 2026-07-07
taakveld: "3 Economie"
beleidsdomeinen:
  - 3 Economie
totaal_entiteiten: 6
totaal_bo: 7
totaal_matches: 1
totaal_hiaten: 6
---

# Entiteitendekking: 3 Economie

## Beoordeling

1 beleidsdomeinen, 6 GGM-entiteiten. Dekking: 6 van 6 (100%) — 1 met BO, 5 ondersteunend, 0 niet gedekt. 6 BO's zonder GGM-entiteit.

Niet-BO entiteiten: 5× detail.

Het beleidsdomein 3 Economie modelleert in het GGM opvallend weinig eigen structuur: op Hotel na zijn alle entiteiten detailgegevens die leunen op BO's uit andere domeinen. Contact, Verkooppunt en Werkgelegenheid beschrijven stuk voor stuk kenmerken van [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] (NHR-domein), en Winkelvloeroppervlak hangt via AdresseerbaarObject aan [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] (BAG-domein) — het is een gemeten kenmerk (oppervlakte, WVO-klasse, leegstand, aantal kassa's) van een winkelpand, geen zelfstandig object, en staat daarmee in hetzelfde patroon als Hotelbezoek: een meting/registratie die een bestaand BO nader kwalificeert in plaats van er zelf een te zijn.

Functioneel is de dekking binnen het GGM 100% (geen niet-gedekte entiteiten), maar dat beeld is misleidend: het GGM legt voor taakveld Economie feitelijk alleen het hotel-domein vast. De 6 BO's zonder GGM-tegenhanger — Bed-and-breakfast, Marktstandplaats, Short Stay Accommodatie, Terras, Warenmarkt en Werklocatie — vormen samen het grootste deel van de economische vergunningenpraktijk van gemeenten (horeca-gerelateerd verblijf, markten, terrassen, bedrijfslocaties) en ontbreken volledig in het GGM. Alle zes zijn geregistreerd als procesobject (vergunningverlening), niet als ggm-hiaat, dus vanuit eerdere beoordeling terecht buiten het datamodel gehouden; niettemin suggereert de omvang van deze lijst dat het GGM voor taakveld Economie sterk onderbevolkt is ten opzichte van de bedrijfsobjecten die gemeenten daadwerkelijk registreren.

Naamconflicten of homoniemen doen zich in dit domein niet voor — de Naamoverlap-kolom is voor alle rijen leeg.

## 3 Economie

6 entiteiten, 1 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/3-economie/3-economie\|Hotel]] | [[Wiki/Bedrijfsobjecten/3-economie/economie/hotel\|Hotel]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/3-economie/3-economie\|Contact]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/3-economie/3-economie\|Hotelbezoek]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/3-economie/economie/hotel\|Hotel]] | Meting/transactie, geen zelfstandig object |
| [[Wiki/GGM/3-economie/3-economie\|Verkooppunt]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/3-economie/3-economie\|Werkgelegenheid]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/3-economie/3-economie\|Winkelvloeroppervlak]] | detail | via AdresseerbaarObject → [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | Meetgegeven (vloeroppervlakte + kenmerken winkelpand), geen zelfstandig object |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/3-economie/economie/bed-and-breakfast\|Bed-and-breakfast]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/marktstandplaats\|Marktstandplaats]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/short-stay-accommodatie\|Short Stay Accommodatie]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/terras\|Terras]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/warenmarkt\|Warenmarkt]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/werklocatie\|Werklocatie]] | nee | procesobject | **Alleen GEMMA-BO** |
