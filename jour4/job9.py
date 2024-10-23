def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

# Demande de saisie des notes à l'utilisateur
notes = []
for i in range(1, 4):
    while True:
        try:
            note = float(input(f"Entrez la {i}ère note (entre 0 et 20) : "))
            if 0 <= note <= 20:
                notes.append(note)
                break
            else:
                print("Veuillez entrer une note valide entre 0 et 20.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Calcul de la moyenne
moyenne_etudiant = moyenne(*notes)

# Affichage du message en fonction de la moyenne
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant < 15:
    print("Bon élève")
elif 8 <= moyenne_etudiant < 11:
    print("Élève moyen")
elif 0 <= moyenne_etudiant < 8:
    print("Élève devant faire des efforts")
else:
    print("Note invalide")