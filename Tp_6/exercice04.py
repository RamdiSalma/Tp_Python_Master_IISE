#Exercice 4 : Exceptions Personnalisées
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("L'age ne peut pas etre negatif ")
    print(f"L'âge a été défini à {age} ans.")


try:
    set_age(25)  
    set_age(-5) 
except NegativeAgeError as e:
    print("Erreur :", e)
