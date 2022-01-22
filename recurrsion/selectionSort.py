

def selectionSort(arr, r, c, max):
    if r == 0:
        return

    if c < r:
        if (arr[c] > arr[max]):
            selectionSort(arr, r, c+1, c)
        else:
            selectionSort(arr, r, c+1, max)

    else:
        arr[max], arr[r-1] = arr[r-1], arr[max]
        selectionSort(arr, r-1, 0, 0)


arr = [3, 5, 2, 1, 4]
selectionSort(arr, len(arr), 0, 0)
print(arr)
