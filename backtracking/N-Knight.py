

def knight(board, row, col, knights):
    if knights == 0:
        display(board)
        print()
        return

    if row == len(board)-1 and col == len(board):
        return

    if col == len(board):
        knight(board, row+1, 0, knights)
        return

    if isSafe(board, row, col):
        board[row][col] = False
        knight(board, row, col+1, 0)
        board[row][col] = True

    knight(board, row, col+1, knights)


def isSafe(board, row, col):
    if isValid(board, row-2, col-1):
        if board[row-2][col-1]:
            return False

    if isValid(board, row-2, col+1):
        if board[row-2][col+1]:
            return False

    if isValid(board, row-1, col+2):
        if board[row-1][col+2]:
            return False

    if isValid(board, row-1, col-2):
        if board[row-1][col-2]:
            return False

    return True

# do not repeat yourself, hence created this function


def isValid(board, row, col):
    if row >= 0 and row < len(board) and col >= 0 and col < len(board):
        return True
    return False


def display(board):
    for row in board:
        for element in row:
            if element:
                print("K ", end="")
            else:
                print("X ", end="")
        print()


N = 4
board = [[0]*N for _ in range(N)]
print(knight(board, 0, 0, 4))
