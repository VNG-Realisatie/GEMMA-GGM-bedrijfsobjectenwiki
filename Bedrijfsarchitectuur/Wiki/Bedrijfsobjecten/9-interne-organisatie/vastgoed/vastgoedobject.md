---
type: element
naam: Vastgoedobject
onderwerp: [Vastgoed]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vastgoedobject
ggm_guid: EAID_28A6F2AC_5AB1_4f25_8876_931152CA28E0
ggm_uml_type: Class
ggm_beleidsdomein: Vastgoed
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Onderwijs: Leerlingen, POC Vastgoed, Vastgoed Domeinmodel, Vastgoed Leveranciers, Vastgoed verankering RSGB IMBAG]
ggm_diagram_ids: [EAID_33E38059_C973_43ff_97EC_B629923074FF, EAID_8B8444CB_1E64_454b_82F9_48A7C9011CE0, EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291, EAID_06E44472_8C2A_40eb_9965_DCF91A1322C9, EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45]
ggm_definitie: "Perceel of vastgoed waar de gemeente een zakelijk recht heeft, en optioneel verhuurd, verpacht of anderzinds aan een derde partij."
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

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Vastgoedobject** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Adresaanduiding** (detail) — Detailgegeven
  - **Bouwdeel** (detail) — GGM-component van Vastgoedobject
  - **CultuurOnbebouwd** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Locatieonroerendezaak** (classificatie) — Typering/referentietabel
  - **Objectrelatie** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Perceel of vastgoed waar de gemeente een zakelijk recht heeft, en optioneel verhuurd, verpacht of anderzinds aan een derde partij."
bo_toelichting:
bo_subtypes: []
bo_via_kandidaten:
  - ggm_entiteit: "Bouwdeel"
    ggm_guid: "EAID_9A739672_6084_4c05_A13E_59DB13551E58"
    reden: "Een bouwdeel is een zelfstandig deel van een vastgoedobject met eigen onderhoudshistorie, geen werkbon."
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Verhuurbare Eenheid]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een vastgoedobject bevat verhuurbare eenheden"
  - type: associatie
    bedrijfsobject: "[[Vastgoedcontract]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een vastgoedobject heeft contractregels"
  - type: associatie
    bedrijfsobject: "[[MJOP]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een vastgoedobject heeft een MJOP"
  - type: associatie
    bedrijfsobject: "[[Inspectie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een vastgoedobject wordt geïnspecteerd"
  - type: associatie
    bedrijfsobject: "[[Werkbon]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Werk aan een vastgoedobject wordt vastgelegd in werkbonnen"
bedrijfsprocessen: [vastgoedbeheer, verhuur gemeentelijk vastgoed, verduurzaming vastgoedportefeuille, verwerving vastgoed, afstoting vastgoed]
bedrijfsfuncties: [vastgoedmanagement, vastgoedexploitatie, gebouwbeheer]
---

## BO-criteria toetsing

1. **Heeft betekenis** — kernobject van het vastgoeddomein, elke gemeente beheert vastgoed
2. **Herkenbaar voor domeinexperts** — vastgoedbeheerders, beleidsmedewerkers en financiën werken dagelijks met vastgoedobjecten
3. **Eigen bestaan** — een pand of perceel bestaat onafhankelijk van contracten, inspecties of gebruikers
4. **Meervoud** — Amsterdam: ~1.000 panden + ~2.000 percelen; Hulst: ~50 gebouwen + kunstwerken
5. **Levenscyclus** — verwerving → beheer/verhuur → renovatie/verduurzaming → afstoting
6. **Relaties** — naar [[Verhuurbare Eenheid]], [[Vastgoedcontract]], [[MJOP]], [[Inspectie]], [[Werkbon]], Kadastraal Perceel, Pand (BAG)

## Beschrijving

Een vastgoedobject is elk perceel, gebouw of terrein waar de gemeente een zakelijk recht op heeft. De vastgoedportefeuille wordt typisch gecategoriseerd naar gebruik: maatschappelijk vastgoed (buurthuizen, sporthallen, theaters), ambtelijke huisvesting (stadhuis, kantoren, werven), vastgoed zonder beleidsdoel (strategisch vastgoed, parkeren) en grond-/waterpercelen.

