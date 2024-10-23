def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("nul")

# Appel de la fonction avec différents paramètres
verifier_nombre(5)   # positif
verifier_nombre(-3)  # négatif
verifier_nombre(0)   # nul
verifier_nombre(12)  # positif
verifier_nombre(-8)  # négatif