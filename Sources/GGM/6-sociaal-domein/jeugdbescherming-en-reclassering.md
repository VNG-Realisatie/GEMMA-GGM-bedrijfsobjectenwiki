---
type: ggm-beleidsdomein
naam: Jeugdbescherming en reclassering
definitie: "Het informatiedomein dat gegevens omvat over de uitvoering van kinderbeschermingsmaatregelen, gericht op het waarborgen van een veilige ontwikkeling van kinderen en jongeren."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 4
---

# GGM Beleidsdomein: Jeugdbescherming en reclassering

Beleidsdomein binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

### Zorgmelding

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Informering** | *(geen definitie in GGM)* | indicatieGeinformeerd, redenNietGeinformeerd, datum, reactie | Nee | GGM |
| **Leefgebied** | Een Leefgebied in het kader van jeugdbescherming verwijst naar een specifiek domein binnen het leven van een kind of jongere waarin factoren van invloed zijn op diens veiligheid, welzijn en ontwikkeling. Voorbeelden van leefgebieden zijn gezinssituatie, onderwijs, sociale relaties, gezondheid, vrije tijd en financiën. Bij jeugdbescherming wordt elk leefgebied onderzocht om risico’s en beschermende factoren te identificeren, zodat er een integraal plan kan worden opgesteld om de veiligheid en het welzijn van het kind of de jongere te waarborgen. Leefgebieden vormen daarmee een leidraad voor een holistische benadering in de ondersteuning en interventies. | toelichting, leefgebiedOmschrijving | Nee | GGM |
| **Zorgelijke Situatie** | Een zorgelijke situatie in de context van jeugdbescherming is een omstandigheid waarin de veiligheid, gezondheid, of ontwikkeling van een kind of jongere in het geding is door bijvoorbeeld verwaarlozing, mishandeling, huiselijk geweld, of andere risicofactoren. Deze situaties worden gekenmerkt door signalen van fysieke, emotionele of sociale schade of het ontbreken van een veilige en stabiele omgeving. Een zorgelijke situatie kan leiden tot interventie door jeugdbeschermingsorganisaties om de risico’s te verminderen en het kind of de jongere te beschermen en ondersteunen bij een gezonde en veilige ontwikkeling. | sitiuatieschets, nadereOmschrijving | Nee | GGM |
| **Zorgmelding** | Een Zorgmelding is een officiële melding bij een gemeente of jeugdhulporganisatie waarin zorgen worden geuit over de veiligheid, gezondheid, of ontwikkeling van een kind of jongere. Deze melding kan worden gedaan door professionals, zoals leraren, huisartsen of politie, maar ook door burgers of familieleden. Een zorgmelding bevat signalen of concrete aanwijzingen van mogelijke risico’s, zoals mishandeling, verwaarlozing, huiselijk geweld, of een onveilige thuissituatie. Het doel van een zorgmelding is om de situatie te laten beoordelen en, indien nodig, passende hulp of bescherming te organiseren om het welzijn van het kind of de jongere te waarborgen. | zorgmeldingsoort, terugkoppelingGewenst, verzoek, omschrijving, nadereOmschrijving | Nee | GGM |

## Overervingshiërarchie

```
AanvraagOfMelding (abstract)
    └── Zorgmelding
```

## Relatiediagrammen

### Zorgmelding

```
Incident [1] ──── Informering [0..*] (informering)
Informering [0..*] ──── NatuurlijkPersoon [1] (informering)
Zorgelijke Situatie [1] ──── Incident [0..*] (berust op)
Zorgelijke Situatie [1] ──── Leefgebied [0..*] (toelichting)
Zorgmelding [0..*] ──── Medewerker [0..*] (betrokken professional)
Zorgmelding [0..*] ──── NatuurlijkPersoon [0..*] (betrokkenen)
Zorgmelding [0..*] ──── NatuurlijkPersoon [1] (betreft)
Zorgmelding [1] ──── Zorgelijke Situatie [1..*] (naar aanleiding van)
```

## Observaties

- Dit beleidsdomein bevat 4 entiteiten.
- Entiteiten zijn gegroepeerd in 1 diagramgroepen: Zorgmelding (4).
- Er is 1 generalisatierelatie aanwezig.
