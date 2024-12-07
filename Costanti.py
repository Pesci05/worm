import pygame
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
clock.tick(30)

MOVEMENT = pygame.USEREVENT+1
pygame.time.set_timer(MOVEMENT,5)
POINT = pygame.USEREVENT+2
eventPoint = pygame.event.Event(POINT)
LOSE = pygame.USEREVENT+3
eventLose = pygame.event.Event(LOSE,messaggio = 'HAI PERSO!!!!!')
