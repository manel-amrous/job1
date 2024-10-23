def time_to_text(minutes):
    """Convertit un nombre entier de minutes en heures et minutes."""
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        reste_minutes = minutes % 60
        print(f"{heures} heures et {reste_minutes} minutes")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Exemple d'utilisation
time_to_text(130)  # 2 heures et 10 minutes
time_to_text(45)   # 0 heures et 45 minutes
time_to_text(-10)  # Veuillez entrer un nombre entier positif.

python
Copier 
def inverse_chaine(chaine):
    """Retourne la chaîne de caractères inversée."""
    return chaine[::-1]

# Exemple d'utilisation
print(inverse_chaine("nikana"))  # anakin
print(inverse_chaine("python"))   # nohtyp