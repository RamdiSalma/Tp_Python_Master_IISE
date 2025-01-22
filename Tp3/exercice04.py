# Exercice 4 : Gestion de Produits avec Encapsulation

class Produits:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    
    def get_nom(self):
        return self.__nom

    
    def get_prix(self):
        return self.__prix

  
    def set_nom(self, nom):
        self.__nom = nom

    
    def set_prix(self, prix):
        if prix >= 0:
            self.__prix = prix
        else:
            print("Le prix ne peut pas être négatif.")

   
    def calculerRemise(self, remise, seuil):
        if self.__prix > seuil:
            prix_remise = self.__prix * (1 - remise / 100)
            return prix_remise
        return self.__prix

# Exemple d'utilisation
if __name__ == "__main__":
    produit1 = Produits("Ordinateur", 10000)
    print(f"Prix avant remise : {produit1.get_prix()} DH")
    prixRemise = produit1.calculerRemise(10, 1000)
    print(f"Prix après remise : {prixRemise} DH")

    
    