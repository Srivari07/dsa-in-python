

def search(matrix, target):
    r = 0
    c = len(matrix)-1

    while r < len(matrix)-1 and c >= 0:
        if matrix[r][c] == target:
            return [r, c]

        if matrix[r][c] < target:
            r += 1
        else:
            c -= 1
    return [-1, -1]


matrix = [[10, 20, 30, 40],
          [15, 25, 35, 45],
          [28, 29, 37, 49],
          [33, 34, 38, 37]]
target = 0

print(search(matrix, target))
