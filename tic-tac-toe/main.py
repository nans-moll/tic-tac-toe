import tkinter as tk
from tkinter import messagebox

class Morpion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TicTacToe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_board_buttons()

    def create_board_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=("Helvetica", 24),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("Gagné !", f"Le joueur {self.current_player} a gagné !")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Match nul", "La partie est nulle !")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        # Vérifie les lignes, colonnes et diagonales pour déterminer s'il y a un gagnant
        # (logique du jeu de morpion)
        return (
            self.check_row(row) or
            self.check_col(col) or
            self.check_diagonals() or
            self.check_reverse_diagonals()
        )

    def check_row(self, row):
        return all(self.board[row][col] == self.current_player for col in range(3))

    def check_col(self, col):
        return all(self.board[row][col] == self.current_player for row in range(3))

    def check_diagonals(self):
        return all(self.board[i][i] == self.current_player for i in range(3))

    def check_reverse_diagonals(self):
        return all(self.board[i][2 - i] == self.current_player for i in range(3))

    def check_draw(self):
        # Vérifie s'il y a un match nul (toutes les cases sont remplies)
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def switch_player(self):
        # Change le joueur actuel
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        # Réinitialise le jeu
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

# Crée et lance le jeu de morpion
morpion_game = Morpion()
morpion_game.run()


