"""Advent of Code 2015, jour 15.

Énumération des compositions de 100 en quatre quantités : trois boucles
imbriquées, la quatrième quantité étant déduite (environ 1,8e5 recettes).
Une recette est notée par le produit des caractéristiques (capacité,
durabilité, saveur, texture) ramenées à 0 si négatives. Partie 2 : on ne
garde que les recettes à 500 calories. Le nombre d'ingrédients (4) est fixé.
"""


def lire_ingredients(donnees):
    ingredients = []
    for ligne in donnees.split('\n'):
        # "Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2"
        mots = ligne.split()
        ingredients.append((int(mots[2][:-1]), int(mots[4][:-1]),
                            int(mots[6][:-1]), int(mots[8][:-1]),
                            int(mots[10])))
    return ingredients


def meilleur_score(ingredients, calories_imposees=None):
    meilleur = 0
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                quantites = [a, b, c, 100 - a - b - c]
                calories = sum(q * ing[4] for q, ing in zip(quantites, ingredients))
                if calories_imposees is not None and calories != calories_imposees:
                    continue
                score = 1
                for i in range(4):
                    score *= max(0, sum(q * ing[i] for q, ing in zip(quantites, ingredients)))
                meilleur = max(score, meilleur)
    return meilleur


def partie1(donnees):
    return meilleur_score(lire_ingredients(donnees))


def partie2(donnees):
    return meilleur_score(lire_ingredients(donnees), 500)


donnees = open('input.txt').read().strip()
print(partie1(donnees))
print(partie2(donnees))
