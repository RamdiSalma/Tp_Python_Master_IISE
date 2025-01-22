def read_file_and_get_integer():
    while True:
        try:
            # Demander le nom du fichier
            file_name = input("Veuillez entrer le nom du fichier à lire : ")
            
            # Tente d'ouvrir et de lire le fichier
            with open(file_name, 'r') as file:
                content = file.read()
            print("Contenu du fichier lu avec succès :")
            print(content)
            
            break  # Sort de la boucle si la lecture est réussie
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{file_name}' est introuvable. Veuillez réessayer.")
        except PermissionError:
            print(f"Erreur : Vous n'avez pas les permissions nécessaires pour lire le fichier '{file_name}'.")
        except Exception as e:
            print(f"Erreur inattendue lors de la lecture du fichier : {e}")
    
    while True:
        try:
            # Demander un entier à l'utilisateur
            user_input = input("Veuillez entrer un entier : ")
            number = int(user_input)
            print(f"Vous avez entré l'entier valide : {number}")
            return  # Sort de la fonction si l'entier est valide
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

# Exemple d'utilisation
if __name__ == "__main__":
    read_file_and_get_integer()
