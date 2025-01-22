class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes_supervises = []
    
    def ajouter_employe(self, employe):
        if isinstance(employe, Employe):
            self.employes_supervises.append(employe)
        else:
            print("L'objet ajouté n'est pas un employé.")
    
    def afficher_employes_supervises(self):
        if not self.employes_supervises:
            return "Aucun employé sous supervision."
        return "\n".join([employe.afficher_informations() for employe in self.employes_supervises])


if __name__ == "__main__":
    manager = Manager("Dupont", "Jean", 70000)
    employe1 = Employe("Martin", "Paul", 40000)
    employe2 = Employe("Durand", "Sophie", 45000)

    manager.ajouter_employe(employe1)
    manager.ajouter_employe(employe2)

    print(manager.afficher_employes_supervises())
