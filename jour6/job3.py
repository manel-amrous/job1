def draw_carpet(n):
    # Créer le tapis
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                print('\\', end='')  # Diagonale
            else:
                print('.', end='')  # Autres cases
        print()  # Nouvelle ligne après chaque ligne du tapis

# Exemple d'utilisation
draw_carpet(10)