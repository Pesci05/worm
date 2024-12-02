import pygame
import pygame.event
from pygame.locals import *
import random
import Costanti
pygame.init()

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
clock.tick(30)

ADD_STAR = pygame.USEREVENT+1
pygame.time.set_timer(30,ADD_STAR)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface([75,25])
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH - self.surf.get_width())/2,
                    SCREEN_HEIGHT - 40
            )
        )
        

    def update(self,pressedKeys):
        if pressedKeys[K_RIGHT]:
            self.rect.move_ip(1,0)
        if pressedKeys[K_LEFT]:
            self.rect.move_ip(-1,0)
        
        if self.rect.right >= SCREEN_WIDTH - 15:
            self.rect.right = SCREEN_WIDTH - 15
        if self.rect.left <= 15:
            self.rect.left = 15
    
    def fire(self):
        m = Shoot(self.rect.centerx, self.rect.bottom)
        shoots.add(m)
        all_sprites.add(m)


class Shoot(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Shoot,self).__init__()
        self.surf = pygame.Surface([15,15])
        self.surf.fill([255,255,255])
        self.rect = self.surf.get_rect(
            center=(x,y)
        )
        self.speed = 3

    def update(self):
        self.rect.move_ip(0,-self.speed)

        if self.rect.top <= 0:
            self.kill()

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star,self).__init__()
        self.surf = pygame.surface.Surface([10,10])
        self.surf.fill([255,255,255])
        self.rect = self.surf.get_rect(
            center = (random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT))
        )
    
    def update(self):
        self.rect.move_ip(0,-1)

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Enemy,self).__init__()
        self.surf = pygame.surface.Surface([50,25])
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center = (x+self.surf.get_width(),15)
        )

p = Player()
shoots = pygame.sprite.Group()
enemies = pygame.sprite.Group()
stars = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(p)

x= 10
for i in range(10):
    e = Enemy(x+10,x)
    enemies.add(e)
    print(e.rect)
    x = x + e.surf.get_width()/2 

all_sprites.add(enemies)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_SPACE:
                p.fire()
        elif event.type == ADD_STAR:
            s = Star()
            stars.add(s)
            

    pressedKeys = pygame.key.get_pressed()
    p.update(pressedKeys)
   

    for s in shoots:
        s.update() 
    
    for s in stars:
        s.update()

    screen.fill([0,0,0])
    for s in all_sprites:
        screen.blit(s.surf, s.rect)

   
    pygame.display.flip()
   

pygame.quit()