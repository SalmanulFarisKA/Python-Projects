chess_pieces = {'R': '♖',
                'N': '♘',
                'B': '♗',
                'K': '♔',
                'Q': '♕',
                'P': '♙',
                'r': '♜',
                'n': '♞',
                'b': '♝',
                'k': '♚',
                'q': '♛',
                'p': '♟︎'}

board = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
]


def draw_board(board):
    print("    A   B   C   D   E   F   G   H")
    print("  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
    for i, row in enumerate(board):
        print(f"{8-i} ║ {chess_pieces.get(row[0], ' ')} │ {chess_pieces.get(row[1], ' ')} │ {chess_pieces.get(row[2], ' ')} │ {chess_pieces.get(row[3], ' ')} │ {chess_pieces.get(row[4], ' ')} │ {chess_pieces.get(row[5], ' ')} │ {chess_pieces.get(row[6], ' ')} │ {chess_pieces.get(row[7], ' ')} ║")
        if i < 7:
            print("  ╟───┼───┼───┼───┼───┼───┼───┼───╢")
    print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝")


draw_board(board)


def get_move():
    move = input("Enter your move (e.g. 'E2 E4'): ")
    return move.split()


def make_move(board, move):
    start, end = move
    start_x, start_y = ord(start[0]) - ord('A'), 8 - int(start[1])
    end_x, end_y = ord(end[0]) - ord('A'), 8 - int(end[1])
    board[end_y][end_x] = board[start_y][start_x]
    board[start_y][start_x] = ' '


def play_game():
    draw_board(board)
    while True:
        for player in ['White', 'Black']:
            print(f"{player}'s turn")
            move = get_move()
            make_move(board, move)
            draw_board(board)


play_game()
