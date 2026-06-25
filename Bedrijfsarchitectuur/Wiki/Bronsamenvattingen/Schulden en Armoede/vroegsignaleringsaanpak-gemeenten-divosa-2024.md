---
type: bronsamenvatting
titel: "De vroegsignaleringsaanpak van gemeenten onder de loep — Kunnen we je helpen?"
onderwerp: [schulden en armoede]
datum_ingest: 2026-06-25
---

# Divosa — Vroegsignaleringsaanpak gemeenten (2024)

Landelijk vragenlijstonderzoek (Divosa, sept. 2024) onder 167 gemeenten die deelnemen aan de Divosa Monitor Vroegsignalering Schulden. Beschrijft de uitvoeringspraktijk, werkwijzen en keuzes rondom vroegsignalering in vijf processtappen.

## Samenvatting

### 1. Ontvangen en oppakken van vroegsignalen

Gemeenten pakken niet alle signalen op. 64% hanteert een drempelbedrag (mediaan €75). 46% gebruikt een automatische BRP-koppeling om te controleren of iemand op het adres staat ingeschreven; vooral 50.000+-gemeenten. De helft van gemeenten met BRP-koppeling controleert standaard de uitgevallen signalen.

Opvolgingscriteria: in nagenoeg alle gemeenten zijn type melding en bedraghoogte bepalend. Eenderde heeft een leeftijdsgebonden aanpak (jongeren, AOW). 15% let op huishoudsamenstelling (minderjarige kinderen).

> "Bij een signaal gaat het om één signaal van een betalingsachterstand doorgegeven door één vastelastenpartner. [...] Signalen kunnen door een gemeente worden gematcht. Er ontstaat dan een melding (dossier), enkelvoudig of meervoudig." (bron: vroegsignaleringsaanpak-gemeenten-divosa-2024)

### 2. Contact leggen en bereiken van de inwoner

Contactvormen: brief (86%), huisbezoek (100%), telefoon, WhatsApp (49%), sms (43%). Zes op de tien gemeenten hebben afspraken over min/max belpogingen (meestal 2-3). 56% heeft geen maximum huisbezoeken per maand. 28% bezoekt ook 's avonds.

**Contactpogingen zijn de belangrijkste factor voor bereik:** een extra [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpoging\|contactpoging]] leidt tot +11 procentpunt bereik. WhatsApp verhoogt het bereik met 4,7 procentpunt. Andere aspecten van de aanpak hangen niet significant samen met het bereik.

### 3. Hulpacceptatie en (door)verwijzing

Bij 7% van alle opgepakte meldingen werd in 2023 hulpacceptatie geregistreerd (35% van de bereikte inwoners). Er is geen eenduidige definitie: gemeenten registreren quick-fix, doorverwijzing en adviesgesprekken verschillend. 56% registreert alsnog als een inwoner zich na 4 weken meldt; 18% niet meer.

### 4. Laatsignalen

Gemeenten besteden ca. 15% van de tijd aan eindeleveringssignalen en huisuitzettingssignalen. 80% staat positief tegenover het ontvangen ervan, maar de helft vindt het geen *vroeg*signalering meer. 20% gebruikt de CAK-lijst (betalingsachterstand zorgpremie); 36% is dat van plan.

### 5. Leren en ontwikkelen

60% vindt vroegsignalering in eigen gemeente succesvol. Drie graadmeters: (1) inwoners weten de weg naar de gemeente, (2) schulden klein houden, (3) zoveel mogelijk inwoners bereiken. Hulpacceptatie is voor driekwart geen maatstaf voor succes. 8% vindt het expliciet niet succesvol.

## Kernbegrippen

- **[[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaal\|Vroegsignaal]]** — bericht van signaalpartner over betalingsachterstand. Rapport onderscheidt vroegsignalen (regulier) en crisissignalen (eindelevering/huisuitzetting).
- **[[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaalzaak\|Vroegsignaalzaak]]** — "melding" in rapport: gematcht dossier van één of meer signalen. Enkelvoudig, meervoudig of opeenvolgend (recidive).
- **[[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/signaalpartner\|Signaalpartner]]** — vastelastenpartners: zorgverzekeraars, energieleveranciers, drinkwaterbedrijven, woningverhuurders. CAK als additionele signaalbron.
- **[[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpoging\|Contactpoging]]** — actie om inwoner te bereiken. Soorten: brief, telefoon, huisbezoek, WhatsApp, sms. Heeft dag/dagdeel, resultaat (bereikt/niet bereikt). Meest bepalende factor voor bereik.
- **Hulpacceptatie** — status/uitkomst van vroegsignaalzaak. Vormen: quick-fix, doorverwijzing. Geen eenduidige definitie tussen gemeenten.
- **Drempelbedrag** — ondergrens schuldbedrag voor opvolging signaal. Parameter, geen object.
- **BRP-koppeling** — automatische controle inschrijving. Technische integratie.
- **CAK-lijst** — overzicht inwoners met betalingsachterstand zorgpremie. Externe databron.

## Relevantie voor bedrijfsarchitectuur

Belangrijkste bijdrage: empirische onderbouwing van **[[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpoging\|Contactpoging]]** als zelfstandig bedrijfsobject. Het rapport toont aan dat contactpogingen individueel worden geregistreerd (soort, tijdstip, resultaat) en dat ze de meest bepalende factor zijn voor het bereik. Dit bevestigt de GGM-entiteit Contactpoging als BO.

Daarnaast verrijking van bestaande BO's:
- [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaal\|Vroegsignaal]]: crisissignaal-attribuut, drempelbedrag-context
- [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaalzaak\|Vroegsignaalzaak]]: matching-typen, hulpacceptatie als resultaat
- [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/signaalpartner\|Signaalpartner]]: CAK als additionele signaalbron

## Bronnen
- [[Sources/Onderwerpen/Schulden en Armoede/vroegsignaleringsaanpak-gemeenten-divosa-2024]]
