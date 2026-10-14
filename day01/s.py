"""Advent of Code 2015, jour 1.

On suit l'étage courant : '(' fait monter d'un étage, ')' descendre.
Partie 1 : étage final ; partie 2 : position (à partir de 1) du premier
caractère qui amène au sous-sol (étage -1).
"""


def partie1(donnees):
    etage = 0
    for c in donnees:
        etage += 1 if c == '(' else -1
    return etage


def partie2(donnees):
    etage = 0
    for i, c in enumerate(donnees):
        etage += 1 if c == '(' else -1
        if etage == -1:
            return i + 1


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
