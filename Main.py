import random

import mm
import pygame

def prog() -> None:
    count = 1
    screen : pygame.display = creerScreen()
    secret : list = creerCombinaisonSecrete()
    mm.afficherPlateau(screen)
    mm.afficherChoixCouleur(screen)
    mm.afficherSecret(screen, secret)
    while True:
        count += 1
        mm.getChoixCouleur()
        a : list = mm.construireProposition(screen, count)
        mm.afficherCombinaison(screen, a, count)
        mm.afficherResultat(screen,tuples(a,secret),count)
        print(determinerVictoire(secret, a))
        if determinerVictoire(secret,a):
            msg = 'Vous avez gagnez ! '
            message = pygame.font.SysFont('Comic Sans MS', 30)
            screen.blit(message,(200,700))
        elif count == 17:
            msg = "Vous avez perdue ! "
            message = pygame.font.SysFont('Comic Sans MS', 30)
            screen.blit(message,(200,700))

def determinerVictoire(secret, a):
    if secret == a :
        return True
    return False

def creerScreen() -> pygame.display:
    pygame.init()
    screen : pygame.display = pygame.display.set_mode((800, 750))
    screen.fill((255, 255, 255))
    return screen

def creerCombinaisonSecrete() -> list:
    secret : list = []
    i : int
    for i in range(5):
        i = random.randint(1, 6)
        secret.append(mm.TabCouleur[i])
    return secret

def tuples(a,b) -> tuple:
    count : int = 0
    i : int
    for i in range(len(a)):
        if a[i][0] == b[i][0] and a[i][1] == b[i][1] and a[i][2] == b[i][2]:
            count += 1
    return (count, i - count)

if __name__ == '__main__':
    prog()