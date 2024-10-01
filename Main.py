import random

import mm
import pygame
def prog():
    secret = []
    count = 1
    for i in range(5):
        i = random.randint(1, 6)
        secret.append(mm.TabCouleur[i])
    pygame.init()
    screen = pygame.display.set_mode((800, 1000))
    screen.fill((255, 255, 255))
    mm.afficherPlateau(screen)
    mm.afficherChoixCouleur(screen)
    mm.afficherSecret(screen, secret)
    while True:
        count += 1
        mm.getChoixCouleur()
        a = mm.construireProposition(screen, count)
        mm.afficherCombinaison(screen, a, count)
        mm.afficherResultat(screen,tuple(a,secret),count)

def tuple(a,b):
    count = 0
    for i in range(len(a)):
        if a[i][0] == b[i][0] and a[i][1] == b[i][1] and a[i][2] == b[i][2]:
            count += 1
    return (count, i - count)







if __name__ == '__main__':
    prog()