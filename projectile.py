import pygame

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self,player):
        super().__init__()
        self.velocity=10
        self.player=player
        self.image=pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x=player.rect.x+(player.rect.width/2)-(self.rect.width/2)
        self.rect.y=player.rect.y+(player.rect.height/2)-(self.rect.height/2)
        self.origin_image = self.image
        self.angle=0
    

    def rotate(self):
        self.angle+=10
        self.image=pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect=self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)
    
    def move(self):
        self.rect.x +=self.velocity
        self.rotate()
        #verifier si les projectile sont présent dans l'ecran
        if self.rect.x>1080:
            self.remove()
            
        
