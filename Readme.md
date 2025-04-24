# Tic-Tac-Toe Game

## About the Game
Tic-Tac-Toe, the classic game of strategy and skill, now comes to life with an intuitive **GUI**, multiplayer and AI modes, and dynamic difficulty settings. Play against a friend or challenge a smart AI that learns and adapts!

## Features
 **Multiplayer & AI Modes** – Play with a friend or challenge an AI at various difficulty levels.
 **Smart AI Opponent** – AI with Easy, Medium, and Hard levels (including Minimax algorithm!).
 **Interactive GUI** – Built using **Tkinter** for a seamless experience.
 **Full-Screen Toggle** – Play in full or windowed mode.
 **Score Tracking** – Keeps records of wins, losses, and ties.

##  Technologies Used
- **Python** 
- **Tkinter** – For GUI interface.
- **Messagebox** – To display alerts.
- **Random** – For AI decision-making in easy and medium modes.
- **Math** – Used in advanced AI computations.

## Libraries Explained

###  **Tkinter** – The Magic Behind the Interface 
> `import tkinter as tk`
> `from tkinter import messagebox`

Tkinter is Python’s built-in **Graphical User Interface (GUI)** library. It's used to:
- Create buttons, labels, and game layout.
- Handle user interactions like clicking and entering inputs.
- Display message boxes for game results.

###  **Random** – The Brain Behind the AI’s ‘Randomness’
> `import random`

- Used for the **Easy AI** to randomly choose a move.
- Helps **Medium AI** make unpredictable decisions.

### **Math** – The Secret Behind AI’s Intelligence 
> `import math`

- Used in the **Minimax algorithm** for Hard AI.
- Calculates the best move for AI by evaluating possible future moves.

## How to Play
1. **Run the game** :
   ```bash
   python tic_tac_toe.py
   ```
2. **Select Game Mode** – Play against a friend or AI.
3. **Choose Difficulty** (for AI mode).
4. **Make Your Move** – Click on the grid to place 'X' or 'O'.
5. **Win the Game!** – Get three in a row, column, or diagonal.

## Screenshots
![image](https://github.com/user-attachments/assets/ba7847e0-7107-4731-b8f8-42335a396052)

##  Future Enhancements
-  Add more themes and customizable board colors.
-  Sound effects for an immersive experience.
- Leaderboard to track player stats.

## License
This project is licensed under the **MIT License**.
