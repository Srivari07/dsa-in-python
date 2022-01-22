

def bubbleSort(arr, r, c):
    if r == 0:
        return

    if c < r:
        if (arr[c] > arr[c+1]):
            arr[c], arr[c+1] = arr[c+1], arr[c]
        bubbleSort(arr, r, c+1)
    else:
        bubbleSort(arr, r-1, 0)


arr = [3, 5, 2, 1, 4]
bubbleSort(arr, len(arr)-1, 0)
print(arr)
