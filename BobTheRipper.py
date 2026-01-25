import os
import time
from hash import HASHERS
from barre import barre_chargement


class WordlistSearcher:
    def __init__(self, hasher, chemin_liste):
        self.hasher = hasher
        self.chemin = chemin_liste

    def chercher_hash(self, hash_cible: bytes):
        taille_totale = os.path.getsize(self.chemin)

        with open(self.chemin, "rb") as f:
            lu = 0
            start = time.time()

            for ligne in f:
                lu += len(ligne)
                pourcentage = int((lu / taille_totale) * 100)
                barre_chargement(pourcentage, start)

                mot = ligne.strip()
                hash_mot = self.hasher.hash(mot)

                if hash_mot == hash_cible:
                    print(f"\n{hash_mot.hex()} : {mot.decode(errors='ignore')}")
                    return True

        print("\n✘ Le hash n'est pas dans la word list")
        return False


def choisir_hasher():
    print("\n=== Types de hash disponibles ===")
    for i, nom in enumerate(HASHERS.keys(), start=1):
        print(f"{i}) {nom}")

    choix = input("\nChoisissez un type de hash : ").strip()

    # choix par numéro
    if choix.isdigit():
        choix = int(choix)
        if 1 <= choix <= len(HASHERS):
            nom = list(HASHERS.keys())[choix - 1]
            return HASHERS[nom]()

    # choix par nom direct
    choix = choix.upper()
    if choix in HASHERS:
        return HASHERS[choix]()

    print("Type de hash invalide.")
    return None


def main():
    hasher = choisir_hasher()
    if hasher is None:
        return

    hash_hex = input("Hash à chercher (hex) : ").strip()

    try:
        hash_cible = bytes.fromhex(hash_hex)
    except ValueError:
        print("Erreur : le hash doit être en hexadécimal.")
        return

    chemin_liste = input("Chemin vers la wordlist : ").strip()

    if not os.path.isfile(chemin_liste):
        print("Erreur : fichier introuvable.")
        return

    searcher = WordlistSearcher(hasher, chemin_liste)
    searcher.chercher_hash(hash_cible)


if __name__ == "__main__":
    main()