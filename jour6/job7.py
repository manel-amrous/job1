def my_sort(lst):
    # Initialiser le compteur d'échanges
    total_swaps = 0
    n = len(lst)
    
    # Boucle principale pour passer à travers tous les éléments de la liste
    for i in range(n):
        # Boucle pour comparer les éléments adjacents
        for j in range(0, n - i - 1):
            # Comparer l'élément courant avec l'élément suivant
            if lst[j] > lst[j + 1]:
                # Échanger les éléments si l'élément courant est plus grand
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                total_swaps += 1  # Incrémenter le compteur d'échanges

    # Afficher le nombre total d'échanges
    print(f"Nombre total de coups nécessaires pour trier : {total_swaps}")
    
    # Retourner la liste triée
    return lst

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
liste_triee = my_sort(ma_liste)
print("Liste triée :", liste_triee)