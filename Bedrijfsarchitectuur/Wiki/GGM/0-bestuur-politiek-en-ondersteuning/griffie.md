---
type: ggm-beleidsdomein
naam: Griffie
definitie: "Het informatiedomein dat gegevens omvat over de ondersteuning van de gemeenteraad en de organisatie van raadsprocessen, gericht op het faciliteren van besluitvorming en democratische controle."
taakveld: "0 Bestuur, Politiek en Ondersteuning"
aantal_entiteiten: 13
---

# GGM Beleidsdomein: Griffie

### Diagram Griffie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanwezige Deelnemer** | iemand die meedoet aan eencollege- of raadsvergadering | aanvangAanwezigheid, eindeAanwezigheid, rol, vertegenwoordigtOrganisatie, naam | Nee | GGM |
| **Agendapunt** | Een onderwerp dat in de vergadering wordt behandeld. | nummer, titel, omschrijving | Nee | GGM |
| **Collegelid** | Iemand die behoort het college van burgemeester en wethouders | voornaam, achternaam, titel, fractie, portefeuille, datumAanstelling, datumUittreding | Nee | GGM |
| **Indiener** | Persoon die meldiing of aanvraag doet | naam, omschrijving | Nee | GGM |
| **Raadscommissie** | Een raadscommissie binnen de Nederlandse gemeenteraad is een groep raadsleden die zich buigt over specifieke thema's of beleidsonderwerpen om de besluitvorming in de volledige raad voor te bereiden en te ondersteunen. | naam | Nee | GGM |
| **Raadslid** | Iemand die behoort de gemeenteraad | voornaam, achternaam, titel, fractie, datumAanstelling, datumUittreding | Nee | GGM |
| **Raadsstuk** | Stuk dat door de gemeenteraad wordt behandeld | datumRegistratie, datumPublicatie, datumExpiratie, besloten, typeRaadsstuk | Nee | GGM |
| **Stemming** | Stem (openbaring van iemands mening (voor of tegen)), uitbrengen bij verkiezingen of bij een vergadering | resultaat, stemmingstype | Nee | GGM |
| **Vergadering** | Een bijeenkomst van meerdere mensen (meestal van eenzelfde organisatie) die met elkaar spreken en/of afspraken maken over de gemeenschappelijke toekomst. | eindtijd, starttijd, titel, locatie | Nee | GGM |

### Diagram Raadsstukken

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Categorie** | Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren | naam | Nee | GGM |
| **Dossier** | Samenhangende set gegevens en informatie voor een specifiek doel | naam | Nee | GGM |
| **Programma** | Een tijdelijke, flexibele organisatiestructuur, die is opgezet om de implementatie van een verzameling met elkaar samenhangende projecten en activiteiten te co&#246;rdineren, te sturen en te controleren teneinde te zorgen voor de realisatie van de eindresultaten en benefits die zijn gerelateerd aan de strategische doelstellingen van de organisatie. | naam | Nee | GGM |
| **Taakveld** | Een samenhangend geheel van activiteiten en taken en hangt onder een programma. | naam | Nee | GGM |

## Overervingshiërarchie

```
Ingezetene (abstract)
    └── Collegelid
    └── Raadslid
```

## Relatiediagrammen

```
Aanwezige Deelnemer [0..1] ──── Collegelid [0..1] (is)
Categorie [0..1] ──── Raadsstuk [0..*] (heeft)
Dossier [0..*] ──── Raadsstuk [0..*] (hoort bij)
Indiener [0..1] ──── Collegelid [0..1] (is)
Indiener [0..1] ──── Raadslid [0..1] (is)
Indiener [0..*] ──── Raadsstuk [1..*] (heeft)
Raadscommissie [0..1] ──── Vergadering [0..*] (heeft)
Raadslid [0..1] ──── Aanwezige Deelnemer [0..1] (is)
Raadslid [0..*] ──── Raadscommissie [0..*] (is lid van)
Raadsstuk [0..*] ──── Agendapunt [0..*] (behandelt)
Raadsstuk [0..*] ──── Programma [0..*] (hoort bij)
Raadsstuk [0..*] ──── Taakveld [0..1] (heeft)
Raadsstuk [0..*] ──── Vergadering [0..*] (wordt behandeld in)
Stemming [0..*] ──── Agendapunt [0..1] (hoort bij)
Stemming [0..1] ──── Raadsstuk [1] (betreft)
Vergadering [1..1] ──── Aanwezige Deelnemer [0..*]
Vergadering [1] ──── Agendapunt [0..*] (heeft)
Vergadering [0..1] ──── Raadsstuk [0..1] (heeft verslag)
```

## Observaties

- Dit beleidsdomein bevat 13 Objecttype-entiteiten (+ 3 Enumeraties).
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Diagram Griffie (9), Diagram Raadsstukken (5).
- Er zijn 2 generalisatierelaties aanwezig.
