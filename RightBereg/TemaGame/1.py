import arcade
import random

# --- Константы ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 50
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 50
PLAYER_SPEED = 5
OBSTACLE_SPEED = 5
OBSTACLE_SPAWN_RATE = 60  # каждые 60 кадров

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, arcade.color.RED)

    def update(self):
        self.y -= OBSTACLE_SPEED

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Гонки без картинок")
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        self.player_x = SCREEN_WIDTH // 2
        self.player_y = 50
        self.obstacles = []
        self.frame_count = 0
        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        if self.game_over:
            arcade.draw_text("Игра окончена", 100, SCREEN_HEIGHT // 2, arcade.color.WHITE, 30)
            return

        # Машина игрока
        arcade.draw_rectangle_filled(self.player_x, self.player_y, PLAYER_WIDTH, PLAYER_HEIGHT, arcade.color.BLUE)

        # Препятствия
        for obs in self.obstacles:
            obs.draw()

    def on_update(self, delta_time):
        if self.game_over:
            return

        self.frame_count += 1

        # Добавление новых препятствий
        if self.frame_count % OBSTACLE_SPAWN_RATE == 0:
            new_x = random.randint(OBSTACLE_WIDTH // 2, SCREEN_WIDTH - OBSTACLE_WIDTH // 2)
            self.obstacles.append(Obstacle(new_x, SCREEN_HEIGHT + OBSTACLE_HEIGHT // 2))

        # Обновление препятствий
        for obs in self.obstacles:
            obs.update()

        # Удаление ушедших вниз
        self.obstacles = [obs for obs in self.obstacles if obs.y > -OBSTACLE_HEIGHT]

        # Проверка столкновений
        for obs in self.obstacles:
            if (abs(obs.x - self.player_x) < (OBSTACLE_WIDTH + PLAYER_WIDTH) / 2 and
                abs(obs.y - self.player_y) < (OBSTACLE_HEIGHT + PLAYER_HEIGHT) / 2):
                self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT and self.player_x > PLAYER_WIDTH // 2:
            self.player_x -= PLAYER_SPEED * 10
        elif key == arcade.key.RIGHT and self.player_x < SCREEN_WIDTH - PLAYER_WIDTH // 2:
            self.player_x += PLAYER_SPEED * 10
        elif key == arcade.key.R and self.game_over:
            self.__init__()
            self.setup()

    def setup(self):
        self.obstacles = []
        self.frame_count = 0
        self.player_x = SCREEN_WIDTH // 2
        self.game_over = False

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
