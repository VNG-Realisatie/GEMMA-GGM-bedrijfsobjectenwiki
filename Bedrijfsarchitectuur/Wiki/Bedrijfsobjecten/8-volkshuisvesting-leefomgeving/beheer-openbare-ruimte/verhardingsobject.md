---
type: bedrijfsobject
naam: Verhardingsobject
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Verhardingsobject"
ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: [EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3]
ggm_definitie: "Verharde lagen van een weglichaam, speel- en sportondergronden en onbegroeid terreindelen inclusief de fundering."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Verhard oppervlak in de openbare ruimte — rijbaan, fietspad, voetpad of parkeervak — dat de gemeente beheert en onderhoudt."
gemma_subtypes:
  - naam: Rijbaan
    omschrijving: "Verharding bestemd voor gemotoriseerd verkeer"
    ggm_entiteit: Verhardingsobject
    ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
    ggm_attribuut: verhardingsobjectModaliteit
  - naam: Fietspad
    omschrijving: "Verharding bestemd voor fietsverkeer"
    ggm_entiteit: Verhardingsobject
    ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
    ggm_attribuut: verhardingsobjectModaliteit
  - naam: Voetpad
    omschrijving: "Verharding bestemd voor voetgangers (trottoir)"
    ggm_entiteit: Verhardingsobject
    ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
    ggm_attribuut: verhardingsobjectModaliteit
  - naam: Parkeervak
    omschrijving: "Verharding bestemd voor het parkeren van voertuigen"
    ggm_entiteit: Verhardingsobject
    ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
    ggm_attribuut: verhardingsobjectWegfunctie
  - naam: Asfaltverharding
    omschrijving: "Verharding van asfalt, levensduur 10-70 jaar, geluidsreducerende variant beschikbaar"
    ggm_entiteit: Verhardingsobject
    ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
    ggm_attribuut: materiaal
  - naam: Betonverharding
    omschrijving: "Verharding van beton, levensduur 20-40 jaar"
    ggm_entiteit: Verhardingsobject
    ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
    ggm_attribuut: materiaal
  - naam: Elementenverharding
    omschrijving: "Verharding van gebakken klinkers, levensduur 70-100 jaar"
    ggm_entiteit: Verhardingsobject
    ggm_guid: EAID_47F12418_C5F8_44E0_8EC6_3D0C5993372
    ggm_attribuut: materiaal
bronnen: [Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht, Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007, Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030, Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte, Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte, Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte, Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing, Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]
relaties:
  - type: generalisatie
    bedrijfsobject: Beheerobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Verhardingsobject is een specialisatie van Beheerobject
bedrijfsprocessen: [Wegbeheer, Groot onderhoud verhardingen, Vervanging wegvakken, Inspectie verhardingen, Straatreiniging]
bedrijfsfuncties: [Beheer openbare ruimte, Wegbeheer, Mobiliteit]
ggm_gemma_naam: "Verhardingsobject"
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Grootste beheerpost in de openbare ruimte, fundament van de weginfrastructuur |
| Is herkenbaar voor domeinexperts | ✅ | Wegen, fietspaden, voetpaden — kern van het dagelijks werk |
| Heeft een eigen bestaan binnen het domein | ✅ | Individueel geregistreerd per wegvak met aanlegjaar, materiaal, conditie |
| Kan in meervoud bestaan | ✅ | Duizenden wegvakken, fietspaden en voetpaden |
| Heeft een eigen levenscyclus | ✅ | Aanleg → dagelijks onderhoud → groot onderhoud (deklagen) → vervanging; theoretische levensduur 40 jaar |
| Heeft relaties met andere concepten | ✅ | Weginrichtingsobject, kwaliteitsniveau, inspectie, melding, ondergrond |

Score: 6/6.

## Beschrijving

Een verhardingsobject is een afgebakend stuk verharding in de openbare ruimte: rijbaan, fietspad, voetpad, parkeervak of plein. De gemeente registreert elk wegvak met aanlegjaar, materiaalsoort, constructieopbouw en conditiescore. De theoretische levensduur is 40 jaar, maar de feitelijke levensduur hangt af van aanlegkwaliteit, materiaal en gebruiksintensiteit (zwaar verkeer).

