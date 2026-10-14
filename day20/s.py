"""Advent of Code 2015, jour 20 (partie 2 seulement).

Le lutin n dépose 11 cadeaux dans les maisons n, 2n, ..., 50n : la maison n
reçoit 11 fois la somme de ses diviseurs d tels que n/d <= 50, c'est-à-dire
d >= n/50. Recherche linéaire : pour chaque n, on somme ces diviseurs par
essais de division, jusqu'à atteindre le seuil. La recherche part de 720720,
entier très composé choisi comme point de départ.
Partie 1 : pas de solution.
La borne n / 50 est arrondie vers le haut : l'arrondi inférieur pourrait
compter un diviseur d avec n/d = 51.
"""

DEPART = 720720


def partie2(donnees):
    seuil = int(donnees) / 11
    n = DEPART
    while True:
        n += 1
        borne = -(-n // 50)  # arrondi supérieur de n / 50
        total = sum(d for d in range(max(1, borne), n + 1) if n % d == 0)
        if total >= seuil:
            return n


donnees = open('input.txt').read().strip()
print(partie2(donnees))
