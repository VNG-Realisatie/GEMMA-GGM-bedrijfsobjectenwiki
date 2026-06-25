---
type: bronsamenvatting
titel: "Catalogus BAG 2018"
onderwerp: [Basisregistraties, BAG]
datum_ingest: 2026-06-25
---

## Samenvatting

De Catalogus BAG 2018 is de systeembeschrijving van de Basisregistratie Adressen en Gebouwen, vastgesteld door de minister van BZK op 29 maart 2018. Sinds 2009 hebben gemeenten de wettelijke taak om basisgegevens over adressen en gebouwen bij te houden in de BAG. Na evaluatie door de Auditdienst Rijk (2013-2014) zijn de voorheen aparte Basisregistratie Adressen en Basisregistratie Gebouwen samengevoegd tot één basisregistratie.

De BAG kent **7 concrete objecttypen** en 1 abstract type:

**Adresobjecten** (vormen samen een adres):
- **[[Woonplaats]]** — door de gemeente aangewezen en van een naam voorzien gedeelte van het grondgebied
- **[[Openbare Ruimte]]** — door de gemeente aangewezen en van een naam voorziene buitenruimte binnen één woonplaats (7 typen: weg, water, spoorbaan, terrein, kunstwerk, landschappelijk gebied, administratief gebied)
- **[[Nummeraanduiding]]** — door de gemeente toegekende aanduiding van een verblijfsobject, standplaats of ligplaats (het "adres": huisnummer + postcode)

**Gebouwobjecten:**
- **[[Pand]]** — kleinste functioneel en bouwkundig-constructief zelfstandige eenheid, direct en duurzaam met de aarde verbonden, betreedbaar en afsluitbaar
- **[[Verblijfsobject]]** — kleinste binnen een of meer panden gelegen eenheid van gebruik, ontsloten via eigen afsluitbare toegang

**Adresseerbare objecten** (krijgen een adres via [[Nummeraanduiding]]):
- **[[Verblijfsobject]]**, **[[Ligplaats]]**, **[[Standplaats]]**
- **Adresseerbaar object** — abstract type waarvan deze drie overerven

De hiërarchie is: Gemeente → [[Woonplaats]] → [[Openbare Ruimte]] → [[Nummeraanduiding]] → Adresseerbaar object ([[Verblijfsobject]]/[[Ligplaats]]/[[Standplaats]]). Een [[Verblijfsobject]] maakt deel uit van een of meer [[Pand]]en.

## Kernbegrippen

- **[[Pand]]** — bouwkundig-constructief zelfstandige eenheid. Gedetailleerde afbakeningsregels: bouwkundige zelfstandigheid, functionele zelfstandigheid, directe en duurzame verbinding met aarde, omsloten en dicht, betreedbaar, kleinste eenheid. Uitzonderingen voor bunkers, hobbykassen, militaire objecten.
- **[[Verblijfsobject]]** — eenheid van gebruik binnen panden. Afbakeningsregels: binnenruimte, samenhangend gebruik met basisvoorzieningen per gebruiksdoel (wonen: keuken/douche/toilet; kantoor: water/toilet; industrie: geen), eigen afsluitbare ontsluiting, onderwerp van goederenrechtelijke handelingen.
- **[[Woonplaats]]** — formeel aangewezen gebiedsdeel met naam. Indeling door het bevoegde gemeentelijke orgaan.
- **[[Openbare Ruimte]]** — benoemde buitenruimte binnen één woonplaats, 7 typen. Vaststelling door formeel gemeentelijk besluit.
- **[[Nummeraanduiding]]** — het adres: huisnummer, huisletter, huisnummertoevoeging, postcode. Gekoppeld aan precies één openbare ruimte en optioneel een woonplaats. Type adresseerbaar object bepaalt of het bij een verblijfsobject, standplaats of ligplaats hoort.
- **[[Ligplaats]]** — aangewezen plaats in het water voor permanent afmeren van drijvend object. Afbakening door formele aanwijzing, daadwerkelijk gebruik niet relevant.
- **[[Standplaats]]** — aangewezen terrein voor permanent plaatsen van verplaatsbare ruimte (bijv. woonwagen). Afbakening door formele aanwijzing, daadwerkelijk gebruik niet relevant.
- **Adresseerbaar object** — abstract type, geen concreet object. Overervingsbasis voor Verblijfsobject, Ligplaats en Standplaats.
- **Gebruiksdoel** — categorisering van het vergunde of geconstateerde gebruik van een verblijfsobject (bijeenkomst, cel, gezondheid, industrie, kantoor, logies, onderwijs, overig, sport, winkel, wonen).
- **Hoofdadres / nevenadres** — elk adresseerbaar object heeft precies 1 hoofdadres; nevenadressen alleen bij meerdere relevante toegangen.

## Relevantie voor bedrijfsarchitectuur

De BAG is de kern van de gemeentelijke gegevenshuishouding. Alle 7 objecttypen zijn wettelijk verplicht te registreren en te gebruiken. Ze vormen het fundament waarop andere registraties aansluiten: WOZ koppelt aan [[Pand]] en [[Verblijfsobject]], BRP koppelt personen aan adressen via [[Nummeraanduiding]], vergunningen refereren aan [[Pand]]en.

> "Registratie in de BAG heeft overigens uitdrukkelijk uitsluitend een administratieve achtergrond en houdt geen legalisering of ander (rechts)gevolg in."

> "De BAG vormt de kern van de overheidsgegevenshuishouding en is verplicht te gebruiken."

De gebiedsindelingen [[Buurt]], [[Wijk]] en [[Gemeente]] zijn geen formele BAG-objecttypen maar worden wel in het GGM-BAG-beleidsdomein gemodelleerd als onderdeel van de ruimtelijke hiërarchie.

## Bronnen

- [[Sources/Standaarden/catalogus-bag-2018]]
