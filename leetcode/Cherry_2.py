from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def isSafe(row, col1, col2):
            if col1 < 0 or col1 >= row or col2 < 0 or col2 >= row:
                    return -inf
                # current cell
                result = 0
                result += grid[row][col1]
                if col1 != col2:
                    result += grid[row][col2]
                # transition
                if row != col-1:
                    result += max(isSafe(row+1, new_col1, new_col2)
                                for new_col1 in [col1, col1+1, col1-1]
                                for new_col2 in [col2, col2+1, col2-1])
                return result
        return isSafe(0,0,col-1)