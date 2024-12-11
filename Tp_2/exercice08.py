#Class : Personne
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []  
    
    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.prenom} {self.nom}, j'ai {self.age} ans."
    
    def ajouter_ami(self, ami):
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami.prenom} {ami.nom} a été ajouté à la liste d'amis de {self.prenom}.")
        else:
            print(f"{ami.prenom} {ami.nom} est déjà dans la liste d'amis de {self.prenom}.")
    
    def afficher_amis(self):
        if not self.amis:
            print(f"{self.prenom} n'a pas encore d'amis.")
        else:
            print(f"Liste des amis de {self.prenom} :")
            for ami in self.amis:
                print(f"{ami.prenom} {ami.nom}")


personne1 = Personne("Dupont", "Jean", 30)
personne2 = Personne("Martin", "Claire", 25)
personne3 = Personne("Durand", "Sophie", 28)
    
print(personne1.se_presenter())
print(personne2.se_presenter())
   
personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)
personne1.ajouter_ami(personne2)  # Tentative de double ajout
    
personne1.afficher_amis()
personne2.afficher_amis()
