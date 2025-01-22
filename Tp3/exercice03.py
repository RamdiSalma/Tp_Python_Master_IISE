#Exercice 3 : Polymorphisme

from math import pi

class Forme:
    def calculer_surface():
        print("Calcul")
        

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
        

    
class Rectangle(Forme):
    def __init__(self, largeur, longeur):
        self.largeur = largeur
        self.longeur = longeur
        
    def calculer_surface(self):
        return self.largeur * self.longeur

class Triangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur
        
    def calculer_surface(self):
        return (self.base * self.hauteur)/ 2
    
def afficher_surface(formes):
    for forme in formes:
        if isinstance(forme, Forme):
            surface = forme.calculer_surface()
            print(f"Surface de la forme: {surface:.2f}")
        else:
            print("L'objet n'est pas une forme valide.")

# Exemple d'utilisation
formes = [
    Cercle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

afficher_surface(formes)