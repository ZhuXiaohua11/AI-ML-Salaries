import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns


# 1. Ladda och rensa data
df = pd.read_csv('rensade_salaries.csv')
df_clean = df[df['salary_in_usd'] <= 400000]

# 2. Koda kategoriska variabler
df_encoded = df_clean.copy()
df_encoded['experience_level'] = df_encoded['experience_level'].map({'EN': 0, 'MI': 1, 'SE': 2, 'EX': 3})
df_encoded['employment_type'] = df_encoded['employment_type'].map({'PT': 0, 'FT': 1, 'CT': 2, 'FL': 3})
df_encoded['company_size'] = df_encoded['company_size'].map({'S': 0, 'M': 1, 'L': 2})

# 3. Välj de variabler du ska använda
features = ['experience_level', 'employment_type', 'company_size', 'remote_ratio', 'salary_in_usd']
X = df_encoded[features]

# 4. Skala datan
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. PCA (ändra till 4 komponenter)
pca = PCA(n_components=5)  # Välj 4 komponenter istället för 5
X_pca = pca.fit_transform(X_scaled)

# 6. Skapa en ny dataframe för PCA-resultat
pca_df = pd.DataFrame(data=X_pca, columns=[f'PC{i+1}' for i in range(5)])  # Skapa rätt antal kolumner (4)
pca_df['experience_level'] = df_encoded['experience_level']  # Lägg till experience_level för färg




# Skapa scatter plot för PC1 och PC2
plt.figure(figsize=(10, 7))
sns.scatterplot(
    x='PC1', y='PC2',
    hue='experience_level',  # Lägg till färg efter experience_level
    palette='viridis',
    data=pca_df,
    alpha=0.7
)
plt.title('PCA - Salaries Dataset (färgat efter experience level)')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% varians)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% varians)')
plt.legend(title='Experience Level')
plt.grid(True)
plt.show()



# Visa loadings för varje komponent
loadings_df = pd.DataFrame(pca.components_.T, columns=[f'PC{i+1}' for i in range(5)], index=features)

# Visa loadings
print("PCA Loadings:")
print(loadings_df)



