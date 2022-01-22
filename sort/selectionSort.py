

def selectionSort(arr):
    for i in range(0, len(arr)):
        lastIndex = len(arr)-1-i
        maxIndex = getMaxIndex(arr, 0, lastIndex)

        arr[maxIndex], arr[lastIndex] = arr[lastIndex], arr[maxIndex]


def getMaxIndex(arr, start, end):
    max = start
    for i in range(start, end):
        if arr[max] < arr[i]:
            max = i
    return max


arr = [5, 6, 7, 8, 9, 1, 2, 3]
selectionSort(arr)
print(arr)
