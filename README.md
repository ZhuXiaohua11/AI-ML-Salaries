# AI-ML-Salaries
Analyze Data Science job salaries from 2020 to 2025

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

📊 Analys och Metod

I detta projekt har vi analyserat lönedata inom AI/ML-området genom både explorativa och prediktiva metoder.

🔍 Explorativ analys med PCA
Vi använde Principal Component Analysis (PCA) för att reducera datans dimensioner och förenkla vidare analys. Vår ursprungliga dataset innehöll 25 variabler, och vi reducerade dessa till 2–5 komponenter:

De två första komponenterna (PC1 och PC2) användes för 2D-visualisering.
Visualiseringen visade att datan är heterogen, med stor spridning och utan tydliga kluster.
Tillsammans förklarar PC1 och PC2 cirka 17 % av datans variation.
Vi genomförde även statistiska tester för att undersöka om PC1 varierade mellan olika grupper:

ANOVA-test visade signifikanta skillnader i PC1 för:
Erfarenhetsnivå (F = 1581.370, p < 0.001)
Anställningstyp (F = 4560.401, p < 0.001)
Företagsstorlek (F = 27 269.167, p < 0.001)
Vi undersökte dessutom korrelationer mellan PC1 och numeriska variabler:

PC1 och lön (salary_in_usd): måttlig positiv korrelation (r = 0.323)
PC1 och distansarbete (remote_ratio): svag negativ korrelation (r = -0.156)
Dessa resultat visar att PCA fångar relevant variation kopplad till både gruppskillnader och numeriska mönster i datan.

🤖 Prediktiv analys
Som komplement till den explorativa analysen genomfördes en prediktiv analys med linjär regression och PCA:

Data reducerades med PCA till 5 komponenter.
En linjär regressionsmodell tränades på de nya komponenterna.
Vi använde cross-validation (cv=5) för att utvärdera modellens prestanda.
Modellens genomsnittliga Mean Squared Error (MSE) beräknades och rapporterades.
Vi inkluderade även:

Biplot för att illustrera hur de ursprungliga variablerna påverkar varje komponent.
Visualisering av explained variance för varje komponent.
Dessa steg syftade till att:

✅ Bygga en modell som predicerar lön baserat på underliggande komponenter
✅ Testa hur bra PCA-komponenterna fångar information om lönerna
✅ Kombinera dimensionreduktion med modellutvärdering
