#création des variables 
nom= 'Tshirt'
prix_unitaire=20
quantité_en_stock=100

#Affichage 
print('les information sur les produit')
print(f'nom de produit : {nom}')
print(f'prix unitaire : {prix_unitaire} $')
print(f'quantité en stock : {quantité_en_stock} unité')

#Demander à l'utilisateur d'ajouter une quantité en stock 
quantité_en_plus=int(input("Combien de T-shirts souhaitez-vous ajouter? "))
quantité_a_jour= quantité_en_stock + quantité_en_plus

# Mise à jour du prix en cas d'inflation (augmentation de 10%)
augmentation = 0.10
prix_unitaire *= (1 + augmentation)

# Affichege des information aprés les modifications 
print('les information sur les produit(mise à jour)')
print(f'nom de produit : {nom}')
print(f'prix unitaire : {prix_unitaire} $')
print(f'quantité en stock : {quantité_a_jour} unité')