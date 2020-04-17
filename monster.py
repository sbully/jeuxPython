import pygame

# classe gérant la notion de monstre

class Monster(pygame.sprite.Sprite):
    
    
    def __init__(self):
        super().__init__()
        self.health=100
        self.max_health = 100
        self.attack = 5
        self.velocity =3
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect();
        self.rect.x = 400
        self.rect.y=800