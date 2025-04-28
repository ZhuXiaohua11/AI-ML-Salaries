import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Ladda och rensa data
df = pd.read_csv('rensade_salaries.csv')
df_clean = df[df['salary_in_usd'] <= 400000]

# 2. Koda kategoriska variabler
df_encoded = df_clean.copy()
df_encoded['experience_level'] = df_encoded['experience_level'].map({'EN':0, 'MI':1, 'SE':2, 'EX':3})
df_encoded['employment_type'] = df_encoded['employment_type'].map({'PT':0, 'FT':1, 'CT':2, 'FL':3})
df_encoded['company_size'] = df_encoded['company_size'].map({'S':0, 'M':1, 'L':2})

# 3. Välj de variabler du ska använda
features = ['experience_level', 'employment_type', 'company_size', 'remote_ratio', 'salary_in_usd']
X = df_encoded[features]

# 4. Skala datan
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. PCA
pca = PCA(n_components=2)  # Välj 2 komponenter för 2D
X_pca = pca.fit_transform(X_scaled)

# 6. Skapa en ny dataframe för PCA-resultat
pca_df = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
pca_df['experience_level'] = df_encoded['experience_level']  # Lägg till experience_level för färg

# 7. Rita scatterplot
plt.figure(figsize=(10,7))
sns.scatterplot(
    x='PC1', y='PC2',
    hue='experience_level',
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

# 8. Visa hur mycket varians varje komponent förklarar
print("Explained variance ratio per component:", pca.explained_variance_ratio_)


# 9. PCA Loadings (hur mycket varje variabel påverkar varje komponent)

# Hämta laddningar (loadings) från PCA:n
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# Sätt ihop till en dataframe för lättare läsning
loadings_df = pd.DataFrame(loadings,
                           columns=['PC1', 'PC2'],
                           index=features)

print("PCA Loadings:")
print(loadings_df)



def biplot(score, coeff, labels=None):
    xs = score[:,0]
    ys = score[:,1]
    n = coeff.shape[0]
    plt.figure(figsize=(10,7))
    plt.scatter(xs, ys, alpha=0.5)
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0]*5, coeff[i,1]*5, color='r', alpha=0.8)
        if labels is None:
            plt.text(coeff[i,0]*5.2, coeff[i,1]*5.2, "Var"+str(i+1), color='g', ha='center', va='center')
        else:
            plt.text(coeff[i,0]*5.2, coeff[i,1]*5.2, labels[i], color='g', ha='center', va='center')
    plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% varians)")
    plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% varians)")
    plt.grid()
    plt.title('PCA Biplot')
    plt.show()

# Kör biplot
biplot(X_pca, pca.components_.T, labels=features)

