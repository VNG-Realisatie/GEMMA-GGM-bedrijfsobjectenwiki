---
type: ggm-beleidsdomein
naam: 1 Veiligheid en Vergunningen
definitie: "Het informatiedomein dat gegevens omvat over het waarborgen van veiligheid, handhaving van regels en crisisbeheersing."
taakveld: "1 Veiligheid en Vergunningen"
aantal_entiteiten: 30
---

# GGM Beleidsdomein: 1 Veiligheid en Vergunningen

### Bedrijfsprocessen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Producttype** | Een *producttype* is een categorie of variant van producten die dezelfde aard of kenmerken delen, waarmee producten binnen een groep worden ingedeeld op basis van gemeenschappelijke eigenschappen. | omschrijving | Nee | GGM |

### Brede Handhaving

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **BOA** | Een buitengewoon opsporingsambtenaar (boa) is een ambtenaar met een specifieke opsporingsbevoegdheid. | *(geen attributen)* | Nee | GGM |
| **Combibon** | Een Combibon is een modelformulier dat handhavende ambtenaren gebruiken om geconstateerde overtredingen en de gekozen afdoeningsmodaliteit (bijv. bekeuring of strafbeschikking) vast te leggen. | sanctie | Nee | https://toezichttafel.wordpress.com/kenniskaart/handhaving-en-interventies/combibon/ |
| **Fietsregistratie** | Adminstreren van fietsen | verwijderd, gelabeld | Nee | GGM |
| **VTH-Melding** | Melding met betrekking tot Vergunningen, Toezicht en Handhaving | referentienummer, soortVTHMelding, locatie, straatnaam, geseponeerd, datumSeponering, datumtijdTot, organisatieonderdeel, status, taaktype, beoordeling, overtredingsgroep, resultaat, activiteit, zaaknummer, overtredingscode | Nee | GGM |
| **Waarneming** | Handhavende taak in het kader van VTH | *(geen attributen)* | Nee | GGM |

### Diagram Aanvragen, Zaken en Besluiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **VOMAanvraagOfMelding** | VOM staat voor Vergunning, Ontheffing of Melding. Het betreft hier een melding of een aanvraag voor een vergunning of een ontheffing. | dossiernummer, intaketype, adres, locatie, kadastraleAanduiding, BAGID, activiteiten, toelichting, locatieOmschrijving, kenmerk, internNummer | Nee | GGM |

### Diagram Vergunningen en Meldingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bevinding** | Een *bevinding* is de uitkomst van een waarneming of onderzoek die aangeeft wat is geconstateerd bij beoordeling of inspectie. | controleElement, controleniveau, resultaat, risico, diepte, activiteit, fase, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor | Nee | GGM |
| **Heffinggrondslag** | De maatstaf waarop een belasting is gebaseerd, het bedrag op basis waarvan een bepaalde belasting wordt geheven of de premie voor sociale zekerheid wordt vastgesteld. | domein, hoofdstuk, paragraaf, omschrijving, bedrag | Nee | GGM |
| **Heffingsverordening** | Een *heffingsverordening* is een door de gemeenteraad vastgestelde verordening die de **heffing en invordering van gemeentelijke belastingen en rechten** regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden. | *(geen attributen)* | Nee | GGM |
| **Indiener** | Persoon die meldiing of aanvraag doet | *(geen attributen)* | Nee | GGM |
| **Inspectie** | het inwinnen, verwerken en interpreteren van informatie met het doel om de momentane toestand van de boezemkade vast te stellen. | datumInspectie, inspectietype, datumGepland, status, kenmerk, omschrijving, opmerkingen, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor | Nee | GGM |
| **VTHAanvraagOfMelding** | VTH staat voor Vergunning, Toezicht en Handhaving. Het betreft hier een melding of een aanvraag voor een vergunning of een melding voor Toezicht en/of Handhaving. | omschrijving | Nee | GGM |
| **VTHzaak** | Een *VTHzaak* is een zaak of dossier binnen de gemeentelijke administratie die betrekking heeft op **vergunningverlening, toezicht en handhaving (VTH)** van regels en voorschriften in de fysieke leefomgeving. | verkamering, bevoegdGezag, uitvoerendeInstantie, behandelaar, prioritering, teamBehandelaar | Nee | GGM |
| **Vordering** | Een *vordering* is een juridisch recht dat een schuldeiser heeft om van een andere partij (schuldenaar) een prestatie te ontvangen, zoals een geldbedrag, levering van goederen of uitvoering van een dienst. | vorderingnummer, omschrijving, totaalbedrag, bedragBTW, totaalbedragInclusief, geaccordeerd, geexporteerd, geaccordeerdOp, geaccordeerdDoor, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor | Nee | GGM |
| **Vorderingregel** | Een *vorderingregel* is een afzonderlijke regel of entry in een gegevensset of lijst die een specifieke *vordering* beschrijft, inclusief kenmerken zoals de omvang, datum, type en status van de vordering. | Omschrijving, Bedrag_incl_btw, Bedrag_excl_btw, Type, Btwcategorie, Periodiek, Gemuteerd_door, Mutatiedatum, Aangemaakt_door, Aanmaakdatum | Nee | GGM |
| **WABOAanvraagOfMelding** | Aanvraag of medling in het kader van de Wet algemene bepalingen omgevingsrecht (WABO) | bouwkosten, projectkosten, omschrijving, registratienummer, OLONummer | Nee | GGM |

### Objecten bij Vergunningaanvraag

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Vaartuig** | Een zee- of binnenvaartuig, tot de vaart gebruikt of bestemd, daaronder begrepen drijvende werktuigen, zoals baggerwerktuigen, kranen, bokken, elevators, alsmede woonschepen, glijboten en ponten. | naamVaartuig, registratienummer, kleur, lengte, breedte, hoogte | Nee | GGM |

