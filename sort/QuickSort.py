
def quickSort(arr, low, high):
    if low >= high:
        return

    s = low
    e = high
    m = s+(e-s)//2
    pivot = arr[m]
    while s <= e:
        # if it is already sorted it will not swap
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    quickSort(arr, low, e)
    quickSort(arr, s, high)


arr = [5, 6, 7, 8, 9, 1, 2, 3]
arr.sort()
quickSort(arr, 0, len(arr)-1)
print(arr)
