#Exercice 4 : Traitement de Fichiers CSV

import csv

# Ouvrir le fichier en mode lecture
with open("contacts.csv", mode = "r", newline= '') as fichier:
    lecteur = csv.reader(fichier)
    en_tete = next(lecteur)  # Lit la première ligne (en-tête)
    
    # Parcourt chaque ligne du fichier CSV
    for ligne in lecteur:
        nom, age, ville = ligne  
        print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")