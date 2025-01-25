import pandas as pd

# Charger le fichier CSV
file_path = "employees.csv"
data = pd.read_csv(file_path)

# Afficher les cinq premières lignes du jeu de données
print("Les cinq premières lignes du fichier :")
print(data.head())

# Calculer et afficher la moyenne d'un champ numérique (par exemple, l'âge des employés)
average_age = data["Age"].mean()
print(f"\nL'âge moyen des employés est : {average_age:.2f} ans")

# Vous pouvez également afficher une statistique supplémentaire, comme la moyenne des salaires
average_salary = data["Salary"].mean()
print(f"Le salaire moyen des employés est : {average_salary:.2f} USD")
