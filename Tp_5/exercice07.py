#Exercice 7 : Copie et Déplacement de Fichiers

import shutil
import os

#Copier le fichier journal.txt
source = "journal.txt"
destination_copie = "journal_copie.txt"

shutil.copy(source, destination_copie)
print("Fichier copié sous le nom 'journal_copie.txt'.")

#Créer un dossier archives s'il n'existe pas
dossier_archives = "archives"
if not os.path.exists(dossier_archives):
    os.mkdir(dossier_archives)
    print("Dossier 'archives' créé.")

#Déplacer le fichier copié dans le dossier archives
destination_finale = os.path.join(dossier_archives, "journal_copie.txt")
shutil.move(destination_copie, destination_finale)
print("Fichier déplacé dans le dossier 'archives'.")
