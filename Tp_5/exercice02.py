#Exercice 2 : Écriture dans un Fichier


# Demande à l'utilisateur d'entrer trois phrases
phrases = []
for i in range(1, 4):
    phrase = input(f"Entrez la phrase {i}: ")
    phrases.append(phrase)

# Ouvrir le fichier en mode ecriture
with open("phrases.txt", "w") as fichier:
    for phrase in phrases:
        fichier.write(phrase + "\n")

print("\nLes phrases ont été enregistrées dans 'phrases.txt'.")