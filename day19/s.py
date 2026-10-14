"""Advent of Code 2015, jour 19.

Partie 1 : on applique chaque règle à chaque position de la molécule et on
range les résultats dans un ensemble pour ne compter que les molécules
distinctes.
Partie 2 : invariant linéaire. On cherche un poids w sur les atomes tel que
chaque règle A -> B1...Bk augmente le poids total d'exactement 1, soit
1 + w(A) = w(B1) + ... + w(Bk) (avec w(e) = 0) : un système linéaire résolu
avec sympy. Toute dérivation de la molécule a alors pour longueur son poids.
Une recherche en profondeur, plus ancienne, est dans
partie2_recherche_profondeur.py.
"""
import re
from collections import defaultdict

import sympy as sp


def lire_entree(donnees):
    lignes = donnees.split('\n')
    regles = defaultdict(list)
    for ligne in lignes:
        if ligne == '':
            break
        a, b = ligne.split(' => ')
        regles[a].append(b)
    return regles, lignes[-1]


def atomes(s):
    """Découpe une molécule en atomes : une majuscule, puis une minuscule éventuelle."""
    return re.findall(r"[A-Z][a-z]?", s)


def partie1(donnees):
    regles, molecule = lire_entree(donnees)
    resultats = set()
    for i in range(len(molecule)):
        for gauche in regles:
            if molecule[i:].startswith(gauche):
                for droite in regles[gauche]:
                    resultats.add(molecule[:i] + droite + molecule[i + len(gauche):])
    return len(resultats)


def partie2(donnees):
    regles, molecule = lire_entree(donnees)
    # Liste des atomes rencontrés (elle était écrite à la main).
    noms = sorted({a for droites in regles.values() for d in droites for a in atomes(d)}
                  | {a for a in regles if a != 'e'} | set(atomes(molecule)))
    inconnues = sp.symbols(noms)
    poids = dict(zip(noms, inconnues))

    def equation(gauche, atomes_droite):
        membre_gauche = 1 + (poids[gauche] if gauche != 'e' else 0)
        return membre_gauche - sum(poids[a] for a in atomes_droite)

    equations = [equation(gauche, atomes(droite))
                 for gauche in regles for droite in regles[gauche]]
    solution = sp.solve(equations, inconnues, dict=True)[0]
    # Les inconnues restées libres (solution non unique) sont fixées à 0 :
    # on obtient un poids valide parmi d'autres.
    w = {nom: 0 for nom in noms}
    for x, expr in solution.items():
        w[x.name] = expr.subs({f: 0 for f in expr.free_symbols})
    return sum(w[a] for a in atomes(molecule))


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
