#Exercice 6 : Renommer et Supprimer des Fichiers

import os

#Renommer le fichier "phrases.txt" en "anciennes_phrases.txt"
ancien_nom = "phrases.txt"
nouveau_nom = "anciennes_phrases.txt"

try:
    os.rename(ancien_nom, nouveau_nom)
    print(f"Fichier renomme en {nouveau_nom}.")
except FileNotFoundError:
    print("Le fichier a renommer n'a pas ete trouve. ")
except IOError:
    print("Erreur lors du renommage du fichier. ")
    
#Supression du fichier
nom_fichier = "anciennes_phrases.txt"

try:
    os.remove(nom_fichier)
    print(f"Fichier {nom_fichier} supprime. ")
except FileNotFoundError:
    print("Le fichier a suprimmer n'a pas ete trouve. ")
except IOError:
    print("Erreur lors de la supression du fichier. ")
    