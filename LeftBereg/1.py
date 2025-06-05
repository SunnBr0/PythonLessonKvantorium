import pygame
import random
import sys
# Инициализация
pygame.init()
# Размеры экрана
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Уклоняйся от блоков")
# Цвета
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
# Игрок
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size - 10]
player_speed = 7
# Блок
block_size = 50
block_pos = [random.randint(0, WIDTH - block_size), 0]
block_speed = 5
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

score = 0

def detect_collision(player_pos, block_pos):
    px, py = player_pos
    bx, by = block_pos

    if (bx < px < bx + block_size or bx < px + player_size < bx + block_size) and \
       (by < py < by + block_size or by < py + player_size < by + block_size):
        return True
    return False

# Главный цикл
running = True
while running:
    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Движение блока
    block_pos[1] += block_speed

    if block_pos[1] > HEIGHT:
        block_pos[1] = 0
        block_pos[0] = random.randint(0, WIDTH - block_size)
        score += 1
        block_speed += 0.3  # Увеличиваем скорость со временем

    # Проверка столкновения
    if detect_collision(player_pos, block_pos):
        text = font.render("Игра окончена! Счёт: " + str(score), True, RED)
        screen.blit(text, (50, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # Рисуем
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, RED, (*block_pos, block_size, block_size))

    # Счёт
    score_text = font.render("Счёт: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