### Verkamering en Woonoverlast

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Activiteit Omgevingswet** | Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd. | omschrijving | Nee | GGM |
| **MORAanvraagOfMelding** | *MORAanvraagOfMelding* is een aanvraag of melding die een burger of organisatie doet bij de gemeente om een **situatie in de openbare ruimte te melden of te laten beoordelen**, zoals schade, overlast, gevaarlijke situaties of onderhoudsproblemen. | locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst, CROW | Nee | GGM |
| **SubProducttype** | *SubProducttype* is een afgeleide of meer specifieke categorie binnen een *Producttype* die producten verder onderscheidt op basis van gedetailleerde kenmerken. | omschrijving, prioriteit | Nee | GGM |
| **WoonfraudeAanvraagOfMelding** | Melding of aanvraag van woonfraude | meldingTekst, meldingOmschrijving, adres, categorie, locatieOmschrijving | Nee | GGM |
| **WoonoverlastAanvraagOfMelding** | Melding of aanvraag met betrekking tot Woonoverlast | locatie, locatieOmschrijving, meldingOmschrijving, meldingTekst | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AOMStatus** | *(geen definitie in GGM)* | datumBeginStatus, datumEindeStatus, status, statusVolgorde, statuscode | Nee | GGM |
| **Grondslag** | Een *grondslag* is de juridische of normatieve basis waarop een besluit, handeling of rechtspraak steunt; het is hetgeen zijn **basis vindt in wetgeving of andere geldende rechtsregels**. | omschrijving, code | Nee | GGM |
| **Kosten** | *Kosten* zijn de prijs of uitgaven die men moet betalen voor het gebruik, verkrijgen of verbruiken van een product, dienst of middel, doorgaans uitgedrukt in geld. | type, omschrijving, opBasisVanGrondslag, naam, aantal, bedrag, bedragTotaal, vastgesteldBedrag, tarief, eenheid, datumAanmaak, aangemaaktDoor, geaccordeerd, gefactureerdOp, datumMutatie, gemuteerdDoor | Nee | GGM |
| **Leges_Grondslag** | *Leges_Grondslag* is de basis of maatstaf waarop de heffing van leges wordt berekend, zoals de omvang van de werkzaamheden, bouwkosten of andere relevante parameters die in de legesverordening zijn vastgelegd. | omschrijving, datumAanmaak, legesGrondslag, aantalOpgegeven, aantalVastgesteld, eenheid, automatisch, aangemaaktDoor, datumMutatie, gemuteerdDoor | Nee | GGM |
| **Ligplaatsontheffing** | Tijdelijke toestemming voor het innemen van een ligplaats op een locatie in een gebied met een verbod op ligplaatsen. | stickernummer | Nee | GGM |
| **OpenbareActiviteit** | Activiteit in het publieke domein | datumStart, datumEinde, evenmentnaam, locatieOmschrijving, status | Nee | GGM |
| **Precario** | Belasting die specifiek wordt geheven voor het plaatsen van voorwerpen onder, op of boven voor de openbare dienst bestemde gemeentegrond. | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
AanvraagOfMelding (abstract)
    └── MORAanvraagOfMelding
    └── VOMAanvraagOfMelding
    └── VTH-Melding
    └── WoonfraudeAanvraagOfMelding
    └── WoonoverlastAanvraagOfMelding
```

```
Document (abstract)
    └── Heffingsverordening
```

```
Rechtspersoon (abstract)
    └── Indiener
```

```
VOMAanvraagOfMelding (abstract)
    └── VTHAanvraagOfMelding
    └── WABOAanvraagOfMelding
```

```
VTH-Melding (abstract)
    └── Combibon
    └── Fietsregistratie
    └── Waarneming
```

```
Zaak (abstract)
    └── VTHzaak
```

## Relatiediagrammen

```
Activiteit Omgevingswet [1] ──── Leges_Grondslag [1..*] (heeft)
Activiteit Omgevingswet [1..*] ──── VTHzaak [1..*] (Heeft)
BOA [1] ──── VTH-Melding [0..*] (verbalisant)
Bevinding [1..1] ──── Bevinding [0..*]
Bevinding [0..*] ──── Inspectie [1..] (heeft)
Grondslag [1..1] ──── Leges_Grondslag [1..1] (heeft)
Heffinggrondslag [1..*] ──── Activiteit Omgevingswet [1..] (heeft)
Heffingsverordening [1] ──── Heffinggrondslag [0..*] (vermeld in)
Inspectie [1..*] ──── VTHzaak [1..] (heeft)
Kosten [1..*] ──── VTHzaak [1..] (heeft)
Leges_Grondslag [1..*] ──── VTHzaak [1..] (is van)
Producttype [1] ──── VTHzaak [1] (Heeft)
SubProducttype [-1..*] ──── Producttype [1..1] (heeft)
SubProducttype [*] ──── VTHzaak [0..*] (Heeft)
Vordering [1..*] ──── VTHzaak [1..] (heeft)
Vordering [1..] ──── Vorderingregel [1..*] (heeft)
Vorderingregel [1..] ──── Kosten [0..1] (betreft)
```

## Observaties

- Dit beleidsdomein bevat 30 Objecttype-entiteiten (+ 3 Enumeraties).
- Entiteiten zijn gegroepeerd in 6 diagramgroepen: Bedrijfsprocessen (1), Brede Handhaving (5), Diagram Aanvragen, Zaken en Besluiten (1), Diagram Vergunningen en Meldingen (11), Objecten bij Vergunningaanvraag (1), Verkamering en Woonoverlast (17).
- Er zijn 13 generalisatierelaties aanwezig.
