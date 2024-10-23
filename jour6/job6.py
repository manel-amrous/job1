def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)  # Échoue, pas d'arrondi
        else:
            # Calculer le prochain multiple de 5
            next_multiple_of_5 = ((note // 5) + 1) * 5
            # Vérifier si l'arrondi est nécessaire
            if next_multiple_of_5 - note < 3:
                notes_arrondies.append(next_multiple_of_5)  # Arrondir à la hausse
            else:
                notes_arrondies.append(note)  # Pas d'arrondi

    return notes_arrondies

# Exemple d'utilisation
notes = [82, 67, 38, 84, 29, 55]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)  # Output : [82, 67, 38, 85, 29, 55]