import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
import numpy as np

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

pca = PCA(n_components=4)  # Välj 4 komponenter istället för 5
X_pca = pca.fit_transform(X_scaled)


pca_df = pd.DataFrame(data=X_pca, columns=[f'PC{i+1}' for i in range(4)])  # Skapa rätt antal kolumner (4)
pca_df['experience_level'] = df_encoded['experience_level']  # Lägg till experience_level för färg


loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# Sätt ihop till en dataframe för lättare läsning
loadings_df = pd.DataFrame(loadings,
                           columns=[f'PC{i+1}' for i in range(4)],  # Skapa rätt antal kolumner (4)
                           index=features)

# Rita en Scree plot för de första 4 komponenterna
plt.figure(figsize=(10, 6))
plt.plot(range(1, 5), pca.explained_variance_ratio_[:4], marker='o')  # Visa endast de första 4 komponenterna
plt.xlabel('Antal komponenter')
plt.ylabel('Förklarad varians')
plt.title('Scree Plot')
plt.show()
