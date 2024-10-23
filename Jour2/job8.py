# Initialisation du numéro du tour
tour_precedent = 0

# Boucle de 12 tours
for i in range(12):
    tour_actuel = tour_precedent + 2
    print(f"Tour {i + 1}: {tour_actuel}")
    tour_precedent = tour_actuel