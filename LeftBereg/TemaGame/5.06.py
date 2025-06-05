import pygame
import os
import random
from pygame.locals import *
# Инициализация Pygame
pygame.init()
# Настройки окна
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра Пазлы")
# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HIGHLIGHT = (255, 255, 0, 100)
# Загрузка изображения
def load_image(path, size=None):
    try:
        img = pygame.image.load(path)
        if size:
            img = pygame.transform.scale(img, size)
        return img
    except:
        # Если изображение не загружено, создаем тестовое
        img = pygame.Surface(size if size else (400, 300))
        img.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        pygame.draw.rect(img, BLACK, (0, 0, *(size if size else (400, 300))), 2)
        return img

# Класс пазла
class PuzzlePiece:
    def __init__(self, image, position, correct_pos, size):
        self.image = image
        self.rect = pygame.Rect(position, size)
        self.correct_pos = correct_pos
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.dragging:
            highlight = pygame.Surface(self.rect.size, pygame.SRCALPHA)
            highlight.fill(HIGHLIGHT)
            surface.blit(highlight, self.rect)
    
    def is_correct(self):
        return self.rect.topleft == self.correct_pos
    
    def snap_to_grid(self):
        """Примагничивание к правильной позиции, если близко"""
        snap_distance = 30
        dx = abs(self.rect.x - self.correct_pos[0])
        dy = abs(self.rect.y - self.correct_pos[1])
        if dx < snap_distance and dy < snap_distance:
            self.rect.topleft = self.correct_pos

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.dragging = True
                self.offset_x = self.rect.x - event.pos[0]
                self.offset_y = self.rect.y - event.pos[1]
                
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1 and self.dragging:
                self.dragging = False
                self.snap_to_grid()
                
        elif event.type == MOUSEMOTION and self.dragging:
            self.rect.x = event.pos[0] + self.offset_x
            self.rect.y = event.pos[1] + self.offset_y

# Основной класс игры
class PuzzleGame:
    def __init__(self):
        self.pieces = []
        self.grid_size = (4, 3)  # 4 колонки, 3 строки
        self.piece_size = (150, 150)
        self.image_path = None
        self.completed = False
        self.font = pygame.font.SysFont(None, 36)
        
        # Кнопки
        self.load_button = pygame.Rect(50, 500, 200, 50)
        self.reset_button = pygame.Rect(300, 500, 200, 50)
        self.exit_button = pygame.Rect(550, 500, 200, 50)
        
        self.load_new_image(os.path.join("images", "sample.jpg"))
    
    def load_new_image(self, path):
        self.image_path = path
        self.completed = False
        
        full_image = load_image(path, (self.grid_size[0] * self.piece_size[0], 
                                       self.grid_size[1] * self.piece_size[1]))
        
        self.pieces = []
        for row in range(self.grid_size[1]):
            for col in range(self.grid_size[0]):
                x = col * self.piece_size[0]
                y = row * self.piece_size[1]
                piece_image = full_image.subsurface((x, y, *self.piece_size))
                
                correct_pos = (150 + col * self.piece_size[0], 50 + row * self.piece_size[1])
                start_pos = (random.randint(50, WIDTH - self.piece_size[0] - 50), 
                             random.randint(50, HEIGHT - self.piece_size[1] - 100))
                
                self.pieces.append(PuzzlePiece(piece_image, start_pos, correct_pos, self.piece_size))
    
    def reset_puzzle(self):
        for piece in self.pieces:
            piece.rect.x = random.randint(50, WIDTH - self.piece_size[0] - 50)
            piece.rect.y = random.randint(50, HEIGHT - self.piece_size[1] - 100)
        self.completed = False
    
    def check_completion(self):
        self.completed = all(piece.is_correct() for piece in self.pieces)
        return self.completed
    
    def draw(self, surface):
        surface.fill(WHITE)

        # Рисуем сетку
        for row in range(self.grid_size[1]):
            for col in range(self.grid_size[0]):
                x = 150 + col * self.piece_size[0]
                y = 50 + row * self.piece_size[1]
                pygame.draw.rect(surface, GRAY, (x, y, *self.piece_size), 2)

        for piece in self.pieces:
            piece.draw(surface)
        
        pygame.draw.rect(surface, GRAY, self.load_button)
        pygame.draw.rect(surface, GRAY, self.reset_button)
        pygame.draw.rect(surface, GRAY, self.exit_button)
        
        load_text = self.font.render("Загрузить", True, BLACK)
        reset_text = self.font.render("Перемешать", True, BLACK)
        exit_text = self.font.render("Выход", True, BLACK)
        
        surface.blit(load_text, (self.load_button.x + 50, self.load_button.y + 15))
        surface.blit(reset_text, (self.reset_button.x + 40, self.reset_button.y + 15))
        surface.blit(exit_text, (self.exit_button.x + 70, self.exit_button.y + 15))
        
        if self.completed:
            completed_text = self.font.render("Пазл собран!", True, (0, 200, 0))
            surface.blit(completed_text, (WIDTH//2 - 80, 20))
    
    def handle_events(self, event):
        for piece in self.pieces:
            piece.handle_event(event)
        
        if event.type == MOUSEBUTTONUP and event.button == 1:
            if self.load_button.collidepoint(event.pos):
                try:
                    import tkinter as tk
                    from tkinter import filedialog
                    root = tk.Tk()
                    root.withdraw()
                    file_path = filedialog.askopenfilename(
                        title="Выберите изображение",
                        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
                    )
                    if file_path:
                        self.load_new_image(file_path)
                except:
                    self.load_new_image(os.path.join("images", "sample.jpg"))
            
            elif self.reset_button.collidepoint(event.pos):
                self.reset_puzzle()
            elif self.exit_button.collidepoint(event.pos):
                pygame.quit()
                exit()
        if event.type == MOUSEBUTTONUP and event.button == 1:
            self.check_completion()
# Запуск
def main():
    game = PuzzleGame()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            game.handle_events(event)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    if not os.path.exists("images"):
        os.makedirs("images")
    main()