# Demander à l'utilisateur de saisir un entier supérieur à zéro
N = int(input("Entrez un entier supérieur à zéro : "))

if N > 0:
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
else:
    print("Veuillez entrer un nombre supérieur à zéro.")