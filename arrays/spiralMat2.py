from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    matrix = [[0]*n]*n
    number = 1
    if n == 0:
        return matrix
    row_begin = 0
    col_begin = 0
    row_end = len(matrix)-1
    col_end = len(matrix[0])-1
    while (row_begin <= row_end and col_begin <= col_end):
        for i in range(col_begin, col_end+1):
            (matrix[row_begin][i]) == number
            number += 1
        row_begin += 1
        for i in range(row_begin, row_end+1):
            (matrix[i][col_end]) == number
            number += 1
        col_end -= 1
        if (row_begin <= row_end):
            for i in range(col_end, col_begin-1, -1):
                (matrix[row_end][i]) == number
                number += 1
            row_end -= 1
        if (col_begin <= col_end):
            for i in range(row_end, row_begin-1, -1):
                (matrix[i][col_begin]) == number
                number += 1
            col_begin += 1
    return matrix


print(generateMatrix(3))
