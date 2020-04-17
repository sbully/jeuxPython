# -*- coding: utf-8 -*-
import pygame

class Mummy(pygame.sprite.Sprite):
    
    def __init__(self):
        self.health=20
        self.maxhealth=20
        self.attack=5
        self.velocity=3
        self.image=pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x=400
        self.rect.y=1080

    def moveleft(self):
        self.rect.x-=self.velocity
        