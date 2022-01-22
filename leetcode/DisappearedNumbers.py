

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


def findDisappearedNumbers(arr):
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
            res.append(j+1)
    return res


arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(arr))
print(arr)
