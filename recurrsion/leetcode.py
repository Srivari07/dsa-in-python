l = [1, 2, 3]
t = 3


def fun(l, t):
    res = []
    l.sort()
    funHelper(l, t, 0, [], res)
    return res


def funHelper(arr, target, index, path, res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(arr)):
        funHelper(arr, target-arr[i], i, path+[arr[i]], res)


# print(fun(l, t))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"


def fun(board, word):
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if funHelper(board, i, j, word):
                return True
    return False


def funHelper(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    temp = board[i][j]
    board[i][j] = "*"
    res = funHelper(board, i+1, j, word[1:]) or funHelper(board, i, j+1, word[1:]) or funHelper(
        board, i-1, j, word[1:]) or funHelper(board, i, j-1, word[1:])

    board[i][j] = temp
    return res


print(fun(board=board, word=word))
