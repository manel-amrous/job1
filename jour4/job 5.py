def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2 if num2 != 0 else "Erreur : Division par zéro"
    elif operator == "%":
        return num1 % num2
    else:
        return "Erreur : Opérateur non valide"

# Exemples d'appels de la fonction
print(calcule(10, "+", 5))   # 15
print(calcule(10, "-", 5))   # 5
print(calcule(10, "*", 5))   # 50
print(calcule(10, "/", 5))   # 2.0
print(calcule(10, "%", 3))   # 1
print(calcule(10, "/", 0))   # Erreur : Division par zéro
print(calcule(10, "^", 5))   # Erreur : Opérateur non valide
