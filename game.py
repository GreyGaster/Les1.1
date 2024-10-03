import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Убеги от препятствий')
clock = pygame.time.Clock()

top_boundary = 0
bottom_boundary = HEIGHT

player_width = 50    # Размер в пикселях
player_height = 50
obstacle_width = 50
obstacle_height = 50

player_speed = 16
obstacle_speed = 8
score = 0
level = 1

player1_x = WIDTH / 2 - 200
player1_y = HEIGHT / 2 - player_height / 2

player2_x = 100
player2_y = HEIGHT / 2 - player_height / 2

obstacle_x = WIDTH
obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)

running = True

# Отрисовка текста
def display_text(text, font_size, x, y, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

while running:

    # Отслеживание нажатия кнопки на экране
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отслеживание нажатия кнопки на клавиатуре
    keys = pygame.key.get_pressed()

    # Управление
    if keys[pygame.K_UP] and player1_y > top_boundary:
        player1_y -= player_speed
    if keys[pygame.K_DOWN] and player1_y < bottom_boundary - player_height:
        player1_y += player_speed
    '''
    if keys[pygame.K_LEFT] and player_x > top_boundary:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < bottom_boundary - player_height:
        player_x += player_speed
    '''

    if keys[pygame.K_w] and player2_y > top_boundary:
        player2_y -= player_speed
    if keys[pygame.K_s] and player2_y < bottom_boundary - player_height:
        player2_y += player_speed

    obstacle_x -= obstacle_speed
    if obstacle_x + obstacle_width < 0:
        obstacle_x = WIDTH
        obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)
        score += 1
        if score % 5 == 0:
            level += 1
            player_speed += 2
            obstacle_speed += 4

    if player1_x + player_width > obstacle_x and player1_x < obstacle_x + obstacle_width and player1_y + player_height > obstacle_y and player1_y < obstacle_y + obstacle_height:
        running = False

    if player2_x + player_width > obstacle_x and player2_x < obstacle_x + obstacle_width and player2_y + player_height > obstacle_y and player2_y < obstacle_y + obstacle_height:
        running = False
    # Обновление

    # Визуализация
    screen.fill(BLUE)

    pygame.draw.rect(screen, WHITE, [player1_x, player1_y, player_width, player_height])  # Персонаж
    pygame.draw.rect(screen, BLACK, [player2_x, player2_y, player_width, player_height])
    pygame.draw.rect(screen, RED, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])

    display_text(f'Score: {score}', 25, 10, 10, GREEN)
    display_text(f'Level: {level}', 25, 10, 40, GREEN)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
