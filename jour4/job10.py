def verifier_pair_impair(nombre):
    # Vérification si le nombre est un entier positif
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est pair")
        else:
            print(f"{nombre} est impair")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appels de la fonction avec des valeurs différentes
verifier_pair_impair(4)    # 4 est pair
verifier_pair_impair(7)    # 7 est impair
verifier_pair_impair(-3)   # Veuillez entrer un nombre entier positif.
verifier_pair_impair(0)    # 0 est pair
verifier_pair_impair(15)   # 15 est impair
verifier_pair_impair(10.5)  # Veuillez entrer un nombre entier positif.