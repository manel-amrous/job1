# Liste d'origine
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Liste pour stocker les éléments uniques
unique_list = []

# Parcours de la liste d'origine
for element in L:
    # Vérifie si l'élément n'est pas déjà dans la liste unique
    found = 0  # Compteur pour vérifier l'existence
    for unique in unique_list:
        if element == unique:
            found = 1
            break
    if found == 0:  # Si l'élément n'est pas trouvé, on l'ajoute
        unique_list += [element]

# Affichage de la liste sans doublons
print("Liste sans doublons :", unique_list)