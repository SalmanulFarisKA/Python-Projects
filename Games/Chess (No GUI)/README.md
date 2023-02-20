# Chess

A simple script that generates a chess game using ASCII symbols in the console. It built using the `python-chess` library. 

Inputs can be entered via [Algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) or by specifying starting and ending points (eg: "e2e4").
The opponent is a simple AI that chooses a random valid move in each turn. More advanced AIs and the option to choose difficulty will be added in the future.

<p align="center">
  <img src="https://raw.githubusercontent.com/SalmanulFarisKA/Python-Projects/main/Games/Chess%20(No%20GUI)/Chess%20No%20GUI%20demo%20image.png" alt="Chess No GUI Demo 1" width="300">
</p>

## Requirements

- Python 3.x
- python-chess library (`pip install python-chess`)

## Game Rules

The game follows standard chess rules. The player with the white pieces moves first. The game ends when one player checkmates the other, or when the game ends in a stalemate or draw.

## Code Documentation

The `chess_game.py` file contains the game code. Here is a brief documentation of the code:

### Variables

- `chess_pieces`: A dictionary mapping chess piece codes to unicode symbols.
- `board`: A `chess.Board` object representing the game board.

### Functions

#### `draw_board(board)`

This function takes a `board` object as input and prints the current state of the board to the console.

#### `play_game()`

This function runs the game loop. It first draws the board, then alternates turns between the two players. If the player is human, it prompts them for a move input. If the player is the AI, it chooses a random legal move. After each move, it redraws the board. Once the game is over, it displays the result and prompts the user if they want to play again.

#### `restart()`

This function prompts the user if they want to play again. If yes, it resets the board and calls `play_game()` again. If no, it exits the program.

### Running the Game

To run the game, simply call `play_game()` function.
