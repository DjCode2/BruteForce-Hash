
# **BobTheRipper **

BobTheRipper est un outil simple et extensible de **brute‑force de hash** écrit en Python.  
Il permet de retrouver un mot de passe à partir d’un hash en parcourant une wordlist, avec une barre de progression et plusieurs algorithmes supportés.

BobTheRipper est conçu à but éducatif, l’objectif étant de comprendre le fonctionnement des outils que nous utilisons fréquemment.
Il n’y a aucune licence. Sentez‑vous libre de modifier ce qu’il vous plaira ! 


---

## **Fonctionnalités**
- Sélection du type de hash via un menu interactif  
- Support de plusieurs algorithmes :
  - **MD5**
  - **SHA‑1**
  - **SHA‑256**
  - **NTLM**
- Lecture rapide de wordlist en mode streaming  
- Barre de progression avec temps écoulé  
- Affichage du mot trouvé + hash correspondant  

---

## **Utilisation**
1. Lancer le script :

```
python BobTheRipper.py
```

2. Choisir le type de hash  
3. Entrer le hash en hexadécimal  
4. Indiquer le chemin vers la wordlist  
5. Attendre que BobTheRipper trouve le mot (ou non)

---

## **Structure du projet**
```
BobTheRipper/
 ├── BobTheRipper.py        # Script principal
 ├── hash/
 │    ├── hasher.py         # Classe abstraite
 │    ├── md5.py
 │    ├── sha1.py
 │    ├── sha256.py
 │    ├── ntlm.py
 │    └── __init__.py       # Dictionnaire HASHERS
 ├── barre.py               # Barre de progression
 └── README.md
```

---

## **Objectif**
BobTheRipper est conçu pour être :
- **simple à comprendre**
- **facile à étendre**, il sera d'ailleurs sans doute étendu au fur et à mesure de mes besoins !
- **pratique en CTF**
- **idéal pour apprendre les bases du cracking CPU**

