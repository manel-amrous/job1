montant_investissement = 10000  # Montant initial de l'investissement
taux_rendement = 5  # Taux de rendement annuel en pourcentage

# calculer le gain annuel
gain_annuel_initial= montant_investissement * (taux_rendement / 100)

# Affichage du gain annuel initial
print(f"Gain annuel initial : {gain_annuel_initial:.2f} €")

# L'investisseur augmente son capital de 5000 euros et le taux augmente de 2%
montant_investissement += 5000
taux_rendement += 2

# Calcul et affichage du nouveau gain
gain_annuel_apres_ajout = montant_investissement * (taux_rendement / 100) 
print(f"Nouveau gain annuel après ajout de 5000 € : {gain_annuel_apres_ajout:.2f} €")

# L'investisseur retire 10% du montant total
retrait = montant_investissement * 0.10
montant_investissement -= retrait


# Le rendement diminue de 1%
taux_rendement -= 1

# Calcul et affichage du montant final et du nouveau gain
gain_annuel_final = montant_investissement (taux_rendement /100)
print(f"Montant après retrait de 10% : {montant_investissement:.2f} €")
print(f"Nouveau gain annuel après retrait et diminution du rendement : {gain_annuel_final:.2f} €")