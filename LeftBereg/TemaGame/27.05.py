import pygame
import random
import sys
# --- Настройки ---
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WORDS = ["РОССИЯ"]
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Виселица — ввод с клавиатуры")
font = pygame.font.SysFont('arial', 40)
# Выбор слова
word = random.choice(WORDS)
guessed = []
wrong = 0
max_wrong = 6
# Отрисовка виселицы
def draw_hangman(errors):
    if errors > 0: pygame.draw.circle(screen, BLACK, (600, 200), 30, 3)           # голова
    if errors > 1: pygame.draw.line(screen, BLACK, (600, 230), (600, 330), 3)     # тело
    if errors > 2: pygame.draw.line(screen, BLACK, (600, 250), (560, 300), 3)     # левая рука
    if errors > 3: pygame.draw.line(screen, BLACK, (600, 250), (640, 300), 3)     # правая рука
    if errors > 4: pygame.draw.line(screen, BLACK, (600, 330), (570, 400), 3)     # левая нога
    if errors > 5: pygame.draw.line(screen, BLACK, (600, 330), (630, 400), 3)     # правая нога

    # Виселица
    pygame.draw.line(screen, BLACK, (500, 100), (500, 400), 5)
    pygame.draw.line(screen, BLACK, (500, 100), (600, 100), 5)
    pygame.draw.line(screen, BLACK, (600, 100), (600, 170), 5)
    pygame.draw.line(screen, BLACK, (450, 400), (550, 400), 5)

# Игровой цикл
running = True
while running:
    screen.fill(WHITE)

    # Слово
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = font.render(display_word.strip(), True, BLACK)
    screen.blit(text, (100, 200))

    # Виселица
    draw_hangman(wrong)

    # Победа / поражение
    won = all([l in guessed for l in word])
    lost = wrong >= max_wrong
    if won:
        msg = font.render("Вы победили! Слово: " + word, True, (0, 128, 0))
        screen.blit(msg, (100, 100))
    elif lost:
        msg = font.render("Вы проиграли! Было слово: " + word, True, 
                          (200, 0, 0))
        screen.blit(msg, (100, 100))

    pygame.display.flip()
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Ввод с клавиатуры
        if event.type == pygame.KEYDOWN and not won and not lost:
            if event.unicode.isalpha():
                char = event.unicode.upper()
                if char not in guessed:
                    if char in word:
                        guessed.append(char)
                    else:
                        guessed.append(char)
                        wrong += 1

pygame.quit()
sys.exit()
