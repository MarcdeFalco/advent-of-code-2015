"""Advent of Code 2015, jour 25.

`rang` donne la position d'une case dans l'ordre de remplissage par
diagonales : c'est la numérotation de Cantor y + (x+y)(x+y+1)/2 (indices à
partir de 0). On applique ensuite la récurrence u(k+1) = 252533 u(k) mod
33554393 autant de fois, en O(k) (l'exponentiation rapide
pow(252533, k, 33554393) donnerait le résultat en O(log k)).
Il n'y a pas de partie 2.
"""
import re

PREMIER_CODE = 20151125


def code_suivant(n):
    return (n * 252533) % 33554393


def code(k):
    p = PREMIER_CODE
    for _ in range(k):
        p = code_suivant(p)
    return p


def rang(x, y):
    return y + ((x + y) * (x + y + 1)) // 2


def partie1(donnees):
    ligne, colonne = map(int, re.findall(r'\d+', donnees))
    return code(rang(ligne - 1, colonne - 1))


donnees = open('input.txt').read().strip()
print(partie1(donnees))
