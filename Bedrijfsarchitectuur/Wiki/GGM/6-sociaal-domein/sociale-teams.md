---
type: ggm-beleidsdomein
naam: Sociale Teams
definitie: "Het informatiedomein dat gegevens omvat over de integrale ondersteuning en hulpverlening die sociale teams bieden aan inwoners, gericht op het bevorderen van zelfredzaamheid, participatie en het oplossen van complexe problemen."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 9
---

# GGM Beleidsdomein: Sociale Teams

### Sociale team:Domeinmodel

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Behandeling** | Een verzameling van interventies om bepaalde behandeldoelen te bewerkstelligen. | datumStart, datumEinde, toelichting | Nee | GGM |
| **Behandelsoort** | Typering van een behandeling | naam, omschrijving | Nee | GGM |
| **Bijzonderheid** | Kenmerkende eigenschap | omschrijving | Nee | GGM |
| **Bijzonderheidsoort** | Typering van een bijzonderheid | naam, omschrijving | Nee | GGM |
| **Caseaanmelding** | Verzoek tot toelating | datum | Nee | GGM |
| **Doelstelling** | Een op korte of middellange termijn nagestreefde situatie | omschrijving | Nee | GGM |
| **Doelstellingsoort** | Typering van een doelstellig | naam, omschrijving | Nee | GGM |
| **SociaalTeamDossier** | SociaalTeamDossier* is een dossier-entiteit binnen het Model Sociale Teams dat de **geïntegreerde registratie van gegevens over ondersteuning, gesprekken, interventies en casusontwikkeling van een sociaal team** voor een inwoner of gezin omvat. | datumStart, omschrijving, datumEinde, status, datumVaststelling | Nee | GGM |
| **SociaalteamDossiersoort** | *SociaalteamDossiersoort* is de classificatie van een *SociaalTeamDossier* die aangeeft **het type of de categorie van het dossier** binnen de context van sociale ondersteuning en casemanagement in een sociaal team. | naam, omschrijving | Nee | GGM |

## Relatiediagrammen

```
Behandeling [0..*] ──── Behandelsoort [1..1] (is van soort)
Bijzonderheid [0..*] ──── Bijzonderheidsoort [1..1] (is van soort)
Doelstelling [0..*] ──── Doelstellingsoort [1..1] (is van soort)
SociaalTeamDossier [1..1] ──── Behandeling [0..*] (heeft behandeling)
SociaalTeamDossier [1..1] ──── Bijzonderheid [0..*] (heeft bijzonderheid)
SociaalTeamDossier [0..1] ──── Caseaanmelding [0..1] (heeft aanmelding)
SociaalTeamDossier [1..1] ──── Doelstelling [0..*] (heeft doelstelling)
SociaalTeamDossier [0..*] ──── SociaalteamDossiersoort [1..1] (heeft soort)
```

## Observaties

- Dit beleidsdomein bevat 9 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 1 diagramgroepen: Sociale team:Domeinmodel (9).