In Utrecht vormen verhardingen de grootste kostenpost in het beheer van de openbare ruimte. Het achterstallig onderhoud bedraagt €35,7 miljoen, vooral in naoorlogse wijken als Overvecht en Kanaleneiland waar veel verhardingen ouder zijn dan 40 jaar. Het onderhoud bestaat uit dagelijks onderhoud (reparaties oneffenheden), groot onderhoud (deklagen) en vervanging. Bij vervanging past de gemeente "ontwikkelend beheer" toe: de verharding wordt niet alleen technisch hersteld maar ook heringericht met aandacht voor vergroening, geluidreductie en klimaatadaptatie.

De kwaliteit wordt gemeten via CROW-beeldkwaliteitsmaatlatten. De ambitie is CROW-niveau B. Bij vervanging worden duurzame materialen toegepast: geluidsreducerend asfalt met tot 60% hergebruikte grondstoffen.

## Specialisaties

### Naar modaliteit (attribuut: verhardingsobjectModaliteit)

| Subtype | Omschrijving | GGM-attribuut |
|---|---|---|
| Rijbaan | Verharding voor gemotoriseerd verkeer | verhardingsobjectModaliteit |
| Fietspad | Verharding voor fietsverkeer | verhardingsobjectModaliteit |
| Voetpad | Verharding voor voetgangers (trottoir) | verhardingsobjectModaliteit |
| Parkeervak | Verharding voor parkeren | verhardingsobjectWegfunctie |

Totaal areaal: 13 miljoen m² wegen, fiets- en voetpaden (Kadernota KOR).

### Naar materiaal (attribuut: materiaal)

| Subtype | Omschrijving | Levensduur |
|---|---|---|
| Asfaltverharding | Asfalt, ook geluidsreducerend (tot 60% hergebruikte grondstoffen) | 10-70 jaar |
| Betonverharding | Beton | 20-40 jaar |
| Elementenverharding | Gebakken klinkers | 70-100 jaar |

Het materiaaltype bepaalt de onderhoudsstrategie en levensduur. De kadernota noemt deze drie als aparte categorieën met elk een eigen levensduurbandbreedte.

Alle subtypes zijn attribuutwaarden op dezelfde GGM-entiteit, geen aparte entiteiten.

## GGM-bron

> "Verharde lagen van een weglichaam, speel- en sportondergronden en onbegroeid terreindelen inclusief de fundering."

- **Entiteit**: Verhardingsobject
- **Beleidsdomein**: Beheer Openbare Ruimte (Model IMBOR)
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Attributen** (55): aanleghoogte, aanOfVrijliggend, aantalDeklagen, aantalOnderlagen, aantalTussenlagen, afmeting, belasting, bergendVermogen, BGTFysiekVoorkomen, breedte, dikteConstructie, draagkrachtig, formaat, fysiekVoorkomenIMGeo, geluidsreducerend, jaarConserveren, jaarOnderhoudUitgevoerd, jaarPraktischEinde, kleur, kwaliteitsniveauActueel, kwaliteitsniveauGewenst, lengte, lengteKunstgras, lengteVoegen, levensduur, materiaal, maximaleValhoogte, omtrek, ondergrondcode, oppervlakte, opTalud, plaatsorientatie, prijsAanschaf, rijstrook, soortVoeg, toelichtingGemengdeBestrating, type, typeConstructie, typeFundering, typePlus, typePlus2, typeRijstrook, typeVoeg, typeVoegvulling, vegen, verhardingsobjectConstructielaag, verhardingsobjectModaliteit, verhardingsobjectRand, verhardingsobjectWegfunctie, verhoogdeLigging, vulmateriaalKunstgras, waterdoorlatendheid, wegas, wegcategorieDV, wegcategorieDVPlus, wegnummer, wegtypeBestaand, wegvak, wegvaknummer

Het GGM-Verhardingsobject is een specialisatie van **Beheerobject**, het abstracte basisobject voor alle objecten in de openbare ruimte.

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Beheerobject (GGM) | Verhardingsobject → Beheerobject | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/kunstwerk\|Kunstwerk]] | bidirectioneel | Beleidsbron: verharding over/langs kunstwerken |

## Bedrijfsprocessen

- **Wegbeheer**: dagelijks onderhoud, reparatie oneffenheden, vegen, onkruidbestrijding
- **Groot onderhoud verhardingen**: aanbrengen nieuwe deklagen, voegwerk
- **Vervanging wegvakken**: volledige vervanging verharding inclusief fundering
- **Inspectie verhardingen**: CROW-beeldkwaliteitsmeting, conditie-inspectie per wegvak
