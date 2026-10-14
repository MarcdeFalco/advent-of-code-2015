"""Advent of Code 2015, jour 4.

Force brute : on essaie i = 0, 1, 2, ... jusqu'à ce que le haché MD5 de la
clé suivie de i commence par cinq (partie 1) ou six (partie 2) zéros
hexadécimaux. Une fonction de hachage n'offre aucune structure exploitable.
"""
import hashlib


def plus_petit_entier(cle, nb_zeros):
    prefixe = '0' * nb_zeros
    i = 0
    while True:
        hache = hashlib.md5((cle + str(i)).encode('ascii')).hexdigest()
        if hache.startswith(prefixe):
            return i
        i += 1


def partie1(donnees):
    return plus_petit_entier(donnees, 5)


def partie2(donnees):
    return plus_petit_entier(donnees, 6)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
