import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400

class Game(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=WIDTH, height=HEIGHT, bg='white')
        self.pack()
        self.player_size = 50
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT - self.player_size - 10
        self.player = self.create_rectangle(self.player_x, self.player_y,
                                            self.player_x + self.player_size,
                                            self.player_y + self.player_size,
                                            fill='blue')

        self.enemies = []
        self.enemy_size = 50
        self.enemy_speed = 5

        self.bind_all('<Left>', self.move_left)
        self.bind_all('<Right>', self.move_right)

        self.game_over = False
        self.spawn_enemy()
        self.move_enemies()
    
    def move_left(self, event):
        if self.player_x > 0:
            self.player_x -= 20
            self.coords(self.player, self.player_x, self.player_y,
                        self.player_x + self.player_size, self.player_y + self.player_size)
    
    def move_right(self, event):
        if self.player_x < WIDTH - self.player_size:
            self.player_x += 20
            self.coords(self.player, self.player_x, self.player_y,
                        self.player_x + self.player_size, self.player_y + self.player_size)

    def spawn_enemy(self):
        if self.game_over:
            return
        x = random.randint(0, WIDTH - self.enemy_size)
        enemy = self.create_rectangle(x, 0, x + self.enemy_size, self.enemy_size, fill='red')
        self.enemies.append(enemy)
        self.after(1000, self.spawn_enemy)

    def move_enemies(self):
        if self.game_over:
            return
        to_remove = []
        for enemy in self.enemies:
            self.move(enemy, 0, self.enemy_speed)
            pos = self.coords(enemy)
            # Проверка столкновения с игроком
            if self.check_collision(pos):
                self.game_over = True
                self.create_text(WIDTH//2, HEIGHT//2, text="Game Over", font=("Arial", 30), fill="black")
                return
            # Удаляем врагов, вышедших за экран
            if pos[1] > HEIGHT:
                to_remove.append(enemy)
        for enemy in to_remove:
            self.delete(enemy)
            self.enemies.remove(enemy)
        self.after(50, self.move_enemies)

    def check_collision(self, enemy_pos):
        px1, py1, px2, py2 = self.coords(self.player)
        ex1, ey1, ex2, ey2 = enemy_pos
        # Проверяем пересечение прямоугольников
        if (px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1):
            return True
        return False

root = tk.Tk()
root.title("Уворачиваемся от квадратов на tkinter")
game = Game(root)
root.mainloop()