Elk vastgoedobject heeft een uitgebreide set kenmerken: adres, boekwaarde, marktwaarde, WOZ-waarde, energielabel, conditiescore (NEN 2767), bouwjaar, oppervlakte en portefeuillecategorie. Het object wordt periodiek geïnspecteerd en heeft een meerjaren onderhoudsplanning (MJOP).

> "De vastgoedportefeuille van Gemeentelijk Vastgoed is een grote, bijzondere, en zeer diverse portefeuille, die bestaat op dit moment uit 1.015 panden, 1.989 grondpercelen en 149 waterpercelen." (bron: Vastgoedstrategie Amsterdam)

## Subtypes

Herkende specialisaties van Vastgoedobject. Gevonden in bronnen. Geen apart BO.

- **Erfstuk** — monumentaal vastgoed dat niet kan worden verkocht en geen beleidsdoel dient (kerktorens, vestingwerken)
- **Maatschappelijk vastgoed** — vastgoed dat een gemeentelijk beleidsdoel dient (onderwijs, zorg, cultuur, sport)
- **Ambtelijke huisvesting** — vastgoed voor de gemeentelijke organisatie (stadhuis, kantoren, werven)

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Vastgoedobject. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Bouwdeel** — zelfstandig aanwijsbaar deel van een gebouw waaraan technische eigenschappen en onderhoudshistorie worden gerelateerd (conform NEN 2767)
- **Bouwdeelelement** — onderdeel van een bouwdeel
- **Adresaanduiding** — de adresaanduiding van het vastgoedobject/WOZ-object
- **Gebruiksdoel** — aanduiding van het gebruiksdoel van het gebouwde object
- **CultuurOnbebouwd** — aanduiding voor de soort cultuur van het onbebouwde gedeelte
- **Objectrelatie** — relatie van het vastgoedobject tot andere objecten (rol-gebaseerd)

## GGM-bron

> Perceel of vastgoed waar de gemeente een zakelijk recht heeft, en optioneel verhuurd, verpacht of anderzinds aan een derde partij.

- **Entiteit:** Vastgoedobject
- **Beleidsdomein:** Vastgoed
- **Attributen:** adresaanduiding, WOZWaarde, marktwaarde, boekwaarde, verzekerdeWaarde, omschrijving, portefeuille, naam, bedragAankoop, aantalEtages, afgekochteErfpacht, afkoopwaarde, asbestrapportageAanwezig, datumAfstoten, datumBerekeningOppervlak, deelportefeuille, objecttype, fiscaleWaarde, gearchiveerd, herbouwwaarde, monument, onderhoudscategorie, provincie, verkoopbedrag, waardeGrond, waardeOpstal, wijk, energielabel, energieverbruik, energiekosten, CO2Uitstoot, jaarLaatsteRenovatie, aantalRioleringen, oppervlakteKantoor, conditiescore, aantalParkeerplaatsen, verkoopbaarheid, afgesprokenConditiescore, kostenplaats, bovenliggendNiveau, bestemmingsplan, locatie, bouwjaar, objectstatuscode, objectstatus, objecttypecode, portefeuillecode, bovenliggendNiveaucode, hoofdstuk, identificatie, foto, toelichting, datumEigendom, datumVerkoop, bouwwerk, brutoVloeroppervlakte, verhuurbaarVloeroppervlak
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/verhuurbare-eenheid\|Verhuurbare Eenheid]] | van-dit-BO | 0..* | Een vastgoedobject bevat verhuurbare eenheden | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] | van-dit-BO | 0..* | Via vastgoedcontractregel | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | van-dit-BO | 0..* | Een vastgoedobject heeft een MJOP | GGM |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]] | van-dit-BO | 0..* | Een vastgoedobject wordt geïnspecteerd | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/werkbon\|Werkbon]] | van-dit-BO | 0..* | Werk aan een vastgoedobject | GGM |
| [[Kadastraal Perceel]] | van-dit-BO | 0..* | Betreft een kadastraal perceel | GGM |

## Bedrijfsprocessen

- Verwerving van vastgoed (koop, huur, nieuwbouw)
- Verhuur en exploitatie van vastgoed
- Beheer en onderhoud (inspecties, MJOP, werkbonnen)
- Verduurzaming vastgoedportefeuille
- Procedure vrijkomend vastgoed (Didam-arrest)
- Afstoting van vastgoed

## Bronnen

- [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam]]
- [[Wiki/Bronsamenvattingen/Vastgoed/beleidsplan-vastgoed-hulst]]
