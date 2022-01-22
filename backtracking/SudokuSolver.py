
'''
https://leetcode.com/problems/sudoku-solver/
'''


class Solution:
    def solveSudoku(self, board):
        n = len(board)
        row, col = -1, -1

        # this is how we replace r,c from arguments
        emptyLeft = True
        for i in range(0, n):
            for j in range(0, n):
                if board[i][j] == ".":    # found empty cell
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
            if self.isSafe(board, row, col, number):
                board[row][col] = str(number)
                if self.solveSudoku(board):
                    # found number
                    return True

                else:
                    # backtracking
                    board[row][col] = "."

        return False

    def isSafe(self, board, row, col, num):
        # check row
        for i in range(0, len(board)):
            if board[row][i] == str(num):
                return False
        # check col
        for i in range(0, len(board)):
            if board[i][col] == str(num):
                return False

        # check grid
        sqrt = round(len(board)**(1/2))
        rowStart = row - row % sqrt
        colStart = col - col % sqrt

        for r in range(rowStart, rowStart+sqrt):
            for c in range(colStart, colStart+sqrt):
                if board[r][c] == str(num):
                    return False

        return True

    def display(self, board):
        for row in board:
            for num in row:
                print(num, end=" ")
            print()

    def main(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        if self.solveSudoku(board):
            self.display(board)
        else:
            print("Cannot Solved")


SS = Solution()
SS.main()
