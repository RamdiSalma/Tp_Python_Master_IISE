# Class Voiture

class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    def afficher_info(self): 
        print("Les informations de la voiture : ")
        print(f"Marque : {self.marque}  Modele : {self.modele} Année : {self.annee}")
        
    

voiture_01 = Voiture("BMW", "Q8", 2023)
voiture_02 = Voiture("Toyota", "Rav4", 2008)
voiture_03 = Voiture("Ford", "Mustang", 2019)

voiture_01.afficher_info()
voiture_02.afficher_info()
voiture_03.afficher_info()