"""Advent of Code 2015, jour 7.

Chaque fil est associé à l'expression qui le définit ; `valeur` évalue un fil
en évaluant récursivement ses opérandes et mémorise le résultat dans un cache
(sans lui, une valeur partagée serait recalculée un nombre exponentiel de
fois). Partie 2 : on vide le cache et on impose au fil b la réponse de la
partie 1.
"""

MASQUE = 65535  # mots de 16 bits


def lire_circuit(donnees):
    definition = {}
    for ligne in donnees.split('\n'):
        expression, fil = ligne.split(' -> ')
        definition[fil] = expression
    return definition


def evaluer_fil(definition, cache, fil):
    def valeur(operande):
        if operande.isdigit():
            return int(operande)
        if operande not in cache:
            cache[operande] = evaluer(definition[operande])
        return cache[operande]

    def evaluer(expression):
        mots = expression.split()
        if len(mots) == 1:
            return valeur(mots[0])
        if len(mots) == 2:  # NOT x
            return MASQUE ^ valeur(mots[1])
        a, op, b = valeur(mots[0]), mots[1], valeur(mots[2])
        if op == 'AND':
            return a & b
        if op == 'OR':
            return a | b
        if op == 'LSHIFT':
            return (a << b) & MASQUE
        if op == 'RSHIFT':
            return a >> b

    return valeur(fil)


def partie1(donnees):
    return evaluer_fil(lire_circuit(donnees), {}, 'a')


def partie2(donnees):
    # Le cache initial contient la valeur imposée au fil b.
    cache = {'b': partie1(donnees)}
    return evaluer_fil(lire_circuit(donnees), cache, 'a')


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
