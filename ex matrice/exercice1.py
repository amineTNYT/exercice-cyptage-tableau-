"""
Exercice (60min) - PRATIQUE

On désire écrire un programme en PYTHON et l'enregistrer dans votre dossier de travail sous le nom de « cryptage » permettant de crypter un MOT comme suit :

1- Saisir un MOT de 25 caractère maximum et non vide, formé uniquement par des lettres alphabétiques majuscules.

2- Remplir puis afficher une matrice M carrée par des entiers aléatoire entre 1 et 25. (ligne=colonne=nombre des caractères du MOT).

3- Former la chaine cryptée en remplaçant chaque lettre du MOT par celle qui la suit de p positions dans l'alphabet français, où p désigne sa position dans la diagonale de la matrice M.

➢ On suppose que le caractère qui suit la lettre "Z" est le caractère "A"

➢ Le code ASCII de la lettre "A" est égal à 65 et "Z" est égale à 90.

4- Afficher le message crypté.

Exemple :

Mot ← "SALUT"

M avec L=C=5 (Nb de caractère de Mot)

   0   1   2   3   4
0  19  5   8   3   7
1  2   3   8   19  22
2  23  23  7   9   7
3  2   11  12  18  3
4  7   6   12  8   15

En effet la lettre 'S' sera remplacée par 'L' car on ajoute 19 lettres
En effet la lettre 'A' sera remplacée par 'D' car on ajoute 3 lettres
En effet la lettre 'L' sera remplacée par 'S' car on ajoute 7 lettres
En effet la lettre 'U' sera remplacée par 'M' car on ajoute 18 lettres
En effet la lettre 'T' sera remplacée par 'I' car on ajoute 15 lettres

On affiche le message crypté est LDSMI
"""

import numpy as np
from random import randint

def verif(ch):
    i = 0
    test = True
    while test and i < len(ch):
        if 'A' <= ch[i] <= 'Z':
            i += 1
        else:
            test = False
    return test

def saisie():
    ch = input('Donner mot = ')
    while len(ch) == 0 or not verif(ch) or len(ch) > 25:
        ch = input('Donner mot = ')
    return ch

def remplirM(M, N):
    for i in range(N):
        for j in range(N):
            M[i, j] = randint(1, 25)

def afficherM(M, I):
    for i in range(I):
        for j in range(I):
            print(M[i, j], end=' ')
        print()

def Afficher(ch, M, I):
    chx = ""
    for i in range(I):
        c = ord(ch[i]) + M[i, i]
        if c > 90:
            chx += chr(c - 26)
        else:
            chx += chr(c)
    print(chx)

# Programme principal
ch = saisie()
l = len(ch)
M = np.zeros((l, l), dtype=int) 
remplirM(M, l)
afficherM(M, l)
Afficher(ch, M, l)


