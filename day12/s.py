"""Advent of Code 2015, jour 12.

`json.loads` construit l'arbre (listes, dictionnaires, entiers, chaînes) et
`total` le parcourt récursivement selon le type du nœud. Partie 2 : un
dictionnaire contenant "red" vaut 0, ce qui élague tout son sous-arbre (le
test porte sur les clés et les valeurs, plus large que nécessaire).
"""
import json


def total(arbre, ignorer_rouge):
    if type(arbre) == list:
        return sum(total(v, ignorer_rouge) for v in arbre)
    if type(arbre) == dict:
        if ignorer_rouge and ('red' in arbre.keys() or 'red' in arbre.values()):
            return 0
        return sum(total(v, ignorer_rouge) for v in arbre.values())
    if type(arbre) == int:
        return arbre
    return 0


def partie1(donnees):
    return total(json.loads(donnees), False)


def partie2(donnees):
    return total(json.loads(donnees), True)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
