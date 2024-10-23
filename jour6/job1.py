def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("La largeur et la hauteur doivent être supérieures ou égales à 2.")
        return

    # Dessiner le haut du rectangle
    print('-' * width)

    # Dessiner les côtés du rectangle
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Dessiner le bas du rectangle
    print('-' * width)

# Exemple d'utilisation
draw_rectangle(10, 3)