import chess
import random
import time

chess_pieces = {'R': '♜',
                'N': '♞',
                'B': '♝',
                'K': '♚',
                'Q': '♛',
                'P': '♟︎',
                'r': '♖',
                'n': '♘',
                'b': '♗',
                'k': '♔',
                'q': '♕',
                'p': '♙'}

board = chess.Board()


def draw_board(board):
    chess_board = []
    for i in reversed(range(8)):  # iterate in reverse order
        row = []
        for j in reversed(range(8)):  # iterate in reverse order
            square = board.piece_at(8 * i + j)
            if square is None:
                row.append(' ')
            else:
                row.append(square.symbol().upper()
                           if square.color else square.symbol().lower())
        chess_board.append(row)

    print("    A   B   C   D   E   F   G   H")  # flip column labels
    print("  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
    for i, row in enumerate(chess_board):
        print(f"{8-i} ║ {chess_pieces.get(row[7], ' ')} │ {chess_pieces.get(row[6], ' ')} │ {chess_pieces.get(row[5], ' ')} │ {chess_pieces.get(row[4], ' ')} │ {chess_pieces.get(row[3], ' ')} │ {chess_pieces.get(row[2], ' ')} │ {chess_pieces.get(row[1], ' ')} │ {chess_pieces.get(row[0], ' ')} ║")  # flip row contents
        if i < 7:
            print("  ╟───┼───┼───┼───┼───┼───┼───┼───╢")
    print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝")


def play_game():
    draw_board(board)
    while not board.is_game_over():
        for player in ['White', 'Black']:
            print(f"{player}'s turn")
            if player == 'White':
                while True:
                    # Input a move
                    move = input("Enter your move (e.g. 'e2e4'): ")
                    try:
                        board.push_san(move)
                        break  # valid move entered, break out of loop
                    except ValueError:
                        print("Invalid move, try again")
            else:
                if len(list(board.legal_moves)) == 0:  # Check if there are any legal moves left
                    break
                legal_moves = list(board.legal_moves)
                # AI chooses a random legal move
                move = random.choice(legal_moves)
                time.sleep(0.5)
                print(f"AI chose move {move}")
                board.push(move)
            draw_board(board)

    # Show the final result
    if board.is_checkmate():
        print('''
         𝘊 𝘏 𝘌 𝘊 𝘒 𝘔 𝘈 𝘛 𝘌 !!
        ''')
    elif board.is_stalemate():
        print('''
         𝘚 𝘛 𝘈 𝘓 𝘌 𝘔 𝘈 𝘛 𝘌 !!
        ''')
    else:
        print("The game ended in a draw.")

    restart()


def restart():
    while True:
        restart = input("Would you like to play again? (y/n): ")
        if restart in ['y', 'Y', 'yes']:
            board = chess.Board()
            game_restart = True
            break
        elif restart in ['n', 'N', 'no']:
            game_restart = False
            break
        else:
            print("Invalid input, Try again.")
            continue
    if game_restart:
        play_game()


play_game()
