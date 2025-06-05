import pygame
import random
import sys
import os

# --- Настройки ---
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0),
(0, 200, 0), (200, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Словоместка (анаграмма)")
font = pygame.font.SysFont("arial", 48)
input_font = pygame.font.SysFont("arial", 36)

# --- Загрузка слов из файла ---
def load_words(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден!")
        sys.exit()
    with open(filename, "r", encoding="utf-8") as f:
        words = [line.strip().upper() for line in f if line.strip()]
    return words

WORDS = load_words("words.txt")
original_word = random.choice(WORDS)
shuffled_word = ''.join(random.sample(original_word,
                                       len(original_word)))

# --- Ввод ---
user_input = ""
result = ""

# --- Отрисовка ---
def draw():
    screen.fill(WHITE)

    # Перемешанное слово
    anagram_text = font.render(f"Слово: {shuffled_word}", True, BLACK)
    screen.blit(anagram_text, (WIDTH//2 - anagram_text.get_width()//2, 100))

    # Ввод игрока
    input_text = input_font.render(f"Ввод: {user_input}", True, BLACK)
    screen.blit(input_text, (WIDTH//2 - input_text.get_width()//2, 200))

    # Результат
    result_text = input_font.render(result, True, GREEN if result == "ПРАВИЛЬНО!" else RED)
    if result:
        screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, 300))

    pygame.display.flip()

# --- Игровой цикл ---
running = True
while running:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Ввод с клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.upper() == original_word:
                    result = "ПРАВИЛЬНО!"
                else:
                    result = "НЕВЕРНО!"
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
                result = ""
            elif event.unicode.isalpha():
                user_input += event.unicode.upper()
                result = ""

pygame.quit()
sys.exit()
