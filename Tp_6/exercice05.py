#Exercice 5 : Multi-Exceptions
def process_input(user_input):
    try:
       value = int(user_input)
       result = 10 / value 
       print(f"Résultat : {result}")
    except ValueError:
       print(f"Erreur : '{user_input}' n'est pas un entier valide.")
    except ZeroDivisionError:
       print("Erreur : Division par zéro interdite.")

input = "210as"
print(f"Entrée : {input}")
process_input(input)