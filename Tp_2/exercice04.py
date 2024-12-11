# Class : Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom 
        self.age = age
        
    def se_presenter(self, nom, prenom, age):
        print(f"Je m'appelle {self.nom} {self.prenom}, age de {self.age}")
        
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)  
        self.matricule = matricule
    
    def etudier(self):
        return f"{self.prenom} {self.nom}, matricule {self.matricule}, est un etudiant."


personne = Personne("Salma", "RAMDI", 20)
print(personne.se_presenter())

    
etudiant = Etudiant("Yasmine", "Idrissi", 22, "E2098")
print(etudiant.se_presenter())
print(etudiant.etudier())