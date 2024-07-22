import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon=pygame.image.load("img/civ740.png")
pygame.display.set_icon(icon) #Установим изображение как иконку для игры

target_img=pygame.image.load("img/target.png")
target_width = 80
target_heigth = 80

target_x=random.randint(0, SCREEN_WIDTH-target_width)
target_y=random.randint(0, SCREEN_HEIGHT-target_heigth)

color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


running = True #игровой цикл
while running:
    pass

pygame.quit()
