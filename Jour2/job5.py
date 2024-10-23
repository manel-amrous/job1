# Demander à l'utilisateur de saisir un entier supérieur à zéro
N = int(input("Entrez un entier supérieur à zéro : "))

if N > 0:
    i = 1
    while i <= N:
        print(f"\nTable de multiplication de {i}:")
        
        j = 1
        while j <= 10:
            print(f"{i} x {j} = {i * j}")
            j += 1
        
        i += 1
else:
    print("Veuillez entrer un nombre supérieur à zéro.")