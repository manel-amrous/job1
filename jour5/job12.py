def trier_liste(liste):
    # Implémentation d'un tri par insertion
    for i in range(1, 100):  # On suppose que la liste a au maximum 100 éléments
        for j in range(i, 0, -1):
            if j > 0 and liste[j] < liste[j - 1]:
                # Échange des éléments
                liste[j], liste[j - 1] = liste[j - 1], liste[j]

# Exemple de liste
L = [42, 11, 7, 39, 2]

# Appel de la fonction de tri
trier_liste(L)

# Affichage de la liste triée
print("Liste triée :", L)