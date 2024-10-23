# Demander à l'utilisateur de saisir un entier
N = int(input("Entrez un entier : "))

# Initialiser un compteur
compteur = 1

# Boucle pour afficher les premiers résultats de la multiplication de N par 7
while compteur <= 10:
    resultat = N * 7 * compteur
    print(f"{N} * 7 * {compteur} = {resultat}")
    compteur += 1