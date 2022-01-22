

# https://leetcode.com/problems/set-mismatch/

def findErrorNums(arr):
    i = 0
    while i < len(arr):
        correct = arr[i]-1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

    res = []
    for j in range(0, len(arr)):
        if arr[j] != j+1:
            res.append(arr[j])
            res.append(j+1)
    return res


arr = [1, 2, 2, 4]
print(findErrorNums(arr))
print(arr)
