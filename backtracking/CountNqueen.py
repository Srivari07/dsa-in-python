

'''
https://leetcode.com/problems/n-queens-ii/
'''


def totalNQueens(n):
    row = 0
    col = 0
    board = [[0]*n for _ in range(n)]
    return queens(board, row, col)


def queens(board, row, col):
    if row == len(board):
        return 1

    count = 0
    for col in range(0, len(board)):
        # place queen if it is safe
        if isSafe(board, row, col):
            board[row][col] = True
            count += queens(board, row+1, 0)
            board[row][col] = False
    return count


def isSafe(board, row, col):
    # check vertical row
    for i in range(0, row):
        if board[i][col]:
            return False

    # check diagonal left
    maxLeft = min(row, col)
    for i in range(0, maxLeft+1):
        if board[row-i][col-i]:
            return False

    # check diagonal right
    maxRight = min(row, len(board)-col-1)
    for i in range(0, maxRight+1):
        if board[row-i][col+i]:
            return False

    return True


print(totalNQueens(5))
