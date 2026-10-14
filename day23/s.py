"""Advent of Code 2015, jour 23.

Interprète direct d'une machine à deux registres : un dictionnaire pour les
registres, un compteur ordinal `pc` incrémenté avant l'exécution de
l'instruction (d'où les « - 1 » dans les sauts). Partie 1 : a vaut 0 au
départ ; partie 2 : a vaut 1.
"""


def executer(donnees, a):
    registres = {'a': a, 'b': 0}
    programme = donnees.split('\n')
    pc = 0
    while pc < len(programme):
        op, arguments = programme[pc].split(' ', 1)
        pc += 1
        if op == 'hlf':
            registres[arguments] //= 2
        elif op == 'tpl':
            registres[arguments] *= 3
        elif op == 'inc':
            registres[arguments] += 1
        elif op == 'jmp':
            pc += int(arguments) - 1
        elif op == 'jie':
            r, decalage = arguments.split(', ')
            if registres[r] % 2 == 0:
                pc += int(decalage) - 1
        elif op == 'jio':  # saut si égal à 1 (« jump if one »)
            r, decalage = arguments.split(', ')
            if registres[r] == 1:
                pc += int(decalage) - 1
    return registres['b']


def partie1(donnees):
    return executer(donnees, 0)


def partie2(donnees):
    return executer(donnees, 1)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
