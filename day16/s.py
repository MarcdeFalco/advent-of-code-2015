"""Advent of Code 2015, jour 16.

La description de la tante cherchée est un dictionnaire ; chaque fiche de
l'entrée est rejetée dès qu'une propriété connue est incompatible.
Partie 1 : égalité partout. Partie 2 : cats et trees doivent dépasser la
valeur cible, pomeranians et goldfish lui être inférieurs.
"""

CIBLE = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
    'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1,
}
PLUS = ['cats', 'trees']
MOINS = ['pomeranians', 'goldfish']


def compatible(propriete, valeur, avec_intervalles):
    if avec_intervalles and propriete in PLUS:
        return valeur > CIBLE[propriete]
    if avec_intervalles and propriete in MOINS:
        return valeur < CIBLE[propriete]
    return valeur == CIBLE[propriete]


def trouver_tante(donnees, avec_intervalles):
    for ligne in donnees.split('\n'):
        # "Sue 1: goldfish: 6, trees: 9, akitas: 0"
        numero = int(ligne.split()[1][:-1])
        debut = ligne.index(':')
        valide = True
        for item in ligne[debut + 2:].split(', '):
            propriete, valeur = item.split(': ')
            if not compatible(propriete, int(valeur), avec_intervalles):
                valide = False
                break
        if valide:
            reponse = numero
    return reponse


def partie1(donnees):
    return trouver_tante(donnees, False)


def partie2(donnees):
    return trouver_tante(donnees, True)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
