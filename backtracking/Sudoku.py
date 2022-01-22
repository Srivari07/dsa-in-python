

def solveSudoku(board):
    n = len(board)
    row, col = -1, -1

    # this is how we replace r,c from arguments
    emptyLeft = True
    for i in range(0, n):
        for j in range(0, n):
            if board[i][j] == 0:    # found empty cell
                row = i
                col = j
                emptyLeft = False
                break
            # if you found some empty element in row, then break
        if emptyLeft == False:
            break
    # if no empty found
    if emptyLeft == True:
        return True
    # sudoku is solved

    # backtracking
    for number in range(1, 10):
        if isSafe(board, row, col, number):
            board[row][col] = number
            if solveSudoku(board):
                # found number
                return True

            else:
                # backtracking
                board[row][col] = 0

    return False


def isSafe(board, row, col, num):
    # check row
    for i in range(0, len(board)):
        if board[row][i] == num:
            return False
    # check col
    for i in range(0, len(board)):
        if board[i][col] == num:
            return False

    # check grid
    sqrt = round(len(board)**(1/2))
    rowStart = row - row % sqrt
    colStart = col - col % sqrt

    for r in range(rowStart, rowStart+sqrt):
        for c in range(colStart, colStart+sqrt):
            if board[r][c] == num:
                return False

    return True


def display(board):
    for row in board:
        for num in row:
            print(num, end=" ")
        print()


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if solveSudoku(board):
    display(board)
else:
    print("Cannot Solved")


"""
Time Complexity:
    Total 9 number.
    For every n^2 times
    T(n)=O(9^n^2)

Space Complexity:
    O(n^2)
"""
