Verwerk de bron: $ARGUMENTS

Input: pad naar bronbestand, domeinnaam (voor alle onverwerkte bronnen in dat domein), of URL.

Orchestrator die de andere skills in volgorde aanroept. Bevat zelf geen beoordelingslogica.

Volg deze stappen exact:

1. **Bronnen identificeren.** Bij een domeinnaam: inventariseer alle bronbestanden in `Sources/` voor dat domein en welke al een bronsamenvatting hebben.
2. **Lees de bron(nen).**
3. **Bespreek kwaliteit bron(nen)** met de gebruiker — welke bronbestanden zijn rijk aan info, welke niet. Bestanden zonder relevante informatie voor BO-kandidaten worden verplaatst naar `Sources/{domein}/Niet-relevant/{beschrijvende-slug}.md`.
4. **Blik op bronnen** — bij het eerste doorlezen: welke objecten, relaties en generalisaties springen eruit? Welke begrippen zijn BO-kandidaten? Dit is signalering, niet beoordeling. Schrijf nog niets.
5. Na akkoord: **maak bronsamenvattingen** aan in `Wiki/Bronsamenvattingen/{domein}/` per bron.
6. **Beoordeel begrippen** — per begrip: voer `/assess-bo` uit (alle beoordelingslogica).
7. **Maak BO-pagina's** — per BO-kandidaat: voer `/write-bo` uit (GGM-match + pagina aanmaken).
8. **Update het domeinoverzicht** in `Wiki/Domeinen/`:
   - Voeg nieuwe begrippen toe aan de begrippentabel (begrip, type, omschrijving, BO?, data-object, reden, voorbeelden, GGM).
   - Begrippen die BO's zijn: maak de naam een `[[link]]` naar de BO-pagina.
   - Voeg verwerkte bronnen toe aan de bronnenlijst.
   - **Vul de GGM-entiteitendekking in**: inventariseer alle GGM-entiteiten in de relevante beleidsdomeinen (uit `Sources/GGM/`) en maak een tabel met per beleidsdomein: totaal entiteiten, hoeveel BO, hoeveel niet-BO, hoeveel **niet beoordeeld** (geen beleidsbron). Dit maakt zichtbaar waar de wiki bewust onvolledig is.
9. **Update** `Wiki/index.md` en `Wiki/log.md`.
