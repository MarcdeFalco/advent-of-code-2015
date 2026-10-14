r"""Advent of Code 2015, jour 8.

Chaque ligne est un littéral de chaîne entre guillemets. On l'analyse
caractère par caractère en reconnaissant les trois échappements (\\, \" et
\xHH), ce qui donne la longueur en mémoire (partie 1). Le compteur `surcout`
mesure ce qu'ajoute le réencodage (partie 2) : 4 pour les guillemets
extérieurs, puis 1 par barre oblique inverse ou guillemet rencontré.
"""


def analyser(ligne):
    """Renvoie (nombre de caractères en mémoire, surcoût du réencodage)."""
    i = 1  # on saute le guillemet ouvrant
    nb_caracteres = 0
    surcout = 4
    while ligne[i] != '"':
        if ligne[i] == '\\':
            surcout += 1
            if ligne[i + 1] in '\\"':
                surcout += 1
                i += 2
            else:  # \xHH
                i += 4
        else:
            i += 1
        nb_caracteres += 1
    return nb_caracteres, surcout


def partie1(donnees):
    return sum(len(ligne) - analyser(ligne)[0] for ligne in donnees.split('\n'))


def partie2(donnees):
    return sum(analyser(ligne)[1] for ligne in donnees.split('\n'))


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
