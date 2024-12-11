#Classe : Rectangle
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def calculer_surface(self):
        return self.largeur * self.hauteur
    
    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)


rectangle = Rectangle(largeur=7, hauteur=9)
    
    
surface = rectangle.calculer_surface()
perimetre = rectangle.calculer_perimetre()
    
print(f"Surface du rectangle : {surface}")
print(f"Périmètre du rectangle : {perimetre}")
