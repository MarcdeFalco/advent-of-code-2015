"""Advent of Code 2015, jour 6.

Simulation case par case : chaque instruction parcourt son rectangle.
Deux dictionnaires indexés par (x, y) sont mis à jour dans la même boucle :
`allumee` pour l'état booléen (partie 1), `luminosite` pour la partie 2
(+1 pour on, -1 sans descendre sous 0 pour off, +2 pour toggle).
"""
from collections import defaultdict


def lire_coord(s):
    x, y = map(int, s.split(','))
    return x, y


def simuler(donnees):
    allumee = defaultdict(bool)
    luminosite = defaultdict(int)
    for ligne in donnees.split('\n'):
        mots = ligne.split()
        if mots[0] == 'toggle':
            x1, y1 = lire_coord(mots[1])
            x2, y2 = lire_coord(mots[3])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    allumee[x, y] = not allumee[x, y]
                    luminosite[x, y] += 2
        else:
            # "turn on x,y through x,y" ou "turn off x,y through x,y"
            on = mots[1] == 'on'
            x1, y1 = lire_coord(mots[2])
            x2, y2 = lire_coord(mots[4])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    allumee[x, y] = on
                    luminosite[x, y] = max(0, luminosite[x, y] + (1 if on else -1))
    return sum(allumee.values()), sum(luminosite.values())


# Les deux parties sont calculées par la même simulation (lente : plusieurs
# dizaines de millions de mises à jour), lancée une seule fois.
donnees = open('input.txt').read().strip()
nb_allumees, luminosite_totale = simuler(donnees)
print(nb_allumees)
print(luminosite_totale)
