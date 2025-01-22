#Exercice 5 : Écriture et Lecture de Fichiers JSON

import json

#Créer le dictionnaire des étudiants
etudiants = [
    {"nom": "Salma", "age": 20, "note": 18},
    {"nom": "Yahya", "age": 22, "note": 16},
    {"nom": "Ferdaous", "age": 17, "note": 19}
]

# Ouvrir le fichier en mode ecriture
with open("etudiants.json", "w") as fichier:
    json.dump(etudiants, fichier, indent = 4)
    
    
# Ouvrir le fichier en mode lecture
with open("etudiants.json", "r") as fichier:
    etudiants = json.load(fichier)
    print(etudiants)