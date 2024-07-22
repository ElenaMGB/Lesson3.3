import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/imgRPG.png")
# Установим изображение как иконку для игры
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height-5)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Инициализируем счетчик очков
score = 0

# игровой цикл
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1  # Увеличиваем счетчик очков при попадании
    screen.blit(target_img, (target_x, target_y))

    # Отображаем счетчик очков на экране
    font = pygame.font.Font(None, 36)
    text = font.render(f"Счет: {score}", True, (128, 0, 0))
    text_rect = text.get_rect(topright=(SCREEN_WIDTH - 10, 10))  # Позиция в правом верхнем углу
    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
