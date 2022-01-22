mazeBoard = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
mazePath = [len(mazeBoard)][len(mazeBoard[0])]


def funAllPath(p, maze, row, col, path, step):
    if row == len(maze)-1 and col == len(maze[0])-1:
        for i in path:
            print(i)
        print(p)
        print()
        return

    if maze[row][col] == False:
        return

    maze[row][col] = False
    path[row][col] = step
    if row < len(maze)-1:
        funAllPath(p+"D", maze, row+1, col, path, step+1)
    if col < len(maze[0])-1:
        funAllPath(p+"R", maze, row, col+1, path, step+1)
    if row > 0:
        funAllPath(p+"U", maze, row-1, col, path, step+1)
    if col > 0:
        funAllPath(p+"L", maze, row, col-1, path, step+1)
    maze[row][col] = 0


print(funAllPath(p="", maze=mazeBoard, row=0, col=0, path=mazePath, step=1))
