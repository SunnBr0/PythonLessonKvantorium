import arcade
import random
import os

# Настройки игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Гоночная игра на Arcade"
PLAYER_SPEED = 5
ENEMY_SPEED = 3
LANE_COUNT = 3
LANE_WIDTH = SCREEN_WIDTH // LANE_COUNT

class Car(arcade.Sprite):
    def __init__(self, filename, scale, lane):
        super().__init__(filename, scale)
        self.lane = lane
        self.center_x = lane * LANE_WIDTH + LANE_WIDTH // 2
        self.center_y = 0 if "enemy" in filename else SCREEN_HEIGHT - 100

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Путь к ресурсам
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # Спрайты
        self.player = None
        self.enemies = None
        self.score = 0
        self.game_over = False
        self.background = None
        
    def setup(self):
        # Игрок
        self.player = Car("images/PlayerCar.jpg", 0.5, 1)
        
        # Враги
        self.enemies = arcade.SpriteList()
        for i in range(5):
            lane = random.randint(0, LANE_COUNT - 1)
            enemy = Car("images/PlayerCar.jpg", 0.5, lane)
            enemy.center_y = random.randint(-300, -100)
            self.enemies.append(enemy)
        
        # Фон
        self.background = arcade.load_texture("images/Phone.jpg")
        self.score = 0
        
    def on_draw(self):
        arcade.start_render()
        
        # Рисуем фон
        arcade.draw_lbwh_rectangle_filled(
            0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background
        )
        
        # Рисуем машины
        self.player.draw()
        self.enemies.draw()
        
        # Рисуем счет
        arcade.draw_text(
            f"Счет: {self.score}",
            10, SCREEN_HEIGHT - 30,
            arcade.color.WHITE, 20
        )
        
        # Если игра окончена
        if self.game_over:
            arcade.draw_rectangle_filled(
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                400, 200, arcade.color.BLACK
            )
            arcade.draw_text(
                "ИГРА ОКОНЧЕНА!",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40,
                arcade.color.RED, 40,
                anchor_x="center"
            )
            arcade.draw_text(
                f"Финальный счет: {self.score}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20,
                arcade.color.WHITE, 24,
                anchor_x="center"
            )
            arcade.draw_text(
                "Нажмите R для рестарта",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60,
                arcade.color.WHITE, 20,
                anchor_x="center"
            )
    
    def on_update(self, delta_time):
        if self.game_over:
            return
            
        # Двигаем врагов
        for enemy in self.enemies:
            enemy.center_y += ENEMY_SPEED
            
            # Если враг уехал за экран
            if enemy.center_y > SCREEN_HEIGHT:
                enemy.center_y = random.randint(-300, -100)
                enemy.lane = random.randint(0, LANE_COUNT - 1)
                enemy.center_x = enemy.lane * LANE_WIDTH + LANE_WIDTH // 2
                self.score += 1
        
        # Проверяем столкновения
        if arcade.check_for_collision_with_list(self.player, self.enemies):
            self.game_over = True
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT and self.player.lane > 0:
            self.player.lane -= 1
            self.player.center_x = self.player.lane * LANE_WIDTH + LANE_WIDTH // 2
        elif key == arcade.key.RIGHT and self.player.lane < LANE_COUNT - 1:
            self.player.lane += 1
            self.player.center_x = self.player.lane * LANE_WIDTH + LANE_WIDTH // 2
        elif key == arcade.key.R and self.game_over:
            self.setup()
            self.game_over = False

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()