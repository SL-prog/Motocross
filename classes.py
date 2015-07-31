#-------------------------------------------------------------------------------
# Name:        class
#
# Author:      sl-prog
#
# Licence:     <GNU GENERAL PUBLIC LICENSE>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *

from random import randint

class WorldPart:
    def __init__(self, GRASS, GROUND, position):
        self.imggrass = pygame.image.load(GRASS)
        self.imgground = pygame.image.load(GROUND)
        self.position = position
        self.hauteur = 20
        self.prevgen = 0
        self.nextgen = 0
        self.rect = pygame.Rect((self.position*15,(self.hauteur+1)*15, 15, (35-self.hauteur)*15))

    def mouvement(self, droite, hauteurlast):
        self.rect = pygame.Rect((self.position*15,(self.hauteur+1)*15, 15, (35-self.hauteur)*15))
        if droite == True:
            self.position -= 1
            if self.position == -1:
                self.position = 49
                self.generate(hauteurlast)
        return self.hauteur

    def generate(self, hauteurlast):
        self.hauteur = hauteurlast + randint(-1,1)
        if self.hauteur <= 10:
            self.hauteur = 10
        if self.hauteur >= 30:
            self.hauteur = 30

    def affiche(self, fenetre):

        posxaffiche = (self.position*15)
        posyaffiche = (self.hauteur*15)
        fenetre.blit(self.imggrass, (posxaffiche,posyaffiche))
        for i in range(34-self.hauteur):
            fenetre.blit(self.imgground, (posxaffiche,((self.hauteur+i+1)*15)))
        #pygame.draw.rect(fenetre, (255,0,0), (self.position*15,(self.hauteur+1)*15, 15, (35-self.hauteur)*15))

class Wheel(pygame.sprite.Sprite):

    def __init__(self, fichier, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.parterre = False
        self.vitesse_y = 15
        self.vitesse_saut = 15
        self.gravite = 0.01
        self.depart_timer, self.fin_timer = False, False
        self.sauter = 0

        self.fichier = fichier
        self.image = pygame.image.load(self.fichier).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


    def affiche(self, fenetre):
        fenetre.blit(self.image, self.rect)
        #pygame.draw.rect(fenetre, (0,255,0), (self.rect.x,self.rect.y,50,50))



    def mouvement(self, saut):
        if not(self.parterre):
            self.vitesse_y += self.gravite  #appliquer la gravite
			     #limiter attraction maximale
            if self.vitesse_y > 10:
                self.vitesse_y = 10
            self.rect.y += self.vitesse_y

    def collision(self, rectangle):
        if rectangle.colliderect(self.rect):
            self.rect.y = rectangle.y-60
            self.parterre = True
            print("lol")
        else:
            self.parterre=False


