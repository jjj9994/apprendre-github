def demander_nombre(message):
    while True:
        valeur = input(message)

        try:
            return float(valeur)
        except ValueError:
            print("Erreur : tu dois entrer un nombre.")


def afficher_resultats(a, b):
    print("Somme :", a + b)
    print("Différence :", a - b)
    print("Produit :", a * b)

    if b != 0:
        print("Division :", a / b)
    else:
        print("Division impossible par zéro.")


while True:
    choix = input("Appuie sur Entrée pour calculer ou tape q pour quitter : ")

    if choix == "q":
        print("Fin du programme.")
        break

    nombre_1 = demander_nombre("Premier nombre : ")
    nombre_2 = demander_nombre("Deuxième nombre : ")

    afficher_resultats(nombre_1, nombre_2)
    print("---")