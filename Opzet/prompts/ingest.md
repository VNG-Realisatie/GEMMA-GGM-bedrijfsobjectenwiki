# ingest

**Doel:** bron(nen) verwerken tot bronsamenvattingen, onderwerpoverzicht en elementpagina's — de orchestrator die de andere prompts in volgorde aanroept; bevat zelf geen beoordelingslogica.
**Aanbevolen model:** standaard
**Parameters:** {{bron}} — pad naar een bronbestand, een onderwerp (= alle onverwerkte bronnen van dat onderwerp) of een URL. Verplicht.
**Benodigde context:** [../context/regels.md](../context/regels.md), [../context/ai-richtlijnen.md](../context/ai-richtlijnen.md), [../templates/bronsamenvatting.md](../templates/bronsamenvatting.md), [../templates/onderwerpoverzicht.md](../templates/onderwerpoverzicht.md), de bron(nen) zelf, `Wiki/index.md`.
**Verwachte uitvoer:** bronsamenvatting(en), bijgewerkt onderwerpoverzicht, elementpagina's voor goedgekeurde kandidaten, bijgewerkte index/log/backlog.

## Prompt

Verwerk de bron: {{bron}}

Volg deze stappen exact:

1. **Bronnen identificeren.** Bij een onderwerp: inventariseer alle bronbestanden in `Sources/` voor dat onderwerp en welke al een bronsamenvatting hebben.
2. **Lees de bron(nen) volledig.**
3. **Bespreek de kwaliteit** met de gebruiker — welke bestanden zijn rijk aan informatie, welke niet. Bestanden zonder relevante informatie voor elementkandidaten verplaats je naar `Sources/Onderwerpen/{onderwerp}/Niet-relevant/`.
4. **Blik op de bronnen** — welke objecten, relaties en generalisaties springen eruit; welke begrippen zijn kandidaat? Dit is signalering, geen beoordeling. Schrijf nog niets.
5. Na akkoord: **maak per bron een bronsamenvatting** in `Wiki/Bronsamenvattingen/{onderwerp}/` volgens het template.
6. **Beoordeel elk begrip** — voer de prompt `assess-element` uit; het getrapte autonomiemodel bepaalt wat je zelfstandig afhandelt en wat je voorlegt.
7. **Leg goedgekeurde elementen vast** — voer per kandidaat de prompt `write-element` uit.
8. **Werk het onderwerpoverzicht bij** in `Wiki/Onderwerpoverzichten/`: nieuwe begrippen in de begrippentabel (begrip, begripstype, omschrijving, BO?, data-object, reden, voorbeelden, GGM); begrippen die element zijn geworden krijgen een link naar hun pagina; verwerkte bronnen toevoegen aan de bronnenlijst.
9. **Werk `Wiki/index.md` en `Wiki/log.md` bij.**
10. **Werk `ToDo/ingest-backlog.md` bij** — vink verwerkte bronnen af; is een onderwerp-sectie compleet, markeer die als afgerond.
11. **Optioneel:** is het onderwerp afgerond, stel dan voor de dekkingsanalyse te verversen (prompt `entiteitendekking` voor het betreffende taakveld).

## Voorbeeld

> Verwerk de bron: `Sources/Onderwerpen/dierenwelzijn/nota-dierenwelzijn-utrecht.md`
