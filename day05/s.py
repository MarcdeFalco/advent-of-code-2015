"""Advent of Code 2015, jour 5.

Chaque critère est vérifié par un balayage de fenêtres de 2 ou 3 caractères.
Partie 2 : s[i:i+2] in s[i+2:] cherche une paire qui réapparaît plus loin,
sans chevauchement.
"""


def gentille1(s):
    voyelles = sum(1 for c in s if c in 'aeiou')
    if voyelles < 3:
        return False
    double = any(s[i] == s[i + 1] for i in range(len(s) - 1))
    if not double:
        return False
    return all(motif not in s for motif in ['ab', 'cd', 'pq', 'xy'])


def gentille2(s):
    paire_repetee = any(s[i:i + 2] in s[i + 2:] for i in range(len(s) - 2))
    if not paire_repetee:
        return False
    return any(s[i] == s[i + 2] for i in range(len(s) - 2))


def partie1(donnees):
    return sum(1 for ligne in donnees.split('\n') if gentille1(ligne))


def partie2(donnees):
    return sum(1 for ligne in donnees.split('\n') if gentille2(ligne))


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
