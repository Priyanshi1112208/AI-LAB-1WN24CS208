COMPUTER = 'O'
HUMAN = 'X'

# Check if a player has won
def winner(board, player):
    # Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Check whether the game is over
def terminal(board):
    return winner(board, COMPUTER) or winner(board, HUMAN) or all(
        board[i][j] != '_' for i in range(3) for j in range(3)
    )

# Utility function
def utility(board):
    if winner(board, COMPUTER):
        return 1

    if winner(board, HUMAN):
        return -1

    return 0


# Get all empty positions
def actions(board):
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                moves.append((i, j))

    return moves


# MAX-VALUE
def max_value(board):
    if terminal(board):
        return utility(board)

    value = -float('inf')

    for i, j in actions(board):
        board[i][j] = COMPUTER
        value = max(value, min_value(board))
        board[i][j] = '_'

    return value


# MIN-VALUE
def min_value(board):
    if terminal(board):
        return utility(board)

    value = float('inf')

    for i, j in actions(board):
        board[i][j] = HUMAN
        value = min(value, max_value(board))
        board[i][j] = '_'

    return value


# MINIMAX-DECISION
def minimax(board):
    best_value = -float('inf')
    best_move = None

    for i, j in actions(board):
        board[i][j] = COMPUTER

        value = min_value(board)

        board[i][j] = '_'

        if value > best_value:
            best_value = value
            best_move = (i, j)

    return best_move


# Print the board
def print_board(board):
    for row in board:
        print(' '.join(row))


# -------------------------
# INPUT
# -------------------------

board = []

for _ in range(3):
    board.append(input().split())

# Find the best move
move = minimax(board)

if move is not None:
    i, j = move
    board[i][j] = COMPUTER

    print("Computer places O in position", (i + 1, j + 1))
    print_board(board)

    if winner(board, COMPUTER):
        print("Computer Wins")

    elif not actions(board):
        print("Game Draw")

    else:
        print("Human's winning move is blocked.")
