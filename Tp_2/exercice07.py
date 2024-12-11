# Classe : Livre
class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
    
    def __str__(self):
        return f"'{self.titre}' par {self.auteur}, publié en {self.annee_publication}"

class Bibliotheque:
    def __init__(self):
        self.livres = []  
    
    def ajouter_livre(self, livre):
        self.livres.append(livre)
    
    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque :")
            for livre in self.livres:
                print(f"{livre}")


livre1 = Livre("Candide ou l'optimisme", "Antoine de Saint-Exupéry", 1759)
livre2 = Livre("Les Misérables", "Victor Hugo", 1862)
    

biblio = Bibliotheque()
  
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
      
biblio.afficher_livres()
