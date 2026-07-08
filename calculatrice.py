while True:
    entree_a = input("Premier nombre ou q pour quitter : ")

    if entree_a == "q":
        print("Fin du programme.")
        break

    entree_b = input("Deuxième nombre : ")

    try:
        a = float(entree_a)
        b = float(entree_b)

        print("Somme :", a + b)
        print("Différence :", a - b)
        print("Produit :", a * b)

        if b != 0:
            print("Division :", a / b)
        else:
            print("Division impossible par zéro.")

        print("---")

    except ValueError:
        print("Erreur : tu dois entrer des nombres.")
        print("---")