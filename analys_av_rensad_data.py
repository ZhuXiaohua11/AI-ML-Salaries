import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Ladda data
df = pd.read_csv('rensade_salaries.csv')

# Sätt en övre gräns (t.ex. 400 000 USD)
df_clean = df[df['salary_in_usd'] <= 400000]

# Kolla ny boxplot efter rensning
sns.boxplot(x=df_clean['salary_in_usd'])
plt.title('Boxplot över löner i USD (rengjord)')
plt.show()


# Beskrivande statistik för numeriska kolumner
print(df_clean.describe())


# Kopiera df_clean och koda kategoriska variabler
df_encoded = df_clean.copy()


# Visualisera löner för varje kategori
plt.figure(figsize=(12, 8))
sns.boxplot(x='experience_level', y='salary_in_usd', data=df_encoded)
plt.title('Salary by Experience Level')
plt.show()

sns.boxplot(x='remote_ratio', y='salary_in_usd', data=df_encoded)
plt.title('Salary by Remote Work Ratio')
plt.show()

sns.boxplot(x='employment_type', y='salary_in_usd', data=df_encoded)
plt.title('Salary by Employment Type')
plt.show()

sns.boxplot(x='company_size', y='salary_in_usd', data=df_encoded)
plt.title('Salary by Company Size')
plt.show()






# Grunddata
mean_salary = df_clean['salary_in_usd'].mean()
median_salary = df_clean['salary_in_usd'].median()
q1 = df_clean['salary_in_usd'].quantile(0.25)
q3 = df_clean['salary_in_usd'].quantile(0.75)

# Rita histogram
plt.figure(figsize=(10,6))
plt.hist(df_clean['salary_in_usd'], bins=30, color='skyblue', edgecolor='black')
plt.axvline(mean_salary, color='red', linestyle='--', label=f'Mean: {mean_salary:.0f} USD')
plt.axvline(median_salary, color='green', linestyle='--', label=f'Median: {median_salary:.0f} USD')
plt.axvline(q1, color='purple', linestyle=':', label=f'25%: {q1:.0f} USD')
plt.axvline(q3, color='orange', linestyle=':', label=f'75%: {q3:.0f} USD')

plt.title('Fördelning av löner med statistiska mått')
plt.xlabel('Lön i USD')
plt.ylabel('Antal personer')
plt.legend()
plt.grid(True)
plt.show()




# Rita boxplot
plt.figure(figsize=(8,4))
sns.boxplot(x=df_clean['salary_in_usd'], color='lightblue')

plt.text(mean_salary, 0.05, 'Mean', horizontalalignment='center', color='red')
plt.text(median_salary, -0.1, 'Median', horizontalalignment='center', color='green')

plt.axvline(mean_salary, color='red', linestyle='--')
plt.axvline(median_salary, color='green', linestyle='--')

plt.title('Boxplot med Mean och Median markerade')
plt.xlabel('Lön i USD')
plt.yticks([])
plt.show()





df_encoded['experience_level'] = df_encoded['experience_level'].map({'EN':0, 'MI':1, 'SE':2, 'EX':3})
df_encoded['employment_type'] = df_encoded['employment_type'].map({'PT':0, 'FT':1, 'CT':2, 'FL':3})
df_encoded['company_size'] = df_encoded['company_size'].map({'S':0, 'M':1, 'L':2})

# Välj numeriska kolumner från df_encoded (inklusive kodade variabler)
numerical_features = df_encoded.select_dtypes(include=['int64', 'float64'])

# Skapa korrelationsmatris
correlation_matrix = numerical_features.corr()

# Rita heatmap
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Korrelationsmatris för numeriska variabler')
plt.show()
