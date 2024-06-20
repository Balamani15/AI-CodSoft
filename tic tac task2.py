import math

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

def is_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_empty_positions(board):
    empty_positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                empty_positions.append((i, j))
    return empty_positions

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_empty_positions(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_empty_positions(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_empty_positions(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    
    human_turn = True
    while True:
        print_board(board)
        if is_winner(board, 'O'):
            print("AI wins!")
            break
        if is_winner(board, 'X'):
            print("Human wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        if human_turn:
            while True:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter col (0, 1, or 2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    human_turn = False
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            print("AI is making a move...")
            move = best_move(board)
            board[move[0]][move[1]] = 'O'
            human_turn = True

if _name_ == "_main_":
    main()