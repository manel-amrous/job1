# Chaîne de caractères répétée 10 fois
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialiser des variables
index = 0
n = 1

# Boucle pour créer la pyramide
while index + n <= len(chaine):
    # Afficher la sous-chaîne pour la ligne actuelle
    print(chaine[index:index + n])
    # Mettre à jour l'index et le nombre de caractères pour la prochaine ligne
    index += n
    n += 1
