Verwerk de bron: $ARGUMENTS

Input: pad naar bronbestand, onderwerp (voor alle onverwerkte bronnen in dat onderwerp), of URL.
Output: `Wiki/Bronsamenvattingen/`, `Wiki/Onderwerpoverzichten/`, `Wiki/index.md`, `Wiki/log.md`. Delegeert alleen BO-beoordeling en -aanmaak naar `/assess-element` en `/write-element`.

Orchestrator die de andere skills in volgorde aanroept. Bevat zelf geen BO-beoordelingslogica (die staat in `/assess-element` en `/write-element`), wel de regels onder "Regels bij ingest".

Volg deze stappen exact:

1. **Bronnen identificeren.** Bij een onderwerp: inventariseer alle bronbestanden in `Sources/` voor dat onderwerp en welke al een bronsamenvatting hebben.
2. **Lees de bron(nen).**
3. **Bespreek kwaliteit bron(nen)** met de gebruiker — welke bronbestanden zijn rijk aan info, welke niet. Bestanden zonder relevante informatie voor BO-kandidaten worden verplaatst naar `Sources/{onderwerp}/Niet-relevant/{beschrijvende-slug}.md`.
4. **Blik op bronnen** — bij het eerste doorlezen: welke objecten, relaties en generalisaties springen eruit? Welke begrippen zijn BO-kandidaten? Dit is signalering, niet beoordeling. Schrijf nog niets.
5. Na akkoord: **maak bronsamenvattingen** aan in `Wiki/Bronsamenvattingen/{onderwerp}/` per bron.
6. **Beoordeel begrippen** — per begrip: voer `/assess-element` uit (alle beoordelingslogica).
7. **Maak BO-pagina's** — per BO-kandidaat: voer `/write-element` uit (GGM-match + pagina aanmaken).
8. **Update het onderwerpoverzicht** in `Wiki/Onderwerpoverzichten/`:
   - Voeg nieuwe begrippen toe aan de begrippentabel (begrip, begripstype, omschrijving, BO?, data-object, reden, voorbeelden, GGM).
   - Begrippen die BO's zijn: maak de naam een `[[link]]` naar de BO-pagina.
   - Voeg verwerkte bronnen toe aan de bronnenlijst.
9. **Update** `Wiki/index.md` en `Wiki/log.md`.
10. **Update `Bedrijfsarchitectuur/ToDo/ingest-backlog.md`** — vink verwerkte bronnen af (`[x]`). Als alle bronnen van een onderwerp-sectie zijn afgevinkt, markeer de sectie als afgerond (`~~Onderwerp~~  ✓`).
11. **Optioneel: entiteitendekking verversen** — als het onderwerp is afgerond (alle bronnen verwerkt), stel voor om `/entiteitendekking {taakveld}` te draaien om de dekkingsanalyse te verversen met de nieuwe BO's.

## Regels bij ingest

**Bronselectie (stap 3)**
- NOOIT een bron afwijzen of niet-relevant noemen omdat die van een andere gemeente dan Utrecht komt. Bronnen uit meerdere gemeenten zijn gewenst: ze leiden tot BO's die voor alle gemeenten bruikbaar zijn.
- Beoordeel een bron ALLEEN op inhoudelijke relevantie voor BO-kandidaten.
- NOOIT een bron afwijzen omdat die niet beschrijft wat gemeenten registreren ([BO4]). Governance-/strategiedocumenten noemen concrete objecten (applicatie, dataproduct, overeenkomst) die BO-kandidaat kunnen zijn. Toets alleen of de bron objecten bevat die de 6 criteria halen.

**GGM-dekking (stap 6–7)**
- NOOIT een beleidsdomein of BO-beoordeling overslaan omdat het GGM daar al entiteiten heeft. Ingest verifieert ook het GGM: klopt het, is het compleet, zit het op het juiste abstractieniveau.
- Neem ALLE relevante GGM-beleidsdomeinen op in de begrippentabel en BO-beoordeling.
- Markeer per GGM-entiteit of de beleidsbron deze bevestigt, nuanceert of aanvult.
- Een BO-pagina voor een GGM-entiteit volgt exact hetzelfde template als een nieuwe BO: volledige 6-punts criteria-lijst, `# Naam`-heading met definitie, beschrijving, relaties met wiki-links. Geen verkorte body.
