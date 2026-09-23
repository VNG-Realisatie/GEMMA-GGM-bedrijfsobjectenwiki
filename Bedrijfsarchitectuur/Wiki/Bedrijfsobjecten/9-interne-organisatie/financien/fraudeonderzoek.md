---
type: element
naam: Fraudeonderzoek
onderwerp: [Risicobeheer, Financien]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

bo_definitie: "Onafhankelijk onderzoek naar aard, omvang, oorzaak en toedracht van een gesignaleerd, redelijk vermoeden van fraude door raadsleden, collegeleden of ambtenaren."
bo_toelichting: "Onderscheiden van de reguliere verbijzonderde interne controle: het fraudeonderzoek start pas bij een redelijk vermoeden van fraude, wordt uitgevoerd door een onafhankelijke externe adviseur, en kan leiden tot aangifte."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/frauderisicoanalyse|Frauderisicoanalyse]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "De frauderisicoanalyse signaleert fraudegevoelige processen en wordt na afronding van het onderzoek aangescherpt"
bedrijfsprocessen: [Fraudeonderzoek]
bedrijfsfuncties: [Financieel beheer, Risicobeheer]
---

# Fraudeonderzoek

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elk onderzoek betreft een specifiek signaal, met eigen dossier en logboek |
| Eigen attributen | Ja — signaalmoment, betrokkene(n), status (vermoeden/bevestigd), extern adviseur, bevindingen (aard, omvang, oorzaak, toedracht), genomen maatregelen |
| Levenscyclus | Ja — signaal → beoordeling redelijk vermoeden → bevriezen fraudelocatie → onafhankelijk onderzoek door externe adviseur → logboekvoering → informeren verzekeringsmakelaar/aangifte → aanvullende beheersmaatregelen → afronding en terugkoppeling |
| Gemeentelijk eigendom | Ja — de gemeentesecretaris en/of aangewezen vertrouwenspersoon beoordeelt en initieert het onderzoek |
| Wettelijke grondslag | Nee — geen eigen wettelijke vormvoorschriften; proces vastgelegd in het gemeentelijk fraudebeleid, niet in wetgeving |
| Registratieverplichting | Ja — verplichte logboekvoering vanaf het moment van redelijk vermoeden |

Score: 5/6 criteria (geen eigen wettelijke grondslag — een intern beleidsproces, geen wettelijk voorgeschreven procedure).

## Beschrijving

Wanneer bij de frauderisico-analyse, of via een melding vanuit de organisatie, een signaal van mogelijke fraude ontstaat, doorloopt de gemeente een vast proces. Het signaal gaat naar de gemeentesecretaris en/of een aangewezen vertrouwenspersoon, die beoordeelt of er een redelijk vermoeden van fraude bestaat. Is dat het geval, dan wordt de fraudelocatie "bevroren" — administratieve en digitale sporen worden veiliggesteld, eventueel inclusief het blokkeren van netwerktoegang en betaalbevoegdheden.

De gemeente benoemt vervolgens een externe adviseur of raadsman die onafhankelijk onderzoek doet naar aard, omvang, oorzaak en toedracht. Gedurende het hele proces wordt een logboek bijgehouden van alle gebeurtenissen vanaf het moment van het redelijk vermoeden. De gemeente informeert de verzekeringsmakelaar en doet, bij strafbaar handelen, aangifte. Bij geconstateerde fraude worden aanvullende beheersmaatregelen getroffen, gericht op de zwakke plekken in de fraudedriehoek (gelegenheid, druk, rationalisatie) die het mogelijk maakten. Na afronding worden bestuur en organisatie geïnformeerd over de uitkomsten, en worden zowel het fraudebeleid als de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/frauderisicoanalyse|frauderisicoanalyse]] waar nodig aangescherpt.

Vergelijkbaar patroon als het bestaande BO [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/bibob-toets|Bibob-toets]]: beide zijn onderzoeksprocessen die op een signaal reageren en resulteren in een beoordeling met mogelijke rechtsgevolgen.

## Procesbron

Het fraudeonderzoek ontstaat in het proces van fraudebeheersing, zoals beschreven in het gemeentelijk fraudebeleid. Zie [[Wiki/Bronsamenvattingen/Risicobeheer/fraudebeleid-en-frauderisicoanalyse-brummen|Fraudebeleid en Frauderisicoanalyse Gemeente Brummen]], hoofdstuk 4 ("Hoe te handelen bij fraude?").

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/frauderisicoanalyse\|Frauderisicoanalyse]] | → | Aanscherping van de analyse na afronding van het onderzoek |

## Bedrijfsprocessen

- **Fraudeonderzoek** — signaal, beoordeling, bevriezen, onafhankelijk onderzoek, logboek, maatregelen/aangifte, terugkoppeling

## Bronnen
- [[Wiki/Bronsamenvattingen/Risicobeheer/fraudebeleid-en-frauderisicoanalyse-brummen]]

## Terugmelding GGM

GGM-hiaat: geen entiteit voor het fraudeonderzoeksproces. Conceptueel vergelijkbaar met het bestaande BO [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/bibob-toets|Bibob-toets]] (signaal-gedreven onderzoek naar integriteit/rechtmatigheid), maar in een ander domein (interne rechtmatigheid i.p.v. externe vergunningverlening) en zonder eigen wettelijke grondslag — daarom geen generalisatie-relatie, wel vermeld als precedent.
