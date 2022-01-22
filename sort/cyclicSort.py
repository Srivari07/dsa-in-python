
def cyclicSort(arr):
    i = 0
    while i < len(arr):
        correct = arr[i]-1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1


arr = [3, 5, 2, 1, 4]
cyclicSort(arr)
print(arr)
