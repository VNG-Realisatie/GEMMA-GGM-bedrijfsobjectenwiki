---
type: bronsamenvatting
titel: "Catalogus Basisregistratie Kadaster"
onderwerp: [Basisregistraties, BRK]
datum_ingest: 2026-06-25
---

## Samenvatting

De Catalogus BRK (versie 1.0, december 2020) is de officiële systeembeschrijving van de Basisregistratie Kadaster in de zin van artikel 48 lid 5 Kadasterwet. De BRK bevat de registratie van onroerende zaken, zakelijke rechten en de kadastrale kaart. Het Kadaster is bronhouder; bestuursorganen (waaronder gemeenten) zijn verplicht gebruiker van authentieke BRK-gegevens. Voor publiekrechtelijke beperkingen (WKPB) is de gemeente één van de bronhouders, naast provincie, waterschap en rijksoverheid.

De catalogus beschrijft het wettelijk kader, de authentieke gegevens en de vertaling naar het informatiemodel Kadaster (IMKAD). Het informatiemodel kent **6 domeinen**:

1. **Kadastraal Object** — generalisatie van Onroerende zaak en Teboekgestelde zaak
2. **Onroerende zaak** — [[Kadastraal Perceel]], [[Appartementsrecht]], Leidingnetwerk
3. **Zakelijk recht** — [[Zakelijk Recht]] (eigendom, beperkte rechten), [[Tenaamstelling]], Zekerheidsstelling
4. **Persoon** — Natuurlijk persoon (koppeling BRP), Niet-natuurlijk persoon (koppeling HR)
5. **Stuk** — [[Stuk]] en [[Stukdeel]] (brondocumenten: notariële akten, kadasterstukken)
6. **Publiekrechtelijke beperking** — [[Publiekrechtelijke Beperking]] en werkingsgebied (WKPB)

De BRK kent **dubbele authenticiteit**: bepaalde gegevens (persoonsnaam, adres) zijn zowel in de BRK als in BRP of BAG authentiek. Bij afwijkingen zijn de brondocumenten (akten) leidend voor de privaatrechtelijke rechtstoestand.

Bijwerking van de BRK vindt plaats via ingeschreven stukken, kadasterstukken, relazen van bevindingen, terugmeldingen en beschikkingen. Bestuursorganen zijn verplicht terugmeldingen te doen bij gerede twijfel over authentieke gegevens.

## Kernbegrippen

- **[[Kadastraal Perceel]]** — kadastraal geïdentificeerd en met kadastrale grenzen begrensd deel van het Nederlands grondgebied (art. 1 lid 1 Kadasterwet). Authentieke gegevens: kadastrale aanduiding, kadastrale grootte, coördinaten.
- **[[Appartementsrecht]]** — aandeel in de goederen die in de splitsing zijn betrokken, met bevoegdheid tot uitsluitend gebruik van bepaalde gedeelten van het gebouw (art. 5:106 lid 4 BW). Geïdentificeerd met kadastrale aanduiding inclusief appartementsrechtvolgnummer.
- **[[Zakelijk Recht]]** — eigendom of beperkt recht (erfpacht, opstal, vruchtgebruik, gebruik en bewoning) van een persoon op een onroerende zaak. Authentieke gegevens: aard van het recht. Rust op een Kadastraal Object.
- **[[Tenaamstelling]]** — relatie tussen een Zakelijk Recht en een Persoon: wie oefent welk recht uit op welk kadastraal object. Authentieke gegevens: persoonsgegevens van de rechthebbende.
- **[[Publiekrechtelijke Beperking]]** — beperking opgelegd door een bestuursorgaan (gemeente, provincie, waterschap, rijk) op een onroerende zaak. De gemeente is bronhouder voor gemeentelijke beperkingen (monument, milieuverordening, voorkeursrecht) en schrijft deze in bij de BRK-PB. Geen authentieke gegevens in BRK-PB, maar wel wettelijk verplichte registratie sinds WKPB 2020.
- **[[Stuk]]** — brondocument ter inschrijving in de openbare registers. Twee soorten: Ter Inschrijving Aangeboden Stuk (notariële akte) en Kadasterstuk (intern correctiestuk). Authentieke gegevens: deel-en-nummer, tijdstip aanbieding.
- **[[Stukdeel]]** — onderdeel van een Stuk waarin rechtsfeiten zijn beschreven (overdracht, hypotheek, splitsing). Bepaalt welke bijwerking van de BRK plaatsvindt.
- **Kadastraal Object** — abstract type, generalisatie van Onroerende zaak (Perceel, Appartementsrecht, Leidingnetwerk) en Teboekgestelde zaak. Identificatie via kadastrale aanduiding.
- **Onroerende Zaak** — abstract, specialisatie van Kadastraal Object. Groepering van Perceel, Appartementsrecht en Leidingnetwerk.
- **Zekerheidsstelling** — hypotheek (ZekerheidsstellingHypothecair) of beslag (ZekerheidsstellingInzakeBeslag) op een kadastraal object.
- **Aantekening** — bijzonderheid bij een kadastraal object, recht of zekerheidsstelling (erfdienstbaarheid, einddatum recht, publiekrechtelijke beperking, kwalitatieve verplichting).
- **Appartementsrechtsplitsing** — het splitsen van een onroerende zaak in appartementsrechten. Onderscheidt hoofd- en ondersplitsing.
- **Kadastrale kaart** — landelijke kaart met perceelsgrenzen, kadastrale aanduidingen en bestuurlijke grenzen. Authentieke gegevens: kadastrale grenzen, perceelnummer.
- **Terugmelding** — melding door bestuursorgaan of belanghebbende van gerede twijfel over juistheid van een authentiek BRK-gegeven. Kan leiden tot aantekening "in onderzoek".

## Relevantie voor bedrijfsarchitectuur

De BRK is het fundament voor gemeentelijk grondbeleid, WOZ-waardering, OZB-heffing, vergunningverlening en handhaving. De gemeente gebruikt BRK-gegevens om te weten:
- **Welke percelen en appartementsrechten** bestaan binnen het grondgebied
- **Wie rechthebbende is** (eigenaar, erfpachter) via zakelijk recht en tenaamstelling — nodig voor OZB-aanslagen, WOZ-beschikkingen, handhaving
- **Welke beperkingen** op een onroerende zaak rusten — en registreert zelf gemeentelijke beperkingen (WKPB-bronhouder)
- **Welke transacties** hebben plaatsgevonden — via stukken/stukdelen

De BRK koppelt aan andere basisregistraties: personen via BRP (BSN), bedrijven via HR (KvK/RSIN), adressen via BAG (nummeraanduiding van verblijfsobject).

> "Een basisregistratie is een door de overheid officieel aangewezen registratie met daarin gegevens van hoogwaardige kwaliteit, die door alle overheidsinstellingen verplicht en zonder nader onderzoek, worden gebruikt bij de uitvoering van publiekrechtelijke taken."

> "Bestuursorganen die veronderstellen dat de BRK een authentiek gegeven niet correct heeft overgenomen uit een brondocument, melden onder opgaaf van redenen hun gerede twijfel omtrent de juistheid van dit in de BRK opgenomen authentieke gegeven."

> "De Wkpb bepaalt dat bestuursorganen die publiekrechtelijke beperkingenbesluiten nemen, de verplichting hebben tot inschrijving in de BRK-PB."

## Bronnen

- [[Sources/Standaarden/catalogus-brk]]
