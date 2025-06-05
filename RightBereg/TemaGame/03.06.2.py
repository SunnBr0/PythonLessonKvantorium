import pygame
import random
# --- Инициализация ---
pygame.init()
WIDTH, HEIGHT = 800, 300
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run")
# --- Цвета ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_Y = HEIGHT - 50
# --- Игрок ---
dino = pygame.Rect(50, GROUND_Y - 40, 40, 40)
dino_vel_y = 0
jumping = False
gravity = 1
# --- Препятствия ---
obstacles = []
obstacle_timer = 0
obstacle_delay = 60
# --- Игра ---
font = pygame.font.SysFont("arial", 24)
score = 0
game_over = False
speed = 7
max_speed = 20
clock = pygame.time.Clock()
# --- Анимация динозавра ---
step = 0
# --- Тряска экрана ---
shake = 0
# --- Основной цикл ---
running = True
while running:
    dt = clock.tick(60)
    win.fill(WHITE if shake == 0 else (255, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if not game_over:
        # Прыжок
        if keys[pygame.K_SPACE] and not jumping:
            dino_vel_y = -15
            jumping = True
        # Гравитация
        dino.y += dino_vel_y
        dino_vel_y += gravity
        # Приземление
        if dino.y >= GROUND_Y - dino.height:
            dino.y = GROUND_Y - dino.height
            jumping = False
        # Препятствия
        obstacle_timer += 1
        if obstacle_timer > obstacle_delay:
            obstacle_timer = 0
            h = random.choice([30, 40, 50])
            w = random.randint(20, 40)
            obstacle = pygame.Rect(WIDTH, GROUND_Y - h, w, h)
            obstacles.append(obstacle)
        for obs in obstacles:
            obs.x -= speed
        obstacles = [obs for obs in obstacles if obs.right > 0]
        # Увеличение скорости
        if score % 500 == 0 and score != 0:
            speed = min(max_speed, speed + 1)
            obstacle_delay = max(30, obstacle_delay - 3)
        # Столкновение
        for obs in obstacles:
            if dino.colliderect(obs):
                game_over = True
                shake = 10
        # Счёт
        score += 1
        # Анимация динозавра
        step = (step + 1) % 20
    else:
        if keys[pygame.K_r]:
            # Перезапуск
            dino.y = GROUND_Y - dino.height
            dino_vel_y = 0
            jumping = False
            obstacles.clear()
            score = 0
            speed = 7
            obstacle_delay = 60
            game_over = False
            shake = 0
    # Отрисовка земли
    pygame.draw.line(win, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 2)
    # Отрисовка динозавра
    if step < 10:
        pygame.draw.rect(win, (0, 120, 255), dino)
    else:
        pygame.draw.rect(win, (0, 100, 200), dino)
    # Препятствия
    for obs in obstacles:
        pygame.draw.rect(win, (0, 200, 0), obs)
    # Счёт
    score_text = font.render(f"Score: {score // 10}", True, BLACK)
    win.blit(score_text, (10, 10))
    # Game Over
    if game_over:
        msg = font.render("Game Over! Press R to Restart", True, BLACK)
        win.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
    if shake > 0:
        shake -= 1
    pygame.display.update()
pygame.quit()
