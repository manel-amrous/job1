# Définition de la liste
L = [8, 24, 48, 2, 16]

# Initialisation du compteur
compteur = 0

# Parcours de la liste pour compter les multiples de 3
for nombre in L:
    if nombre % 3 == 0:
        compteur += 1

# Affichage du résultat
print("Nombre de multiples de 3 dans la liste :", compteur)