#Exercice 2 :  Vérification de Type
def convert_to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Impossible de convertir {value} en entier.")


try:
    result = convert_to_int(None)
    print(f"Résultat: {result}")
except ValueError as e:
    print(e)
