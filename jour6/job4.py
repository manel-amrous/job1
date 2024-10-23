
def caesar_cipher(message, shift):
    result = []

    for char in message:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            # Gérer le décalage pour les lettres minuscules
            base = ord('a') if char.islower() else ord('A')
            # Appliquer le décalage et gérer le dépassement
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)  # Garder les caractères non alphabétiques tels quels

    return ''.join(result)

# Exemple d'utilisation
message = "Bonjour, monde!"
shift = 3
print(caesar_cipher(message, shift))  # Output : "Erqmxur, prqgh!"