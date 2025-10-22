import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib 
print("--- Début de l'entraînement du modèle ---")


try:
    data = pd.read_csv("salaires_maroc.csv", encoding='latin1', sep=';')
    print("Fichier CSV chargé avec succès.")
except FileNotFoundError:
    print("ERREUR: Fichier 'salaires_maroc.csv' non trouvé.")
    exit()


try:
    data_processed = pd.get_dummies(data, columns=['Poste', 'Ville', 'Etudes'], drop_first=True)
    print("Données transformées (get_dummies).")
except Exception as e:
    print(f"ERREUR lors de la transformation des données : {e}")
    exit()


Y = data_processed['Salaire_DHS']


X = data_processed.drop('Salaire_DHS', axis=1)

print(f"Objectif (Y) défini : Salaire_DHS")
print(f"Caractéristiques (X) définies. Nombre de colonnes : {len(X.columns)}")


model = LinearRegression()


model.fit(X, Y)
print("Modèle entraîné avec succès.")


joblib.dump(model, 'predi_salaire_model.pkl')


joblib.dump(X.columns, 'salaire_model_columns.pkl')

print("--- Modèle et colonnes sauvegardés ('predi_salaire_model.pkl' et 'salaire_model_columns.pkl') ---")
print("--- Entraînement terminé ---")