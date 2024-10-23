def distance_parcourue_phare(marches, hauteur):
    # Calculer la distance d'un aller-retour
    distance_un_trajet = marches * hauteur / 100  # convertir cm en m
    distance_allers_retours = distance_un_trajet * 2  # aller + retour

    # Calculer le nombre de trajets par semaine
    trajets_par_jour = 5  # 5 fois par jour
    jours_par_semaine = 7
    distance_semaine = distance_allers_retours * trajets_par_jour * jours_par_semaine

    return distance_semaine

# Exemple d'utilisation
marches = 100  # Nombre de marches
hauteur = 20   # Hauteur de chaque marche en cm
distance = distance_parcourue_phare(marches, hauteur)

print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance:.2f} m par semaine.")