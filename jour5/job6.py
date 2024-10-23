# Création d'une liste quelconque
liste = [5, 10, 15, 20, 25]

# Vérification que la liste n'est pas vide
if len(liste) > 0:
    # Échange des valeurs de la première et de la dernière case
    liste[0], liste[-1] = liste[-1], liste[0]

# Affichage de la liste après l'échange
print("Liste après échange :", liste)