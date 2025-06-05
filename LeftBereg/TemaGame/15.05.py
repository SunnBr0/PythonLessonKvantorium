import pygame
import random
import sys
# Инициализация Pygame
pygame.init()
# Параметры экрана
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
# Шрифт
font = pygame.font.SysFont("Arial", 25)
# Змейка
snake = [[100, 100]]
snake_dir = (CELL_SIZE, 0)  # вправо
snake_speed = 10
# Еда
food = [random.randrange(0, WIDTH, CELL_SIZE), 
        random.randrange(0, HEIGHT, CELL_SIZE)]
clock = pygame.time.Clock()
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, 
        (*segment, CELL_SIZE, CELL_SIZE))
def game_over():
    text = font.render("Игра окончена!", True, RED)
    screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()
# Главный игровой цикл
while True:
    clock.tick(snake_speed)
    screen.fill(BLACK)
    # Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # Движение змейки
    new_head = [snake[0][0] + snake_dir[0], 
                snake[0][1] + snake_dir[1]]
    snake.insert(0, new_head)

    # Проверка съедания еды
    if snake[0] == food:
        food = [random.randrange(0, WIDTH,CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)]
    else:
        snake.pop()

    # Проверка столкновений
    if (
        new_head in snake[1:] or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        game_over()

    # Рисуем змейку и еду
    draw_snake(snake)
    pygame.draw.rect(screen, RED, 
        (*food, CELL_SIZE, CELL_SIZE))

    pygame.display.update()