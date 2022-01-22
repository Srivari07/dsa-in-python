

def bubbleSort(arr):
    for i in range(0, len(arr)):
        swap = False
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swap = True
    # if you didnt swap for particular value of i, it means array is sorted,hence stop
        if not swap:  # not false=true
            break


arr = [3, 5, 2, 1, 4]
# arr = [1, 2, 3, 4, 5]
bubbleSort(arr)
print(arr)
