from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Ladda och rensa data
df = pd.read_csv('rensade_salaries.csv')
df_clean = df[df['salary_in_usd'] <= 400000]

# Koda kategoriska variabler
df_encoded = df_clean.copy()
df_encoded['experience_level'] = df_encoded['experience_level'].map({'EN': 0, 'MI': 1, 'SE': 2, 'EX': 3})
df_encoded['employment_type'] = df_encoded['employment_type'].map({'PT': 0, 'FT': 1, 'CT': 2, 'FL': 3})
df_encoded['company_size'] = df_encoded['company_size'].map({'S': 0, 'M': 1, 'L': 2})

# Välj de variabler du ska använda
features = ['experience_level', 'employment_type', 'company_size', 'remote_ratio', 'salary_in_usd']
X = df_encoded[features]

# Skala datan
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Applicera PCA
pca = PCA(n_components=5)  # Välj antal komponenter
X_pca = pca.fit_transform(X_scaled)

# Definiera en modell (exempelvis Linear Regression)
model = LinearRegression()

# Utför cross-validation och få resultat för varje uppdelning
cv_scores = cross_val_score(model, X_pca, df_encoded['salary_in_usd'], cv=5, scoring='neg_mean_squared_error')

# Visa resultatet
print(f"Cross-validation MSE: {-cv_scores.mean()}")  # Negativ MSE för att visa det som ett positivt värde
print(f"Standard deviation of MSE: {cv_scores.std()}")  # Standardavvikelse för att se variationen
