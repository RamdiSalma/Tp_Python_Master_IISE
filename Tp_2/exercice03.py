# Class CompteBancaire

class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    
    def deposer(self, montant):
        self.solde += montant
        
    def retirer(self, montant):
        if(montant >= self.solde):
            print("vérifiez que le solde est suffisant")
            
        else:
            self.solde -= montant
                
    def afficher_solde(self):
        print("Solde ")
        print(f"Votre solde est : {self.solde}")
        

compte = CompteBancaire("Ferdaous", 4000000)
compte.afficher_solde()
compte.deposer(500000)
compte.afficher_solde()
compte.retirer(300000)
compte.afficher_solde()