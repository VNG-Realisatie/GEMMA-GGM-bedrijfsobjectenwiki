audit-skills vereenvoudigen
- `/audit-duplicaten`, `/audit-definities` en `/audit-actoren` zijn te ingewikkeld
- doel: per audit één helder doel, minder stappen, minder overlap met `/lint` en `/write-element`
- audit-duplicaten (6 stappen, 3 rapportcategorieën): overlapt met lint-checks voor homoniemen/synoniemen/symmetrie (`tools/lint_checks.py`)
- audit-definities (4 stappen, scenariotabel + vormcontrole): controleert tegen de definitieregels in `/write-element` Stap 5
- audit-actoren: alleen werkvoorraad, beoordeling via `/assess-element`
- te onderzoeken: welke audit-checks kunnen deterministisch in `tools/lint_checks.py`, welke blijven modelwerk
