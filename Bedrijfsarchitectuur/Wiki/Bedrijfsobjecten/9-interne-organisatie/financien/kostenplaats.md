---
type: element
naam: Kostenplaats
onderwerp: [Financien]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Kostenplaats"
ggm_guid: EAID_D90E822D_7EF8_4ea6_AF5C_4A4362577941
ggm_uml_type: Class
ggm_beleidsdomein: "Financien"
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Prinsenhof Events en Relaties, Verplichtingen, Diagram GGM en Inkomen, Subsidies, Subsidie en Kostenplaats, Vastgoed Domeinmodel , Financien Verwerken Mutaties, Financien Verplichtingen en Facturen, Financien Begroting en Budgetverantwoordelijkheid, Diagram Verlengen Inhuur, Diagram Inkoop Inhuur, Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_22110445_1906_4602_8004_6BA4D6C063D0, EAID_4E7479D8_ACA3_45ed_B349_24A3CC271F29, EAID_FD4BAB10_5D3E_4d14_8949_24CA09AC42A7, EAID_F408BDED_51D4_4204_9B95_F0C6C2474DC3, EAID_ACD61AD1_1B3D_46aa_96E7_F438387BE495, EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291, EAID_B758018F_CB22_420e_B4E4_E17EB5F71EDA, EAID_0723EB5C_4A2C_44d4_B15B_37AC71B5D711, EAID_42C2960F_FED7_467e_AAB1_5195BED59A39, EAID_21AD192F_EEF1_493b_9BFD_D37EF6C93236, EAID_1172FBF0_04B4_46c7_9FB5_F34730E060FB, EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Kostenplaats"
ggm_gemma_guid: "126c564a-16fa-4e61-b52d-3af4968904d8"
ggm_gemma_definitie: "Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-126c564a-16fa-4e61-b52d-3af4968904d8"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Kostenplaats** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Batchregel** (onderdeel) — Onderdeel (naamindicatie)
  - **Betaalmoment** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Museumrelatie** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Mutatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Programma** (detail) — Component van Begroting
  - **Programmasoort** (classificatie) — Typering/referentietabel
  - **Subrekening** (detail) — Detailgegeven (geassocieerd met BO)
  - **Subsidiecomponent** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven."
bo_toelichting:
definitie: Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven
bedrijfsprocessen: [Begrotingscyclus, Financiële administratie]
bedrijfsfuncties: [Financieel beheer, Planning en control]
status: concept
---

# Kostenplaats

Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven. Kostenplaatsen maken het mogelijk kosten toe te rekenen aan organisatieonderdelen, projecten of activiteiten.

## GGM-bron

> Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven.

- **Entiteit:** Kostenplaats
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** naam, omschrijving, kostenplaatssoortCode, kostenplaatssoortOmschrijving, kostenplaatstypeCode, kostenplaatstypeOmschrijving, BTWCode, BTWOmschrijving

## Bedrijfsprocessen

- **Begrotingscyclus** — kostenplaatsen structureren de begroting
- **Financiële administratie** — boekingen op kostenplaatsen

## Bedrijfsfuncties

- **Financieel beheer** — kostentoerekening en -bewaking
- **Planning en control** — analyse per kostenplaats

## Relaties

- Onderdeel van de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting|begroting]]structuur
- Relevant voor kostendekkend-tarief: kosten van een bestemmingsbelasting of retributie moeten toerekenbaar zijn aan kostenplaatsen

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/raadgever-inkomstenbronnen]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-gemeentebegroting]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-verordening]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-conditie]]
