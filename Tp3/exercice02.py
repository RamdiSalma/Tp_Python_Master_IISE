#Class Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    
    def get_nom(self):
        return self.__nom

    
    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom 
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
        
    def get_age(self):
        return self.__age 
    
    def set_age(self, age):
        self.__age = age
        

    def afficher_infos(self):
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, Âge: {self.__age}")


personne = Personne("RAMDI", "Salma",20)
personne.afficher_infos()
personne.set_age(31)
print("Nouvel âge:", personne.get_age())
