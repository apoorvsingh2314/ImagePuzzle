from tkinter.tix import WINDOW
from turtle import Screen, window_width
import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
Screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Puzzle Game')

FPS = 10
clock = pygame.time.Clock()

WHITE =(255, 255, 255)
RED =(255 , 0 , 0)
BLACK =(0, 0, 0)
ORANGE =(255, 127, 0)
CRIMSON =(220, 20, 60)


bg = pygame.image.load( 'elephant.jpg' or 'IITM.jpg')
bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Screen.fill(WHITE)
    Screen.blit(bg,bg_rect)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()