import pygame
import sys
import random
import os
# --- Настройки ---
TILE_SIZE = 100
GRID_SIZE = 4
FIELD_SIZE = TILE_SIZE * GRID_SIZE
LEFT_WIDTH = FIELD_SIZE
RIGHT_WIDTH = FIELD_SIZE
WINDOW_WIDTH = LEFT_WIDTH + RIGHT_WIDTH
WINDOW_HEIGHT = FIELD_SIZE
FPS = 30
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Пятнашки: Слева оригинал, справа сборка")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 36)
# --- Загрузка картинки ---
image_path = "image.jpg"
if not os.path.exists(image_path):
    print("Файл image.jpg не найден.")
    sys.exit()
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (FIELD_SIZE, FIELD_SIZE))
# --- Создание тайлов ---
tiles = []
positions = []
correct_order = []
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        tile_image = image.subsurface(rect).copy()
        tiles.append(tile_image)
        positions.append((row, col))
        correct_order.append(tile_image)
# --- Пустая клетка ---
tiles[-1] = None
correct_order[-1] = None
blank_index = len(tiles) - 1
# --- Перемешивание ---
def shuffle():
    global blank_index
    for _ in range(1000):
        moves = get_valid_moves(blank_index)
        target = random.choice(moves)
        swap(blank_index, target)
        blank_index = target
def get_valid_moves(blank):
    row, col = positions[blank]
    moves = []
    for i, (r, c) in enumerate(positions):
        if abs(row - r) + abs(col - c) == 1:
            moves.append(i)
    return moves

def swap(i, j):
    tiles[i], tiles[j] = tiles[j], tiles[i]

def is_solved():
    return tiles == correct_order

# --- Отрисовка ---
def draw():
    screen.fill((50, 50, 50))

    # Оригинал слева
    screen.blit(image, (0, 0))

    # Игровое поле справа
    for i, tile in enumerate(tiles):
        if tile:
            x = positions[i][1] * TILE_SIZE + LEFT_WIDTH
            y = positions[i][0] * TILE_SIZE
            screen.blit(tile, (x, y))

    if is_solved():
        text = font.render("СОБРАНО!", True, (0, 255, 0))
        screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, 10))

    pygame.display.flip()

# --- Получение индекса тайла по позиции мыши ---
def get_clicked_index(pos):
    x, y = pos
    if x < LEFT_WIDTH:
        return -1  # клик по оригиналу
    col = (x - LEFT_WIDTH) // TILE_SIZE
    row = y // TILE_SIZE
    for i, (r, c) in enumerate(positions):
        if r == row and c == col:
            return i
    return -1

# --- Игра ---
shuffle()
running = True

while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif not is_solved() and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = get_clicked_index(event.pos)
            if clicked != -1 and clicked in get_valid_moves(blank_index):
                swap(clicked, blank_index)
                blank_index = clicked

    clock.tick(FPS)

pygame.quit()
sys.exit()
