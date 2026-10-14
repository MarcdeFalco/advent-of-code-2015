"""Advent of Code 2015, jour 11.

On énumère les mots de passe dans l'ordre alphabétique jusqu'au premier
valide : `suivant` incrémente la chaîne comme un nombre en base 26 (retenue
sur les 'z') en sautant directement les lettres interdites i, o, l, et
`valide` vérifie les règles par balayage. La partie 2 repart de la réponse
de la partie 1.
Le saut de deux lettres se fait depuis 'n' (la lettre interdite est 'o'),
pour que 'n' reste engendré.
"""


def valide(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    # Une suite croissante de trois lettres consécutives (abc, xyz...).
    longueur_suite = 1
    suite = False
    for precedent, c in zip(s, s[1:]):
        if ord(c) == ord(precedent) + 1:
            longueur_suite += 1
            if longueur_suite == 3:
                suite = True
        else:
            longueur_suite = 1
    if not suite:
        return False
    # Deux paires de lettres doublées qui ne se chevauchent pas.
    nb_paires = 0
    derniere_paire = None
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and derniere_paire != i - 1:
            nb_paires += 1
            derniere_paire = i
    return nb_paires >= 2


def suivant(s):
    # On cherche la dernière lettre différente de 'z', on l'incrémente
    # et on remet des 'a' après elle.
    for i in range(len(s)):
        c = s[len(s) - i - 1]
        if c != 'z':
            pas = 2 if c in 'hkn' else 1  # saute i, l et o
            return s[:len(s) - i - 1] + chr(ord(c) + pas) + 'a' * i
    return None


def prochain_valide(s):
    s = suivant(s)
    while not valide(s):
        s = suivant(s)
    return s


def partie1(donnees):
    return prochain_valide(donnees)


def partie2(donnees):
    return prochain_valide(partie1(donnees))


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
