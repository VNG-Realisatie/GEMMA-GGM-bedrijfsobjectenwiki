---
type: element
naam: Activiteit
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Activiteit
ggm_guid: EAID_8BE600D0_EBF4_475b_8801_F387A5D39009
ggm_uml_type: Class
ggm_beleidsdomein: Omgevingswet
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram:
  - "Omgevingswet Juridische Regels (CIMOW)"
  - "Omgevingswet Toepasbare Regels"
  - "Omgevingswet Verzoek Activiteit op Locatie"
ggm_diagram_ids:
  - EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0
  - EAID_B9209AD2_0648_4482_BB24_135F27C2FECC
  - EAID_30B09C29_F649_4248_97FC_35A5F9331BBF
ggm_definitie: "Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd."
ggm_toelichting: "Bijvoorbeeld: het lozen van afvalwater, het bouwen van hoogbouw, het exploiteren van een jachthaven."
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
  Dit BO heeft de GGM-entiteit **Activiteit** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Activiteitsoort** (classificatie) — Typering/referentietabel
  - **Bemiddelingsactiviteit** (detail) — Detailgegeven
  - **Gemachtigde** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **SBIActiviteit** (detail) — Detailgegeven
  - **Specificatie** (detail) — Detailgegeven
  - **Verzoek** (detail) — Detailgegeven
bo_definitie: "Gereguleerd menselijk handelen of nalaten in de fysieke leefomgeving waarvoor regels gelden in het omgevingsplan."
bo_toelichting: "Activiteiten worden hiërarchisch gestructureerd in het omgevingsplan met een tophaak-activiteit per gemeente. Elke activiteit heeft een eigen NEN3610-identificatie, naam en groep, en is gekoppeld aan juridische regels die bepalen of de activiteit vergunningplichtig, meldingsplichtig of vergunningvrij is."
bo_subtypes: []
bo_via_kandidaten:
  - ggm_entiteit: "Gemachtigde"
    ggm_guid: "EAID_02BDED5E_9106_4aed_94C2_513689353284"
    reden: "Een gemachtigde treedt op namens een initiatiefnemer bij een Omgevingswet-activiteit in het algemeen, niet specifiek bij archeologisch onderzoek."
  - ggm_entiteit: "Specificatie"
    ggm_guid: "EAID_DF63FBD0_DCA2_45bd_81E8_EE5E72D38EDE"
    reden: "Generieke specificatie van onderdelen, in Omgevingswet-context toegepast op de activiteit."
  - ggm_entiteit: "Verzoek"
    ggm_guid: "EAID_B18119D9_5BF8_498f_B9D3_ECCE7A770012"
    reden: "Een verzoek aan het bevoegd gezag betreft doorgaans een activiteit onder de Omgevingswet in het algemeen."
bo_synoniemen:
  - naam: Milieubelastende activiteit
    context: "Bal — activiteit met nadelige gevolgen voor het milieu"
  - naam: Bouwactiviteit
    context: "Bbl — activiteit bestaande uit het bouwen van een bouwwerk"
