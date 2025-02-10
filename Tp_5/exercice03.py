# Demander à l'utilisateur d'entrer trois phrases
phrases = [input(f"Entrez la phrase {i + 1} : ") for i in range(3)]

# Écrire les phrases dans un fichier
with open("phrases.txt", "w") as fichier:
    for phrase in phrases:
        fichier.write(phrase + "\n")

print("Les phrases ont été enregistrées dans 'phrases.txt'.")

# Demander si l'utilisateur veut ajouter d'autres phrases
while True:
    reponse = input("Voulez-vous ajouter d'autres phrases ? (oui/non) : ").strip().lower()
    if reponse == "non":
        print("Fin de l'opération.")
        break
    elif reponse == "oui":
        phrase = input("Entrez une phrase à ajouter : ")
        with open("phrases.txt", "a") as fichier:
            fichier.write(phrase + "\n")
        print("Phrase ajoutée.")
    else:
        print("Réponse invalide, veuillez répondre par 'oui' ou 'non'.")
