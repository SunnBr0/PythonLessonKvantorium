class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    def make_move(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        return False
    def check_winner(self):
        # Проверка строк
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        row = int(input(f"{self.name}, enter the row (0, 1, or 2): "))
        col = int(input(f"{self.name}, enter the column (0, 1, or 2): "))
        return row, col

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            row, col = current_player.get_move()

            if self.board.make_move(row, col, current_player.symbol):
                winner = self.board.check_winner()
                if winner:
                    self.board.display()
                    print(f"{winner} wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a tie!")
                    break
                else:
                    self.current_player_index = 1 - self.current_player_index
            else:
                print("Invalid move. Try again.")

# Запуск игры

player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")
game = Game(player1, player2)
game.play()