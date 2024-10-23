# Demander à l'utilisateur de saisir les longueurs
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Vérifier si les longueurs peuvent former un triangle
if a + b > c and a + c > b and b + c > a:
    print("Les longueurs peuvent former un triangle.")

    # Déterminer le type de triangle
    if a == b == c:
        print("C'est un triangle équilatéral.")
    elif a == b or b == c or a == c:
        # Vérification pour un triangle rectangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("C'est un triangle isocèle et rectangle.")
        else:
            print("C'est un triangle isocèle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("C'est un triangle rectangle.")
    else:
        print("C'est un triangle quelconque.")
else:
    print("Les longueurs ne peuvent pas former un triangle.")