bo_homoniemen:
  - bedrijfsobject: "Activiteit (Musea)"
    ggm_entiteit: Activiteit
    ggm_guid: EAID_A1C60F39_3074_4d1c_A37D_5F431F54DF92
    ggm_beleidsdomein: Musea
    toelichting: "Museumactiviteit met attributen naam, omschrijving, aantalPersonen — ander concept"
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Activiteit]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "bovenliggendeActiviteit — hiërarchische positie in functionele structuur"
  - type: associatie
    bedrijfsobject: "[[Juridische Regel]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "RegelVoorIedereen beschrijft activiteit"
  - type: associatie
    bedrijfsobject: "[[Toepasbare Regel]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Toepasbare regel betreft activiteit"
  - type: associatie
    bedrijfsobject: "[[Gebiedsaanwijzing]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Activiteit en gebiedsaanwijzing zijn gekoppeld via juridische regels"
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/risicobron|Risicobron]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Risicobron is een specialisatie van Activiteit (een activiteit met externe veiligheidsrisico's)"
bedrijfsprocessen:
  - "Omgevingsplanvorming"
  - "Vergunningverlening"
  - "Toezicht en handhaving"
bedrijfsfuncties:
  - "Ruimtelijke ordening"
  - "Vergunningverlening, toezicht en handhaving"
---

# Activiteit

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen NEN3610-identificatie, naam, groep |
| Levenscyclus | ✅ | Kan worden aangemaakt, gewijzigd en beëindigd (status 'B') in het DSO |
| Eigenaarschap | ✅ | Gemeente beheert activiteiten als bronhouder in het omgevingsplan |
| Relaties | ✅ | Hiërarchisch (bovenliggendeActiviteit), gekoppeld aan juridische regels, locaties |
| Meervoud | ✅ | Tientallen per omgevingsplan, hiërarchisch gestructureerd |
| Registratie | ✅ | Geregistreerd in DSO/LVBB met NEN3610-ID |

## Beschrijving

Een Activiteit is menselijk handelen of nalaten dat in het omgevingsplan wordt gereguleerd vanwege gevolgen voor de fysieke leefomgeving. De gemeente definieert activiteiten hiërarchisch: elke activiteit heeft een bovenliggende activiteit, met als top de "tophaak-activiteit" per gemeente ("Activiteit gereguleerd in het omgevingsplan gemeente [naam]").

Per activiteit bepalen juridische regels (type RegelVoorIedereen) of de activiteit vergunningplichtig, meldingsplichtig of vergunningvrij is, via een activiteitregelkwalificatie. Activiteiten zijn gekoppeld aan locaties die aangeven wáár de regels gelden.

Voorbeelden: bouwen van een woning, exploiteren van een horecagelegenheid, lozen van afvalwater, kappen van een boom, aanleggen van een uitrit.

## Specialisaties

| Specialisatie | Omschrijving | Eigen pagina |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/risicobron\|Risicobron]] | Activiteit met externe veiligheidsrisico's (bedrijf, buisleiding of transportroute met gevaarlijke stoffen) | Ja — voldoet zelfstandig aan de 6 BO-criteria, eigen relaties naar Aandachtsgebied/Voorschriftengebied |

## GGM-bron

> "Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd." (GGM, Omgevingswet)

- **Entiteit:** Activiteit
- **Beleidsdomein:** Omgevingswet
- **Attributen:** naam, groep, NEN3610ID
- **Matchsterkte:** exact

## Homoniemen

De GGM-entiteit "Activiteit" komt ook voor in beleidsdomein Musea (EAID_A1C60F39) met attributen naam, omschrijving, aantalPersonen. Dat is een ander concept (museumactiviteit/evenement). Teruggemeld als #106 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| associatie | [[Activiteit]] (zelf) | hiërarchisch | bovenliggendeActiviteit — positie in functionele structuur | GGM/IMOW |
| associatie | [[Juridische Regel]] | ← | RegelVoorIedereen beschrijft activiteit | GGM |
| associatie | [[Toepasbare Regel]] | ← | Toepasbare regel betreft activiteit | GGM |
| associatie | [[Gebiedsaanwijzing]] | ↔ | Gekoppeld via juridische regels en locaties | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | ← | GGM Verzoek betreft activiteit; bouwmelding/sloopmelding/gebruiksmelding zijn verzoeken over specifieke activiteiten | GGM (Verzoek) |
| generalisatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/risicobron\|Risicobron]] | ← | Risicobron is een specialisatie van Activiteit (activiteit met extern veiligheidsrisico) | cross-domein |
| associatie | BOR Beheerobjecten | ← | BOR-objecten ([[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/boom\|Boom]], [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kunstwerk\|Kunstwerk]], etc.) zijn onderwerp van activiteiten (kappen, slopen, bouwen) | cross-domein |

## Bedrijfsprocessen

- **Omgevingsplanvorming** — gemeente definieert activiteiten en koppelt regels
- **Vergunningverlening** — beoordeling aanvragen voor vergunningplichtige activiteiten
- **Toezicht en handhaving** — controle op naleving regels per activiteit

## Bronnen

- [[Wiki/Bronsamenvattingen/Omgevingswet/imow-informatiemodel-omgevingswet]]
- [[Wiki/Bronsamenvattingen/Omgevingswet/besluit-activiteiten-leefomgeving]]
