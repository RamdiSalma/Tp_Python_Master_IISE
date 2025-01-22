#Exercice 8 : Gestion des Erreurs

try:
    # Tentative d'ouverture du fichier inexistant
    with open("inexistant.txt", "r") as fichier:
        contenu = fichier.read()
        print(contenu)

except FileNotFoundError:
    # Gestion de l'erreur si le fichier n'est pas trouvé
    print("Erreur : Le fichier 'inexistant.txt' n'a pas été trouvé.")

except Exception as e:
    # Gestion d'autres erreurs imprévues
    print(f"Une erreur est survenue : {e}")
