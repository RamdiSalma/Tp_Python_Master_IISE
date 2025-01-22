#Exercice 9 : Statistiques de Fichier

# Ouvrir le fichier en mode lecture
with open("journal.txt", "r") as fichier:
    contenu = fichier.read()  # Lire tout le contenu du fichier

# Calcul des statistiques
nombre_lignes = contenu.count("\n") + 1  # Compte les sauts de ligne (+1 pour la dernière ligne sans \n)
nombre_mots = len(contenu.split())  # Découpe le texte en mots
nombre_caracteres = len(contenu)  # Compte tous les caractères, y compris les espaces et sauts de ligne

# Affichage des résultats
print("Statistiques du fichier :")
print(f"Nombre total de lignes     : {nombre_lignes}")
print(f"Nombre total de mots       : {nombre_mots}")
print(f"Nombre total de caractères : {nombre_caracteres}")
