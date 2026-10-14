"""Advent of Code 2015, jour 14.

Partie 1 : formule fermée. En t secondes, un renne fait t // (vol + repos)
cycles complets, plus une fraction de vol (au plus `vol`) du cycle en cours.
Partie 2 : il faut le classement à chaque seconde, donc une vraie
simulation, en suivant pour chaque renne le temps de vol ou de repos
restant, la distance parcourue et les points.
"""

DUREE = 2503


def lire_rennes(donnees):
    rennes = []
    for ligne in donnees.split('\n'):
        # "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."
        mots = ligne.split()
        rennes.append((mots[0], int(mots[3]), int(mots[6]), int(mots[-2])))
    return rennes


def distance(renne, t):
    _, vitesse, vol, repos = renne
    nb_cycles = t // (vol + repos)
    reste = min(t % (vol + repos), vol)
    return vitesse * (vol * nb_cycles + reste)


def partie1(donnees):
    return max(distance(renne, DUREE) for renne in lire_rennes(donnees))


def partie2(donnees):
    rennes = lire_rennes(donnees)
    repos_restant = {r[0]: 0 for r in rennes}
    vol_restant = {r[0]: r[2] for r in rennes}
    points = {r[0]: 0 for r in rennes}
    dist = {r[0]: 0 for r in rennes}

    for _ in range(DUREE):
        for nom, vitesse, vol, repos in rennes:
            if repos_restant[nom] > 0:
                repos_restant[nom] -= 1
                if repos_restant[nom] == 0:
                    vol_restant[nom] = vol
            else:
                dist[nom] += vitesse
                vol_restant[nom] -= 1
                if vol_restant[nom] == 0:
                    repos_restant[nom] = repos
        # Un point pour chaque renne en tête (ex aequo compris).
        en_tete = max(dist.values())
        for nom in dist:
            if dist[nom] == en_tete:
                points[nom] += 1

    return max(points.values())


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
