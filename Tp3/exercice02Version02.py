#Class Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def prenom(self):
        return self.__prenom
    
    @property
    def age(self):
        return self.__age
        

    def afficher_infos(self):
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, Âge: {self.__age}")

# Exemple d'utilisation
personne = Personne("RAMDI", "Salma",20)
personne.afficher_infos()

