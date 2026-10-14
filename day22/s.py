"""Advent of Code 2015, jour 22.

Retour sur trace mémoïsé : `combat` explore toutes les suites de sorts à
partir d'un état complet (à qui le tour, points de vie, mana, points de vie
de l'adversaire, dépense, durées restantes des effets Shield, Poison et
Recharge) et renvoie la dépense minimale pour gagner (INFINI en cas de
défaite). Au tour du joueur on prend le minimum sur les sorts lançables ; au
tour de l'adversaire il n'y a qu'un successeur. Partie 2 : le joueur perd
1 point de vie au début de chacun de ses tours.
"""
import re

INFINI = 10000000000


def depense_minimale(donnees, difficile):
    pv_adv, degats_adv = map(int, re.findall(r'\d+', donnees))
    cache = {}

    def combat(*etat):
        if etat in cache:
            return cache[etat]
        tour_joueur, pv, mana, pv_adv, depense, shield, poison, recharge = etat

        if difficile and tour_joueur:
            pv -= 1

        # Application des effets en cours.
        if shield > 0:
            shield -= 1
        armure = 7 if shield > 0 else 0
        if poison > 0:
            pv_adv -= 3
            poison -= 1
        if recharge > 0:
            mana += 101
            recharge -= 1

        if pv <= 0:
            v = INFINI
        elif pv_adv <= 0:
            v = depense
        elif mana < 53:
            # Plus aucun sort lançable. Ce test est fait aussi au tour de
            # l'adversaire, alors qu'une recharge pourrait encore rendre du
            # mana : cela peut écarter à tort quelques branches.
            v = INFINI
        elif tour_joueur:
            v = INFINI
            # Magic Missile
            v = min(v, combat(False, pv, mana - 53, pv_adv - 4, depense + 53,
                              shield, poison, recharge))
            if mana >= 73:  # Drain
                v = min(v, combat(False, pv + 2, mana - 73, pv_adv - 2, depense + 73,
                                  shield, poison, recharge))
            if mana >= 113 and shield == 0:
                v = min(v, combat(False, pv, mana - 113, pv_adv, depense + 113,
                                  6, poison, recharge))
            if mana >= 173 and poison == 0:
                v = min(v, combat(False, pv, mana - 173, pv_adv, depense + 173,
                                  shield, 6, recharge))
            if mana >= 229 and recharge == 0:
                v = min(v, combat(False, pv, mana - 229, pv_adv, depense + 229,
                                  shield, poison, 5))
        else:
            pv -= max(1, degats_adv - armure)
            v = combat(True, pv, mana, pv_adv, depense, shield, poison, recharge)
        cache[etat] = v
        return v

    return combat(True, 50, 500, pv_adv, 0, 0, 0, 0)


def partie1(donnees):
    return depense_minimale(donnees, False)


def partie2(donnees):
    return depense_minimale(donnees, True)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
