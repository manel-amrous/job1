def my_long_word(length, text):
    # Initialisation de la liste pour stocker les mots longs
    long_words = []
    
    # Séparation des mots dans la chaîne de caractères
    current_word = ""
    for char in text:
        if char == " ":
            # Si le mot est plus long que le chiffre, on l'ajoute à la liste
            if current_word != "" and count_characters(current_word) > length:
                long_words += [current_word]
            current_word = ""  # Réinitialisation du mot
        else:
            current_word += char  # Construction du mot
    
    # Vérifier le dernier mot après la boucle
    if current_word != "" and count_characters(current_word) > length:
        long_words += [current_word]
     # Conversion de la liste de mots en une chaîne
    result = ""
    for word in long_words:
        result += word + " "
    
    return result.strip()  # Enlever l'espace final

def count_characters(word):
    # Compter le nombre de caractères dans un mot
    count = 0
    for char in word:
        count += 1
    return count

# Exemple d'utilisation
text = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
output = my_long_word(3, text)
print(output)
# Liste d'origine
numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Fonction pour arrondir un nombre
def round_number(num):
    integer_part = int(num)
    decimal_part = num - integer_part
    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part

# Arrondir les nombres dans la liste
rounded_numbers = []
for number in numbers:
    rounded_numbers += [round_number(number)]

# Tri de la liste arrondie (tri par insertion)
for i in range(1, 100):  # On suppose que la liste a au maximum 100 éléments
    for j in range(i, 0, -1):
        if j > 0 and rounded_numbers[j] < rounded_numbers[j - 1]:
            # Échange des éléments
            rounded_numbers[j], rounded_numbers[j - 1] = rounded_numbers[j - 1], rounded_numbers[j]

# Affichage de la liste triée
print("Liste arrondie et triée :", rounded_numbers)