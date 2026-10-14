"""Advent of Code 2015, jour 2.

Pour chaque pavé l x w x h, formules fermées :
- papier : surface totale plus la plus petite face ;
- ruban : plus petit périmètre d'une face plus le volume.
On accumule les deux quantités sur toutes les lignes.
"""


def papier_et_ruban(donnees):
    papier = 0
    ruban = 0
    for ligne in donnees.split('\n'):
        l, w, h = map(int, ligne.split('x'))
        papier += 2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l)
        ruban += 2 * min(l + w, l + h, w + h) + l * w * h
    return papier, ruban


def partie1(donnees):
    return papier_et_ruban(donnees)[0]


def partie2(donnees):
    return papier_et_ruban(donnees)[1]


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
