---
type: element
naam: Verhaal
onderwerp: [werk en inkomen]
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
bo_definitie: "Het besluit waarmee het college de kosten van bijstand verhaalt op een onderhoudsplichtige derde, tot de grens van diens onderhoudsplicht volgens Boek 1 van het Burgerlijk Wetboek."
bo_toelichting: "Grondslag: art. 61-62i Participatiewet. Andere debiteurrelatie dan Vordering: het verhaal richt zich niet op de bijstandsgerechtigde zelf maar op een onderhoudsplichtige derde (ex-echtgenoot, ouder, meerderjarig kind) die zijn onderhoudsplicht niet nakomt. Kan volgen uit een rechterlijke uitspraak (art. 62b) of uit een eigen vaststelling door het college. Degene op wie verhaald wordt kan in verzet komen bij de rechtbank (art. 62b lid 3). Het verhaalsbedrag wordt jaarlijks geïndexeerd (art. 62d) en kan worden herzien bij gewijzigde omstandigheden (art. 62e)."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]]"
  richting: naar-dit-BO
  kardinaliteit: "0..*"
  beschrijving: Verhaal betreft de kosten van een verleende inkomensvoorziening
bedrijfsprocessen: [vaststelling verhaalsrecht, besluit tot verhaal, invordering verhaal, herziening verhaalsbedrag]
bedrijfsfuncties: [inkomensondersteuning, handhaving]
---

# Verhaal

Besluit waarmee de gemeente de kosten van bijstand verhaalt op een onderhoudsplichtige derde — een ex-partner, ouder of meerderjarig kind — in plaats van op de bijstandsgerechtigde zelf.

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Herkenbaar mechanisme, apart van terugvordering |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip bij klantmanagers en juristen sociale zaken |
| Eigen bestaan | ✅ Eigen verhaalsbedrag, eigen debiteur (de onderhoudsplichtige derde, niet de bijstandsgerechtigde) |
| Meervoud | ✅ Meerdere verhaalsbesluiten mogelijk, per onderhoudsplichtige |
| Levenscyclus | ✅ Vaststelling verhaalsrecht → besluit → betaling/invordering → jaarlijkse indexering → herziening bij gewijzigde omstandigheden |
| Relaties | ✅ Relatie met Inkomensvoorziening |

Score: **6/6**

## Beschrijving

Naast het terugvorderen van ten onrechte verstrekte bijstand ([[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|Vordering]]) kan de gemeente de kosten van rechtmatig verleende bijstand verhalen op een derde die daarvoor volgens Boek 1 van het Burgerlijk Wetboek een onderhoudsplicht heeft: een ex-echtgenoot, een ouder jegens een minderjarig kind, een minderjarig kind jegens zijn ouders, of — voor bijzondere bijstand — een meerderjarig kind jegens zijn ouders (art. 62 Participatiewet). Dit is een fundamenteel andere debiteurrelatie dan bij Vordering: de bijstandsgerechtigde zelf blijft buiten de invordering, de onderhoudsplichtige derde betaalt.

Het verhaal volgt bij voorkeur een rechterlijke uitspraak over levensonderhoud (art. 62b); zonder zo'n uitspraak stelt het college het verhaalsbedrag zelf vast met inachtneming van dezelfde maatstaven als een rechter zou hanteren (art. 62a). Degene op wie verhaald wordt kan tegen het besluit in verzet komen bij de rechtbank (art. 62b lid 3). Het verhaalsbedrag wordt jaarlijks geïndexeerd (art. 62d) en kan worden herzien bij gewijzigde omstandigheden (art. 62e) of bij schenking of nalatenschap (art. 62f). Verhuist de bijstandsgerechtigde naar een andere gemeente, dan gaat de bevoegdheid tot invordering mee over (art. 62c).

Het GGM modelleert geen entiteit voor dit verhaalsmechanisme; de bestaande Terug-en-invordering-cluster (Vordering, Aflossingsplan, Kwijtschelding) is gericht op de bijstandsgerechtigde als debiteur, niet op een onderhoudsplichtige derde.

**Onderscheid met Onderhoudsplicht:** de onderliggende onderhoudsplicht-relatie zelf (wie is wettelijk gehouden tot levensonderhoud aan wie, Boek 1 BW titel 17) is civielrechtelijk en wordt niet door de gemeente uitgevoerd of geregistreerd als eigen object — terecht geen BO (zie [[Wiki/Bronsamenvattingen/Werk en Inkomen/burgerlijk-wetboek-boek-1-titel-17-levensonderhoud|BW Boek 1, Titel 17]]). Verhaal is iets anders: het is het besluit waarmee de gemeente die bestaande onderhoudsplicht *verzilvert* ten behoeve van de bijstandskosten — een eigen gemeentelijk proces met eigen besluitvorming, betaling en verzetmogelijkheid.

## Procesbron

Afgeleid uit art. 61-62i Participatiewet (§6.5 Verhaal). Zie [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet|Participatiewet]].

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Verhaal betreft de kosten van deze inkomensvoorziening |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]
- [[Wiki/Bronsamenvattingen/Werk en Inkomen/burgerlijk-wetboek-boek-1-titel-17-levensonderhoud]] (onderhoudsplicht als grondslag voor het verhaalsrecht)

## Terugmelding GGM

GGM-hiaat: het GGM modelleert geen entiteit voor verhaal van bijstandskosten op een onderhoudsplichtige derde — een andere debiteurrelatie dan de bestaande Terug-en-invordering-cluster (Vordering e.a.), die alleen de bijstandsgerechtigde zelf als debiteur kent. Teruggemeld als #96 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
