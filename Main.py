import random
import sys
from itertools import count

import mm
import pygame
import doctest


# Programme principale
def prog() -> None:
    """
    Programme principale

    :return: None
    """

    # Initialisation des variables
    count = 1
    screen: pygame.display = creerScreen()
    secret: list = creerCombinaisonSecrete()
    mm.afficherPlateau(screen)
    mm.afficherChoixCouleur(screen)
    mm.afficherSecret(screen, secret)

    # Tant que le jeu est en cours
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        count += 1
        a: list = mm.construireProposition(screen, count)
        victory: bool = afficherVictoire(secret, a, screen, count)
        mm.afficherResultat(screen, tuples(a, secret), count)

        if victory:
            # Affiche la combinaison secréte en cas de victoire
            mm.afficherCombinaison(screen, a, count)


# Détermine le résultat de la partie
def determinerVictoire(secret: list, a: list) -> bool:
    """
    Détermine si la combinaison de l'utilisateur est similaire à la combinaison secréte
    :param secret:
    :param a:
    :return: bool

    >>> determinerVictoire([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    True
    >>> determinerVictoire([1, 2, 3, 4, 5], [1, 2, 3, 4, 6])
    False
    """

    # Regarde si la combinaison secret et similaire à la combinaison de l'utilisateur
    if secret == a:
        return True
    return False


# Affichage du résultat de la partie
def afficherVictoire(secret: list, a: list, screen: pygame.surface, count: int) -> bool:
    """
    Affiche le résultat de la partie
    :param secret:
    :param a:
    :param screen:
    :param count:
    :return: bool

    >>> afficherVictoire([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], creerScreen(), 16)
    True
    >>> afficherVictoire([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], creerScreen(), 16)
    True
    >>> afficherVictoire([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], creerScreen(), 15)
    False
    """

    # Affiche la victoire
    if determinerVictoire(secret, a):
        msg: str = "Vous avez gagnez ! en " + str(count - 1) + " coup !"
        message = pygame.font.SysFont('monospace', 20)
        message.set_bold(True)
        label = message.render(msg, 1, mm.Noir)
        screen.blit(label, (250, 700))
        mm.afficherSecret(screen, secret)
        return True

    # Affiche la défaite
    elif count == 16:
        msg: str = "Vous avez perdue ! en " + str(count - 1) + " coup !"
        message = pygame.font.SysFont('monospace', 20)
        message.set_bold(True)
        label = message.render(msg, 1, 30)
        screen.blit(label, (250, 700))
        mm.afficherSecret(screen, secret)
        return True
    else:
        return False


# Création de l'affichage graphique
def creerScreen() -> pygame.display:
    """
    Création de l'affichage graphique

    :return: pygame.display

    >>> creerScreen()
    <Surface(800x750x32 SW)>
    """

    pygame.init()
    # Taille d'affichage sur 800px de largeur et 750px de hauteur
    screen: pygame.surface = pygame.display.set_mode((800, 750))
    screen.fill((255, 255, 255))
    return screen


# Création de la combinaison secréte en aléatoire
def creerCombinaisonSecrete() -> list:
    """
    Création de la combinaison secréte en aléatoire

    :return: list
    """

    secret: list = []
    i: int
    for _ in range(5):
        i = random.randint(1, 6)
        secret.append(mm.TabCouleur[i])
    # print(secret)
    return secret


# Fonction nb bien placé / nb mal placé
def tuples(a,secret) -> tuple:
    """
    Permet de déterminer le nombre de bien placé et de mal placé
    :param a:
    :param secret:
    :return: tuple

    >>> tuples([1, 2, 3, 4, 5],[1, 2, 3, 4, 5])
    (5, 0)
    >>> tuples([1, 2, 3, 4, 5],[1, 2, 3, 4, 6])
    (4, 0)
    >>> tuples([1, 2, 3, 4, 5],[2, 1, 3, 4, 5])
    (3, 2)
    >>> tuples([1, 2, 3, 4, 5],[1, 1, 6, 6, 6])
    (1, 0)
    """

    countGood: int = 0
    countBad: int = 0
    counts: dict = {}

    for i in secret:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1

    for i,j in zip(a, secret):
        if i == j:
            countGood += 1
            counts[i] -= 1

    for i in a:
        if i in counts and counts[i] > 0:
            countBad += 1
            counts[i] -= 1


    return (countGood, countBad)


# Programme de lancement
if __name__ == '__main__':
    prog()
