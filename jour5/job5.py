# Création de la liste L
L = [10, 20, 30, 40, 50]

# Affichage de la deuxième valeur de la liste
print("Deuxième valeur de la liste :", L[1])

# Fonction pour remplacer L[3] par la somme des cases voisines L[2] et L[4]
def remplacer_case_voisine():
    L[3] = L[2] + L[4]

# Appel de la fonction
remplacer_case_voisine()