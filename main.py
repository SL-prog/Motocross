#-------------------------------------------------------------------------------
# Name:        Motocross
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
pygame.init()

from constantes import *
import classes

fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_icon(pygame.image.load(icon).convert_alpha())
pygame.display.set_caption(titre_fenetre)

part = [0]*50
for number in range(50):
        part[number] = classes.WorldPart(GRASS, GROUND, number)

hauteurlast = 20

roue1 = classes.Wheel(WHEEL, 20,200)
roue2 = classes.Wheel(WHEEL, 120,200)

jeu = True
while jeu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                jeu = False

            if event.key == pygame.K_RIGHT:
                droite = True
            if event.key == pygame.K_SPACE:
                saut=True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                droite = False
            if event.key == pygame.K_SPACE:
                saut=False

    fenetre.blit(SKY, (0,0))

    roue1.mouvement(saut)
    roue2.mouvement(saut)
    for number in range(50):
        hauteurlast = part[number].mouvement(droite, hauteurlast)
        if part[number].position < 12:
            roue1.collision(part[number].rect)
            roue2.collision(part[number].rect)
        part[number].affiche(fenetre)

    print(roue1.parterre)

    roue1.affiche(fenetre)
    roue2.affiche(fenetre)
    pygame.draw.line(fenetre, (0,0,0), roue1.rect.center,  (roue1.rect.x+45,roue1.rect.y-20), 5)
    pygame.draw.line(fenetre, (0,0,0), roue2.rect.center,  (roue1.rect.x+105,roue1.rect.y-20), 5)
    fenetre.blit(MOTO, (roue1.rect.x,roue1.rect.y-50))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
