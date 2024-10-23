def draw_triangle(height):
    for i in range(height):
        # Afficher les espaces à gauche
        print(' ' * (height - i - 1), end='')
        # Afficher les côtés du triangle
        if i == height - 1:
            print('_' * (2 * i + 1))
        else:
            print('/', end='')
            print(' ' * (2 * i - 1), end='')
            print('\\')

# Exemple d'utilisation
draw_triangle(5)