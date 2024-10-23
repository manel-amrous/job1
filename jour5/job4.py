def ajouter_fruit():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, "mangue")  # Ajoute "mangue" à l'index 2
    return fruits

# Appel de la fonction et affichage du résultat
resultat = ajouter_fruit()
print(resultat)