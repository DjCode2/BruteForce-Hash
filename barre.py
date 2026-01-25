import time

start = time.time()
def barre_chargement(pourcentage,start):
    if type(pourcentage) != int:
        print("le pourcentage doit être un entier")
        return

    # Barre d'origine
    bar = f"[ {pourcentage * '-'}{(100 - pourcentage) * ' '} {pourcentage}% ]"

    elapsed = time.time() - start

    if elapsed > 60:
        elapsed_affiche = elapsed / 60
        signe_elapsed = "m"
    else:
        elapsed_affiche = elapsed
        signe_elapsed = "s"

        
    # Remonter d'une ligne + réécrire les deux lignes
    print("\r\033[F" + bar)  # ligne 1
    print(f"Temps écoulé : {elapsed_affiche:5.1f}{signe_elapsed}   ", end="")  # ligne 2


# Pré-affichage de 2 lignes vides pour pouvoir les réécrire ensuite
print("\n")
