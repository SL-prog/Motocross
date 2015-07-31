#-------------------------------------------------------------------------------
# Name:        constantes
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
pygame.init()

#Dimension ecran
largeur_ecran = 750
hauteur_ecran = 525


#Titre ecran
titre_fenetre = 'Motocross'
icon = "icon.png"

WHEEL = "wheel.png"

SKY = pygame.image.load("sky.png")

GRASS = "grass.png"
GROUND = "ground.png"

MOTO = pygame.image.load("moto.png")

droite = False
saut = False
