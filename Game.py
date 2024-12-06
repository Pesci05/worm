import pygame
import pygame.event
from pygame.locals import *
import random
from Costanti import *
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
clock.tick(30)

MOVEMENT = pygame.USEREVENT+1
pygame.time.set_timer(MOVEMENT,5)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.x = 1
        self.y = 0
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
            self.x = 1
            self.y = 0
        if pressedKeys[K_LEFT]:
            self.x = -1
            self.y = 0
        if pressedKeys[K_UP]:
            self.y = -1
            self.x = 0
        if pressedKeys[K_DOWN]:
            self.y = 1
            self.x = 0
        
        if pressedKeys is not None:
            self.rect.move_ip(self.x,self.y)

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
            
        elif event.type == MOVEMENT:
            pressedKeys = pygame.key.get_pressed()
            p.update(pressedKeys)
    
    
    

    screen.fill((0, 0, 0))
    for s in all_sprites:
        screen.blit(s.surf,s.rect)

    
   
    pygame.display.flip()
   

pygame.quit()