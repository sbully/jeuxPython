import pygame
pygame.init()

from game import Game


#generer la fenetre de jeu
pygame.display.set_caption("Comet fall Game")
screen=pygame.display.set_mode((1080,720))

#chargement du background
background = pygame.image.load("assets/bg.jpg")

#chargement du joueur
game = Game()



running = True

#def dispatcher(key):
#    return{
#            pygame.K_RIGHT : moveRight,
#            pygame.K_LEFT : moveLeft,
#            pygame.K_UP : moveUp,
#            pygame.K_SPACE : moveSpace
#            }.get(key,defaultEvent)()
#            
#def moveRight():
#    game.player.move_right()
#    print("deplacement à droite")
#    
#def moveLeft():
#    game.player.move_left()
#    print("deplacement à gauche")
#    
#def moveUp():
#    print("deplacement en haut")    
#    
#def moveSpace():
#    print('jump')
#    
#def defaultEvent():
#    print("Event Default")


while running:
    #appliquer la fenetre de jeu
    screen.blit(background,(0,-200))
    
    #appliquer l'image du joueur
    screen.blit(game.player.image,game.player.rect)
    
    #screen.blit(game.)
    
    #recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    #appliquer l ensemble des images du groupe projectiles
    game.player.all_projectiles.draw(screen)
    
    
    #appliquer l ensemble des images du groupe de monsters
    game.all_monsters.draw(screen)
    
    #mettre a jour l ecran
    pygame.display.flip()

    #print(game.pressed)
    
    if game.pressed.get(pygame.K_RIGHT)and game.player.rect.x < (screen.get_width()-game.player.rect.width):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
         game.player.move_left()

    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        elif event.type==pygame.KEYDOWN: 
            game.pressed[event.key]= True
            
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type==pygame.KEYUP:
            game.pressed[event.key]=False
            
            #dispatcher(event.key)
        #evenement de fermeture de la fenetre
#        if event.type== pygame.QUIT:
#            running=False
#            pygame.quit()
#        #detecter si un joueur relache une touche
#        elif event.type == pygame.KEYDOWN:
#        #quel touche a ete utilisé
#            if event.key == pygame.K_RIGHT:
#                print("deplacement a droite")

