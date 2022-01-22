

# https://leetcode.com/problems/first-missing-positive/

def firstMissingPositive(arr):
    i = 0
    while i < len(arr):
        correct = arr[i]-1
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

    for j in range(0, len(arr)):
        if arr[j] != j+1:
            return j+1

    return len(arr)+1


arr = [7, 8, 9, 11, 12]
firstMissingPositive(arr)
print(arr)
print(firstMissingPositive(arr))
