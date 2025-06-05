import pygame
import random
# Инициализация Pygame
pygame.init()
# Настройки окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Уворачиваемся от квадратов")
# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
# Игрок
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 7
# Враги
enemy_size = 50
enemy_speed = 5
enemies = []
# Таймер для появления врагов
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 800)  # каждые 800 мс создаём врага
clock = pygame.time.Clock()
running = True
def collision(rect1, rect2):
    return rect1.colliderect(rect2)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_EVENT:
            x_pos = random.randint(0, SCREEN_WIDTH - enemy_size)
            enemies.append(pygame.Rect(x_pos,
             -enemy_size, enemy_size, enemy_size))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_size))
    player_rect = pygame.Rect(player_x, player_y, 
                              player_size, player_size)
    # Двигаем врагов вниз
    for enemy in enemies:
        enemy.y += enemy_speed
    enemies = [e for e in enemies if e.y < SCREEN_HEIGHT]
    for enemy in enemies:
        if collision(player_rect, enemy):
            running = False  # Игра окончена
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    pygame.display.flip()
pygame.quit()
