from player import Player
from monster import Monster
import pygame

class Game:
    
    def __init__(self):
        #generer le joueur
        self.player=Player()
        
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()

        # list des touches pressé
        self.pressed={}
        
        # création d un monstre au chargement du jeu
        self.spawn_monster();
        
    def spawn_monster(self):
        # creation d un monstre
        monster = Monster()
        # ajout du monstre a la liste des monstre
        self.all_monsters.add(monster)
    