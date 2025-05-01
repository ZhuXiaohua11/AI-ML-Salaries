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

I detta projekt har vi analyserat lönedata inom AI/ML-området genom både explorativa och prediktiva metoder. Vi har använt Principal Component Analysis (PCA) för att förstå datans struktur och, i ett senare steg, även för att bygga prediktiva modeller.

🔍 Explorativ analys med PCA
Syftet med den explorativa analysen var att förenkla datan och identifiera övergripande mönster. Vi reducerade de ursprungliga 25 variablerna till två huvudkomponenter (PC1 och PC2) för att möjliggöra 2D-visualisering. Även om dessa endast förklarar cirka 17 % av den totala variationen, räcker det för att få en visuell känsla för datans struktur och variation.

För att tolka dessa komponenter genomförde vi:

ANOVA-tester som visade signifikanta skillnader i PC1 beroende på:
Erfarenhetsnivå (F = 1581.370, p < 0.001)
Anställningstyp (F = 4560.401, p < 0.001)
Företagsstorlek (F = 27 269.167, p < 0.001)
Korrelationer mellan PC1 och numeriska variabler:
PC1 vs. lön (salary_in_usd): r = 0.323
PC1 vs. distansarbete (remote_ratio): r = -0.156
Dessa resultat visar att även med en begränsad andel förklarad varians fångar PC1 upp meningsfulla mönster relaterade till både grupper och numeriska faktorer.

🤖 Prediktiv analys med PCA och linjär regression
I ett separat moment använde vi PCA som förbehandling för prediktiv modellering. Här var målet att använda fler komponenter (5 st) för att bevara mer information inför modellträning. Vi använde:

PCA med 5 komponenter för att representera datan med högre informationsinnehåll.
Linjär regression för att förutsäga salary_in_usd baserat på de nya komponenterna.
Cross-validation (cv=5) för att utvärdera modellens generaliseringsförmåga.
MSE (Mean Squared Error) som prestandamått.
Biplot och variansförklaring för att tolka komponenterna.
Detta tillvägagångssätt kompletterade den explorativa analysen och visade att PCA-komponenter även kan användas för att bygga enkla men informativa prediktiva modeller.
