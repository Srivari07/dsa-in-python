

arr = [1, 2, 3, 4, 5, 8, 6, 7]


def Sorted(arr, i):
    if i == len(arr)-1:
        return True

    return arr[i] < arr[i+1] and Sorted(arr, i+1)


print(Sorted(arr, 0))
