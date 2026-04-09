import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3:(i+1)*3])

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i, j, k in wins:
        if b[i] == b[j] == b[k] and b[i] != " ":
            return b[i]
    if " " not in b:
        return "Draw"
    return None

def minimax(b, depth, is_max, alpha, beta):
    result = check_winner(b)
    if result == "X":
        return -1
    if result == "O":
        return 1
    if result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = minimax(b, depth+1, False, alpha, beta)
                b[i] = " "
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = minimax(b, depth+1, True, alpha, beta)
                b[i] = " "
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if move_val > best_val:
                move = i
                best_val = move_val
    return move

def play():
    while True:
        print_board()
        pos = int(input("Enter position (0-8): "))
        if board[pos] != " ":
            continue
        board[pos] = "X"
        if check_winner(board):
            break
        ai = best_move()
        board[ai] = "O"
        if check_winner(board):
            break

    print_board()
    print("Result:", check_winner(board))

play()