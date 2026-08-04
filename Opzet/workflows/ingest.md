# Workflow: ingest

Van bron naar onderbouwde wiki-pagina's. De uitvoerbare taakprompt staat in [../prompts/ingest.md](../prompts/ingest.md); dit bestand beschrijft het proces.

## Proces

```
bron(nen) → bespreken → bronsamenvatting → begrippen beoordelen → elementen vastleggen → afronden
```

1. **Bronnen identificeren** — bij een onderwerp: welke bronbestanden zijn er en welke hebben al een bronsamenvatting?
2. **Lezen en bespreken** — de volledige bron lezen; kwaliteit en kernpunten met de gebruiker bespreken (welke bestanden zijn rijk, welke begrippen springen eruit). Nog niets schrijven. Niet-relevante bestanden verhuizen naar een `Niet-relevant/`-submap.
3. **Bronsamenvatting** aanmaken per bron ([../templates/bronsamenvatting.md](../templates/bronsamenvatting.md)).
4. **Begrippen beoordelen** — per begrip de volledige beoordeling ([../prompts/assess-element.md](../prompts/assess-element.md)); het getrapte autonomiemodel bepaalt wat zelfstandig mag en wat wordt voorgelegd.
5. **Elementen vastleggen** — per goedgekeurde kandidaat een pagina met GGM-match en onderbouwing ([../prompts/write-element.md](../prompts/write-element.md)).
6. **Onderwerpoverzicht bijwerken** — begrippentabel aanvullen, verwerkte bronnen registreren ([../templates/onderwerpoverzicht.md](../templates/onderwerpoverzicht.md)).
7. **Afronden** — `Wiki/index.md`, `Wiki/log.md` en de ingest-backlog bijwerken; bij een afgerond onderwerp de dekkingsanalyse verversen.

Eén bron kan 10-15 wiki-pagina's raken — dat is normaal.

## Kwaliteitsanker

De keten moet na elke ingest sluitend zijn: elke nieuwe elementpagina verwijst naar bronsamenvattingen, elke bronsamenvatting naar het bronbestand, en het onderwerpoverzicht toont van elk begrip de beoordeling — óók van afgewezen begrippen (BO? = ❌ met reden).
