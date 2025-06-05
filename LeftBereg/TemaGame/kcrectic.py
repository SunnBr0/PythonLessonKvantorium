import pygame
import sys
# Инициализация Pygame
pygame.init()
# Константы
WIDTH, HEIGHT = 600, 650  # Увеличили высоту для текста
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 200
# Цвета
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 150, 200)
# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)

# Доска
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Шрифты
font = pygame.font.SysFont('Arial', 40)
button_font = pygame.font.SysFont('Arial', 30)

# Нарисовать игровое поле
def draw_lines():
    # Горизонтальные линии
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
    # Вертикальные линии
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - BUTTON_HEIGHT - 20), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - BUTTON_HEIGHT - 20), LINE_WIDTH)

# Нарисовать фигуры
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                 (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                  int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                 CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                               (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                               (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                               CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                               (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                               (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                               CROSS_WIDTH)

# Нарисовать кнопку рестарта
def draw_button():
    button_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, HEIGHT - BUTTON_HEIGHT - 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    mouse_pos = pygame.mouse.get_pos()
    
    # Проверка наведения мыши
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)
    
    # Текст кнопки
    text = button_font.render("Новая игра", True, TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    
    return button_rect

# Нарисовать текст победителя
def draw_winner_text(winner):
    if winner == 'X':
        text = font.render("Победили Крестики!", True, CROSS_COLOR)
    elif winner == 'O':
        text = font.render("Победили Нолики!", True, CIRCLE_COLOR)
    else:
        text = font.render("Ничья!", True, TEXT_COLOR)
    
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - BUTTON_HEIGHT - 50))
    screen.blit(text, text_rect)

# Отметить ход на доске
def mark_square(row, col, player):
    board[row][col] = player

# Проверить доступность клетки
def available_square(row, col):
    return board[row][col] is None

# Проверить заполнена ли доска
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

# Проверить победу
def check_win(player):
    # Проверка по вертикали
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    # Проверка по горизонтали
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    
    # Проверка диагоналей
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

# Сбросить игру
def reset_game():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None
    screen.fill(BG_COLOR)
    draw_lines()
    return 'X'  # Первый ход всегда за крестиками

# Основная функция игры
def main():
    player = 'X'
    game_over = False
    winner = None
    
    draw_lines()
    button_rect = draw_button()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX, mouseY = event.pos
                
                # Проверка клика по доске
                if mouseY < HEIGHT - BUTTON_HEIGHT - 20:
                    clicked_row = mouseY // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE
                    
                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)
                        
                        if check_win(player):
                            game_over = True
                            winner = player
                        elif is_board_full():
                            game_over = True
                            winner = None
                        
                        player = 'O' if player == 'X' else 'X'
            
            # Обработка клика по кнопке
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                player = reset_game()
                game_over = False
                winner = None
        
        # Отрисовка
        draw_figures()
        button_rect = draw_button()
        
        if game_over:
            draw_winner_text(winner)
        
        pygame.display.update()

if __name__ == "__main__":
    main()