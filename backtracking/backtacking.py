# going all path i.e up,down,left,right
'''
make a change and then reverse that change.

when a choice can affect future answer, use backtracking.
'''
mazeBoard = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]


def funAllPath(p, maze, row, col):
    if row == len(maze)-1 and col == len(maze[0])-1:
        print(p)
        return

    if maze[row][col] == False:
        return
    # this is the block of my path
    maze[row][col] = False

    if row < len(maze)-1:
        funAllPath(p+"D", maze, row+1, col)
    if col < len(maze[0])-1:
        funAllPath(p+"R", maze, row, col+1)
    if row > 0:
        funAllPath(p+"U", maze, row-1, col)
    if col > 0:
        funAllPath(p+"L", maze, row, col-1)
    # this line is where function will be over
    # so before the function gets removed, also remove the changes that where made by the function
    maze[row][col] = True


print(funAllPath(p="", maze=mazeBoard, row=0, col=0))
