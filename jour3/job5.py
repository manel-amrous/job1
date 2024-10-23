def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Afficher les nombres premiers jusqu'à 1000
for nombre in range(1, 1001):
    if est_premier(nombre):
        print(nombre)