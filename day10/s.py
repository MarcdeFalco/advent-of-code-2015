"""Advent of Code 2015, jour 10.

Suite « lire et dire » : chaque étape remplace chaque plage de chiffres
identiques par sa longueur suivie du chiffre, ce que fait directement
`itertools.groupby`. La longueur est multipliée par environ 1,3 à chaque
étape (constante de Conway) : plusieurs millions de caractères à la fin.
"""
from itertools import groupby


def lire_et_dire(s):
    return ''.join(str(len(list(plage))) + chiffre for chiffre, plage in groupby(s))


def longueur_apres(donnees, nb_etapes):
    s = donnees
    for _ in range(nb_etapes):
        s = lire_et_dire(s)
    return len(s)


def partie1(donnees):
    return longueur_apres(donnees, 40)


def partie2(donnees):
    return longueur_apres(donnees, 50)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
