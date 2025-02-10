import tkinter as tk
from tkinter import messagebox
import random
import math

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")

        self.board = ['' for _ in range(9)]  # Initialize empty board
        self.turn = 'X'  # X starts first
        self.game_over = False
        self.mode = None  # Game mode (None, 'multiplayer', 'ai')
        self.difficulty = 'Easy'  # Default AI difficulty
        self.scores = {'X': 0, 'O': 0, 'Ties': 0}  # Score tracking

        # Set up the GUI
        self.buttons = [tk.Button(root, text='', width=10, height=3, font=('normal', 20), command=lambda i=i: self.make_move(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

        self.reset_button = tk.Button(root, text="Reset", width=10, height=2, command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

        self.mode_button = tk.Button(root, text="Select Mode: Multiplayer", width=20, height=2, command=self.select_mode)
        self.mode_button.grid(row=4, column=0, columnspan=3)

        self.difficulty_button = tk.Button(root, text="Select Difficulty: Easy", width=20, height=2, command=self.select_difficulty)
        self.difficulty_button.grid(row=5, column=0, columnspan=3)

        self.resize_button = tk.Button(root, text="Toggle Full/Half Screen", width=20, height=2, command=self.toggle_resize)
        self.resize_button.grid(row=6, column=0, columnspan=3)

        self.score_label = tk.Label(root, text="Scores - X: 0, O: 0, Ties: 0", font=('normal', 15))
        self.score_label.grid(row=7, column=0, columnspan=3)

    def select_mode(self):
        if self.mode is None:
            self.mode = 'multiplayer'
            self.mode_button.config(text="Mode: Multiplayer")
        elif self.mode == 'multiplayer':
            self.mode = 'ai'
            self.mode_button.config(text="Mode: AI")
        else:
            self.mode = None
            self.mode_button.config(text="Select Mode: Multiplayer")
        self.reset_game()

    def select_difficulty(self):
        if self.difficulty == 'Easy':
            self.difficulty = 'Medium'
            self.difficulty_button.config(text="Select Difficulty: Medium")
        elif self.difficulty == 'Medium':
            self.difficulty = 'Hard'
            self.difficulty_button.config(text="Select Difficulty: Hard")
        else:
            self.difficulty = 'Easy'
            self.difficulty_button.config(text="Select Difficulty: Easy")
        self.reset_game()

    def toggle_resize(self):
        if self.root.state() == "normal":
            self.root.attributes('-fullscreen', True)  # Set to full screen
        else:
            self.root.attributes('-fullscreen', False)  # Set to half screen
            self.root.geometry("600x600")  # Default half-screen size

    def make_move(self, index):
        if self.game_over or self.board[index] != '':
            return
        
        self.board[index] = self.turn
        self.buttons[index].config(text=self.turn)
        
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.highlight_winner(winner)
            messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
            self.scores[self.turn] += 1
            self.update_score()
            self.reset_game()
            return

        if all(cell != '' for cell in self.board):
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a tie!")
            self.scores['Ties'] += 1
            self.update_score()
            self.reset_game()
            return
        
        self.turn = 'O' if self.turn == 'X' else 'X'  # Switch turn
        
        if self.mode == 'ai' and self.turn == 'O' and not self.game_over:
            self.ai_move()

    def ai_move(self):
        if self.difficulty == 'Easy':
            self.easy_ai()
        elif self.difficulty == 'Medium':
            self.medium_ai()
        else:
            self.hard_ai()

    def easy_ai(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == '']
        move = random.choice(empty_cells)
        self.board[move] = 'O'
        self.buttons[move].config(text='O')
        
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.highlight_winner(winner)
            messagebox.showinfo("Game Over", "AI wins!")
            self.scores['O'] += 1
            self.update_score()
            self.reset_game()
            return

        if all(cell != '' for cell in self.board):
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a tie!")
            self.scores['Ties'] += 1
            self.update_score()
            self.reset_game()
            return
        
        self.turn = 'X'

    def medium_ai(self):
        move = self.block_or_win('O') or self.block_or_win('X') or random.choice([i for i, cell in enumerate(self.board) if cell == ''])
        self.board[move] = 'O'
        self.buttons[move].config(text='O')
        
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.highlight_winner(winner)
            messagebox.showinfo("Game Over", "AI wins!")
            self.scores['O'] += 1
            self.update_score()
            self.reset_game()
            return

        if all(cell != '' for cell in self.board):
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a tie!")
            self.scores['Ties'] += 1
            self.update_score()
            self.reset_game()
            return
        
        self.turn = 'X'

    def hard_ai(self):
        move = self.minimax(self.board, 'O')['index']
        self.board[move] = 'O'
        self.buttons[move].config(text='O')
        
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.highlight_winner(winner)
            messagebox.showinfo("Game Over", "AI wins!")
            self.scores['O'] += 1
            self.update_score()
            self.reset_game()
            return

        if all(cell != '' for cell in self.board):
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a tie!")
            self.scores['Ties'] += 1
            self.update_score()
            self.reset_game()
            return
        
        self.turn = 'X'

    def block_or_win(self, player):
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = player
                if self.check_winner():
                    self.board[i] = ''
                    return i
                self.board[i] = ''
        return None

    def minimax(self, board, player):
        empty_cells = [i for i, cell in enumerate(board) if cell == '']
        
        if self.check_winner():
            return {'score': -1} if player == 'O' else {'score': 1}
        elif len(empty_cells) == 0:
            return {'score': 0}
        
        moves = []
        for cell in empty_cells:
            board[cell] = player
            result = self.minimax(board, 'X' if player == 'O' else 'O')
            board[cell] = ''
            moves.append({'index': cell, 'score': result['score']})
        
        if player == 'O':
            best_move = min(moves, key=lambda x: x['score'])
        else:
            best_move = max(moves, key=lambda x: x['score'])
        
        return best_move

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]
        
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != '':
                return condition
        return None

    def highlight_winner(self, winner):
        for index in winner:
            self.buttons[index].config(bg='lightgreen')

    def reset_game(self):
        self.board = ['' for _ in range(9)]
        self.turn = 'X'
        self.game_over = False
        for button in self.buttons:
            button.config(text='', bg='SystemButtonFace')
        self.mode_button.config(state='normal')

    def update_score(self):
        self.score_label.config(text=f"Scores - X: {self.scores['X']}, O: {self.scores['O']}, Ties: {self.scores['Ties']}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.geometry("600x600")  # Default half-screen size
    root.mainloop()

