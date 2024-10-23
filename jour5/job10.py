# Définition de la liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation du produit
produit = 1
trouve = False  # Pour vérifier s'il y a des valeurs dans l'intervalle

# Parcours de la liste pour multiplier les valeurs dans l'intervalle [25, 90]
for nombre in L:
    if 25 <= nombre <= 90:
        produit *= nombre
        trouve = True

# Affichage du résultat
if trouve:
    print("Produit des valeurs dans l'intervalle [25, 90] :", produit)
else:
    print("Aucune valeur dans l'intervalle [25, 90]")