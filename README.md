# AI-ML-Salaries
Analyze Data Science job salaries from 2020 to 2023

📚 Korrigerad sammanfattning av datarensning
Vi har nu färdigställt datarensningen av vårt dataset. Följande steg har genomförts:

✅ Kontrollerat och hanterat saknade värden: Inga saknade värden hittades.

✅ Tagit bort dubbletter: Alla dubbletter har tagits bort från datamängden.

✅ Kontrollerat orimliga värden:

Inga negativa löner eller orimliga remote_ratio-värden upptäcktes.

✅ Kontrollerat och korrigerat kategorier:

Variabler som experience_level, employment_type och company_size har korrekta nivåer.

✅ Kontrollerat logisk konsistens:

Ingen inkonsekvent eller motsägande data identifierades.

✅ Identifierat outliers:

Outliers i lönen (salary_in_usd) identifierades via boxplot, men togs inte bort.

Vi valde istället att analysera sambandet mellan höga löner och andra variabler.

✅ Gjort kategoriska variabler numeriska:

experience_level, employment_type, company_size, job_title har one-hot-enkodats.

✅ Hanterat för många kategorier i job_title:

Endast de 10 vanligaste jobbtitlarna behölls. Övriga titlar grupperades under kategorin "Other".

📢 Kommentar:
Vi valde att behålla outliers eftersom hög lön kan vara relevant och intressant att analysera, särskilt kopplat till exempelvis erfarenhetsnivå, företagsland, företagsstorlek och jobbtitel.

