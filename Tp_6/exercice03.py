#Exercice 3 :  Lecture de Fichier
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
    finally:
        if file:
            file.close()
            print("Le fichier est ferme")


try:
    contenu = read_file("exemples.txt")
    if contenu:
        print("Contenu du fichier :")
        print(contenu)
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

