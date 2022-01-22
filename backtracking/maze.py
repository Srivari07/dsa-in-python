'''
you can go down and right
'''

# count the no. of ways


def funCount(row, col):
    if row == 1 or col == 1:
        return 1
    left = funCount(row-1, col)
    right = funCount(row, col-1)
    return left+right

# print(funCount(row=3, col=3))


# print all no. of ways
def funWays(p, row, col):
    if row == 1 and col == 1:
        print(p)
        return
    if row > 1:
        funWays(p+"D", row-1, col)
    if col > 1:
        funWays(p+"R", row, col-1)

# print(funWays(p="", row=3, col=3))

# using array


def funWaysArray(p, row, col):

    if row == 1 and col == 1:
        list = []
        list.append(p)
        return list

    list = []
    if row > 1:
        list.append(funWaysArray(p+"D", row-1, col))

    if col > 1:
        list.append(funWaysArray(p+"R", row, col-1))
    return list


# print(funWaysArray(p="", row=3, col=3))

# now going diagonal

def funWaysDiagonal(p, row, col):
    if row == 1 and col == 1:
        print(p, end=" ")
        return
    if row > 1 and col > 1:
        funWaysDiagonal(p+"D", row-1, col-1)
    if row > 1:
        funWaysDiagonal(p+"V", row-1, col)
    if col > 1:
        funWaysDiagonal(p+"H", row, col-1)


# print(funWaysDiagonal(p="", row=3, col=3))

# maze with obstacles
mazeBoard = [
    ["Start", True, True],
    [True, False, True],
    [True, True, "End"]
]


def funWaysWithObstacles(p, maze, row, col):
    if row == len(maze)-1 and col == len(maze[0])-1:
        print(p)
        return
    if maze[row][col] == False:
        return
    if row < len(maze)-1:
        funWaysWithObstacles(p+"D", maze, row+1, col)
    if col < len(maze[0])-1:
        funWaysWithObstacles(p+"R", maze, row, col+1)


# print(funWaysWithObstacles(p="", maze=mazeBoard, row=0, col=0))
