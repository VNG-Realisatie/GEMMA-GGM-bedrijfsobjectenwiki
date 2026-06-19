---
type: bedrijfsobject
naam: PVT
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: PVT
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Het Participatieverklaringstraject (PVT) is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige kennismaakt met de basiswaarden van de Nederlandse samenleving, en deze onderschrijft door het ondertekenen van de participatieverklaring."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: Leerroute
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Is onderdeel van de leerroute"
---

# PVT

Participatieverklaringstraject — verplicht onderdeel waarin de inburgeraar kennismaakt met de basiswaarden van de Nederlandse samenleving en de participatieverklaring ondertekent.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Het Participatieverklaringstraject (PVT) is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige kennismaakt met de basiswaarden van de Nederlandse samenleving, en deze onderschrijft door het ondertekenen van de participatieverklaring.

- **Entiteit:** PVT
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** Resultaat, DatumOndertekening PVT, RedenNietVoldaan, VerwijtbaarNietVoldaan
- **Matchsterkte:** exact

## Relaties

- ← [[leerroute]] — is onderdeel van de leerroute [1]
