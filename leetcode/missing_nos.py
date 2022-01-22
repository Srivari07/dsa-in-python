'''
https://leetcode.com/problems/missing-number/
'''


def missingNumber(arr):
    i = 0
    while i < len(arr):
        correct = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    for index in range(0, len(arr)):
        if (arr[index] != index):
            return index

    return len(arr)


arr = [4, 0, 2, 1]
print(missingNumber(arr))
