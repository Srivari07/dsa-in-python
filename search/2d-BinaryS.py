

# sorted matrix

def binarySearch(matrix, row, cStart, cEnd, target):
    while cStart <= cEnd:
        mid = cStart+(cEnd-cStart)//2
        if matrix[row][mid] == target:
            return [row, mid]
        if matrix[row][mid] < target:
            cStart = mid+1
        else:
            cEnd = mid-1
    return [-1, -1]


def search(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 1:
        return binarySearch(matrix, 0, 0, cols-1, target)
    rStart = 0
    rEnd = rows-1
    cMid = cols//2
    while (rStart < (rEnd-1)):
        mid = rStart+(rEnd-rStart)//2
        if matrix[mid][cMid] == target:
            return [mid, cMid]

        if matrix[mid][cMid] < target:
            rStart = mid
        else:
            rEnd = mid

        if matrix[rStart][cMid] == target:
            return[rStart, cMid]

        if matrix[rStart+1][cMid] == target:
            return[rStart+1, cMid]
