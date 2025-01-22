#Exercice 1 : Division par zero
def safe_division(a, b):
    if (b == 0):
        raise ZeroDivisionError("Division par zéro n'est pas autorisée.")
    return a / b

try:
    
    result = safe_division(10, 0)  # Cela lèvera une exception.
    print("Résultat :", result)
except ZeroDivisionError as e:
    print("Erreur :", e)
