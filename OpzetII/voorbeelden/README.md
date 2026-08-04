# Voorbeelden

Een doorgewerkt, **fictief** voorbeeld van de wiki in werking: gemeente "Voorbeeldstad" met een VTH-beleidsplan als bron. Alle citaten en paden zijn verzonnen ter illustratie van het paginamodel — dit is geen echte bron-intake.

De map spiegelt de wiki-mappenstructuur uit [../ontwerp/mappenstructuur.md](../ontwerp/mappenstructuur.md):

```
voorbeelden/
├── bronnen/vth-beleidsplan.md                              source-pagina (stap 1)
├── onderwerpen/vergunningverlening-toezicht-handhaving.md  topic-pagina (stap 2)
├── kandidaten/omgevingsvergunning.md                       Business Object — status goedgekeurd, geëxporteerd
├── kandidaten/omgevingsdienst.md                           Business Actor — status review
├── kandidaten/toezichthouder.md                            Business Role — status kandidaat (stub na extractie)
├── log.md                                                  het logboek van deze keten
└── voortgang.md                                            gegenereerd statusoverzicht
```

De drie kandidaten tonen bewust drie stadia van de statuscyclus:

- **[omgevingsvergunning](kandidaten/omgevingsvergunning.md)** — de volledige cyclus: extractie → bronanalyse → beoordeling (product afgevallen, business object gekozen) → goedgekeurd → geëxporteerd, inclusief een relatie die op de wachtlijst staat omdat het doel nog niet is goedgekeurd.
- **[omgevingsdienst](kandidaten/omgevingsdienst.md)** — beoordeeld en in `review`: multi-type analyse (business actor voorgesteld, business object afgevallen), wacht op teambesluit.
- **[toezichthouder](kandidaten/toezichthouder.md)** — verse stub na type-extractie, met twee overwogen typen (rol én actor) die pas bij beoordeling worden getoetst.
