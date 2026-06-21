Maak een GGM-dekkingsanalyse voor domein: $ARGUMENTS

Doel: inventariseer voor een GGM-beleidsdomein welke GGM-entiteiten wél/niet een BO hebben. Het resultaat is geen aparte pagina, maar een bijwerking van het domeinoverzicht.

Coverage telt en signaleert; het beoordeelt niet zelf of een entiteit een BO moet worden. Voor beoordeling: verwijs door naar `/assess-bo`.

Stappen:
1. Lees het geparsede GGM uit `Sources/GGM-repository/ggm_parsed.json`.
2. Bepaal welke GGM-entiteiten tot dit domein behoren via `beleidsdomein` en `taakveld` uit de JSON.
3. Lees de bestaande BO-pagina's in `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/`.
4. Match BO's op GGM-entiteiten via `ggm_guid` (betrouwbaarst) of `ggm_entiteit` naam.
5. Maak een dekkingsoverzicht:

   **GGM-entiteiten MET BO:**
   Per entiteit: naam, ggm_guid, BO-naam, matchsterkte, diagrammen.

   **GGM-entiteiten ZONDER BO:**
   Per entiteit: naam, ggm_guid, definitie, diagrammen. Markeer als "niet beoordeeld" — beoordeling via `/assess-bo`.

   **BO's ZONDER GGM-grondslag:**
   Per BO: naam, grondslag, of dit structureel verwacht is (procesobject/governance-object).

6. Update het **domeinoverzicht**:
   - Werk de GGM-entiteitendekkingstabel bij (entiteiten / BO / niet-BO / niet-beoordeeld per GGM-beleidsdomein).
   - Voeg niet-gedekte data-objecten toe aan de openstaande acties.
7. Voeg hiaten (data-objecten zonder GGM-match) toe aan `Wiki/Analyses/ggm-terugmeldingen.md`.
8. Voeg een entry toe aan `Wiki/log.md`.
