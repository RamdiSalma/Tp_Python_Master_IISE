#Exercice 10 : Application Finale

import csv
import os

# Nom du fichier CSV
fichier_contacts = "contacts.csv"

# Créer le fichier CSV avec des en-têtes s'il n'existe pas
if not os.path.exists(fichier_contacts):
    with open(fichier_contacts, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Nom", "Téléphone", "Email"])  # En-têtes du fichier

# Boucle du menu principal
while True:
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    print("5. Quitter")
    
    choix = input("Choisissez une option : ")
    
    # Ajouter un contact
    if choix == "1":
        nom = input("Nom du contact : ")
        telephone = input("Téléphone : ")
        email = input("Email : ")

        with open(fichier_contacts, "a", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerow([nom, telephone, email])

        print(f"Contact '{nom}' ajouté avec succès.\n")

    # Afficher tous les contacts
    elif choix == "2":
        with open(fichier_contacts, "r", encoding="utf-8") as fichier:
            reader = csv.reader(fichier)
            for ligne in reader:
                print(", ".join(ligne))
        print()

    # Rechercher un contact
    elif choix == "3":
        recherche = input("Nom du contact à rechercher : ")
        trouve = False

        with open(fichier_contacts, "r", encoding="utf-8") as fichier:
            reader = csv.reader(fichier)
            for ligne in reader:
                if recherche.lower() in ligne[0].lower():
                    print(", ".join(ligne))
                    trouve = True
        
        if not trouve:
            print(f"Aucun contact trouvé pour '{recherche}'.\n")

    # Supprimer un contact
    elif choix == "4":
        nom_supp = input("Nom du contact à supprimer : ")
        contacts = []

        with open(fichier_contacts, "r", encoding="utf-8") as fichier:
            reader = csv.reader(fichier)
            for ligne in reader:
                if ligne[0].lower() != nom_supp.lower():
                    contacts.append(ligne)
        
        with open(fichier_contacts, "w", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerows(contacts)
        
        print(f"Contact '{nom_supp}' supprimé (si existant).\n")

    # Quitter l'application
    elif choix == "5":
        print("Au revoir !")
        break

    else:
        print("Option invalide, veuillez réessayer.\n")
