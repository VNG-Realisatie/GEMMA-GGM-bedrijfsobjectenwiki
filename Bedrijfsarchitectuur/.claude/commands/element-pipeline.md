Verwerk begrip(pen) tot element: $ARGUMENTS

Input: begripsnaam (of lijst/onderwerp), nog niet beoordeeld.
Output: BO-/actor-/rol-pagina bij een positieve beoordeling, anders een afwijzing met reden. Bevat zelf geen beoordelings- of vastlegginglogica — orchestreert alleen `/assess-element` en `/write-element`.

Orchestrator voor de keten "begrip → beoordeeld → vastgelegd". Enige plek waar deze sequencing staat: wordt aangeroepen door `/ingest` en `/audit-element` (modus `werkvoorraad`), en kan ook direct door de gebruiker voor een los begrip worden gestart.

Volg deze stappen exact, per begrip (niet in batch — zie `/assess-element` Stap 12):

1. **Beoordeel** — voer `/assess-element {begrip}` uit (classificatie, criteria, data-object, hiaat).
2. **Beslis op basis van de uitkomst** (autonomieregels: `/assess-element` Stap 11):
   - **BO, actor of rol** (zelfstandig af te handelen) → ga naar stap 3.
   - **Geen BO** → geen vervolgactie; geef de beoordeling terug aan de aanroepende skill voor de begrippentabel (BO?=❌, reden).
   - **Voorleggen aan het team** (governance-instrument, <5 criteria, matchsterkte partieel/zwak, generalisatiekeuze, GGM-terugmelding) → presenteer de beoordeling aan de gebruiker (`/assess-element` Stap 12) en wacht op akkoord voordat je naar stap 3 gaat.
3. **Leg vast** — voer `/write-element {begrip}` uit (GGM-match + pagina aanmaken). Bij het twee-pagina-patroon (actor/rol én BO): beide pagina's.
4. **Rapporteer terug** aan de aanroepende skill of gebruiker: welke pagina('s) zijn aangemaakt, of waarom niet.

Bij "onderwerp X" of een lijst begrippen: herhaal stap 1-4 per begrip.
