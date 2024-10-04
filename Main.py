import random
import mm
import pygame

#Programme principale
def prog() -> None:
    count = 1
    boole = True
    screen : pygame.display = creerScreen()
    secret : list = creerCombinaisonSecrete()
    mm.afficherPlateau(screen)
    mm.afficherChoixCouleur(screen)

    #Tant que le jeu est en cours
    while True:
        count += 1
        mm.getChoixCouleur()
        a: list = mm.construireProposition(screen, count)
        boole = afficherVictoire(secret, a, screen, count)
        victory : bool = afficherVictoire(secret, a, screen, count)
        mm.afficherResultat(screen, tuples(a, secret), count)

        if victory:
            #Affiche la combinaison secréte en cas de victoire
            mm.afficherCombinaison(screen, a, count)



#Détermine le résultat de la partie
def determinerVictoire(secret: list, a: list)-> bool:
    # Regarde si la combinaison secret et similaire à la combinaison de l'utilisateur
    if secret == a :
        return True
    return False

#Affichage du résultat de la partie
def afficherVictoire(secret: list, a: list, screen: pygame.surface, count: int)-> bool:
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

#Création de l'affichage graphique
def creerScreen() -> pygame.display:
    pygame.init()
    #Taille d'affichage sur 800px de largeur et 750px de hauteur
    screen: pygame.surface = pygame.display.set_mode((800, 750))
    screen.fill((255, 255, 255))
    return screen

#Création de la combinaison secréte en aléatoire
def creerCombinaisonSecrete() -> list:
    secret : list = []
    i : int
    for _ in range(5):
        i = random.randint(1, 6)
        secret.append(mm.TabCouleur[i])
    return secret

#Fonction nb bien placé / nb mal placé
def tuples(a,b) -> tuple:
    countGood : int = 0
    countBad : int = 0
    i : int

    for i in range(len(a)):
        # Compte ceux au même endroit et de même couleur
        if a[i] == b[i] :
            countGood += 1

        # Compte ceux qui sont similaire mais pas au bon endroit
        elif a[i] in b and a[i] != b[i]:
            countBad += 1

    return (countGood,countBad)



#Programme de lancement
if __name__ == '__main__':
    prog()