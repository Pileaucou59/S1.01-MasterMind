import random
import mm
import pygame

def prog() -> None:
    count = 1
    boole = True
    screen : pygame.display = creerScreen()
    secret : list = creerCombinaisonSecrete()
    mm.afficherPlateau(screen)
    mm.afficherChoixCouleur(screen)
    mm.afficherSecret(screen, secret)
    while True :
        count += 1
        mm.getChoixCouleur()
        a: list = mm.construireProposition(screen, count)
        boole = afficherVictoire(secret, a, screen, count)
        mm.afficherCombinaison(screen, a, count)
        mm.afficherResultat(screen, tuples(a, secret), count)
        if not boole:
            pass

            exit()






def determinerVictoire(secret: list, a: list)-> bool:
    if secret == a :
        return True
    return False

def afficherVictoire(secret : list, a : list, screen : pygame.surface, count : int)-> bool:
    if determinerVictoire(secret, a):
        msg: str = 'Vous avez gagnez !'
        message = pygame.font.SysFont('monospace', 25)
        message.set_bold(True)
        label = message.render(msg, 1, mm.Noir)
        screen.blit(label, (250, 700))
        return False
    elif count == 16:
        msg: str = "Vous avez perdue !"
        message = pygame.font.SysFont('monospace', 25)
        message.set_bold(True)
        label = message.render(msg, 1, 30)
        screen.blit(label, (250, 700))
        return False
    else:
        return True

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
        if a[i] == b[i]:
            count += 1
    return (count, i - count)



if __name__ == '__main__':
    prog()