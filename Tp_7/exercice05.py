import pandas as pd

# Charger le fichier CSV
file_path = "employees.csv"
donne = pd.read_csv(file_path)

# Afficher les cinq premières lignes du jeu de données
print("Les cinq premières lignes du fichier :")
print(donne.head())

# Calculer et afficher la moyenne d'un champ numérique
average_age = donne["Age"].mean()
print(f"\nL'âge moyen des employés est : {average_age:.2f} ans")

