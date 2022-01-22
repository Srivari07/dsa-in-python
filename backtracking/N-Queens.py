''' The Space Complexity=O(N x N)
    The Time Complexity=O(N!)
'''
# board = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]


def queens(board, row, col):
    if row == len(board):
        display(board)
        print()
        return 1

    # placing the queen and checking every row and col
    count = 0
    for col in range(0, len(board)):
        # place queen if it is safe
        if isSafe(board, row, col):
            board[row][col] = True
            count += queens(board, row+1, col)
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
    maxRight = min(row, (len(board)-col-1))
    for i in range(0, maxRight+1):
        if board[row-i][col+i]:
            return False

    return True


def display(board):
    for row in board:
        for element in row:
            if element:
                print("Q ", end="")
            else:
                print("X ", end="")
        print()


N = 4
board = [[0]*N for _ in range(N)]

print(queens(board, 0, 0))
