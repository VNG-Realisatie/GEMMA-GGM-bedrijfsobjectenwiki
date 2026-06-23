---
type: ggm-beleidsdomein
naam: Model Inkomen
definitie: "Het informatiedomein dat gegevens omvat over inkomensvoorzieningen, -regelingen en financiële ondersteuning voor inwoners, gericht op het waarborgen van bestaanszekerheid en participatie in de samenleving."
taakveld: "Inkomen"
aantal_entiteiten: 11
---

# GGM Beleidsdomein: Model Inkomen

### Diagram Basismodel Inkomen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Component** | Een *inkomenscomponent* is een afzonderlijk onderdeel of bron van inkomen, zoals loon, winst uit onderneming, uitkeringen of andere inkomensbronnen, die samen het totale inkomen van een persoon of huishouden vormen. | bedrag, begindatumBetrekkingop, eindatumBetrekkingop, debetCredit, rekeningNummer, grootboekcode, grootboekomschrijving, kostenplaats, groep, omschrijving, toelichting, groepcode | Nee | GGM |
| **ComponentSoort** | *ComponentSoort* is de classificatie of het type van een inkomenscomponent binnen een inkomen- of financiële administratie, waarmee wordt bepaald welke categorie of soort een specifieke component behoort. | regelingcode, regeling, kolom, kolomcode, componentcode, omschrijving | Nee | GGM |
| **Inkomensvoorziening** | Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving | ingangsdatum, einddatum, toekenningsdatum, bedrag, eenmalig, groep, administratieveEinddatum, administratieveStartdatum, betalingsmomentcode, code, datumToekenning, indicatieBlokkering, indicatieStudietoeslag, indicatieUitkeringSplitsen, indicatieUitkeringsspecificatie, versterkkingsvorm, verwerktTotEnMetDatum | Nee | GGM |
| **Inkomensvoorzieningsoort** | Typering van een inkomensvoorziening | naam, omschrijving, wet, vergoeding, vergoedingscode, regeling, regelingscode, code | Nee | GGM |
| **Regeling** | Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert. | startdatum, einddatum, toekenningsdatum, omschrijving | Nee | GGM |
| **Regelingsoort** | Typologie van een regeling | naam, omschrijving | Nee | GGM |
| **UitkeringsRun** | Een *UitkeringsRun* is een geautomatiseerde verwerking in een financieel of administratief systeem waarbij **een groep uitkeringen of betalingen tegelijk wordt berekend en uitgevoerd** als onderdeel van een periodieke batch-verwerking. | datumRun, periodeRun, soortRun, frequentie | Nee | GGM |

### In- en uitstroom inkomensvoorziening

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Huisvestingsoort** | Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, soorthuisvestingCode | Nee | GGM |
| **RedenBlokkering** | Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenBlokkeringCode | Nee | GGM |
| **RedenInstroom** | De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenInstroomCode, CBS-code, CBS-omschrijving | Nee | GGM |
| **RedenUitstroom** | De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering beëindigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen. | begindatumGeldigheid, einddatumGeldigheid, omschrijving, redenUitstroomCode, CBS-code, CBS-omschrijving | Nee | GGM |

## Relatiediagrammen

```
Component [1..*] ──── ComponentSoort [1..1]
Component [1..*] ──── UitkeringsRun [1..1]
Inkomensvoorziening [1..1] ──── Component [1..*]
Inkomensvoorziening ──── Huisvestingsoort
Inkomensvoorziening ──── RedenBlokkering
Inkomensvoorziening ──── RedenInstroom
Inkomensvoorziening ──── RedenUitstroom
Inkomensvoorzieningsoort [1..1] ──── Inkomensvoorziening [0..*]
Regeling [0..*] ──── Regelingsoort [1..1]
```

## Observaties

- Dit beleidsdomein bevat 11 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Diagram Basismodel Inkomen (7), In- en uitstroom inkomensvoorziening (5).
