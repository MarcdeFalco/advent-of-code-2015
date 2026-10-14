"""Advent of Code 2015, jour 21.

On énumère arme x armure x paire d'anneaux (l'armure vide et deux anneaux
vides permettent de n'en prendre aucun ou un seul). Le combat n'est pas
simulé : le joueur a besoin de ceil(pv_adversaire / dégâts_nets) tours et
gagne s'il survit aux attaques reçues d'ici là (il frappe en premier).
Partie 1 : coût minimal pour gagner ; partie 2 : coût maximal pour perdre.
Les dégâts nets valent au moins 1 (règle de l'énoncé), ce qui évite aussi
une division par zéro.
"""
import re
from math import ceil

# (coût, dégâts, armure)
ARMES = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
ARMURES = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
ANNEAUX = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0),
           (20, 0, 1), (40, 0, 2), (80, 0, 3)]
PV_JOUEUR = 100


def victoire(joueur, adversaire):
    pv_adv, degats_adv, armure_adv = adversaire
    pv, degats, armure = joueur
    nb_tours = ceil(pv_adv / max(1, degats - armure_adv))
    return pv > (nb_tours - 1) * max(1, degats_adv - armure)


def equipements():
    """Engendre (coût, dégâts, armure) pour chaque équipement possible."""
    for arme in ARMES:
        for armure in ARMURES:
            for i, anneau1 in enumerate(ANNEAUX):
                for anneau2 in ANNEAUX[i + 1:]:
                    objets = (arme, armure, anneau1, anneau2)
                    yield tuple(sum(o[k] for o in objets) for k in range(3))


def partie1(donnees):
    adversaire = tuple(map(int, re.findall(r'\d+', donnees)))
    return min(cout for cout, degats, armure in equipements()
               if victoire((PV_JOUEUR, degats, armure), adversaire))


def partie2(donnees):
    adversaire = tuple(map(int, re.findall(r'\d+', donnees)))
    return max(cout for cout, degats, armure in equipements()
               if not victoire((PV_JOUEUR, degats, armure), adversaire))


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
