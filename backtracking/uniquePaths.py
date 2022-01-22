

'''
https://leetcode.com/problems/unique-paths/
'''


def uniquePaths(row, col):
    if row == 1 or col == 1:
        return 1
    left = uniquePaths(row-1, col)
    right = uniquePaths(row, col-1)
    return left+right


print(uniquePaths(23, 12))
ans = 193536720
