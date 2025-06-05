import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH = 800
HEIGHT = 800  # Увеличили высоту для лучшего обзора дороги
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гоночная игра с движением вперед")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Дорожная разметка
road_width = 600
road_x = (WIDTH - road_width) // 2

# Класс игрока
class Player:
    def __init__(self):
        self.width = 60
        self.height = 100
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 20
        self.speed_x = 0
        self.speed_y = 0
        self.max_speed = 10
        self.acceleration = 0.1
        self.deceleration = 0.05
        self.score = 0
        
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
    
    def update(self):
        # Движение по X
        self.x += self.speed_x
        
        # Движение по Y (вперед/назад)
        self.y -= self.speed_y
        
        # Ограничения движения
        if self.x < road_x:
            self.x = road_x
        if self.x > road_x + road_width - self.width:
            self.x = road_x + road_width - self.width
            
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height
            
        # Постепенное замедление
        if abs(self.speed_x) > 0:
            self.speed_x *= 0.95
        if abs(self.speed_y) > 0:
            self.speed_y *= 0.95
            
        # Полная остановка при очень малой скорости
        if abs(self.speed_x) < 0.1:
            self.speed_x = 0
        if abs(self.speed_y) < 0.1:
            self.speed_y = 0

# Класс препятствий
class Enemy:
    def __init__(self, player_y):
        self.width = 60
        self.height = 100
        self.x = random.randint(road_x, road_x + road_width - self.width)
        self.y = -self.height
        self.speed = random.randint(3, 7)
        self.base_speed = self.speed
        self.player_y = player_y
        
    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y,
                                         self.width, self.height))
    def update(self, player_speed_y):
        # Учитываем скорость игрока для относительного движения
        self.y += self.base_speed + player_speed_y * 0.5
        return self.y > HEIGHT
# Класс дорожной разметки
class RoadMark:
    def __init__(self, y):
        self.width = 10
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = y
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 
                                         self.width, self.height))
    
    def update(self, speed):
        self.y += speed
        if self.y > HEIGHT:
            self.y = -self.height
            return True
        return False

# Класс игры
class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.road_marks = []
        self.last_enemy_time = time.time()
        self.enemy_interval = 1.5
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        
        # Создаем начальную разметку
        for i in range(0, HEIGHT, 100):
            self.road_marks.append(RoadMark(i))
    
    def spawn_enemy(self):
        if time.time() - self.last_enemy_time > self.enemy_interval:
            self.enemies.append(Enemy(self.player.y))
            self.last_enemy_time = time.time()
            self.enemy_interval = max(0.5, self.enemy_interval * 0.99)
    
    def check_collisions(self):
        player_rect = pygame.Rect(self.player.x, self.player.y, 
                                self.player.width, self.player.height)
        
        for enemy in self.enemies:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, 
                                   enemy.width, enemy.height)
            if player_rect.colliderect(enemy_rect):
                self.game_over = True
    
    def update(self):
        # Обновляем разметку дороги
        for mark in self.road_marks:
            mark.update(self.player.speed_y)
        
        # Обновляем врагов
        self.enemies = [enemy for enemy in self.enemies if not enemy.update(self.player.speed_y)]
        
        # Добавляем очки
        self.player.score += abs(self.player.speed_y) * 0.1
        
        self.spawn_enemy()
        self.check_collisions()
        self.player.update()
    
    def draw(self):
        # Рисуем дорогу
        pygame.draw.rect(screen, GRAY, (road_x, 0, road_width, HEIGHT))
        
        # Рисуем разметку
        for mark in self.road_marks:
            mark.draw()
        
        # Рисуем игрока и врагов
        for enemy in self.enemies:
            enemy.draw()
        self.player.draw()
        
        # Очки и скорость
        score_text = self.font.render(f"Очки: {int(self.player.score)}", True, WHITE)
        speed_text = self.font.render(f"Скорость: {abs(int(self.player.speed_y))}", True, WHITE)
        screen.blit(score_text, (20, 20))
        screen.blit(speed_text, (20, 60))
        
        if self.game_over:
            game_over_text = self.font.render("ИГРА ОКОНЧЕНА! Нажмите R для рестарта", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2))

# Основной игровой цикл
def main():
    game = Game()
    running = True
    
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game.game_over:
                    game = Game()  # Рестарт игры
        
        if not game.game_over:
            keys = pygame.key.get_pressed()
            # Управление
            if keys[pygame.K_LEFT]:
                game.player.speed_x -= 0.5
            if keys[pygame.K_RIGHT]:
                game.player.speed_x += 0.5
            if keys[pygame.K_UP]:  # Движение вперед
                game.player.speed_y += 0.6
                if game.player.speed_y > game.player.max_speed:
                    game.player.speed_y = game.player.max_speed
            if keys[pygame.K_DOWN]:  # Движение назад
                game.player.speed_y -= 0.6
                if game.player.speed_y < -game.player.max_speed / 2:
                    game.player.speed_y = -game.player.max_speed / 2
            game.update()
        game.draw()
        pygame.display.flip()
        game.clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()