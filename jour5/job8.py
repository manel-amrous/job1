# Définition de la liste
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialisation de la somme
somme_paires = 0

# Parcours de la liste pour additionner les valeurs paires
for nombre in L:
    if nombre % 2 == 0:
        somme_paires += nombre

# Affichage du résultat
print("Somme des valeurs paires dans la liste :", somme_paires)