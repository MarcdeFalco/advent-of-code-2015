"""Advent of Code 2015, jour 24.

On cherche le plus petit premier groupe de paquets de poids total/k
(k = 3 groupes en partie 1, 4 en partie 2) : `combinations` énumère les
sous-ensembles par taille croissante, on s'arrête à la première taille qui
donne une solution et on garde le plus petit produit des poids. Pour chaque
candidat, on vérifie seulement qu'un deuxième groupe de même poids existe
dans le reste (suffisant en pratique, mais ce n'est pas une preuve que la
répartition complète existe). On suppose les poids distincts.
"""
from itertools import combinations
from math import prod


def deuxieme_groupe_possible(restants, cible):
    for taille in range(len(restants)):
        for groupe in combinations(restants, taille):
            if sum(groupe) == cible:
                return True
    return False


def meilleure_intrication(donnees, nb_groupes):
    poids = list(map(int, donnees.split('\n')))
    cible = sum(poids) // nb_groupes
    for taille in range(len(poids)):
        solutions = []
        for groupe in combinations(poids, taille):
            if sum(groupe) == cible:
                restants = [p for p in poids if p not in groupe]
                if deuxieme_groupe_possible(restants, cible):
                    solutions.append(prod(groupe))
        if solutions:
            return min(solutions)


def partie1(donnees):
    return meilleure_intrication(donnees, 3)


def partie2(donnees):
    return meilleure_intrication(donnees, 4)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
