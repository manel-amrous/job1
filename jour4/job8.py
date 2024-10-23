def afficher_produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Aucun produit disponible pour ces critères.")

# Appels de la fonction avec différents paramètres
afficher_produits("fruits", "hiver")  # orange, mandarine et kiwi
afficher_produits("fruits", "été")     # poire, fraise, cassis
afficher_produits("légume", "hiver")    # carotte, topinambour, endive
afficher_produits("légume", "été")      # artichaut, aubergine, navet
afficher_produits("fruits", "printemps") # Aucun produit disponible pour ces critères.