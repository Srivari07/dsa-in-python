

def binarySearch(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:

        mid = start+(end-start)//2

        if target == arr[mid]:
            return mid

        if target > arr[mid]:
            start = mid+1
        else:
            end = mid-1

    return -1


arr = [3, 4, 5, 6, 7, 8, 9]
target = 7
print(binarySearch(arr, target))


# there is Order-Agnostic Binary Search, see in notes or yt.
