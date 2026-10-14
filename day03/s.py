"""Advent of Code 2015, jour 3.

Les cases visitées sont rangées dans un ensemble de couples (x, y), ce qui
élimine les doublons. Avec plusieurs marcheurs, le k-ième déplacement est
effectué par le marcheur k modulo leur nombre (partie 1 : un seul marcheur,
partie 2 : deux marcheurs qui alternent).
"""

DEPLACEMENTS = {'<': (-1, 0), '>': (1, 0), 'v': (0, 1), '^': (0, -1)}


def nb_cases_visitees(donnees, nb_marcheurs):
    positions = [(0, 0)] * nb_marcheurs
    visitees = {(0, 0)}
    for i, c in enumerate(donnees):
        dx, dy = DEPLACEMENTS[c]
        k = i % nb_marcheurs
        x, y = positions[k]
        positions[k] = (x + dx, y + dy)
        visitees.add(positions[k])
    return len(visitees)


def partie1(donnees):
    return nb_cases_visitees(donnees, 1)


def partie2(donnees):
    return nb_cases_visitees(donnees, 2)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
