"""Advent of Code 2015, jour 19, partie 2 : recherche en profondeur.

Première approche, remplacée par l'invariant linéaire de s.py. On inverse
les règles et on cherche en profondeur une réduction de la molécule vers 'e',
en essayant les remplacements depuis la fin de la chaîne. On renvoie la
première réduction trouvée : elle n'est pas garantie minimale en général,
mais toutes les dérivations ont ici la même longueur (voir s.py).
"""
from collections import defaultdict


def lire_entree(donnees):
    lignes = donnees.split('\n')
    regles = defaultdict(list)
    for ligne in lignes:
        if ligne == '':
            break
        a, b = ligne.split(' => ')
        regles[a].append(b)
    return regles, lignes[-1]


def partie2(donnees):
    regles, molecule = lire_entree(donnees)
    regles_inverses = defaultdict(list)
    for gauche in regles:
        for droite in regles[gauche]:
            regles_inverses[droite].append(gauche)

    def explorer(s, nb_etapes, vues):
        if s == 'e':
            return nb_etapes
        vues2 = vues | {s}
        # On remplace un motif qui se termine en position i, i décroissant.
        for i in reversed(range(1, len(s) + 1)):
            for motif in regles_inverses:
                if s[:i].endswith(motif):
                    for remplacement in regles_inverses[motif]:
                        s2 = s[:i - len(motif)] + remplacement + s[i:]
                        if s2 not in vues:
                            v = explorer(s2, nb_etapes + 1, vues2)
                            if v is not None:
                                return v

    return explorer(molecule, 0, set())


donnees = open('input.txt').read().strip()
print(partie2(donnees))
