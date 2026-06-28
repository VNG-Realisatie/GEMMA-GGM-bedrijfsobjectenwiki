---
type: bronsamenvatting
titel: Procesbeschrijving iJw 3.1
onderwerp: [Maatschappelijke Ondersteuning]
datum_ingest: 2026-06-27
---

## Samenvatting

Officiële procesbeschrijving bij release iJw 3.1 (30 september 2021, van kracht 1 april 2022), opgesteld door het Ketenbureau i-Sociaal Domein. Het document beschrijft het volledige ketenproces van de Jeugdwet-gegevensuitwisseling tussen gemeente en aanbieder, gestructureerd in vier fasen: Beoordelen, Toeleiden, Leveren en Declareren.

Het ketenproces kent drie **uitvoeringsvarianten**:
- **Inspanningsgericht:** gemeente wijst specifiek product toe met volume, eenheid en frequentie; toewijzing kan specifiek, aspecifiek (alleen productcategorie + budget) of generiek (alleen budget) zijn.
- **Outputgericht:** gemeente en aanbieder spreken te behalen output af; het product is vooraf gedefinieerd met een aantal of bedrag.
- **Taakgericht:** aanbieder bepaalt zelf de toegang; geen individuele toewijzing door gemeente, maar een taak voor een (deel)populatie met een totaalbedrag.

**Beoordelen** — de gemeente (of sociaal wijkteam, huisarts, rechter, gecertificeerde instelling) stelt vast of de cliënt toegang heeft tot jeugdhulp en stelt een [[Beschikking]] vast. Bij inspannings-/outputgericht wordt vastgelegd welke producten, in welke omvang en voor welke periode.

**Toeleiden** — de gemeente stuurt een [[Toewijzing]] aan de aanbieder als opdracht tot levering. Toewijzingen kunnen worden gewijzigd (via Verzoek om Wijziging door aanbieder) of ingetrokken. Intrekkingsredenen zijn gecodeerd: cliënt overleden, contractwijziging, herbeoordeling, verhuizing, uitstroom naar ander domein, wijziging leveringsvorm (naar PGB), overstap naar andere aanbieder, gemeentelijke herindeling, of correctie (reden 13: verwijderd, reden 14: administratieve correctie).

**Leveren** — de aanbieder meldt via Start- en Stopberichten (regieberichten) wanneer de [[Levering]] daadwerkelijk plaatsvindt. Regieberichten zijn informatief en mogen niet voorwaardelijk zijn voor declaraties. Bij tijdelijke beëindiging (bijv. ziekenhuisopname) blijft de toewijzing geldig en kan later hervat worden.

**Declareren** — de aanbieder declareert maandelijks de geleverde producten. De gemeente beantwoordt binnen 10 werkdagen met een declaratie-antwoordbericht. Afgewezen prestaties kunnen gecorrigeerd worden aangeleverd. Bij taakgerichte uitvoering vindt geen declaratie via het berichtenverkeer plaats.

## Kernbegrippen

- **[[Beschikking]]** — formeel besluit op aanvraag/melding; legt producten, omvang en periode vast
- **[[Toewijzing]]** — opdracht van gemeente aan aanbieder; kan specifiek, aspecifiek of generiek zijn
- **[[Levering]]** — daadwerkelijk geleverde zorg; gemeld via Start- en Stopberichten
- **Verzoek om Toewijzing (VOT)** — bericht van aanbieder aan gemeente om toewijzing te vragen (bij bestaand recht op jeugdhulp); gemeente toetst woonplaatsbeginsel
- **Verzoek om Wijziging (VOW)** — bericht van aanbieder bij verandering cliëntsituatie (verlengen, verkorten, volume/budget wijzigen, nieuw product)
- **Declaratie** — opgave van te vergoeden kosten door aanbieder, maandelijks ingediend
- **Prestatie** — individuele declaratieregel met bedrag, product en productperiode
- **Uitvoeringsvariant** — inspanningsgericht, outputgericht of taakgericht; bepaalt hoe toewijzing en declaratie verlopen
- **Regiebericht** — Start- en Stopzorg; informatief, niet voorwaardelijk voor declaratie
- **Intrekking** — beëindiging van toewijzing door gemeente, met gecodeerde reden
- **Woonplaatsbeginsel** — bepaalt welke gemeente verantwoordelijk is voor een jeugdige

## Relevantie voor bedrijfsarchitectuur

Het document geeft de procescontext bij de bestaande BO's [[Beschikking]], [[Toewijzing]], [[Levering]] en [[Client]]. Het beschrijft de drie uitvoeringsvarianten die bepalen hoe de gemeente-aanbieder interactie verloopt. Declaratie wordt als apart processtap beschreven met eigen berichtenverkeer en attributen.

De berichttypen (VOT, VOW, Start/Stop, Intrekking) zijn onderdelen van het protocol en worden niet als zelfstandige BO's gemodelleerd; ze zijn processtappen die leiden tot wijzigingen in Toewijzing en Levering.

## Bronnen

- [[Sources/Onderwerpen/Maatschappelijke Ondersteuning/procesbeschrijving-ijw-3.1]]
