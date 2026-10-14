"""Advent of Code 2015, jour 13.

Le gain de chaque couple (a, b) est rangé dans un dictionnaire ; on essaie
toutes les permutations des convives et on somme, pour chaque paire de
voisins, les gains dans les deux sens, en refermant le cercle. Partie 2 : on
ajoute un convive neutre ('vous', gain nul avec tout le monde).
"""
from itertools import permutations


def lire_gains(donnees):
    gain = {}
    convives = []
    for ligne in donnees.split('\n'):
        # "Alice would gain 54 happiness units by sitting next to Bob."
        mots = ligne[:-1].split()
        a, b = mots[0], mots[-1]
        g = int(mots[3])
        if mots[2] == 'lose':
            g = -g
        gain[a, b] = g
        if a not in convives:
            convives.append(a)
    return gain, convives


def meilleur_placement(gain, convives):
    meilleur = 0
    for p in permutations(convives):
        bonheur = 0
        for a, b in zip(p, p[1:] + (p[0],)):
            bonheur += gain[a, b] + gain[b, a]
        meilleur = max(bonheur, meilleur)
    return meilleur


def partie1(donnees):
    return meilleur_placement(*lire_gains(donnees))


def partie2(donnees):
    gain, convives = lire_gains(donnees)
    for p in convives:
        gain[p, 'vous'] = 0
        gain['vous', p] = 0
    return meilleur_placement(gain, convives + ['vous'])


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
