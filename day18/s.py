"""Advent of Code 2015, jour 18.

Automate cellulaire du type jeu de la vie sur une grille 100 x 100 : à
chaque étape, `etape_suivante` construit une nouvelle grille (double tampon)
en comptant les huit voisins de chaque case. Partie 2 : les quatre coins
restent allumés (remis à '#' au départ et après chaque étape).
"""
from itertools import product


def nb_voisins_allumes(grille, x, y):
    w, h = len(grille), len(grille[0])
    nb = 0
    for dx, dy in product(range(-1, 2), range(-1, 2)):
        if (dx, dy) == (0, 0):
            continue
        if 0 <= x + dx < w and 0 <= y + dy < h and grille[x + dx][y + dy] == '#':
            nb += 1
    return nb


def allumer_coins(grille):
    w, h = len(grille), len(grille[0])
    grille[0][0] = grille[w - 1][0] = grille[0][h - 1] = grille[w - 1][h - 1] = '#'


def etape_suivante(grille, coins_bloques):
    w, h = len(grille), len(grille[0])
    nouvelle = [['.'] * h for _ in range(w)]
    for x in range(w):
        for y in range(h):
            c = nb_voisins_allumes(grille, x, y)
            if (grille[x][y] == '#' and c in [2, 3]) or (grille[x][y] == '.' and c == 3):
                nouvelle[x][y] = '#'
    if coins_bloques:
        allumer_coins(nouvelle)
    return nouvelle


def nb_allumees_apres(donnees, nb_etapes, coins_bloques):
    grille = list(map(list, donnees.split('\n')))
    if coins_bloques:
        allumer_coins(grille)
    for _ in range(nb_etapes):
        grille = etape_suivante(grille, coins_bloques)
    return sum(ligne.count('#') for ligne in grille)


def partie1(donnees):
    return nb_allumees_apres(donnees, 100, False)


def partie2(donnees):
    return nb_allumees_apres(donnees, 100, True)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
