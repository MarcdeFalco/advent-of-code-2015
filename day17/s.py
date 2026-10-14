"""Advent of Code 2015, jour 17.

Dénombrement du sac à dos par mémoïsation : nb_facons(i, n) compte les
sous-ensembles des récipients d'indice >= i de contenance totale n, en
prenant ou non le récipient i. Partie 2 : on calcule d'abord le nombre
minimal de récipients, puis on compte les solutions de cette taille avec un
état enrichi (i, n, m), m étant le nombre de récipients déjà pris.
"""
from functools import cache

VOLUME = 150
INFINI = 1000000


def partie1(donnees):
    contenances = list(map(int, donnees.split('\n')))

    @cache
    def nb_facons(i, n):
        if i == len(contenances):
            return 1 if n == 0 else 0
        v = nb_facons(i + 1, n)
        if contenances[i] <= n:
            v += nb_facons(i + 1, n - contenances[i])
        return v

    return nb_facons(0, VOLUME)


def partie2(donnees):
    contenances = list(map(int, donnees.split('\n')))

    @cache
    def nb_min(i, n):
        """Nombre minimal de récipients d'indice >= i pour remplir n."""
        if i == len(contenances):
            return 0 if n == 0 else INFINI
        v = nb_min(i + 1, n)
        if contenances[i] <= n:
            v = min(v, 1 + nb_min(i + 1, n - contenances[i]))
        return v

    minimum = nb_min(0, VOLUME)

    @cache
    def nb_facons_minimales(i, n, m):
        if i == len(contenances):
            return 1 if n == 0 and m == minimum else 0
        v = nb_facons_minimales(i + 1, n, m)
        if contenances[i] <= n:
            v += nb_facons_minimales(i + 1, n - contenances[i], m + 1)
        return v

    return nb_facons_minimales(0, VOLUME, 0)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
