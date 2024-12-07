import pygame
import pygame.event
from pygame.locals import *
import random
from Costanti import *
from tkinter import messagebox
pygame.init()




class Player(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super(Player,self).__init__()
        self.v = False
        self.points = 0
        self.x = 1
        self.y = 0
        self.surf = pygame.Surface([width,height])
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH - self.surf.get_width())/2,
                    (SCREEN_HEIGHT - self.surf.get_height())/2
            )
        )

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
            pygame.event.post(eventLose)
        if self.rect.left <= 0:
            pygame.event.post(eventLose)
        if self.rect.bottom >= SCREEN_HEIGHT:
            pygame.event.post(eventLose)
        if self.rect.top <= 0:
            pygame.event.post(eventLose)
    

class Punto(pygame.sprite.Sprite):
        def __init__(self):
            super(Punto,self).__init__()
            self.surf = pygame.Surface([15,15])
            self.surf.fill((255,255,255))
            self.rect = self.surf.get_rect(
                center=(
                        random.randint(0,SCREEN_WIDTH),
                        random.randint(0,SCREEN_HEIGHT)
                )
            )
        


player = pygame.sprite.Group()
width = 25
height = 25
p = Player(width,height)
point = Punto()

player.add(point)

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
        
        elif event.type == POINT:
            point = Punto()
        
        elif event.type == LOSE:
            messagebox.showinfo("SNAKE",event.messaggio)
            pygame.quit()

    if pygame.sprite.collide_rect(point,p):
        point.kill()

        if p.v is True:
            height += 10
        else:
            width += 10
        p = Player(width,height)

        
        pygame.event.post(eventPoint)
       

    screen.fill((0, 0, 0))
    screen.blit(p.surf,p.rect)
    screen.blit(point.surf,point.rect)

    pygame.display.flip()
   

pygame.quit()