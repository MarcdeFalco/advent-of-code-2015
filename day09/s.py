"""Advent of Code 2015, jour 9.

Retour sur trace sans élagage : `meilleure_route` explore tous les chemins
simples depuis une ville en gardant la liste des villes visitées, et renvoie
la meilleure longueur au sens de `choix` (min pour la partie 1, max pour la
partie 2). O(n!) chemins, raisonnable pour 8 villes.
"""
from collections import defaultdict


def lire_graphe(donnees):
    voisins = defaultdict(list)
    for ligne in donnees.split('\n'):
        a, _, b, _, d = ligne.split()  # "A to B = d"
        voisins[a].append((b, int(d)))
        voisins[b].append((a, int(d)))
    return voisins


def meilleure_route(voisins, choix):
    nb_villes = len(voisins)

    def explorer(ville, visitees, longueur):
        if len(visitees) == nb_villes:
            return longueur
        resultats = [explorer(v, visitees + [v], longueur + d)
                     for v, d in voisins[ville] if v not in visitees]
        # Impasse (aucun voisin libre) : None, ignoré par l'appelant.
        resultats = [r for r in resultats if r is not None]
        return choix(resultats) if resultats else None

    return choix(explorer(v, [v], 0) for v in voisins)


def partie1(donnees):
    return meilleure_route(lire_graphe(donnees), min)


def partie2(donnees):
    return meilleure_route(lire_graphe(donnees), max)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
