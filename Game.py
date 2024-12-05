import pygame
import pygame.event
from pygame.locals import *
import random
import Costanti
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
clock.tick(15)

ADD_STAR = pygame.USEREVENT+1
pygame.time.set_timer(30,ADD_STAR)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface([25,25])
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH - self.surf.get_width())/2,
                    (SCREEN_HEIGHT - self.surf.get_height())/2
            )
        )
        self.dead = False
        

    def update(self,pressedKeys):
        if pressedKeys[K_RIGHT]:
            self.rect.move_ip(1,0)
        if pressedKeys[K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressedKeys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressedKeys[K_DOWN]:
            self.rect.move_ip(0,1)
        
        if self.rect.right >= SCREEN_WIDTH:
            self.kill()
            self.dead = True
        if self.rect.left <= 0:
            self.kill()
            self.dead = True
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
            self.dead = True
        if self.rect.top <= 0:
            self.kill()
            self.dead = True
    
   

all_sprites = pygame.sprite.Group()
p = Player()

all_sprites.add(p)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            
    

    pressedKeys = pygame.key.get_pressed()
    
    p.update(pressedKeys)
    for s in all_sprites:
        screen.blit(s.surf,s.rect)

   
    pygame.display.flip()
   

pygame.quit()