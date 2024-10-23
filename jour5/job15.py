# Liste d'origine
numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Fonction pour arrondir un nombre
def round_number(num):
    integer_part = int(num)  # Partie entière
    decimal_part = num - integer_part  # Partie décimale
    if decimal_part >= 0.5:
        return integer_part + 1  # Arrondir au supérieur
    else:
        return integer_part  # Garder la partie entière

# Arrondir les nombres dans la liste
rounded_numbers = []
for number in numbers:
    rounded_numbers += [round_number(number)]

# Tri de la liste arrondie (tri par insertion)
for i in range(1, 100):  # On suppose que la liste a au maximum 100 éléments
    for j in range(i, 0, -1):
        if j > 0 and rounded_numbers[j] < rounded_numbers[j - 1]:
            # Échange des éléments
            rounded_numbers[j], rounded_numbers[j - 1] = rounded_numbers[j - 1], rounded_numbers[j]

# Affichage de la liste triée
print("Liste arrondie et triée :", rounded_numbers)