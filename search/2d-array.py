

arr = [[11, 12, 5, 2],
       [15, 6, 10, 0],
       [10, 8, 12, 5],
       [12, 15, 8, 6]]
t = 8


def fun(arr, t):
    for row in range(0, len(arr)-1):
        for col in range(0, row):
            if arr[row][col] == t:
                return [row, col]
    return -1


def maxfun(arr):
    maxValue = arr[0][0]
    for row in range(0, len(arr)-1):
        for col in range(0, row):
            if arr[row][col] > maxValue:
                maxValue = arr[row][col]
    return maxValue


print(maxfun(arr))
