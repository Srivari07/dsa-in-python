

'''
https://www.youtube.com/watch?v=lsOOs5J8ycw&list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&index=18&ab_channel=KunalKushwaha
'''


def pattern1(n):
    for row in range(0, n):
        for col in range(0, row+1):
            print("* ", end="")
        print()


def pattern2(n):
    for i in range(0, n):
        for j in range(n):
            print("* ", end="")
        print()


def pattern3(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print("* ", end="")
        print()


def pattern4(n):
    for i in range(1, n):
        for j in range(1, i+1):
            print(f"{j} ", end="")
        print()


def pattern5(n):
    for row in range(0, n):
        for col in range(0, row+1):
            print("* ", end="")
        print()

    for row in range(row+1, 0, -1):
        for col in range(0, row-1):
            print("* ", end="")
        print()


def pattern6(n):
    spaces = 2*n-2
    for i in range(0, n):

        for s in range(0, spaces):
            print(end=" ")
        spaces = spaces-1

        for j in range(0, i+1):
            print("* ", end="")
        print()

    spaces = n-2
    for i in range(n, -1, -1):
        for s in range(spaces, 0, -1):
            print(end=" ")
        spaces += 1
        for j in range(0, i+1):
            print("* ", end="")
        print()


def pattern7(n):
    ogN = n
    n = 2*n
    for i in range(1, n):
        for j in range(1, n):
            atEveryIndex = ogN-min(min(i, j), min(n-i, n-j))
            print(f"{atEveryIndex} ", end="")
        print()


pattern7(5)
