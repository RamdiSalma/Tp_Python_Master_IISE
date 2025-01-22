#Exercice 1 : Lecture de fichiers


# Ouvrir le fichier en mode lecture
with open("exemple.txt", "r") as fichier:
    # Lire toutes les lignes
    lignes = fichier.readlines()
    
    # Parcourir chaque ligne avec son index
    for i, ligne in enumerate(lignes, start=1):
        print(f"{i} - {ligne.strip()}")
