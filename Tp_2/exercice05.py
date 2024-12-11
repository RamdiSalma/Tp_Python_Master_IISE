#Class : Animal
class Animal:
    def faire_du_bruit(self):
        print("Cet animal fait du bruit.")

#Sous-classe : Chien
class Chien(Animal):
    def faire_du_bruit(self):
        return "Aboie !"

# Sous-classe : Chat
class Chat(Animal):
    def faire_du_bruit(self):
        return "Miole !"


chien = Chien()
chat = Chat()

print("Le chien :", chien.faire_du_bruit())
print("Le chat  :", chat.faire_du_bruit())
